# Diagnosis Trees

Use these trees when the founder's bottleneck is unclear or when a command needs a structured branch.

## Retention And Recurrence Tree

Use this in `wedge`, `progress`, and `experiment` whenever the founder says users liked the demo but did not come back.

1. Is the workflow genuinely recurring?
   - `No` -> likely episodic workflow masquerading as product.
   - `Yes` -> continue.
2. Are users returning without heavy prompting?
   - `No` -> likely novelty trap, weak embed, or low urgency.
   - `Yes` -> continue.
3. Is the retained cohort concentrated in one segment?
   - `Yes` -> likely hidden ICP; route toward `icp`.
   - `No` -> broad curiosity may be hiding weak pull.
4. Is the value tied to money, time, or risk?
   - `No` -> likely nice-to-have.
   - `Yes` -> continue.
5. Is trust failure blocking repeat use?
   - `Yes` -> route toward `trust`.
   - `No` -> continue.
6. Is setup or integration burden too high relative to value?
   - `Yes` -> deployment tax is killing recurrence.
   - `No` -> the wedge or ICP is still probably wrong.

Likely diagnoses:

- Wrong wedge
- Wrong ICP
- Novelty trap
- Trust boundary too aggressive
- Insufficient ROI clarity
- Onboarding or integration burden too high
- Episodic workflow masquerading as product

## Trust Boundary Tree

Use this in `trust` and anywhere the founder pushes for "full agent" behavior.

1. Does the action create irreversible consequences?
   - `Yes` -> default away from unattended automation.
2. Can errors be cheaply reviewed before execution?
   - `No` -> prefer copilot or human-only steps.
3. Is the output objectively checkable?
   - `No` -> trust cost is high; prefer review or human ownership.
4. Are there clear confidence signals or fallback behavior?
   - `No` -> require instrumentation before expanding autonomy.
5. Is audit history required?
   - `Yes` -> insist on logging and approval artifacts.
6. Does the human currently act by judgment or by deterministic policy?
   - `Judgment-heavy` -> prefer review queue or copilot.
   - `Policy-heavy` -> constrained automation is more plausible.
7. Would a 5% failure rate kill adoption?
   - `Yes` -> keep autonomy narrow.
8. Does partial automation already create most of the value?
   - `Yes` -> do not force an agent narrative.

Recommendation rules:

- `Copilot first` when trust costs are high and outputs are subjective.
- `Review queue` when outputs are inspectable but execution risk is nontrivial.
- `Constrained agent` when the domain is structured, rollback exists, and red lines are clear.
- `Full automation` only when outputs are highly verifiable and failure cost is low.
