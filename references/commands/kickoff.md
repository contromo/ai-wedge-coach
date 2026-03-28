# kickoff

`kickoff` initializes state or reseeds it after a dead wedge.

## Modes

- `Initial setup`: first-time state creation.
- `Reseed after kill`: preserve what was learned, clear the dead wedge, and define constraints for the next wedge.

`kickoff` is intake-first. If founder-specific facts are missing, do not fabricate a completed kickoff summary from placeholders or empty state.
If `kickoff` is inferred from a founder story that already contains useful context, use those facts immediately and ask the next missing question instead of restarting intake.
Use [../conversation-protocol.md](../conversation-protocol.md) for question cadence.
Use [../guided-flow.md](../guided-flow.md) for the onboarding sequence.

If the founder has prior interviews, objections, or experiments, backfill them into the optional append-only logs.

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
- `state.md` is mostly placeholder or scaffold text
- core fields are still mostly `Unknown`, `None`, `None recorded`, or equivalent boilerplate

In that case:

- ask for the missing intake directly
- if the founder already supplied partial intake, ask only for the next missing fact
- ask one best next question instead of a multi-question template
- do not output fake company facts
- do not assign an archetype from empty evidence
- do not claim confidence beyond the fact that intake is missing
- do not create durable baseline assessments until the founder has supplied enough facts to justify them

## Inferred Entry Behavior

When `kickoff` is inferred instead of explicitly requested:

- start with `I'm treating this as kickoff because [brief reason].`
- use any facts already present in the founder's message
- ask the next missing kickoff question, not a generic opener
- on follow-up turns, stay in `kickoff` without repeating the acknowledgement unless routing changes

## Required State Actions

- Create `state.md` if missing.
- Create optional logs only when the founder supplies backfill detail or a workflow trigger fires.
- If intake is incomplete, ask the single most useful next question first and wait for the founder's answer.
- Populate `state.md` as soon as there is enough information to make the state useful, even if some fields remain open.
- Keep `state.md` focused on `Current Thesis`, `Open Questions`, `Evidence Collected`, and `Next Move` until expanded mode is justified.
- Keep `Evidence Collected` split into `Observed facts`, `Founder assertions`, and `Model inferences` from the start.
- During early kickoff, update those four sections before adding expanded-mode detail.
- Backfill `interview_log.md`, `objection_log.md`, and `experiment_log.md` if the founder supplies prior history that warrants those logs.
- Append a starter entry to `market_research_log.md` only when kickoff defines concrete claims or open questions worth validating externally.
- If prior dead wedges are backfilled and `cohort_memory/wedge_failures.md` exists, append normalized failed-wedge entries using [../cohort-memory.md](../cohort-memory.md).
- If recurring objections are backfilled and `cohort_memory/objection_patterns.md` exists, append normalized objection entries using [../cohort-memory.md](../cohort-memory.md).
- If this is a reseed after `kill`, preserve surviving assets and next-wedge constraints from `wedge_graveyard.md`.
- Add `Company Assessments` and `Assessment History` only when the evidence depth justifies expanded mode.

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

If this is a bare `kickoff` with no founder-specific context yet, return exactly:

```markdown
Let's make this concrete fast.

Start with this: what are you building, in one sentence?

Rough bullets are fine.
```

If `kickoff` was inferred from a founder story or the founder has already given partial intake, and one more answer is needed before readback, return exactly:

```markdown
I'm treating this as kickoff because [brief reason].

[one best next question]
```

If `kickoff` is already active and discovery is still in progress, return exactly:

```markdown
[one best next question]
```

If intake is sufficient for discovery but not yet sufficient for a hard diagnosis, return exactly:

```markdown
## Current Thesis
- Company / product:
- Candidate workflow:
- Primary user:
- Economic buyer:
- Current workaround:
- Trust boundary:

## Open Questions
- ...

## Evidence Collected
- Observed fact:
- Founder assertion:
- Model inference:

## Next Move
- Immediate action:
- Why this now:

**Recommended next**: `[command]` - ...
```

If intake is complete enough to initialize state, return exactly:

```markdown
## Current Thesis
- Company:
- Product one-liner:
- Workflow wedge:
- Primary user:
- Economic buyer:
- Trigger:
- Current workaround:
- Trust boundary:

## Open Questions
- ...

## Evidence Collected
- Observed fact:
- Founder assertion:
- Model inference:

## Next Move
- Immediate action:
- Why this now:

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

- If the founder story is still mostly narrative and no usable state exists yet, keep `kickoff` active until the guided flow is complete.
- If the founder story needs external validation, recommend `research`.
- If the wedge is broad, recommend `wedge`.
- If the wedge was killed and a new segment is emerging, recommend `icp`.
- If the product ambition is "full agent" without a boundary, recommend `trust`.
- If evidence is thin, recommend `experiment`.
