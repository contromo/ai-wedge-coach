# progress

`progress` summarizes what has actually been learned across sessions.
It is also the accelerator operator handoff command.

If recent changes, evidence, or the current thesis are unclear, ask one clarifying question before producing the progress summary.

## Required Inputs

Read:

- `state.md`

If present, also read:

- `interview_log.md`
- `objection_log.md`
- `experiment_log.md`
- `market_research_log.md`
- `wedge_graveyard.md`
- `cohort_memory/wedge_failures.md`
- `cohort_memory/objection_patterns.md`
- `cohort_memory/trust_patterns.md`
- `cohort_memory/segment_benchmarks.md`

Use [../cohort-memory.md](../cohort-memory.md) when these files are available.

## Required Behavior

- Use `state.md` as the primary source of truth.
- If expanded assessment detail exists or is clearly warranted, assess the six company-level dimensions in [../rubrics.md](../rubrics.md).
- Show deltas using `Assessment History` when that section exists.
- Call out `Value Recurrence` explicitly every time.
- Identify at least one founder archetype when the evidence supports it.
- Identify the current coaching posture when the evidence supports it.
- Name repeated pathologies without drifting into generic coaching.
- Include what external market research has confirmed or weakened.
- Separate observed facts, founder assertions, and model inferences explicitly in the summary.
- Keep any dimension at `untested` when there is no direct observed support instead of pretending it is stronger.
- Produce accelerator ops outputs: partner briefing, weekly company status delta, red-flag memo, and `needs human help now` triggers.
- Evaluate whether human intervention is needed now, not just what the founder should do next.
- Compare the company against relevant cohort memory when shared cohort files are available.
- Surface sample-size caveats when the cohort memory is too thin for a strong comparison.

## Needs Human Help Now Triggers

Set `Needs human help now` to `yes` when one or more of these conditions fire:

- `Wedge reset`: the current wedge is dead, split without a credible surviving branch, or clearly needs reseeding.
- `Evidence stall`: evidence quality is `untested` or `weak evidence` and no meaningful new observed facts were added since the last snapshot.
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

## Founder-Facing Response

- If progress cannot be summarized honestly yet, ask one best next progress question only. If the real issue is missing or placeholder state, route to `kickoff`.
- Once there is enough clarity, keep the visible response concise. Cover:
  - the current trajectory across the company dimensions in use
  - an explicit read on `Value Recurrence`
  - the biggest improvement and biggest unresolved drag
  - the current best thesis, repeated pathology, or coaching posture when one materially matters
  - the next move and, when another command is clearly next, a consent-first handoff sentence
- Cohort memory, partner briefing, weekly delta, red-flag, and human-help outputs can still exist, but surface them only when they materially change the decision.

## State Updates

- Update `state.md` first.
- Refresh `Current Thesis`, `Open Questions`, `Evidence Collected`, and `Next Move`.
- Update `Company Assessments` and append to `Assessment History` only when expanded mode is active or newly warranted.
- Update `Founder Handling`, `Accelerator Ops`, and `Cohort Comparison` only when those sections exist or are newly warranted.
- If `cohort_memory/segment_benchmarks.md` exists and the segment is specific enough with direct observed support, append a new benchmark snapshot using [../cohort-memory.md](../cohort-memory.md).
- Update `Current Diagnosis` only if that section exists or is newly warranted.
