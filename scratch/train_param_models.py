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
    print(f"Loading data from {data_file}...")
    with open(data_file, 'r', encoding='utf-8') as f:
        dataset = json.load(f)

    # Filter out UNKNOWN
    dataset = [q for q in dataset if q.get('intent', q.get('expected_intent')) != 'UNKNOWN']

    queries = []
    status_labels = []
    date_target_labels = []
    is_bill_labels = []

    for item in dataset:
        queries.append(item['query'].lower())
        entities = item.get('expected_entities', {})
        
        # Extract status_filter (default to 'None' string to avoid actual None types in scikit)
        status = entities.get('status_filter')
        status_labels.append(status if status else 'None')

        # Extract date_target
        dt = entities.get('date_target')
        date_target_labels.append(dt if dt else 'None')

        # Extract is_bill_query
        ib = entities.get('is_bill_query')
        is_bill_labels.append(str(ib))

    print(f"Total valid queries: {len(queries)}")

    models_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')
    os.makedirs(models_dir, exist_ok=True)

    def train_model(name, X, y):
        print(f"\nTraining {name}...")
        unique_labels = list(set(y))
        print(f"Classes: {unique_labels}")
        
        # If there's only one class (shouldn't happen with full dataset), handle gracefully
        if len(unique_labels) < 2:
            print(f"Skipping {name}, not enough classes.")
            return

        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=(1, 2), max_features=3000, token_pattern=r"[a-zA-Z0-9]+")),
            ('clf', LogisticRegression(C=50.0, class_weight='balanced', max_iter=500))
        ])

        pipeline.fit(X, y)
        
        # Evaluate on training set
        acc = pipeline.score(X, y)
        print(f"Training Accuracy: {acc:.4f}")

        # Convert to ONNX
        initial_type = [('string_input', StringTensorType([None, 1]))]
        onx = convert_sklearn(pipeline, initial_types=initial_type, 
                              options={id(pipeline): {'zipmap': False}})
        
        onnx_path = os.path.join(models_dir, f'{name}_model.onnx')
        with open(onnx_path, "wb") as f:
            f.write(onx.SerializeToString())
        
        print(f"Saved {name} to {onnx_path} (Size: {os.path.getsize(onnx_path)/1024:.2f} KB)")

    train_model("status_filter", queries, status_labels)
    train_model("date_target", queries, date_target_labels)
    train_model("is_bill_query", queries, is_bill_labels)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="../training_data.json")
    args = parser.parse_args()
    train_and_export(args.data)
