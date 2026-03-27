# progress

`progress` summarizes what has actually been learned across sessions.
It is also the accelerator operator handoff command.

If recent changes, evidence, or the current thesis are unclear, ask one clarifying question before producing the progress summary.

## Required Inputs

Read:

- `founder_state.md`
- `interview_log.md`
- `objection_log.md`
- `experiment_log.md`
- `market_research_log.md`
- `wedge_graveyard.md`

If present, also read:

- `cohort_memory/wedge_failures.md`
- `cohort_memory/objection_patterns.md`
- `cohort_memory/trust_patterns.md`
- `cohort_memory/segment_benchmarks.md`

Use [../cohort-memory.md](../cohort-memory.md) when these files are available.

## Required Behavior

- Score only the six company-level dimensions in [../rubrics.md](../rubrics.md).
- Show deltas using `Score History`.
- Call out `Value Recurrence` explicitly every time.
- Identify at least one founder archetype when the evidence supports it.
- Name repeated pathologies without drifting into generic coaching.
- Include what external market research has confirmed or weakened.
- Separate observed facts, founder assertions, and model inferences explicitly in the summary.
- Suppress any dimension that lacks direct observed support instead of forcing a numeric score.
- Produce accelerator ops outputs: partner briefing, weekly company status delta, red-flag memo, and `needs human help now` triggers.
- Evaluate whether human intervention is needed now, not just what the founder should do next.
- Compare the company against relevant cohort memory when shared cohort files are available.
- Surface sample-size caveats when the cohort memory is too thin for a strong comparison.

## Needs Human Help Now Triggers

Set `Needs human help now` to `yes` when one or more of these conditions fire:

- `Wedge reset`: the current wedge is dead, split without a credible surviving branch, or clearly needs reseeding.
- `Evidence stall`: evidence quality is weak or suppressed and no meaningful new observed facts were added since the last snapshot.
- `Buyer blockage`: the buyer path is still unclear and that ambiguity is blocking sales, pilots, or wedge selection.
- `Trust blocker`: trust, compliance, audit, or irreversible-action constraints require expert intervention beyond the founder team.
- `External contradiction`: market research, pilot feedback, or user behavior materially undermines the current thesis.
- `Founder thrash`: repeated pathology, abandoned experiments, or contradictory wedge changes suggest human coaching is needed.
- `Pilot risk`: a design partner, pilot, or high-signal user relationship appears at risk right now.

When a trigger fires:

- name the trigger explicitly
- say why it matters now
- recommend the human owner or type of operator who should step in
- recommend the immediate intervention, not just more analysis

## Output Schema

If progress cannot be summarized honestly yet, return exactly:

```markdown
[one best next progress question]
```

Once there is enough clarity, return exactly:

```markdown
## Current Scoreboard
- Wedge Sharpness: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- ICP Focus: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Value Recurrence: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Trust Architecture: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Evidence Quality: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...
- Learning Velocity: [1-5 or suppressed] | Confidence: [High / Medium / Low / n/a] | Evidence: ...

## Score Trend
- Biggest improvement:
- Biggest unresolved drag:
- Value recurrence read:

## Pattern Read
- Primary archetype:
- Repeated pathology:
- Current best thesis:

## Evidence Classification
- Observed facts:
- Founder assertions:
- Model inferences:

## Market Reality
- Strongest external confirmation:
- Biggest external contradiction:
- What still needs validation:

## Cohort Memory
- Similar failed wedge pattern:
- Repeated objection pattern:
- Relevant trust-boundary pattern:
- Segment benchmark:
- Where this company is above cohort:
- Where this company is below cohort:
- Cohort sample caveat:

## Partner Briefing
- Company in one line:
- What matters this week:
- Primary bottleneck for partners:
- Best current thesis:
- Recommended partner action:

## Weekly Status Delta
- New observed facts since last snapshot:
- Thesis change since last snapshot:
- Score changes since last snapshot:
- Decision changes since last snapshot:

## Red-Flag Memo
- Status: [none / active]
- Primary red flag:
- Why this matters:
- Evidence:
- Immediate mitigation:

## Needs Human Help Now
- Triggered: [yes / no]
- Trigger(s):
- Suggested human owner:
- Suggested intervention:
- By when:

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

- Update `Company Scores`.
- Append a new `Score History` entry when scores changed since the last snapshot, including confidence, evidence, or suppression reason.
- Refresh `Evidence Log` when the evidence mix or thesis changed.
- Update `Accelerator Ops`.
- Update `Cohort Comparison`.
- If `cohort_memory/segment_benchmarks.md` exists and the segment is specific enough with direct observed support, append a new benchmark snapshot using [../cohort-memory.md](../cohort-memory.md).
- Update `Current Diagnosis` and `Next 7 Days`.
