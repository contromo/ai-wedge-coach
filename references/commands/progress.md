# progress

`progress` summarizes what has actually been learned across sessions.

If recent changes, evidence, or the current thesis are unclear, ask one clarifying question before producing the progress summary.

## Required Inputs

Read:

- `founder_state.md`
- `interview_log.md`
- `objection_log.md`
- `experiment_log.md`
- `market_research_log.md`
- `wedge_graveyard.md`

## Required Behavior

- Score only the six company-level dimensions in [../rubrics.md](../rubrics.md).
- Show deltas using `Score History`.
- Call out `Value Recurrence` explicitly every time.
- Identify at least one founder archetype when the evidence supports it.
- Name repeated pathologies without drifting into generic coaching.
- Include what external market research has confirmed or weakened.

## Output Schema

If progress cannot be summarized honestly yet, return exactly:

```markdown
[one best next progress question]
```

Once there is enough clarity, return exactly:

```markdown
## Current Scoreboard
- Wedge Sharpness:
- ICP Focus:
- Value Recurrence:
- Trust Architecture:
- Evidence Quality:
- Learning Velocity:

## Score Trend
- Biggest improvement:
- Biggest unresolved drag:
- Value recurrence read:

## Pattern Read
- Primary archetype:
- Repeated pathology:
- Current best thesis:

## Market Reality
- Strongest external confirmation:
- Biggest external contradiction:
- What still needs validation:

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

- Update `Company Scores`.
- Append a new `Score History` entry when scores changed since the last snapshot.
- Update `Current Diagnosis` and `Next 7 Days`.
