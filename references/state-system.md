# State System

Runtime state lives in the founder's current working directory.
Default mode is one-file-first: `state.md` is the only required runtime file.
Use append-only behavior for optional logs. Do not silently overwrite prior learning.

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
Use these tags literally inside `## Evidence Collected`:

- `Observed fact:`
- `Founder assertion:`
- `Model inference:`

## Default Mode File Set

- `state.md`

## Expanded Mode

Expanded mode is optional. Do not activate it by session count alone.
Activate lazy expansion when the workflow actually produces detail that is worth preserving:

- first real customer conversation: create `interview_log.md`
- first durable objection or trust blocker: create `objection_log.md`
- first real experiment: create `experiment_log.md`
- first external market validation pass: create `market_research_log.md`
- first killed or split-deprioritized wedge: create `wedge_graveyard.md`
- `state.md` is getting too long or too detailed to scan quickly: split supporting detail into the relevant log and keep `state.md` as the latest synthesis

When expanded mode is active, `state.md` stays canonical.
The logs hold append-only supporting detail. They do not replace `state.md`.

## Optional Expanded Files

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

## state.md

`state.md` is the canonical state file. All working commands update it first.
Use it for durable internal structure. Founder-facing replies do not need to mirror this schema unless the founder explicitly asks for a template or a structured dump.
When recording the next step, store it as a freeform coach-led move. You can optionally name the command in parentheses, for example `Map the trust boundary with the founder (command: trust)`.

Create it with this structure as soon as kickoff intake becomes useful:

```markdown
# State

## Current Thesis
- Company:
- Product one-liner:
- Current workflow wedge:
- Primary user:
- Economic buyer:
- Trigger:
- Current workaround:
- Trust boundary:
- Current bottleneck:

## Open Questions
- ...

## Evidence Collected
- Observed fact:
- Founder assertion:
- Model inference:

## Next Move
- Immediate action:
- Why this now:
- Next coach-led move:
```

Default mode rules:

- Keep `Current Thesis` to the best current read, not every discarded theory.
- Keep `Open Questions` to the highest-signal unresolved questions.
- Keep `Evidence Collected` as tagged bullets, not raw transcripts.
- Keep `Next Move` operational and singular when possible.

## Expanded Mode Sections Inside state.md

When more structure materially helps, add only the sections that are justified:
These sections are not required at kickoff. A fresh founder can stay in the four default sections until the coaching actually produces enough evidence, operator need, or workflow detail to warrant expansion.

### Market Reality
- Claims tested:
- Strongest external validation:
- Biggest external contradiction:
- Visible substitutes:
- Buyer / procurement clues:
- Trust / deployment clues:

### Founder Handling
- Current archetype:
- Coaching posture:
- Why this posture:
- What the coach should do next:

### Current Diagnosis
- Primary bottleneck:
- Confidence:
- Observed facts used:
- Founder assertions carrying load:
- Model inferences used:
- If we're wrong:
- Next coach-led move:

### Company Assessments
- Wedge Sharpness: [untested / weak evidence / validated / strong] | Evidence: ...
- ICP Focus: [untested / weak evidence / validated / strong] | Evidence: ...
- Value Recurrence: [untested / weak evidence / validated / strong] | Evidence: ...
- Trust Architecture: [untested / weak evidence / validated / strong] | Evidence: ...
- Evidence Quality: [untested / weak evidence / validated / strong] | Evidence: ...
- Learning Velocity: [untested / weak evidence / validated / strong] | Evidence: ...

### Assessment History
| Date | Wedge | ICP | Recurrence | Trust | Evidence | Velocity | Trigger |
|------|-------|-----|------------|-------|----------|----------|---------|
| YYYY-MM-DD |  |  |  |  |  |  | initial baseline / assessment change trigger |

### Active Experiments
- Name:
- Status:
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

### Decision Log
- Older decisions summary:
- Date:
  - Source experiment:
  - Decision:
  - Why:
  - Evidence:
  - Revisit when:

### Accelerator Ops
- Partner briefing:
- Weekly company status delta:
- Red-flag memo:
- Needs human help now:
- Trigger(s):
- Suggested human owner:
- Suggested intervention:
- By when:

### Cohort Comparison
- Similar failed wedge patterns:
- Repeated objection patterns:
- Relevant trust-boundary patterns:
- Segment benchmark read:
- Where this company is above cohort:
- Where this company is below cohort:
- Cohort sample caveat:

## Write Contracts

All working commands update `state.md` first.
Whenever a working command materially changes the thesis, update `Current Thesis`, `Open Questions`, `Evidence Collected`, and `Next Move` before writing supporting detail anywhere else.
`kickoff` and `progress` are the canonical commands for updating `Founder Handling` when that section exists.
`progress` is the canonical command for updating `Accelerator Ops` and `Cohort Comparison` when those sections exist.

## Experiment Feedback Loop

`experiment` is the canonical command for maintaining experiment state.

When an experiment is created or updated:

- update `Next Move` in `state.md`
- ensure owner, deadline, falsifier, thresholds, and decision rule are all present
- if `Active Experiments` exists or the experiment cadence is real enough to justify expanded mode, write the structured experiment entry there
- append the experiment plan to `experiment_log.md`, creating the file if needed

When an experiment result is reported:

- append the outcome to `experiment_log.md`
- update the matching `Active Experiments` entry with `Latest result`, `Status`, and `Next decision` if that section exists
- update `Evidence Collected` with any new observed facts
- update `Current Thesis`, `Open Questions`, and `Next Move`
- update `Current Diagnosis` if that section exists and the result materially changes the best current thesis
- append a `Decision Log` entry if that section exists and the result triggered a real decision
- update linked assessments only when `Company Assessments` is in use

## Decision Log Archival Rule

When `Decision Log` in `state.md` exceeds `15` entries:

- compress older entries into `Older decisions summary`
- keep the most recent `10` full entries
- preserve the main narrative arc, major thesis changes, and still-open revisitation points
- do not drop unresolved decisions just to hit the limit

These logs are optional. Create each one only when its trigger first fires.

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
- When a wedge dies, clear only the active wedge fields in `state.md` that are no longer true; preserve the rest of company state.
- Do not create expanded-mode sections just to satisfy a template. Add them only when they are materially useful.
- When an assessment changes and `Assessment History` exists or expanded mode clearly warrants it, append a dated row.
- Use the compact columns `Wedge`, `ICP`, `Recurrence`, `Trust`, `Evidence`, `Velocity`, and `Trigger`.
- Use only `untested`, `weak evidence`, `validated`, or `strong` in assessment cells.
- `progress` always reads `state.md` and reads founder-specific logs only if they exist.
- `progress` should not append to founder-specific logs unless it is explicitly recording a new decision or expanded-mode update in `state.md`.
- `progress` may append to shared cohort memory files when [cohort-memory.md](cohort-memory.md) says the evidence threshold is met.
