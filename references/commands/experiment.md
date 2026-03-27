# experiment

`experiment` designs or updates one 7-day or 14-day experiment.

If the hypothesis, method, or decision threshold is still unclear, ask one clarifying question at a time before drafting the experiment.

## Modes

- `Auto-prioritized`: default. Select the top unresolved hypothesis from the current diagnosis.
- `User-specified`: if the founder explicitly names the hypothesis they want to test, use that instead.

In both modes, attach the experiment to one company-level dimension:

- Wedge Sharpness
- ICP Focus
- Value Recurrence
- Trust Architecture
- Evidence Quality
- Learning Velocity

## Rules

- One experiment only.
- The hypothesis must be falsifiable.
- The method must be concrete enough to run this week.
- Success and failure thresholds must imply a decision.
- If the hypothesis depends on unvalidated market assumptions, recommend `research` first or in parallel.
- If the experiment uses customer conversations, append those results to `interview_log.md`.
- If the experiment surfaces objections, append them to `objection_log.md`.
- If `cohort_memory/objection_patterns.md` exists and the experiment surfaces a concrete objection with direct evidence, append a normalized objection pattern entry using [../cohort-memory.md](../cohort-memory.md).
- Always append the experiment itself to `experiment_log.md`.
- Separate observed facts, founder assertions, and model inferences before choosing the experiment.

## Output Schema

If the experiment is not yet well-formed, return exactly:

```markdown
[one best next experiment question]
```

Once there is enough clarity, return exactly:

```markdown
## Experiment Brief
- Mode:
- Linked dimension:
- Hypothesis:
- Falsifier:
- Owner:
- Deadline:

## Method
- Steps:
- Required inputs:

## Signal Thresholds
- Success means:
- Failure means:
- Ambiguous result means:

## Decision Rule
- If success:
- If failure:
- If ambiguous:

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

- Update `Active Experiments`.
- Update `Evidence Log` if the hypothesis basis changed materially.
- Update `Learning Velocity` and any linked company-level dimension that materially changed only with cited observed evidence and a confidence label; otherwise keep the score suppressed.
- Append a `Score History` entry when scores change, including confidence, evidence, or suppression reason.
