from __future__ import annotations

from html import escape
from typing import Dict, List

from wedge_coach.models import (
    ACCELERATOR_OPS_LABELS,
    ASSESSMENT_DIMENSIONS,
    COHORT_COMPARISON_LABELS,
    CURRENT_DIAGNOSIS_LABELS,
    CURRENT_THESIS_LABELS,
    CoachState,
    FOUNDER_HANDLING_LABELS,
    MARKET_REALITY_LABELS,
    NEXT_MOVE_LABELS,
)

STATUS_ORDER = {
    "": 0,
    "untested": 0,
    "weak evidence": 1,
    "validated": 2,
    "strong": 3,
}


def render_progress_markdown(state: CoachState) -> str:
    if not state.has_material_state():
        return "No structured state yet.\n\nRun `wedge-coach kickoff` or `wedge-coach import --from-markdown .` first.\n"

    assessments = {entry.dimension: entry for entry in state.company_assessments}
    weakest = sorted(
        state.company_assessments,
        key=lambda item: (STATUS_ORDER.get(item.status, 0), item.dimension),
    )[0]
    biggest_improvement = _biggest_improvement(state)
    recurrence = assessments.get("Value Recurrence")
    observed = [item.text for item in state.evidence_collected if item.bucket == "observed_fact"]
    assertions = [
        item.text for item in state.evidence_collected if item.bucket == "founder_assertion"
    ]
    inferences = [
        item.text for item in state.evidence_collected if item.bucket == "model_inference"
    ]

    lines: List[str] = []
    lines.extend(["## Current Thesis"])
    lines.append("- Best current wedge: %s" % _value(state.current_thesis["current_workflow_wedge"]))
    lines.append("- Primary user: %s" % _value(state.current_thesis["primary_user"]))
    lines.append("- Economic buyer: %s" % _value(state.current_thesis["economic_buyer"]))
    lines.append("- Trust boundary: %s" % _value(state.current_thesis["trust_boundary"]))
    lines.append("- Current bottleneck: %s" % _value(state.current_thesis["current_bottleneck"]))
    lines.append("")
    lines.extend(["## Open Questions"])
    lines.append(
        "- Most important unresolved question: %s"
        % _value(state.open_questions[0] if state.open_questions else "")
    )
    lines.append(
        "- Second unresolved question: %s"
        % _value(state.open_questions[1] if len(state.open_questions) > 1 else "")
    )
    lines.append("")
    lines.extend(["## Evidence Collected"])
    lines.append("- Observed fact: %s" % _value(observed[0] if observed else ""))
    lines.append("- Founder assertion: %s" % _value(assertions[0] if assertions else ""))
    lines.append("- Model inference: %s" % _value(inferences[0] if inferences else ""))
    lines.append("")
    lines.extend(["## Progress Read"])
    lines.append("- Biggest improvement: %s" % _value(biggest_improvement))
    lines.append(
        "- Biggest unresolved drag: %s"
        % _value("%s (%s)" % (weakest.dimension, weakest.status or "untested"))
    )
    lines.append(
        "- Value recurrence read: %s"
        % _value(
            "%s%s"
            % (
                recurrence.status or "untested",
                (" | Evidence: %s" % recurrence.evidence) if recurrence and recurrence.evidence else "",
            )
            if recurrence
            else ""
        )
    )
    lines.append("")
    lines.extend(["## Pattern Read"])
    lines.append(
        "- Repeated pathology: %s"
        % _value(state.cohort_comparison.get("repeated_objection_patterns", ""))
    )
    lines.append(
        "- Current best thesis: %s"
        % _value(state.current_thesis.get("current_workflow_wedge", ""))
    )
    lines.append("")
    lines.extend(["## Founder Handling"])
    lines.append(
        "- Primary archetype: %s" % _value(state.founder_handling.get("current_archetype", ""))
    )
    lines.append(
        "- Coaching posture: %s" % _value(state.founder_handling.get("coaching_posture", ""))
    )
    lines.append(
        "- Why this posture now: %s"
        % _value(state.founder_handling.get("why_this_posture", ""))
    )
    lines.append(
        "- What the coach should do next: %s"
        % _value(state.founder_handling.get("what_the_coach_should_do_next", ""))
    )
    lines.append("")
    lines.extend(["## Evidence Classification"])
    lines.append("- Observed facts: %s" % _value("; ".join(observed[:3])))
    lines.append("- Founder assertions: %s" % _value("; ".join(assertions[:3])))
    lines.append("- Model inferences: %s" % _value("; ".join(inferences[:3])))
    lines.append("")
    lines.extend(["## Market Reality"])
    lines.append(
        "- Strongest external confirmation: %s"
        % _value(state.market_reality.get("strongest_external_validation", ""))
    )
    lines.append(
        "- Biggest external contradiction: %s"
        % _value(state.market_reality.get("biggest_external_contradiction", ""))
    )
    lines.append(
        "- What still needs validation: %s"
        % _value("; ".join(state.open_questions[:3]))
    )
    lines.append("")
    lines.extend(["## Cohort Memory"])
    lines.append(
        "- Similar failed wedge pattern: %s"
        % _value(state.cohort_comparison.get("similar_failed_wedge_patterns", ""))
    )
    lines.append(
        "- Repeated objection pattern: %s"
        % _value(state.cohort_comparison.get("repeated_objection_patterns", ""))
    )
    lines.append(
        "- Relevant trust-boundary pattern: %s"
        % _value(state.cohort_comparison.get("relevant_trust_boundary_patterns", ""))
    )
    lines.append(
        "- Segment benchmark: %s"
        % _value(state.cohort_comparison.get("segment_benchmark_read", ""))
    )
    lines.append(
        "- Where this company is above cohort: %s"
        % _value(state.cohort_comparison.get("where_this_company_is_above_cohort", ""))
    )
    lines.append(
        "- Where this company is below cohort: %s"
        % _value(state.cohort_comparison.get("where_this_company_is_below_cohort", ""))
    )
    lines.append(
        "- Cohort sample caveat: %s"
        % _value(state.cohort_comparison.get("cohort_sample_caveat", ""))
    )
    lines.append("")
    lines.extend(["## Partner Briefing"])
    lines.append("- Company in one line: %s" % _value(state.current_thesis.get("product_one_liner", "")))
    lines.append(
        "- What matters this week: %s"
        % _value(state.next_move.get("immediate_action", ""))
    )
    lines.append(
        "- Primary bottleneck for partners: %s"
        % _value(state.current_diagnosis.get("primary_bottleneck", ""))
    )
    lines.append(
        "- Best current thesis: %s"
        % _value(state.current_thesis.get("current_workflow_wedge", ""))
    )
    lines.append(
        "- Recommended partner action: %s"
        % _value(state.accelerator_ops.get("suggested_intervention", ""))
    )
    lines.append("")
    lines.extend(["## Weekly Status Delta"])
    lines.append(
        "- New observed facts since last snapshot: %s"
        % _value("; ".join(observed[:2]))
    )
    lines.append(
        "- Thesis change since last snapshot: %s"
        % _value(state.accelerator_ops.get("weekly_company_status_delta", ""))
    )
    lines.append(
        "- Assessment changes since last snapshot: %s"
        % _value(biggest_improvement)
    )
    lines.append(
        "- Decision changes since last snapshot: %s"
        % _value(state.decision_log[0].decision if state.decision_log else "")
    )
    lines.append("")
    lines.extend(["## Red-Flag Memo"])
    red_flag = state.accelerator_ops.get("red_flag_memo", "")
    lines.append("- Status: %s" % ("active" if red_flag and red_flag.lower() != "none" else "none"))
    lines.append("- Primary red flag: %s" % _value(red_flag))
    lines.append(
        "- Why this matters: %s" % _value(state.current_diagnosis.get("primary_bottleneck", ""))
    )
    lines.append(
        "- Evidence: %s" % _value(state.current_diagnosis.get("observed_facts_used", ""))
    )
    lines.append(
        "- Immediate mitigation: %s"
        % _value(state.accelerator_ops.get("suggested_intervention", ""))
    )
    lines.append("")
    lines.extend(["## Needs Human Help Now"])
    needs_help = state.accelerator_ops.get("needs_human_help_now", "")
    lines.append("- Triggered: %s" % ("yes" if needs_help.lower() == "yes" else "no"))
    lines.append("- Trigger(s): %s" % _value(state.accelerator_ops.get("triggers", "")))
    lines.append(
        "- Suggested human owner: %s"
        % _value(state.accelerator_ops.get("suggested_human_owner", ""))
    )
    lines.append(
        "- Suggested intervention: %s"
        % _value(state.accelerator_ops.get("suggested_intervention", ""))
    )
    lines.append("- By when: %s" % _value(state.accelerator_ops.get("by_when", "")))
    lines.append("")
    lines.extend(["## Diagnosis"])
    lines.append(
        "- Primary bottleneck: %s" % _value(state.current_diagnosis.get("primary_bottleneck", ""))
    )
    lines.append("- Confidence: %s" % _value(state.current_diagnosis.get("confidence", "")))
    lines.append("- Evidence: %s" % _value(state.current_diagnosis.get("observed_facts_used", "")))
    lines.append("- If I'm wrong: %s" % _value(state.current_diagnosis.get("if_we_re_wrong", "")))
    lines.append("")
    lines.extend(["## Recommendation"])
    lines.append("- %s" % _value(state.next_move.get("why_this_now", "")))
    lines.append("")
    lines.extend(["## Next Move"])
    lines.append("- %s" % _value(state.next_move.get("immediate_action", "")))
    lines.append("")
    lines.append(
        "**Recommended next**: `%s` - %s"
        % (
            _value(state.next_move.get("recommended_next_command", "")),
            _value(state.next_move.get("why_this_now", "")),
        )
    )
    lines.append("")
    return "\n".join(lines)


def render_report_markdown(
    state: CoachState, logs: Dict[str, List[Dict[str, object]]], generated_at: str
) -> str:
    lines = [
        "# Wedge Coach Report",
        "",
        "Generated: %s" % generated_at,
        "",
        "## Current Thesis",
    ]
    lines.extend(_render_section_bullets(state.current_thesis, CURRENT_THESIS_LABELS))
    lines.extend(["", "## Current Diagnosis"])
    lines.extend(_render_section_bullets(state.current_diagnosis, CURRENT_DIAGNOSIS_LABELS))
    lines.extend(["", "## Company Assessments"])
    for entry in state.company_assessments:
        if not (entry.status or entry.evidence):
            continue
        lines.append(
            "- %s: %s%s"
            % (
                entry.dimension,
                _value(entry.status),
                (" | Evidence: %s" % entry.evidence) if entry.evidence else "",
            )
        )
    lines.extend(["", "## Evidence Collected"])
    for item in state.evidence_collected:
        lines.append("- %s: %s" % (_bucket_label(item.bucket), _value(item.text)))
    lines.extend(["", "## Open Questions"])
    for item in state.open_questions:
        lines.append("- %s" % item)
    lines.extend(["", "## Active Experiments"])
    for experiment in state.active_experiments:
        lines.append("### %s" % _value(experiment.name))
        lines.append("- Status: %s" % _value(experiment.status))
        lines.append("- Hypothesis: %s" % _value(experiment.hypothesis))
        lines.append("- Falsifier: %s" % _value(experiment.falsifier))
        lines.append("- Next decision: %s" % _value(experiment.next_decision))
        lines.append("")
    lines.extend(["## Next Move"])
    lines.extend(_render_section_bullets(state.next_move, NEXT_MOVE_LABELS))
    lines.extend(["", "## Recent Log Activity"])
    if not logs:
        lines.append("- No log activity recorded yet.")
    for log_name, items in sorted(logs.items()):
        if not items:
            continue
        lines.append("### %s" % log_name.replace("_", " ").title())
        for item in items[-3:]:
            lines.append(
                "- %s (%s)"
                % (_value(item.get("title", "")), _value(item.get("created_at", "")))
            )
    lines.append("")
    return "\n".join(lines)


def render_report_html(
    state: CoachState, logs: Dict[str, List[Dict[str, object]]], generated_at: str
) -> str:
    sections = []
    sections.append(_html_section("Current Thesis", state.current_thesis, CURRENT_THESIS_LABELS))
    sections.append(
        _html_section("Current Diagnosis", state.current_diagnosis, CURRENT_DIAGNOSIS_LABELS)
    )
    sections.append(_html_assessments(state))
    sections.append(_html_evidence(state))
    sections.append(_html_open_questions(state))
    sections.append(_html_experiments(state))
    sections.append(_html_section("Next Move", state.next_move, NEXT_MOVE_LABELS))
    sections.append(_html_logs(logs))
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Wedge Coach Report</title>
  <style>
    :root {{
      --bg: #f6f2e8;
      --card: #fffdf8;
      --ink: #13232f;
      --muted: #5d6b75;
      --accent: #a44200;
      --line: #d9c8b5;
    }}
    body {{
      margin: 0;
      font-family: Georgia, "Iowan Old Style", "Palatino Linotype", serif;
      background: linear-gradient(160deg, #f2ecdf 0%, #faf7ef 45%, #efe4cf 100%);
      color: var(--ink);
    }}
    main {{
      max-width: 960px;
      margin: 0 auto;
      padding: 48px 24px 72px;
    }}
    header {{
      margin-bottom: 28px;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: 2.5rem;
      letter-spacing: -0.03em;
    }}
    .subtitle {{
      color: var(--muted);
      font-size: 1rem;
    }}
    section {{
      background: rgba(255, 253, 248, 0.92);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 22px 22px 18px;
      margin-bottom: 18px;
      box-shadow: 0 16px 40px rgba(34, 24, 12, 0.06);
    }}
    h2 {{
      margin: 0 0 14px;
      font-size: 1.3rem;
      color: var(--accent);
    }}
    ul {{
      margin: 0;
      padding-left: 20px;
    }}
    li {{
      margin-bottom: 8px;
      line-height: 1.5;
    }}
    .label {{
      font-weight: 700;
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Wedge Coach Report</h1>
      <div class="subtitle">Generated {generated_at}</div>
    </header>
    {sections}
  </main>
</body>
</html>
""".format(
        generated_at=escape(generated_at),
        sections="\n".join(sections),
    )


def _render_section_bullets(section: Dict[str, str], labels: Dict[str, str]) -> List[str]:
    lines = []
    for key, label in labels.items():
        value = section.get(key, "")
        if not value:
            continue
        lines.append("- %s: %s" % (label, value))
    if not lines:
        lines.append("- None yet.")
    return lines


def _bucket_label(bucket: str) -> str:
    mapping = {
        "observed_fact": "Observed fact",
        "founder_assertion": "Founder assertion",
        "model_inference": "Model inference",
    }
    return mapping.get(bucket, bucket.replace("_", " ").title())


def _html_section(title: str, section: Dict[str, str], labels: Dict[str, str]) -> str:
    items = []
    for key, label in labels.items():
        value = section.get(key, "")
        if not value:
            continue
        items.append("<li><span class='label'>%s:</span> %s</li>" % (escape(label), escape(value)))
    if not items:
        items.append("<li>None yet.</li>")
    return "<section><h2>%s</h2><ul>%s</ul></section>" % (escape(title), "".join(items))


def _html_assessments(state: CoachState) -> str:
    items = []
    for entry in state.company_assessments:
        if not (entry.status or entry.evidence):
            continue
        text = "%s" % _value(entry.status)
        if entry.evidence:
            text += " | Evidence: %s" % entry.evidence
        items.append("<li><span class='label'>%s:</span> %s</li>" % (escape(entry.dimension), escape(text)))
    if not items:
        items.append("<li>No assessments yet.</li>")
    return "<section><h2>Company Assessments</h2><ul>%s</ul></section>" % "".join(items)


def _html_evidence(state: CoachState) -> str:
    items = []
    for item in state.evidence_collected:
        items.append(
            "<li><span class='label'>%s:</span> %s</li>"
            % (escape(_bucket_label(item.bucket)), escape(item.text))
        )
    if not items:
        items.append("<li>No evidence captured yet.</li>")
    return "<section><h2>Evidence Collected</h2><ul>%s</ul></section>" % "".join(items)


def _html_open_questions(state: CoachState) -> str:
    items = ["<li>%s</li>" % escape(question) for question in state.open_questions]
    if not items:
        items.append("<li>No open questions captured yet.</li>")
    return "<section><h2>Open Questions</h2><ul>%s</ul></section>" % "".join(items)


def _html_experiments(state: CoachState) -> str:
    items = []
    for experiment in state.active_experiments:
        items.append(
            "<li><span class='label'>%s:</span> %s</li>"
            % (
                escape(_value(experiment.name)),
                escape(
                    "Status: %s | Hypothesis: %s | Next decision: %s"
                    % (
                        _value(experiment.status),
                        _value(experiment.hypothesis),
                        _value(experiment.next_decision),
                    )
                ),
            )
        )
    if not items:
        items.append("<li>No active experiments yet.</li>")
    return "<section><h2>Active Experiments</h2><ul>%s</ul></section>" % "".join(items)


def _html_logs(logs: Dict[str, List[Dict[str, object]]]) -> str:
    items = []
    for log_name, entries in sorted(logs.items()):
        if not entries:
            continue
        for entry in entries[-3:]:
            items.append(
                "<li><span class='label'>%s:</span> %s (%s)</li>"
                % (
                    escape(log_name.replace("_", " ").title()),
                    escape(_value(entry.get("title", ""))),
                    escape(_value(entry.get("created_at", ""))),
                )
            )
    if not items:
        items.append("<li>No recent log activity.</li>")
    return "<section><h2>Recent Log Activity</h2><ul>%s</ul></section>" % "".join(items)


def _biggest_improvement(state: CoachState) -> str:
    if len(state.assessment_history) < 2:
        return state.assessment_history[0].trigger if state.assessment_history else "No prior assessment history yet."
    earlier = state.assessment_history[-2]
    later = state.assessment_history[-1]
    deltas = [
        ("Wedge Sharpness", STATUS_ORDER.get(later.wedge, 0) - STATUS_ORDER.get(earlier.wedge, 0), later.trigger),
        ("ICP Focus", STATUS_ORDER.get(later.icp, 0) - STATUS_ORDER.get(earlier.icp, 0), later.trigger),
        ("Value Recurrence", STATUS_ORDER.get(later.recurrence, 0) - STATUS_ORDER.get(earlier.recurrence, 0), later.trigger),
        ("Trust Architecture", STATUS_ORDER.get(later.trust, 0) - STATUS_ORDER.get(earlier.trust, 0), later.trigger),
        ("Evidence Quality", STATUS_ORDER.get(later.evidence, 0) - STATUS_ORDER.get(earlier.evidence, 0), later.trigger),
        ("Learning Velocity", STATUS_ORDER.get(later.velocity, 0) - STATUS_ORDER.get(earlier.velocity, 0), later.trigger),
    ]
    best = sorted(deltas, key=lambda item: item[1], reverse=True)[0]
    if best[1] <= 0:
        return "No positive assessment delta yet."
    return "%s improved after %s" % (best[0], best[2])


def _value(value: object) -> str:
    text = str(value).strip() if value is not None else ""
    return text or "Unknown"
