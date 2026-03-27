# wedge

`wedge` pressure-tests the current workflow wedge.

If a single missing fact blocks useful scoring, ask the single best next wedge question and wait before scoring.

Stay in `wedge` mode until there is enough clarity to score the wedge honestly.

## First Step

If the founder is vague, force wedge compression before scoring:

1. Broad version
2. Narrower version
3. Brutally narrow version

Use this sentence frame:

`We help [specific user] handle [specific recurring workflow] when [trigger] so they can [measurable outcome].`

Do not score a broad category statement like "AI operations agent for SMBs" without compressing it first.

## Scoring

Use the 7-axis wedge rubric in [../rubrics.md](../rubrics.md):

- Specificity
- Pain
- Recurrence
- Buyer Alignment
- Trust Fit
- Value Realization
- Deployment Fit

Then run the non-scored `Why AI?` check.

## Recurrence Rule

Always surface `Recurrence` as a first-class line item in both the scorecard and diagnosis. Do not bury it.

## Recommendation Options

- `keep`
- `narrow`
- `kill`
- `split`

## Kill Path

If the result is `kill`:

- Append a `wedge_graveyard.md` entry.
- Preserve surviving assets, evidence, and next-wedge constraints.
- Clear the active wedge fields in `founder_state.md` that are no longer true.
- Update `Current Diagnosis` to reflect that the wedge is dead and the company needs a reseed.
- Route to `kickoff` in reseed-after-kill mode.

If the result is `split`:

- Keep the active branch in `founder_state.md`.
- Append the deprioritized branch to `wedge_graveyard.md` as `split-deprioritized`.

## Output Schema

If the wedge is still too fuzzy to score, return exactly:

```markdown
[one best next wedge question]
```

Once there is enough clarity, return exactly:

```markdown
## Current Workflow
- Workflow:
- Primary user:
- Economic buyer:
- Trigger:
- Current workaround:
- Desired outcome:

## Wedge Compression
- Broad:
- Narrower:
- Brutally narrow:

## Scorecard
- Specificity:
- Pain:
- Recurrence:
- Buyer Alignment:
- Trust Fit:
- Value Realization:
- Deployment Fit:
- Total:
- Band:

## Why AI?
- Step-change:
- If AI disappeared:

## Diagnosis
- Primary bottleneck:
- Confidence:
- Evidence:
- If I'm wrong:

## Recommendation
- keep / narrow / kill / split:
- Why:

## Next Move
- One 7-day test:

**Recommended next**: `[command]` - ...
```

## State Updates

- Update the `Current Primary Wedge` section.
- Update `Wedge Sharpness`, `Value Recurrence`, and any other company-level scores materially affected.
- Append a `Score History` entry when scores change.
