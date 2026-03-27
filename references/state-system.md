# State System

Runtime state lives in the founder's current working directory. Use append-only behavior for logs. Do not silently overwrite prior learning.

Do not commit runtime files as part of the skill package. They are founder-specific working state, not repo content.

## Evidence Classification Rule

All working commands must keep three evidence buckets separate in state and outputs:

- `Observed facts`
- `Founder assertions`
- `Model inferences`

Observed facts are things actually seen in interviews, usage, pilots, pricing conversations, objections, experiment results, or external artifacts.
Founder assertions are unverified founder claims.
Model inferences are coach interpretations built on top of the other two buckets.

Do not silently promote an assertion or an inference into a fact.

## Canonical File Set

- `founder_state.md`
- `interview_log.md`
- `objection_log.md`
- `experiment_log.md`
- `market_research_log.md`
- `wedge_graveyard.md`

## Optional Shared Cohort Memory

If `cohort_memory/` exists in the current working directory, treat it as shared accelerator memory.
For multi-company use, point each founder workspace at the same shared directory.

Shared cohort files:

- `cohort_memory/wedge_failures.md`
- `cohort_memory/objection_patterns.md`
- `cohort_memory/trust_patterns.md`
- `cohort_memory/segment_benchmarks.md`

## founder_state.md

`founder_state.md` is the canonical state file. All working commands update it.

Create it with this structure after kickoff intake is complete:

```markdown
# Founder State

## Company Snapshot
- Company:
- Stage:
- Team size:
- Category:
- Product one-liner:
- Funding context:
- Sales motion:
- Current revenue:
- Active pilots:
- Design partners:
- Main concern right now:

## Current Primary Wedge
- Workflow:
- Job to be done:
- Primary user:
- Economic buyer:
- Champion:
- Trigger moment:
- Current workaround:
- Why now:
- Time to value:
- Frequency:
- Consequence of failure:
- Must-have or nice-to-have:
- Why AI step-change:
- Recommendation status:
- Last wedge score: [numeric total or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...

## ICP Hypotheses
### Primary
- Persona:
- Company type:
- Team:
- Pain:
- Buyer:
- Champion:
- Budget owner:
- Urgency trigger:

### Secondary
- Persona:
- Company type:
- Why considered:

### Excluded
- ICPs we are explicitly not chasing:

## Trust Boundary
- Fully autonomous steps:
- Human review steps:
- Human-only steps:
- Irreversible actions:
- Compliance / audit constraints:
- Error tolerance:
- Main trust blocker:
- Recommended operating mode:

## Evidence Log
- Observed facts:
- Founder assertions:
- Model inferences:
- Interviews completed:
- Strongest observed signal:
- Weakest assertion:
- Biggest inference risk:
- Pricing evidence:
- Retention evidence:
- Top objections:

## Founder Handling
- Current archetype:
- Coaching posture: [compression / contradiction / proof / containment]
- Why this posture:
- Secondary blocking archetype:
- What the coach should do next:
- Last updated:

## Guided Discovery
- Current phase:
- What we know:
- What still needs validation:
- Planned market checks:
- Current plan of attack:

## Market Reality Check
- Claims tested:
- Strongest external validation:
- Biggest external contradiction:
- Visible substitutes:
- Buyer / procurement clues:
- Trust / deployment clues:
- Open research questions:

## Current Diagnosis
- Primary bottleneck:
- Confidence:
- Observed facts used:
- Founder assertions carrying load:
- Model inferences used:
- If we're wrong:
- Recommended next command:

## Accelerator Ops
- Partner briefing:
- Weekly company status delta:
- Red-flag memo:
- Needs human help now: [yes / no]
- Trigger(s):
- Suggested human owner:
- Suggested intervention:
- By when:
- Last ops update:

## Cohort Comparison
- Similar failed wedge patterns:
- Repeated objection patterns:
- Relevant trust-boundary patterns:
- Segment benchmark read:
- Where this company is above cohort:
- Where this company is below cohort:
- Cohort sample caveat:
- Last cohort update:

## Company Scores
- Wedge Sharpness: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- ICP Focus: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Value Recurrence: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Trust Architecture: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Evidence Quality: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Learning Velocity: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...

## Score History
- Date:
  - Reason for score change:
  - Wedge Sharpness: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
  - ICP Focus: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
  - Value Recurrence: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
  - Trust Architecture: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
  - Evidence Quality: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
  - Learning Velocity: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...

## Active Experiments
### Experiment 1
- Name:
- Status: [planned / running / complete / killed]
- Linked dimension:
- Hypothesis:
- Falsifier:
- Owner:
- Deadline:
- Success threshold:
- Failure threshold:
- Ambiguous threshold:
- Decision rule:
- Latest result:
- Next decision:

### Experiment 2
- Name:
- Status: [planned / running / complete / killed]
- Linked dimension:
- Hypothesis:
- Falsifier:
- Owner:
- Deadline:
- Success threshold:
- Failure threshold:
- Ambiguous threshold:
- Decision rule:
- Latest result:
- Next decision:

### Experiment 3
- Name:
- Status: [planned / running / complete / killed]
- Linked dimension:
- Hypothesis:
- Falsifier:
- Owner:
- Deadline:
- Success threshold:
- Failure threshold:
- Ambiguous threshold:
- Decision rule:
- Latest result:
- Next decision:

## Decision Log
- Older decisions summary:
- Date:
  - Source experiment:
  - Decision:
  - Why:
  - Evidence:
  - Revisit when:

## Next Wedge Constraints
- What must remain true in the next wedge:
- What we refuse to repeat:

## Next 7 Days
- 
- 
- 
```

## Write Contracts

Whenever a working command materially changes the thesis, update `Evidence Log` with the latest observed facts, founder assertions, and model inferences instead of blending them into one evidence summary.
`kickoff` and `progress` are the canonical commands for updating `Founder Handling`.
`progress` is the canonical command for updating `Accelerator Ops`.
`progress` is also the canonical command for updating `Cohort Comparison`.

## Experiment Feedback Loop

`experiment` is the canonical command for maintaining `Active Experiments`.

When an experiment is created or updated:

- write the structured experiment entry into `Active Experiments`
- ensure owner, deadline, falsifier, thresholds, and decision rule are all present
- append the experiment plan to `experiment_log.md`

When an experiment result is reported:

- append the outcome to `experiment_log.md`
- update the matching `Active Experiments` entry with `Latest result`, `Status`, and `Next decision`
- update `Evidence Log` with any new observed facts
- update `Current Diagnosis` if the result materially changes the best current thesis
- update `Next 7 Days`
- append a `Decision Log` entry if the result triggered a real decision
- update linked scores only with cited observed evidence and confidence, otherwise keep them suppressed

## Decision Log Archival Rule

When `Decision Log` exceeds `15` entries:

- compress older entries into `Older decisions summary`
- keep the most recent `10` full entries
- preserve the main narrative arc, major thesis changes, and still-open revisitation points
- do not drop unresolved decisions just to hit the limit

### interview_log.md

Purpose: append-only record of real customer conversations or direct user/buyer signal.

Append when:

- `kickoff` backfills prior interviews, discovery calls, design-partner conversations, or observational research.
- `icp` captures new user, buyer, or champion conversations.
- `experiment` records results from tests that include interview-style feedback.

Append format:

```markdown
# Interview Log

## YYYY-MM-DD - [contact or segment]
- Command source:
- Persona:
- Company type:
- Buyer / user / champion:
- Trigger discussed:
- Pain observed:
- Current workaround:
- Objections:
- Pricing / urgency signal:
- What changed in our thesis:
```

### objection_log.md

Purpose: append-only record of objections clustered by source and root cause.

Append when:

- `kickoff` backfills known recurring objections.
- `icp` surfaces buyer, user, or champion objections.
- `trust` surfaces trust, compliance, audit, or error-tolerance objections.
- `experiment` surfaces objections during tests or follow-ups.

Append format:

```markdown
# Objection Log

## YYYY-MM-DD - [short label]
- Command source:
- Source segment:
- Objection:
- Root cause guess:
- Type: [pain / buyer / trust / integration / ROI / timing / price / other]
- What evidence supports that guess:
- Follow-up action:
```

### experiment_log.md

Purpose: append-only record of planned experiments and later outcomes.

Append when:

- `kickoff` backfills active or recent experiments.
- `experiment` creates a new experiment.
- `experiment` receives results for a prior experiment and appends an outcome update instead of overwriting the old entry.

Append format:

```markdown
# Experiment Log

## YYYY-MM-DD - [experiment name]
- Status: [planned / running / complete / killed]
- Linked dimension:
- Hypothesis:
- Falsifier:
- Owner:
- Deadline:
- Method:
- Success threshold:
- Failure threshold:
- Ambiguous threshold:
- Decision rule:
- Expected signal:
- Result:
- Interpretation:
- Next decision:
```

### market_research_log.md

Purpose: append-only record of external market validation work tied to founder claims.

Append when:

- `kickoff` defines a market-research plan of attack worth preserving.
- `research` validates or challenges the founder story.
- `progress` should only read it, not append to it.

Append format:

```markdown
# Market Research Log

## YYYY-MM-DD - [research focus]
- Command source:
- Workflow / claim tested:
- Founder assertions tested:
- Observed external facts:
- Model inferences carried forward:
- Required source types:
- Minimum evidence threshold:
- Threshold met:
- What supports the story:
- What weakens the story:
- Strongest contradiction:
- Visible substitutes:
- Buyer / procurement clues:
- Trust / deployment clues:
- Sources or artifact types reviewed:
- Overall verdict:
- What changed in our thesis:
```

### wedge_graveyard.md

Purpose: preserve dead wedges and prevent repeated mistakes.

Append when:

- `wedge` recommends `kill`.
- `wedge` recommends `split` and one branch is explicitly deprioritized.

Append format:

```markdown
# Wedge Graveyard

## YYYY-MM-DD - [wedge name]
- Outcome: [kill / split-deprioritized]
- Workflow:
- User:
- Buyer:
- Why it died:
- Evidence:
- Surviving assets:
- Constraints for the next wedge:
- Routed next step:
```

### cohort_memory/

Purpose: optional shared accelerator memory across companies.

Use [cohort-memory.md](cohort-memory.md) for normalization and write thresholds.
If the directory does not exist, skip cohort reads and writes.

#### cohort_memory/wedge_failures.md

Append-only record of failed wedges across companies.

Primary writer:

- `wedge`

#### cohort_memory/objection_patterns.md

Append-only record of normalized objection patterns across companies.

Primary writers:

- `kickoff`
- `icp`
- `trust`
- `research`
- `experiment`

#### cohort_memory/trust_patterns.md

Append-only record of trust-boundary patterns across companies.

Primary writers:

- `trust`
- `progress`

#### cohort_memory/segment_benchmarks.md

Append-only record of segment benchmark snapshots across companies.

Primary writer:

- `progress`

## Update Rules

- Do not delete historical decisions unless the founder explicitly asks.
- When a wedge dies, clear only the active wedge fields that are no longer true; preserve the rest of company state.
- When a score changes, add a dated entry to `Score History` with a short reason, confidence label, and cited evidence or suppression reason.
- `progress` reads all founder logs and should not append to founder-specific logs unless it is explicitly recording a new decision in `founder_state.md`.
- `progress` may append to shared cohort memory files when [cohort-memory.md](cohort-memory.md) says the evidence threshold is met.
