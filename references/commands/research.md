# research

`research` validates founder claims against external market evidence.

`market` is an alias.

Use this command when the founder has a plausible story but weak proof, or when you need to sanity-check wedge, buyer, urgency, substitutes, or trust assumptions before locking in a diagnosis.

If the claim under test is still fuzzy, ask one clarifying question before doing research.

Stay in `research` mode until the claim under test is precise enough to investigate.

Read [../market-research.md](../market-research.md) before running this command.

## Inputs

Use the current founder thesis and research these claims where possible:

- the workflow is real
- the workflow is recurring
- the pain is consequential
- the likely buyer exists
- substitutes and current workarounds are visible
- trust, compliance, or deployment constraints are plausible

## State And Logging

- Update `Evidence Log` in `founder_state.md`.
- Update `Current Diagnosis` only if the research materially changes the best current thesis.
- Append a summary entry to `market_research_log.md`.
- If research uncovers concrete objections, append them to `objection_log.md`.

## Output Schema

If the claim under test is still unclear, return exactly:

```markdown
[one best next research question]
```

Once there is enough clarity, return exactly:

```markdown
## Research Focus
- Workflow / claim under test:
- Why this matters:

## Claims To Validate
- Claim 1:
- Claim 2:
- Claim 3:

## Market Reality Check
- What supports the founder story:
- What weakens or contradicts it:
- Visible substitutes / competitors:
- Buyer and implementation clues:
- Trust / deployment concerns:

## What This Changes
- Stronger thesis:
- Weaker thesis:
- Still unknown:

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
