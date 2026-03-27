# State System

Runtime state lives in the founder's current working directory. Use append-only behavior for logs. Do not silently overwrite prior learning.

Do not commit runtime files as part of the skill package. They are founder-specific working state, not repo content.

## Canonical File Set

- `founder_state.md`
- `interview_log.md`
- `objection_log.md`
- `experiment_log.md`
- `market_research_log.md`
- `wedge_graveyard.md`

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
- Last wedge score:

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
- Interviews completed:
- Strongest signal:
- Weakest assumption:
- Pricing evidence:
- Retention evidence:
- Top objections:

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
- Evidence:
- If we're wrong:
- Recommended next command:

## Company Scores
- Wedge Sharpness:
- ICP Focus:
- Value Recurrence:
- Trust Architecture:
- Evidence Quality:
- Learning Velocity:

## Score History
- Date:
  - Wedge Sharpness:
  - ICP Focus:
  - Value Recurrence:
  - Trust Architecture:
  - Evidence Quality:
  - Learning Velocity:
  - Reason for score change:

## Active Experiments
1.
2.
3.

## Decision Log
- Date:
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
- What supports the story:
- What weakens the story:
- Visible substitutes:
- Buyer / procurement clues:
- Trust / deployment clues:
- Sources or artifact types reviewed:
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

## Update Rules

- Do not delete historical decisions unless the founder explicitly asks.
- When a wedge dies, clear only the active wedge fields that are no longer true; preserve the rest of company state.
- When a score changes, add a dated entry to `Score History` with a short reason.
- `progress` reads all files but should not append to the logs unless it is explicitly recording a new decision in `founder_state.md`.
