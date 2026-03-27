# Founder State

## Company Snapshot
- Company: Unknown
- Stage: Unknown
- Team size: Unknown
- Category: Candidate: legislative interview-prep intelligence for congressional reporting
- Product one-liner: AI-generated interview-prep briefs for journalists interviewing members of Congress, starting with bill summaries and clause analysis tied to that member's record.
- Funding context: Unknown
- Sales motion: Unknown
- Current revenue: Unknown
- Active pilots: Unknown
- Design partners: Unknown
- Main concern right now: Choose one beachhead user and prove the workflow recurs often enough to support repeat use.

## Current Primary Wedge
- Workflow: Candidate: help a journalist prep for an interview with a member of Congress by quickly assembling that member's legislative record and issue history.
- Job to be done: Turn legislative context into an interview-prep brief covering the member's record and the issues they have cared about, so the journalist can ask sharper questions.
- Primary user: Candidate: journalist prepping for an interview
- Economic buyer: Editor and production crew
- Champion: Candidate: reporter on the legislative beat
- Trigger moment: Candidate: an upcoming interview with a member of Congress, often tied to a live bill or news cycle
- Current workaround: Spend hours reading the member's legislative record in LexisNexis and Congress.gov, then manually piece together the issues they have cared about
- Why now: Candidate: legislative information volume is high and speed matters during live news windows
- Time to value: Candidate: within minutes of opening a bill
- Frequency: At least weekly for the target user
- Consequence of failure: Candidate: slow or shallow coverage, missed implications, and inaccurate interpretation under deadline
- Must-have or nice-to-have: Unproven; likely situational until urgency is validated
- Why AI step-change: AI can summarize dense bills and analyze clauses faster than a reporter manually tracing the member's record across LexisNexis and Congress.gov
- Recommendation status: Keep the wedge, but differentiate on source-linked interview prep rather than generic bill summary
- Last wedge score: 17/35 - dangerous

## ICP Hypotheses
### Primary
- Persona: Candidate: congressional reporter or legislative journalist
- Company type: Newsroom or policy publication covering federal legislation
- Team: Unknown
- Pain: Interview prep on a member of Congress is slow because the reporter has to manually reconstruct the member's legislative record and issue history under time pressure
- Buyer: Editor and production crew
- Champion: Candidate: beat reporter
- Budget owner: Candidate: editor and production leadership
- Urgency trigger: Candidate: an upcoming interview with a member of Congress, often around live legislative news

### Secondary
- Persona: Policy analyst
- Company type: Think tank, advocacy group, trade association, or government affairs team
- Why considered: Similar bill-comprehension pain, but likely different output, buying motion, and recurrence pattern

### Excluded
- ICPs we are explicitly not chasing: General public, students, and generic civics readers

## Trust Boundary
- Fully autonomous steps: Candidate: generate bill summaries and clause analysis for interview prep
- Human review steps: Journalist or editor spot-checks claims against linked raw bill text; final use still sits with the newsroom
- Human-only steps: Candidate: final editorial judgment, framing, and the actual interview
- Irreversible actions: Unknown
- Compliance / audit constraints: Unknown
- Error tolerance: Unknown
- Main trust blocker: AI output will not be trusted unless each summary or clause claim can be validated against linked raw bill text
- Recommended operating mode: AI-generated interview-prep brief with source-linked validation back to raw bill text and explicit human editorial accountability

## Evidence Log
- Interviews completed: 2 founder-reported conversations
- Strongest signal: In two founder-reported conversations, journalists/editors said interview prep can take about 4 hours each
- Weakest assumption: Whether source-linked validation is sufficient to make editors and journalists rely on the output regularly
- Pricing evidence: External buyer clues exist because LexisNexis packages research products for newsrooms and production teams, but no direct willingness-to-pay signal has been observed yet
- Retention evidence: None yet
- Top objections: External market signal says AI output is treated as unvetted unless it is source-linked and editor-reviewed

## Guided Discovery
- Current phase: Market reality check complete
- What we know: The strongest current candidate is a journalist preparing for an interview with a member of Congress who needs a fast brief on that member's legislative record and issue history, with the editor and production crew as likely buyers, source-linked validation as the key trust condition, and a crowded substitute market around legislative summaries.
- What still needs validation: Whether a source-linked interview-prep brief replaces enough of the 4-hour workflow to earn budget in a constrained newsroom, and whether journalists are a stronger first wedge than adjacent producer or policy workflows.
- Planned market checks: Validate direct willingness to pay, switching behavior from current tools, and whether the brief beats existing legislative products in real prep sessions.
- Current plan of attack: 1) prototype a source-linked interview-prep brief, 2) test whether it materially cuts prep time against the manual workflow, 3) validate who owns the budget and whether the buyer is actually editor, producer, or research leadership.

## Market Reality Check
- Claims tested: The workflow is real; the workflow is recurring enough to matter; substitutes are visible; newsroom/prod-team buyers are plausible; source validation is a real trust requirement
- Strongest external validation: Congressional reporting roles at CQ Roll Call explicitly require reading, summarizing, and analyzing bills and amendments on deadline, and newsroom research roles explicitly prepare pre-interview briefs for interviewers and producers
- Biggest external contradiction: Bill summaries and legislative tracking are already sold by incumbents like LexisNexis, FiscalNote/CQ, Quorum, Congress.gov, and LegiStorm, so a generic summary wedge is weak
- Visible substitutes: Congress.gov; LexisNexis Nexis, Nexis+ AI, and Newsdesk; FiscalNote/CQ; Quorum; LegiStorm
- Buyer / procurement clues: LexisNexis sells to journalists, producers, research teams, and newsrooms as a packaged solution; AP survey evidence suggests editors, managers, and executives are expected to govern AI adoption
- Trust / deployment clues: AP standards treat AI output as unvetted source material; market tools increasingly emphasize cited answers, source metadata, and verification workflows
- Open research questions: Which newsroom segment has the most acute pain; whether editors or producers will actually budget for a new workflow tool; and whether source-linked interview prep is differentiated enough from incumbent legislative products

## Current Diagnosis
- Primary bottleneck: The workflow is real, but the current product story is too close to incumbent legislative-summary tools for a budget-constrained newsroom. The wedge only works if it is clearly a source-linked interview-prep product that saves real time.
- Confidence: Medium-low
- Evidence: Two founder-reported interviews showed about 4 hours of prep pain each; external evidence shows newsroom interview-prep and congressional bill-analysis workflows are real, current substitute tooling is crowded, and newsroom AI standards require source-level verification and human accountability.
- If we're wrong: The stronger issue may still be segment choice rather than differentiation, meaning the better first buyer could be producers, researchers, or policy teams instead of beat reporters.
- Recommended next command: progress

## Company Scores
- Wedge Sharpness: 2
- ICP Focus: 1
- Value Recurrence: 2
- Trust Architecture: 3
- Evidence Quality: 1
- Learning Velocity: 2

## Score History
| Date | Wedge | ICP | Recurrence | Trust | Evidence | Velocity | Trigger |
|------|-------|-----|------------|-------|----------|----------|---------|
| 2026-03-26 | 2 | 1 | 2 | 3 | 1 | 1 | First-pass wedge assessment from founder narrative |
| 2026-03-26 | 2 | 1 | 2 | 3 | 1 | 2 | Added a concrete 7-day experiment to test whether a source-linked interview-prep brief actually replaces manual prep time |

## Active Experiments
1. Planned - Source-linked interview-prep brief test with 3-5 journalists or producers by 2026-04-02
2.
3.

## Decision Log
- 2026-03-26:
  - Decision: Start in guided kickoff mode instead of scoring aggressively
  - Why: Intake is partial and the wedge is still broad
  - Evidence: Founder narrative only
  - Revisit when: Primary user, trigger, workaround, and trust boundary are specified
- 2026-03-26:
  - Decision: Use legislative journalists as the active candidate wedge and keep policy analysts as the secondary branch
  - Why: The current story is more legible when tied to deadline-driven bill coverage
  - Evidence: Founder narrative and wedge compression only
  - Revisit when: ICP interviews clarify recurrence, buyer path, and whether policy analysts are stronger
- 2026-03-26:
  - Decision: Narrow the active journalist wedge to interview preparation rather than general bill coverage
  - Why: The founder clarified a sharper trigger and user context
  - Evidence: Founder stated the first user is a journalist prepping for an interview
  - Revisit when: The required output artifact and recurrence pattern are clear
- 2026-03-26:
  - Decision: Treat "legislative record and issues they cared about" as the current candidate output artifact
  - Why: The founder specified what the journalist wants in hand before the interview
  - Evidence: Founder stated the needed artifact is the interview subject's legislative record and issues of concern
  - Revisit when: It is clear whether the workflow is centered on a bill, a person, or both
- 2026-03-26:
  - Decision: Anchor the interview-prep wedge on members of Congress as the interview subject
  - Why: The founder clarified who the journalist is preparing to interview
  - Evidence: Founder stated the interview is usually with a member of Congress
  - Revisit when: The current workaround and frequency are known
- 2026-03-26:
  - Decision: Record the current workaround as manual prep in LexisNexis and Congress.gov
  - Why: The founder clarified the concrete toolchain and time cost in the workflow
  - Evidence: Founder stated journalists spend hours reading a member's legislative record on LexisNexis or Congress.gov
  - Revisit when: Frequency and willingness to switch are clearer
- 2026-03-26:
  - Decision: Treat recurrence as plausible enough to keep the journalist interview-prep wedge alive
  - Why: The founder stated this happens at least once a week for the target user
  - Evidence: Founder reported weekly frequency
  - Revisit when: Buyer and budget path are clearer
- 2026-03-26:
  - Decision: Treat editors and production crew as the likely initial buying center
  - Why: The founder identified who would actually pay in the newsroom
  - Evidence: Founder stated the editor and production crew would pay
  - Revisit when: Real budget ownership and procurement behavior are validated
- 2026-03-26:
  - Decision: Treat bill summary and clause analysis as the first AI-owned output in the workflow
  - Why: The founder specified what the AI should do first without human review
  - Evidence: Founder stated the AI should own the bill summary and clause analysis
  - Revisit when: Trust expectations and error tolerance are validated with users
- 2026-03-26:
  - Decision: Count the thesis as having at least minimal direct user signal
  - Why: The founder reported two relevant conversations
  - Evidence: Founder stated they have talked to two journalists or editors
  - Revisit when: Those conversations are backfilled with actual observations and objections
- 2026-03-26:
  - Decision: Treat prep time as the strongest observed pain signal so far
  - Why: Both conversations pointed to a substantial manual time cost
  - Evidence: Founder reported about 4 hours of interview prep per conversation
  - Revisit when: Trust, willingness to switch, and willingness to pay are clearer
- 2026-03-26:
  - Decision: Treat source-linked validation as the key trust requirement for the first version
  - Why: The founder reported that AI output would be trusted if it linked claims back to raw bill text
  - Evidence: Founder stated journalists would use the output as long as there was validation tied to the source bill text
  - Revisit when: More users confirm whether that condition is sufficient
- 2026-03-26:
  - Decision: Treat generic bill summary as an overcrowded feature, not the wedge
  - Why: External research showed multiple incumbents already sell legislative tracking, summaries, member data, and cited AI research workflows
  - Evidence: Congress.gov, LexisNexis, FiscalNote/CQ, Quorum, and LegiStorm all expose parts of the workflow; LexisNexis and Quorum already market AI summaries and cited answers
  - Revisit when: A prototype proves that source-linked interview prep is differentiated enough to replace current workflow steps

## Next Wedge Constraints
- What must remain true in the next wedge: The product should make dense congressional bill text faster to understand and more usable for action.
- What we refuse to repeat: Broad "for everyone who cares about Congress" positioning.

## Next 7 Days
- Put a source-linked interview-prep brief in front of 3-5 journalists or producers and measure time saved against current prep.
- Test whether users trust the brief enough to shape questions without rebuilding the research from scratch.
- Validate whether the actual buyer is editor, producer, or research leadership before assuming newsroom spend exists.
