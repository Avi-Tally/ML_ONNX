# Daily Progress Report Template

**When to use this template**: generating an end-of-day (EOD) engineering summary of work completed during a work session or day. Typical triggers: "generate my daily report," "summarize today's progress," "create an EOD update for the team."

**Destination & Naming Convention**:
- **Directory**: Must always be saved to `reports/agenticreports/`
- **Filename**: `YYYY-MM-DD_HHMM_daily-report.md` (e.g., `reports/agenticreports/2026-07-24_1830_daily-report.md`)

Follow the parent skill's rules: ground all claims in actual git history (`git log`, `git status`, `git diff`) and modified files (§1); pair major accomplishments with verbatim code snippets (§4); include concrete test execution results (§7, verified facts over assumptions).

---

## Template

# Daily Progress Report — [YYYY-MM-DD HH:MM]

**Author / Contributor**: [Name or Agent]  
**Repository**: [Repo Name]  
**Branch**: `[branch-name]`  
**Session Focus**: [One-line summary of primary objective for the day]  
**Report File**: `reports/agenticreports/YYYY-MM-DD_HHMM_daily-report.md`

---

## Executive Summary
A concise paragraph (2–3 sentences) summarizing the main progress made today, key problems resolved, and overall state of the codebase following this session.

---

## Accomplishments & Features Built

### 1. [Feature / Component / Module Name]
- **Summary**: Detailed description of what was added or refactored.
- **Touched Files**: `path/to/file1.py`, `path/to/file2.py`
- **Key Implementation Snippet**:
  ```python
  # Verbatim snippet representing today's core logic change
  def new_feature_handler(arg: str) -> bool:
      ...
  ```
- **Rationale / Design Notes**: Why this specific implementation approach was chosen.

---

## Code Modifications Breakdown

| File Modified | Change Type | Scope / Purpose |
|---|---|---|
| `path/to/modified_file.py` | Added / Modified / Deleted | Added error handling for timeout conditions |
| `tests/test_modified_file.py` | Added | Added unit tests for edge case coverage |

---

## Technical Decisions & Trade-offs
- **[Decision 1]**: Brief explanation of architectural or technical choices made today.
- **Link to ADR**: [`ADR-0002`](./docs/adr/0002-cache-strategy.md) *(if applicable)*.

---

## Verification & Testing

### Automated Test Results
Commands executed to verify today's work:
```bash
pytest tests/test_modified_file.py
```
- **Status**: Passed (12 passed, 0 failed in 1.42s)
- **Coverage**: Verified core logic and failure recovery paths.

### Manual Verification
- Verified runtime behavior against target environment/endpoint.

---

## Blockers, Edge Cases & Open Issues
- **[Blocker / Issue 1]**: Description of any unresolved bug, external dependency delay, or technical debt encountered.
- **Action Needed**: `<!-- TODO: confirm expected behavior with team -->`

---

## Plan for Next Session
1. [ ] **[High Priority Task]**: Specific next step to build or refactor.
2. [ ] **[Secondary Task]**: Follow-up test writing or documentation update.

---

## Notes for filling this in

- **Mandatory Storage Path**: Always save output to `reports/agenticreports/` using the date-time prefix format `YYYY-MM-DD_HHMM_daily-report.md` (e.g. `reports/agenticreports/2026-07-24_1325_daily-report.md`). Create the directory if it does not exist.
- **Must be grounded in Git history.** Run `git log --since="24 hours ago"` or `git status` / `git diff` before writing this report. Never summarize work from memory when git history is available.
- **Always include verbatim code snippets.** Do not just state "updated the auth handler" — show the exact function or lines modified today (§4).
- **Test execution must be factual.** Include the exact test command and actual pass/fail numbers verified during the session.
- **Keep files and paths clickable.** Use relative Markdown links or precise backticked file paths (`path/to/file.py`) so the reader can jump directly to the code.
