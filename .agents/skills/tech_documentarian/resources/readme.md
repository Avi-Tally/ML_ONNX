# README Template

**When to use this template**: the entry-point doc for a repo or package — what it is, how to install it, and how to make the first call succeed. Not the place to duplicate the full API surface (`api-reference.md`) or internal structure (`architecture.md`) — link to those instead. Typical triggers: "write a README," "document this repo for new contributors."

Follow the parent skill's rules: pull the install command and usage example from something that actually works, not from memory (§1); pair any behavior claim with real code (§4); keep the top of the file tight — the first screen is the part actually read (§7, concrete over vague).

---

## Template

# [Project/Package Name]

One sentence: what this does and who it's for.

## Installation
```bash
pip install package-name
```

## Usage
The minimal example that gets a new user to a working first call — pulled from a real test or actual call site, not invented:

```python
from package import thing
thing.do_x()
```

## Configuration
| Key | Default | Required | Description |
|---|---|---|---|
| `API_KEY` | — | yes | ... |
| `TIMEOUT_MS` | `5000` | no | ... |

## API Reference
See [`api-reference.md`](./api-reference.md) for the full public surface. Don't restate it here — link to it.

## Architecture
One or two sentences on how this is organized internally, with a link to [`architecture.md`](./architecture.md) if the project has enough internal structure to warrant a separate doc. Omit this section entirely for a single-file package.

## Edge Cases & Gotchas
Anything a new user would hit and not expect: version constraints, platform-specific behavior, common misconfigurations.

## Contributing / Development
```bash
git clone ...
pip install -e ".[dev]"
pytest
```
Only include this section if other engineers will actually contribute to this repo — omit for a pure consumer-facing package.

## License
[License name] — see `LICENSE`.

---

## Notes for filling this in

- **Keep the top tight.** Name, one-liner, install, minimal usage — in that order, before anything else. That's the part almost everyone actually reads; everything below it is reference material for the smaller group that needs more.
- **Don't duplicate `api-reference.md` or `architecture.md`.** If both exist, the README's job is to get someone to a working example fast and then hand off — link out rather than inlining the full parameter tables or file layout here. If either doc doesn't exist yet, it's fine to inline a short version, but flag it as something worth splitting out once the project grows.
- **The Usage example must actually run.** An example that doesn't work is the single most damaging thing a README can contain, since it's usually the very first thing a new user tries.
- **Omit sections that don't apply** rather than leaving them as empty headers — an empty "Contributing" section on a closed package is worse than no section at all.
