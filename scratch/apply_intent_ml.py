import re

def apply_changes():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()
        
    init_target = """            self.is_bill_session = ort.InferenceSession(os.path.join(param_models_dir, 'is_bill_query_model.onnx'))"""
    init_replacement = """            self.is_bill_session = ort.InferenceSession(os.path.join(param_models_dir, 'is_bill_query_model.onnx'))
            self.intent_session = ort.InferenceSession(os.path.join(param_models_dir, 'intent_model.onnx'))"""
    content = content.replace(init_target, init_replacement)
    
    # find predict_intent and replace it
    predict_intent_match = re.search(r'    def predict_intent\(self, query\):.*?    def predict_param\(self, session, text: str\):', content, re.DOTALL)
    
    new_predict_intent = """    def predict_intent(self, query):
        if hasattr(self, 'intent_session') and self.intent_session:
            ml_intent, conf = self.predict_param(self.intent_session, query)
            if ml_intent:
                return ml_intent
        return "GET_LEDGER_BALANCE"

    def predict_param(self, session, text: str):"""
    
    content = content.replace(predict_intent_match.group(0), new_predict_intent)
    
    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done applying intent ML")

if __name__ == '__main__':
    apply_changes()
