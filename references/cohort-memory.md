# Cohort Memory

Use this reference when the coach is being used by an accelerator, studio, or portfolio team that wants memory across multiple companies.

## Purpose

The goal is to stop relearning the same lesson company by company.

Track:

- common failed wedges
- repeated objection patterns
- trust-boundary patterns
- segment-specific benchmark snapshots

## Storage Model

Founder state is still company-specific.
Cohort memory is optional shared operator memory.

If a `cohort_memory/` directory exists in the current working directory, treat it as accelerator-wide shared memory and read or update it.
If the coach is used across multiple founder workspaces, point each workspace at the same `cohort_memory/` directory, typically by symlink or shared mount.
If the directory does not exist, skip cohort reads and writes without failing the founder workflow.

## Shared Files

- `cohort_memory/wedge_failures.md`
- `cohort_memory/objection_patterns.md`
- `cohort_memory/trust_patterns.md`
- `cohort_memory/segment_benchmarks.md`

## Evidence Rules

- Cohort memory should be built from observed facts, not founder optimism.
- Founder assertions can be preserved as context, but not as cohort truth.
- Model inferences can help cluster patterns, but they must be labeled as inferences.
- Do not write a cohort pattern entry unless at least one direct observed fact supports it.
- Do not call something a segment benchmark from one company alone. One company can add a benchmark snapshot; a usable benchmark requires at least `2` company snapshots in the same segment with direct observed evidence.

## Normalization Rules

Normalize entries so they can be compared later.

Use these fields whenever possible:

- segment
- workflow
- buyer
- trigger
- root-cause cluster
- trust mode
- retrieval tags

Suggested root-cause clusters:

- recurrence
- buyer-misalignment
- trust-blocker
- deployment-drag
- weak-pain
- no-ai-step-change
- services-drift
- timing
- integration
- data-readiness
- other

## Read Guidance

When reading cohort memory:

- prefer entries with matching segment, workflow, buyer, or trust mode
- surface only the most relevant pattern, not a dump of raw history
- distinguish `similar pattern exists` from `this company must have the same problem`
- if the cohort sample is too thin, say that explicitly

## Write Contracts

### wedge_failures.md

Purpose: preserve normalized failed wedge patterns across companies.

Append when:

- `wedge` recommends `kill`
- `wedge` recommends `split` and one branch is deprioritized
- `kickoff` backfills a previously dead wedge with real observed evidence

Append format:

```markdown
# Cohort Wedge Failures

## YYYY-MM-DD - [company] - [wedge label]
- Company:
- Segment:
- Workflow:
- Trigger:
- Buyer:
- Failure cluster:
- Observed facts:
- Founder assertions at time of failure:
- Surviving assets:
- Retrieval tags:
```

### objection_patterns.md

Purpose: track repeated objection patterns across companies.

Append when:

- `kickoff` backfills recurring objections
- `icp`, `trust`, `research`, or `experiment` surfaces a concrete objection with direct evidence

Append format:

```markdown
# Cohort Objection Patterns

## YYYY-MM-DD - [cluster label]
- Company:
- Segment:
- Workflow:
- Buyer / user / champion:
- Objection:
- Root cause cluster:
- Observed facts:
- Suggested countermeasure:
- Retrieval tags:
```

### trust_patterns.md

Purpose: preserve reusable trust-boundary patterns across workflows and segments.

Append when:

- `trust` reaches a concrete operating recommendation
- `research` or `progress` finds a repeated trust blocker pattern with direct evidence

Append format:

```markdown
# Cohort Trust Patterns

## YYYY-MM-DD - [pattern label]
- Company:
- Segment:
- Workflow:
- Recommended operating mode:
- Main trust blocker:
- Irreversible step:
- Review requirement:
- Observed facts:
- Outcome / adoption implication:
- Retrieval tags:
```

### segment_benchmarks.md

Purpose: preserve segment-level benchmark snapshots that can later be compared across companies.

Append when:

- `progress` has enough direct observed evidence to snapshot the current company's segment
- the segment is specific enough to compare later

Append format:

```markdown
# Segment Benchmarks

## YYYY-MM-DD - [segment label]
- Company:
- Segment:
- Workflow:
- Buyer clarity:
- Value recurrence read:
- Trust mode:
- Time-to-value read:
- Pilot / revenue read:
- Evidence quality read:
- Benchmark status: [provisional / usable]
- Observed facts:
- Retrieval tags:
```
