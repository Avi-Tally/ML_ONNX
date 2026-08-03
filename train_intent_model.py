import json
import argparse
import os
import onnxruntime as ort
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import StringTensorType
import numpy as np

def train_and_export(data_file):
    """
    Trains a Logistic Regression model on top of TF-IDF vectors to classify user queries 
    into Tally intents, and exports the resulting pipeline to ONNX format for high-performance inference.
    """
    print(f"Loading data from {data_file}...")
    
    # 1. Data Loading and Preprocessing
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    queries = []
    intents = []
    
    # Extract query text and expected intent labels from the JSON dataset
    for item in data:
        q = item.get("query", "").strip()
        i = item.get("expected_intent") or item.get("intent")
        
        # Skip invalid or empty entries
        if not q or not i: continue
        
        queries.append(q)
        intents.append(i)

    print(f"Total valid queries for intent: {len(queries)}")

    # 2. Pipeline Construction
    # TfidfVectorizer: Converts text to numerical TF-IDF features. 
    #   - ngram_range=(1,2) captures both single words and 2-word phrases.
    #   - token_pattern=r"[a-zA-Z0-9]+" restricts matching to alphanumeric characters.
    # LogisticRegression: Predicts the intent category based on the TF-IDF features.
    #   - C=50.0 is the inverse regularization strength (higher means less regularization).
    #   - solver='lbfgs' is the optimization algorithm used.
    pipeline = make_pipeline(
        TfidfVectorizer(ngram_range=(1, 2), max_features=3000, token_pattern=r"[a-zA-Z0-9]+"),
        LogisticRegression(C=50.0, solver='lbfgs', max_iter=500)
    )
    
    # 3. Model Training
    # Fit the text and labels to the pipeline (trains the vectorizer and regression model)
    pipeline.fit(queries, intents)
    
    # 4. Evaluation
    # Calculate and print basic training accuracy to ensure the model learned the dataset
    preds = pipeline.predict(queries)
    acc = np.mean(preds == intents)
    print(f"Training Accuracy: {acc:.4f}")
    
    # 5. ONNX Export Preparation
    # Define the expected input signature for the ONNX model: 
    # A single string tensor of shape [None, 1] (batch of strings).
    initial_type = [('string_input', StringTensorType([None, 1]))]
    
    # Convert the scikit-learn pipeline into an ONNX graph representation
    # zipmap=False optimizes output by returning a direct array of probabilities instead of a list of dictionaries
    onx = convert_sklearn(pipeline, initial_types=initial_type, 
                          options={id(pipeline): {'zipmap': False}})
                          
    # 6. Save the ONNX Model
    out_dir = "models"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "intent_model.onnx")
    
    # Serialize and write the ONNX graph to a binary file
    with open(out_path, "wb") as f:
        f.write(onx.SerializeToString())
        
    size_kb = os.path.getsize(out_path) / 1024
    print(f"Saved intent model to {out_path} (Size: {size_kb:.2f} KB)")

if __name__ == "__main__":
    # Standard command-line argument parsing for standalone execution
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="training_data.json", help="Path to training data")
    args = parser.parse_args()
    train_and_export(args.data)
