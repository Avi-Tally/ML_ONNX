import os

search_paths = [
    "c:/Users/avija/projects/ML_ONNX",
    "C:/Users/avija/.gemini/antigravity/brain/b17f1b4c-0c87-45b9-b9be-fe3b17f6d0d3"
]

print("Searching for files containing 'augmented' or 'training_data':")
for path in search_paths:
    print(f"\nIn: {path}")
    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for f in files:
                if "augmented" in f.lower() or "training_data" in f.lower() or "expected" in f.lower():
                    full_path = os.path.join(root, f)
                    print(f"  {full_path} | Size={os.path.getsize(full_path)} bytes")
