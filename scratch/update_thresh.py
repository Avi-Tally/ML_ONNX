import re

def apply_changes():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()
        
    target = """        use_ml_status = status_conf > 0.80
        use_ml_date_tgt = date_tgt_conf > 0.80
        use_ml_is_bill = is_bill_conf > 0.80"""
        
    replacement = """        use_ml_status = status_conf > 0.45
        use_ml_date_tgt = date_tgt_conf > 0.45
        use_ml_is_bill = is_bill_conf > 0.55"""
        
    content = content.replace(target, replacement)

    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done")

if __name__ == '__main__':
    apply_changes()
