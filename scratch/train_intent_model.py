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
    print(f"Loading data from {data_file}...")
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    queries = []
    intents = []
    
    for item in data:
        q = item.get("query", "").strip()
        i = item.get("expected_intent") or item.get("intent")
        
        if not q or not i: continue
        
        queries.append(q)
        intents.append(i)

    print(f"Total valid queries for intent: {len(queries)}")

    pipeline = make_pipeline(
        TfidfVectorizer(ngram_range=(1, 2), max_features=3000, token_pattern=r"[a-zA-Z0-9]+"),
        LogisticRegression(C=50.0, solver='lbfgs', max_iter=500)
    )
    
    pipeline.fit(queries, intents)
    
    preds = pipeline.predict(queries)
    acc = np.mean(preds == intents)
    print(f"Training Accuracy: {acc:.4f}")
    
    initial_type = [('string_input', StringTensorType([None, 1]))]
    onx = convert_sklearn(pipeline, initial_types=initial_type, 
                          options={id(pipeline): {'zipmap': False}})
                          
    out_dir = "models"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "intent_model.onnx")
    
    with open(out_path, "wb") as f:
        f.write(onx.SerializeToString())
        
    size_kb = os.path.getsize(out_path) / 1024
    print(f"Saved intent model to {out_path} (Size: {size_kb:.2f} KB)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="training_data.json", help="Path to training data")
    args = parser.parse_args()
    train_and_export(args.data)
