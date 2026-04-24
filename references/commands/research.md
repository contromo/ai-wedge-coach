# research

`research` validates founder claims against external market evidence.

`market` is an alias.

Use this command when the founder has a plausible story but weak proof, or when you need to sanity-check wedge, buyer, urgency, substitutes, or trust assumptions before locking in a diagnosis.

If the claim under test is still fuzzy, ask one clarifying question before doing research.

Stay in `research` mode until the claim under test is precise enough to investigate.

Read [../market-research.md](../market-research.md) before running this command.

## Inputs

Use the current founder thesis and research these claims where possible:

- the workflow is real
- the workflow is recurring
- the pain is consequential
- the likely buyer exists
- substitutes and current workarounds are visible
- trust, compliance, or deployment constraints are plausible

## Operational Standard

Treat `research` as a lightweight diligence pass, not generic internet browsing.

For each research run:

1. Define the single workflow, segment, or claim under test.
2. Write down the founder assertions being tested.
3. Review the minimum source mix from [../market-research.md](../market-research.md).
4. Separate observed external facts from model inferences.
5. Score each claim as `supported`, `mixed`, `contradicted`, or `insufficient evidence`.
6. Surface the highest-signal contradiction explicitly instead of averaging it away.
7. If the minimum threshold is not met, say `insufficient evidence` rather than pretending the market check is complete.

If the current coaching posture is `contradiction`, prioritize the strongest disconfirming evidence first.
If the current coaching posture is `proof`, prioritize converting the highest-load founder assertion into an observed external fact.

Do not call a claim `supported` from one good-looking source or repeated vendor copy.

## Verdict Rules

Use these verdicts for each major claim:

- `supported`: enough independent evidence exists and no stronger contradiction outweighs it.
- `mixed`: real support exists, but meaningful contradiction or segmentation caveats remain.
- `contradicted`: the best available evidence points against the founder story.
- `insufficient evidence`: the source mix or evidence count is too weak to make a responsible call.

## State And Logging

- Update `state.md` first.
- Refresh `Current Thesis`, `Open Questions`, `Evidence Collected`, and `Next Move` when research materially changes the best current thesis.
- Update `Current Diagnosis` only if expanded mode is active or the research clearly warrants that section.
- Append a summary entry to `market_research_log.md`, creating the file if needed.
- If research uncovers concrete objections, append them to `objection_log.md`, creating the file if needed.
- If `cohort_memory/objection_patterns.md` exists and research uncovered a concrete objection with direct evidence, append a normalized objection pattern entry using [../cohort-memory.md](../cohort-memory.md).
- Record the source types reviewed, whether the minimum threshold was met, the strongest contradiction, and the overall verdict.

## Founder-Facing Response

- If the claim under test is still unclear, ask one best next research question only.
- Once there is enough clarity, keep the visible response concise. Cover:
  - the workflow or claim under test and why it matters
  - the strongest support for the founder story
  - the strongest contradiction or weakening signal
  - visible substitutes, buyer clues, or trust concerns when they matter
  - what the research changes, one next move, and, when another command is clearly next, a consent-first handoff sentence
- The source mix, evidence threshold, claim verdicts, and evidence classification still matter, but do not force them into the visible reply if a tighter market read communicates the result more clearly.
