import re

def apply_changes():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Init ONNX Models
    init_target = """            self.tokenizer = Tokenizer.from_file(tokenizer_path)
            self.session = ort.InferenceSession(model_path)
            
            self.INTENT_BENCHMARKS = {"""
            
    init_replacement = """            self.tokenizer = Tokenizer.from_file(tokenizer_path)
            self.session = ort.InferenceSession(model_path)
            
            # Parameter Extractors
            param_models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
            self.status_session = None
            self.date_target_session = None
            self.is_bill_session = None
            try:
                self.status_session = ort.InferenceSession(os.path.join(param_models_dir, 'status_filter_model.onnx'))
                self.date_target_session = ort.InferenceSession(os.path.join(param_models_dir, 'date_target_model.onnx'))
                self.is_bill_session = ort.InferenceSession(os.path.join(param_models_dir, 'is_bill_query_model.onnx'))
            except Exception as e:
                print(f"Warning: Param ONNX models not found ({e}). Falling back to regex.")
            
            self.INTENT_BENCHMARKS = {"""
    content = content.replace(init_target, init_replacement)
    
    # 2. Predict helper
    predict_target = """    def extract_parameters(self, query: str) -> dict:"""
    predict_replacement = """    def predict_param(self, session, text: str):
        if not session:
            return None, 0.0
        try:
            inputs = {'string_input': np.array([[text]], dtype=object)}
            label, probs = session.run(None, inputs)
            predicted = label[0]
            confidence = float(np.max(probs[0]))
            
            if predicted == 'None':
                predicted = None
            elif predicted == 'True':
                predicted = True
            elif predicted == 'False':
                predicted = False
                
            return predicted, confidence
        except Exception as e:
            print(f"Error predicting param: {e}")
            return None, 0.0

    def extract_parameters(self, query: str) -> dict:"""
    content = content.replace(predict_target, predict_replacement)
    
    # 3. Status Filter ML Logic
    status_target = """        # Binary flags & simple keyword limits
        is_cleared = bool(re.search(r'\\b(cleared|settled)\\b', q_lower) or re.search(r'(?<!not )(?<!to be )\\bpaid\\b', q_lower))
        if is_cleared and bool(re.search(r'\\b(pending|due|dues|outstanding|unpaid|overdue)\\s+(?:and|or|as well as|also)\\s+(?:cleared|settled|paid)\\b', q_lower)) or bool(re.search(r'\\b(?:cleared|settled|paid)\\s+(?:and|or|as well as|also)\\s+(pending|due|dues|outstanding|unpaid|overdue)\\b', q_lower)):
            params["status_filter"] = None # mixed query
        elif is_cleared:
            params["status_filter"] = "cleared"
        elif any(w in q_lower for w in ["pending", "overdue", "unpaid", "not paid"]):
            if "settled" in q_lower or "cleared" in q_lower:
                params["status_filter"] = None
            else:
                params["status_filter"] = "pending"
                
        # If explicitly asking for a single bill's details, status doesn't matter
        if params.get("document_ref") and "overdue" not in q_lower:
            params["status_filter"] = None"""
            
    status_replacement = """        # ML Inference for Semantic Parameters
        ml_status, status_conf = self.predict_param(self.status_session, query)
        ml_date_tgt, date_tgt_conf = self.predict_param(self.date_target_session, query)
        ml_is_bill, is_bill_conf = self.predict_param(self.is_bill_session, query)
        
        use_ml_status = status_conf > 0.80
        use_ml_date_tgt = date_tgt_conf > 0.80
        use_ml_is_bill = is_bill_conf > 0.80

        if use_ml_is_bill:
            params["is_bill_query"] = ml_is_bill

        # Binary flags & simple keyword limits
        if use_ml_status:
            params["status_filter"] = ml_status
        else:
            is_cleared = bool(re.search(r'\\b(cleared|settled)\\b', q_lower) or re.search(r'(?<!not )(?<!to be )\\bpaid\\b', q_lower))
            if is_cleared and bool(re.search(r'\\b(pending|due|dues|outstanding|unpaid|overdue)\\s+(?:and|or|as well as|also)\\s+(?:cleared|settled|paid)\\b', q_lower)) or bool(re.search(r'\\b(?:cleared|settled|paid)\\s+(?:and|or|as well as|also)\\s+(pending|due|dues|outstanding|unpaid|overdue)\\b', q_lower)):
                params["status_filter"] = None # mixed query
            elif is_cleared:
                params["status_filter"] = "cleared"
            elif any(w in q_lower for w in ["pending", "overdue", "unpaid", "not paid"]):
                if "settled" in q_lower or "cleared" in q_lower:
                    params["status_filter"] = None
                else:
                    params["status_filter"] = "pending"
                    
        # If explicitly asking for a single bill's details, status doesn't matter
        if params.get("document_ref") and "overdue" not in q_lower:
            params["status_filter"] = None"""
    content = content.replace(status_target, status_replacement)
    
    # 4. Date Target ML Logic
    date_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable", "paid", "get", "getting", "cash", "received", "receipts"]):
            params["date_target"] = "due_date"
        if "on account" in q_lower or "on-account" in q_lower:
            params["date_target"] = "bill_date"
        # For ledger balances or voucher queries, date_target is irrelevant/None
        if "ledger" in q_lower or "balance" in q_lower or "voucher type" in q_lower:
            if "bill" not in q_lower and "receivable" not in q_lower and "payable" not in q_lower and "on-account" not in q_lower and "on account" not in q_lower:
                params["date_target"] = None
        # Explicit bill details
        if "which ledger is associated" in q_lower or "which voucher type" in q_lower or params.get("document_ref"):
            params["date_target"] = None"""
            
    date_replacement = """        if use_ml_date_tgt:
            params["date_target"] = ml_date_tgt
        else:
            if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable", "paid", "get", "getting", "cash", "received", "receipts"]):
                params["date_target"] = "due_date"
            if "on account" in q_lower or "on-account" in q_lower:
                params["date_target"] = "bill_date"
            # For ledger balances or voucher queries, date_target is irrelevant/None
            if "ledger" in q_lower or "balance" in q_lower or "voucher type" in q_lower:
                if "bill" not in q_lower and "receivable" not in q_lower and "payable" not in q_lower and "on-account" not in q_lower and "on account" not in q_lower:
                    params["date_target"] = None
            # Explicit bill details
            if "which ledger is associated" in q_lower or "which voucher type" in q_lower or params.get("document_ref"):
                params["date_target"] = None"""
    content = content.replace(date_target, date_replacement)
    
    # 5. Is Bill Query ML Logic
    bill_target = """        if "bills" in q_lower or "invoices" in q_lower or "bill amount" in q_lower or "receivable bill" in q_lower or "payable bill" in q_lower or "collections due" in q_lower:
            params["is_bill_query"] = True
        elif bool(re.search(r'\\b(?:oldest|latest|pending|unpaid|highest|lowest|which|overdue date|receivables|payables)\\s+bill\\b', q_lower)) or "bill amount" in q_lower:
            params["is_bill_query"] = True
            
        if params["is_bill_query"] and not params["document_ref"]:
            if bool(re.search(r'\\b(parties|debtors|creditors|payments)\\b', q_lower)):
                if not bool(re.search(r'\\b(list|show|all).*bills\\b', q_lower)) and not bool(re.search(r'oldest.*bill', q_lower)) and "bill amount" not in q_lower:
                    params["is_bill_query"] = False"""
                    
    bill_replacement = """        if not use_ml_is_bill:
            if "bills" in q_lower or "invoices" in q_lower or "bill amount" in q_lower or "receivable bill" in q_lower or "payable bill" in q_lower or "collections due" in q_lower:
                params["is_bill_query"] = True
            elif bool(re.search(r'\\b(?:oldest|latest|pending|unpaid|highest|lowest|which|overdue date|receivables|payables)\\s+bill\\b', q_lower)) or "bill amount" in q_lower:
                params["is_bill_query"] = True
                
            if params["is_bill_query"] and not params["document_ref"]:
                if bool(re.search(r'\\b(parties|debtors|creditors|payments)\\b', q_lower)):
                    if not bool(re.search(r'\\b(list|show|all).*bills\\b', q_lower)) and not bool(re.search(r'oldest.*bill', q_lower)) and "bill amount" not in q_lower:
                        params["is_bill_query"] = False"""
    content = content.replace(bill_target, bill_replacement)

    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done")

if __name__ == '__main__':
    apply_changes()
