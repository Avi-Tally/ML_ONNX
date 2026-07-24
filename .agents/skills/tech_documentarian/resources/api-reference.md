# API Reference Template

**When to use this template**: documenting the *public* surface of a module, class, or function — signatures, parameters, return values, exceptions. Distinct from `architecture.md` (internal structure/how the pieces fit together) and `readme.md` (how to install and get started). Typical triggers: "explain this function," "document this class," "add docs for this module's public API."

Follow the parent skill's rules: pull every signature, type, and default verbatim from source (§1) — never paraphrase a type; pair every entry with its actual code (§4); use tables for parameters (§5); skip diagrams entirely unless there's a genuine multi-call sequence worth showing (§6); keep descriptions concrete (§7 — state the actual exception and condition, not "handles errors gracefully").

---

## Template

# [Module/Class Name] — API Reference

## Overview
One paragraph: what this exposes and when a caller should reach for it.

## `function_name(param1, param2=default) -> ReturnType`

```python
def function_name(param1: str, param2: int = 10) -> bool:
    ...
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `param1` | `str` | — | required, what it represents |
| `param2` | `int` | `10` | what changing it does |

**Returns**: `bool` — what `True`/`False` (or the value) means concretely.

**Raises**

| Exception | Condition |
|---|---|
| `ValueError` | pulled from an actual `raise` statement, not assumed |

**Example**
```python
result = function_name("x", param2=5)
```

**Edge Cases**
- Behavior on empty/`None` input — verified against tests, not assumed.
- Thread-safety, idempotency, or ordering notes, if relevant.

---
*(repeat one block per public function, method, or class)*

## See Also
Link to `architecture.md` for how this fits together internally, and `adr.md` for why it's shaped this way, if either exists.

---

## Notes for filling this in

- **One entry per public symbol.** Private/internal helpers belong in `architecture.md`'s "Key Types & Interfaces" section, not here — mixing them makes it harder to tell what's actually safe to depend on.
- **Exceptions must come from real `raise` statements or tests**, not "this probably throws on bad input." If you can't find where an error condition is actually enforced, say so in the doc rather than inventing the exception type.
- **Skip the diagram entirely** unless there's a genuine multi-call sequence worth showing (e.g. a method that triggers callbacks across files) — most API reference entries don't need one, and a diagram per function is noise per skill §6.
- **The Example must run.** Prefer pulling it from an existing test or real call site over writing one from scratch; an example that doesn't actually work is worse than no example.
