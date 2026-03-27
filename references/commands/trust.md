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

## Output Schema

If the trust boundary is still ambiguous, return exactly:

```markdown
[one best next trust question]
```

Once there is enough clarity, return exactly:

```markdown
## Automation Map
- Safe for autonomy:
- Requires review:
- Human-only:

## Failure Taxonomy
- Wrong answer:
- Missing context:
- Hallucinated action:
- Bad retrieval:
- Compliance miss:
- Silent degradation:

## Operating Recommendation
- Copilot / review queue / constrained agent / full automation:
- Why:

## Minimum Trust Artifacts
- Audit log:
- Confidence scoring:
- Approval queue:
- Fallback behavior:
- Eval set:

## Evidence Classification
- Observed facts:
- Founder assertions:
- Model inferences:

## Diagnosis
- Primary bottleneck:
- Confidence:
- Evidence:
- If I'm wrong:

## Recommendation
- ...

## Next Move
- ...

**Recommended next**: `[command]` - ...
```

## State Updates

- Update `state.md` first.
- Refresh `Current Thesis`, `Open Questions`, `Evidence Collected`, and `Next Move`.
- Add or update `Trust Boundary` only if expanded mode is active or newly warranted.
- Update `Trust Architecture` only when `Company Assessments` is in use.
- Update `Current Diagnosis` only if that section exists or is newly warranted.
