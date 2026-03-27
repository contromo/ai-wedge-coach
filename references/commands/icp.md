# icp

`icp` pressure-tests who the product is really for.

If user, buyer, champion, or trigger are still ambiguous, ask one clarifying question at a time before producing the full ICP snapshot.

Stay in `icp` mode until the beachhead is clear enough to name credibly.

## Non-Negotiables

- Separate user, buyer, and champion explicitly.
- Name the trigger event and current workaround.
- Force explicit exclusions.
- Pick the narrowest plausible beachhead instead of a compromise segment.

## Evidence Handling

If the founder shares customer conversations, append them to `interview_log.md`.
If they share objections, append them to `objection_log.md`.

## Output Schema

If the ICP is still too ambiguous, return exactly:

```markdown
[one best next ICP question]
```

Once there is enough clarity, return exactly:

```markdown
## ICP Snapshot
- Primary persona:
- Company type:
- User:
- Economic buyer:
- Champion:
- Trigger event:
- Current workaround:

## Exclusions
- Explicit non-targets:

## Beachhead Verdict
- Narrowest credible beachhead:
- Why this segment first:

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

- Update `ICP Hypotheses`.
- Update `ICP Focus` in company scores.
- Update `Current Diagnosis` and `Next 7 Days`.
