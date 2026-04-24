# trust

`trust` is the canonical command name for AI trust architecture. `autonomy` is an alias.

Use this command to define what runs unattended, what needs review, and what must stay human-only.

If the workflow steps are still unclear, ask one clarifying question at a time before producing the automation map.

Stay in `trust` mode until the autonomy boundary is concrete enough to map.

## Questions To Resolve

- Which workflow steps are safe for autonomy?
- Which require human review?
- Which must stay human-only?
- Which actions are irreversible?
- Which failures are unacceptable?
- What audit or compliance constraints matter?
- Is partial automation already enough?

Use [../diagnosis-trees.md](../diagnosis-trees.md) for the trust-boundary tree.

## Log Writes

Append to `objection_log.md`, creating the file if needed, when trust, compliance, auditability, or error-tolerance objections surface.
Keep observed trust facts, founder assertions, and model inferences separate before recommending an operating mode.
If `cohort_memory/objection_patterns.md` exists and a concrete objection surfaced, append a normalized objection pattern entry.
If `cohort_memory/trust_patterns.md` exists and the trust boundary is concrete enough, append a normalized trust-pattern entry using [../cohort-memory.md](../cohort-memory.md).

## Founder-Facing Response

- If the trust boundary is still ambiguous, ask one best next trust question only.
- Once there is enough clarity, keep the visible response concise. Cover:
  - what is safe for autonomy
  - what requires review
  - what must stay human-only
  - the highest-risk failure or irreversible step
  - the recommended operating mode, the main trust blocker, one next move, and, when another command is clearly next, a consent-first handoff sentence
- Audit requirements, fallback behavior, confidence scoring, and evidence classification still matter, but surface them only when they materially support the recommendation.

## State Updates

- Update `state.md` first.
- Refresh `Current Thesis`, `Open Questions`, `Evidence Collected`, and `Next Move`.
- Add or update `Trust Boundary` only if expanded mode is active or newly warranted.
- Update `Trust Architecture` only when `Company Assessments` is in use.
- Update `Current Diagnosis` only if that section exists or is newly warranted.
