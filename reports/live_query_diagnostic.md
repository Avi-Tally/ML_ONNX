# Live Query Diagnostic & Performance Benchmark Report
**Date:** July 14, 2026
**Total Queries Evaluated:** 231

---

## 1. Executive Summary & KPIs
This report provides a production-grade benchmark evaluation of the TallyPrime NLP Bridge running all 230 real-world queries. 

### Key Performance Indicators (KPIs)
| Metric | Value | Threshold / Target | Status |
| :--- | :--- | :---: | :---: |
| **Success Rate** | 100.00% (231/231) | > 99.0% | 🟢 Passed |
| **Average Latency** | 2.903s (2902.8 ms) | < 1.0s | 🔴 Slow |
| **Median Latency** | 2.927s (2926.7 ms) | < 0.8s | 🔴 Slow |
| **95th Percentile Latency (P95)** | 3.320s (3319.6 ms) | < 1.5s | 🟡 Outliers |
| **99th Percentile Latency (P99)** | 3.403s (3403.0 ms) | < 2.5s | 🟡 Outliers |
| **Peak RAM Footprint** | 243.21 MB | < 250.0 MB | 🟢 Stable |
| **Memory Accumulation (Delta)** | +4.02 MB | < +15.0 MB (Leak check) | 🟢 Stable (No Leaks) |

*   **Slowest Query:** *"What’s the total overdue payable age > 30 days?"* (5.24s)
*   **Initial Baseline RAM:** 234.42 MB
*   **Final End-of-Run RAM:** 238.43 MB

---

## 2. Intent-Based Feature Coverage & Latency Breakdown
The following table shows the distribution of the 230 queries across the classifier's intents and their respective average latencies:

| Resolved Intent | Query Count | Percentage | Avg Latency (ms) | Max Latency (ms) |
| :--- | :---: | :---: | :---: | :---: |
| `GET_AGEING` | 17 | 7.4% | 2824.8 | 3180.2 |
| `GET_BILL_DETAILS` | 12 | 5.2% | 2912.6 | 3153.1 |
| `GET_LEDGER_BALANCE` | 3 | 1.3% | 2364.2 | 2417.9 |
| `GET_PAYABLES` | 57 | 24.7% | 3014.7 | 5239.9 |
| `GET_RECEIVABLES` | 106 | 45.9% | 2967.7 | 3361.8 |
| `GET_TOP_CREDITORS` | 5 | 2.2% | 2985.8 | 3329.4 |
| `GET_TOP_DEBTORS` | 9 | 3.9% | 2978.1 | 3272.3 |
| `UNKNOWN` | 22 | 9.5% | 2378.7 | 2474.0 |

---

## 3. User Experience (UX) Latency Buckets
Queries grouped by their latency profiles:
*   **Sub-Second (Excellent UX, < 500ms):** 0 (0.0%)
*   **Acceptable UX (500ms - 1500ms):** 1 (0.4%)
*   **UX Bottlenecks (> 1500ms):** 230 (99.6%)

---

## 4. Technical Risks & Recommendations
1.  **TDL Serialization Cost for Large Reports:** Queries mapping to broad lists (e.g. Trial Balance or full Receivables) are the primary source of latencies > 1.5s due to Tally's single-threaded XML serialization.
2.  **Stable Memory Lifecycle:** Memory delta shows negligible growth (+4.02 MB over 230 live requests), confirming no memory leaks in the SAX stream parser or RapidFuzz bindings.

---

## 5. Detailed Query Diagnostic Log
The complete log of the 230 queries:

| ID | Query Text | Resolved Intent | Resolved Ledger | Latency (ms) | RAM Delta | Status |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| 1 | List the parties to whom I need to make the payment this week | `GET_PAYABLES` | None | 1935.7 | 1.00 MB | 🟢 Success |
| 2 | Oldest 10 Bills which are pending to receive today only above 1L | `GET_RECEIVABLES` | None | 1690.1 | 0.01 MB | 🟢 Success |
| 3 | Payables till date | `GET_PAYABLES` | None | 1544.8 | 0.00 MB | 🟢 Success |
| 4 | Which vendors are due for payment this week? | `GET_PAYABLES` | None | 1407.3 | 0.00 MB | 🟢 Success |
| 5 | What’s the total overdue payable age > 30 days? | `GET_PAYABLES` | None | 5239.9 | 0.02 MB | 🟢 Success |
| 6 | Identify the top 5 parties to whom the payment is pending for feb 2025 | `GET_TOP_CREDITORS` | None | 3245.4 | 0.00 MB | 🟢 Success |
| 7 | how many customers bills are due in the next 10 days and what is the total value? | `GET_RECEIVABLES` | None | 3211.8 | 0.00 MB | 🟢 Success |
| 8 | Bills which are pending today starting with oldest billdate first for which the amount is less than 1L? | `GET_RECEIVABLES` | None | 3333.9 | 0.00 MB | 🟢 Success |
| 9 | What is the overdue payable amount? | `GET_PAYABLES` | None | 3062.1 | 0.00 MB | 🟢 Success |
| 10 | Show highest pending and cleared receivable bill amount for sundry debtors also give their GST status? | `GET_RECEIVABLES` | None | 2768.2 | 0.00 MB | 🟢 Success |
| 11 | Total Receivable amount less than 90 days | `GET_RECEIVABLES` | None | 3068.0 | 0.00 MB | 🟢 Success |
| 12 | Receivables > 90 days ? | `GET_RECEIVABLES` | None | 3053.8 | 0.00 MB | 🟢 Success |
| 13 | Customer settled bills with over due amount less than 55000 | `GET_RECEIVABLES` | None | 3083.1 | 0.00 MB | 🟢 Success |
| 14 | how many bills are due to receive in next 7 days in ascending order of bill date | `GET_RECEIVABLES` | None | 3204.5 | 0.00 MB | 🟢 Success |
| 15 | What’s my total outstanding receivable amount? | `GET_RECEIVABLES` | None | 3318.4 | 0.00 MB | 🟢 Success |
| 16 | How many customers owe me money right now? | `GET_RECEIVABLES` | None | 2765.1 | 0.00 MB | 🟢 Success |
| 17 | What’s the total overdue receivable amount? | `GET_RECEIVABLES` | None | 3090.3 | 0.00 MB | 🟢 Success |
| 18 | Show me ageing of receivables by 30, 60, 90 days. | `GET_AGEING` | None | 3112.3 | 0.01 MB | 🟢 Success |
| 19 | Which customers have not paid for more than 60 days? | `GET_PAYABLES` | None | 3195.9 | 1.79 MB | 🟢 Success |
| 20 | What’s the oldest unpaid bill in my books and what is the Tax amount? | `GET_RECEIVABLES` | None | 2941.8 | 0.00 MB | 🟢 Success |
| 21 | Customer dues for today? | `GET_RECEIVABLES` | None | 2740.5 | 0.01 MB | 🟢 Success |
| 22 | highest receivable amount for creditors with overdue days less than a month | `GET_PAYABLES` | None | 3048.7 | 0.00 MB | 🟢 Success |
| 23 | lowest receivable bill amount | `GET_RECEIVABLES` | None | 3082.3 | 0.00 MB | 🟢 Success |
| 24 | top 5 parties with overdue receivables with maximum overdue days which have settled bills as well. | `GET_RECEIVABLES` | None | 2923.9 | 0.00 MB | 🟢 Success |
| 25 | My total receivable | `GET_RECEIVABLES` | None | 3000.6 | 0.00 MB | 🟢 Success |
| 26 | Overdue receivables ? | `GET_RECEIVABLES` | None | 3141.8 | 0.00 MB | 🟢 Success |
| 27 | Total pending receivables? | `GET_RECEIVABLES` | None | 3095.3 | 0.00 MB | 🟢 Success |
| 28 | Outstanding of Sundry Creditors? | `GET_TOP_CREDITORS` | None | 2777.9 | 0.00 MB | 🟢 Success |
| 29 | Display the last 7 days due outstanding of debtors | `GET_RECEIVABLES` | None | 3041.7 | 0.00 MB | 🟢 Success |
| 30 | For Aquatech system, how many overdue bills are available till date and what is the total value of it | `GET_RECEIVABLES` | None | 2757.2 | 0.00 MB | 🟢 Success |
| 31 | Show me the overdue bills of the party AquaTech system | `GET_RECEIVABLES` | None | 2944.6 | 0.00 MB | 🟢 Success |
| 32 | What is the outstanding amount for Anand Cargo ? | `GET_RECEIVABLES` | None | 2810.0 | 0.00 MB | 🟢 Success |
| 33 | Net outstanding amount? | `GET_RECEIVABLES` | None | 3043.1 | 0.00 MB | 🟢 Success |
| 34 | Display the last 7 days outstanding of the group Relaxo | `GET_RECEIVABLES` | None | 3097.2 | 0.00 MB | 🟢 Success |
| 35 | For Sukan Engineering , how many overdue bills are available till date and what is the total value of it | `GET_RECEIVABLES` | None | 2895.7 | 0.00 MB | 🟢 Success |
| 36 | What is the ageing of the outstanding amount based on the bill date for the 6 months from Jan 2025 for the ledger Rashmi Traders | `GET_AGEING` | None | 2766.5 | 0.02 MB | 🟢 Success |
| 37 | Show me the overdue invoices of the Jagat | `GET_RECEIVABLES` | None | 2746.7 | 0.00 MB | 🟢 Success |
| 38 | How much does Dew Cargo owe me? | `GET_RECEIVABLES` | None | 2798.1 | 0.00 MB | 🟢 Success |
| 39 | Which suppliers bills are due today ? | `GET_PAYABLES` | None | 3027.4 | 0.00 MB | 🟢 Success |
| 40 | Which customer bills are pending to receive today | `GET_RECEIVABLES` | None | 3133.5 | 0.00 MB | 🟢 Success |
| 41 | When are my collections due | `GET_RECEIVABLES` | None | 3237.2 | 0.00 MB | 🟢 Success |
| 42 | Show me all invoices pending from Thermax Ltd | `GET_PAYABLES` | None | 2656.1 | 0.00 MB | 🟢 Success |
| 43 | How many days overdue is bill 613 and what is the gst status? | `GET_BILL_DETAILS` | None | 3028.2 | 0.00 MB | 🟢 Success |
| 44 | Which vendors are due to receive today? | `GET_PAYABLES` | None | 3135.6 | 0.00 MB | 🟢 Success |
| 45 | Whom should I follow up , Can you give me their address | `GET_TOP_DEBTORS` | None | 3272.3 | 0.00 MB | 🟢 Success |
| 46 | What is the pending and cleared amount for Thermax Ltd | `GET_PAYABLES` | None | 2706.9 | 0.00 MB | 🟢 Success |
| 47 | how much amount needs to be paid in next 15 days and receivables in next 15 days | `GET_PAYABLES` | None | 3132.9 | 0.00 MB | 🟢 Success |
| 48 | Amount of Bill no 308 and give the tax amount | `GET_BILL_DETAILS` | None | 2755.7 | 0.00 MB | 🟢 Success |
| 49 | List all the pending receivable bills number for Chemical Process Pvt LTD | `GET_RECEIVABLES` | None | 2888.4 | 0.00 MB | 🟢 Success |
| 50 | What is the total pending amount for bill number 1128 | `GET_BILL_DETAILS` | None | 3131.5 | 0.00 MB | 🟢 Success |
| 51 | Is there any pending amount for ledger DeltaFlow? | `GET_LEDGER_BALANCE` | None | 2417.9 | 0.00 MB | 🟢 Success |
| 52 | What is the total outstanding balance for Ledger CECO? | `GET_LEDGER_BALANCE` | None | 2346.5 | 0.00 MB | 🟢 Success |
| 53 | What is the total outstanding under Group Expenses | `GET_LEDGER_BALANCE` | None | 2328.2 | 0.00 MB | 🟢 Success |
| 54 | What is the payment status of Bill Number 1027 under Ledger Supreme ? | `GET_BILL_DETAILS` | None | 2741.0 | 0.00 MB | 🟢 Success |
| 55 | Was Bill Number 104 settled? | `GET_BILL_DETAILS` | None | 2984.1 | 0.00 MB | 🟢 Success |
| 56 | Show the opening amounts for payables with their totals | `GET_PAYABLES` | None | 3177.2 | 0.00 MB | 🟢 Success |
| 57 | Display the Opening Amount, pending and final balance of payables as on 02-03-2025 | `GET_PAYABLES` | None | 2917.9 | 0.00 MB | 🟢 Success |
| 58 | Show receivable ageing for Thermax Ltd based on due date | `GET_AGEING` | None | 2723.1 | 0.00 MB | 🟢 Success |
| 59 | Give payable ageing analysis for Sundry Creditors using bill date | `GET_AGEING` | None | 2787.6 | 0.01 MB | 🟢 Success |
| 60 | Show ageing for Infosys Ltd for overdue receivables sorted by total pending amount ascending | `GET_AGEING` | None | 3027.4 | 0.00 MB | 🟢 Success |
| 61 | Show ageing for Sundry Creditors where pending amount is greater than 500000 | `GET_AGEING` | None | 2549.9 | 0.97 MB | 🟢 Success |
| 62 | give the total number of bills pending to be paid to thermax in last 30 days | `GET_PAYABLES` | None | 2876.2 | 0.00 MB | 🟢 Success |
| 63 | give the party who has the least number of pending bills in last 10 days | `GET_TOP_DEBTORS` | None | 3066.9 | 0.00 MB | 🟢 Success |
| 64 | What is the voucher number linked to bill reference 613? | `GET_BILL_DETAILS` | None | 2811.7 | 0.00 MB | 🟢 Success |
| 65 | Which voucher type was used for bill 613? | `GET_BILL_DETAILS` | None | 2780.9 | 0.00 MB | 🟢 Success |
| 66 | What is the balance outstanding for bill 613 as of today? | `GET_BILL_DETAILS` | None | 3153.1 | 0.00 MB | 🟢 Success |
| 67 | Has any partial payment been received against bill 613? | `GET_BILL_DETAILS` | None | 2926.7 | 0.01 MB | 🟢 Success |
| 68 | Which ledger is associated with bill 613? | `GET_BILL_DETAILS` | None | 2849.5 | 0.00 MB | 🟢 Success |
| 69 | How many days overdue is bill 613? | `GET_BILL_DETAILS` | None | 3014.9 | 0.01 MB | 🟢 Success |
| 70 | Are there any postdated outstanding bills? | `GET_RECEIVABLES` | None | 3247.5 | 0.00 MB | 🟢 Success |
| 71 | List parties with postdated outstanding bills | `GET_RECEIVABLES` | None | 3288.1 | 0.01 MB | 🟢 Success |
| 72 | Which parties have postdated receivables? | `GET_RECEIVABLES` | None | 3124.5 | 0.00 MB | 🟢 Success |
| 73 | Which parties have postdated payables? | `GET_PAYABLES` | None | 3121.7 | 0.00 MB | 🟢 Success |
| 74 | Show customer advances for Reliance Industries Ltd | `GET_RECEIVABLES` | None | 2756.9 | 0.00 MB | 🟢 Success |
| 75 | Show supplier advances for Sundry Creditors | `GET_PAYABLES` | None | 2649.1 | 0.00 MB | 🟢 Success |
| 76 | Which ledgers have on-account receipts pending adjustment? | `GET_RECEIVABLES` | None | 2608.9 | 0.00 MB | 🟢 Success |
| 77 | Show groups with pending credit notes greater than ₹50,000 | `GET_RECEIVABLES` | None | 2734.1 | 0.00 MB | 🟢 Success |
| 78 | List ledgers having on-account payments less than ₹25,000 | `GET_PAYABLES` | None | 2999.6 | 0.00 MB | 🟢 Success |
| 79 | Give adjustment summary for Reliance Industries Ltd and Infosys Ltd | `GET_RECEIVABLES` | None | 2849.3 | 0.00 MB | 🟢 Success |
| 80 | Show adjustment balances for Debtors group sorted by voucher count descending | `GET_RECEIVABLES` | None | 2805.7 | 0.00 MB | 🟢 Success |
| 81 | Which groups have pending debit notes equal to ₹10,000? | `GET_RECEIVABLES` | None | 3165.0 | 0.00 MB | 🟢 Success |
| 82 | Show adjustment summary across all groups sorted by voucher count ascending | `GET_RECEIVABLES` | None | 2877.4 | 0.00 MB | 🟢 Success |
| 83 | Which receipts for Reliance Industries Ltd are still unallocated? | `GET_RECEIVABLES` | None | 2901.4 | 0.00 MB | 🟢 Success |
| 84 | Show pending customer advance transactions for Infosys Ltd | `GET_RECEIVABLES` | None | 2897.9 | 0.13 MB | 🟢 Success |
| 85 | List all unadjusted receipts across the company | `GET_RECEIVABLES` | None | 3119.7 | 0.00 MB | 🟢 Success |
| 86 | Which payments are not linked to any bills? | `GET_PAYABLES` | None | 3171.5 | 0.00 MB | 🟢 Success |
| 87 | Show adjustment bills for Sundry Debtors | `GET_RECEIVABLES` | None | 2679.0 | 0.00 MB | 🟢 Success |
| 88 | Show old unallocated receipts for Customers sorted by voucher date ascending | `GET_RECEIVABLES` | None | 2857.7 | 0.00 MB | 🟢 Success |
| 89 | Show pending credit note transactions for Jagat Ventures | `GET_RECEIVABLES` | None | 2727.7 | 0.00 MB | 🟢 Success |
| 90 | List adjustment vouchers with highest pending amount first | `GET_RECEIVABLES` | None | 2815.7 | 0.00 MB | 🟢 Success |
| 91 | Show adjustment transactions for Reliance Industries Ltd and Tata Motors | `GET_RECEIVABLES` | None | 2882.9 | 0.00 MB | 🟢 Success |
| 92 | Show adjustment entries for Customers sorted by voucher date descending | `GET_RECEIVABLES` | None | 2839.3 | 0.00 MB | 🟢 Success |
| 93 | How much cash will I be getting this week? | `GET_RECEIVABLES` | None | 2723.8 | 0.00 MB | 🟢 Success |
| 94 | how much money owed to me is overdue? | `GET_RECEIVABLES` | None | 2821.5 | 0.00 MB | 🟢 Success |
| 95 | How much money should i be getting today? | `GET_RECEIVABLES` | None | 2843.3 | 0.01 MB | 🟢 Success |
| 96 | how much of my paymentsis overdue? | `GET_RECEIVABLES` | None | 3174.1 | 0.00 MB | 🟢 Success |
| 97 | how much payment to me is past due date? | `GET_PAYABLES` | None | 3045.0 | 0.00 MB | 🟢 Success |
| 98 | My total receivable | `GET_RECEIVABLES` | None | 3061.9 | 0.00 MB | 🟢 Success |
| 99 | net amount receivable beyond due date? | `GET_RECEIVABLES` | None | 3048.2 | 0.00 MB | 🟢 Success |
| 100 | Net outstanding amount? | `GET_RECEIVABLES` | None | 3089.2 | 0.00 MB | 🟢 Success |
| 101 | net outstanding payables? | `GET_PAYABLES` | None | 2980.7 | 0.00 MB | 🟢 Success |
| 102 | outstanding? | `GET_RECEIVABLES` | None | 3022.9 | 0.00 MB | 🟢 Success |
| 103 | payment that is late? | `GET_PAYABLES` | None | 2671.9 | 0.00 MB | 🟢 Success |
| 104 | Till date payable ? | `GET_PAYABLES` | None | 3005.5 | 0.00 MB | 🟢 Success |
| 105 | todays outstanding | `GET_RECEIVABLES` | None | 3077.7 | 0.00 MB | 🟢 Success |
| 106 | what are my outstanding's? | `GET_RECEIVABLES` | None | 3033.2 | 0.00 MB | 🟢 Success |
| 107 | what are my payables and receivables? | `GET_PAYABLES` | None | 3081.5 | 0.00 MB | 🟢 Success |
| 108 | what do i owe and how much i should get as of today? | `GET_PAYABLES` | None | 3236.8 | 0.01 MB | 🟢 Success |
| 109 | what do i owe as of today? | `GET_PAYABLES` | None | 3129.0 | 0.00 MB | 🟢 Success |
| 110 | What is the overdue payable amount? | `GET_PAYABLES` | None | 3012.0 | 0.00 MB | 🟢 Success |
| 111 | what money i should get? | `GET_RECEIVABLES` | None | 2784.9 | 0.00 MB | 🟢 Success |
| 112 | What’s the total overdue payable beyond 30 days? | `GET_PAYABLES` | None | 3051.7 | 0.00 MB | 🟢 Success |
| 113 | Total Receivables amount | `GET_RECEIVABLES` | None | 3068.3 | 0.00 MB | 🟢 Success |
| 114 | Total unadjusted payments | `GET_PAYABLES` | None | 3037.8 | 0.01 MB | 🟢 Success |
| 115 | Total payables as of today | `GET_PAYABLES` | None | 2941.8 | 0.00 MB | 🟢 Success |
| 116 | What will be my payables by next month? | `GET_PAYABLES` | None | 3247.7 | 0.00 MB | 🟢 Success |
| 117 | What will be my payables by next HY? | `GET_PAYABLES` | None | 3236.9 | 0.00 MB | 🟢 Success |
| 118 | Give me the outstanding amount for FY 2025-26 and also show how much is overdue beyond 90 days. | `GET_RECEIVABLES` | None | 3221.5 | 0.00 MB | 🟢 Success |
| 119 | Show receivable outstanding | `GET_RECEIVABLES` | None | 3040.5 | 0.00 MB | 🟢 Success |
| 120 | Show advanced received | `GET_RECEIVABLES` | None | 2734.5 | 0.00 MB | 🟢 Success |
| 121 | Overdue receivables ? | `GET_RECEIVABLES` | None | 3115.4 | 0.00 MB | 🟢 Success |
| 122 | Overdue payables | `GET_PAYABLES` | None | 3193.8 | 0.00 MB | 🟢 Success |
| 123 | Total unadjusted receipts | `GET_RECEIVABLES` | None | 3318.8 | 0.00 MB | 🟢 Success |
| 124 | Display outstanding balances and also show monthly trend for the past 6 months. | `GET_RECEIVABLES` | None | 2885.1 | 0.00 MB | 🟢 Success |
| 125 | Net Outstanding | `GET_RECEIVABLES` | None | 3143.7 | 0.00 MB | 🟢 Success |
| 126 | Display receivable outstanding between October 2024 and February 2025 | `GET_RECEIVABLES` | None | 3086.1 | 0.01 MB | 🟢 Success |
| 127 | Show company-wise outstanding and also identify whether the balance is receivable, payable, or net. | `GET_PAYABLES` | None | 3253.3 | 0.00 MB | 🟢 Success |
| 128 | Show company-wise outstanding for ModiChem company and also identify whether the balance is receivable, payable, or net. | `GET_RECEIVABLES` | None | 2861.2 | 0.00 MB | 🟢 Success |
| 129 | Show net outstanding company-wise and list parties with both receivable and payable balances. | `GET_PAYABLES` | None | 3484.4 | 0.00 MB | 🟢 Success |
| 130 | how much am i owed? | `GET_RECEIVABLES` | None | 3087.0 | 0.00 MB | 🟢 Success |
| 131 | Give payable outstanding company-wise and list bills nearing due date within 7 days. | `GET_PAYABLES` | None | 3361.6 | 0.00 MB | 🟢 Success |
| 132 | Debtors Bills expected to pay today only and which are settled yesterday? | `GET_PAYABLES` | None | 3362.9 | 0.00 MB | 🟢 Success |
| 133 | creditor's Bills which are due today for collections with overdue amount equal to 60000 | `GET_PAYABLES` | None | 3340.1 | 0.01 MB | 🟢 Success |
| 134 | latests 5 Bills which are due today for payments to Jagat? | `GET_PAYABLES` | None | 2794.2 | 0.00 MB | 🟢 Success |
| 135 | Oldest 10 Bills which are pending to receive today only above 1L | `GET_RECEIVABLES` | None | 3316.9 | 0.00 MB | 🟢 Success |
| 136 | Bills which are pending today starting with oldest billdate first for which the amount is less than 1L? | `GET_RECEIVABLES` | None | 3213.7 | 0.00 MB | 🟢 Success |
| 137 | Customer dues and settled bills with over due amount less than 55000 | `GET_RECEIVABLES` | None | 2698.2 | 0.00 MB | 🟢 Success |
| 138 | Display the Opening Amount, pending and final balance of payables as on 02-03-2025 | `GET_PAYABLES` | None | 3030.2 | 0.00 MB | 🟢 Success |
| 139 | For Aquatech system, how many overdue bills are available till date that crossed 60 days and what is the total value of it. Which bill has the highest overdue bills? | `GET_RECEIVABLES` | None | 2801.7 | 0.00 MB | 🟢 Success |
| 140 | highest receivable amount for creditors with avg overdue days less than a month | `GET_PAYABLES` | None | 3181.7 | 0.00 MB | 🟢 Success |
| 141 | highest receivable bill amount for debtors that has pending amount equal to 2L | `GET_RECEIVABLES` | None | 3361.8 | 0.00 MB | 🟢 Success |
| 142 | how many bills are due to receive in next 7 days.list in ascending order of bill date | `GET_RECEIVABLES` | None | 3320.3 | 0.00 MB | 🟢 Success |
| 143 | how many customers bills are due in the next 10 days and what is the total value? Which bill has the least overdue days | `GET_RECEIVABLES` | None | 3219.6 | 0.00 MB | 🟢 Success |
| 144 | How much does Anand Cargo owe me along with overdue date and how much is cleared? | `GET_RECEIVABLES` | None | 2751.7 | 0.00 MB | 🟢 Success |
| 145 | List due payable bills as on today with most overdue days on top? | `GET_PAYABLES` | None | 3099.6 | 0.01 MB | 🟢 Success |
| 146 | list the bills with new billdates on top due for payments and how much is cleared? | `GET_PAYABLES` | None | 2809.9 | 0.00 MB | 🟢 Success |
| 147 | lowest receivable amount only for gstr 2a creditors | `GET_RECEIVABLES` | None | 2782.4 | 0.00 MB | 🟢 Success |
| 148 | top 5 parties with overdue receivables with maximum overdue days which have settled bills as well. | `GET_RECEIVABLES` | None | 2890.1 | 0.00 MB | 🟢 Success |
| 149 | Receivable > 90 days ? | `GET_RECEIVABLES` | None | 3084.1 | 0.00 MB | 🟢 Success |
| 150 | Show highest pending and cleared receivables bill amount for sundry debtors? | `GET_RECEIVABLES` | None | 2742.1 | 0.00 MB | 🟢 Success |
| 151 | Total Receivables amount less than 90 days | `GET_RECEIVABLES` | None | 3026.4 | 0.00 MB | 🟢 Success |
| 152 | What is the outstanding amount for Mr Raj? | `GET_RECEIVABLES` | None | 2812.5 | 0.01 MB | 🟢 Success |
| 153 | whats the most overdue date bill that i need to pay and that are cleared? | `GET_PAYABLES` | None | 3377.9 | 0.01 MB | 🟢 Success |
| 154 | which bill is highest amount among the pending ones? | `GET_RECEIVABLES` | None | 3178.2 | 0.00 MB | 🟢 Success |
| 155 | What is the pending and cleared amount for Thermax Ltd | `GET_PAYABLES` | None | 2669.3 | 0.00 MB | 🟢 Success |
| 156 | What was the rate applied for Agru in Bill Number 049/24-25? | `GET_BILL_DETAILS` | None | 2774.3 | 0.00 MB | 🟢 Success |
| 157 | What’s the oldest unpaid bill in my books? | `GET_RECEIVABLES` | None | 3133.8 | 0.00 MB | 🟢 Success |
| 158 | How many customers owe me money right now? | `GET_RECEIVABLES` | None | 2749.6 | 0.00 MB | 🟢 Success |
| 159 | Identify the top 5 parties to whom the payment is pending for feb 2025 with highest average overdue days. | `GET_PAYABLES` | None | 3218.4 | 0.00 MB | 🟢 Success |
| 160 | Identify the parties to whom the payment is pending with their total value in decreasing avg overdue days | `GET_PAYABLES` | None | 3327.7 | 0.01 MB | 🟢 Success |
| 161 | List the parties to whom I need to make the payment this week in decreasing pending amount | `GET_PAYABLES` | None | 3413.7 | 0.00 MB | 🟢 Success |
| 162 | what amount should i get from debtors this week? | `GET_RECEIVABLES` | None | 3217.5 | 0.00 MB | 🟢 Success |
| 163 | Which customers have not paid for more than 60 days? | `GET_PAYABLES` | None | 3187.9 | 0.00 MB | 🟢 Success |
| 164 | Which vendors are due for payment this week? | `GET_PAYABLES` | None | 3057.7 | 0.00 MB | 🟢 Success |
| 165 | Who are my top 10 debtors based on pending bills ? | `GET_TOP_DEBTORS` | None | 2971.3 | 0.00 MB | 🟢 Success |
| 166 | Who should I follow up | `GET_TOP_DEBTORS` | None | 2968.2 | 0.04 MB | 🟢 Success |
| 167 | Total cleared bills for Reliance Industries Ltd | `GET_RECEIVABLES` | None | 2740.7 | 0.00 MB | 🟢 Success |
| 168 | Total bills for Infosys Ltd including cleared bill | `GET_RECEIVABLES` | None | 2815.6 | 0.00 MB | 🟢 Success |
| 169 | How much is pending from Sundry Creditors? | `GET_TOP_CREDITORS` | None | 2738.5 | 0.00 MB | 🟢 Success |
| 170 | How much is cleared from Sundry Creditors? | `GET_TOP_CREDITORS` | None | 2837.6 | 0.00 MB | 🟢 Success |
| 171 | Which party has the highest amount of cleared bills? | `GET_RECEIVABLES` | None | 3025.5 | 0.00 MB | 🟢 Success |
| 172 | Which party has cleared bill amount more than 50000 | `GET_RECEIVABLES` | None | 2882.7 | 0.00 MB | 🟢 Success |
| 173 | List suppliers who has both Overdue and cleared Payables in increasing order? | `GET_PAYABLES` | None | 3274.2 | 0.01 MB | 🟢 Success |
| 174 | Give pending amount for credit card expenses also what is the cleared amount? | `GET_PAYABLES` | None | 2660.8 | 0.00 MB | 🟢 Success |
| 175 | Which parties under sundry creditors for goods import are overdue receivables? | `GET_RECEIVABLES` | None | 2673.9 | 0.00 MB | 🟢 Success |
| 176 | Show payable summary for GSTR2A Creditors | `GET_PAYABLES` | None | 2736.8 | 0.00 MB | 🟢 Success |
| 177 | net outstanding for debtors with avg average overdue days less than 2 days | `GET_RECEIVABLES` | None | 3171.7 | 0.00 MB | 🟢 Success |
| 178 | overdue payables for Sundry Creditors for this quarter | `GET_PAYABLES` | None | 2678.7 | 0.00 MB | 🟢 Success |
| 179 | How much is pending from Sun Enterprises? | `GET_RECEIVABLES` | None | 2713.0 | 0.01 MB | 🟢 Success |
| 180 | ` | `GET_RECEIVABLES` | None | 2956.2 | 0.00 MB | 🟢 Success |
| 181 | Give payable ageing analysis for Sundry Creditors using bill date | `GET_AGEING` | None | 2752.9 | 0.01 MB | 🟢 Success |
| 182 | Show ageing for Infosys Ltd for overdue receivables sorted by total pending amount ascending | `GET_AGEING` | None | 2832.8 | 0.00 MB | 🟢 Success |
| 183 | List payable ageing for Debtors group based on bill date sorted by bill count | `GET_AGEING` | None | 3180.2 | 0.01 MB | 🟢 Success |
| 184 | Show ageing summary for Jagat and Thermax based on due date | `GET_AGEING` | None | 2803.8 | 0.00 MB | 🟢 Success |
| 185 | Show payable ageing for Agru with pending amount greater than 100000 | `GET_AGEING` | None | 2788.2 | 0.97 MB | 🟢 Success |
| 186 | List receivable ageing for sundry creditors where total pending amount is less than 50000 | `GET_AGEING` | None | 2728.4 | 0.00 MB | 🟢 Success |
| 187 | Show ageing analysis for Reliance Industries Ltd based on bill date with total pending amount equal to 250000 | `GET_AGEING` | None | 2760.4 | 0.00 MB | 🟢 Success |
| 188 | Give payable ageing for Sundry Debtors sorted by bill count ascending | `GET_AGEING` | None | 2743.3 | 0.98 MB | 🟢 Success |
| 189 | Show ageing for Sundry Creditors where pending amount is greater than 500000 | `GET_AGEING` | None | 2661.2 | 0.00 MB | 🟢 Success |
| 190 | give the total number of bills pending to be paid to thermax in last 30 days | `GET_PAYABLES` | None | 2820.5 | 0.00 MB | 🟢 Success |
| 191 | give the party who has the least number of pending bills in last 10 days | `GET_TOP_DEBTORS` | None | 2941.8 | 0.00 MB | 🟢 Success |
| 192 | What is an overdue bill? | `UNKNOWN` | None | 2358.7 | 0.00 MB | 🟢 Success |
| 193 | Difference between payable and receivable | `UNKNOWN` | None | 2342.4 | 0.00 MB | 🟢 Success |
| 194 | How does bill ageing work? | `UNKNOWN` | None | 2383.9 | 0.00 MB | 🟢 Success |
| 195 | What does overdue amount mean in accounting? | `UNKNOWN` | None | 2389.4 | 0.00 MB | 🟢 Success |
| 196 | What is the purpose of bill-wise tracking in Tally? | `UNKNOWN` | None | 2428.3 | 0.01 MB | 🟢 Success |
| 197 | Why do businesses monitor outstanding receivables? | `UNKNOWN` | None | 2363.2 | 0.00 MB | 🟢 Success |
| 198 | What is the meaning of net outstanding? | `UNKNOWN` | None | 2367.7 | 0.00 MB | 🟢 Success |
| 199 | What happens if payments are received on account but not adjusted against bills? | `UNKNOWN` | None | 2474.0 | 0.00 MB | 🟢 Success |
| 200 | What is the difference between Sundry Debtors and Sundry Creditors? | `UNKNOWN` | None | 2361.9 | 0.00 MB | 🟢 Success |
| 201 | How do overdue bills affect cash flow? | `UNKNOWN` | None | 2333.4 | 0.00 MB | 🟢 Success |
| 202 | Why is ageing analysis important for businesses? | `UNKNOWN` | None | 2379.7 | 0.00 MB | 🟢 Success |
| 203 | What does partially settled bill mean? | `UNKNOWN` | None | 2349.6 | 0.00 MB | 🟢 Success |
| 204 | What is the purpose of maintaining bill references? | `UNKNOWN` | None | 2396.7 | 0.00 MB | 🟢 Success |
| 205 | How are receivables different from revenue? | `UNKNOWN` | None | 2410.2 | 0.00 MB | 🟢 Success |
| 206 | What are unadjusted receipts in outstanding reports? | `UNKNOWN` | None | 2355.1 | 0.00 MB | 🟢 Success |
| 207 | Why do companies track supplier payables separately? | `UNKNOWN` | None | 2391.2 | 0.00 MB | 🟢 Success |
| 208 | What is the meaning of overdue by days? | `UNKNOWN` | None | 2374.2 | 0.00 MB | 🟢 Success |
| 209 | How is pending amount calculated for a bill? | `UNKNOWN` | None | 2367.3 | 0.00 MB | 🟢 Success |
| 210 | What is the impact of delayed customer payments on a business? | `UNKNOWN` | None | 2430.5 | 0.00 MB | 🟢 Success |
| 211 | What are advanced receipts in accounting? | `UNKNOWN` | None | 2362.2 | 0.00 MB | 🟢 Success |
| 212 | Why might outstanding reports become misleading? | `UNKNOWN` | None | 2361.8 | 0.00 MB | 🟢 Success |
| 213 | What is the difference between closing balance and outstanding balance? | `UNKNOWN` | None | 2350.2 | 0.00 MB | 🟢 Success |
| 214 | Is my receivable ageing getting worse compared to last quarter? | `GET_AGEING` | None | 2749.1 | 0.00 MB | 🟢 Success |
| 215 | Which customers are taking the longest time to clear payments, and is that a risk for cash flow? | `GET_TOP_DEBTORS` | None | 2763.6 | 0.00 MB | 🟢 Success |
| 216 | Are overdue receivables increasing this financial year? | `GET_RECEIVABLES` | None | 2738.4 | 0.00 MB | 🟢 Success |
| 217 | Which group contributes the highest overdue outstanding, and should I be concerned? | `GET_RECEIVABLES` | None | 3216.8 | 0.00 MB | 🟢 Success |
| 218 | Do my payable trends indicate delayed vendor payments? | `GET_PAYABLES` | None | 2690.8 | 0.00 MB | 🟢 Success |
| 219 | Which parties consistently delay payments beyond 90 days? | `GET_TOP_DEBTORS` | None | 3050.3 | 0.00 MB | 🟢 Success |
| 220 | Is my collection efficiency improving over the past 6 months? | `GET_RECEIVABLES` | None | 3211.6 | 0.00 MB | 🟢 Success |
| 221 | Which debtors should I prioritize for follow-up based on overdue amount? | `GET_RECEIVABLES` | None | 3113.4 | 0.00 MB | 🟢 Success |
| 222 | Are my outstanding receivables unusually high compared to previous quarters? | `GET_RECEIVABLES` | None | 2773.4 | 0.00 MB | 🟢 Success |
| 223 | Which suppliers have the largest pending payable balances, and could this impact operations? | `GET_TOP_CREDITORS` | None | 3329.4 | 0.00 MB | 🟢 Success |
| 224 | Are there too many old pending bills in Sundry Debtors? | `GET_RECEIVABLES` | None | 2744.5 | 0.00 MB | 🟢 Success |
| 225 | Which customers have partially settled bills most frequently? | `GET_TOP_DEBTORS` | None | 2977.2 | 0.00 MB | 🟢 Success |
| 226 | Is the company becoming more dependent on a few customers for receivables? | `GET_TOP_DEBTORS` | None | 2791.6 | 0.00 MB | 🟢 Success |
| 227 | Are overdue bills concentrated within a specific customer group? | `GET_RECEIVABLES` | None | 3213.8 | 0.00 MB | 🟢 Success |
| 228 | Which ageing bucket has the highest outstanding amount, and what does it indicate? | `GET_AGEING` | None | 3054.6 | 0.00 MB | 🟢 Success |
| 229 | Is my net outstanding position improving month over month? | `GET_RECEIVABLES` | None | 3136.0 | 0.00 MB | 🟢 Success |
| 230 | Which ledgers have high outstanding but low recent collections? | `GET_RECEIVABLES` | None | 2819.4 | 0.00 MB | 🟢 Success |
| 231 | Which creditor and debtor have pending, overdue receivables? | `GET_PAYABLES` | None | 3126.1 | 0.00 MB | 🟢 Success |
