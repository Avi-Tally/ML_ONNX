import onnxruntime as ort
import numpy as np

def test_inference():
    sess = ort.InferenceSession('models/status_filter_model.onnx')
    
    # scikit-learn string inputs must be 2D array of objects
    text = "settled bills with overdue amounts"
    inputs = {'string_input': np.array([[text]], dtype=object)}
    
    label, probs = sess.run(None, inputs)
    print(f"Text: {text}")
    print(f"Label: {label[0]}")
    print(f"Probs: {probs[0]}")

if __name__ == "__main__":
    test_inference()
