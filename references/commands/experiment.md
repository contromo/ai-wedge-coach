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

## Experiment Quality Gate

An experiment is not valid unless it has all of these:

- owner
- deadline
- falsifier
- signal threshold
- decision rule

If any of those fields are missing, do not draft a partial experiment and do not pretend it is ready to run.
Ask the single missing question that most directly completes the experiment.

## Result Update Mode

If the founder is reporting back on an existing experiment:

- interpret the result against the stated thresholds
- decide whether the result is `success`, `failure`, or `ambiguous`
- apply the linked decision rule
- feed that result back into founder state automatically

Do not leave an experiment result sitting in `experiment_log.md` without updating `state.md`.

If the current coaching posture is `proof`, use the experiment to convert the biggest assertion into an observed fact.
If the current coaching posture is `containment`, make the experiment define the threshold for changing direction.

## Rules

- One experiment only.
- The hypothesis must be falsifiable.
- The experiment must name one explicit owner.
- The experiment must have one deadline.
- The experiment must have one explicit falsifier.
- The experiment must have concrete success, failure, and ambiguous thresholds.
- The experiment must have a decision rule that changes what the team does next.
- The method must be concrete enough to run this week.
- Success and failure thresholds must imply a decision.
- If the hypothesis depends on unvalidated market assumptions, recommend `research` first or in parallel.
- If the experiment uses customer conversations, append those results to `interview_log.md`, creating the file if needed.
- If the experiment surfaces objections, append them to `objection_log.md`, creating the file if needed.
- If `cohort_memory/objection_patterns.md` exists and the experiment surfaces a concrete objection with direct evidence, append a normalized objection pattern entry using [../cohort-memory.md](../cohort-memory.md).
- Always append the experiment itself to `experiment_log.md`, creating the file if needed.
- Separate observed facts, founder assertions, and model inferences before choosing the experiment.

## Output Schema

If the experiment is not yet well-formed, return exactly:

```markdown
[one best next experiment question]
```

Once there is enough clarity, return exactly:

```markdown
## Experiment Brief
- Status: [planned / running / complete / killed]
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

- Update `state.md` first.
- Refresh `Current Thesis`, `Open Questions`, `Evidence Collected`, and `Next Move`.
- If `Active Experiments` exists or expanded mode is newly warranted, update it with the experiment's status, linked dimension, hypothesis, falsifier, owner, deadline, thresholds, and decision rule.
- When a result is reported, append the outcome to `experiment_log.md`, update `Evidence Collected`, update `Current Diagnosis` if that section exists, and append a `Decision Log` entry if that section exists and the decision rule fired.
- Update `Learning Velocity` and any linked company-level dimension only when `Company Assessments` is in use.
- Append an `Assessment History` row only when that section exists or expanded mode is newly warranted.
