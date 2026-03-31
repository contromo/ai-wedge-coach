# wedge

`wedge` pressure-tests the current workflow wedge.

If a single missing fact blocks useful assessment, ask the single best next wedge question and wait before assessing.

Stay in `wedge` mode until there is enough clarity to assess the wedge honestly.

## First Step

If the founder is vague, force wedge compression before assessing:

1. Broad version
2. Narrower version
3. Brutally narrow version

Use this sentence frame:

`We help [specific user] handle [specific recurring workflow] when [trigger] so they can [measurable outcome].`

Do not assess a broad category statement like "AI operations agent for SMBs" without compressing it first.
If the current coaching posture is `contradiction`, surface the strongest wedge inconsistency before deciding whether to keep, narrow, kill, or split.

## Assessment

Use the 7-axis wedge rubric in [../rubrics.md](../rubrics.md):

- Specificity
- Pain
- Recurrence
- Buyer Alignment
- Trust Fit
- Value Realization
- Deployment Fit

Then run the non-rubric `Why AI?` check.

Before assessing, separate observed facts from founder assertions and model inferences.
If a wedge assessment depends mostly on assertions or inference, keep it at `untested` or `weak evidence` and say so.
If any wedge axis lacks direct observed support, mark that axis `untested` instead of forcing a stronger label.

## Recurrence Rule

Always surface `Recurrence` as a first-class line item in both the assessment and diagnosis. Do not bury it.

## Recommendation Options

- `keep`
- `narrow`
- `kill`
- `split`

## Kill Path

If the result is `kill`:

- Append a `wedge_graveyard.md` entry.
- If `cohort_memory/wedge_failures.md` exists, append a normalized failed-wedge entry using [../cohort-memory.md](../cohort-memory.md).
- Preserve surviving assets, evidence, and next-wedge constraints.
- Clear the active wedge fields in `state.md` that are no longer true.
- Update `Current Diagnosis` to reflect that the wedge is dead and the company needs a reseed.
- Route to `kickoff` in reseed-after-kill mode.

If the result is `split`:

- Keep the active branch in `state.md`.
- Append the deprioritized branch to `wedge_graveyard.md` as `split-deprioritized`.
- If `cohort_memory/wedge_failures.md` exists, append the deprioritized branch as a normalized failed-wedge pattern using [../cohort-memory.md](../cohort-memory.md).

## Output Schema

If the wedge is still too fuzzy to assess, return exactly:

```markdown
Phase: [Workflow / User / Trigger / Desired outcome / Current workaround / Recurrence / Buyer clarification]
What we know: [running readback]
Why this next question matters: [what part of the wedge assessment or recommendation is still blocked]

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

## Wedge Assessment
- Specificity: [untested / weak evidence / validated / strong] | Evidence: ...
- Pain: [untested / weak evidence / validated / strong] | Evidence: ...
- Recurrence: [untested / weak evidence / validated / strong] | Evidence: ...
- Buyer Alignment: [untested / weak evidence / validated / strong] | Evidence: ...
- Trust Fit: [untested / weak evidence / validated / strong] | Evidence: ...
- Value Realization: [untested / weak evidence / validated / strong] | Evidence: ...
- Deployment Fit: [untested / weak evidence / validated / strong] | Evidence: ...

## Why AI?
- Step-change:
- If AI disappeared:

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
- keep / narrow / kill / split:
- Why:

## Next Move
- One 7-day test:

**Recommended next**: `[command]` - ...
```

## State Updates

- Update `state.md` first.
- Refresh `Current Thesis`, `Open Questions`, `Evidence Collected`, and `Next Move`.
- If expanded mode is active or newly warranted, update any detailed wedge, assessment, or diagnosis sections that are in use.
- Append an `Assessment History` row only when that section exists or expanded mode is newly warranted.
