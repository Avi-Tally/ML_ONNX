import pandas as pd
import json
import sys

# Windows stdout encoding fix
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_excel(r'C:\Users\avija\projects\ML_ONNX\Real_world_queries\482 suite.xlsx')
print(df.head().to_json(orient="records", indent=2))
