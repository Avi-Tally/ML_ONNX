# Queries (1).xlsx Pipeline Confidence & Feasibility Report

**Total Queries Evaluated**: `482`  
**High Confidence (90-100%)**: `387` (`80.3%`)  
**Medium Confidence (70-89%)**: `30` (`6.2%`)  
**Low Confidence (<70%)**: `65` (`13.5%`)

---
## Query-by-Query Breakdown

| # | Query Text | Predicted Intent | Confidence | Technical Pipeline Analysis |
|---|---|---|:---:|---|
| 1 | `List the parties to whom I need to make the payment this week` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 2 | `Oldest 10 Bills which are pending to receive today only above 1L` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 3 | `Payables till date` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 4 | `Which vendors are due for payment this week?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 5 | `What’s the total overdue payable beyond 30 days?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 6 | `Identify the top 5 parties to whom the payment is pending for feb 2025` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 7 | `how many customers bills are due in the next 10 days and what is the total value?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 8 | `Bills which are pending today starting with oldest billdate first for which the amount is less than 1L?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 9 | `What is the overdue payable amount?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 10 | `Show highest pending and cleared receivables bill amount for sundry debtors also give their GST status?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES; GST / Tax attribute filter present |
| 11 | `Total Receivables amount less than 90 days` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 12 | `Receivable > 90 days ?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 13 | `Customer dues and settled bills with over due amount less than 55000` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 14 | `how many bills are due to receive in next 7 days.list in ascending order of bill date` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 15 | `What’s my total outstanding receivable amount?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 16 | `How many customers owe me money right now?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 17 | `What’s the total overdue receivable amount?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 18 | `Show me ageing of receivables by 30, 60, 90 days.` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 19 | `Which customers have not paid for more than 60 days?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 20 | `What’s the oldest unpaid bill in my books and what is the Tax amount?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 21 | `Customer dues for today?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 22 | `highest receivable amount for creditors with overdue days less than a month` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 23 | `lowest receivable bill amount` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 24 | `top 5 parties with overdue receivables with maximum overdue days which have settled bills as well.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 25 | `My total receivable` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 26 | `Overdue receivables ?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 27 | `Total pending receivables?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 28 | `Outstanding of Sundry Creditors?` | `GET_TOP_CREDITORS` | **100%** | Intent classified cleanly as GET_TOP_CREDITORS |
| 29 | `Display the last 7 days due outstanding of debtors` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 30 | `For Aquatech system, how many overdue bills are available till date and what is the total value of it` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 31 | `Show me the overdue bills of the party AquaTech system` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 32 | `What is the outstanding amount for Anand Cargo ?` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 33 | `Net outstanding amount?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 34 | `Display the last 7 days outstanding of the group Relaxo` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 35 | `For Sukan Engineering , how many overdue bills are available till date and what is the total value of it` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 36 | `What is the ageing of the outstanding amount based on the bill date for the 6 months from Jan 2025 for the ledger Rashmi Traders` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 37 | `Show me the overdue invoices of the Jagat` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 38 | `How much does Dew Cargo owe me?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 39 | `Which suppliers bills are due today ?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 40 | `Which customer bills are pending to receive today` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 41 | `When are my collections due` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 42 | `Show me all invoices pending from Thermax Ltd` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 43 | `How many days overdue is bill 613 and what is the gst status?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS; GST / Tax attribute filter present |
| 44 | `Which vendors are due to receive today?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 45 | `Whom should I follow up , Can you give me their address` | `GET_TOP_DEBTORS` | **100%** | Intent classified cleanly as GET_TOP_DEBTORS |
| 46 | `What is the pending and cleared amount for Thermax Ltd` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 47 | `how much amount needs to be paid in next 15 days and receivables in next 15 days` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 48 | `Amount of Bill no 308 for Abhishek and give the tax amount` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 49 | `List all the pending receivable bills number for Chemical Process Pvt LTD` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 50 | `What is the total pending amount for Chemical Process Pipping Pvt Ltd for bill number MODI/25-26/956` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 51 | `Is there any pending amount for ledger DeltaFlow?` | `GET_LEDGER_BALANCE` | **100%** | Intent classified cleanly as GET_LEDGER_BALANCE |
| 52 | `What is the total outstanding balance for Ledger CECO?` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 53 | `What is the total outstanding under Group Expenses` | `GET_LEDGER_BALANCE` | **100%** | Intent classified cleanly as GET_LEDGER_BALANCE |
| 54 | `What is the payment status of Bill Number 1027 under Ledger Supreme ?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 55 | `Was Bill Number 104 settled fully for Varad engineers?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 56 | `Show the opening amounts for payables with their totals` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES; Opening balance TDL collection supported |
| 57 | `Display the Opening Amount, pending and final balance of payables as on 02-03-2025` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES; Opening balance TDL collection supported |
| 58 | `Show receivable ageing for Thermax Ltd based on due date` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 59 | `Give payable ageing analysis for Sundry Creditors using bill date` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 60 | `Show ageing for Infosys Ltd for overdue receivables sorted by total pending amount ascending` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 61 | `Show ageing for Sundry Creditors where pending amount is greater than 500000` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 62 | `give the total number of bills pending to be paid to thermax in last 30 days` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 63 | `give the party who has the least number of pending bills in last 10 days` | `GET_TOP_DEBTORS` | **100%** | Intent classified cleanly as GET_TOP_DEBTORS |
| 64 | `What is the voucher number linked to bill reference 613?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 65 | `Which voucher type was used for bill 613?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 66 | `What is the balance outstanding for bill 613 as of today?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 67 | `Has any partial payment been received against bill 613?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 68 | `Which ledger is associated with bill 613?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 69 | `How many days overdue is bill 613?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 70 | `Are there any postdated outstanding bills?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES; PDC / Post-dated flag extracted |
| 71 | `List parties with postdated outstanding bills` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES; PDC / Post-dated flag extracted |
| 72 | `Which parties have postdated receivables?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES; PDC / Post-dated flag extracted |
| 73 | `Which parties have postdated payables?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES; PDC / Post-dated flag extracted |
| 74 | `Show customer advances for Reliance Industries Ltd` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 75 | `Show supplier advances for Sundry Creditors` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 76 | `Which ledgers have on-account receipts pending adjustment?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 77 | `Show groups with pending credit notes greater than ₹50,000` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 78 | `List ledgers having on-account payments less than ₹25,000` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 79 | `Give adjustment summary for Reliance Industries Ltd and Infosys Ltd` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 80 | `Show adjustment balances for Debtors group sorted by voucher count descending` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 81 | `Which groups have pending debit notes equal to ₹10,000?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 82 | `Show adjustment summary across all groups sorted by voucher count ascending` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 83 | `Which receipts for Reliance Industries Ltd are still unallocated?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 84 | `Show pending customer advance transactions for Infosys Ltd` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 85 | `List all unadjusted receipts across the company` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 86 | `Which payments are not linked to any bills?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 87 | `Show adjustment bills for Sundry Debtors` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 88 | `Show old unallocated receipts for Customers sorted by voucher date ascending` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 89 | `Show pending credit note transactions for Jagat Ventures` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 90 | `List adjustment vouchers with highest pending amount first` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 91 | `Show adjustment transactions for Reliance Industries Ltd and Tata Motors` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 92 | `Show adjustment entries for Customers sorted by voucher date descending` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 93 | `How much cash will I be getting this week?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 94 | `how much money owed to me is overdue?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 95 | `How much money should i be getting today?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 96 | `how much of my paymentsis overdue?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 97 | `how much payment to me is past due date?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 98 | `My total receivable` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 99 | `net amount receivable beyond due date?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 100 | `Net outstanding amount?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 101 | `net outstanding payables?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 102 | `outstanding?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 103 | `payment that is late?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 104 | `Till date payable ?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 105 | `todays outstanding` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 106 | `what are my outstanding's?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 107 | `what are my payables and receivables?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 108 | `what do i owe and how much i should get as of today?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 109 | `what do i owe as of today?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 110 | `What is the overdue payable amount?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 111 | `what money i should get?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 112 | `What’s the total overdue payable beyond 30 days?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 113 | `Total Receivables amount` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 114 | `Total unadjusted payments` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 115 | `Total payables as of today` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 116 | `What will be my payables by next month?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 117 | `What will be my payables by next HY?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 118 | `Give me the outstanding amount for FY 2025-26 and also show how much is overdue beyond 90 days.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 119 | `Show receivable outstanding` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 120 | `Show advanced received` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 121 | `Overdue receivables ?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 122 | `Overdue payables` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 123 | `Total unadjusted receipts` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 124 | `Display outstanding balances and also show monthly trend for the past 6 months.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 125 | `Net Outstanding` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 126 | `Display receivable outstanding between October 2024 and February 2025` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 127 | `Show company-wise outstanding and also identify whether the balance is receivable, payable, or net.` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 128 | `Show company-wise outstanding for ModiChem company and also identify whether the balance is receivable, payable, or net.` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 129 | `Show net outstanding company-wise and list parties with both receivable and payable balances.` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 130 | `how much am i owed?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 131 | `Give payable outstanding company-wise and list bills nearing due date within 7 days.` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 132 | `Debtors Bills expected to pay today only and which are settled yesterday?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 133 | `creditor's Bills which are due today for collections with overdue amount equal to 60000` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 134 | `latests 5 Bills which are due today for payments to Jagat?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 135 | `Oldest 10 Bills which are pending to receive today only above 1L` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 136 | `Bills which are pending today starting with oldest billdate first for which the amount is less than 1L?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 137 | `Customer dues and settled bills with over due amount less than 55000` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 138 | `Display the Opening Amount, pending and final balance of payables as on 02-03-2025` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES; Opening balance TDL collection supported |
| 139 | `For Aquatech system, how many overdue bills are available till date that crossed 60 days and what is the total value of it. Which bill has the highest overdue bills?` | `GET_LEDGER_360` | 75% | Intent 'GET_LEDGER_360' requires custom handler; Complex min/max sort requirement |
| 140 | `highest receivable amount for creditors with avg overdue days less than a month` | `GET_PAYABLES` | **90%** | Intent classified cleanly as GET_PAYABLES; Contains average calculation parameter (handled via Python stream aggregator) |
| 141 | `highest receivable bill amount for debtors that has pending amount equal to 2L` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 142 | `how many bills are due to receive in next 7 days.list in ascending order of bill date` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 143 | `how many customers bills are due in the next 10 days and what is the total value? Which bill has the least overdue days` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 144 | `How much does Anand Cargo owe me along with overdue date and how much is cleared?` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 145 | `List due payable bills as on today with most overdue days on top?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 146 | `list the bills with new billdates on top due for payments and how much is cleared?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 147 | `lowest receivable amount only for gstr 2a creditors` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES; GST / Tax attribute filter present |
| 148 | `top 5 parties with overdue receivables with maximum overdue days which have settled bills as well.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 149 | `Receivable > 90 days ?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 150 | `Show highest pending and cleared receivables bill amount for sundry debtors?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 151 | `Total Receivables amount less than 90 days` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 152 | `What is the outstanding amount for Mr Raj?` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 153 | `whats the most overdue date bill that i need to pay and that are cleared?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 154 | `which bill is highest amount among the pending ones?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 155 | `What is the pending and cleared amount for Thermax Ltd` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 156 | `What was the rate applied for Agru in Bill Number 049/24-25?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 157 | `What’s the oldest unpaid bill in my books?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 158 | `How many customers owe me money right now?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 159 | `Identify the top 5 parties to whom the payment is pending for feb 2025 with highest average overdue days.` | `GET_PAYABLES` | 85% | Intent classified cleanly as GET_PAYABLES; Contains average calculation parameter (handled via Python stream aggregator); Complex min/max sort requirement |
| 160 | `Identify the parties to whom the payment is pending with their total value in decreasing avg overdue days` | `GET_PAYABLES` | **90%** | Intent classified cleanly as GET_PAYABLES; Contains average calculation parameter (handled via Python stream aggregator) |
| 161 | `List the parties to whom I need to make the payment this week in decreasing pending amount` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 162 | `what amount should i get from debtors this week?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 163 | `Which customers have not paid for more than 60 days?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 164 | `Which vendors are due for payment this week?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 165 | `Who are my top 10 debtors based on pending bills ?` | `GET_TOP_DEBTORS` | **100%** | Intent classified cleanly as GET_TOP_DEBTORS |
| 166 | `Who should I follow up` | `GET_TOP_DEBTORS` | **100%** | Intent classified cleanly as GET_TOP_DEBTORS |
| 167 | `Total cleared bills for Reliance Industries Ltd` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 168 | `Total bills for Infosys Ltd including cleared bill` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 169 | `How much is pending from Sundry Creditors?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 170 | `How much is cleared from Sundry Creditors?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 171 | `Which party has the highest amount of cleared bills?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 172 | `Which party has cleared bill amount more than 50000` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 173 | `List suppliers who has both Overdue and cleared Payables in increasing order?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 174 | `Give pending amount for credit card expenses also what is the cleared amount?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 175 | `Which parties under sundry creditors for goods import are overdue receivables?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 176 | `Show payable summary for GSTR2A Creditors` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES; GST / Tax attribute filter present |
| 177 | `net outstanding for debtors with avg average overdue days less than 2 days` | `GET_RECEIVABLES` | **90%** | Intent classified cleanly as GET_RECEIVABLES; Contains average calculation parameter (handled via Python stream aggregator) |
| 178 | `overdue payables for Sundry Creditors for this quarter` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 179 | `How much is pending from Sun Enterprises?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 180 | ``` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 181 | `Give payable ageing analysis for Sundry Creditors using bill date` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 182 | `Show ageing for Infosys Ltd for overdue receivables sorted by total pending amount ascending` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 183 | `List payable ageing for Debtors group based on bill date sorted by bill count` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 184 | `Show ageing summary for Jagat and Thermax based on due date` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 185 | `Show payable ageing for Agru with pending amount greater than 100000` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 186 | `List receivable ageing for sundry creditors where total pending amount is less than 50000` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 187 | `Show ageing analysis for Reliance Industries Ltd based on bill date with total pending amount equal to 250000` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 188 | `Give payable ageing for Sundry Debtors sorted by bill count ascending` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 189 | `Show ageing for Sundry Creditors where pending amount is greater than 500000` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 190 | `give the total number of bills pending to be paid to thermax in last 30 days` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 191 | `give the party who has the least number of pending bills in last 10 days` | `GET_TOP_DEBTORS` | **100%** | Intent classified cleanly as GET_TOP_DEBTORS |
| 192 | `What is an overdue bill?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 193 | `Difference between payable and receivable` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 194 | `How does bill ageing work?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 195 | `What does overdue amount mean in accounting?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 196 | `What is the purpose of bill-wise tracking in Tally?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 197 | `Why do businesses monitor outstanding receivables?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 198 | `What is the meaning of net outstanding?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 199 | `What happens if payments are received on account but not adjusted against bills?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 200 | `What is the difference between Sundry Debtors and Sundry Creditors?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 201 | `How do overdue bills affect cash flow?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 202 | `Why is ageing analysis important for businesses?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 203 | `What does partially settled bill mean?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 204 | `What is the purpose of maintaining bill references?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 205 | `How are receivables different from revenue?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 206 | `What are unadjusted receipts in outstanding reports?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 207 | `Why do companies track supplier payables separately?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 208 | `What is the meaning of overdue by days?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 209 | `How is pending amount calculated for a bill?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 210 | `What is the impact of delayed customer payments on a business?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 211 | `What are advanced receipts in accounting?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 212 | `Why might outstanding reports become misleading?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 213 | `What is the difference between closing balance and outstanding balance?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 214 | `Is my receivable ageing getting worse compared to last quarter?` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 215 | `Which customers are taking the longest time to clear payments, and is that a risk for cash flow?` | `GET_TOP_DEBTORS` | **100%** | Intent classified cleanly as GET_TOP_DEBTORS |
| 216 | `Are overdue receivables increasing this financial year?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 217 | `Which group contributes the highest overdue outstanding, and should I be concerned?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 218 | `Do my payable trends indicate delayed vendor payments?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 219 | `Which parties consistently delay payments beyond 90 days?` | `GET_TOP_DEBTORS` | **100%** | Intent classified cleanly as GET_TOP_DEBTORS |
| 220 | `Is my collection efficiency improving over the past 6 months?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 221 | `Which debtors should I prioritize for follow-up based on overdue amount?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 222 | `Are my outstanding receivables unusually high compared to previous quarters?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 223 | `Which suppliers have the largest pending payable balances, and could this impact operations?` | `GET_TOP_CREDITORS` | **100%** | Intent classified cleanly as GET_TOP_CREDITORS |
| 224 | `Are there too many old pending bills in Sundry Debtors?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 225 | `Which customers have partially settled bills most frequently?` | `GET_TOP_DEBTORS` | **95%** | Intent classified cleanly as GET_TOP_DEBTORS; Complex min/max sort requirement |
| 226 | `Is the company becoming more dependent on a few customers for receivables?` | `GET_TOP_DEBTORS` | **100%** | Intent classified cleanly as GET_TOP_DEBTORS |
| 227 | `Are overdue bills concentrated within a specific customer group?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 228 | `Which ageing bucket has the highest outstanding amount, and what does it indicate?` | `GET_AGEING` | **95%** | Intent classified cleanly as GET_AGEING; Complex min/max sort requirement |
| 229 | `Is my net outstanding position improving month over month?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 230 | `Which ledgers have high outstanding but low recent collections?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 231 | `Which creditor and debtor have pending, overdue receivables?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 232 | `How many products belong to the category A` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 233 | `What is the total value of stock in category A and B?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 234 | `How has the stock quantity for each category changed over the period?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 235 | `How has the stock value for each category changed over the period?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 236 | `What is the total movement (inward and outward) for each category?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 237 | `Which categories have the highest stock movement?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 238 | `Which stock item in the above category has the highest stock movement?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 239 | `Which stock item in the above category has the lowest stock movement?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 240 | `Which categories have the lowest stock movement?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 241 | `Which stock item in the above category has the highest stock movement?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 242 | `Which stock item in the above category has the lowest stock movement?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 243 | `What valuation method is used for each stock category (FIFO, LIFO, Average Cost, etc.)?` | `UNKNOWN` | 55% | Intent classified as UNKNOWN (educational/non-executable query); Contains average calculation parameter (handled via Python stream aggregator) |
| 244 | `What is the average cost per unit for each category?` | `UNKNOWN` | 55% | Intent classified as UNKNOWN (educational/non-executable query); Contains average calculation parameter (handled via Python stream aggregator) |
| 245 | `How do stock values compare to historical data for each category?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 246 | `How much stock is nearing expiry within each category?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 247 | `What is the utilization rate of stock within each category?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 248 | `Are there any underutilized stock categories?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 249 | `How can stock utilization be optimized within each category?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 250 | `Are there any stock items below reorder levels within each category?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 251 | `What are the quantities and values of stock categories at different locations or warehouses?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 252 | `What are the available quantities and values of each batch for stock category A` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 253 | `Which categories have the lowest stock levels?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 254 | `Which categories have the highest stock levels?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 255 | `What is the total value of stock in each category?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 256 | `How do sales trends impact stock levels within each category?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 257 | `How many units were received in each batch during the period for each category?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 258 | `How many units were issued from each batch during the period for each category?` | `GET_RECENT_VOUCHERS` | **100%** | Intent classified cleanly as GET_RECENT_VOUCHERS |
| 259 | `What are the details of returns from customers for each category?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 260 | `What are the details of returns to suppliers for each category?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 261 | `Are there any stock items with high sales but low stock levels within each category?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 262 | `Are there any stock items with low sales but high stock levels within each category?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 263 | `What are the key insights from the stock category summary report?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 264 | `What trends can be identified from the stock category summary report?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 265 | `Give me closing balance as on today as per FIFO valuation method for each category( base costing method is average cost)` | `GET_TRIAL_BALANCE` | **90%** | Intent classified cleanly as GET_TRIAL_BALANCE; Contains average calculation parameter (handled via Python stream aggregator) |
| 266 | `Give me closing stock for today for Category A as per FIFO method` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 267 | `What is the impact of stock valuation methods on financial statements?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 268 | `What is the closing stock as on today as per LIFO Annual stock valuation method?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 269 | `What is the closing stock as on today as per FIFO Perpetual stock valuation method?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 270 | `What is the closing stock as on today as per LIFO Perpetual stock valuation method?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 271 | `What is the closing stock as on today as per Avg Cost valuation method?` | `UNKNOWN` | 55% | Intent classified as UNKNOWN (educational/non-executable query); Contains average calculation parameter (handled via Python stream aggregator) |
| 272 | `What is the closing stock as on today as per Avg Price valuation method?` | `GET_STOCK_SUMMARY` | **90%** | Intent classified cleanly as GET_STOCK_SUMMARY; Contains average calculation parameter (handled via Python stream aggregator) |
| 273 | `What is the closing stock as on today as per Last Purchase Cost valuation method?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 274 | `What is the closing stock as on today as per Last Sale price valuation method?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 275 | `What is the closing stock as on today as per Monthly Avg Cost valuation method?` | `UNKNOWN` | 55% | Intent classified as UNKNOWN (educational/non-executable query); Contains average calculation parameter (handled via Python stream aggregator) |
| 276 | `What is the closing stock as on today as per Standard Cost valuation method?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 277 | `What is the closing stock as on today as per Standard Price valuation method?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 278 | `Show Outstanding Sales Bills` | `AMBIGUOUS_OUTSTANDINGS` | **100%** | Intent classified cleanly as AMBIGUOUS_OUTSTANDINGS |
| 279 | `Show Cleared Sales Bills` | `GET_RECENT_VOUCHERS` | **100%** | Intent classified cleanly as GET_RECENT_VOUCHERS |
| 280 | `Show Bills made but Goods not delivered` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 281 | `Show Outstanding Purchase Bills` | `AMBIGUOUS_OUTSTANDINGS` | **100%** | Intent classified cleanly as AMBIGUOUS_OUTSTANDINGS |
| 282 | `Show Cleared Purchase Bills` | `GET_RECENT_VOUCHERS` | **100%** | Intent classified cleanly as GET_RECENT_VOUCHERS |
| 283 | `Show Bills received but Goods not received` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 284 | `Show Outstanding Bills for Job Work Materials` | `AMBIGUOUS_OUTSTANDINGS` | **100%** | Intent classified cleanly as AMBIGUOUS_OUTSTANDINGS |
| 285 | `Show Cleared Bills for Job Work Materials` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 286 | `Show Actual and Billed Quantities` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 287 | `Show Alternate units` | `AMBIGUOUS_OUTSTANDINGS` | **100%** | Intent classified cleanly as AMBIGUOUS_OUTSTANDINGS |
| 288 | `Show tail unit of Compound Unit` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 289 | `Show Location details` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 290 | `Show Batch details` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 291 | `Format of Report` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 292 | `Display name for Ledgers` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 293 | `Display name for Stock Items` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 294 | `Sorting Method` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 295 | `Enable Stripe View` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 296 | `Is the payment done for the party Asian Paints Limited for the bill number TN1701286266` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 297 | `List the payment transactions which are not reconciled` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 298 | `Why was the payment made to the party Marini rani.` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 299 | `How to generate the Payment Advice` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 300 | `What is the total number of payments made to the party Banu, and what is the aggregate value of those payments?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 301 | `Is the payment made against the bill 2554 of Banu party  and what is the value paid` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 302 | `Classify the payment records based on the mode of payment with the count and the amount` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 303 | `Name the bills which were cleared when the payment was made to AVPC  dated 2nd dec -17` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 304 | `List the payments made via Same bank transfer` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 305 | `Is the payment advice issued to Warnar Ltd for the latest payment ?` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 306 | `Display monthly payment trend bank wise` | `GET_RECENT_VOUCHERS` | **100%** | Intent classified cleanly as GET_RECENT_VOUCHERS |
| 307 | `When was the last payment made to M& M Marbels and what was the mode of the payment` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 308 | `Give me the count of only  cheque payment for the past 6 months and including value` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 309 | `Give me the count of reconciled and unreconciled payment records` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 310 | `Can you provide information about the payment made with reference number UIKIK009988777, including the recipient's account details?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 311 | `Display the list of the payment advice which are pending to email to the suppliers` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 312 | `Remind me to make the payment for Asain paints tomorrow` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 313 | `Share the payment Advice via whatsapp or email for the payments made today` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 314 | `List the reconciled payment records for the current month` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 315 | `Display the payment transactions of only forex transactions` | `GET_RECENT_VOUCHERS` | **100%** | Intent classified cleanly as GET_RECENT_VOUCHERS |
| 316 | `List only printed and e-mail payment advice for the month of april` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 317 | `Display the payment entry records of Tax payments` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 318 | `How to update the email ID before emailing the payment advice ?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 319 | `Find the payment record with the narration 'Payment made against the bank charges …..'` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 320 | `Display the payment records in which favourning name is different from the ledger name` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 321 | `Can I mail the payment advice to all the suppliers together.` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 322 | `Display the sample format of the Payment advice to send the deails` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 323 | `Can I change the title of the payment advice report` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 324 | `Is it possible to change the payment advice Date while printing the payment advice` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 325 | `I need to print the payment advice with the contact details, how can I do it` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 326 | `How to print the payment advice with the bill wise details ? Including due on date` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 327 | `How to issue the payment advice with the beneficiary account details /` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 328 | `Print the payment advice which is recorded for the party 'Warnar Ltd' with billwise details and transfer details` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 329 | `How to print each payment advice in the new page` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 330 | `How to change the template of the payment advice and customize accordingly` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 331 | `List the payment transactions which are recorded with the On account reference` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 332 | `What is the total value of all negative stocks as of today?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 333 | `List all the stock items that have negative opening balance for today?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES; Opening balance TDL collection supported |
| 334 | `List all the stock items that have negative closing balance for today?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 335 | `Which godown has the highest negative stock?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 336 | `Which godown has the lowest negative stock?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 337 | `Which item has the highest negative stock quantity?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 338 | `Which item has the lowest negative stock quantity?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 339 | `Which items have the highest negative stock values?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 340 | `Which items have the Lowest negative stock values?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 341 | `List all the negative stock items in Descending order in quantity` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 342 | `How much kgs of item A is in negative?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 343 | `What is the total number of items that are in negative?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 344 | `List all the stock groups that have negative quantity?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 345 | `What is the total negative quantity of each group?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 346 | `What is the total value of all the negative stock items in each group` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 347 | `Which stock group has the most negative quantity and what is the value?` | `GET_STOCK_SUMMARY` | **95%** | Intent classified cleanly as GET_STOCK_SUMMARY; Complex min/max sort requirement |
| 348 | `What is value of the highest negative quantity stock item?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 349 | `What is the quantity required for item A to convert the negative stock?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 350 | `Are there any items with negative closing balance still with profit?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 351 | `Which month has the highest negative quantity and value in closing balance for Item a?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 352 | `List the sales transactions made for item A before the purchase transactions.` | `GET_RECENT_VOUCHERS` | **100%** | Intent classified cleanly as GET_RECENT_VOUCHERS |
| 353 | `Give me closing negative stock as on today as per FIFO valuation method ( base costing method is average cost)` | `GET_STOCK_SUMMARY` | **90%** | Intent classified cleanly as GET_STOCK_SUMMARY; Contains average calculation parameter (handled via Python stream aggregator) |
| 354 | `What is the value of negative stock received from third party ?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 355 | `What is the value of Negative stock with third party ?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 356 | `What is the value of our and third party negative stock with us?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 357 | `What is the value of our negative stock with us?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 358 | `What is the value of our Negative stockwith us and third party?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 359 | `Give me closing negative stockfor today for Item P as per FIFO method` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 360 | `What is the closing negative stockas on today as per LIFO Annual negative stockvaluation method?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 361 | `What is the closing negative stockas on today as per FIFO Perpetual negative stockvaluation method?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 362 | `What is the closing negative stockas on today as per LIFO Perpetual negative stockvaluation method?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 363 | `What is the closing negative stockas on today as per Avg Cost valuation method?` | `UNKNOWN` | 55% | Intent classified as UNKNOWN (educational/non-executable query); Contains average calculation parameter (handled via Python stream aggregator) |
| 364 | `What is the closing negative stock as on today as per Avg Price valuation method?` | `UNKNOWN` | 55% | Intent classified as UNKNOWN (educational/non-executable query); Contains average calculation parameter (handled via Python stream aggregator) |
| 365 | `What is the closing negative stock as on today as per Last Purchase Cost valuation method?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 366 | `What is the closing negative stock as on today as per Last Sale price valuation method?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 367 | `What is the closing negative stock as on today as per Monthly Avg Cost valuation method?` | `UNKNOWN` | 55% | Intent classified as UNKNOWN (educational/non-executable query); Contains average calculation parameter (handled via Python stream aggregator) |
| 368 | `What is the closing negative stock as on today as per Standard Cost valuation method?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 369 | `What is the closing negative stock as on today as per Standard Price valuation method?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 370 | `What is the total value of all negative batches as of today?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 371 | `List all the batches that have negative opening balance for today?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES; Opening balance TDL collection supported |
| 372 | `List all the batches that have negative closing balance for today?` | `GET_TRIAL_BALANCE` | **100%** | Intent classified cleanly as GET_TRIAL_BALANCE |
| 373 | `List all the batches that have negative total inwards Quantity` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 374 | `List all the batches that have negative total outwards Quantity` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 375 | `Which godown has the highest negative stock for batch A` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 376 | `Which godown has the lowest negative stock for Batch A?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 377 | `Which batch has the highest negative stock quantity?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 378 | `Which batch has the lowest negative stock quantity?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 379 | `Which batch have the highest negative stock values?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 380 | `Which batch have the Lowest negative stock values?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 381 | `List all the negative batches in Descending order in quantity for closing balance` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 382 | `List all the negative batches with values in increasing order for outwards` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 383 | `List all the negative batches with quantity in decreasing order for opening balance` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES; Opening balance TDL collection supported |
| 384 | `How much kgs of item A is in negative for batch A?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 385 | `What is the total number of batches that are in negative for stock item A?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 386 | `List all the batches that have negative quantity?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 387 | `Which batch has the most negative quantity and what is the value for item A?` | `UNKNOWN` | 60% | Intent classified as UNKNOWN (educational/non-executable query); Complex min/max sort requirement |
| 388 | `What is value of the highest negative quantity batch ?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 389 | `What is the quantity required for batch 1 of item A to convert the negative stock?` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 390 | `Which month has the highest negative quantity and value in closing balance for Batch 1?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 391 | `List the sales transactions made for batch A before the purchase transactions.` | `GET_RECENT_VOUCHERS` | **100%** | Intent classified cleanly as GET_RECENT_VOUCHERS |
| 392 | `How many days are there till expiry for batch that have higher negative quantity?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 393 | `what is the quantity required to be purchased for each batch for item A to convert the negative quantity?` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 394 | `List the batches with negative quantity that have the expiry date 2 days from today?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 395 | `Show Quantity` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 396 | `Show Tail unit of Compound Unit` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 397 | `Show Basic Rate & Effective Rate` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 398 | `Show Value` | `GET_STOCK_SUMMARY` | **100%** | Intent classified cleanly as GET_STOCK_SUMMARY |
| 399 | `Show Suppliers` | `GET_TOP_CREDITORS` | **100%** | Intent classified cleanly as GET_TOP_CREDITORS |
| 400 | `Show Transfers Inward (Production)` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 401 | `Show Job Work Transfer Inward` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 402 | `Show Buyers` | `AMBIGUOUS_OUTSTANDINGS` | **100%** | Intent classified cleanly as AMBIGUOUS_OUTSTANDINGS |
| 403 | `Show Transfers Outward (Consumption)` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 404 | `Show Job Work Transfer Outward` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 405 | `What is the pending amount of  the party "PISHA SERVICES INDIA PVT LTD.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 406 | `Which is the recent pending bill for the party "PISHA SERVICES INDIA PVT LTD.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 407 | `What is the pending amount for bill reference ' JAN/980/23-24' for the party 'PISHA SERVICES INDIA PVT LTD` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 408 | `Which is the olders bills which is pending for the  party 'PISHA SERVICES INDIA PVT LTD` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 409 | `For the party' PISHA SERVICES INDIA PVT LTD , list all the advance bill references` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 410 | `For the party' PISHA SERVICES INDIA PVT LTD , list the on account bill references` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 411 | `Display the bills which are raised in the previous year but are pending in the current year for the debtors '  PISHA SERVICES INDIA PVT LTD` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 412 | `What is the due date of the bill number MAY/237/24-25 for the party PISHA SERVICES INDIA PVT LTD` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 413 | `Display the bills which are overdue by 90 days for the party PISHA SERVICES INDIA PVT LTD` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 414 | `What is the due date of the bill reference MAY/238/24-25  for the party PISHA SERVICES INDIA PVT LTD` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 415 | `What is the opening amount for the bill no 470 for the party 'Pisha services india pvt ltd'` | `GET_LEDGER_BALANCE` | **100%** | Intent classified cleanly as GET_LEDGER_BALANCE; Opening balance TDL collection supported |
| 416 | `From how many days the bill no 477 is pending for the customer Pisha services India pvt ltd'` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 417 | `For the Party Pisha services India pvt ltd, exclude the on account bill reference and display the pending amounts` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 418 | `For the Party Pisha services India pvt ltd, exclude the advance bill reference and display the pending amounts` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 419 | `For the party rajendra enterprise , how many bils are pending and what is the total outstanding amount` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 420 | `For Rajendra Enterprises , what is the total outstanding pending amount till the end of the April - 24.` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 421 | `Till the month of April- 24, for the party Rajendra enterprise, how many bills are overdue by 90 days.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 422 | `What is the pending amount for the reference number ST-7950 and does this reference belongs to Rajendra enterprises or Pisha service India pvt ltd` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 423 | `Does the reference number 8920 & 8922  belongs to the Rajendra enterprise ?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 424 | `What is the invoice value for the reference number ST-26604.` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 425 | `For Rajendra enterprise, display the Bill with the highest pending amount with the due date.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 426 | `For Rajendra enterprises, display the Bill with the lowest pending amount with the due date.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 427 | `Show the details of the invoice, inventory details of the bill reference ST-26604.` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 428 | `What is the pending amount for the party Pine Labs private limited` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 429 | `Which inventory items were purchased against the bill reference number MAY/238/24-25 for the customer Pisha?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 430 | `Show me the order number and the date of the bill  reference MAY/236/24-25 for the same party` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 431 | `Display the 3 months graph trend of the pending bills for the party Pisha?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 432 | `What is the ageing of the outstanding amount  based on the bill date for the 6 months for the ledger Pisha.` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 433 | `Display the above data using the graph for the pending amount and the age wise` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 434 | `How many bills are due below 90 days and how many bills are due above 90 days for the party Rajendra enterprises, with the total pending value` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 435 | `Which is the outstanding bill will the longest delay for rajendra party.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 436 | `For the rajendra party, how many overdue bills are available till date and what is the total value of it` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 437 | `Print the overdue bills for the Rajendra party ?` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 438 | `Print the reminder letter for the party Pisha services India ltd?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 439 | `Email the reminder letter for the party pisha service India ltd` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 440 | `Export the reminder letter in the excel format for the same party ?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 441 | `Print only  overdue bills for the Rajendra party ?` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 442 | `Whats app the ledger outstanding of the party phoenix ?` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 443 | `Settle all the bill reference of the party Sree venkatestwara and co from the ledger outstanding report` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 444 | `Display the address of the below parties` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 445 | `1. Sree venkatesthwara and co` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 446 | `2. Solai Agency` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 447 | `With the pending amount and the contact details such as address, number and total value` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 448 | `Display the complete details  of the bill reference number 2425056 i.e. vouchers included and the inventory details for supreme Agro products` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 449 | `What is the total outstanding of the vendor 'Sri Devi Transport ' pending for the financial period 23-24.` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 450 | `Continuation of the above questions` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 451 | `For the total pending amount vendor 'Sri Devi Transport, exclude the advance references and then display the Pending value.` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 452 | `What is the pending amount for the 'Control Print Ltd' party excluding the 'On Account References' bills` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 453 | `Settle the bill references of 3252014438EX of the party Control print Ltd, from axis bank OD account for the full amount` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 454 | `Show me the overdue invoices of the party 'CONVAY WATER PURIFIER PVT LTD',` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 455 | `How can I view the overdue invoices of the ledger ' Wheels India Private Limited` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 456 | `What is the Ageing analyis for the party Wheels India Private Limited (Based on the due dates) and present it graphically` | `GET_LEDGER_360` | 80% | Intent 'GET_LEDGER_360' requires custom handler |
| 457 | `How many invoices are pending for payment for the party 'Wheels India Limited".` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 458 | `Break up the outstanding amount by less than and more than 180 days by due date for the ledger 'Wheels India Limited".` | `GET_AGEING` | **100%** | Intent classified cleanly as GET_AGEING |
| 459 | `Display the narration provided for the bill reference no JUN/229/24-25 for the above party` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 460 | `Which are the stocks purchased for the reference number JUN/259/24-25- Ref1  for the same party.` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 461 | `Display those with the bill details.` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 462 | `Display party wise pending invoice count with their total value for all the parties` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 463 | `For the party KLM ltd >> invoice number  HO/21/2024, what is the ITC at risk and the balance pending amount considering different in tax ?` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS |
| 464 | `Display status wise pending bills for the Party KLM Ltd with the consolidated pending amount, Difference in Tax, Balance amount diff in Tax` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 465 | `How much is the total amount of difference in tax for Laxmi Traders` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 466 | `For the OM Stell Traders display the GST Information for the reference number KM/21/24-25.` | `GET_BILL_DETAILS` | **100%** | Intent classified cleanly as GET_BILL_DETAILS; GST / Tax attribute filter present |
| 467 | `What is the Balance after 'Difference in Tax ' for the party OM Stell Tranders.` | `UNKNOWN` | 65% | Intent classified as UNKNOWN (educational/non-executable query) |
| 468 | `Is there any difference in amount in books vs amount on portal for SLM Private Ltd.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 469 | `List the transactions available only in the books for all the Party with the respective  bill reference numbers?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 470 | `List the transactions available only in the Portal for all the Party with their respective  reference numbers and date ?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 471 | `List party name with their GST Numbers and pending amount and difference in the tax amount for all the party` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES; GST / Tax attribute filter present |
| 472 | `List the bills with Mismatched status for the party Om Stell Traders` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 473 | `List the bills with Reconciled status for the party Om Stell Traders` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 474 | `List the bills with Excluded status for the party Om Stell Traders` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 475 | `List the bills with Uncertain status for the party OM Stell Traders` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 476 | `What is the outstanding of Laxmi Traders and compare it with the company of 'Raj Company Pvt Ltd' .` | `GET_COMPARATIVE_SUMMARY` | 80% | Intent 'GET_COMPARATIVE_SUMMARY' requires custom handler |
| 477 | `List  only the bills pending in the next week for the party Lakshmi Traders` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 478 | `List all the advance receipts agains which the invoice is made, but the bills are yet pending ?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 479 | `When should we settle  Young India Stell corporation bill.` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |
| 480 | `Analyze the payment behaviour of Sona Steel enterprises.` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 481 | `Identify the parties who is  a buyer and a seller and what is the net value either payable or receivable.` | `GET_PAYABLES` | **100%** | Intent classified cleanly as GET_PAYABLES |
| 482 | `Show me the bills of Mr Nirman Timbers  and for how long the bill are pending and what are the items which are sold to them?` | `GET_RECEIVABLES` | **100%** | Intent classified cleanly as GET_RECEIVABLES |