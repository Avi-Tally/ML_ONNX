# Exhaustive Project History & Technical Report (Part 2: The Hybrid ONNX NLP Engine & Entity Extraction Subsystem)

---

## 1. The Machine Learning Engine Architecture (`nlp_engine.py`)

### 1.1 Why ONNX Runtime?
Open Neural Network Exchange (ONNX) is an open format built to represent machine learning models. Instead of loading heavyweight Python libraries like PyTorch or Scikit-Learn in production, models are trained in Python, serialized to `.onnx` protobuf files, and loaded using Microsoft's high-speed C++ `onnxruntime` engine.

In our system, ONNX inference happens in **< 0.5 ms per model** on CPU.

### 1.2 Training & Export Pipeline (`train_27_param_models.py`)
Each classifier is built using a scikit-learn `Pipeline` combining:
1. **TF-IDF Vectorizer (`TfidfVectorizer`):** Converts raw string query into character/word n-gram features (`ngram_range=(1, 2)`).
2. **Logistic Regression (`LogisticRegression`):** Fits a high-dimensional linear decision boundary with $L_2$ regularization (`C=5.0`).

#### Code Implementation for Model Training & Export:
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import StringTensorType

def train_and_export(model_name, X_text, y_labels):
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
        ('clf', LogisticRegression(max_iter=1000, C=5.0))
    ])
    pipeline.fit(X_text, y_labels)
    
    # Define String Input Tensor for ONNX Runtime
    initial_type = [('string_input', StringTensorType([None, 1]))]
    onnx_model = convert_sklearn(pipeline, initial_types=initial_type, target_opset=12)
    
    with open(f"models/{model_name}.onnx", "wb") as f:
        f.write(onnx_model.SerializeToString())
```

---

## 2. Low-Level Details of the 11 Parameter Models & Intent Model

| ONNX Model Name | Target Task / Parameter | Possible Output Classes | Key Feature Triggers |
| :--- | :--- | :--- | :--- |
| **`intent_model.onnx`** | Primary Intent Classification | `GET_RECEIVABLES`, `GET_PAYABLES`, `GET_AGEING`, `GET_LEDGER_BALANCE`, `GET_BILL_DETAILS`, `GET_RECENT_VOUCHERS`, `GET_TOP_DEBTORS`, `GET_TOP_CREDITORS`, `GET_TRIAL_BALANCE`, `GET_STOCK_SUMMARY`, `GET_LEDGER_360`, `GET_COMPARATIVE_SUMMARY`, `AMBIGUOUS_OUTSTANDINGS`, `UNKNOWN` | Keywords like *"ageing"*, *"trial balance"*, *"stock summary"*, *"overdue"*, *"compare"* |
| **`status_filter_model.onnx`** | Invoice Settlement Status | `'None'`, `'pending'`, `'cleared'` | *"unpaid"*, *"overdue"*, *"pending"*, *"settled"*, *"cleared"* |
| **`date_target_model.onnx`** | Target Date Field for Filtering | `'None'`, `'bill_date'`, `'due_date'` | *"due date"*, *"overdue days"*, *"invoice date"*, *"bill date"* |
| **`is_bill_query_model.onnx`** | Bill-Level vs. Ledger-Level | `'True'`, `'False'` | *"bill"*, *"invoices"*, *"ref no"*, *"bill allocations"* |
| **`voucher_type_model.onnx`** | Day Book Voucher Type Filter | `'None'`, `'Sales'`, `'Purchase'`, `'Receipt'`, `'Payment'`, `'Journal'`, `'Contra'` | *"sales invoices"*, *"purchase bills"*, *"payment receipts"*, *"journal entries"* |
| **`tax_filter_model.onnx`** | Tax Component Flag | `'True'`, `'False'` | *"tax amount"*, *"gst portion"*, *"vat"* |
| **`pdc_only_model.onnx`** | Post-Dated Cheque Flag | `'True'`, `'False'` | *"pdc"*, *"post-dated"*, *"future receipts"* |
| **`include_cleared_model.onnx`**| Include Settled Invoices | `'True'`, `'False'` | *"include cleared"*, *"all settled bills"*, *"historical ledger"* |
| **`group_name_model.onnx`** | Tally Account Group Name | `'None'`, `'Expenses'`, `'Sundry Creditors'`, `'Sundry Debtors'`, `'Fixed Assets'`, `'Duties & Taxes'` | *"group expenses"*, *"under group indirect expenses"*, *"creditors group"* |
| **`gst_status_model.onnx`** | GSTR-2A Reconciliation Status | `'None'`, `'reconciled'`, `'unregistered'` | *"gstr 2a"*, *"gstr2a"*, *"unregistered vendor"* |
| **`godown_name_model.onnx`** | Warehouse / Location Filter | `'None'`, `'Bhiwandi Godown'` | *"bhiwandi"*, *"godown"*, *"warehouse"* |

---

## 3. The Ledger Resolution Subsystem (`resolve_ledger`)

Extracting exact party names from freeform user queries (e.g. *"Show me the overdue invoices of Jagat"*) without false positives is one of the hardest challenges in NLP. `nlp_engine.py` implements a multi-tiered resolution algorithm:

```
                      ┌─────────────────────────┐
                      │    Raw User Query       │
                      └────────────┬────────────┘
                                   │
                                   ▼
                      ┌─────────────────────────┐
                      │ Stop-Phrase Stripper    │
                      │ (Strips "show invoices  │
                      │  of", "balance for",    │
                      │  "sales invoices for")  │
                      └────────────┬────────────┘
                                   │
                                   ▼
                      ┌─────────────────────────┐
                      │ TIER 1: Exact Substring │
                      │ Word-Boundary Match     │
                      └────────────┬────────────┘
                                   │
                     (If No Exact Match or Ambiguous)
                                   ▼
                      ┌─────────────────────────┐
                      │ TIER 2: Sliding Window  │
                      │ N-Gram Generator (1-4w) │
                      └────────────┬────────────┘
                                   │
                                   ▼
                      ┌─────────────────────────┐
                      │ RapidFuzz Token Set     │
                      │ Ratio Matcher           │
                      └────────────┬────────────┘
                                   │
                                   ▼
                      ┌─────────────────────────┐
                      │  Ambiguity Interceptor  │
                      │  (If >1 candidate with  │
                      │   score >= 85.0%)       │
                      └─────────────────────────┘
```

### 3.1 Step 1: Stop-Phrase Stripping
Before searching ledger names in the database, `nlp_engine.py` strips out accounting noise words that could corrupt ledger matching:
```python
self.stop_phrases = [
    "what is the balance of", "balance for", "show balance of", "total outstanding",
    "show me the overdue invoices of the", "show me the overdue invoices of", "show me the",
    "show all sales invoices for", "sales invoices for", "purchase invoices for",
    "vendors", "customers", "creditors", "debtors", "parties", "suppliers"
]
```

### 3.2 Step 2: Sliding N-Gram Window Generator
If no exact ledger match is found, the engine splits the query into all candidate n-grams of length 1 to 4 words, filtering out common dictionary words (`the`, `for`, `amount`, `pending`, `balance`):
```python
common = {"what", "is", "the", "balance", "of", "show", "me", "how", "much", "amount", "for", "party", "invoices", "pending", "bill", "due"}

windows = []
for n in range(1, 5):
    for i in range(len(words) - n + 1):
        window = " ".join(words[i:i+n])
        if not all(w in common or w.isdigit() for w in words[i:i+n]):
            if len(window) >= 3:
                windows.append(window)
```

### 3.3 Step 3: RapidFuzz Matcher & Multi-Ledger Ambiguity Interceptor
Each candidate window is scored against all active Tally ledgers using `rapidfuzz.process.extract` with `fuzz.token_set_ratio`.

**The Ambiguity Interceptor Fix:**
If a query contains a generic term like `"Reliance"`, and the Tally database has 80+ matching ledgers (`Reliance Industries Limited`, `RELIANCE NEW SOLAR ENERGY LIMITED`, `Reliance Industries Limited (Guj)`), returning any single ledger is dangerous.

```python
if best_window:
    top_matches = process.extract(best_window, ledger_names_lower, scorer=fuzz.token_set_ratio, limit=5)
    high_score_candidates = [ledger_names[m[2]] for m in top_matches if m[1] >= 85.0]
    
    if len(high_score_candidates) > 1:
        # Halt execution and return Ambiguity Candidates to user!
        return None, best_score, high_score_candidates[:4]
```

---

## 4. Pros and Cons of the Machine Learning Subsystem

### Pros:
1. **Sub-Millisecond Speed:** All 11 ONNX classifiers evaluate in under 1 millisecond combined.
2. **Robustness to Syntax Variations:** TF-IDF n-grams capture fuzzy phrasing (*"how much cash will I get this week"*, *"who hasn't paid us"*) without breaking on novel punctuation.
3. **Ambiguity Prevention:** Explicitly catches ambiguous ledger names (`"Reliance"`) or directionally ambiguous outstandings (`"Show pending bills"`) and asks for user clarification instead of outputting incorrect financial figures.

### Cons:
1. **Model Retraining Overhead:** Adding a brand new parameter requires running `train_27_param_models.py` to regenerate the `.onnx` model files.
2. **Fixed Vocabulary Boundary:** Extremely rare typos not seen during TF-IDF vocabulary construction may fall back to heuristic rule matching.
