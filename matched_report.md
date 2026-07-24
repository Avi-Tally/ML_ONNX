# NLP Engine Matched Report (True Passes)

**Total Queries:** 727
**Passed:** 727
**Total FAQ/Unknown:** 84
**Pass Rate:** 100.00%

## Matches

### Query: `List the parties to whom I need to make the payment this week`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Oldest 10 Bills which are pending to receive today only above 1L `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Payables till date`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which vendors are due for payment this week?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What’s the total overdue payable beyond 30 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Identify the top 5 parties to whom the payment is pending for feb 2025`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 2, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `how many customers bills are due in the next 10 days and what is the total value?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 10}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Bills which are pending today starting with oldest billdate first for which the amount is less than 1L? `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the overdue payable amount?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show highest pending and cleared receivables bill amount for sundry debtors also give their GST status?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": true, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Debtors", "currency": null, "forex_only": false, "gst_status": true, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total Receivables amount less than 90 days `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receivable > 90 days ?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Customer dues and settled bills with over due amount less than 55000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 55000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `how many bills are due to receive in next 7 days.list in ascending order of bill date`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 7}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What’s my total outstanding receivable amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many customers owe me money right now?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What’s the total overdue receivable amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show me ageing of receivables by 30, 60, 90 days.`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "ageing_intervals": [30, 60, 90]}`

---

### Query: `Which customers have not paid for more than 60 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What’s the oldest unpaid bill in my books and what is the Tax amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Customer dues for today?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `highest receivable amount for creditors with overdue days less than a month`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `lowest receivable bill amount`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `top 5 parties with overdue receivables with maximum overdue days which have settled bills as well. `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `My total receivable `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Overdue receivables ?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Total pending receivables?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Outstanding of Sundry Creditors?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Display the last 7 days due outstanding of debtors`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 7}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `For Aquatech system, how many overdue bills are available till date and what is the total value of it `
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Aquatech system`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show me the overdue bills of the party AquaTech system`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Aquatech system`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `What is the outstanding amount for Anand Cargo ?`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Anand Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Net outstanding amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Display the last 7 days outstanding of the group Relaxo`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Relaxo`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 7}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `For Sukan Engineering , how many overdue bills are available till date and what is the total value of it `
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Sukan Engineering`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `What is the ageing of the outstanding amount based on the bill date for the 6 months from Jan 2025 for the ledger Rashmi Traders`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Rashmi Traders`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 30, "end_month": 6, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show me the overdue invoices of the Jagat`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `How much does Dew Cargo owe me?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Dew Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which suppliers bills are due today ?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which customer bills are pending to receive today `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `When are my collections due `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show me all invoices pending from Thermax Ltd`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many days overdue is bill 613 and what is the gst status?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": true, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Which vendors are due to receive today?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Whom should I follow up , Can you give me their address `
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the pending and cleared amount for Thermax Ltd`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": true, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `how much amount needs to be paid in next 15 days and receivables in next 15 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Amount of Bill no 308 for Abhishek and give the tax amount`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Abhishek`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "308", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List all the pending receivable bills number for Chemical Process Pvt LTD`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the total pending amount for Chemical Process Pipping Pvt Ltd for bill number MODI/25-26/956`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Chemical Process Pipping Pvt Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": null, "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Is there any pending amount for ledger DeltaFlow?`
- **Intent:** `GET_LEDGER_BALANCE`
- **Ledger:** `DeltaFlow`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the total outstanding balance for Ledger CECO?`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `CECO`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the total outstanding under Group Expenses`
- **Intent:** `GET_LEDGER_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `What is the payment status of Bill Number 1027 under Ledger Supreme ?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Supreme`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "1027", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Was Bill Number 104 settled fully for Varad engineers?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Varad engineers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "104", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show the opening amounts for payables with their totals`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Display the Opening Amount, pending and final balance of payables as on 02-03-2025`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": "02-Mar-2025", "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show receivable ageing for Thermax Ltd based on due date`
- **Intent:** `GET_AGEING`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Give payable ageing analysis for Sundry Creditors using bill date`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show ageing for Infosys Ltd for overdue receivables sorted by total pending amount ascending`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show ageing for Sundry Creditors where pending amount is greater than 500000`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 500000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `give the total number of bills pending to be paid to thermax in last 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `give the party who has the least number of pending bills in last 10 days`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 10}, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the voucher number linked to bill reference 613?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which voucher type was used for bill 613?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the balance outstanding for bill 613 as of today?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": "today", "is_bill_query": true, "document_ref": "613", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Has any partial payment been received against bill 613?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which ledger is associated with bill 613?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many days overdue is bill 613?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Are there any postdated outstanding bills?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List parties with postdated outstanding bills`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which parties have postdated receivables?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which parties have postdated payables?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show customer advances for Reliance Industries Ltd`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show supplier advances for Sundry Creditors`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Loans & Advances`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which ledgers have on-account receipts pending adjustment?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `GST Adjustment`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show groups with pending credit notes greater than ₹50,000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `List ledgers having on-account payments less than ₹25,000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Give adjustment summary for Reliance Industries Ltd and Infosys Ltd`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show adjustment balances for Debtors group sorted by voucher count descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `GST Adjustment`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Debtors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `Which groups have pending debit notes equal to ₹10,000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 10001.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `Show adjustment summary across all groups sorted by voucher count ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `GST Adjustment`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `Which receipts for Reliance Industries Ltd are still unallocated?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show pending customer advance transactions for Infosys Ltd`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List all unadjusted receipts across the company`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which payments are not linked to any bills?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show adjustment bills for Sundry Debtors`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `GST Adjustment`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Debtors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show old unallocated receipts for Customers sorted by voucher date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show pending credit note transactions for Jagat Ventures`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List adjustment vouchers with highest pending amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `GST Adjustment`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show adjustment transactions for Reliance Industries Ltd and Tata Motors`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show adjustment entries for Customers sorted by voucher date descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `GST Adjustment`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How much cash will I be getting this week?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `how much money owed to me is overdue?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `How much money should i be getting today?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `how much of my paymentsis overdue?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `how much payment to me is past due date?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `My total receivable `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `net amount receivable beyond due date?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Net outstanding amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `net outstanding payables?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `outstanding?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `payment that is late?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Till date payable ?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `todays outstanding`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `what are my outstanding's?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `what are my payables and receivables?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `what do i owe and how much i should get as of today?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `what do i owe as of today?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the overdue payable amount?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `what money i should get?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What’s the total overdue payable beyond 30 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Total Receivables amount`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total unadjusted payments`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total payables as of today`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What will be my payables by next month?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 30}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What will be my payables by next HY?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 180}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Give me the outstanding amount for FY 2025-26 and also show how much is overdue beyond 90 days.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2026}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show receivable outstanding`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show advanced received`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Overdue receivables ?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Overdue payables`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Total unadjusted receipts`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Display outstanding balances and also show monthly trend for the past 6 months.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 180}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Net Outstanding`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Display receivable outstanding between October 2024 and February 2025`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2024, "end_day": 28, "end_month": 2, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show company-wise outstanding and also identify whether the balance is receivable, payable, or net.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show company-wise outstanding for ModiChem company and also identify whether the balance is receivable, payable, or net.`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `ModiChem company`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show net outstanding company-wise and list parties with both receivable and payable balances.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `how much am i owed?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Give payable outstanding company-wise and list bills nearing due date within 7 days.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 7}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Debtors Bills expected to pay today only and which are settled yesterday?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `creditor's Bills which are due today for collections with overdue amount equal to 60000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 60001.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `latests 5 Bills which are due today for payments to Jagat?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Oldest 10 Bills which are pending to receive today only above 1L `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Bills which are pending today starting with oldest billdate first for which the amount is less than 1L? `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Customer dues and settled bills with over due amount less than 55000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 55000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Display the Opening Amount, pending and final balance of payables as on 02-03-2025`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": "02-Mar-2025", "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `For Aquatech system, how many overdue bills are available till date that crossed 60 days and what is the total value of it. Which bill has the highest overdue bills?`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Aquatech system`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `highest receivable amount for creditors with avg overdue days less than a month`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `highest receivable bill amount for debtors that has pending amount equal to 2L`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 200001.0}, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `how many bills are due to receive in next 7 days.list in ascending order of bill date`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 7}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `how many customers bills are due in the next 10 days and what is the total value? Which bill has the least overdue days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 10}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `How much does Anand Cargo owe me along with overdue date and how much is cleared?`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Anand Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `List due payable bills as on today with most overdue days on top?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `list the bills with new billdates on top due for payments and how much is cleared?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `lowest receivable amount only for gstr 2a creditors`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `gstr 2a creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": "reconciled", "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `top 5 parties with overdue receivables with maximum overdue days which have settled bills as well. `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Receivable > 90 days ?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show highest pending and cleared receivables bill amount for sundry debtors?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": true, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Debtors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total Receivables amount less than 90 days `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the outstanding amount for Mr Raj?`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Mr Raj`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `whats the most overdue date bill that i need to pay and that are cleared?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `which bill is highest amount among the pending ones?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the pending and cleared amount for Thermax Ltd`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": true, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What was the rate applied for Agru in Bill Number 049/24-25?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Agru`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "049/24-25", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What’s the oldest unpaid bill in my books?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many customers owe me money right now?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Identify the top 5 parties to whom the payment is pending for feb 2025 with highest average overdue days.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 2, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Identify the parties to whom the payment is pending with their total value in decreasing avg overdue days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `List the parties to whom I need to make the payment this week in decreasing pending amount`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `what amount should i get from debtors this week?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which customers have not paid for more than 60 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which vendors are due for payment this week?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Who are my top 10 debtors based on pending bills ?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Who should I follow up `
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total cleared bills for Reliance Industries Ltd`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "cleared", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total bills for Infosys Ltd including cleared bill`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How much is pending from Sundry Creditors? `
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How much is cleared from Sundry Creditors?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "cleared", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which party has the highest amount of cleared bills?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "cleared", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which party has cleared bill amount more than 50000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "cleared", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List suppliers who has both Overdue and cleared Payables in increasing order?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Give pending amount for credit card expenses also what is the cleared amount?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `credit card expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": true, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which parties under sundry creditors for goods import are overdue receivables?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show payable summary for GSTR2A Creditors`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `GSTR2A Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": "reconciled", "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `net outstanding for debtors with avg average overdue days less than 2 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 2}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `overdue payables for Sundry Creditors for this quarter`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `How much is pending from Sun Enterprises?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sun Enterprises`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Give payable ageing analysis for Sundry Creditors using bill date`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show ageing for Infosys Ltd for overdue receivables sorted by total pending amount ascending`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `List payable ageing for Debtors group based on bill date sorted by bill count`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Debtors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `Show ageing summary for Jagat and Thermax based on due date`
- **Intent:** `GET_AGEING`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show payable ageing for Agru with pending amount greater than 100000`
- **Intent:** `GET_AGEING`
- **Ledger:** `Agru`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List receivable ageing for sundry creditors where total pending amount is less than 50000`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show ageing analysis for Reliance Industries Ltd based on bill date with total pending amount equal to 250000`
- **Intent:** `GET_AGEING`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 250001.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Give payable ageing for Sundry Debtors sorted by bill count ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Debtors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show ageing for Sundry Creditors where pending amount is greater than 500000`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 500000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `give the total number of bills pending to be paid to thermax in last 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `give the party who has the least number of pending bills in last 10 days`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 10}, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is an overdue bill?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Difference between payable and receivable`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How does bill ageing work?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What does overdue amount mean in accounting?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `What is the purpose of bill-wise tracking in Tally?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Why do businesses monitor outstanding receivables?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the meaning of net outstanding?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What happens if payments are received on account but not adjusted against bills?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the difference between Sundry Debtors and Sundry Creditors?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How do overdue bills affect cash flow?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Why is ageing analysis important for businesses?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What does partially settled bill mean?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the purpose of maintaining bill references?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How are receivables different from revenue?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What are unadjusted receipts in outstanding reports?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Why do companies track supplier payables separately?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the meaning of overdue by days?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `How is pending amount calculated for a bill?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the impact of delayed customer payments on a business?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What are advanced receipts in accounting?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Why might outstanding reports become misleading?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the difference between closing balance and outstanding balance?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Is my receivable ageing getting worse compared to last quarter?`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which customers are taking the longest time to clear payments, and is that a risk for cash flow?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Are overdue receivables increasing this financial year?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Which group contributes the highest overdue outstanding, and should I be concerned?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true, "group_breakdown": true}`

---

### Query: `Do my payable trends indicate delayed vendor payments?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which parties consistently delay payments beyond 90 days?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Is my collection efficiency improving over the past 6 months?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 180}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which debtors should I prioritize for follow-up based on overdue amount?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Are my outstanding receivables unusually high compared to previous quarters?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which suppliers have the largest pending payable balances, and could this impact operations?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Are there too many old pending bills in Sundry Debtors?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Debtors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which customers have partially settled bills most frequently?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Is the company becoming more dependent on a few customers for receivables?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Are overdue bills concentrated within a specific customer group?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true, "group_breakdown": true}`

---

### Query: `Which ageing bucket has the highest outstanding amount, and what does it indicate?`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Is my net outstanding position improving month over month?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which ledgers have high outstanding but low recent collections?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Which creditor and debtor have pending, overdue receivables?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `What is the total receivable amount from clients?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List all outstanding bills for Acme Corp`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending customer bills above 50,000 rupees`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show receivables due this week`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Count of pending receivable bills for Zenith Solutions`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Zenith Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receivable bills starting with highest amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Outstanding receivable balance for Apex Infotech`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Apex Infotech`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Customer invoices pending collection today`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receivables from Global Logistics under 1 lakh`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Global Logistics`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show all unpaid sales bills for Metro Retail`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Metro Retail`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total pending collection amount for Q1 2025`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receivable bills due in next 15 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many customer bills are pending to be collected?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receivables for Dynamic Traders between 50k and 2L`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Dynamic Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 50000.0, "max": 200000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show due receivables sorted by due date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the receivable balance of Starlight Enterprises?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Starlight Enterprises`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List receivables till 31st March 2025`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total outstanding receivables for Horizon Media`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Horizon Media`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Fetch all pending debtor invoices for March 2025`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Are there any pending receivables above 5 lakhs?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 5.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show bill details for invoice REF-9942`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "-9942", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending sales bill status for Prime Agencies`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Prime Agencies`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total value of pending receivables due this month`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get customer bills due for collection today`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending debtor balance for Synergy Ltd`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Synergy Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List customer bills pending collection under invoice date filter`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Uncollected receivables for Apex Infotech exceeding 20000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Apex Infotech`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 20000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receivable summary for accounts in North Zone`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `North Zone`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the total payable amount to vendors?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show all pending bills payable to Tata Steel`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Tata Steel`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Vendor payables above 1 lakh`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Payable bills due this week`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Count of unpaid vendor bills for Reliance Industries`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Sort pending payables by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total amount payable to Larsen & Toubro`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Larsen & Toubro`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending vendor payments due today`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Payables for Thermax under 50,000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show all outstanding purchase bills for Aquatech System`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Aquatech system`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total payables due for month of April 2025`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 4, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Supplier bills due in next 7 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 7}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many purchase invoices are pending payment?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Payables to Siemens between 1L and 5L`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Siemens India`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 100000.0, "max": 500000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show pending payables sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is our net payable balance to Bosch Ltd?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Bosch Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Vendor payables till 30th June 2025`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 6, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total outstanding payables for General Engineering`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `General Engineering`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Fetch all supplier dues for May 2025`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 5, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending vendor bills greater than 2,00,000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 200000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Details for purchase reference PUR-2025-042`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "PUR-2025-042", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending payment status for ABB Power`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `ABB Power`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total value of supplier payables due next month`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 30}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List vendor bills due for payment today`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Outstanding payables for Schneider Electric`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Schneider Electric`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Vendor payables filtered by purchase invoice date`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Unpaid purchase bills for Tata Steel exceeding 75000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Tata Steel`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Supplier payables summary for West Zone`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `West Zone`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show bill ageing report for all customers`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Overdue bills beyond 30 days`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Bills pending for more than 90 days`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Ageing breakdown of outstanding receivables for Acme Corp`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Overdue payables aged between 30 and 60 days`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `What is the total overdue amount exceeding 60 days?`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Ageing analysis of vendor bills for Siemens`
- **Intent:** `GET_AGEING`
- **Ledger:** `Siemens India`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Bills overdue by less than 15 days`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `How many bills are overdue for more than 120 days?`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Ageing summary based on invoice date`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Overdue bills above 1 lakh aged > 45 days`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 45}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Oldest overdue bills listed first`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show ageing report as on 31-Mar-2025`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": "31-Mar-2025", "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Ageing profile of receivables for Metro Retail`
- **Intent:** `GET_AGEING`
- **Ledger:** `Metro Retail`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Bills pending 0 to 30 days old`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total overdue receivables past 180 days`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 180}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Age-wise outstanding report for Bosch Ltd`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Bosch Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show bills overdue between 60 and 90 days`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Count of overdue payables over 45 days`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 45}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Ageing report for bills under 50000`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Overdue invoices older than 15 days sorted by age`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 15}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `What is the sum of receivables overdue beyond 60 days for Zenith Solutions?`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Zenith Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Ageing slab summary for outstanding bills`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending invoices with overdue age > 30 days for Global Logistics`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Global Logistics`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show bills overdue by more than 10 days today`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 10}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Top 5 debtors by outstanding balance`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Who are the top 10 customers with highest overdue amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Top 3 debtors for Q1 2025`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Highest outstanding customer accounts`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 5 overdue debtors with balance over 1 lakh`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Top 10 debtors having bills overdue beyond 30 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `List top 5 receivables accounts by pending amount`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top customer balances as of 31st March 2025`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show top 5 debtors this month`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 3 customer accounts with largest pending dues`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 10 receivables by total pending balance today`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Identify top 5 clients owe us the most money`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 5 debtors for May 2025`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 5, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Who are our top 10 debtors exceeding 50k?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 5 customer outstandings ordered by amount`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 5 creditors by pending balance`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Who are the top 10 vendors we owe money to?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 3 suppliers to be paid in Q1 2025`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Highest pending vendor accounts`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 5 creditors with payables exceeding 2 lakhs`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 2.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 10 creditors having dues older than 60 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List top 5 payables accounts by total due amount`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top vendor balances as of 31st March 2025`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show top 5 creditors for this month`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 3 suppliers with largest outstanding bills`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 10 creditors by total pending payment today`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Identify top 5 suppliers needing payment priority`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 5 creditors for June 2025`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 6, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Who are our top 10 creditors above 1L?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 5 vendor payables ordered by amount`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Net outstanding after pdc for Reliance Industries`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show post-dated receipts for Reliance`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Receipt", "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Net payable after PDC for Tata Steel`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Tata Steel`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List post-dated payment vouchers for Siemens`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Siemens India`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Payment", "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the net receivable after pdc netting?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show post-dated sales invoices for Acme Corp`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Sales", "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Net outstanding payables including post dated cheques`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Post-dated purchase vouchers for Bosch Ltd`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Bosch Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Purchase", "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Post dated receipt status for Zenith Solutions`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Zenith Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Net receivable after PDC for Metro Retail`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Metro Retail`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show post dated cheques issued to Larsen & Toubro`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Larsen & Toubro`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Net outstanding balance for Thermax after pdc`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Post-dated journal entries for adjustment`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `GST Adjustment`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Journal", "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Net outstanding receivable after pdc deduction for Apex Infotech`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Apex Infotech`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show all Sales invoices for Delta Cargo`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Recent 5 Sales vouchers for Acme Corp`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List sales invoices above 50000 from last month`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Sales entries for Infosys in April 2025`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 4, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get all sales bills for Sunrise Enterprises`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Sunrise Enterprises`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many Sales vouchers were recorded this week?`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total sales amount for Apex Electronics this month`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Apex Electronics`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show sales invoice INV-2025-001 details`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "INV-2025-001", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get details of Sales Bill 402 for Reliance Industries`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "402", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending sales invoices for Vanguard Traders`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Vanguard Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Cleared sales bills for Delta Cargo`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 10 highest Sales invoices this year`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Sales entries recorded today`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Sales vouchers under ledger Global Logistics`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Global Logistics`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Count of sales invoices generated last month`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Details for sales voucher SL-904`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "SL-904", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Sales transactions exceeding 200000 in Q1`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 200000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Latest sales invoice for Wipro Technologies`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Wipro Technologies`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show sales invoice 782 status`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "782", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List all sales vouchers with amount under 10000`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Sales bills for Zenith Motors from last week`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Zenith Motors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Sum of sales vouchers billed to Orion Tech`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Orion Tech`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show sales voucher details for invoice reference SAL-105`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "SAL-105", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Oldest 5 sales invoices pending payment`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Sales transactions for Tata Motors yesterday`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Tata Motors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show all Purchase vouchers from Sharma Suppliers`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Sharma Suppliers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Recent 10 Purchase invoices for Acme Chemicals`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Acme Chemicals`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Purchase bills above 150000 in last month`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List purchase entries for Bharat Heavy Electricals in May 2025`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Bharat Heavy Electricals`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 5, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get purchase invoice PUR-2025-88 details`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "PUR-2025-88", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many purchase vouchers were entered yesterday?`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total purchase amount from Steel Authority this month`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Steel Authority`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show purchase bill 509 for National Traders`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `National Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "509", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending purchase invoices for Hindalco`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Hindalco`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Cleared purchase bills for Apex Polymers`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Apex Polymers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Purchase transactions for Bajaj Auto this week`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Bajaj Auto`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Count of purchase vouchers recorded in Q2`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show details of purchase voucher reference PB-332`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "PB-332", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Purchase entries exceeding 500000 from Mahindra`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Mahindra Finance`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 500000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Latest 3 purchase invoices from Larsen & Toubro`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Larsen & Toubro`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 3, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Check purchase bill reference 1044 status`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "1044", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Purchase vouchers with amount less than 20000`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 20000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Purchase entries recorded today`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Sum of all purchase invoices from Sterling Tools`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Sterling Tools`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Purchase bill reference P-771 details`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "P-771", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Oldest 10 purchase vouchers pending payment`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List purchase bills for Schneider Electric last year`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Schneider Electric`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show purchase invoices for Siemens India`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Siemens India`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Purchase vouchers in June 2025 above 100000`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 6, "year": 2025}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get total count of purchase invoices from Bosch`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Bosch Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": "Purchase", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List payment receipts from Reliance above 100000`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show all receipt vouchers for Tata Consultancy`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Tata Consultancy`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Recent 5 Receipt transactions from ICICI Bank`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `ICICI Bank`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receipt vouchers recorded last month`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total receipt sum from Infosys this week`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receipt voucher details for reference RCT-409`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "RCT-409", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many receipt vouchers were entered today?`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receipt entries for HDFC Bank in March 2025`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `HDFC Bank`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Cleared receipt vouchers for Delta Logistics`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Delta Logistics`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receipt voucher reference 882 details`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "882", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Latest receipt from Adani Enterprises`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Adani Enterprises`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 5 largest receipt transactions this year`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receipt vouchers exceeding 500000`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 500000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show receipt voucher reference REC-102`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "REC-102", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receipt entries from State Bank of India yesterday`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `State Bank of India`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Count of receipt vouchers in Q3`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Receipt vouchers for Sun Pharma above 50000`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Sun Pharma`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show payment receipt 305 for Mahindra Finance`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Mahindra Finance`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Sum of receipt vouchers received last week`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `All receipt vouchers under Customer Cash`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Customer Cash`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show payment vouchers to Axis Bank`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Axis Bank`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Recent 5 payment entries for Electricity Board`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Electricity Board`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Payment vouchers above 25000 in last month`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List payment entries to Rent Account in May 2025`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Rent Account`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 5, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Details of payment voucher reference PAY-551`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "PAY-551", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many payment vouchers were recorded this month?`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total payment amount to Vendor General this week`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Vendor General`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Check payment voucher 912 details`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "912", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Cleared payment entries for Petty Cash`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Petty Cash`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Latest payment voucher to Larsen & Toubro`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Larsen & Toubro`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Payment vouchers exceeding 100000 today`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show payment reference PV-2025-14`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "PV-2025-14", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 10 highest payment vouchers this year`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Payment entries to Salary Account yesterday`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Salary Account`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Count of payment vouchers in Q4`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Payment vouchers under 5000 rupees`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 5000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Details of payment voucher reference 667`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "667", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Sum of payment vouchers to Airtel Telecom`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Airtel Telecom`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Payment vouchers to Municipal Tax Dept from last week`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Municipal Tax Dept`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending payment vouchers for Freight Express`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Freight Express`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Journal vouchers in April 2025`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 4, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show all Journal vouchers for Depreciation Account`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Depreciation Account`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Recent 5 Journal entries recorded this month`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Journal adjustment vouchers above 50000`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `GST Adjustment`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get journal voucher JV-2025-09 details`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "JV-2025-09", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many Journal vouchers were posted yesterday?`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total amount in Journal vouchers for Provision Expenses`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Provision Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Journal voucher reference 441 details`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "441", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Journal entries for GST Adjustment last month`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `GST Adjustment`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Latest Journal voucher posted`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Journal vouchers exceeding 100000 in Q1`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show journal voucher reference JRN-703`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "JRN-703", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Journal entries for Audit Fee Provision`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Audit Fee Provision`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Count of journal vouchers this year`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Journal vouchers with amount under 10000`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Journal entries for TDS Payable account today`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `TDS Payable`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show details for Journal voucher 512`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "512", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List journal vouchers from last week`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Contra transactions for last month`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show all Contra vouchers between HDFC and ICICI`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `HDFC Bank`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Recent 5 Contra vouchers for Cash Account`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Cash Account`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Contra entries above 100000 recorded this week`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get contra voucher CTR-2025-04 details`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "CTR-2025-04", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many Contra transactions were created yesterday?`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total contra sum between Bank and Petty Cash`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `Petty Cash`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Contra voucher reference 208 details`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "208", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Contra entries in April 2025`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 4, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Latest Contra voucher recorded`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Contra transactions exceeding 500000`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 500000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show contra voucher reference CON-101`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "CON-101", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Contra vouchers recorded today`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Count of contra vouchers this month`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Contra entries for SBI Bank last year`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `SBI Bank`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Details of contra voucher 901`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "901", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Contra transfers under 20000 rupees`
- **Intent:** `GET_RECENT_VOUCHERS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 20000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show pending bills`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the total overdue amount?`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `List all unpaid items for last month`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show outstanding balance`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get pending bills list`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How much total amount is pending?`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show pending bills for Zenith Traders`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `Zenith Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List unpaid invoices of Apex Enterprises`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `Apex Enterprises`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the overdue balance for Global Solutions?`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Global Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Pending bills count`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show me all overdue items`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Total pending amount as of today`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Overdue bills list for this month`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Outstanding summary for last quarter`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show pending bills greater than 50000`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Top 5 overdue invoices by amount`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `List pending bills overdue by more than 30 days`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Count of unpaid bills older than 60 days`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show oldest 10 pending bills`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Bills pending clearance`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending bills between 10000 and 50000`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Check status of pending bill INV-2024-001`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "INV-2024-001", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Is invoice REF-9948 still pending?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "-9948", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show overdue bills sorted by bill date`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `List all pending bills for FY 2023-24`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2023, "end_day": 31, "end_month": 3, "end_year": 2024}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total overdue balance above 1 Lakh`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show pending invoices for Metro Logistics`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `Metro Logistics`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Overdue bill count for Alpha Tech`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Alpha Tech`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `What is the pending bill amount for Sunrise Corp?`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `Sunrise Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show all outstanding vouchers`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List pending items due this week`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Overdue amount for today`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show pending bills under 25000`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get outstanding bill report`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many bills are currently overdue?`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Total unpaid invoice count`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show pending bills overdue by less than 15 days`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `List unpaid bills due next week`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending bills for past 90 days`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show outstandings for Phoenix Retail`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Phoenix Retail`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Highest 3 pending bills`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total overdue amount for Q1`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show pending bills with amount equal to 100000`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100001.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List unpaid bills sorted by due date ascending`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show outstanding balance for Delta Systems`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Delta Systems`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Count of pending outstandings`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show pending bills from 1st April to 30th April`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List all overdue bills for Omega Electronics`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Omega Electronics`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show unpaid invoices for batch 2024`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the sum of all pending bills?`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get pending bill status for bill number BILL-505`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "BILL-505", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show top pending bills`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Overdue outstandings list`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Pending bills with age over 45 days`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 45}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show all unpaid bills for Orion Infotech`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `Orion Infotech`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the total pending bill count?`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List overdue bills for last financial year`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Show pending bills sorted by amount ascending`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Pending invoices summary`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show outstanding list above 500000`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 500000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show all unpaid items`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total overdue count for Zenith Traders`
- **Intent:** `GET_LEDGER_360`
- **Ledger:** `Zenith Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `Pending bill details for invoice 1045`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "1045", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show outstanding bills aged 30 to 60 days`
- **Intent:** `AMBIGUOUS_OUTSTANDINGS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is a ledger?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to record a payment voucher?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Payment", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Why use cost centers?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is a trial balance?`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to pass a sales entry in Tally?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is bank reconciliation?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Explain input tax credit under GST`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the difference between debit note and credit note?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to create a multi-currency ledger?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is FIFO method in inventory valuation?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to take backup of company data?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is TDS threshold for professional fees under section 194J?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to split company data in Tally?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What are contra vouchers used for?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to print invoice with QR code?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the shortcut key to delete a voucher?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to enable e-invoicing in Tally Prime?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is a Sundry Creditor?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to generate GSTR-3B report?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Why does my balance sheet not tally?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is bill-wise accounting?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to record purchase voucher with GST?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is cost category in Tally?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to alter ledger details?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is cash flow statement?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to apply interest calculation on overdue bills?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "overdue_only": true}`

---

### Query: `What is zero-rated supply in GST?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to pass journal entry for bad debts?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Journal", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is compound unit of measure?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to restore Tally backup data?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the shortcut key for inventory vouchers?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to configure discount column in sales invoice?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is a group in Tally accounting?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `How to track stock item serial numbers?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is RCM in GST?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to record advance payment to supplier?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Why use post-dated vouchers?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": "Receipt", "tax_filter": false, "pdc_only": true, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is work in progress (WIP) tracking?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to cancel a generated voucher?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is credit limit in ledger master?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to set up price list in Tally?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the default tally admin password reset procedure?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to export financial reports to PDF?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is trade discount vs cash discount?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to pass entry for salary payment?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is automated bank reconciliation?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to configure TCS in sales invoice?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Sales", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is godown management in Tally?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": "Bhiwandi Godown", "compare_companies": false}`

---

### Query: `How to record receipt voucher from customer?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Receipt", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is chart of accounts?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to view audit trail in Tally Prime?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is deferred tax asset?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to record contra voucher for cash deposit?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": "Contra", "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is physical stock verification entry?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to set budget and scenario control?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is HSN code requirement for e-way bill?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to pass debit note voucher?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is opening balance in ledger creation?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Why is cash ledger created by default?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How to enable multi-location inventory?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance for Indirect Expenses`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Closing balance of Duties & Taxes as of March 2025`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show trial balance of Group Capital Account`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Capital Goods`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `Trial balance report as of today`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Fetch trial balance for FY 2024-25`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2024, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get trial balance for Direct Expenses group`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `What is the net trial balance of Fixed Assets for last month?`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance of Sundry Creditors as on 31-03-2025`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": "31-Mar-2025", "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Creditors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Give me the trial balance for Current Liabilities`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Statutory Liabilities`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show detailed trial balance for Sales Account`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Sales Account`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance of Loans & Advances`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Loans & Advances`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the closing trial balance of Bank Accounts as of March 2025?`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Bank Accounts`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Display trial balance for Administrative Expenses`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Administrative Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance for Investments for Q4 2024`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What's the total trial balance sum for Operating Expenses?`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Operating Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Closing balances in Trial Balance for Branch/Divisions`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Branch/Divisions`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get TB for Provisions group as of 31 Dec 2024`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Provisions`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": "31-Dec-2024", "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `Show me trial balance for Audit Fees`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Audit Fees`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance summary of Purchase Accounts for this year`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Purchase Accounts`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Fetch closing trial balance of Goods and Services Tax`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Goods and Services Tax`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show trial balance for Depreciation ledger group`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Depreciation Account`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `Trial balance as on today for Cash-in-hand`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Cash-in-hand`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get trial balance for Indirect Incomes`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance listing for Group Direct Incomes as of Q1`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `Can I see the full trial balance for this month?`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show me trial balance for Reserves & Surplus`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Reserves & Surplus`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance of Secured Loans`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Secured Loans`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Give trial balance summary for Salary and Wages`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Salary and Wages`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance report for Travelling Expenses for January 2025`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Travelling Expenses`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 1, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the trial balance position for Rent Expenses?`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Rent Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Display trial balance for Freight and Cartage`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Freight and Cartage`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get overall trial balance figures as of yesterday`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance of Sundry Debtors group`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Sundry Debtors", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `Fetch trial balance for Printing & Stationery`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Printing & Stationery`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance of Legal and Professional Fees`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Legal and Professional Fees`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show trial balance for Electricity Charges for Q2 2024`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Electricity Charges`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get trial balance summary of Commission Received`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Commission Received`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance for GST Input Tax Credit`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `GST Input Tax Credit`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance position for GST Output Tax Liability`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `GST Output Tax Liability`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show trial balance for Miscellaneous Expenses`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Miscellaneous Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance report for Office Expenses for this month`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Office Expenses`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Fetch trial balance for Repairs and Maintenance`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Repairs and Maintenance`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance for Discount Allowed Account`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Discount Allowed Account`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance of Discount Received Account`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Discount Received Account`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Display trial balance for Bank Overdraft Account`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Bank Overdraft Account`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show trial balance for Telephone & Internet Expenses`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Telephone & Internet Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the trial balance for Conveyance Expenses?`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Conveyance Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance of Insurance Expenses as on March 2025`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Insurance Expenses`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": "Expenses", "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Give trial balance summary for Marketing and Advertising`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Marketing and Advertising`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show me the trial balance for Statutory Liabilities`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Statutory Liabilities`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance position for TDS Payable`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `TDS Payable`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get trial balance for Professional Tax Payable`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Professional Tax Payable`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance for Provident Fund Payable`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Provident Fund Payable`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the trial balance of ESIC Payable as of this month?`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `ESIC Payable`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance for Advance Tax Paid`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Advance Tax Paid`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show trial balance of Security Deposits`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Security Deposits`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance report for Loan to Directors`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Loan to Directors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Fetch trial balance for Capital Goods`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Capital Goods`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Trial balance for Plant & Machinery`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Plant & Machinery`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show trial balance for Vehicles Group`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Vehicles`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false, "group_breakdown": true}`

---

### Query: `Trial balance of Furniture & Fixtures as of 2025`
- **Intent:** `GET_TRIAL_BALANCE`
- **Ledger:** `Furniture & Fixtures`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for Raw Materials`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How much inventory of Finished Goods do we have?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total stock value for Packaging Materials`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Current stock position of Electronics items`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary as of March 2025`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show available quantity and value of Spare Parts`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Inventory summary for Chemical Raw Materials`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many stock items in Steel Pipes category have zero stock?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total stock valuation for Finished Goods as of today`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Get stock summary for Hardware components`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show stock report for Plastic Granules`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the total closing stock of Office Supplies?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Inventory details for Electrical Accessories for this month`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for Textiles & Fabrics`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How much stock do we have for Lubricants & Oils?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show inventory breakdown for Auto Components`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total stock value of Medical Supplies`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Give me the stock summary for Fasteners & Bolts`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Inventory status of Heavy Machinery Spares`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock balance for Printed Cartons`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show stock position of Raw Chemicals as on 31st March 2025`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary report for Trading Goods`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Count of stock items in Work in Progress category`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the total stock value of Consumer Goods?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `List all stock items under Safety Equipment with quantity`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for Plumbing Fixtures`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How much stock of Cables & Wires is available in warehouse?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": "Bhiwandi Godown", "compare_companies": false}`

---

### Query: `Stock valuation summary for Electronic Components as of FY 2024-25`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2024, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show current stock summary of Laboratory Reagents`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total stock value of Construction Materials`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock report for Hydraulic Fittings`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the available stock of Bearings & Bushings?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary of Aluminum Sheets for Q3 2024`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show stock status of Copper Wires`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Inventory total value for Agricultural Products`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for Solar Panels and Accessories`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many stock items of Rubber Hoses are in stock?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for HVAC Equipment`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show inventory valuation for Industrial Gases`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Current stock position of Paints & Coatings`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for Printing Inks`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the stock summary of Adhesives & Sealants?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total value of stock for Furniture Goods`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for Glass Bottles & Containers`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show stock of Metal Fasteners as of end of last month`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock position report for Food Ingredients`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How much inventory of Dairy Products is remaining?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for Frozen Foods`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total stock valuation of Beverages`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for Pharmaceutical Ingredients`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Inventory report for Surgical Instruments`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show stock summary of Personal Protective Equipment`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the total inventory value of Footwear Products?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for Garments & Ready-made Apparel`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock position for Leather Goods as of today`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `How many stock items in Toys & Games have stock greater than 100?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for Kitchenware & Utensils`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Total stock value of Home Appliances`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Stock summary for IT Hardware & Peripherals`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Inventory summary for Networking Cables`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `Show stock position of Computer Accessories`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

### Query: `What is the stock summary for Power Tools?`
- **Intent:** `GET_STOCK_SUMMARY`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "voucher_type": null, "tax_filter": false, "pdc_only": false, "include_cleared": false, "item_name": null, "stock_group": null, "stock_category": null, "group_name": null, "currency": null, "forex_only": false, "gst_status": null, "cost_center": null, "godown_name": null, "compare_companies": false}`

---

