import json
import os
import onnx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import StringTensorType
import numpy as np

def train_and_export(data_file: str):
    """
    Trains multiple Logistic Regression models to extract specific entities/parameters 
    (like status filters, date targets, and bill flags) from natural language queries.
    Exports each trained model to the ONNX format for fast local inference.
    """
    print(f"Loading data from {data_file}...")
    
    # 1. Data Loading
    with open(data_file, 'r', encoding='utf-8') as f:
        dataset = json.load(f)

    # Filter out UNKNOWN intents so the models only learn from valid queries
    dataset = [q for q in dataset if q.get('intent', q.get('expected_intent')) != 'UNKNOWN']

    # Initialize lists to hold the text inputs and corresponding labels for each parameter
    queries = []
    status_labels = []
    date_target_labels = []
    is_bill_labels = []

    # 2. Label Extraction
    for item in dataset:
        queries.append(item['query'].lower())
        entities = item.get('expected_entities', {})
        
        # Extract status_filter (e.g., 'pending', 'cleared'). 
        # Default to 'None' string to avoid actual Python None types crashing scikit-learn
        status = entities.get('status_filter')
        status_labels.append(status if status else 'None')

        # Extract date_target (e.g., 'bill_date', 'due_date')
        dt = entities.get('date_target')
        date_target_labels.append(dt if dt else 'None')

        # Extract boolean is_bill_query flag (converted to string for classification)
        ib = entities.get('is_bill_query')
        is_bill_labels.append(str(ib))

    print(f"Total valid queries: {len(queries)}")

    # Ensure the models directory exists in the project root
    models_dir = os.path.join(os.path.dirname(__file__), 'models')
    os.makedirs(models_dir, exist_ok=True)

    def train_model(name, X, y):
        """
        Helper function to train a single TF-IDF + Logistic Regression pipeline 
        and export it to an ONNX file.
        """
        print(f"\nTraining {name}...")
        unique_labels = list(set(y))
        print(f"Classes: {unique_labels}")
        
        # If there's only one class (e.g., all queries resolve to 'None'), 
        # a classifier cannot be trained, so we skip gracefully.
        if len(unique_labels) < 2:
            print(f"Skipping {name}, not enough classes.")
            return

        # Define the machine learning pipeline:
        # 1. TfidfVectorizer: Extracts unigrams and bigrams, alphanumeric only.
        # 2. LogisticRegression: Uses class_weight='balanced' because some parameters 
        #    (like specific date targets) appear very rarely compared to 'None'.
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=(1, 2), max_features=3000, token_pattern=r"[a-zA-Z0-9]+")),
            ('clf', LogisticRegression(C=50.0, class_weight='balanced', max_iter=500))
        ])

        # Train the model on the full dataset
        pipeline.fit(X, y)
        
        # Evaluate on the training set to ensure the model memorized/learned the patterns
        acc = pipeline.score(X, y)
        print(f"Training Accuracy: {acc:.4f}")

        # 3. ONNX Conversion
        # Define the input type as a batch of strings
        initial_type = [('string_input', StringTensorType([None, 1]))]
        
        # Convert to ONNX format. zipmap=False is used for performance optimization 
        # (returns raw probability arrays instead of dictionaries)
        onx = convert_sklearn(pipeline, initial_types=initial_type, 
                              options={id(pipeline): {'zipmap': False}})
        
        # Save the resulting binary protobuf file
        onnx_path = os.path.join(models_dir, f'{name}_model.onnx')
        with open(onnx_path, "wb") as f:
            f.write(onx.SerializeToString())
        
        print(f"Saved {name} to {onnx_path} (Size: {os.path.getsize(onnx_path)/1024:.2f} KB)")

    # Execute the training pipeline for each distinct parameter model
    train_model("status_filter", queries, status_labels)
    train_model("date_target", queries, date_target_labels)
    train_model("is_bill_query", queries, is_bill_labels)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="training_data.json")
    args = parser.parse_args()
    train_and_export(args.data)
