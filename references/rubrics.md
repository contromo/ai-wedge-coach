# Rubrics

This skill uses two scoring layers:

- A company-level progress rubric used by `progress` and stored in `founder_state.md`.
- A wedge-specific rubric used only by `wedge`.

Use 1-5 integer scores only when a numeric score is justified. Do not invent half-points.
If the evidence is too weak, suppress the score instead of forcing a number.

## Evidence Taxonomy For Scoring

All scoring and diagnosis should separate:

- `Observed facts`
- `Founder assertions`
- `Model inferences`

Scoring rules:

- Observed facts can support strong scores and high confidence.
- Founder assertions can shape a hypothesis, but they should not justify an aggressive score by themselves.
- Model inferences can explain a pattern, but they should never be the only reason a score moves.
- If a dimension depends mostly on assertions or inferences, suppress the score and say why.

## Score Reporting Rule

Never emit a naked score.

Every score must include:

- `Score`: `1-5` or `suppressed`
- `Confidence`: `High`, `Medium`, `Low`, or `n/a`
- `Evidence`: a short citation to the observed fact or artifact that justifies the score, or the reason the score was suppressed

Numeric score rule:

- Use a numeric score only when at least one direct observed fact bears on that dimension.
- If the support is mostly founder assertions or model inferences, suppress the score.
- If contradictions are strong enough that a single number would be misleading, suppress the score until the contradiction is resolved.

Score confidence rule:

- `High`: multiple direct observed facts support the score and little contradiction remains.
- `Medium`: at least one direct observed fact supports the score, but gaps or caveats remain.
- `Low`: a small amount of direct observed evidence supports the score, but it is still fragile.
- If no direct observed fact exists, use `suppressed` rather than `Low`.

Wedge total rule:

- Compute `Total` and `Band` only when all seven wedge axes have numeric scores.
- If any wedge axis is suppressed, suppress `Total` and `Band` and say which axes were not scorable.

## Company-Level Progress Rubric

Score these six dimensions on every `progress` run and whenever a working command materially changes one of them.

### Wedge Sharpness

Definition: one workflow, one trigger, one primary user, and one clear measurable outcome.

- `1`: broad category language, multiple workflows, fuzzy output.
- `3`: one plausible workflow exists but boundaries are still unstable.
- `5`: narrow, explicit, and easy to restate without hand-waving.

### ICP Focus

Definition: user, buyer, and champion are separated; exclusions are explicit; beachhead is reachable.

- `1`: "everyone" or multiple unrelated segments.
- `3`: primary segment exists but buyer or exclusions remain fuzzy.
- `5`: narrow beachhead with clear buyer path and explicit non-targets.

### Value Recurrence

Definition: the workflow repeats often enough and users return without heavy prompting.

- `1`: episodic or novelty-driven; repeat use is asserted, not observed.
- `3`: recurring in theory or in a subset, but behavior is unstable.
- `5`: recurrence is clearly embedded in the workflow and reinforced by observed return behavior.

### Trust Architecture

Definition: autonomy and review boundaries match reversibility, observability, and risk.

- `1`: "full agent" ambition without error-boundary clarity.
- `3`: plausible review boundary but weak instrumentation or red lines.
- `5`: autonomy map, review gates, and forbidden zones are crisp and adoption-safe.

### Evidence Quality

Definition: claims are backed by customer interviews, usage, objections, pricing, external market validation, or eval evidence.

- `1`: mostly founder intuition or anecdote.
- `3`: some real evidence exists but it is thin, inconsistent, unranked, or mixed with too many assertions.
- `5`: multiple observed evidence types point in the same direction and support decisions.

### Learning Velocity

Definition: the team runs falsifiable experiments and closes loops quickly.

- `1`: building dominates learning; no clear hypotheses or deadlines.
- `3`: experiments happen, but owner, falsifier, thresholds, or decisions are sloppy.
- `5`: there is a repeatable cadence of hypothesis, owner, falsifier, deadline, threshold, result, and decision.

## Wedge-Specific Rubric

Use this only inside `wedge`.

Score range and bands:

- `29-35`: strong candidate
- `22-28`: plausible but fuzzy
- `15-21`: dangerous
- `<15`: founder fiction or services drift

### Specificity

One concrete workflow, one trigger, one primary user.

- `1`: category language or capability soup.
- `3`: one workflow exists but still competes with adjacent jobs.
- `5`: explicit workflow sentence with clear trigger and owner.

### Pain

Consequence of failure is material in time, money, or risk.

- `1`: nice-to-have or curiosity.
- `3`: meaningful pain but weak urgency or vague consequences.
- `5`: delay or failure obviously hurts.

### Recurrence

The job happens often enough to support repeat use.

- `1`: episodic or low-frequency.
- `3`: recurring for some segments or periods, but not reliably.
- `5`: embedded in weekly, daily, or event-triggered recurring work.

### Buyer Alignment

The user pain maps cleanly to an economic owner.

- `1`: user feels pain but buyer is unclear or misaligned.
- `3`: buyer is plausible but budget path is still inferred.
- `5`: the economic owner and budget adjacency are obvious.

### Trust Fit

Useful automation is possible at an acceptable error cost.

- `1`: failure cost is high and reviewability is weak.
- `3`: partial automation is plausible but trust conditions need work.
- `5`: useful autonomy is credible with acceptable risk and correction cost.

### Value Realization

Value is felt quickly and output quality is legible.

- `1`: delayed payoff or hard-to-read outcomes.
- `3`: value appears, but setup or interpretation slows adoption.
- `5`: time-to-value is fast and the result is easy to judge.

### Deployment Fit

Setup and integration burden are acceptable relative to value.

- `1`: integration tax dominates.
- `3`: deployment burden is real but may be worth it.
- `5`: adoption path is light enough for the value being promised.

## Non-Scored Why AI? Check

After the wedge score, answer:

- Does AI create a real step-change here?
- If AI disappeared, would the wedge still be compelling?
- Is the product really a workflow wedge, or is it just a nicer interface on generic software?

If the answer is weak, say so in the diagnosis. Do not turn this into an eighth rubric axis.

## Mapping Between Layers

- `Wedge Sharpness` is driven mainly by `Specificity`, `Pain`, and `Value Realization`.
- `ICP Focus` is informed by `Buyer Alignment` and the output of `icp`.
- `Value Recurrence` is fed directly by `Recurrence`.
- `Trust Architecture` is informed by `Trust Fit` and the output of `trust`.
- `Evidence Quality` is influenced by the strength of interviews, objections, usage, pricing, market research, and experiment results.
- `Learning Velocity` is influenced by experiment quality, decision cadence, and whether dead wedges are retired cleanly.

## Diagnosis Guidance

Use the weakest score as the first candidate for `Primary bottleneck`, but override that default if stronger evidence points elsewhere.

In every diagnosis, make clear:

- which points are observed facts
- which points are founder assertions still carrying the thesis
- which points are model inferences used to connect the dots

Confidence labels:

- `High`: multiple observed evidence types agree.
- `Medium`: some observed evidence exists, but alternatives remain plausible or assertions still carry part of the case.
- `Low`: diagnosis is mostly inferred from sparse, assertion-heavy, or conflicting evidence.
