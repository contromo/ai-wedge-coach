# kickoff

`kickoff` initializes founder state or reseeds it after a dead wedge.

## Modes

- `Initial setup`: first-time state creation.
- `Reseed after kill`: preserve what was learned, clear the dead wedge, and define constraints for the next wedge.

`kickoff` is intake-first. If founder-specific facts are missing, do not fabricate a completed kickoff summary from placeholders or empty state.
Use [../conversation-protocol.md](../conversation-protocol.md) for question cadence.
Use [../guided-flow.md](../guided-flow.md) for the onboarding sequence.

If the founder has prior interviews, objections, or experiments, backfill them into the append-only logs.

## Required Collection

Collect enough to populate:

- Company snapshot
- Current or next wedge hypothesis
- Primary ICP hypothesis
- Trust concern
- Evidence baseline
- Current bottleneck

Also detect one primary archetype and coaching posture from [../archetypes.md](../archetypes.md) when possible.

## Guided Pre-Diagnosis Flow

Before formal diagnosis on a new founder, move through:

1. Founder narrative
2. Workflow extraction
3. Evidence audit
4. Market reality check
5. Plan of attack

Do not jump straight from intake to hard diagnosis unless the founder already has substantial evidence.

## Empty Or Placeholder State Rule

Treat the workspace as uninitialized if any of the following are true:

- runtime files do not exist
- runtime files are empty
- `founder_state.md` is mostly placeholder or scaffold text
- core fields are still mostly `Unknown`, `None`, `None recorded`, or equivalent boilerplate

In that case:

- ask for the missing intake directly
- ask one best next question instead of a multi-question template
- do not output fake company facts
- do not assign an archetype from empty evidence
- do not claim confidence beyond the fact that intake is missing
- do not create durable baseline scores until the founder has supplied enough facts to justify them

## Required State Actions

- Create all runtime files if missing.
- If intake is incomplete, ask the single most useful next question first and wait for the founder's answer.
- Populate `founder_state.md` as soon as there is enough information to make the state useful, even if some fields remain open.
- Keep `Evidence Log` split into `Observed facts`, `Founder assertions`, and `Model inferences` from the start.
- Populate `Founder Handling` as soon as there is enough evidence to justify an archetype or posture. Do not invent one from thin signal.
- During early kickoff, populate `Guided Discovery`, `Market Reality Check`, and `Current plan of attack` before scoring aggressively.
- Backfill `interview_log.md`, `objection_log.md`, and `experiment_log.md` if the founder supplies prior history.
- Append a starter entry to `market_research_log.md` when kickoff defines concrete claims or open questions worth validating externally.
- If prior dead wedges are backfilled and `cohort_memory/wedge_failures.md` exists, append normalized failed-wedge entries using [../cohort-memory.md](../cohort-memory.md).
- If recurring objections are backfilled and `cohort_memory/objection_patterns.md` exists, append normalized objection entries using [../cohort-memory.md](../cohort-memory.md).
- If this is a reseed after `kill`, preserve surviving assets and next-wedge constraints from `wedge_graveyard.md`.
- Record the first `Company Scores` baseline and append a `Score History` row with the trigger `initial baseline` or `reseed after wedge kill` only when each numeric score has direct observed support.
- If a dimension lacks direct observed support, mark that score as `suppressed` with a reason instead of forcing a baseline number.

## Intake Checklist

When facts are missing, collect this intake:

- Company
- Stage
- Team size
- Product one-liner
- Single workflow to own
- Primary user
- Economic buyer
- Champion
- Trigger moment
- Current workaround
- Consequence of failure
- Frequency
- Time-to-value
- What the AI does
- What requires human review
- What must stay human
- Prior interviews, objections, pilots, or experiments to backfill

Prefer one question at a time rather than a long template.

## Minimal Viable Kickoff Threshold

You have enough to initialize useful founder state when you have at least:

- a product one-liner or company description
- one candidate workflow wedge
- one primary user
- one trigger or current workaround
- a rough description of what the AI does

Do not block on having every buyer, trust, and evidence detail perfectly filled in before moving forward.

## Output Schema

If intake is incomplete, return exactly:

```markdown
Let's make this concrete fast.

Start with this: what are you building, in one sentence?

Rough bullets are fine.
```

If discovery is still in progress and one more answer is needed before readback, return exactly:

```markdown
[one best next question]
```

If intake is sufficient for discovery but not yet sufficient for a hard diagnosis, return exactly:

```markdown
## Kickoff Readback
- What you're building:
- Candidate workflow:
- Primary user:
- Economic buyer:
- Current workaround:
- AI role:

## Evidence Classification
- Observed facts:
- Founder assertions:
- Model inferences:

## Founder Handling
- Current archetype:
- Coaching posture:
- Why this posture now:

## What Looks Promising
- ...

## What Needs Validation
- ...

## Plan Of Attack
1. ...
2. ...
3. ...

**Recommended next**: `[command]` - ...
```

If intake is complete enough to initialize state, return exactly:

```markdown
## Kickoff Summary
- Mode:
- Company:
- Product one-liner:
- Primary concern:
- Current archetype:

## Company Snapshot
- Stage:
- Team size:
- Sales motion:
- Revenue / pilots / design partners:

## Current Thesis
- Workflow wedge:
- Primary user:
- Economic buyer:
- Trigger:
- Why now:

## Baseline Scores
- Wedge Sharpness: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- ICP Focus: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Value Recurrence: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Trust Architecture: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Evidence Quality: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Learning Velocity: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...

## Evidence Classification
- Observed facts:
- Founder assertions:
- Model inferences:

## Founder Handling
- Current archetype:
- Coaching posture:
- Why this posture now:

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

## Routing Guidance

- If the founder story needs external validation, recommend `research`.
- If the wedge is broad, recommend `wedge`.
- If the wedge was killed and a new segment is emerging, recommend `icp`.
- If the product ambition is "full agent" without a boundary, recommend `trust`.
- If evidence is thin, recommend `experiment`.
