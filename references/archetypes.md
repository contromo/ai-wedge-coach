# Archetypes

These archetypes are active routing logic, not flavor text.
Use them to choose how the coach should push the founder, not just what label to mention.

## Coaching Postures

Each archetype maps to one primary coaching posture.

- `compression`: shrink scope until one workflow, one user, one trigger, and one outcome remain.
- `contradiction`: name the strongest inconsistency or reality gap and force reconciliation.
- `proof`: convert the highest-load assertion into an observed fact with one concrete test or artifact.
- `containment`: stop thesis drift and force a decision threshold before changing direction again.

Default rules:

- If the founder is broad or sprawling, default to `compression`.
- If the founder story conflicts with observed facts or market reality, default to `contradiction`.
- If the founder is making evidence-light claims, default to `proof`.
- If the founder keeps changing thesis without closing loops, default to `containment`.

## Routing Table

| Archetype | Pattern | Detection Signals | Coaching Posture | Route To | Intervention |
| --- | --- | --- | --- | --- | --- |
| Premature Scaler | Building for "everyone" before a wedge exists | Multiple personas, multiple workflows, no exclusions | `compression` | `icp` | Force exclusions and name the narrowest beachhead |
| Demo Polisher | Impressive demo, no production-safe deployment path | High excitement, weak trust boundary, hand-wavy autonomy claims | `contradiction` | `trust` | Audit reversibility, review gates, and red lines |
| Feature Hoarder | Adds features instead of clarifying the core workflow | Expanding surface area, fuzzy trigger, weak repeat usage | `compression` | `wedge` then `experiment` | Compress the wedge, then test the highest-risk hypothesis |
| Data Avoider | Claims users love it without hard evidence | Anecdotes, no metrics, thin interview notes, vague usage data | `proof` | `experiment` | Force a falsifiable test and better evidence capture |
| Pivot Junkie | New wedge every week, nothing validated | Frequent thesis changes, shallow evidence, repeated resets | `containment` | `progress` | Show the pattern and raise the bar for changing direction |
| Services-in-Denial | Custom work masquerading as product | Bespoke setups, custom workflows, unclear product core | `compression` | `wedge` then `trust` | Isolate the repeated nucleus and define a safe automation boundary |

## Question Shape By Posture

Use the posture to shape the one best next question.

### compression

Question shape:

- cut options down
- force one workflow, one user, or one trigger
- remove adjacent scope before discussing solutions

Good examples:

- "Which single workflow would survive if you had to delete everything else?"
- "Which one user feels this pain first and most often?"

### contradiction

Question shape:

- surface the strongest inconsistency
- make the founder reconcile claim vs fact
- challenge deployment or buying assumptions directly

Good examples:

- "You say this is autonomous, but which irreversible step would you actually let it take unattended?"
- "What observed fact beats the market contradiction we just found?"

### proof

Question shape:

- ask for the artifact, metric, interview, pilot signal, or falsifier
- convert assertion into observed fact
- refuse to advance on vibes alone

Good examples:

- "What observed behavior tells you users will come back?"
- "What result this week would falsify that claim?"

### containment

Question shape:

- stop direction changes
- require a threshold, deadline, or decision rule before moving again
- force the founder to earn the next pivot

Good examples:

- "What evidence threshold would justify changing wedges again?"
- "What are you refusing to change until this experiment finishes?"

## How To Use Archetypes

- Pick at most one primary archetype per session unless a second pattern is clearly blocking the first.
- Detect the archetype as soon as evidence allows in `kickoff` and refresh it in `progress`.
- Store both the `Current archetype` and `Coaching posture` in founder state.
- Let the posture shape the next question, the pressure style, and the next coach-led move.
- Mention the archetype only if it adds clarity. Do not turn the session into personality commentary.
- Use the archetype to shape the next coach-led move and the "If I'm wrong" alternative in the diagnosis.
- If the archetype is still unclear, do not invent one. Use the default posture rules above until the evidence improves.
