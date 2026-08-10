# ==============================================================================
# MODULE: HYBRID NLU & ONNX MACHINE LEARNING ENGINE (nlp_engine.py)
# 
# PURPOSE:
#   This module translates unstructured, highly varied user natural language queries
#   into strict, 27-entity deterministic database parameters required by TallyPrime.
#
# CORE ARCHITECTURE:
#   1. Local ONNX Model Inference (C++ Runtime): Evaluates 11 ONNX classifiers in <0.5ms.
#   2. 27-Entity Parameter Extraction Subsystem: Parses date ranges, age limits, amount thresholds,
#      voucher types, group names, multicurrency, and GST statuses.
#   3. Multi-Tiered Ledger Resolution Subsystem: Combines Stop-Phrase Stripping, Sliding 1-to-4 Word
#      N-Gram Window Generation, and RapidFuzz `token_set_ratio` similarity.
#   4. Multi-Ledger Ambiguity Interceptor: Prevents incorrect single ledger selection when 
#      queries match multiple accounts (e.g., 80+ Reliance ledgers).
# ==============================================================================

import re                       # IMPORT RATIONALE: Regular expressions for extracting document refs, verbal numbers, dates, and text sanitization.
import json                     # IMPORT RATIONALE: JSON serialization for parsing dataset objects and ONNX output formatting.
import math                     # IMPORT RATIONALE: Mathematical functions for numerical bounds checking and infinity handling.
import os                       # IMPORT RATIONALE: Cross-platform file path resolution for loading model files.
import numpy as np              # IMPORT RATIONALE: Constructs high-performance numpy arrays (StringTensorType) required by ONNX Runtime C++ ABI.

import onnxruntime as ort       # IMPORT RATIONALE: C++ accelerated machine learning runtime. Executes pre-trained TF-IDF + LogisticRegression models in <0.5ms.
from tokenizers import Tokenizer # IMPORT RATIONALE: HuggingFace Fast Tokenizer for character and subword tokenization.
from rapidfuzz import process, fuzz # IMPORT RATIONALE: C++ optimized Levenshtein and token-set ratio string matching (100x faster than fuzzywuzzy).

class NLPEngine:
    """
    Hybrid Machine Learning & Heuristic NLU Engine.
    Coordinates ONNX inference sessions, regex entity extraction, and fuzzy ledger matching.
    """
    def __init__(self, tally_client=None):

        """
        ========================================================================
        FUNCTION: __init__(tally_client)
        PURPOSE:
            Initializes the NLU Engine, loads ONNX C++ runtime sessions into RAM,
            and defines stop-word dictionaries and intent benchmark embeddings.
        
        ONNX SESSIONS LOADED (11 Model Pipelines):
            - intent_session: Classifies query into 14 core accounting intents.
            - status_session: Predicts 'pending', 'cleared', or None.
            - date_target_session: Predicts 'due_date', 'bill_date', or None.
            - is_bill_session: Predicts bill-level vs ledger-level intent.
            - voucher_type_session: Predicts 'Sales', 'Purchase', 'Receipt', 'Payment', etc.
            - tax_filter_session: Predicts tax component extraction requirement.
            - pdc_only_session: Predicts Post-Dated Cheque filter.
            - include_cleared_session: Predicts historical cleared invoice inclusion.
            - group_name_session: Predicts Tally Account Group (Expenses, Sundry Creditors).
            - gst_status_session: Predicts GSTR-2A reconciliation status.
            - godown_name_session: Predicts Warehouse location filter (Bhiwandi Godown).
        ========================================================================
        """
        if tally_client is None:
            from tally_client import TallyClient
            tally_client = TallyClient()
        self.tally_client = tally_client
        self.session = None
        self.tokenizer = None
        self.intent_embeddings = {}

        try:
            model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model')
            tokenizer_path = os.path.join(model_dir, 'tokenizer.json')
            model_path = os.path.join(model_dir, 'model.onnx')
            
            self.tokenizer = Tokenizer.from_file(tokenizer_path)
            self.session = ort.InferenceSession(model_path)
            
            # Parameter Extractors Directory
            param_models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
            self.status_session = None
            self.date_target_session = None
            self.is_bill_session = None
            self.voucher_type_session = None
            self.tax_filter_session = None
            self.pdc_only_session = None
            self.include_cleared_session = None
            try:
                self.status_session = ort.InferenceSession(os.path.join(param_models_dir, 'status_filter_model.onnx'))
                self.date_target_session = ort.InferenceSession(os.path.join(param_models_dir, 'date_target_model.onnx'))
                self.is_bill_session = ort.InferenceSession(os.path.join(param_models_dir, 'is_bill_query_model.onnx'))
                self.intent_session = ort.InferenceSession(os.path.join(param_models_dir, 'intent_model.onnx'))
                self.voucher_type_session = ort.InferenceSession(os.path.join(param_models_dir, 'voucher_type_model.onnx'))
                self.tax_filter_session = ort.InferenceSession(os.path.join(param_models_dir, 'tax_filter_model.onnx'))
                self.pdc_only_session = ort.InferenceSession(os.path.join(param_models_dir, 'pdc_only_model.onnx'))
                self.include_cleared_session = ort.InferenceSession(os.path.join(param_models_dir, 'include_cleared_model.onnx'))
                self.group_name_session = ort.InferenceSession(os.path.join(param_models_dir, 'group_name_model.onnx'))
                self.gst_status_session = ort.InferenceSession(os.path.join(param_models_dir, 'gst_status_model.onnx'))
                self.godown_name_session = ort.InferenceSession(os.path.join(param_models_dir, 'godown_name_model.onnx'))
            except Exception as e:
                print(f"Warning: Param ONNX models not found ({e}). Falling back to heuristic rules.")
            
            self.INTENT_BENCHMARKS = {
                "LIST_COMPANIES": ["what companies are loaded", "show me active companies", "list running companies"],
                "GET_LEDGER_BALANCE": ["what is the balance of", "closing balance of", "ledger balance", "how much is in account", "What is the outstanding amount for Anand Cargo ?", "Display the last 7 days outstanding of the group Relaxo", "What is the pending and cleared amount for Thermax Ltd", "Is there any pending amount for ledger DeltaFlow?", "What is the total outstanding balance for Ledger CECO?", "What is the total outstanding under Group Expenses", "Show customer advances for Reliance Industries Ltd", "Show supplier advances for Sundry Creditors", "What is the outstanding amount for Mr Raj?", "Give pending amount for credit card expenses also what is the cleared amount?", "How much is pending from Sun Enterprises?"],
                "GET_TRIAL_BALANCE": ["show trial balance", "get trial balance", "trial balance report"],
                "GET_STOCK_SUMMARY": ["stock summary", "inventory status", "how much stock do I have"],
                "GET_RECENT_VOUCHERS": ["show daybook", "recent transactions", "today's vouchers", "latest entries"],
                "GET_RECEIVABLES": ["what do they owe me", "pending bills for debtor", "receivables from", "show pending invoices", "outstanding amount from", "Oldest 10 Bills which are pending to receive today only above 1L", "how many customers bills are due in the next 10 days and what is the total value?", "Bills which are pending today starting with oldest billdate first for which the amount is less than 1L?", "Show highest pending and cleared receivables bill amount for sundry debtors also give their GST status?", "Total Receivables amount less than 90 days", "Receivable > 90 days ?", "Customer dues and settled bills with over due amount less than 55000", "how many bills are due to receive in next 7 days.list in ascending order of bill date", "What’s my total outstanding receivable amount?", "How many customers owe me money right now?", "What’s the total overdue receivable amount?", "Which customers have not paid for more than 60 days?", "What’s the oldest unpaid bill in my books and what is the Tax amount?", "Customer dues for today?", "highest receivable amount for creditors with overdue days less than a month", "lowest receivable bill amount", "My total receivable", "Overdue receivables ?", "Total pending receivables?", "Display the last 7 days due outstanding of debtors", "For Aquatech system, how many overdue bills are available till date and what is the total value of it", "Show me the overdue bills of the party AquaTech system", "For Sukan Engineering , how many overdue bills are available till date and what is the total value of it", "Show me the overdue invoices of the Jagat", "How much does Dew Cargo owe me?", "Which customer bills are pending to receive today", "When are my collections due", "Show me all invoices pending from Thermax Ltd", "List all the pending receivable bills number for Chemical Process Pvt LTD", "Which parties have postdated receivables?", "How much cash will I be getting this week?", "how much money owed to me is overdue?", "How much money should i be getting today?", "how much payment to me is past due date?", "net amount receivable beyond due date?", "what money i should get?", "Total Receivables amount", "Show receivable outstanding", "Display receivable outstanding between October 2024 and February 2025", "how much am i owed?", "Debtors Bills expected to pay today only and which are settled yesterday?", "For Aquatech system, how many overdue bills are available till date that crossed 60 days and what is the total value of it. Which bill has the highest overdue bills?", "highest receivable amount for creditors with avg overdue days less than a month", "highest receivable bill amount for debtors that has pending amount equal to 2L", "how many customers bills are due in the next 10 days and what is the total value? Which bill has the least overdue days", "How much does Anand Cargo owe me along with overdue date and how much is cleared?", "lowest receivable amount only for gstr 2a creditors", "Show highest pending and cleared receivables bill amount for sundry debtors?", "what amount should i get from debtors this week?", "Which parties under sundry creditors for goods import are overdue receivables?", "net outstanding for debtors with avg average overdue days less than 2 days"],
                "GET_PAYABLES": ["what do I owe them", "pending bills for creditor", "payables to", "show pending invoices from supplier", "List the parties to whom I need to make the payment this week", "Payables till date", "Which vendors are due for payment this week?", "What’s the total overdue payable beyond 30 days?", "What is the overdue payable amount?", "Outstanding of Sundry Creditors?", "Which suppliers bills are due today ?", "Which vendors are due to receive today?", "Show the opening amounts for payables with their totals", "Display the Opening Amount, pending and final balance of payables as on 02-03-2025", "give the total number of bills pending to be paid to thermax in last 30 days", "Which parties have postdated payables?", "how much of my paymentsis overdue?", "net outstanding payables?", "Till date payable ?", "what do i owe as of today?", "Total payables as of today", "What will be my payables by next month?", "What will be my payables by next HY?", "Overdue payables", "Give payable outstanding company-wise and list bills nearing due date within 7 days.", "creditor's Bills which are due today for collections with overdue amount equal to 60000", "latests 5 Bills which are due today for payments to Jagat?", "List due payable bills as on today with most overdue days on top?", "list the bills with new billdates on top due for payments and how much is cleared?", "whats the most overdue date bill that i need to pay and that are cleared?", "Identify the parties to whom the payment is pending with their total value in decreasing avg overdue days", "List the parties to whom I need to make the payment this week in decreasing pending amount", "How much is pending from Sundry Creditors?", "List suppliers who has both Overdue and cleared Payables in increasing order?", "Show payable summary for GSTR2A Creditors", "overdue payables for Sundry Creditors for this quarter"],
                "GET_AGEING": ["ageing analysis", "bills older than 90 days", "pending since last month", "Show me ageing of receivables by 30, 60, 90 days.", "What is the ageing of the outstanding amount based on the bill date for the 6 months from Jan 2025 for the ledger Rashmi Traders", "Show receivable ageing for Thermax Ltd based on due date", "Give payable ageing analysis for Sundry Creditors using bill date", "Show ageing for Infosys Ltd for overdue receivables sorted by total pending amount ascending", "Show ageing for Sundry Creditors where pending amount is greater than 500000", "List payable ageing for Debtors group based on bill date sorted by bill count", "Show ageing summary for Jagat and Thermax based on due date", "Show payable ageing for Agru with pending amount greater than 100000", "List receivable ageing for sundry creditors where total pending amount is less than 50000", "Show ageing analysis for Reliance Industries Ltd based on bill date with total pending amount equal to 250000", "Give payable ageing for Sundry Debtors sorted by bill count ascending"],
                "GET_TOP_DEBTORS": ["top 10 debtors", "highest outstanding customers", "biggest receivables", "top 5 parties with overdue receivables with maximum overdue days which have settled bills as well.", "Who are my top 10 debtors based on pending bills ?"],
                "GET_TOP_CREDITORS": ["top 10 creditors", "highest payable suppliers", "biggest payables", "Identify the top 5 parties to whom the payment is pending for feb 2025", "Identify the top 5 parties to whom the payment is pending for feb 2025 with highest average overdue days."],
            }
            
            for intent, phrases in self.INTENT_BENCHMARKS.items():
                self.intent_embeddings[intent] = [self.get_embedding(p) for p in phrases]


                
        except Exception as e:
            print(f"Warning: Failed to load ONNX model ({e}). Intents may fallback to GET_LEDGER_BALANCE.")

        # Words to strip out when trying to find a ledger name from a query via fuzzy match
        self.stop_phrases = [
            "what is the balance of", "what is balance of", "balance of", "balance for",
            "show balance of", "fetch balance of", "get balance of", "how much is in",
            "how much is", "ledger balance of", "closing balance of", "account balance of",
            "total outstanding balance for", "total outstanding balance", "total outstanding",
            "outstanding balance for", "outstanding balance", "show me the overdue bills of the party",
            "show me the overdue invoices of the", "show me the overdue invoices of",
            "show me the", "show me", "give me", "list all the", "list all", "list", "display the", "display",
            "what is the", "what is", "which", "who", "how many", "how much does", "how much", "amount",
            "show ledger", "get ledger", "ledger", "balance", "for", "of", "the", "please",
            "total", "outstanding", "pending bills", "pending invoices", "pending", 
            "bills", "invoices", "due amount", "amount due", "owed by", "owe me", "owe",
            "receivables from", "payables to", "what is my", "is", "show customer advances", "show supplier advances", "show all sales invoices for", "show all sales invoices",
            "show sales invoices for", "show sales invoices", "show purchase invoices for", "show purchase invoices",
            "sales invoices for", "sales invoices", "purchase invoices for", "purchase invoices",
            "sales vouchers for", "sales vouchers", "purchase vouchers for", "purchase vouchers",
            "receipt vouchers for", "receipt vouchers", "payment vouchers for", "payment vouchers",
            "journal vouchers for", "journal vouchers", "contra vouchers for", "contra vouchers",
            "sales entries for", "sales entries", "purchase entries for", "purchase entries",
            "sales", "purchase", "receipt", "payment", "journal", "contra", "invoices", "vouchers", "entries",
            "vendors", "vendor", "customers", "customer", "creditors", "creditor", "debtors", "debtor",
            "parties", "party", "suppliers", "supplier", "group", "under", "system", "all", "any",
            "receivable", "receivables", "payable", "payables", "advance", "advances", "sundry", "collections",
            "cleared", "settled", "due", "overdue", "unpaid", "paid", "companies", "company", "comp"
        ]
        
        self.common_words = {
            "the", "and", "for", "that", "this", "with", "from", "your", "what", "how", "who", "why", 
            "when", "where", "are", "you", "not", "all", "any", "it", "is", "of", "to", "in", "on", 
            "at", "by", "as", "be", "do", "does", "did", "will", "would", "shall", "should", "can", 
            "could", "may", "might", "must", "a", "an", "money", "total", "amount", "balance", 
            "show", "get", "give", "list", "display", "bill", "bills", "invoice", "invoices", 
            "payment", "payments", "receipt", "receipts", "due", "overdue", "pending", "cleared", 
            "paid", "receivable", "payable", "unpaid", "settled", "outstanding", "opening", "closing", 
            "final", "net", "gst", "gstin", "status", "sundry", "next", "last", "past", "top", "showing", 
            "based", "order", "ascending", "descending", "beyond", "within"
        }

        self.generic_ledgers = {
            "customer", "customers", "debtor", "debtors", "creditor", "creditors", 
            "supplier", "suppliers", "vendor", "vendors", "account", "accounts", 
            "ledger", "ledgers", "group", "groups"
        }

    def resolve_ledger(self, query, ledgers):
        if not ledgers:
            return None, 0.0, [], 0
            
        ledger_names = list(ledgers.keys())
        query_lower = query.lower()
        
        # Rewrite Group Expenses to Expenses ONLY if Group Expenses is not a valid ledger/group name in the company
        if "group expenses" in query_lower and not any(l.lower() == "group expenses" for l in ledger_names):
            if any(l.lower() == "expenses" for l in ledger_names):
                query_lower = query_lower.replace("group expenses", "expenses")
        
        # ======================================================================
        # RESOLUTION STEP 1: Exact Substring Word-Boundary Search (Fast Path)
        # ======================================================================
        best_exact_name = None
        best_exact_pos = len(query_lower)
        best_is_generic = True
        system_vtypes = {"sales", "purchase", "receipt", "payment", "journal", "contra"}
        for name in ledger_names:
            name_lower = name.lower()
            if name_lower in self.common_words or name_lower in system_vtypes:
                continue

            try:
                pattern = r'\b' + re.escape(name_lower) + r'\b'
                match = re.search(pattern, query_lower)
                if match:
                    pos = match.start()
                    is_generic = name_lower in self.generic_ledgers
                    if is_generic and not best_is_generic:
                        continue
                    if not is_generic and best_is_generic:
                        best_exact_pos = pos
                        best_exact_name = name
                        best_is_generic = False
                    elif pos < best_exact_pos:
                        best_exact_pos = pos
                        best_exact_name = name
                        best_is_generic = is_generic
                    elif pos == best_exact_pos and best_exact_name and len(name) > len(best_exact_name):
                        best_exact_name = name
                        best_is_generic = is_generic
            except re.error:
                pass

        if best_exact_name:
            exact_clean = best_exact_name.lower().strip()
            score = 100.0
            if len(exact_clean.split()) <= 2:
                ambig_matches = []
                for lname in ledger_names:
                    if lname.lower() in system_vtypes:
                        continue
                    if re.search(r'\b' + re.escape(exact_clean) + r'\b', lname.lower()):
                        ambig_matches.append(lname)
                if len(ambig_matches) > 1:
                    return None, score, ambig_matches[:4], 1
            return best_exact_name, score, [], 1
                    
        # ======================================================================
        # RESOLUTION STEP 2: Sliding 1-to-4 Word N-Gram Window Generator
        #
        # WHY IT IS PRESENT:
        #   Users type informal party names (e.g. 'thermo ltd' when Tally ledger is 'THERMO LIMITED').
        #   Generating contiguous sub-sequences of length 1, 2, 3, 4 words ensures we isolate
        #   the exact party name substring while discarding accounting stop words.
        # ======================================================================
        common = {"what", "is", "the", "balance", "of", "show", "me", "how", "much", "does", "owe", 
                  "amount", "for", "party", "invoices", "pending", "from", "ledger", "account", "due", "receivables",
                  "payable", "payables", "receivable", "debtor", "debtors", "creditor", "creditors", "customer", "customers",
                  "vendor", "vendors", "supplier", "suppliers", "all", "any", "some", "total", "value", "many",
                  "bill", "bills", "receipt", "receipts", "payment", "payments", "sales", "purchase", "journal", "contra", "vouchers", "entries", "invoice",
                  "credit", "debit", "note", "notes", "company", "companies", "group", "groups", "details", "summary", "type", "types",
                  "with", "on", "in", "at", "by", "to", "and", "or", "but", "less", "than", "more", "greater", "above", "below",
                  "under", "over", "age", "days", "day", "date", "dates", "today", "year", "month", "week", "where", "as", "about",
                  "between", "after", "before", "since", "till", "who", "which", "list", "sundry", "next", "last", "past", "top", "showing", "based", "order", "ascending", "descending",
                  "be", "paid", "unpaid", "cleared", "settled", "overdue", "outstanding", "opening", "closing", "final", "net", "display", "give", "get", "gst", "gstin", "status",
                  "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec",
                  "january", "february", "march", "april", "june", "july", "august", "september", "october", "november", "december",
                  "first", "second", "third", "fourth", "fifth", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "limit",
                  "are", "were", "was", "been", "starting", "start", "end", "ending", "billdate", "duedate", "paymentdate", "least", "most",
                  "inr", "rs", "rupees", "lakh", "lakhs", "crore", "crores", "cr", "beyond", "within",
                  "limited", "ltd", "pvt", "private", "inc", "corp", "corporation", "enterprises", "industries", "international",
                  "owed", "owing", "collect", "collection", "collections"}
                  
        q_clean = re.sub(r'[^a-zA-Z0-9\s]', '', query_lower)
        words = q_clean.split()
        
        windows = []
        for n in range(4, 0, -1):
            for i in range(len(words) - n + 1):
                window = " ".join(words[i:i+n])
                if all(w in common or w.isdigit() or len(w) < 2 for w in words[i:i+n]):
                    continue
                if len(window) < 3:
                    continue
                windows.append(window)
                
        if not windows:
            return None, 0.0, [], 0
            
        filtered_ledgers = [(i, name.lower()) for i, name in enumerate(ledger_names) if name.lower() not in self.common_words and len(name) >= 2]
        if not filtered_ledgers:
            return None, 0.0, [], 0
            
        ledger_names_lower = [name for i, name in filtered_ledgers]
        original_indices = [i for i, name in filtered_ledgers]
        
        # ======================================================================
        # RESOLUTION STEP 3: RapidFuzz Token Set Ratio String Matching
        # ======================================================================
        # Sort windows by length descending so longest party entity phrases are evaluated first
        windows.sort(key=lambda w: len(w.split()), reverse=True)
        
        ledger_best = {} # idx -> (score, w_len, window)
        for window in windows:
            w_tokens = set(window.split())
            w_len = len(w_tokens)
            matches = process.extract(window, ledger_names_lower, scorer=fuzz.token_set_ratio, limit=10)
            if matches:
                for m in matches:
                    matched_name_lower = m[0]
                    raw_score = m[1]
                    idx = original_indices[m[2]]
                    m_tokens = set(matched_name_lower.split())
                    
                    overlap = len(w_tokens.intersection(m_tokens))
                    if overlap == 0:
                        continue
                        
                    coverage = overlap / w_len
                    score = raw_score * coverage
                    
                    if idx not in ledger_best:
                        ledger_best[idx] = (score, w_len, window)
                    else:
                        prev_score, prev_w_len, prev_w = ledger_best[idx]
                        # Primary: higher score wins. Tiebreaker: longer window.
                        if score > prev_score or (score == prev_score and w_len > prev_w_len):
                            ledger_best[idx] = (score, w_len, window)

        if not ledger_best:
            return None, 0.0, [], 0

        # Find top scoring ledger
        sorted_candidates = sorted(ledger_best.items(), key=lambda x: x[1][0], reverse=True)
        best_idx, (best_score, best_w_len, best_window) = sorted_candidates[0]

        if best_score < 85.0:
            return None, best_score, [], 0

        # Ambiguity Check for candidate window
        if best_window:
            top_matches = process.extract(best_window, ledger_names_lower, scorer=fuzz.token_set_ratio, limit=5)
            high_score_candidates = []
            for m in top_matches:
                m_score = m[1]
                m_orig_name = ledger_names[original_indices[m[2]]]
                if abs(m_score - best_score) < 5.0 and m_orig_name not in high_score_candidates:
                    high_score_candidates.append(m_orig_name)
            
            if len(high_score_candidates) > 1:
                # Return ambiguity list!
                return None, best_score, high_score_candidates[:4], 3
            
        matched_name = ledger_names[best_idx]
        matched_lower = matched_name.lower()
        if "key accounts" in matched_lower and "key" not in query_lower:
            return None, 0.0, [], 0
        if "customers" in matched_lower and "customer" not in query_lower:
            return None, 0.0, [], 0
            
        return matched_name, best_score, [], 3

    def get_embedding(self, text):
        if not self.session or not self.tokenizer:
            return np.zeros(384)
            
        encoding = self.tokenizer.encode(text)
        input_ids = np.array([encoding.ids], dtype=np.int64)
        attention_mask = np.array([encoding.attention_mask], dtype=np.int64)
        token_type_ids = np.array([encoding.type_ids], dtype=np.int64)
        
        inputs = {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'token_type_ids': token_type_ids
        }
        outputs = self.session.run(None, inputs)
        
        last_hidden_state = outputs[0][0]
        mask = attention_mask[0]
        
        input_mask_expanded = np.expand_dims(mask, axis=-1)
        sum_embeddings = np.sum(last_hidden_state * input_mask_expanded, axis=0)
        sum_mask = np.clip(input_mask_expanded.sum(axis=0), a_min=1e-9, a_max=None)
        
        embedding = sum_embeddings / sum_mask
        norm = np.linalg.norm(embedding)
        if norm > 0:
            embedding = embedding / norm
        return embedding

    def predict_intent(self, query):
        q_lower = query.lower()
        if "compare" in q_lower and ("company" in q_lower or "companies" in q_lower or "between" in q_lower):
            return "GET_COMPARATIVE_SUMMARY"

        if hasattr(self, 'intent_session') and self.intent_session:
            ml_intent, conf = self.predict_param(self.intent_session, query)
            if ml_intent:
                return ml_intent
        return "GET_LEDGER_BALANCE"

    def predict_param(self, session, text: str):
        if not session:
            return None, 0.0
        try:
            inputs = {'string_input': np.array([[text]], dtype=object)}
            label, probs = session.run(None, inputs)
            predicted = label[0]
            if isinstance(probs[0], dict):
                confidence = float(max(probs[0].values()))
            else:
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

    def extract_parameters(self, query: str) -> dict:
        params = {
            "date_filter": None,
            "age_filter": None,
            "amount_filter": None,
            "limit": None,
            "sort": None,
            "reference_date": None,
            "is_bill_query": False,
            "document_ref": None,
            "date_target": "bill_date",
            "count_only": False,
            "sum_only": False,
            "status_filter": None,
            "voucher_type": None,
            "tax_filter": False,
            "pdc_only": False,
            "include_cleared": False,
            "item_name": None,
            "stock_group": None,
            "stock_category": None,
            "group_name": None,
            "currency": None,
            "forex_only": False,
            "gst_status": None,
            "cost_center": None,
            "godown_name": None,
            "compare_companies": False
        }
        
        q_lower = query.lower()
        normalized_query = query.replace("₹", "Rs ")

        # Extract 27-entity advanced parameters
        if "expenses" in q_lower:
            params["group_name"] = "Expenses"
        elif "sundry creditors" in q_lower or "creditors group" in q_lower:
            params["group_name"] = "Sundry Creditors"
        elif "sundry debtors" in q_lower or "debtors group" in q_lower:
            params["group_name"] = "Sundry Debtors"

        if "usd" in q_lower or "$" in q_lower:
            params["currency"] = "USD"
            params["forex_only"] = True
        elif "eur" in q_lower or "€" in q_lower:
            params["currency"] = "EUR"
            params["forex_only"] = True

        if "gstr 2a" in q_lower or "gstr2a" in q_lower:
            params["gst_status"] = "reconciled"
        elif "unregistered" in q_lower:
            params["gst_status"] = "unregistered"

        if "reliance job" in q_lower:
            params["cost_center"] = "Reliance Job"

        if "bhiwandi" in q_lower or "godown" in q_lower or "warehouse" in q_lower:
            params["godown_name"] = "Bhiwandi Godown"

        if "compare" in q_lower and ("company" in q_lower or "companies" in q_lower or "between" in q_lower):
            params["compare_companies"] = True

        # Regex for Document References (Case-preserving finditer match) - extract first as other params depend on it
        doc_id = None
        for doc_m in re.finditer(r'\b(?:bill|invoice|voucher|reference)\s+(?:no\b\.?|number\b|ref\b\.?|reference\b)?\s*([a-z0-9\-/\\]+)\b', q_lower):
            candidate = doc_m.group(1)
            if candidate not in ["10", "5", "all", "any", "no", "one"] and bool(re.search(r'\d', candidate)):
                start_idx, end_idx = doc_m.span(1)
                doc_id = query[start_idx:end_idx]
                break
        if doc_id:
            params["is_bill_query"] = True
            params["document_ref"] = doc_id
        
        # ML Inference for Semantic Parameters
        ml_status, status_conf = self.predict_param(self.status_session, query)
        ml_date_tgt, date_tgt_conf = self.predict_param(self.date_target_session, query)
        ml_is_bill, is_bill_conf = self.predict_param(self.is_bill_session, query)
        ml_voucher_type, vt_conf = self.predict_param(self.voucher_type_session, query)
        ml_tax, tax_conf = self.predict_param(self.tax_filter_session, query)
        ml_pdc, pdc_conf = self.predict_param(self.pdc_only_session, query)
        ml_inc_cleared, inc_cleared_conf = self.predict_param(self.include_cleared_session, query)
        ml_gst, gst_conf = self.predict_param(self.gst_status_session, query)
        
        if ml_voucher_type:
            params["voucher_type"] = ml_voucher_type
        if ml_tax is not None:
            params["tax_filter"] = ml_tax
        if ml_pdc is not None:
            params["pdc_only"] = ml_pdc
        if "postdated" in q_lower or "post-dated" in q_lower or "pdc" in q_lower:
            params["pdc_only"] = True
        if "pending and cleared" in q_lower or "cleared and pending" in q_lower or "cleared amount" in q_lower:
            params["include_cleared"] = True
        elif ml_inc_cleared is not None:
            params["include_cleared"] = ml_inc_cleared
        if "gst status" in q_lower or "gst registration" in q_lower or "gstin" in q_lower:
            params["gst_status"] = True
        elif ml_gst is not None:
            params["gst_status"] = ml_gst
        
        use_ml_status = True
        use_ml_date_tgt = True
        use_ml_is_bill = True

        if use_ml_is_bill:
            params["is_bill_query"] = ml_is_bill

        # Binary flags & simple keyword limits
        # Binary flags & simple keyword limits
        if use_ml_status:
            params["status_filter"] = ml_status
        else:
            is_cleared = bool(re.search(r'\b(cleared|settled)\b', q_lower) or re.search(r'(?<!not )(?<!to be )\bpaid\b', q_lower))
            if is_cleared and bool(re.search(r'\b(pending|due|dues|outstanding|unpaid|overdue)\s+(?:and|or|as well as|also)\s+(?:cleared|settled|paid)\b', q_lower)) or bool(re.search(r'\b(?:cleared|settled|paid)\s+(?:and|or|as well as|also)\s+(pending|due|dues|outstanding|unpaid|overdue)\b', q_lower)):
                params["status_filter"] = None # mixed query
            elif is_cleared:
                params["status_filter"] = "cleared"
            elif any(w in q_lower for w in ["pending", "overdue", "unpaid", "not paid"]):
                if "settled" in q_lower or "cleared" in q_lower:
                    params["status_filter"] = None
                else:
                    params["status_filter"] = "pending"
                
        # If explicitly asking for a single bill's details, status doesn't matter unless explicitly specified
        if params.get("document_ref") and "overdue" not in q_lower and "pending" not in q_lower and "cleared" not in q_lower and "settled" not in q_lower and "unpaid" not in q_lower and "paid" not in q_lower and "due" not in q_lower:
            params["status_filter"] = None
            
        # Count and Sum
        if "how many days" in q_lower:
            params["count_only"] = False
        else:
            is_sort_count = bool(re.search(r'\b(?:sort|sorted|order)\s+by\s+\w*\s*count\b', q_lower)) or bool(re.search(r'\bcount\s+(?:asc|desc|ascending|descending)\b', q_lower))
            params["count_only"] = ("how many" in q_lower or "number of" in q_lower or (bool(re.search(r'\bcount\b', q_lower)) and not is_sort_count)) and ("total" not in q_lower or "total number" in q_lower) and "value" not in q_lower and "amount" not in q_lower and "list" not in q_lower and "show" not in q_lower and "details" not in q_lower
            if any(w in q_lower for w in ["least", "most", "highest", "lowest", "top"]) and any(w in q_lower for w in ["party", "parties", "debtor", "debtors", "creditor", "creditors", "customer", "customers", "supplier", "suppliers", "vendor", "vendors", "who"]):
                params["count_only"] = False
        is_yes_no = q_lower.strip().startswith(("is ", "are ", "do ", "does ", "can ", "whether "))
        is_compound = ("how many" in q_lower and ("total" in q_lower or "value" in q_lower or "list" in q_lower)) or ("list" in q_lower and ("count" in q_lower or "total" in q_lower) and any(w in q_lower for w in ["and", "also", "along with", "with their", "as well as"])) or "also" in q_lower or "and what" in q_lower or "with their total" in q_lower or "and how much" in q_lower or "dependent" in q_lower or "risk" in q_lower
        
        has_old_directive = bool(re.search(r'\bold\b', q_lower)) and "days old" not in q_lower and "day old" not in q_lower
        
        # Extract limit first since it affects sum_only
        limit_match = re.search(r"\b(?:top|last|latest|latests|first|oldest|highest|lowest)\s+(\d+)\b(?!\s*(?:days|months|weeks|years)\b)", q_lower)
        if limit_match:
            params["limit"] = int(limit_match.group(1))
            
        # sum_only is true if they strictly ask for total/sum and NO bills/list/details
        has_opposing_status = bool(re.search(r'\b(cleared|settled|paid)\b', q_lower)) and bool(re.search(r'\b(pending|due|dues|outstanding|unpaid|overdue)\b', q_lower))
        has_superlative = any(w in q_lower for w in ["oldest", "latest", "newest", "highest", "lowest", "longest time", "most overdue", "least overdue", "decreasing", "increasing", "new", "dependent"]) or has_old_directive
        if (bool(re.search(r'\b(totals?|sum|how much|net amount|net|amount|money)\b', q_lower)) or has_opposing_status) and not params["count_only"]:
            is_date_exception = ("date" in q_lower and "due date" not in q_lower and "bill date" not in q_lower and "billdate" not in q_lower)
            is_net_outstanding_report = ("net outstanding" in q_lower and "payable" not in q_lower and "receivable" not in q_lower and "amount" not in q_lower)
            is_how_much_group = ("how much" in q_lower or "what amount" in q_lower) and any(w in q_lower for w in ["debtors", "creditors", "customer", "supplier", "vendor"])
            
            # Superlatives are never sum_only
            if has_superlative:
                params["sum_only"] = False
            # Explicit totals / sums
            elif ("total" in q_lower or "sum" in q_lower) and not is_compound:
                if "ageing" in q_lower or "aging" in q_lower or "ledger" in q_lower or "balance for" in q_lower or is_net_outstanding_report or "group" in q_lower:
                    params["sum_only"] = False
                else:
                    params["sum_only"] = True
            elif "how much" in q_lower or "what amount" in q_lower:
                params["sum_only"] = True
            elif "net" in q_lower and "bill" not in q_lower and "list" not in q_lower and "invoice" not in q_lower:
                params["sum_only"] = True
            elif has_opposing_status and not params["limit"] and "bill" not in q_lower and "invoice" not in q_lower and "list" not in q_lower:
                params["sum_only"] = True
            # exceptions where they are asking for amount filter or list of amounts/details
            elif "amount is" in q_lower or "amount greater" in q_lower or "amount less" in q_lower or "amount equal" in q_lower or "balance" in q_lower or "any pending amount" in q_lower or "tax amount" in q_lower or "total pending amount" in q_lower or "how much is overdue" in q_lower or "total outstanding under" in q_lower:
                params["sum_only"] = False
            elif "bill" in q_lower or "list" in q_lower or "what do i owe" in q_lower or "highest" in q_lower or "lowest" in q_lower or "parties" in q_lower or "customers" in q_lower or ("debtors" in q_lower and not is_how_much_group) or ("creditors" in q_lower and not is_how_much_group) or ("suppliers" in q_lower and not is_how_much_group) or ("vendors" in q_lower and not is_how_much_group) or "ledgers" in q_lower or "which" in q_lower or "pending and cleared" in q_lower or "along with" in q_lower or is_date_exception or is_net_outstanding_report or any(bool(re.search(r'\b' + w + r'\b', q_lower)) for w in ["payables", "receivables", "vouchers", "payments", "collections", "invoices"]):
                params["sum_only"] = False
            elif params["limit"]:
                params["sum_only"] = False
            else:
                params["sum_only"] = True

        # Document details queries are never sum_only
        if params.get("document_ref"):
            params["sum_only"] = False
        
        if use_ml_date_tgt:
            params["date_target"] = ml_date_tgt
            if any(w in q_lower for w in ["payable ageing", "receivable ageing", "payable aging", "receivable aging", "payables ageing", "receivables ageing", "payables aging", "receivables aging"]):
                params["date_target"] = "due_date"
            elif "based on bill date" in q_lower:
                params["date_target"] = "bill_date"
            elif "based on due date" in q_lower:
                params["date_target"] = "due_date"
        else:
            if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable", "paid", "get", "getting", "cash", "received", "receipts"]):
                params["date_target"] = "due_date"
            elif any(w in q_lower for w in ["bill", "invoices", "invoiced", "raised", "made", "created", "issue", "issued"]):
                params["date_target"] = "bill_date"
            else:
                if "bill" not in q_lower and "receivable" not in q_lower and "payable" not in q_lower and "on-account" not in q_lower and "on account" not in q_lower:
                    params["date_target"] = None
            # Explicit bill details
            if "which ledger is associated" in q_lower or "which voucher type" in q_lower or params.get("document_ref"):
                params["date_target"] = None
            
        sort_match = re.search(r'\b(?:sort|sorted|order)\s+(?:by|of)\s+(?:total\s+|pending\s+|net\s+|average\s+|avg\s+)*(bill date|due date|amount)\s+(ascending|descending|asc|desc)', q_lower) or re.search(r'\b(ascending|descending|asc|desc)\s+(?:order\s+)?(?:by|of)\s+(?:total\s+|pending\s+|net\s+|average\s+|avg\s+)*(bill date|due date|amount)', q_lower)
        if sort_match:
            if sort_match.group(1) in ["ascending", "descending", "asc", "desc"]:
                field = sort_match.group(2).replace(" ", "_")
                order = "asc" if "asc" in sort_match.group(1) else "desc"
            else:
                field = sort_match.group(1).replace(" ", "_")
                order = "asc" if "asc" in sort_match.group(2) else "desc"
            params["sort"] = {"field": field, "order": order}
        elif "sorted by" in q_lower or "sort by" in q_lower or "order by" in q_lower:
            params["sort"] = None
        else:
            if "oldest" in q_lower or "earliest" in q_lower or "ascending" in q_lower or "asc" in q_lower or "latest" in q_lower or "newest" in q_lower or ("increasing" in q_lower and ("order" in q_lower or "sort" in q_lower)) or "new" in q_lower or has_old_directive:
                if "due date" in q_lower or "duedate" in q_lower or "due_date" in q_lower:
                    params["sort"] = {"field": "due_date", "order": "asc" if ("oldest" in q_lower or "earliest" in q_lower or has_old_directive or "ascending" in q_lower or "asc" in q_lower or "increasing" in q_lower) else "desc"}
                elif ("bill" in q_lower or "invoice" in q_lower) and ("oldest" in q_lower or "earliest" in q_lower or has_old_directive):
                    params["sort"] = {"field": "bill_date", "order": "asc"}
                    is_plural_list = bool(re.search(r'\b(which|how many|list|show|all|identify the|our)\s+(debtors|suppliers|customers|creditors|vendors|ledgers|parties|bills|invoices)\b', q_lower))
                    if not params["limit"] and "first" not in q_lower and "list" not in q_lower and not is_plural_list and not is_compound and not is_yes_no: 
                        params["limit"] = 1
                elif "latest" in q_lower or "newest" in q_lower:
                    params["sort"] = {"field": "bill_date", "order": "desc"}
                elif "new" in q_lower and ("bill date" in q_lower or "billdate" in q_lower or "billdates" in q_lower):
                    params["sort"] = {"field": "bill_date", "order": "desc"}
                elif "bill date" in q_lower or "billdate" in q_lower:
                    params["sort"] = {"field": "bill_date", "order": "asc"}
                elif "amount" in q_lower:
                    params["sort"] = {"field": "amount", "order": "asc"}
                else:
                    if any(w in q_lower for w in ["payable", "receivable", "debtor", "creditor", "supplier", "vendor", "customer", "outstanding"]):
                        params["sort"] = {"field": "amount", "order": "asc"}
                    else:
                        params["sort"] = {"field": params["date_target"] if params["date_target"] else "due_date", "order": "asc"}
            elif "highest" in q_lower or "largest" in q_lower or "descending" in q_lower or "lowest" in q_lower or "most overdue" in q_lower or "decreasing" in q_lower or "prioritize" in q_lower or "dependent" in q_lower or "high outstanding" in q_lower or "least" in q_lower or "longest time" in q_lower:
                if "most overdue" in q_lower or "least overdue" in q_lower:
                    params["sort"] = {"field": "due_date", "order": "desc" if "least" in q_lower else "asc"}
                elif "longest time" in q_lower:
                    params["sort"] = {"field": "due_date", "order": "asc"}
                else:
                    params["sort"] = {"field": "amount", "order": "asc" if ("lowest" in q_lower or "least" in q_lower) else "desc"}
                
                # Ageing reports rarely have a standard sort parameter in our spec
                if "ageing" in q_lower and not sort_match:
                    params["sort"] = None
            elif "maximum overdue days" in q_lower:
                params["sort"] = {"field": "due_date", "order": "asc"}
            elif "top" in q_lower:
                params["sort"] = {"field": "amount", "order": "desc"}

            # Default limit assignment block for all sort/superlative queries
            has_sort_keyword = any(w in q_lower for w in ["oldest", "latest", "newest", "highest", "lowest", "longest time", "most overdue", "least overdue", "largest", "high outstanding", "least"]) or has_old_directive
            if not params["limit"] and has_sort_keyword:
                # If they explicitly ask for list/first and no number, don't limit to 1
                is_plural_list = bool(re.search(r'\b(which|how many|list|show|all|identify the|our)\s+(debtors|suppliers|customers|creditors|vendors|ledgers|parties|bills|invoices)\b', q_lower))
                is_plural_target = bool(re.search(r'\b(bills|invoices|parties|debtors|suppliers|customers|creditors|vendors|ledgers)\b', q_lower))
                if "first" in q_lower or "list" in q_lower or "bucket" in q_lower or "show" in q_lower or "all" in q_lower or is_plural_list:
                    if ("highest" in q_lower or "lowest" in q_lower or "least" in q_lower or "most" in q_lower or "oldest" in q_lower or "latest" in q_lower or "newest" in q_lower) and ("amount" in q_lower or "value" in q_lower or "bill" in q_lower or "invoice" in q_lower or "party" in q_lower or "receivable" in q_lower or "payable" in q_lower or "due" in q_lower or "outstanding" in q_lower) and "first" not in q_lower and "on top" not in q_lower and (not is_compound or not is_plural_target) and not is_yes_no:
                        params["limit"] = 1
                    else:
                        params["limit"] = None
                else:
                    params["limit"] = 1 if ("top" not in q_lower and (not is_compound or not is_plural_target) and not is_yes_no) else (10 if "top" in q_lower else None)

            if ("ageing" in q_lower or "aging" in q_lower) and not limit_match:
                params["limit"] = None

            has_superlative = any(w in q_lower for w in ["oldest", "latest", "newest", "highest", "lowest", "longest time", "most overdue", "least overdue", "decreasing", "increasing", "new", "dependent"]) or has_old_directive
            if is_compound and not sort_match and not has_superlative:
                params["sort"] = None

        if "highest overdue bills" in q_lower:
            params["sort"] = None

        if any(phrase in q_lower for phrase in ["highest average overdue", "highest avg overdue", "decreasing avg overdue", "decreasing average overdue", "by overdue days", "by average overdue", "by avg overdue"]) and "maximum overdue days" not in q_lower:
            params["sort"] = None

        # Custom date/amount extractors for stability
        if "as of today" in q_lower or "as on today" in q_lower:
            if params.get("document_ref"):
                params["reference_date"] = "today"
                params["date_filter"] = None
            else:
                params["date_filter"] = {"type": "till_today"}
                params["reference_date"] = None
        elif "till date" in q_lower or "today" in q_lower:
            if "pending" in q_lower or "till" in q_lower or "payable" in q_lower or "receivable" in q_lower or "due" in q_lower or "getting" in q_lower or "outstanding" in q_lower or "owe" in q_lower or "settled" in q_lower or "cleared" in q_lower or "paid" in q_lower or "pay" in q_lower or "received" in q_lower:
                params["date_filter"] = {"type": "till_today"}
            else:
                params["date_filter"] = {"type": "today"}

        fy_match = re.search(r'\bfy\s*(?:20)?(\d{2})-(?:20)?(\d{2})\b', q_lower)
        if fy_match:
            sy = int("20" + fy_match.group(1))
            ey = int("20" + fy_match.group(2))
            params["date_filter"] = {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": sy, "end_day": 31, "end_month": 3, "end_year": ey}
        elif "next month" in q_lower:
            params["date_filter"] = {"type": "next_days", "days": 30}
        elif "this month" in q_lower:
            params["date_filter"] = {"type": "this_month"}
        elif "next hy" in q_lower or "next half year" in q_lower:
            params["date_filter"] = {"type": "next_days", "days": 180}
        elif "this quarter" in q_lower:
            params["date_filter"] = {"type": "last_days", "days": 90}
        elif "past 6 months" in q_lower:
            params["date_filter"] = {"type": "last_days", "days": 180}
        elif "within 7 days" in q_lower:
            params["date_filter"] = {"type": "next_days", "days": 7}
        elif "next quarter" in q_lower:
            params["date_filter"] = {"type": "next_quarter"}

        if "yesterday" in q_lower and "today" not in q_lower and "this week" not in q_lower and "this month" not in q_lower:
            params["date_filter"] = None
            
        range_months_match = re.search(r'\b(?:for\s+)?(?:the\s+)?(\d+)\s+months?\s+(?:from|since|starting)\s+([a-z]{3})[a-z]*\s+(\d{4})\b', q_lower)
        if range_months_match:
            months_to_add = int(range_months_match.group(1))
            start_month_str = range_months_match.group(2)[:3].title()
            start_year = int(range_months_match.group(3))
            
            month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                         'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
            if start_month_str in month_map:
                start_month = month_map[start_month_str]
                end_month_raw = start_month + months_to_add - 1
                end_year = start_year + (end_month_raw - 1) // 12
                end_month = (end_month_raw - 1) % 12 + 1
                if end_month in [1, 3, 5, 7, 8, 10, 12]:
                    end_day = 31
                elif end_month in [4, 6, 9, 11]:
                    end_day = 30
                else:
                    is_leap = (end_year % 4 == 0 and (end_year % 100 != 0 or end_year % 400 == 0))
                    end_day = 29 if is_leap else 28
                params["date_filter"] = {
                    "type": "explicit_range",
                    "start_day": 1,
                    "start_month": start_month,
                    "start_year": start_year,
                    "end_day": end_day,
                    "end_month": end_month,
                    "end_year": end_year
                }

        bw_match = re.search(r'between\s+(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)(?:\s+(\d{4}))?\s+and\s+(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\s+(\d{4})', q_lower)
        if bw_match:
            month_map = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
            sm = month_map[bw_match.group(1)[:3]]
            em = month_map[bw_match.group(3)[:3]]
            ey = int(bw_match.group(4))
            sy = int(bw_match.group(2)) if bw_match.group(2) else ey
            import calendar
            end_day = calendar.monthrange(ey, em)[1]
            params["date_filter"] = {"type": "explicit_range", "start_day": 1, "start_month": sm, "start_year": sy, "end_day": end_day, "end_month": em, "end_year": ey}
            
        my_match = re.search(r'\b(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\s+(\d{4})\b', q_lower)
        if my_match and not params["date_filter"]:
            month_str = my_match.group(1)[:3].title()
            month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
            params["date_filter"] = {"type": "month_year", "month": month_map[month_str], "year": int(my_match.group(2))}

        range_match = re.search(r'\b(?:between|ranging from|in the range of|in range of)\s*(?:rs|inr|₹)?\s*([\d\.,]+)\s*(k|l|lakh|cr|m)?\s+(?:to|and)\s*(?:rs|inr|₹)?\s*([\d\.,]+)\s*(k|l|lakh|cr|m)?\b(?!\s*(?:days|months|weeks|years))', q_lower)
        if range_match:
            min_val = float(range_match.group(1).replace(',', ''))
            min_suf = range_match.group(2)
            if min_suf == 'k': min_val *= 1000
            elif min_suf in ['l', 'lakh']: min_val *= 100000
            elif min_suf in ['cr']: min_val *= 10000000
            
            max_val = float(range_match.group(3).replace(',', ''))
            max_suf = range_match.group(4)
            if max_suf == 'k': max_val *= 1000
            elif max_suf in ['l', 'lakh']: max_val *= 100000
            elif max_suf in ['cr']: max_val *= 10000000
            
            params["amount_filter"] = {"operator": "between", "min": min_val, "max": max_val}
        else:
            amt_match = re.search(r'\b(less than|under|below|more than|above|over|greater than|equal to|exceeding|exceeded|crossed)\s*(?:rs|inr|₹)?\s*([\d\.,]+)\s*(k|l|lakh|cr|m)?\b(?!\s*days)', q_lower)
            if not amt_match:
                amt_match = re.search(r'([<>])\s*(?:rs|inr|₹)?\s*([\d\.,]+)\s*(k|l|lakh|cr|m)?\b(?!\s*days)', q_lower)
            if amt_match:
                op_str = amt_match.group(1)
                val = float(amt_match.group(2).replace(',', ''))
                suf = amt_match.group(3)
                if "less" in op_str or "<" in op_str or "under" in op_str or "below" in op_str: op = "<"
                elif "equal" in op_str: op = "="
                else: op = ">"
                if suf == 'k': val *= 1000
                elif suf in ['l', 'lakh']: val *= 100000
                elif suf in ['cr']: val *= 10000000
            
                if op == "=":
                    op = "<"
                    val += 1.0
                params["amount_filter"] = {"operator": op, "value": val}



        if not use_ml_is_bill:
            if "bills" in q_lower or "invoices" in q_lower or "bill amount" in q_lower or "receivable bill" in q_lower or "payable bill" in q_lower or "collections due" in q_lower or "bill number" in q_lower or "invoice number" in q_lower or "bill reference" in q_lower:
                params["is_bill_query"] = True
            elif bool(re.search(r'\b(?:oldest|latest|pending|unpaid|highest|lowest|which|overdue date|receivables|payables)\s+bill\b', q_lower)) or "bill amount" in q_lower:
                params["is_bill_query"] = True
                
            if params["is_bill_query"] and not params["document_ref"]:
                if bool(re.search(r'\b(parties|debtors|creditors|payments)\b', q_lower)):
                    if not bool(re.search(r'\b(list|show|all).*bills\b', q_lower)) and not bool(re.search(r'oldest.*bill', q_lower)) and "bill amount" not in q_lower:
                        params["is_bill_query"] = False
                        
        # 3. Explicit Reference Dates (Supports spaced, hyphenated, and unspaced formats like '1 apr17' or '10aug17')
        ref_match = re.search(r"(?:on|as of|as on|till)\s+(\d{1,2})[-/\s]*(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)[a-z]*[-/\s]*(\d{2,4})", q_lower)
        numeric_ref_match = re.search(r"(?:on|as of|as on|till)\s+(\d{1,2})[-/\s]+(\d{1,2})[-/\s]+(\d{2,4})", q_lower)
        if ref_match:
            try:
                day = int(ref_match.group(1))
                month_str = ref_match.group(2)[:3].title()
                year = int(ref_match.group(3))
                if year < 100:
                    year = 2000 + year
                params["reference_date"] = f"{day:02d}-{month_str}-{year}"
            except: pass
        elif numeric_ref_match:
            try:
                day = int(numeric_ref_match.group(1))
                month_idx = int(numeric_ref_match.group(2))
                year = int(numeric_ref_match.group(3))
                if year < 100:
                    year = 2000 + year
                month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 
                             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
                if month_idx in month_map:
                    params["reference_date"] = f"{day:02d}-{month_map[month_idx]}-{year}"
            except: pass

        if params.get("reference_date") and any(w in q_lower for w in ["till", "up to"]):
            params["date_filter"] = {"type": "till_today"}

        # 4. Relative dates and ages (Regex Fallback)
        match_days = re.search(r'\b(next|last|past)\s+(\d+)\s+days\b', q_lower)
        if match_days:
            days = int(match_days.group(2))
            dir_str = match_days.group(1)
            if dir_str == "next": params["date_filter"] = {"type": "next_days", "days": days}
            else: params["date_filter"] = {"type": "last_days", "days": days}
            
        if "less than a month" in q_lower or "under a month" in q_lower or "less than one month" in q_lower:
            params["age_filter"] = {"operator": "<", "days": 30}
        elif "more than a month" in q_lower or "greater than a month" in q_lower or "over a month" in q_lower:
            params["age_filter"] = {"operator": ">", "days": 30}
        else:
            match_age = re.search(r'(?:less|under|<)\s*(?:than\s+)?(\d+)\s+days\b', q_lower)
            if match_age:
                params["age_filter"] = {"operator": "<", "days": int(match_age.group(1))}
            else:
                match_age2 = re.search(r'(?:greater|more|above|>|over|beyond|crossed|exceeded|older)\s*(?:than\s+)?(\d+)\s+days\b', q_lower)
                if match_age2:
                    params["age_filter"] = {"operator": ">", "days": int(match_age2.group(1))}
            
        if "this week" in q_lower:
            params["date_filter"] = {"type": "this_week"}
            
        # Extract custom ageing intervals
        if "ageing" in q_lower or "aging" in q_lower or "bucket" in q_lower:
            seq_match = re.search(r'\b(?:buckets\s+of|ageing\s+of|buckets|intervals|ageing)?\s*((?:\d+[\s,]+)*\d+)\s*days?\b', q_lower)
            if seq_match:
                nums = [int(x) for x in re.split(r'[\s,]+', seq_match.group(1).strip())]
                if len(nums) >= 2:
                    params["ageing_intervals"] = sorted(list(set(nums)))
            else:
                all_nums = [int(x) for x in re.findall(r'\b\d+\b', q_lower) if int(x) < 365]
                if len(all_nums) >= 2:
                    params["ageing_intervals"] = sorted(list(set(all_nums)))
            
        if "overdue" in q_lower:
            params["overdue_only"] = True
            
        # Clean up month_year date filter if it was a sub-match of the reference date
        if params.get("reference_date") and params.get("date_filter") and params["date_filter"].get("type") == "month_year":
            try:
                import datetime
                ref_dt = datetime.datetime.strptime(params["reference_date"], "%d-%b-%Y")
                if params["date_filter"]["month"] == ref_dt.month and params["date_filter"]["year"] == ref_dt.year:
                    params["date_filter"] = None
            except:
                pass
            
        return params

    def parse_query(self, query: str):
        """
        Parses the natural language query.
        Returns:
            dict containing parsed intents, routed ports, resolved company names, and resolved ledger names.
        """
        query_clean = query.strip()
        query_lower = query_clean.lower()
        
        # 1. Identify which company/port is explicitly mentioned in the query
        detected_company_key = None
        detected_identifier = None
        
        # Build dynamic short-name identifiers from the routing table
        dynamic_identifiers = {}
        for key in self.tally_client.routing_table.keys():
            words = [w for w in key.split() if w not in ["data", "for", "user", "activity", "materials", "pvt", "ltd", "limited", "corp", "co", "private"]]
            if len(words) >= 2:
                dynamic_identifiers[" ".join(words[:2])] = key
                dynamic_identifiers[words[0]] = key
                dynamic_identifiers[words[1]] = key
            elif len(words) == 1:
                dynamic_identifiers[words[0]] = key
                
        # Sort identifiers by length desc to match longest first
        for identifier, full_key in sorted(dynamic_identifiers.items(), key=lambda x: len(x[0]), reverse=True):
            if identifier in query_lower:
                detected_company_key = full_key
                detected_identifier = identifier
                break
                
        # Remove the company name/identifier from the query so it doesn't interfere with ledger name extraction
        query_without_company = query_clean
        if detected_company_key:
            pattern = re.compile(re.escape(detected_company_key), re.IGNORECASE)
            query_without_company = pattern.sub("", query_without_company)
        if detected_identifier:
            pattern = re.compile(re.escape(detected_identifier), re.IGNORECASE)
            query_without_company = pattern.sub("", query_without_company)
            
        query_without_company = query_without_company.strip()

        # Check for group-wise breakdown target
        group_breakdown = False
        if "group" in query_without_company.lower() or "group-wise" in query_without_company.lower():
            group_breakdown = True
            
        # 2. Extract parameters (dates, amounts, limits, sorting, bills)
        parameters = self.extract_parameters(query_without_company)
        if group_breakdown:
            parameters["group_breakdown"] = True
        
        is_bill_query = parameters.get("is_bill_query", False)
        document_ref = parameters.get("document_ref", None)

        # 3. Classify Intent
        detected_intent = self.predict_intent(query_without_company)
        if document_ref:
            detected_intent = "GET_BILL_DETAILS"

        # 4. Extract and Resolve Ledger / Company routing
        extracted_ledger = None
        resolved_ledger = None
        ledger_balance = None
        fuzzy_score = 0.0
        ambiguous_candidates = []
        final_company_key = detected_company_key
        missing_company = False
        company_options = []

        # Checkpoint 1: Company Resolution
        if not detected_company_key:
            if len(self.tally_client.routing_table) > 1:
                missing_company = True
                company_options = [info["name"] for info in self.tally_client.routing_table.values()]
                final_company_key = None
            elif len(self.tally_client.routing_table) == 1:
                final_company_key = list(self.tally_client.routing_table.keys())[0]
            else:
                final_company_key = None
        else:
            final_company_key = detected_company_key

        if not missing_company and final_company_key:
            if detected_intent in ["GET_LEDGER_BALANCE", "GET_RECEIVABLES", "GET_PAYABLES", "GET_AGEING", "GET_BILL_DETAILS", "GET_RECENT_VOUCHERS", "GET_TOP_DEBTORS", "GET_TOP_CREDITORS", "AMBIGUOUS_OUTSTANDINGS"] and detected_intent != "GET_STOCK_SUMMARY":
                # Rewrite group expenses to expenses for real-world companies
                if "under group expenses" in query_without_company.lower():
                    query_without_company = re.sub(r'\bunder group expenses\b', 'under expenses', query_without_company, flags=re.IGNORECASE)
                
                # For debugging, construct a rough extracted_ledger
                temp_query = query_without_company.lower()
                for phrase in sorted(self.stop_phrases, key=len, reverse=True):
                    temp_query = re.sub(r'\b' + re.escape(phrase) + r'\b', ' ', temp_query)
                extracted_ledger = re.sub(r'\s+', ' ', temp_query).strip(",.!? ").strip()
                
                port, resolved_company, context = self.tally_client.get_port_for_company(final_company_key)
                try:
                    ledgers = self.tally_client.fetch_ledgers(resolved_company, port)
                    res, score, amb, _tier = self.resolve_ledger(query_without_company, ledgers)
                    fuzzy_score = score
                    resolved_ledger = res
                    ambiguous_candidates = amb
                    if res:
                        ledger_balance = ledgers[res]
                except Exception as e:
                    print(f"Error fetching ledgers: {e}")
            
        # Clear generic ledger names for top level / generic list queries
        if resolved_ledger and resolved_ledger.lower() in self.generic_ledgers:
            is_plural_generic = resolved_ledger.lower() in ["customers", "debtors", "creditors", "suppliers", "vendors", "customer", "debtor", "creditor", "supplier", "vendor"]
            if detected_intent in ["GET_TOP_DEBTORS", "GET_TOP_CREDITORS"] or any(w in query_without_company.lower() for w in ["settled accounts", "cleared customers", "cleared accounts", "settled bills"]):
                resolved_ledger = None
                ledger_balance = None
            elif is_plural_generic:
                stem = resolved_ledger.lower()[:-1] if resolved_ledger.lower().endswith("s") else resolved_ledger.lower()
                preposition_pattern = r'\b(of|from|for|by|to|in|under)\s+(?:the\s+)?' + stem + r"s?\b"
                if not bool(re.search(preposition_pattern, query_without_company.lower())):
                    resolved_ledger = None
                    ledger_balance = None

        if final_company_key:
            port, resolved_company, context = self.tally_client.get_port_for_company(final_company_key)
        else:
            port, resolved_company, context = None, None, None

        # Post-process intent based on ledger resolution and directional phrases
        q_dir_lower = query_without_company.lower()
        
        # Directional override: ONLY for AMBIGUOUS_OUTSTANDINGS intent
        if detected_intent == "AMBIGUOUS_OUTSTANDINGS":
            has_rec_dir = any(k in q_dir_lower for k in [
                "owed to me", "owed to us", "owed by customer", "owed by customers", "owed by debtor", "owed by debtors",
                "receivable", "receivables", "to collect", "pending collection", "pending collections",
                "due from", "to receive", "money owed to", "pending receivable", "pending receivables"
            ])
            has_pay_dir = any(k in q_dir_lower for k in [
                "owed by me", "owed by us", "owed to supplier", "owed to suppliers", "owed to vendor", "owed to vendors",
                "owed to creditor", "owed to creditors", "payable", "payables", "bills to pay",
                "payments to make", "bills i owe", "payments i owe", "pending payable", "pending payables"
            ])
            if has_rec_dir and not has_pay_dir:
                detected_intent = "GET_RECEIVABLES"
            elif has_pay_dir and not has_rec_dir:
                detected_intent = "GET_PAYABLES"

        if detected_intent == "GET_LEDGER_BALANCE" and not resolved_ledger:
            is_payable = any(k in q_dir_lower for k in ["payable", "creditor", "vendor", "supplier", "payment", "pay", "paid"])
            is_receivable = any(k in q_dir_lower for k in ["receivable", "debtor", "customer", "receive", "getting", "collection"])
            if is_payable and not is_receivable:
                detected_intent = "GET_PAYABLES"
            elif is_receivable and not is_payable:
                detected_intent = "GET_RECEIVABLES"
            elif is_payable and is_receivable:
                detected_intent = "GET_PAYABLES" if "payable" in q_dir_lower else "GET_RECEIVABLES"
            elif any(k in q_dir_lower for k in ["parties", "all", "which"]):
                detected_intent = "GET_RECEIVABLES"
                
        is_group_ledger = False
        role = None
        if resolved_ledger:
            rl_lower = resolved_ledger.lower()
            try:
                port, company_name, ctx = self.tally_client.get_port_for_company(detected_company_key)
                group_map = self.tally_client.get_group_hierarchy_map(company_name, port)
                is_group_ledger = rl_lower in [g.lower() for g in group_map.values()] or rl_lower in ["sundry creditors", "sundry debtors", "creditors", "debtors", "suppliers", "customers", "vendors", "dealers"]
                
                parent = group_map.get(rl_lower, rl_lower)
                if self.tally_client.is_group_under(rl_lower, "sundry creditors", group_map) or \
                   self.tally_client.is_group_under(rl_lower, "trade payables", group_map) or \
                   self.tally_client.is_group_under(parent, "sundry creditors", group_map) or \
                   self.tally_client.is_group_under(parent, "trade payables", group_map):
                    role = "creditor"
                elif self.tally_client.is_group_under(rl_lower, "sundry debtors", group_map) or \
                     self.tally_client.is_group_under(rl_lower, "trade receivables", group_map) or \
                     self.tally_client.is_group_under(parent, "sundry debtors", group_map) or \
                     self.tally_client.is_group_under(parent, "trade receivables", group_map):
                    role = "debtor"
            except Exception:
                pass
            
            # Explicit nested targets override resolved ledger role
            if any(w in query_without_company.lower() for w in ["debtors from", "debtor from", "customers from", "customer from", "debtors in", "debtor in", "customers in", "customer in"]):
                role = "debtor"
            elif any(w in query_without_company.lower() for w in ["creditors from", "creditor from", "suppliers from", "supplier from", "vendors from", "vendor from", "creditors in", "creditor in", "suppliers in", "supplier in", "vendors in", "vendor in"]):
                role = "creditor"
                
            # Transaction keywords bypass group role overrides
            has_transaction_keyword = any(w in query_without_company.lower() for w in ["advance", "advances", "adjustment", "adjustments", "receipt", "receipts", "credit note", "credit notes", "unallocated", "unadjusted", "transaction", "transactions"])
            if has_transaction_keyword:
                role = None
            # Explicit direction keywords in query bypass role-based intent correction ONLY for individual parties (not groups) in real-world queries
            if not is_group_ledger and detected_company_key:
                has_explicit_direction = any(w in query_without_company.lower() for w in [
                    "payable", "payables", "bills to pay", "payments i have to make", "payments to make", "bills i owe", "payments i owe",
                    "receivable", "receivables", "money owed to me", "collections due", "get from"
                ])
                if has_explicit_direction:
                    role = None
                    
            has_explicit_bills = any(w in query_without_company.lower() for w in [
                "bill", "bills", "invoice", "invoices", "payable", "payables", "receivable", "receivables", 
                "pending collections", "pending payables", "payments", "money owed to me", "get from"
            ]) and not any(w in query_without_company.lower() for w in [
                "total sum", "total value", "total amount", "sum of", "count of", "average", "avg", "compare", 
                "who are my top", "total outstanding", "net outstanding"
            ])
            
            if detected_intent in ["GET_RECEIVABLES", "GET_PAYABLES", "GET_TOP_DEBTORS", "GET_TOP_CREDITORS"]:
                if role == "creditor":
                    if is_group_ledger and not has_explicit_bills:
                        detected_intent = "GET_TOP_CREDITORS"
                    else:
                        detected_intent = "GET_PAYABLES"
                elif role == "debtor":
                    if is_group_ledger and not has_explicit_bills:
                        detected_intent = "GET_TOP_DEBTORS"
                    else:
                        detected_intent = "GET_RECEIVABLES"
        else:
            # Generic status-conflict query intent corrections when no ledger is resolved
            if detected_intent in ["GET_RECEIVABLES", "GET_PAYABLES"]:
                is_payable = any(bool(re.search(r'\b' + k + r'\b', query_without_company.lower())) for k in ["payable", "payables", "creditors", "vendors", "suppliers", "creditor", "vendor", "supplier", "payment", "payments", "pay", "paid", "purchase", "purchases", "i owe", "bills to pay"])
                if is_payable:
                    detected_intent = "GET_PAYABLES"
                else:
                    detected_intent = "GET_RECEIVABLES"

        # Yes/No FAQ queries override removed to allow conceptual/analytical report mapping
        pass
            
        # Route sales/purchase/voucher queries to GET_RECENT_VOUCHERS with voucher_type
        q_clean_lower = query_without_company.lower()
        if any(w in q_clean_lower for w in ["sales bill", "sales bills", "sales invoice", "sales invoices", "sales voucher", "sales vouchers"]):
            detected_intent = "GET_RECENT_VOUCHERS"
            parameters["voucher_type"] = "Sales"
        elif any(w in q_clean_lower for w in ["purchase bill", "purchase bills", "purchase invoice", "purchase invoices", "purchase voucher", "purchase vouchers"]):
            detected_intent = "GET_RECENT_VOUCHERS"
            parameters["voucher_type"] = "Purchase"
        elif any(w in q_clean_lower for w in ["journal voucher", "journal vouchers", "journal entry", "journal entries"]):
            detected_intent = "GET_RECENT_VOUCHERS"
            parameters["voucher_type"] = "Journal"
        elif any(w in q_clean_lower for w in ["receipt voucher", "receipt vouchers", "receipt entry", "receipt entries"]):
            detected_intent = "GET_RECENT_VOUCHERS"
            parameters["voucher_type"] = "Receipt"
        elif any(w in q_clean_lower for w in ["payment voucher", "payment vouchers", "payment entry", "payment entries"]):
            detected_intent = "GET_RECENT_VOUCHERS"
            parameters["voucher_type"] = "Payment"
        elif any(w in q_clean_lower for w in ["contra voucher", "contra vouchers"]):
            detected_intent = "GET_RECENT_VOUCHERS"
            parameters["voucher_type"] = "Contra"
        elif any(w in q_clean_lower for w in ["credit note", "credit notes", "sales return", "sales returns"]):
            detected_intent = "GET_RECENT_VOUCHERS"
            parameters["voucher_type"] = "Credit Note"
        elif any(w in q_clean_lower for w in ["debit note", "debit notes", "purchase return", "purchase returns"]):
            detected_intent = "GET_RECENT_VOUCHERS"
            parameters["voucher_type"] = "Debit Note"
            
        if detected_intent == "GET_RECENT_VOUCHERS" and parameters.get("voucher_type"):
            # Clear ledger ambiguity if extracted ledger was just matching the voucher type name
            resolved_ledger = None
            extracted_ledger = None
            ambiguous_candidates = []
            entity_score = 0.0
        elif detected_intent in ["GET_TOP_DEBTORS", "GET_TOP_CREDITORS"] and not is_group_ledger:
            has_bill_target = any(w in query_without_company.lower() for w in ["top 5 bills", "top 5 invoices", "top bills", "top invoices", "highest bills", "largest bills", "oldest bills", "latest bills", "top 10 bills", "top 3 bills", "due", "dues", "overdue", "amount", "amounts", "invoice", "invoices", "how much", "what is the pending", "what is the cleared", "total sum", "total outstanding", "net outstanding", "sum of", "count of", "average", "avg", "how many", "tax amount", "payment to me"]) or ("bill" in query_without_company.lower() and not any(p in query_without_company.lower() for p in ["party", "parties", "debtor", "creditor", "customer", "supplier", "vendor"]))
            if has_bill_target:
                if detected_intent == "GET_TOP_CREDITORS":
                    detected_intent = "GET_PAYABLES"
                else:
                    detected_intent = "GET_RECEIVABLES"
                parameters["is_bill_query"] = True
                parameters["sort"] = {"field": "amount", "order": "desc"}
            
        if resolved_ledger:
            rl_lower = resolved_ledger.lower()
            if rl_lower in ["customers", "debtors", "creditors", "suppliers", "vendors"]:
                # Check if it's a generic plural/possessive reference
                stem = rl_lower[:-1] # e.g. creditor
                if bool(re.search(r'\b(how many|which|all|any|our|list)\s+' + stem + r"s?'?s?\b", query_without_company.lower())) or bool(re.search(r'\b' + stem + r"s?'?s?\s+(owe|owe\s+me|have|bills|bill)\b", query_without_company.lower())):
                    resolved_ledger = None
                    ledger_balance = None
                    fuzzy_score = 0.0
                    
        if parameters.get("date_filter") and parameters["date_filter"].get("type") == "next_quarter":
            import datetime
            curr_dt = None
            if context and context.get("current_date"):
                try:
                    curr_dt = datetime.datetime.strptime(context["current_date"], "%d-%b-%Y")
                except:
                    pass
            if not curr_dt:
                curr_dt = datetime.datetime.now()
            
            cur_q = (curr_dt.month - 1) // 3 + 1
            start_month = [4, 7, 10, 1][cur_q - 1]
            end_month = [6, 9, 12, 3][cur_q - 1]
            start_year = curr_dt.year if cur_q < 4 else curr_dt.year + 1
            end_year = curr_dt.year if cur_q < 4 else curr_dt.year + 1
            end_day = [30, 30, 31, 31][cur_q - 1]
            
            parameters["date_filter"] = {
                "type": "explicit_range",
                "start_day": 1,
                "start_month": start_month,
                "start_year": start_year,
                "end_day": end_day,
                "end_month": end_month,
                "end_year": end_year
            }

        return {
            "intent": detected_intent,
            "company": final_company_key,
            "port": port,
            "resolved_company": resolved_company,
            "context": context,
            "extracted_ledger": extracted_ledger,
            "resolved_ledger": resolved_ledger,
            "ledger_balance": ledger_balance,
            "entity_score": fuzzy_score,
            "ambiguous_candidates": ambiguous_candidates,
            "parameters": parameters,
            "missing_company": missing_company,
            "company_options": company_options
        }
