# pivot

`pivot` is planned but not fully implemented in v1.

For now:

- If a wedge is still active, route to `wedge` for kill-path review.
- If the current wedge is already dead or deprioritized, route to `kickoff` in reseed-after-kill mode.
- Preserve the evidence, surviving assets, and next-wedge constraints from `wedge_graveyard.md`.

Return a short redirect, not a fake pivot memo.
