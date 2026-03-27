# objections

`objections` is planned but not fully implemented in v1.

For now:

- Route to `trust` if the dominant objections are trust, compliance, auditability, or error tolerance.
- Otherwise route to `icp` to diagnose buyer, user, ROI, timing, or pricing objections.
- If new objections are shared during the redirect flow, append them to `objection_log.md` per [../state-system.md](../state-system.md).

Return a short redirect, not a fake full clustering analysis.
