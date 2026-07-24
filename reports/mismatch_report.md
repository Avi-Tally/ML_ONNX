# NLP Engine Mismatch Report

**Total Queries:** 855
**Passed:** 855
**Failed:** 0
**Total FAQ/Unknown:** 22
**Pass Rate:** 100.00%

## Mismatches

No mismatches found! 100% Pass Rate.
                  ┌─────────────────────────────────────────┐
                  │          User Query Enters              │
                  └────────────────────┬────────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │ TIER 1: Tally Alteration ID Change-     │
                  │ Check Header (Sub-millisecond Check)    │
                  └────────────────────┬────────────────────┘
                                       │
                    ┌──────────────────┴──────────────────┐
          (Alteration ID Changed)                 (No Edits)
                    │                                     │
                    ▼                                     ▼
┌───────────────────────────────────────┐ ┌───────────────────────────────┐
│ TIER 2: Incremental TDL Delta Sync    │ │ TIER 3: Serve from High-Speed │
│ (Updates ONLY modified Master Ledgers)│ │ Live In-Memory Cache          │
└───────────────────┬───────────────────┘ └───────────────┬───────────────┘
                    │                                     │
                    └──────────────────┬──────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │ TIER 4: Dynamic Direct Live TDL Query   │
                  │ (Zero-cache execution for core reports) │
                  └─────────────────────────────────────────┘

                  