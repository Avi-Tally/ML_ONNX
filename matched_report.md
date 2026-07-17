# NLP Engine Matched Report (True Passes)

**Total Queries:** 855
**Passed:** 855
**Total FAQ/Unknown:** 22
**Pass Rate:** 100.00%

## Matches

### Query: `List the parties to whom I need to make the payment this week`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Oldest 10 Bills which are pending to receive today only above 1L `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Payables till date`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Which vendors are due for payment this week?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What’s the total overdue payable beyond 30 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Identify the top 5 parties to whom the payment is pending for feb 2025`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 2, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `how many customers bills are due in the next 10 days and what is the total value?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 10}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Bills which are pending today starting with oldest billdate first for which the amount is less than 1L? `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the overdue payable amount?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show highest pending and cleared receivables bill amount for sundry debtors also give their GST status?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `sundry debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Total Receivables amount less than 90 days `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Receivable > 90 days ?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Customer dues and settled bills with over due amount less than 55000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 55000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `how many bills are due to receive in next 7 days.list in ascending order of bill date`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 7}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What’s my total outstanding receivable amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `How many customers owe me money right now?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": null}`

---

### Query: `What’s the total overdue receivable amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me ageing of receivables by 30, 60, 90 days.`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [30, 60, 90]}`

---

### Query: `Which customers have not paid for more than 60 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What’s the oldest unpaid bill in my books and what is the Tax amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Customer dues for today?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `highest receivable amount for creditors with overdue days less than a month`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `creditors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `lowest receivable bill amount`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `top 5 parties with overdue receivables with maximum overdue days which have settled bills as well. `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `My total receivable `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Overdue receivables ?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Total pending receivables?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Outstanding of Sundry Creditors?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Display the last 7 days due outstanding of debtors`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 7}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `For Aquatech system, how many overdue bills are available till date and what is the total value of it `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Aquatech system`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me the overdue bills of the party AquaTech system`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `AquaTech system`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `What is the outstanding amount for Anand Cargo ?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Anand Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Net outstanding amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Display the last 7 days outstanding of the group Relaxo`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Relaxo`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 7}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "group_breakdown": true}`

---

### Query: `For Sukan Engineering , how many overdue bills are available till date and what is the total value of it `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sukan Engineering`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `What is the ageing of the outstanding amount based on the bill date for the 6 months from Jan 2025 for the ledger Rashmi Traders`
- **Intent:** `GET_AGEING`
- **Ledger:** `Rashmi Traders`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 30, "end_month": 6, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me the overdue invoices of the Jagat`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `How much does Dew Cargo owe me?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Dew Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Which suppliers bills are due today ?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Which customer bills are pending to receive today `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `When are my collections due `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me all invoices pending from Thermax Ltd`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many days overdue is bill 613 and what is the gst status?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `Which vendors are due to receive today?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Whom should I follow up , Can you give me their address `
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the pending and cleared amount for Thermax Ltd`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `how much amount needs to be paid in next 15 days and receivables in next 15 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Amount of Bill no 308 for Abhishek and give the tax amount`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Abhishek`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "308", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List all the pending receivable bills number for Chemical Process Pvt LTD`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total pending amount for Chemical Process Pipping Pvt Ltd for bill number MODI/25-26/956`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Chemical Process Pipping Pvt Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": null, "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Is there any pending amount for ledger DeltaFlow?`
- **Intent:** `GET_LEDGER_BALANCE`
- **Ledger:** `DeltaFlow`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total outstanding balance for Ledger CECO?`
- **Intent:** `GET_LEDGER_BALANCE`
- **Ledger:** `CECO`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What is the total outstanding under Group Expenses`
- **Intent:** `GET_LEDGER_BALANCE`
- **Ledger:** `Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null, "group_breakdown": true}`

---

### Query: `What is the payment status of Bill Number 1027 under Ledger Supreme ?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Supreme`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "1027", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Was Bill Number 104 settled fully for Varad engineers?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Varad engineers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "104", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show the opening amounts for payables with their totals`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Display the Opening Amount, pending and final balance of payables as on 02-03-2025`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": "02-Mar-2025", "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show receivable ageing for Thermax Ltd based on due date`
- **Intent:** `GET_AGEING`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Give payable ageing analysis for Sundry Creditors using bill date`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show ageing for Infosys Ltd for overdue receivables sorted by total pending amount ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show ageing for Sundry Creditors where pending amount is greater than 500000`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 500000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `give the total number of bills pending to be paid to thermax in last 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `thermax`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending"}`

---

### Query: `give the party who has the least number of pending bills in last 10 days`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 10}, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the voucher number linked to bill reference 613?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Which voucher type was used for bill 613?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What is the balance outstanding for bill 613 as of today?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": "today", "is_bill_query": true, "document_ref": "613", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Has any partial payment been received against bill 613?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Which ledger is associated with bill 613?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `How many days overdue is bill 613?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `Are there any postdated outstanding bills?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List parties with postdated outstanding bills`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Which parties have postdated receivables?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Which parties have postdated payables?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show customer advances for Reliance Industries Ltd`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show supplier advances for Sundry Creditors`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Which ledgers have on-account receipts pending adjustment?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show groups with pending credit notes greater than ₹50,000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "group_breakdown": true}`

---

### Query: `List ledgers having on-account payments less than ₹25,000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Give adjustment summary for Reliance Industries Ltd and Infosys Ltd`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show adjustment balances for Debtors group sorted by voucher count descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "group_breakdown": true}`

---

### Query: `Which groups have pending debit notes equal to ₹10,000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 10001.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "group_breakdown": true}`

---

### Query: `Show adjustment summary across all groups sorted by voucher count ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "group_breakdown": true}`

---

### Query: `Which receipts for Reliance Industries Ltd are still unallocated?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show pending customer advance transactions for Infosys Ltd`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List all unadjusted receipts across the company`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Which payments are not linked to any bills?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show adjustment bills for Sundry Debtors`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show old unallocated receipts for Customers sorted by voucher date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Customers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show pending credit note transactions for Jagat Ventures`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Jagat Ventures`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List adjustment vouchers with highest pending amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show adjustment transactions for Reliance Industries Ltd and Tata Motors`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show adjustment entries for Customers sorted by voucher date descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Customers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `How much cash will I be getting this week?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `how much money owed to me is overdue?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "overdue_only": true}`

---

### Query: `How much money should i be getting today?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `how much of my paymentsis overdue?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "overdue_only": true}`

---

### Query: `how much payment to me is past due date?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `My total receivable `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `net amount receivable beyond due date?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Net outstanding amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `net outstanding payables?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `outstanding?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `payment that is late?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Till date payable ?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `todays outstanding`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `what are my outstanding's?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `what are my payables and receivables?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `what do i owe and how much i should get as of today?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `what do i owe as of today?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What is the overdue payable amount?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "overdue_only": true}`

---

### Query: `what money i should get?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `What’s the total overdue payable beyond 30 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Total Receivables amount`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Total unadjusted payments`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Total payables as of today`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `What will be my payables by next month?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 30}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What will be my payables by next HY?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 180}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Give me the outstanding amount for FY 2025-26 and also show how much is overdue beyond 90 days.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2026}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "overdue_only": true}`

---

### Query: `Show receivable outstanding`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show advanced received`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Overdue receivables ?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Overdue payables`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Total unadjusted receipts`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Display outstanding balances and also show monthly trend for the past 6 months.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 180}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Net Outstanding`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Display receivable outstanding between October 2024 and February 2025`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2024, "end_day": 28, "end_month": 2, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show company-wise outstanding and also identify whether the balance is receivable, payable, or net.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Show company-wise outstanding for ModiChem company and also identify whether the balance is receivable, payable, or net.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `ModiChem company`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Show net outstanding company-wise and list parties with both receivable and payable balances.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `how much am i owed?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Give payable outstanding company-wise and list bills nearing due date within 7 days.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 7}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Debtors Bills expected to pay today only and which are settled yesterday?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `creditor's Bills which are due today for collections with overdue amount equal to 60000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 60001.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `latests 5 Bills which are due today for payments to Jagat?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Oldest 10 Bills which are pending to receive today only above 1L `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Bills which are pending today starting with oldest billdate first for which the amount is less than 1L? `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Customer dues and settled bills with over due amount less than 55000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 55000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Display the Opening Amount, pending and final balance of payables as on 02-03-2025`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": "02-Mar-2025", "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `For Aquatech system, how many overdue bills are available till date that crossed 60 days and what is the total value of it. Which bill has the highest overdue bills?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Aquatech system`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `highest receivable amount for creditors with avg overdue days less than a month`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `creditors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `highest receivable bill amount for debtors that has pending amount equal to 2L`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 200001.0}, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `how many bills are due to receive in next 7 days.list in ascending order of bill date`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 7}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `how many customers bills are due in the next 10 days and what is the total value? Which bill has the least overdue days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 10}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `How much does Anand Cargo owe me along with overdue date and how much is cleared?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Anand Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "overdue_only": true}`

---

### Query: `List due payable bills as on today with most overdue days on top?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `list the bills with new billdates on top due for payments and how much is cleared?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `lowest receivable amount only for gstr 2a creditors`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `gstr 2a creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `top 5 parties with overdue receivables with maximum overdue days which have settled bills as well. `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Receivable > 90 days ?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show highest pending and cleared receivables bill amount for sundry debtors?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `sundry debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Total Receivables amount less than 90 days `
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `What is the outstanding amount for Mr Raj?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Mr Raj`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `whats the most overdue date bill that i need to pay and that are cleared?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "overdue_only": true}`

---

### Query: `which bill is highest amount among the pending ones?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the pending and cleared amount for Thermax Ltd`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `What was the rate applied for Agru in Bill Number 049/24-25?`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Agru`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "049/24-25", "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What’s the oldest unpaid bill in my books?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many customers owe me money right now?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": null}`

---

### Query: `Identify the top 5 parties to whom the payment is pending for feb 2025 with highest average overdue days.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 2, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Identify the parties to whom the payment is pending with their total value in decreasing avg overdue days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List the parties to whom I need to make the payment this week in decreasing pending amount`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `what amount should i get from debtors this week?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `debtors`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Which customers have not paid for more than 60 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Which vendors are due for payment this week?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Who are my top 10 debtors based on pending bills ?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who should I follow up `
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Total cleared bills for Reliance Industries Ltd`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "cleared"}`

---

### Query: `Total bills for Infosys Ltd including cleared bill`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `How much is pending from Sundry Creditors? `
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `How much is cleared from Sundry Creditors?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "cleared"}`

---

### Query: `Which party has the highest amount of cleared bills?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Which party has cleared bill amount more than 50000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List suppliers who has both Overdue and cleared Payables in increasing order?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `Give pending amount for credit card expenses also what is the cleared amount?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `credit card expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Which parties under sundry creditors for goods import are overdue receivables?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `sundry creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show payable summary for GSTR2A Creditors`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `GSTR2A Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `net outstanding for debtors with avg average overdue days less than 2 days`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `debtors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 2}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null, "overdue_only": true}`

---

### Query: `overdue payables for Sundry Creditors for this quarter`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `How much is pending from Sun Enterprises?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sun Enterprises`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Give payable ageing analysis for Sundry Creditors using bill date`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show ageing for Infosys Ltd for overdue receivables sorted by total pending amount ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List payable ageing for Debtors group based on bill date sorted by bill count`
- **Intent:** `GET_AGEING`
- **Ledger:** `Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "group_breakdown": true}`

---

### Query: `Show ageing summary for Jagat and Thermax based on due date`
- **Intent:** `GET_AGEING`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show payable ageing for Agru with pending amount greater than 100000`
- **Intent:** `GET_AGEING`
- **Ledger:** `Agru`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List receivable ageing for sundry creditors where total pending amount is less than 50000`
- **Intent:** `GET_AGEING`
- **Ledger:** `sundry creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show ageing analysis for Reliance Industries Ltd based on bill date with total pending amount equal to 250000`
- **Intent:** `GET_AGEING`
- **Ledger:** `Reliance Industries Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 250001.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Give payable ageing for Sundry Debtors sorted by bill count ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show ageing for Sundry Creditors where pending amount is greater than 500000`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 500000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `give the total number of bills pending to be paid to thermax in last 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `thermax`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": true, "sum_only": false, "status_filter": "pending"}`

---

### Query: `give the party who has the least number of pending bills in last 10 days`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 10}, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is an overdue bill?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Difference between payable and receivable`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `How does bill ageing work?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What does overdue amount mean in accounting?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending", "overdue_only": true}`

---

### Query: `What is the purpose of bill-wise tracking in Tally?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Why do businesses monitor outstanding receivables?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What is the meaning of net outstanding?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `What happens if payments are received on account but not adjusted against bills?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the difference between Sundry Debtors and Sundry Creditors?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `How do overdue bills affect cash flow?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Why is ageing analysis important for businesses?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What does partially settled bill mean?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What is the purpose of maintaining bill references?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `How are receivables different from revenue?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What are unadjusted receipts in outstanding reports?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Why do companies track supplier payables separately?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What is the meaning of overdue by days?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `How is pending amount calculated for a bill?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the impact of delayed customer payments on a business?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What are advanced receipts in accounting?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Why might outstanding reports become misleading?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What is the difference between closing balance and outstanding balance?`
- **Intent:** `UNKNOWN`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Is my receivable ageing getting worse compared to last quarter?`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Which customers are taking the longest time to clear payments, and is that a risk for cash flow?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Are overdue receivables increasing this financial year?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Which group contributes the highest overdue outstanding, and should I be concerned?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true, "group_breakdown": true}`

---

### Query: `Do my payable trends indicate delayed vendor payments?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Which parties consistently delay payments beyond 90 days?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Is my collection efficiency improving over the past 6 months?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 180}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Which debtors should I prioritize for follow-up based on overdue amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Are my outstanding receivables unusually high compared to previous quarters?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Which suppliers have the largest pending payable balances, and could this impact operations?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Are there too many old pending bills in Sundry Debtors?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Which customers have partially settled bills most frequently?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Is the company becoming more dependent on a few customers for receivables?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Are overdue bills concentrated within a specific customer group?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true, "group_breakdown": true}`

---

### Query: `Which ageing bucket has the highest outstanding amount, and what does it indicate?`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": null, "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Is my net outstanding position improving month over month?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Which ledgers have high outstanding but low recent collections?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Which creditor and debtor have pending, overdue receivables?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me ageing of 40, 50, 65 days for receivables from Acme Corp between Jan and March 2025 based on bill date`
- **Intent:** `GET_AGEING`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "ageing_intervals": [40, 50, 65]}`

---

### Query: `List all receivable bills for the next quarter greater than 100000 sorted by amount descending showing top 10`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending payables in the last 45 days overdue by more than 30 days based on due date with amount less than 50000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me payments I have to make for Reliance Industries in March 2025 showing top 10 bill wise`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Get details for bill INV-100 for Sundry Debtors in March 2025`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "INV-100", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Pending payables for Reliance Industries this week overdue by more than 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show receivables for Sundry Debtors in the last 45 days based on due date showing top 20 sorted by due date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": null, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Get details for bill 613 based on due date sorted by bill date ascending`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Ageing analysis of 40, 50, 65 days for Chemical Process Pvt LTD till today`
- **Intent:** `GET_AGEING`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `Who do I owe money to for Chemical Process Pvt LTD showing top 20 bill wise`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Get details for bill MODI/25-26/956 for Thermax Ltd till today based on due date showing top 5`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Get details for bill MODI/25-26/956 for Acme Corp based on bill date`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List all receivable bills for Thermax Ltd this week overdue by more than 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Get details for bill MODI/25-26/956 for Infosys Ltd sorted by due date descending`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Get details for bill BILL/2026/01 for the next quarter with amount greater than 50000 sorted by bill date descending`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": "BILL/2026/01", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show top debtors between Jan and March 2025 with amount greater than 100000 sorted by due date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Ageing analysis this week based on bill date sorted by amount ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Pending collections for the next quarter less than 15 days old with amount less than 50000 showing top 5`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show top debtors for the next quarter`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List payables for Jagat in March 2025 overdue by more than 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Ageing analysis of 40, 50, 65 days for Infosys Ltd in March 2025 sorted by bill date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `Pending payables in the last 45 days less than 15 days old with amount less than 250000 sorted by amount ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show top creditors based on due date showing top 10`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show top creditors`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me payments I have to make for Infosys Ltd till today based on bill date with amount less than 50000 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Give me the ageing buckets for Thermax Ltd this week with amount less than 100000 showing top 20`
- **Intent:** `GET_AGEING`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Get details for bill MODI/25-26/956 for Chemical Process Pvt LTD for the next quarter sorted by amount descending`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List all receivable bills for Sundry Debtors based on bill date less than 15 days old`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What money is owed to me this week less than 15 days old showing top 20`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Get details for bill 613 for Infosys Ltd this week based on bill date`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What is the ageing of 15, 30, 45, 60 days till today based on due date with amount greater than 250000 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [15, 30, 45, 60]}`

---

### Query: `Show receivables based on due date less than 15 days old showing top 10 bill wise`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending payables for Acme Corp for the next quarter less than 15 days old sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who do I owe money to this week with amount greater than 50000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the ageing of 15, 30, 45, 60 days for Infosys Ltd between Jan and March 2025 based on due date`
- **Intent:** `GET_AGEING`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [15, 30, 45, 60]}`

---

### Query: `Show receivables for Sundry Debtors in the last 45 days based on due date overdue by more than 30 days with amount greater than 100000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Pending collections less than 15 days old with amount greater than 100000 sorted by amount ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Get details for bill MODI/25-26/956 for Chemical Process Pvt LTD sorted by amount ascending`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What is the ageing based on due date with amount greater than 250000 showing top 10`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show top debtors in March 2025 based on bill date sorted by amount ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show receivables for Reliance Industries showing top 5 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Ageing analysis of 30 60 90 for Sundry Debtors showing top 5 sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [5, 30, 60, 90]}`

---

### Query: `Who do I owe money to this week less than 15 days old with amount less than 100000 showing top 5 bill wise`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What money is owed to me for Chemical Process Pvt LTD between Jan and March 2025 based on due date overdue by more than 30 days showing top 20`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me the ageing buckets for Acme Corp in March 2025`
- **Intent:** `GET_AGEING`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List all receivable bills for Sundry Debtors in the last 45 days based on bill date sorted by amount ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending collections based on bill date`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who do I owe money to for the next quarter overdue by more than 30 days with amount greater than 50000 showing top 10`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me payments I have to make based on due date less than 15 days old bill wise`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Give me the ageing buckets`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Get details for bill MODI/25-26/956 for Reliance Industries till today`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Who do I owe money to in the last 45 days bill wise`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show top creditors till today based on bill date sorted by due date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Pending payables this week based on due date overdue by more than 30 days showing top 20 bill wise`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Pending payables this week sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Get details for bill MODI/25-26/956 for the next quarter based on bill date`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Pending collections this week based on bill date`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who do I owe money to based on bill date showing top 5 sorted by due date ascending bill wise`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending payables with amount less than 100000 sorted by bill date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List all receivable bills for Reliance Industries based on bill date less than 15 days old`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending collections for Thermax Ltd sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who do I owe money to this week with amount less than 100000 bill wise`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Ageing analysis of 30 60 90 for the next quarter based on due date showing top 20`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": null, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [20, 30, 60, 90]}`

---

### Query: `Pending payables for the next quarter based on due date sorted by due date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending collections based on bill date sorted by due date ascending bill wise`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List all receivable bills for Jagat till today less than 15 days old with amount less than 250000 showing top 5 sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show receivables for Thermax Ltd showing top 20 bill wise`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who do I owe money to based on due date with amount less than 50000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show ageing of 40, 50, 65 days in the last 45 days based on due date with amount less than 250000 showing top 5 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `Get details for bill MODI/25-26/956 for Infosys Ltd in the last 45 days`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Pending payables for Jagat till today overdue by more than 30 days with amount greater than 50000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Get details for bill MODI/25-26/956 for the next quarter based on due date with amount greater than 50000 sorted by due date ascending`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Give me the ageing buckets of 15, 30, 45, 60 days based on bill date with amount less than 250000 sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [15, 30, 45, 60]}`

---

### Query: `List all receivable bills for Sundry Debtors this week based on bill date overdue by more than 30 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Get details for bill MODI/25-26/956 between Jan and March 2025`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show ageing`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Pending collections for the next quarter based on bill date with amount greater than 250000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show top debtors between Jan and March 2025 based on bill date`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show receivables in March 2025 with amount less than 50000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Get details for bill MODI/25-26/956 for Reliance Industries till today based on due date with amount less than 250000 showing top 5 sorted by due date ascending`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 5, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": "MODI/25-26/956", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show top creditors for the next quarter with amount less than 250000 showing top 5`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Who do I owe money to for Thermax Ltd based on due date with amount less than 100000 sorted by amount ascending bill wise`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show top debtors till today sorted by bill date descending`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show top debtors for the next quarter based on bill date`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show top debtors based on bill date`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Pending collections for Thermax Ltd based on bill date`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What money is owed to me till today based on bill date with amount greater than 100000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Get details for bill 613 for Sundry Debtors based on due date showing top 10 sorted by due date ascending`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": "613", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show receivables based on bill date less than 15 days old`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Ageing analysis of 40, 50, 65 days for the next quarter based on bill date`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `What is the ageing of 30 60 90 till today based on due date`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [30, 60, 90]}`

---

### Query: `Who do I owe money to based on due date with amount less than 250000 bill wise`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show top debtors with amount greater than 100000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show top creditors between Jan and March 2025 based on bill date with amount less than 50000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Get details for bill BILL/2026/01 this week with amount less than 250000 sorted by bill date descending`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": "BILL/2026/01", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What money is owed to me for Jagat in the last 45 days based on due date with amount greater than 250000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Get details for bill 308 for Reliance Industries between Jan and March 2025 based on due date`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "308", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List all receivable bills for Infosys Ltd between Jan and March 2025 based on due date with amount greater than 100000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Give me the ageing buckets for Acme Corp with amount less than 100000 sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Get details for bill INV-100 in the last 45 days based on bill date sorted by due date descending`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": "INV-100", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show ageing for Infosys Ltd based on due date`
- **Intent:** `GET_AGEING`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show top debtors based on due date with amount greater than 250000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show top creditors based on bill date showing top 20`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Pending payables for the next quarter based on due date`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show ageing of 30 60 90 between Jan and March 2025 showing top 5`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [5, 30, 60, 90]}`

---

### Query: `Pending collections till today less than 15 days old with amount less than 100000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the ageing of 30 60 90 for Acme Corp showing top 10`
- **Intent:** `GET_AGEING`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 30, 60, 90]}`

---

### Query: `List payables for Infosys Ltd between Jan and March 2025 overdue by more than 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `What is the ageing of 0-30, 31-60, 61-90 for Jagat with amount less than 100000`
- **Intent:** `GET_AGEING`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [0, 30, 31, 60, 61, 90]}`

---

### Query: `Give me the ageing buckets till today based on due date`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Pending payables between Jan and March 2025 overdue by more than 30 days with amount less than 50000 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show receivables in the last 45 days based on bill date overdue by more than 30 days with amount less than 50000 bill wise`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show top creditors between Jan and March 2025 sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Give me the ageing buckets of 0-30, 31-60, 61-90 in March 2025 showing top 10`
- **Intent:** `GET_AGEING`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [0, 10, 30, 31, 60, 61, 90]}`

---

### Query: `Pending collections in March 2025 based on due date overdue by more than 30 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `What money is owed to me for Thermax Ltd this week showing top 5 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show top debtors based on bill date`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Get details for bill 308 for Jagat`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "308", "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show top debtors with amount less than 100000`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Get details for bill INV-100 based on bill date`
- **Intent:** `GET_BILL_DETAILS`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": "INV-100", "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `What money is owed to me showing top 5`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List payables for Sundry Debtors based on due date less than 15 days old bill wise`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List payables till today less than 15 days old`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Ageing analysis for Reliance Industries this week sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List all receivable bills this week sorted by bill date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Settled bills with overdue amounts for delta cargo above 100000 and less than 60 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 3 unpaid bills marked as cleared for delta cargo above 75000 and older than 60 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 unpaid bills marked as cleared below 150000 and less than 30 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Unpaid bills marked as cleared for acme corp above 75000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 unpaid bills marked as cleared for acme corp below 75000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 fully settled bills with late payment dues for acme corp below 10000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Settled bills with overdue amounts for acme corp above 10000 and less than 30 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 10 paid bills with remaining overdue balance for delta cargo above 75000 and less than 120 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 120}, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 15 pending vs paid bills above 10000 and less than 60 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending vs paid bills for sunrise industries below 25000 and less than 30 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 settled accounts with pending dues for global traders above 75000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 settled bills with overdue amounts below 75000 and older than 45 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 45}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Unpaid bills marked as cleared below 50000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 settled accounts with pending dues below 10000 and less than 90 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 pending balances for cleared customers for sunrise industries above 25000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Settled accounts with pending dues above 150000 and older than 120 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Paid bills with remaining overdue balance for tech solutions below 150000 and older than 120 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 10 pending vs paid bills for delta cargo below 75000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 invoices paid yesterday but pending today for global traders below 25000 and less than 15 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 settled accounts with pending dues below 25000 and less than 30 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Paid bills with remaining overdue balance below 75000 and less than 120 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 120}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Settled bills with overdue amounts below 25000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 15 overdue amount on settled bills for acme corp below 25000 and less than 90 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 3 overdue amount on settled bills for tech solutions below 25000 and less than 90 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 10 pending amounts on paid invoices for acme corp below 25000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 paid bills with remaining overdue balance for global traders above 100000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 15 paid bills with remaining overdue balance for acme corp below 150000 and less than 60 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 10 cleared vs pending invoices for global traders above 150000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 unpaid bills marked as cleared below 10000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 overdue amount on settled bills for tech solutions above 150000 and less than 60 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 10 cleared dues showing as pending for global traders below 100000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 pending vs paid bills below 75000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 unpaid dues that were cleared yesterday above 50000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Partially cleared invoices still pending for acme corp above 100000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Invoices paid yesterday but pending today for delta cargo below 75000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 overdue amount on settled bills for sunrise industries above 50000 and less than 30 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 5 cleared dues showing as pending for tech solutions above 25000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 pending balances for cleared customers below 25000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 overdue amount on settled bills below 150000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Pending vs paid bills above 50000 and less than 120 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 120}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 invoices paid yesterday but pending today for delta cargo above 10000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 unpaid dues that were cleared yesterday for sunrise industries below 150000 and less than 30 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Partially cleared invoices still pending above 75000 and older than 90 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending balances for cleared customers above 10000 and older than 120 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Top 5 partially cleared invoices still pending for tech solutions above 150000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Overdue amount on settled bills for global traders below 50000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 3 cleared dues showing as pending for sunrise industries above 100000 and less than 15 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 settled bills with overdue amounts for delta cargo above 150000 and less than 120 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 120}, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Unpaid bills marked as cleared for global traders below 150000 and less than 45 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Invoices paid yesterday but pending today for tech solutions above 10000 and less than 120 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": "<", "days": 120}, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 paid bills with remaining overdue balance for acme corp above 150000 and older than 30 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Unpaid bills marked as cleared above 10000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending balances for cleared customers below 150000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Settled bills with overdue amounts for acme corp below 150000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 15 unpaid dues that were cleared yesterday for tech solutions above 50000 and less than 45 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 cleared vs pending invoices for delta cargo below 10000 and older than 45 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 45}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 partially cleared invoices still pending for global traders above 10000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 unpaid dues that were cleared yesterday for sunrise industries above 25000 and less than 60 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending amounts on paid invoices for delta cargo below 75000 and older than 45 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 45}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 pending amounts on paid invoices below 75000 and older than 30 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 invoices paid yesterday but pending today above 150000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 unpaid bills marked as cleared below 100000 and less than 15 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 overdue amount on settled bills above 25000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Pending amounts on paid invoices for sunrise industries above 100000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 overdue amount on settled bills for delta cargo above 25000 and less than 45 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Unpaid bills marked as cleared for acme corp below 100000 and older than 15 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 cleared vs pending invoices for acme corp below 50000 and less than 90 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 unpaid dues that were cleared yesterday above 10000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 settled accounts with pending dues for global traders below 150000 and older than 60 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Settled bills with overdue amounts below 50000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Pending amounts on paid invoices below 100000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 settled bills with overdue amounts below 50000 and less than 15 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Cleared dues showing as pending for sunrise industries below 50000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Top 3 settled bills with overdue amounts below 50000 and older than 45 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 45}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 5 pending vs paid bills below 75000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending vs paid bills above 100000 and older than 30 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Overdue amount on settled bills for acme corp above 25000 and older than 90 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 3 pending balances for cleared customers for acme corp above 10000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending balances for cleared customers for global traders below 50000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Top 10 pending balances for cleared customers for acme corp below 25000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 unpaid dues that were cleared yesterday for sunrise industries above 50000 and older than 60 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Cleared vs pending invoices for acme corp above 10000 and older than 120 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending amounts on paid invoices for delta cargo below 150000 and less than 15 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 partially cleared invoices still pending for delta cargo below 25000 and older than 60 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 cleared vs pending invoices for acme corp below 50000 and older than 120 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 cleared dues showing as pending above 25000 and less than 15 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Settled accounts with pending dues for acme corp below 100000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Settled accounts with pending dues below 150000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Settled accounts with pending dues above 50000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Top 10 unpaid bills marked as cleared for sunrise industries above 10000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending vs paid bills for delta cargo above 50000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 paid bills with remaining overdue balance for acme corp below 100000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Unpaid dues that were cleared yesterday for sunrise industries above 75000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": "pending"}`

---

### Query: `Top 15 fully settled bills with late payment dues for delta cargo below 25000 and less than 60 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Pending vs paid bills below 150000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 cleared dues showing as pending for tech solutions above 75000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 unpaid dues that were cleared yesterday for sunrise industries above 75000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 fully settled bills with late payment dues for delta cargo below 75000 and older than 120 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Top 5 unpaid bills marked as cleared for delta cargo below 25000 and less than 120 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 120}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Fully settled bills with late payment dues for global traders below 100000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Top 3 paid bills with remaining overdue balance above 75000 and older than 90 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 3 cleared dues showing as pending below 10000 and older than 90 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Invoices paid yesterday but pending today above 100000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Cleared vs pending invoices below 75000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 settled bills with overdue amounts for acme corp above 10000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Cleared vs pending invoices below 150000 and older than 120 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 pending vs paid bills below 10000 and older than 15 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 fully settled bills with late payment dues for global traders below 25000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Top 15 cleared vs pending invoices above 10000 and older than 15 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 unpaid bills marked as cleared for delta cargo above 50000 and older than 45 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 45}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 overdue amount on settled bills for sunrise industries below 25000 and less than 45 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 10 pending balances for cleared customers for global traders above 100000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 fully settled bills with late payment dues for global traders above 25000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Top 10 pending vs paid bills for delta cargo below 150000 and less than 90 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 settled bills with overdue amounts for tech solutions above 10000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 15 pending balances for cleared customers for sunrise industries above 25000 and older than 90 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 overdue amount on settled bills below 10000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 15 cleared dues showing as pending below 150000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 overdue amount on settled bills for sunrise industries below 10000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Top 5 pending balances for cleared customers for delta cargo below 10000 and older than 120 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 3 pending balances for cleared customers for sunrise industries above 25000 and less than 90 days?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sunrise Industries`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 10 pending amounts on paid invoices for global traders above 25000 and older than 15 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 5 unpaid dues that were cleared yesterday for delta cargo below 50000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Delta Cargo`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Top 15 settled accounts with pending dues for global traders below 50000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Unpaid bills marked as cleared for global traders above 25000 and older than 45 days?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Traders`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 45}, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many pending receivable bills are there this week overdue by more than 30 days and what is their total value earliest due date first?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List the top 50 pending payable bills of Acme Corp this week pending for over 60 days less than 25k sorted by highest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 50, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me all bills I owe till today above 50,000 earliest due date first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show the Highest cleared purchase invoices for Tech Solutions greater than 1L .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all unpaid payables for March 2025 older than 90 days less than 25k sorted by highest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many receivables are there till today pending for over 60 days above 50,000 and what is their total value earliest due date first?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me all unpaid invoices to receive this week greater than 1L oldest first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 50 cleared bills I owe this week with age less than 15 days latest due date first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": 50, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Oldest settled invoices to receive till today pending for over 60 days above 50,000 .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Newest settled invoices to receive for Global Exports till today above 50,000 .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Global Exports`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Lowest settled sales invoices this week with age less than 15 days above 50,000 .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `How many cleared payables are there this week overdue by more than 30 days less than 25k and what is their total value newest first?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "overdue_only": true}`

---

### Query: `Show me all pending receivable bills related to John Doe for March 2025 older than 90 days less than 25k sorted by highest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `John Doe`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many payables are there till today pending for over 60 days and what is their total value earliest due date first?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show the Oldest settled purchase invoices for Global Exports this week older than 90 days .`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Exports`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 15 cleared receivables of John Doe for March 2025 pending for over 60 days less than 25k sorted by lowest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `John Doe`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 15, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Oldest cleared receivables for Sundry Creditors in the next 15 days .`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": null, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 10 unpaid receivable bills of Sundry Creditors older than 90 days latest due date first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": 10, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 15 payables of Global Exports in the last 30 days older than 90 days above 50,000 latest due date first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Exports`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 15, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `How many purchase invoices are there in the next 15 days above 50,000 and what is their total value sorted by lowest amount?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `How many pending payable bills for Sundry Creditors are there and what is their total value sorted by lowest amount?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 50 pending bills customers owe me of Sundry Creditors till today older than 90 days above 50,000 latest due date first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 50, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me all settled bills I owe this week earliest due date first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all settled bills to pay for March 2025 sorted by highest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 15 pending payable bills of Tech Solutions in the last 30 days older than 90 days above 50,000 newest first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 15, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many bills I owe for Sundry Debtors are there less than 25k and what is their total value sorted by highest amount?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List the top 20 settled invoices to receive in the next 15 days overdue by more than 30 days greater than 1L sorted by highest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 20, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "overdue_only": true}`

---

### Query: `Show me all settled sales invoices till today older than 90 days less than 25k earliest due date first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Highest pending invoices to receive pending for over 60 days less than 25k .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many receivable bills are there in the last 30 days overdue by more than 30 days and what is their total value latest due date first?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": null, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `How many pending receivable bills for John Doe are there in the next 15 days less than 25k and what is their total value sorted by lowest amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `John Doe`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me all cleared sales invoices this week with age less than 15 days above 50,000 oldest first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `How many cleared bills customers owe me are there greater than 1L and what is their total value latest due date first?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Lowest cleared receivables for Sundry Creditors this week with age less than 15 days .`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `How many bills I owe are there for March 2025 with age less than 15 days less than 25k and what is their total value earliest due date first?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show the Oldest unpaid payable bills for Global Exports pending for over 60 days above 50,000 .`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Exports`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many cleared bills customers owe me for John Doe are there in the last 30 days older than 90 days under 10,000 and what is their total value sorted by highest amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `John Doe`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all cleared purchase invoices related to Acme Corp this week with age less than 15 days above 50,000 earliest due date first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Highest unpaid payables for Acme Corp for March 2025 overdue by more than 30 days less than 25k .`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List the top 5 cleared sales invoices of Acme Corp till today under 10,000 sorted by lowest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 5, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 20 payables for March 2025 overdue by more than 30 days above 50,000 sorted by lowest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 20, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `How many settled invoices to receive are there for March 2025 overdue by more than 30 days under 10,000 and what is their total value sorted by lowest amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "overdue_only": true}`

---

### Query: `List the top 10 pending payable bills this week older than 90 days under 10,000 oldest first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me all cleared invoices to receive till today under 10,000 oldest first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all pending payable bills related to Global Exports in the last 30 days with age less than 15 days sorted by highest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Global Exports`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 15 purchase invoices in the last 30 days greater than 1L latest due date first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 15, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `How many sales invoices for Sundry Creditors are there for March 2025 overdue by more than 30 days under 10,000 and what is their total value newest first?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `Show me all unpaid payables for March 2025 with age less than 15 days less than 25k oldest first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me all bills to pay this week overdue by more than 30 days greater than 1L earliest due date first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `List the top 20 settled receivables in the last 30 days under 10,000 oldest first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 20, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 5 settled bills to pay for March 2025 overdue by more than 30 days less than 25k newest first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "overdue_only": true}`

---

### Query: `List the top 5 unpaid payables this week with age less than 15 days above 50,000 sorted by lowest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 5, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 20 invoices to receive older than 90 days greater than 1L earliest due date first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me all unpaid bills to pay related to Tech Solutions older than 90 days above 50,000 sorted by lowest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show the Newest settled receivables for Acme Corp this week older than 90 days less than 25k .`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Newest payables in the next 15 days overdue by more than 30 days greater than 1L .`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "overdue_only": true}`

---

### Query: `Show the Oldest pending bills customers owe me till today older than 90 days .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 20 cleared bills customers owe me in the last 30 days above 50,000 sorted by lowest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 20, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `How many settled invoices to receive for Sundry Debtors are there till today pending for over 60 days greater than 1L and what is their total value newest first?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all sales invoices for March 2025 less than 25k newest first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List the top 20 settled bills customers owe me in the next 15 days pending for over 60 days less than 25k latest due date first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 20, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all settled bills customers owe me older than 90 days under 10,000 earliest due date first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `How many sales invoices for Sundry Creditors are there older than 90 days less than 25k and what is their total value latest due date first?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List the top 20 pending sales invoices of Sundry Debtors with age less than 15 days greater than 1L oldest first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many cleared purchase invoices are there in the next 15 days with age less than 15 days and what is their total value newest first?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 5 unpaid bills customers owe me of John Doe for March 2025 sorted by lowest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `John Doe`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": null, "limit": 5, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show the Oldest unpaid invoices to receive for Sundry Debtors in the last 30 days overdue by more than 30 days greater than 1L .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me all cleared bills I owe related to Tech Solutions pending for over 60 days oldest first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `How many pending bills I owe for Sundry Creditors are there with age less than 15 days less than 25k and what is their total value sorted by highest amount?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me all cleared payables pending for over 60 days under 10,000 sorted by highest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 50 cleared payable bills for March 2025 older than 90 days above 50,000 newest first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 5 settled payables in the next 15 days pending for over 60 days under 10,000 oldest first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 5, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all bills to pay related to Sundry Debtors in the last 30 days older than 90 days under 10,000 sorted by highest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show the Oldest pending bills I owe till today with age less than 15 days under 10,000 .`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 20 pending receivables of Acme Corp for March 2025 older than 90 days greater than 1L latest due date first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 20, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show the Oldest cleared bills to pay for Acme Corp this week older than 90 days above 50,000 .`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all settled payables for March 2025 pending for over 60 days under 10,000 oldest first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 10 pending purchase invoices overdue by more than 30 days under 10,000 sorted by highest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 10, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List the top 15 sales invoices in the last 30 days pending for over 60 days under 10,000 sorted by highest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 15, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `How many unpaid bills customers owe me for Global Exports are there for March 2025 pending for over 60 days above 50,000 and what is their total value oldest first?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Global Exports`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show the Highest pending receivables for March 2025 older than 90 days .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many cleared bills to pay are there this week under 10,000 and what is their total value newest first?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Lowest unpaid sales invoices in the last 30 days above 50,000 .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me all settled invoices to receive related to Sundry Creditors in the last 30 days pending for over 60 days less than 25k sorted by lowest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `How many bills to pay are there in the next 15 days with age less than 15 days less than 25k and what is their total value latest due date first?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `How many unpaid invoices to receive for Global Exports are there this week overdue by more than 30 days above 50,000 and what is their total value latest due date first?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Global Exports`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `How many settled receivable bills are there for March 2025 pending for over 60 days greater than 1L and what is their total value oldest first?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 20 settled bills customers owe me overdue by more than 30 days under 10,000 earliest due date first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "overdue_only": true}`

---

### Query: `List the top 15 pending receivables of John Doe till today overdue by more than 30 days sorted by highest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `John Doe`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": null, "limit": 15, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me all cleared bills to pay related to Sundry Debtors for March 2025 older than 90 days under 10,000 latest due date first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 50 cleared payable bills of Sundry Debtors in the last 30 days with age less than 15 days sorted by highest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": 50, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all settled bills customers owe me related to Tech Solutions in the last 30 days older than 90 days under 10,000 sorted by lowest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `How many cleared payable bills are there in the next 15 days with age less than 15 days under 10,000 and what is their total value earliest due date first?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all settled bills customers owe me till today older than 90 days less than 25k sorted by highest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all cleared bills customers owe me older than 90 days less than 25k sorted by highest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 15 cleared payable bills of Sundry Creditors in the last 30 days older than 90 days greater than 1L sorted by highest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 15, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 15 settled bills customers owe me less than 25k sorted by lowest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 15, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 20 unpaid receivables this week greater than 1L sorted by highest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 20, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 20 settled payables in the next 15 days older than 90 days above 50,000 newest first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `How many cleared receivables for Acme Corp are there in the next 15 days with age less than 15 days less than 25k and what is their total value oldest first?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Oldest pending purchase invoices in the next 15 days pending for over 60 days greater than 1L .`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 20 pending bills to pay for March 2025 overdue by more than 30 days less than 25k newest first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List the top 50 settled bills customers owe me in the next 15 days overdue by more than 30 days greater than 1L sorted by highest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 50, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "overdue_only": true}`

---

### Query: `List the top 20 unpaid payable bills in the last 30 days older than 90 days earliest due date first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many cleared receivable bills are there till today pending for over 60 days greater than 1L and what is their total value earliest due date first?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `How many cleared payables are there for March 2025 older than 90 days less than 25k and what is their total value sorted by highest amount?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 15 unpaid bills customers owe me of John Doe in the next 15 days newest first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `John Doe`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": null, "amount_filter": null, "limit": 15, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 10 unpaid receivable bills till today with age less than 15 days under 10,000 newest first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 20 pending payables of Tech Solutions pending for over 60 days greater than 1L latest due date first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 20, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show the Newest cleared invoices to receive in the next 15 days with age less than 15 days .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 15}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Oldest cleared receivable bills in the last 30 days with age less than 15 days greater than 1L .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Newest settled purchase invoices for Sundry Debtors overdue by more than 30 days greater than 1L .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "overdue_only": true}`

---

### Query: `How many settled purchase invoices for John Doe are there till today less than 25k and what is their total value earliest due date first?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `John Doe`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `List the top 5 cleared purchase invoices of Sundry Creditors this week overdue by more than 30 days less than 25k oldest first.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared", "overdue_only": true}`

---

### Query: `Show the Highest unpaid bills customers owe me in the last 30 days with age less than 15 days above 50,000 .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show the Newest pending bills to pay for Tech Solutions in the last 30 days with age less than 15 days less than 25k .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Tech Solutions`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `How many cleared bills customers owe me are there for March 2025 with age less than 15 days and what is their total value newest first?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Highest invoices to receive till today greater than 1L .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 1, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List the top 20 cleared sales invoices in the last 30 days older than 90 days under 10,000 sorted by highest amount.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": 20, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Oldest receivables this week greater than 1L .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 1, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `List the top 50 unpaid payable bills of Acme Corp till today older than 90 days sorted by highest amount.`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": null, "limit": 50, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List the top 20 cleared sales invoices for March 2025 pending for over 60 days greater than 1L latest due date first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 20, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show me all cleared sales invoices with age less than 15 days above 50,000 newest first.`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": null, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `Show the Newest cleared bills customers owe me for John Doe in the last 30 days with age less than 15 days .`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `John Doe`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": null, "limit": 1, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "cleared"}`

---

### Query: `How many unpaid receivable bills are there for March 2025 overdue by more than 30 days less than 25k and what is their total value sorted by highest amount?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 25000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me individual pending bills for VIP Clients generated this month where the amount is between 5000 and 7500 sorted by highest amount first`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `VIP Clients`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 5000.0, "max": 7500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 5 debtors from South Region Debtors having outstanding older than 90 days with balances exceeding 21000?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `South Region Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 21000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Local Suppliers from the last 15 days where the bill value was under 2500?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Local Suppliers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 15}, "age_filter": null, "amount_filter": {"operator": "<", "value": 2500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `compare top 3 creditors in south region debtors who have pending bills between 2500 and 22500 overdue by 7 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `South Region Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 22500.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me an ageing summary of Sundry Debtors for invoices due in the next 30 days ranging from 2500 to 7500 please`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 30}, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 7500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 15 oldest bills for East Zone Dealers with value strictly > 6000 and age < 120 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `East Zone Dealers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 120}, "amount_filter": {"operator": ">", "value": 6000.0}, "limit": 15, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Retrieve individual pending bills for Retailers generated this month where the amount is between 7500 and 27500 sorted by highest amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 27500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 3 debtors from Wholesalers having outstanding older than 60 days with balances exceeding 15000?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 15000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `what is the total sum of payables for south region debtors from the last 120 days where the bill value was under 2500?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `South Region Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 120}, "age_filter": null, "amount_filter": {"operator": "<", "value": 2500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 7 creditors in Retailers who have pending bills between 5000 and 15000 overdue by 30 days please`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 5000.0, "max": 15000.0}, "limit": 7, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me an ageing summary of Local Suppliers for invoices due in the next 60 days ranging from 2500 to 5000`
- **Intent:** `GET_AGEING`
- **Ledger:** `Local Suppliers`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 60}, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 5000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 15 oldest bills for Key Vendors with value strictly > 17500 and age < 90 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Key Vendors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": ">", "value": 17500.0}, "limit": 15, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me individual pending bills for Retailers generated this month where the amount is in the range of 10000 and 30000 sorted by highest amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 30000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `who are my top 3 debtors from wholesalers having outstanding older than 30 days with balances exceeding 15000?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 15000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Key Vendors from the last 30 days where the bill value was under 2500? please`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Key Vendors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 30}, "age_filter": null, "amount_filter": {"operator": "<", "value": 2500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 20 creditors in Hardware Suppliers who have pending bills between 2500 and 12500 overdue by 30 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Hardware Suppliers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 12500.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Fetch an ageing summary of Group Expenses for invoices due in the next 60 days ranging from 7500 to 27500`
- **Intent:** `GET_AGEING`
- **Ledger:** `Group Expenses`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 60}, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 27500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "group_breakdown": true}`

---

### Query: `Count only the top 5 oldest bills for Retailers with value strictly > 12500 and age < 45 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": ">", "value": 12500.0}, "limit": 5, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `show me individual pending bills for group expenses generated this month where the amount is between 7500 and 27500 sorted by highest amount first`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Group Expenses`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 27500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "group_breakdown": true}`

---

### Query: `Who are my top 3 debtors from Key Vendors having outstanding older than 90 days with balances exceeding 15000? please`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Key Vendors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 15000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Retailers from the last 60 days where the bill value was under 7500?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 60}, "age_filter": null, "amount_filter": {"operator": "<", "value": 7500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 5 creditors in Group Expenses who have pending bills between 1000 and 11000 overdue by 60 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Group Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 1000.0, "max": 11000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true, "group_breakdown": true}`

---

### Query: `Give me an ageing summary of VIP Clients for invoices due in the next 90 days between 7500 to 10000`
- **Intent:** `GET_AGEING`
- **Ledger:** `VIP Clients`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 90}, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `count only the top 20 oldest bills for group expenses with value strictly > 11000 and age < 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Group Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 11000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "group_breakdown": true}`

---

### Query: `Show me individual pending bills for Key Accounts generated this month where the amount is between 10000 and 30000 sorted by highest amount first please`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Key Accounts`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 30000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 10 debtors from Group Expenses having outstanding older than 120 days with balances exceeding 12500?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Group Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": {"operator": ">", "value": 12500.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "group_breakdown": true}`

---

### Query: `What is the total sum of payables for Local Suppliers from the last 7 days where the bill value was under 5000?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Local Suppliers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 7}, "age_filter": null, "amount_filter": {"operator": "<", "value": 5000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 10 creditors in Sundry Creditors who have pending bills in the range of 10000 and 12500 overdue by 120 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 12500.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `give me an ageing summary of sundry debtors for invoices due in the next 30 days ranging from 7500 to 17500`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 30}, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 17500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 20 oldest bills for Sundry Debtors with value strictly > 25000 and age < 60 days please`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me individual pending bills for Retailers generated this month where the amount is between 1000 and 6000 sorted by highest amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 1000.0, "max": 6000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 5 debtors from Hardware Suppliers having outstanding older than 15 days with balances exceeding 12500?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Hardware Suppliers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 12500.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Retailers from the last 120 days where the bill value was under 2500?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 120}, "age_filter": null, "amount_filter": {"operator": "<", "value": 2500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `compare top 10 creditors in vip clients who have pending bills between 2500 and 5000 overdue by 15 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `VIP Clients`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 5000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me an ageing summary of Wholesalers for invoices due in the next 30 days ranging from 1000 to 21000 please`
- **Intent:** `GET_AGEING`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 30}, "age_filter": null, "amount_filter": {"operator": "between", "min": 1000.0, "max": 21000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 7 oldest bills for South Region Debtors with value strictly > 7500 and age < 60 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `South Region Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": ">", "value": 7500.0}, "limit": 7, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Retrieve individual pending bills for East Zone Dealers generated this month where the amount is between 1000 and 6000 sorted by highest amount first`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `East Zone Dealers`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 1000.0, "max": 6000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 20 debtors from Key Accounts having outstanding older than 7 days with balances exceeding 10000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Key Accounts`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 7}, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `what is the total sum of payables for group expenses from the last 60 days where the bill value was under 2500?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Group Expenses`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 60}, "age_filter": null, "amount_filter": {"operator": "<", "value": 2500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "group_breakdown": true}`

---

### Query: `Compare top 15 creditors in Hardware Suppliers who have pending bills between 5000 and 15000 overdue by 15 days please`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Hardware Suppliers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 5000.0, "max": 15000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me an ageing summary of Hardware Suppliers for invoices due in the next 60 days ranging from 2500 to 7500`
- **Intent:** `GET_AGEING`
- **Ledger:** `Hardware Suppliers`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 60}, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 7500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 15 oldest bills for Key Accounts with value strictly > 12500 and age < 120 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Key Accounts`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 120}, "amount_filter": {"operator": ">", "value": 12500.0}, "limit": 15, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me individual pending bills for South Region Debtors generated this month where the amount is in the range of 7500 and 17500 sorted by highest amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `South Region Debtors`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 17500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `who are my top 5 debtors from group expenses having outstanding older than 15 days with balances exceeding 7500?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Group Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 7500.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "group_breakdown": true}`

---

### Query: `What is the total sum of payables for South Region Debtors from the last 7 days where the bill value was under 10000? please`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `South Region Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 7}, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 20 creditors in Key Vendors who have pending bills between 2500 and 22500 overdue by 60 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Key Vendors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 22500.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Fetch an ageing summary of Key Vendors for invoices due in the next 30 days ranging from 2500 to 12500`
- **Intent:** `GET_AGEING`
- **Ledger:** `Key Vendors`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 30}, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 12500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 10 oldest bills for South Region Debtors with value strictly > 3500 and age < 60 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `South Region Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": ">", "value": 3500.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `show me individual pending bills for retailers generated this month where the amount is between 7500 and 10000 sorted by highest amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 10 debtors from Key Accounts having outstanding older than 30 days with balances exceeding 10000? please`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Key Accounts`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Retailers from the last 90 days where the bill value was under 1000?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": null, "amount_filter": {"operator": "<", "value": 1000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 5 creditors in Key Vendors who have pending bills between 5000 and 7500 overdue by 7 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Key Vendors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 5000.0, "max": 7500.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me an ageing summary of Local Suppliers for invoices due in the next 90 days between 10000 to 12500`
- **Intent:** `GET_AGEING`
- **Ledger:** `Local Suppliers`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 90}, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 12500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `count only the top 7 oldest bills for local suppliers with value strictly > 15000 and age < 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Local Suppliers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 15000.0}, "limit": 7, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me individual pending bills for Sundry Creditors generated this month where the amount is between 1000 and 11000 sorted by highest amount first please`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 1000.0, "max": 11000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 20 debtors from South Region Debtors having outstanding older than 45 days with balances exceeding 6000?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `South Region Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 45}, "amount_filter": {"operator": ">", "value": 6000.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Group Expenses from the last 90 days where the bill value was under 7500?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Group Expenses`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": null, "amount_filter": {"operator": "<", "value": 7500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "group_breakdown": true}`

---

### Query: `Compare top 15 creditors in East Zone Dealers who have pending bills in the range of 7500 and 10000 overdue by 60 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `East Zone Dealers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 10000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `give me an ageing summary of sundry debtors for invoices due in the next 30 days ranging from 10000 to 30000`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 30}, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 30000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 5 oldest bills for VIP Clients with value strictly > 10000 and age < 45 days please`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `VIP Clients`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me individual pending bills for North Zone Customers generated this month where the amount is between 2500 and 5000 sorted by highest amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `North Zone Customers`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 5000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 3 debtors from Marketing Expenses having outstanding older than 60 days with balances exceeding 7500?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Marketing Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 7500.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Wholesalers from the last 120 days where the bill value was under 1000?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 120}, "age_filter": null, "amount_filter": {"operator": "<", "value": 1000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `compare top 5 creditors in local suppliers who have pending bills between 5000 and 25000 overdue by 45 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Local Suppliers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 5000.0, "max": 25000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me an ageing summary of Wholesalers for invoices due in the next 45 days ranging from 7500 to 10000 please`
- **Intent:** `GET_AGEING`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 45}, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 10 oldest bills for Local Suppliers with value strictly > 12500 and age < 60 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Local Suppliers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": ">", "value": 12500.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Retrieve individual pending bills for Wholesalers generated this month where the amount is between 1000 and 3500 sorted by highest amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 1000.0, "max": 3500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 20 debtors from Key Vendors having outstanding older than 15 days with balances exceeding 27500?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Key Vendors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 27500.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `what is the total sum of payables for key accounts from the last 120 days where the bill value was under 2500?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Key Accounts`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 120}, "age_filter": null, "amount_filter": {"operator": "<", "value": 2500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 15 creditors in East Zone Dealers who have pending bills between 7500 and 17500 overdue by 15 days please`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `East Zone Dealers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 17500.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me an ageing summary of Sundry Creditors for invoices due in the next 90 days ranging from 2500 to 12500`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 90}, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 12500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 3 oldest bills for North Zone Customers with value strictly > 12500 and age < 7 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `North Zone Customers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 7}, "amount_filter": {"operator": ">", "value": 12500.0}, "limit": 3, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me individual pending bills for East Zone Dealers generated this month where the amount is in the range of 10000 and 12500 sorted by highest amount first`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `East Zone Dealers`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 12500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `who are my top 5 debtors from key accounts having outstanding older than 90 days with balances exceeding 12500?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Key Accounts`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 12500.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Wholesalers from the last 45 days where the bill value was under 5000? please`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": {"operator": "<", "value": 5000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 10 creditors in North Zone Customers who have pending bills between 1000 and 6000 overdue by 7 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `North Zone Customers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 1000.0, "max": 6000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Fetch an ageing summary of VIP Clients for invoices due in the next 7 days ranging from 1000 to 21000`
- **Intent:** `GET_AGEING`
- **Ledger:** `VIP Clients`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 7}, "age_filter": null, "amount_filter": {"operator": "between", "min": 1000.0, "max": 21000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 15 oldest bills for Sundry Creditors with value strictly > 15000 and age < 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 15000.0}, "limit": 15, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `show me individual pending bills for sundry creditors generated this month where the amount is between 7500 and 17500 sorted by highest amount first`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 17500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 20 debtors from Retailers having outstanding older than 120 days with balances exceeding 10000? please`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": {"operator": ">", "value": 10000.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for East Zone Dealers from the last 120 days where the bill value was under 10000?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `East Zone Dealers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 120}, "age_filter": null, "amount_filter": {"operator": "<", "value": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 15 creditors in Wholesalers who have pending bills between 7500 and 10000 overdue by 7 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 10000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me an ageing summary of Sundry Creditors for invoices due in the next 7 days between 5000 to 7500`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 7}, "age_filter": null, "amount_filter": {"operator": "between", "min": 5000.0, "max": 7500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `count only the top 7 oldest bills for retailers with value strictly > 25000 and age < 30 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 25000.0}, "limit": 7, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me individual pending bills for Local Suppliers generated this month where the amount is between 1000 and 21000 sorted by highest amount first please`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Local Suppliers`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 1000.0, "max": 21000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 10 debtors from North Zone Customers having outstanding older than 15 days with balances exceeding 22500?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `North Zone Customers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 22500.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Key Accounts from the last 90 days where the bill value was under 5000?`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Key Accounts`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": null, "amount_filter": {"operator": "<", "value": 5000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 7 creditors in Retailers who have pending bills in the range of 1000 and 11000 overdue by 15 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 1000.0, "max": 11000.0}, "limit": 7, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `give me an ageing summary of south region debtors for invoices due in the next 120 days ranging from 2500 to 7500`
- **Intent:** `GET_AGEING`
- **Ledger:** `South Region Debtors`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 120}, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 7500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 7 oldest bills for Sundry Debtors with value strictly > 6000 and age < 15 days please`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 6000.0}, "limit": 7, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me individual pending bills for Marketing Expenses generated this month where the amount is between 7500 and 27500 sorted by highest amount first`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Marketing Expenses`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 27500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 10 debtors from Sundry Creditors having outstanding older than 30 days with balances exceeding 7500?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 7500.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for East Zone Dealers from the last 120 days where the bill value was under 1000?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `East Zone Dealers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 120}, "age_filter": null, "amount_filter": {"operator": "<", "value": 1000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `compare top 15 creditors in wholesalers who have pending bills between 10000 and 12500 overdue by 30 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 12500.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me an ageing summary of Sundry Debtors for invoices due in the next 120 days ranging from 2500 to 12500 please`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 120}, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 12500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 7 oldest bills for Wholesalers with value strictly > 21000 and age < 30 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 21000.0}, "limit": 7, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Retrieve individual pending bills for Hardware Suppliers generated this month where the amount is between 5000 and 15000 sorted by highest amount first`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Hardware Suppliers`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 5000.0, "max": 15000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 20 debtors from Marketing Expenses having outstanding older than 60 days with balances exceeding 6000?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Marketing Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 6000.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `what is the total sum of payables for sundry debtors from the last 15 days where the bill value was under 2500?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 15}, "age_filter": null, "amount_filter": {"operator": "<", "value": 2500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 7 creditors in Sundry Creditors who have pending bills between 5000 and 7500 overdue by 90 days please`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 5000.0, "max": 7500.0}, "limit": 7, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me an ageing summary of Sundry Debtors for invoices due in the next 7 days ranging from 2500 to 22500`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 7}, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 22500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 20 oldest bills for Key Accounts with value strictly > 3500 and age < 30 days`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Key Accounts`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 3500.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me individual pending bills for Group Expenses generated this month where the amount is in the range of 2500 and 7500 sorted by highest amount first`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Group Expenses`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 7500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "group_breakdown": true}`

---

### Query: `who are my top 3 debtors from retailers having outstanding older than 15 days with balances exceeding 27500?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 27500.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Hardware Suppliers from the last 45 days where the bill value was under 5000? please`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Hardware Suppliers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": {"operator": "<", "value": 5000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 20 creditors in Wholesalers who have pending bills between 1000 and 21000 overdue by 90 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 1000.0, "max": 21000.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Fetch an ageing summary of Marketing Expenses for invoices due in the next 120 days ranging from 10000 to 30000`
- **Intent:** `GET_AGEING`
- **Ledger:** `Marketing Expenses`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 120}, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 30000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 3 oldest bills for Local Suppliers with value strictly > 12500 and age < 45 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Local Suppliers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": ">", "value": 12500.0}, "limit": 3, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `show me individual pending bills for sundry debtors generated this month where the amount is between 10000 and 15000 sorted by highest amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 15000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 7 debtors from Group Expenses having outstanding older than 60 days with balances exceeding 27500? please`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Group Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 27500.0}, "limit": 7, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "group_breakdown": true}`

---

### Query: `What is the total sum of payables for Sundry Debtors from the last 120 days where the bill value was under 2500?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 120}, "age_filter": null, "amount_filter": {"operator": "<", "value": 2500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 3 creditors in Marketing Expenses who have pending bills between 7500 and 12500 overdue by 45 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Marketing Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 12500.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me an ageing summary of North Zone Customers for invoices due in the next 7 days between 10000 to 12500`
- **Intent:** `GET_AGEING`
- **Ledger:** `North Zone Customers`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 7}, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 12500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `count only the top 20 oldest bills for sundry creditors with value strictly > 30000 and age < 30 days`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Sundry Creditors`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 30000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me individual pending bills for Key Vendors generated this month where the amount is between 7500 and 12500 sorted by highest amount first please`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Key Vendors`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 12500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who are my top 7 debtors from Marketing Expenses having outstanding older than 7 days with balances exceeding 12500?`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Marketing Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 7}, "amount_filter": {"operator": ">", "value": 12500.0}, "limit": 7, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Local Suppliers from the last 120 days where the bill value was under 1000?`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Local Suppliers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 120}, "age_filter": null, "amount_filter": {"operator": "<", "value": 1000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Compare top 3 creditors in Wholesalers who have pending bills in the range of 7500 and 10000 overdue by 120 days`
- **Intent:** `GET_TOP_CREDITORS`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 7500.0, "max": 10000.0}, "limit": 3, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `give me an ageing summary of north zone customers for invoices due in the next 90 days ranging from 10000 to 12500`
- **Intent:** `GET_AGEING`
- **Ledger:** `North Zone Customers`
- **Parameters:** `{"date_filter": {"type": "next_days", "days": 90}, "age_filter": null, "amount_filter": {"operator": "between", "min": 10000.0, "max": 12500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Count only the top 5 oldest bills for Wholesalers with value strictly > 11000 and age < 120 days please`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Wholesalers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": "<", "days": 120}, "amount_filter": {"operator": ">", "value": 11000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `what is the total outstanding for Group Expenses for amounts between 5000 and 10000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Group Expenses`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": "between", "min": 5000.0, "max": 10000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "group_breakdown": true}`

---

### Query: `top 5 creditors vs top 10 debtors report for amounts > 50000`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `None`
- **Parameters:** `{"date_filter": null, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Show me individual pending bills for Key Accounts generated this month where the amount is in the range of 2500 and 5000 sorted by highest amount first`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Key Accounts`
- **Parameters:** `{"date_filter": {"type": "this_month"}, "age_filter": null, "amount_filter": {"operator": "between", "min": 2500.0, "max": 5000.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `who are my top 15 debtors from hardware suppliers having outstanding older than 120 days with balances exceeding 15000?`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Hardware Suppliers`
- **Parameters:** `{"date_filter": null, "age_filter": {"operator": ">", "days": 120}, "amount_filter": {"operator": ">", "value": 15000.0}, "limit": 15, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the total sum of payables for Retailers from the last 15 days where the bill value was under 2500? please`
- **Intent:** `GET_TOP_DEBTORS`
- **Ledger:** `Retailers`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 15}, "age_filter": null, "amount_filter": {"operator": "<", "value": 2500.0}, "limit": null, "sort": null, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": true, "status_filter": null}`

---

### Query: `Pending payables next quarter for Alpha Omega based on bill date with amount greater than 250000 overdue by more than 90 days showing top 20 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me the ageing buckets of 30 60 90 last 45 days for Jagat based on bill date with amount less than 250000 showing top 20 sorted by due date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 20, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Give me the ageing buckets of 0-30, 31-60, 61-90 this week for Acme Corp based on due date with amount less than 150000 showing top 5 sorted by amount descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [0, 5, 30, 31, 60, 61, 90]}`

---

### Query: `What is the ageing of 40, 50, 65 days last 90 days for Jagat based on bill date with amount greater than 150000 showing top 10 sorted by due date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": null, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 10, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `Give me the ageing buckets of 45, 90, 120 days last 45 days for Infosys Ltd based on bill date with amount greater than 100000 showing top 50 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [45, 90, 120]}`

---

### Query: `Show ageing of 30 60 90 this week for Wipro based on due date with amount greater than 50000 showing top 10 sorted by amount descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 30, 60, 90]}`

---

### Query: `List all receivable bills last 45 days for Reliance Industries based on bill date with amount less than 50000 less than 15 days old showing top 50 sorted by due date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 50, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me payments I have to make last 90 days for Sundry Debtors based on due date with amount less than 150000 less than 90 days old showing top 5 sorted by amount descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What money is owed to me till today for Chemical Process Pvt LTD based on due date with amount less than 100000 overdue by more than 15 days showing top 10 sorted by due date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 10, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show receivables till today for Chemical Process Pvt LTD based on bill date with amount less than 75000 overdue by more than 15 days showing top 50 sorted by due date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 50, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show ageing of 45, 90, 120 days next quarter for Acme Corp based on due date with amount less than 150000 showing top 5 sorted by bill date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [45, 90, 120]}`

---

### Query: `Show ageing of 10, 20, 30, 40 days till today for Jagat based on due date with amount less than 250000 showing top 20 sorted by bill date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 20, 30, 40]}`

---

### Query: `Show receivables next quarter for Acme Corp based on due date with amount greater than 75000 overdue by more than 15 days showing top 50 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List all receivable bills next quarter for Sundry Debtors based on due date with amount less than 100000 less than 90 days old showing top 5 sorted by due date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 5, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me payments I have to make next quarter for Thermax Ltd based on due date with amount greater than 75000 overdue by more than 15 days showing top 10 sorted by bill date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Who do I owe money to last 90 days for TCS based on due date with amount greater than 100000 less than 45 days old showing top 10 sorted by bill date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show receivables last 90 days for TCS based on bill date with amount less than 250000 less than 90 days old showing top 50 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 50, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Give me the ageing buckets of 15, 30, 45, 60 days next quarter for Jagat based on bill date with amount greater than 100000 showing top 10 sorted by amount descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [15, 30, 45, 60]}`

---

### Query: `Ageing analysis of 10, 20, 30, 40 days next quarter for Wipro based on bill date with amount less than 250000 showing top 50 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 20, 30, 40]}`

---

### Query: `Pending payables between Jan and March 2025 for Wipro based on bill date with amount greater than 50000 overdue by more than 90 days showing top 5 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Ageing analysis of 40, 50, 65 days last 45 days for Alpha Omega based on bill date with amount greater than 150000 showing top 10 sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 10, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `Show me payments I have to make between April and September 2026 for Jagat based on due date with amount greater than 50000 overdue by more than 60 days showing top 20 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List payables next quarter for TCS based on bill date with amount less than 100000 overdue by more than 60 days showing top 10 sorted by amount ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 10, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `What is the ageing of 30 60 90 till today for Reliance Industries based on bill date with amount greater than 50000 showing top 20 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [20, 30, 60, 90]}`

---

### Query: `Give me the ageing buckets of 40, 50, 65 days between April and September 2026 for Alpha Omega based on due date with amount less than 150000 showing top 20 sorted by bill date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `List all receivable bills between Jan and March 2025 for Reliance Industries based on due date with amount greater than 100000 overdue by more than 60 days showing top 10 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show ageing of 10, 20, 30, 40 days last 90 days for Infosys Ltd based on due date with amount less than 100000 showing top 50 sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 50, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 20, 30, 40]}`

---

### Query: `Pending payables between April and September 2026 for Thermax Ltd based on due date with amount less than 100000 overdue by more than 45 days showing top 5 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": ">", "days": 45}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List all receivable bills till today for Infosys Ltd based on bill date with amount greater than 150000 overdue by more than 60 days showing top 10 sorted by amount descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show ageing of 45, 90, 120 days March 2025 for Reliance Industries based on bill date with amount greater than 250000 showing top 20 sorted by bill date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [45, 90, 120]}`

---

### Query: `List payables last 45 days for Jagat based on bill date with amount less than 150000 overdue by more than 15 days showing top 20 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List all receivable bills next quarter for Chemical Process Pvt LTD based on bill date with amount less than 75000 overdue by more than 90 days showing top 20 sorted by bill date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Who do I owe money to between Jan and March 2025 for Infosys Ltd based on due date with amount greater than 50000 overdue by more than 15 days showing top 50 sorted by amount ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 50, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Ageing analysis of 30 60 90 March 2025 for Sundry Debtors based on bill date with amount greater than 75000 showing top 5 sorted by due date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 5, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [5, 30, 60, 90]}`

---

### Query: `Give me the ageing buckets of 0-30, 31-60, 61-90 this week for Wipro based on due date with amount less than 100000 showing top 50 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [0, 30, 31, 50, 60, 61, 90]}`

---

### Query: `Show receivables last 45 days for Acme Corp based on due date with amount greater than 150000 less than 30 days old showing top 5 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Ageing analysis of 0-30, 31-60, 61-90 till today for Thermax Ltd based on bill date with amount greater than 50000 showing top 10 sorted by amount ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 10, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [0, 10, 30, 31, 60, 61, 90]}`

---

### Query: `Ageing analysis of 30 60 90 till today for Acme Corp based on bill date with amount less than 100000 showing top 20 sorted by bill date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [20, 30, 60, 90]}`

---

### Query: `Pending collections between Jan and March 2025 for Wipro based on bill date with amount less than 100000 less than 90 days old showing top 5 sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show ageing of 10, 20, 30, 40 days till today for Sundry Debtors based on bill date with amount greater than 150000 showing top 10 sorted by amount ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 10, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 20, 30, 40]}`

---

### Query: `What money is owed to me this week for Reliance Industries based on due date with amount less than 150000 less than 30 days old showing top 20 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Who do I owe money to next quarter for Wipro based on bill date with amount less than 50000 less than 15 days old showing top 20 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show receivables last 90 days for Alpha Omega based on bill date with amount greater than 100000 overdue by more than 90 days showing top 10 sorted by amount ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Ageing analysis of 15, 30, 45, 60 days last 45 days for Infosys Ltd based on due date with amount greater than 150000 showing top 10 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [15, 30, 45, 60]}`

---

### Query: `Give me the ageing buckets of 15, 30, 45, 60 days between April and September 2026 for Acme Corp based on bill date with amount greater than 50000 showing top 50 sorted by amount descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 50, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [15, 30, 45, 60]}`

---

### Query: `Give me the ageing buckets of 40, 50, 65 days between April and September 2026 for Acme Corp based on bill date with amount less than 250000 showing top 50 sorted by bill date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `List all receivable bills between April and September 2026 for Infosys Ltd based on due date with amount less than 50000 less than 60 days old showing top 10 sorted by bill date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending payables between April and September 2026 for TCS based on bill date with amount less than 150000 less than 90 days old showing top 20 sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me payments I have to make next quarter for Wipro based on due date with amount greater than 75000 less than 90 days old showing top 20 sorted by bill date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending collections between Jan and March 2025 for Sundry Debtors based on due date with amount less than 150000 less than 30 days old showing top 5 sorted by due date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 5, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending payables next quarter for Alpha Omega based on bill date with amount less than 50000 overdue by more than 30 days showing top 5 sorted by amount ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 5, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me payments I have to make last 45 days for TCS based on bill date with amount less than 150000 less than 30 days old showing top 20 sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Ageing analysis of 10, 20, 30, 40 days next quarter for Acme Corp based on due date with amount less than 100000 showing top 50 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 20, 30, 40]}`

---

### Query: `Who do I owe money to between April and September 2026 for Alpha Omega based on bill date with amount greater than 250000 less than 45 days old showing top 5 sorted by amount ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 5, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the ageing of 10, 20, 30, 40 days between April and September 2026 for Thermax Ltd based on due date with amount greater than 250000 showing top 10 sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 10, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 20, 30, 40]}`

---

### Query: `Who do I owe money to March 2025 for Thermax Ltd based on bill date with amount greater than 250000 less than 45 days old showing top 20 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Ageing analysis of 0-30, 31-60, 61-90 till today for Jagat based on bill date with amount greater than 75000 showing top 20 sorted by due date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 20, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [0, 20, 30, 31, 60, 61, 90]}`

---

### Query: `Show ageing of 30 60 90 this week for Alpha Omega based on due date with amount greater than 75000 showing top 20 sorted by amount ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 20, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [20, 30, 60, 90]}`

---

### Query: `Pending collections last 90 days for TCS based on due date with amount less than 100000 overdue by more than 15 days showing top 50 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List all receivable bills next quarter for Sundry Debtors based on bill date with amount less than 75000 less than 45 days old showing top 20 sorted by due date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show receivables between April and September 2026 for Alpha Omega based on bill date with amount greater than 250000 less than 90 days old showing top 10 sorted by due date descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 10, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the ageing of 0-30, 31-60, 61-90 last 45 days for Reliance Industries based on bill date with amount less than 250000 showing top 10 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null}`

---

### Query: `Give me the ageing buckets of 10, 20, 30, 40 days this week for Alpha Omega based on bill date with amount greater than 75000 showing top 50 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 20, 30, 40]}`

---

### Query: `List payables last 45 days for Alpha Omega based on due date with amount less than 250000 less than 15 days old showing top 20 sorted by bill date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show ageing of 45, 90, 120 days till today for Infosys Ltd based on due date with amount less than 250000 showing top 50 sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 50, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [45, 90, 120]}`

---

### Query: `Pending payables this week for Sundry Debtors based on bill date with amount less than 100000 less than 90 days old showing top 10 sorted by bill date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Give me the ageing buckets of 40, 50, 65 days between Jan and March 2025 for Wipro based on due date with amount less than 50000 showing top 50 sorted by amount descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 50, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `What money is owed to me this week for TCS based on bill date with amount less than 75000 less than 45 days old showing top 5 sorted by due date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 5, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What money is owed to me last 90 days for Thermax Ltd based on due date with amount greater than 50000 less than 30 days old showing top 5 sorted by due date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 5, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What money is owed to me between Jan and March 2025 for Acme Corp based on bill date with amount greater than 100000 less than 15 days old showing top 50 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the ageing of 45, 90, 120 days last 45 days for Thermax Ltd based on due date with amount greater than 250000 showing top 5 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": null, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [45, 90, 120]}`

---

### Query: `Pending payables between April and September 2026 for Infosys Ltd based on bill date with amount greater than 50000 less than 45 days old showing top 5 sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me payments I have to make this week for Infosys Ltd based on bill date with amount less than 100000 less than 45 days old showing top 10 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 10, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show receivables this week for Thermax Ltd based on bill date with amount less than 50000 less than 60 days old showing top 50 sorted by amount ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 50, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What is the ageing of 40, 50, 65 days between Jan and March 2025 for TCS based on due date with amount less than 100000 showing top 5 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `What money is owed to me between April and September 2026 for Wipro based on due date with amount greater than 150000 less than 30 days old showing top 50 sorted by amount ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 50, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Give me the ageing buckets of 15, 30, 45, 60 days March 2025 for Chemical Process Pvt LTD based on due date with amount less than 75000 showing top 20 sorted by amount ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 20, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [15, 30, 45, 60]}`

---

### Query: `What money is owed to me last 90 days for Acme Corp based on bill date with amount less than 50000 less than 90 days old showing top 10 sorted by due date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 10, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show me payments I have to make between Jan and March 2025 for Thermax Ltd based on due date with amount less than 75000 overdue by more than 90 days showing top 10 sorted by bill date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show ageing of 30 60 90 next quarter for Alpha Omega based on due date with amount less than 250000 showing top 50 sorted by amount ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 50, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [30, 50, 60, 90]}`

---

### Query: `Who do I owe money to March 2025 for Wipro based on bill date with amount less than 100000 overdue by more than 30 days showing top 50 sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 50, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show receivables between Jan and March 2025 for Chemical Process Pvt LTD based on due date with amount less than 50000 overdue by more than 30 days showing top 20 sorted by bill date descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `What money is owed to me last 90 days for Jagat based on bill date with amount greater than 75000 overdue by more than 60 days showing top 50 sorted by amount ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 50, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Who do I owe money to March 2025 for Reliance Industries based on bill date with amount less than 150000 overdue by more than 90 days showing top 50 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me payments I have to make till today for Reliance Industries based on due date with amount greater than 100000 overdue by more than 60 days showing top 50 sorted by amount ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 50, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `What money is owed to me between Jan and March 2025 for Thermax Ltd based on bill date with amount less than 150000 overdue by more than 30 days showing top 20 sorted by bill date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show receivables this week for Alpha Omega based on due date with amount less than 150000 overdue by more than 90 days showing top 10 sorted by due date descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 10, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List all receivable bills March 2025 for Sundry Debtors based on due date with amount less than 150000 overdue by more than 30 days showing top 50 sorted by bill date ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 50, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me payments I have to make this week for Alpha Omega based on bill date with amount greater than 75000 overdue by more than 15 days showing top 20 sorted by bill date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Who do I owe money to between April and September 2026 for TCS based on due date with amount less than 75000 overdue by more than 30 days showing top 5 sorted by due date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 5, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Who do I owe money to last 90 days for Thermax Ltd based on due date with amount less than 250000 overdue by more than 15 days showing top 5 sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me payments I have to make last 45 days for TCS based on bill date with amount greater than 250000 less than 15 days old showing top 20 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List payables last 45 days for Thermax Ltd based on due date with amount greater than 100000 less than 30 days old showing top 20 sorted by amount ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 20, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `List payables last 45 days for Thermax Ltd based on due date with amount greater than 250000 overdue by more than 90 days showing top 10 sorted by bill date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List payables this week for Acme Corp based on due date with amount greater than 75000 less than 15 days old showing top 10 sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 10, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show ageing of 15, 30, 45, 60 days till today for Reliance Industries based on bill date with amount greater than 75000 showing top 10 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [15, 30, 45, 60]}`

---

### Query: `What money is owed to me between April and September 2026 for Wipro based on bill date with amount greater than 100000 overdue by more than 15 days showing top 50 sorted by amount ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 50, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show receivables between Jan and March 2025 for Alpha Omega based on due date with amount greater than 150000 less than 15 days old showing top 20 sorted by bill date descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": {"operator": "<", "days": 15}, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Show ageing of 30 60 90 March 2025 for Alpha Omega based on bill date with amount less than 100000 showing top 50 sorted by amount descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 50, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [30, 50, 60, 90]}`

---

### Query: `Ageing analysis of 10, 20, 30, 40 days next quarter for Alpha Omega based on bill date with amount less than 150000 showing top 5 sorted by bill date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Alpha Omega`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": "<", "value": 150000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 20, 30, 40]}`

---

### Query: `Show me payments I have to make this week for Chemical Process Pvt LTD based on bill date with amount less than 100000 overdue by more than 90 days showing top 5 sorted by due date descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 5, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show receivables last 90 days for Jagat based on bill date with amount less than 250000 overdue by more than 15 days showing top 10 sorted by due date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 10, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show me payments I have to make between April and September 2026 for Jagat based on bill date with amount less than 50000 less than 90 days old showing top 5 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": "<", "days": 90}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 5, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `What money is owed to me last 45 days for Sundry Debtors based on bill date with amount less than 50000 overdue by more than 45 days showing top 10 sorted by amount ascending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 45}, "age_filter": {"operator": ">", "days": 45}, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 10, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me the ageing buckets of 15, 30, 45, 60 days March 2025 for Infosys Ltd based on bill date with amount greater than 100000 showing top 5 sorted by amount ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 5, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [15, 30, 45, 60]}`

---

### Query: `List payables last 90 days for Sundry Debtors based on bill date with amount greater than 150000 less than 45 days old showing top 5 sorted by due date descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "last_days", "days": 90}, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 5, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending payables next quarter for Reliance Industries based on bill date with amount less than 75000 overdue by more than 30 days showing top 5 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 5, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me the ageing buckets of 0-30, 31-60, 61-90 between Jan and March 2025 for Acme Corp based on bill date with amount greater than 75000 showing top 10 sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 10, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [0, 10, 30, 31, 60, 61, 90]}`

---

### Query: `List all receivable bills this week for TCS based on bill date with amount greater than 75000 overdue by more than 30 days showing top 5 sorted by due date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "this_week"}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": ">", "value": 75000.0}, "limit": 5, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List all receivable bills between April and September 2026 for Wipro based on bill date with amount greater than 50000 overdue by more than 60 days showing top 20 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `List all receivable bills between April and September 2026 for Reliance Industries based on due date with amount less than 100000 overdue by more than 60 days showing top 10 sorted by bill date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show ageing of 40, 50, 65 days till today for Sundry Debtors based on bill date with amount greater than 100000 showing top 10 sorted by due date descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Sundry Debtors`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 10, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `Show receivables next quarter for TCS based on due date with amount less than 250000 overdue by more than 30 days showing top 10 sorted by bill date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": {"operator": ">", "days": 30}, "amount_filter": {"operator": "<", "value": 250000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "asc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show receivables between April and September 2026 for Thermax Ltd based on bill date with amount greater than 250000 overdue by more than 60 days showing top 50 sorted by due date ascending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Thermax Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": ">", "days": 60}, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 50, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me the ageing buckets of 15, 30, 45, 60 days till today for Wipro based on bill date with amount greater than 50000 showing top 20 sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": null, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 20, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [15, 30, 45, 60]}`

---

### Query: `List all receivable bills between April and September 2026 for TCS based on bill date with amount greater than 250000 overdue by more than 90 days showing top 20 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": ">", "days": 90}, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 20, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Show ageing of 10, 20, 30, 40 days next quarter for Wipro based on due date with amount less than 75000 showing top 50 sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 10, "start_year": 2026, "end_day": 31, "end_month": 12, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": "<", "value": 75000.0}, "limit": 50, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 20, 30, 40]}`

---

### Query: `Show me payments I have to make till today for Reliance Industries based on due date with amount greater than 100000 less than 45 days old showing top 5 sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Reliance Industries`
- **Parameters:** `{"date_filter": {"type": "till_today"}, "age_filter": {"operator": "<", "days": 45}, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Pending payables between April and September 2026 for TCS based on bill date with amount less than 100000 less than 30 days old showing top 10 sorted by bill date descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": "<", "days": 30}, "amount_filter": {"operator": "<", "value": 100000.0}, "limit": 10, "sort": {"field": "bill_date", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Give me the ageing buckets of 40, 50, 65 days between Jan and March 2025 for Chemical Process Pvt LTD based on due date with amount greater than 100000 showing top 20 sorted by amount ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Chemical Process Pvt LTD`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 1, "start_year": 2025, "end_day": 31, "end_month": 3, "end_year": 2025}, "age_filter": null, "amount_filter": {"operator": ">", "value": 100000.0}, "limit": 20, "sort": {"field": "amount", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [40, 50, 65]}`

---

### Query: `Give me the ageing buckets of 15, 30, 45, 60 days between April and September 2026 for TCS based on bill date with amount greater than 250000 showing top 5 sorted by due date ascending`
- **Intent:** `GET_AGEING`
- **Ledger:** `TCS`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": null, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 5, "sort": {"field": "due_date", "order": "asc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "bill_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [15, 30, 45, 60]}`

---

### Query: `List all receivable bills between April and September 2026 for Infosys Ltd based on due date with amount greater than 250000 overdue by more than 15 days showing top 5 sorted by due date descending`
- **Intent:** `GET_RECEIVABLES`
- **Ledger:** `Infosys Ltd`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": ">", "days": 15}, "amount_filter": {"operator": ">", "value": 250000.0}, "limit": 5, "sort": {"field": "due_date", "order": "desc"}, "reference_date": null, "is_bill_query": true, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending", "overdue_only": true}`

---

### Query: `Give me the ageing buckets of 45, 90, 120 days March 2025 for Jagat based on due date with amount less than 50000 showing top 50 sorted by amount descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Jagat`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": {"operator": "<", "value": 50000.0}, "limit": 50, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [45, 90, 120]}`

---

### Query: `List all receivable bills between April and September 2026 for Acme Corp based on due date with amount greater than 50000 less than 60 days old showing top 5 sorted by amount descending`
- **Intent:** `GET_PAYABLES`
- **Ledger:** `Acme Corp`
- **Parameters:** `{"date_filter": {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": 2026, "end_day": 30, "end_month": 9, "end_year": 2026}, "age_filter": {"operator": "<", "days": 60}, "amount_filter": {"operator": ">", "value": 50000.0}, "limit": 5, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": "pending"}`

---

### Query: `Give me the ageing buckets of 10, 20, 30, 40 days March 2025 for Wipro based on due date with amount greater than 150000 showing top 20 sorted by amount descending`
- **Intent:** `GET_AGEING`
- **Ledger:** `Wipro`
- **Parameters:** `{"date_filter": {"type": "month_year", "month": 3, "year": 2025}, "age_filter": null, "amount_filter": {"operator": ">", "value": 150000.0}, "limit": 20, "sort": {"field": "amount", "order": "desc"}, "reference_date": null, "is_bill_query": false, "document_ref": null, "date_target": "due_date", "count_only": false, "sum_only": false, "status_filter": null, "ageing_intervals": [10, 20, 30, 40]}`

---

