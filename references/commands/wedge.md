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

## Founder-Facing Response

- If the wedge is still too fuzzy to assess honestly, ask one best next wedge question only.
- Once there is enough clarity, keep the visible response tight. Cover:
  - a concise wedge restatement or compression
  - an explicit recurrence read
  - the main bottleneck and why it matters
  - a `keep`, `narrow`, `kill`, or `split` verdict
  - one concrete next move and, when another command is clearly next, a consent-first handoff sentence such as `Next best move is trust. Want me to map that now?`
- The evidence-backed wedge assessment, `Why AI?` check, and evidence classification still matter, but they are internal by default. Surface only the score or evidence detail that materially explains the verdict.

## State Updates

- Update `state.md` first.
- Refresh `Current Thesis`, `Open Questions`, `Evidence Collected`, and `Next Move`.
- If expanded mode is active or newly warranted, update any detailed wedge, assessment, or diagnosis sections that are in use.
- Append an `Assessment History` row only when that section exists or expanded mode is newly warranted.
