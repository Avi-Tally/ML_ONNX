# Architecture Decision Record (ADR) Template

**When to use this template**: recording *why* a significant technical decision was made — not what the system does now (`architecture.md`) or how to call it (`api-reference.md`). Typical triggers: "write up why we chose X," "document this decision," a linked design doc or discussion thread that ended in a concrete choice.

Follow the parent skill's rules: ground Context and Consequences in what was actually discussed/tested, not a retrofitted justification (§1); keep language concrete rather than vague (§7 — "reduces p99 latency from 400ms to 80ms" beats "improves performance"); this template does not use the skill's baseline skeleton from §3 — MADR format replaces it.

---

## Template

# ADR-[NNNN]: [Decision Title]

**Status**: Proposed | Accepted | Deprecated | Superseded by ADR-[NNNN]
**Date**: YYYY-MM-DD
**Deciders**: [names or team]

## Context
What problem forced this decision? What constraints — technical, organizational, timeline — were actually in play? State the facts as they stood at decision time, not the conclusion you're about to reach. A reader six months from now should be able to tell whether the constraints that drove this still apply.

## Decision
State the decision in one clear sentence, then the concrete details — the library, pattern, or config actually chosen:

```[language]
# representative snippet showing the decision in practice, if applicable
```

## Consequences

**Positive**
- What this makes easier, faster, safer, or simpler — concretely.

**Negative / Trade-offs**
- What this makes harder or gives up. Every real decision has at least one of these — an ADR with no trade-offs listed is usually incomplete.

**Neutral / Follow-ups**
- Anything that changes but isn't clearly good or bad, and any follow-up work this decision implies.

## Alternatives Considered

### [Alternative A]
Why it was rejected — a concrete reason ("adds a 200ms cold-start penalty," "requires a license we don't have"), not "wasn't as good."

### [Alternative B]
...

## See Also
Related ADRs, `architecture.md` for the resulting structure, and the PR/discussion thread that led here.

---

## Notes for filling this in

- **Status and Date are not optional.** A reader's first question is "is this still true?" — an ADR without a status is ambiguous by default.
- **Superseded ADRs get linked forward, not deleted.** History matters here — silently removing a stale ADR erases the record of why the old approach was tried in the first place.
- **Alternatives Considered is the section most often skipped and the most valuable one for future readers second-guessing the decision.** Keep at least one real alternative with a concrete reason it lost — "we didn't think of anything else" is itself useful information, but say that explicitly rather than leaving the section blank.
- **Don't retrofit the Context section.** If the real reasoning was messier than the eventual decision suggests (a deadline forced a call before all options were evaluated), say that — it's more useful to a future reader than a tidied-up narrative.
