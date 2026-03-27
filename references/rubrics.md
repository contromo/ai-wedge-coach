# Rubrics

This skill uses two rubric layers:

- A company-level progress rubric used by `progress` and stored in `state.md` when expanded assessment detail is warranted.
- A wedge-specific rubric used only by `wedge`.

Use qualitative evidence states instead of numeric scores:

- `untested`
- `weak evidence`
- `validated`
- `strong`

Do not add totals, bands, or confidence overlays to rubric outputs.

## Evidence Taxonomy For Assessment

All assessment and diagnosis should separate:

- `Observed facts`
- `Founder assertions`
- `Model inferences`

Assessment rules:

- Observed facts can justify `validated` or `strong`.
- Founder assertions can shape a hypothesis, but they should not carry a dimension past `untested` or `weak evidence` by themselves.
- Model inferences can explain a pattern, but they should never be the only reason a dimension looks mature.
- If contradictions are meaningful, name them in the evidence note and avoid inflating the label.

## Assessment Reporting Rule

Never emit a naked assessment.

Every assessment must include:

- `Status`: `untested`, `weak evidence`, `validated`, or `strong`
- `Evidence`: a short citation to the observed fact or artifact that justifies the status

Assessment label rule:

- Use `untested` when no direct observed fact bears on that dimension yet.
- Use `weak evidence` when some signal exists, but it is thin, contradictory, or still carried mostly by founder assertions.
- Use `validated` when direct observed evidence supports the dimension enough to make a real decision.
- Use `strong` when multiple observed evidence types support the dimension and little contradiction remains.

## Company-Level Progress Rubric

Assess these six dimensions on every `progress` run and whenever a working command materially changes one of them.

### Wedge Sharpness

Definition: one workflow, one trigger, one primary user, and one clear measurable outcome.

- `untested`: workflow, trigger, or user is still too fuzzy to judge.
- `weak evidence`: one plausible workflow exists but boundaries are still unstable.
- `validated`: one workflow, one trigger, and one primary user are specific enough to operate against.
- `strong`: the wedge is narrow, explicit, and repeatedly legible without hand-waving.

### ICP Focus

Definition: user, buyer, and champion are separated; exclusions are explicit; beachhead is reachable.

- `untested`: the segment is still mostly asserted or blended across multiple audiences.
- `weak evidence`: a primary segment exists but buyer, exclusions, or reachability remain fuzzy.
- `validated`: the beachhead is narrow enough to act on and the buyer path is plausible.
- `strong`: the beachhead, buyer path, and non-targets are explicit and backed by direct evidence.

### Value Recurrence

Definition: the workflow repeats often enough and users return without heavy prompting.

- `untested`: recurrence is still a guess.
- `weak evidence`: recurrence is plausible, but direct observed repeat behavior is thin or segment-specific.
- `validated`: the workflow clearly recurs often enough to support repeat use.
- `strong`: recurrence is embedded in the workflow and reinforced by direct observed return behavior.

### Trust Architecture

Definition: autonomy and review boundaries match reversibility, observability, and risk.

- `untested`: the trust boundary is mostly unexplored.
- `weak evidence`: a plausible review boundary exists, but instrumentation or forbidden zones remain weak.
- `validated`: the autonomy boundary is coherent enough to support a safe first deployment.
- `strong`: autonomy map, review gates, and forbidden zones are crisp and adoption-safe.

### Evidence Quality

Definition: claims are backed by customer interviews, usage, objections, pricing, external market validation, or eval evidence.

- `untested`: the thesis still rests mainly on founder intuition.
- `weak evidence`: some real evidence exists but it is thin, inconsistent, or still mixed with too many assertions.
- `validated`: multiple observed artifacts support the current thesis enough to guide decisions.
- `strong`: multiple observed evidence types point in the same direction and consistently support decisions.

### Learning Velocity

Definition: the team runs falsifiable experiments and closes loops quickly.

- `untested`: there is no real learning loop yet.
- `weak evidence`: experiments happen, but owner, falsifier, thresholds, or decisions are still sloppy.
- `validated`: the team is running real experiments and closing decisions with usable cadence.
- `strong`: there is a repeatable loop of hypothesis, owner, falsifier, deadline, threshold, result, and decision.

## Wedge-Specific Rubric

Use this only inside `wedge`.

Assess these seven axes with the same four evidence states:

### Specificity

One concrete workflow, one trigger, one primary user.

- `untested`: the wedge is still category language or capability soup.
- `weak evidence`: one workflow exists but still competes with adjacent jobs.
- `validated`: the workflow sentence is explicit with a clear trigger and owner.
- `strong`: the workflow is consistently narrow and hard to confuse with adjacent work.

### Pain

Consequence of failure is material in time, money, or risk.

- `untested`: the consequence of failure is still mostly asserted.
- `weak evidence`: pain appears real but urgency or consequence remains fuzzy.
- `validated`: delay or failure clearly hurts enough to matter.
- `strong`: the pain is acute, visible, and repeatedly confirmed.

### Recurrence

The job happens often enough to support repeat use.

- `untested`: frequency is not yet known.
- `weak evidence`: recurrence appears plausible for some users or periods, but not reliably enough yet.
- `validated`: recurrence is directly supported enough to treat it as part of the wedge.
- `strong`: recurrence is embedded in weekly, daily, or event-triggered work and directly reinforced by user behavior.

### Buyer Alignment

The user pain maps cleanly to an economic owner.

- `untested`: the buyer is still unclear.
- `weak evidence`: a buyer is plausible but budget path remains inferred.
- `validated`: the economic owner is identifiable enough to pursue.
- `strong`: the economic owner, budget adjacency, and buying path are obvious and observed.

### Trust Fit

Useful automation is possible at an acceptable error cost.

- `untested`: the acceptable error boundary is still unclear.
- `weak evidence`: partial automation seems plausible but trust conditions remain soft.
- `validated`: useful automation is credible with an acceptable review cost.
- `strong`: autonomy is both useful and credibly safe within a well-defined trust boundary.

### Value Realization

Value is felt quickly and output quality is legible.

- `untested`: time-to-value and legibility are still mostly guessed.
- `weak evidence`: value appears, but setup or interpretation still slows adoption.
- `validated`: time-to-value is fast enough and the result is easy enough to judge.
- `strong`: value becomes obvious quickly and consistently to real users.

### Deployment Fit

Setup and integration burden are acceptable relative to value.

- `untested`: deployment burden has not been pressure-tested yet.
- `weak evidence`: setup cost appears real and may still outweigh value.
- `validated`: adoption burden looks acceptable for the value being promised.
- `strong`: the path to adoption is light and unlikely to block the wedge.

## Non-Rubric Why AI? Check

After the wedge assessment, answer:

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

Use the weakest or least-validated dimension as the first candidate for `Primary bottleneck`, but override that default if stronger evidence points elsewhere.

In every diagnosis, make clear:

- which points are observed facts
- which points are founder assertions still carrying the thesis
- which points are model inferences used to connect the dots

Diagnosis confidence labels:

- `High`: multiple observed evidence types agree.
- `Medium`: some observed evidence exists, but alternatives remain plausible or assertions still carry part of the case.
- `Low`: diagnosis is mostly inferred from sparse, assertion-heavy, or conflicting evidence.
