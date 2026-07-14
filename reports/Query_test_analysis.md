# NLP Tuning Progress Report

## Summary
Per your instructions, we proceeded with iteratively tuning the spaCy and structural extraction rules to handle edge cases found in the 230-query test suite. 

We took a highly strict approach: if even a single parameter (e.g., `count_only`, `sum_only`, `date_target`, `status_filter`) mismatches the strict ground truth established by our labeler subagent, the entire query fails.

## Tuning Phases Executed
1. **Initial Hotfixes (Previous Session):**
   - Normalizing `₹` for proper spaCy MONEY entity recognition.
   - Using regex word boundaries (`\bcount\b`) to prevent false positives on phrases like "on-account".
   - *Result: 4.81% -> 5.29% pass rate.*

2. **Phase 1 Structural Tuning:**
   - Improved `date_target` assignments: By default, Tally handles amounts with `date_target=bill_date`, but "payable", "receivable", "due", and "pending" queries require `date_target=due_date`.
   - Fixed `date_filter` mapping for "till date" and implicit "today" logic.
   - Repaired `GET_BILL_DETAILS` override bug: Modified `parse_query` so it only overrides the ONNX predicted intent to `GET_BILL_DETAILS` if a specific bill number (`document_ref`) is explicitly extracted, avoiding false overrides for queries like "list oldest 10 bills".
   - *Result: 5.29% -> 8.17% pass rate.*

3. **Phase 2 & 3 Advanced Logic Updates:**
   - Tuned `sum_only` vs `count_only` interactions: Complex compound queries (e.g. "how many bills... and what is the total amount?") require both to be `False` to force standard ledger list rendering with totals.
   - Tuned `status_filter`: Stop defaulting to `pending` unless explicitly queried, as `GET_RECEIVABLES` implies pending inherently.
   - Adjusted `sort` heuristics to correctly prioritize `bill_date` when words like "oldest" appear alongside "bills".
   - Prevented `age_filter` collision with `amount_filter` (e.g., stopping "90 days" from being parsed as amount `< 90`).
   - *Result: 8.17% -> 20.67% pass rate.*

4. **Phases 4-8 Aggressive Edge Case Elimination:**
   - Fixed `status_filter` by introducing negative lookaheads (e.g., distinguishing "due" and "dues" from "overdue" and "pending").
   - Expanded `date_target` logic to correctly interpret "paid", "getting", and "cash" as due_date anchors.
   - Prevented purely alphabetical strings (like "bill" or "reference") from being falsely tagged as `document_ref` by enforcing regex `\d` presence.
   - Fixed `amount_filter` boundaries for "greater than", "equal to", and comma-separated amounts (e.g. "25,000").
   - Implemented Tally-specific timeframes ("this quarter" = last 90 days, "next hy" = next 180 days, "FY 2025-26" = explicit_range).
   - Patched `limit` behavior to avoid capping to `1` when sorting logic uses modifiers like "first" or "list".
   - *Result: 20.67% -> 35.10% pass rate.*

5. **Phases 9-10 Deep Logic Tweaks:**
   - Improved `status_filter` by intelligently ignoring status when explicitly asking for a single bill details (`document_ref` is present) and correctly classifying mixed states like "outstanding as well as settled".
   - Refined `date_target` logic to correctly ignore targets for abstract metrics like `group` balances or `ageing` analysis.
   - Refined `sum_only` exceptions to correctly calculate single bills vs totals.
   - *Result: 35.10% -> 40.38% pass rate (84 True Passes).*

## Next Steps
The strict parsing has exposed how much implicit context Tally users rely on (e.g., "highest outstanding" means sorting by amount descending; "maximum overdue days" means sorting by due date ascending). 

We have successfully patched the core NLP engine rules and bumped the pass rate to **40.38%** (84 True Passes). To push this higher, we will need to continue iterative patching of `nlp_engine.py` using `run_test_suite.py` as our feedback loop, carefully analyzing the generated `mismatch_report.md` at each step.

Would you like me to continue the iterative rule tuning loop to push the pass rate even higher?