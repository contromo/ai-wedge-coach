from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Tuple

from wedge_coach.models import (
    ACCELERATOR_OPS_LABELS,
    ASSESSMENT_DIMENSIONS,
    COHORT_COMPARISON_LABELS,
    CURRENT_DIAGNOSIS_LABELS,
    CURRENT_THESIS_LABELS,
    CoachState,
    DecisionEntry,
    EvidenceItem,
    ExperimentEntry,
    FOUNDER_HANDLING_LABELS,
    LogRecord,
    MARKET_REALITY_LABELS,
    NEXT_MOVE_LABELS,
    AssessmentEntry,
    AssessmentHistoryEntry,
)


def import_markdown_workspace(source_root: Path) -> Tuple[CoachState, List[LogRecord], Dict[str, object]]:
    source_root = source_root.resolve()
    warnings: List[str] = []
    errors: List[str] = []
    imported_logs: Dict[str, int] = {}

    state_path = None
    if (source_root / "state.md").exists():
        state_path = source_root / "state.md"
        state = _parse_current_state(state_path.read_text(encoding="utf-8"), warnings, errors)
    elif (source_root / "founder_state.md").exists():
        state_path = source_root / "founder_state.md"
        state = _parse_legacy_founder_state(
            state_path.read_text(encoding="utf-8"), warnings, errors
        )
    else:
        raise FileNotFoundError("No state.md or founder_state.md found in %s" % source_root)

    log_records: List[LogRecord] = []
    for log_name in (
        "interview_log",
        "objection_log",
        "experiment_log",
        "market_research_log",
        "wedge_graveyard",
    ):
        markdown_path = source_root / ("%s.md" % log_name)
        if not markdown_path.exists():
            imported_logs[log_name] = 0
            continue
        entries = _parse_markdown_log(markdown_path, log_name)
        imported_logs[log_name] = len(entries)
        log_records.extend(entries)

    report = {
        "source_root": str(source_root),
        "state_source": state_path.name if state_path else "",
        "warnings": warnings,
        "errors": errors,
        "imported_logs": imported_logs,
    }
    return state, log_records, report


def _parse_current_state(text: str, warnings: List[str], errors: List[str]) -> CoachState:
    sections = _split_h2_sections(text)
    state = CoachState.empty()

    thesis = _parse_bullet_map(sections.get("Current Thesis", []))
    state.current_thesis = _mapped_section(
        thesis,
        CURRENT_THESIS_LABELS,
        required=("Product one-liner", "Current workflow wedge", "Primary user"),
        warnings=warnings,
        errors=errors,
        section_name="Current Thesis",
    )

    state.open_questions = _parse_bullet_list(sections.get("Open Questions", []))
    state.evidence_collected = _parse_evidence(sections.get("Evidence Collected", []))
    state.next_move = _mapped_section(
        _parse_bullet_map(sections.get("Next Move", [])),
        NEXT_MOVE_LABELS,
        warnings=warnings,
        errors=errors,
        section_name="Next Move",
    )
    state.market_reality = _mapped_section(
        _parse_bullet_map(sections.get("Market Reality", [])),
        MARKET_REALITY_LABELS,
        warnings=warnings,
        errors=errors,
        section_name="Market Reality",
    )
    state.founder_handling = _mapped_section(
        _parse_bullet_map(sections.get("Founder Handling", [])),
        FOUNDER_HANDLING_LABELS,
        warnings=warnings,
        errors=errors,
        section_name="Founder Handling",
    )
    state.current_diagnosis = _mapped_section(
        _parse_bullet_map(sections.get("Current Diagnosis", [])),
        CURRENT_DIAGNOSIS_LABELS,
        warnings=warnings,
        errors=errors,
        section_name="Current Diagnosis",
    )
    state.company_assessments = _parse_assessments(sections.get("Company Assessments", []))
    state.assessment_history = _parse_assessment_history(
        sections.get("Assessment History", [])
    )
    state.active_experiments = _parse_experiments(sections.get("Active Experiments", []))
    state.decision_log_summary, state.decision_log = _parse_decision_log(
        sections.get("Decision Log", [])
    )
    state.accelerator_ops = _mapped_section(
        _parse_bullet_map(sections.get("Accelerator Ops", [])),
        ACCELERATOR_OPS_LABELS,
        warnings=warnings,
        errors=errors,
        section_name="Accelerator Ops",
    )
    state.cohort_comparison = _mapped_section(
        _parse_bullet_map(sections.get("Cohort Comparison", [])),
        COHORT_COMPARISON_LABELS,
        warnings=warnings,
        errors=errors,
        section_name="Cohort Comparison",
    )
    return state


def _parse_legacy_founder_state(text: str, warnings: List[str], errors: List[str]) -> CoachState:
    warnings.append(
        "Importing founder_state.md uses a compatibility mapping and may be lossy."
    )
    sections = _split_h2_sections(text)
    state = CoachState.empty()

    company = _parse_bullet_map(sections.get("Company Snapshot", []))
    wedge = _parse_bullet_map(sections.get("Current Primary Wedge", []))
    diagnosis = _parse_bullet_map(sections.get("Current Diagnosis", []))
    market = _parse_bullet_map(sections.get("Market Reality Check", []))
    discovery = _parse_bullet_map(sections.get("Guided Discovery", []))
    evidence = _parse_bullet_map(sections.get("Evidence Log", []))

    state.current_thesis["company"] = company.get("Company", "")
    state.current_thesis["product_one_liner"] = company.get("Product one-liner", "")
    state.current_thesis["current_workflow_wedge"] = wedge.get("Workflow", "")
    state.current_thesis["primary_user"] = wedge.get("Primary user", "")
    state.current_thesis["economic_buyer"] = wedge.get("Economic buyer", "")
    state.current_thesis["trigger"] = wedge.get("Trigger moment", "")
    state.current_thesis["current_workaround"] = wedge.get("Current workaround", "")
    state.current_thesis["trust_boundary"] = _parse_bullet_map(
        sections.get("Trust Boundary", [])
    ).get("Recommended operating mode", "")
    state.current_thesis["current_bottleneck"] = diagnosis.get("Primary bottleneck", "")

    for key in ("What still needs validation", "Open research questions"):
        value = discovery.get(key, "") or market.get(key, "")
        if value:
            state.open_questions.extend(_split_sentences(value))

    strongest_signal = evidence.get("Strongest signal", "")
    if strongest_signal:
        state.evidence_collected.append(
            EvidenceItem(bucket="observed_fact", text=strongest_signal)
        )
    weakest_assumption = evidence.get("Weakest assumption", "")
    if weakest_assumption:
        state.evidence_collected.append(
            EvidenceItem(bucket="founder_assertion", text=weakest_assumption)
        )
    if diagnosis.get("Evidence", ""):
        state.evidence_collected.append(
            EvidenceItem(bucket="model_inference", text=diagnosis.get("Evidence", ""))
        )

    next_7_days = _parse_numbered_list(sections.get("Next 7 Days", []))
    if next_7_days:
        state.next_move["immediate_action"] = next_7_days[0]
    state.next_move["why_this_now"] = diagnosis.get("Primary bottleneck", "")
    state.next_move["recommended_next_command"] = diagnosis.get(
        "Recommended next command", ""
    )

    state.market_reality["claims_tested"] = market.get("Claims tested", "")
    state.market_reality["strongest_external_validation"] = market.get(
        "Strongest external validation", ""
    )
    state.market_reality["biggest_external_contradiction"] = market.get(
        "Biggest external contradiction", ""
    )
    state.market_reality["visible_substitutes"] = market.get("Visible substitutes", "")
    state.market_reality["buyer_procurement_clues"] = market.get(
        "Buyer / procurement clues", ""
    )
    state.market_reality["trust_deployment_clues"] = market.get(
        "Trust / deployment clues", ""
    )

    state.current_diagnosis["primary_bottleneck"] = diagnosis.get(
        "Primary bottleneck", ""
    )
    state.current_diagnosis["confidence"] = diagnosis.get("Confidence", "")
    state.current_diagnosis["observed_facts_used"] = evidence.get(
        "Strongest signal", ""
    )
    state.current_diagnosis["founder_assertions_carrying_load"] = evidence.get(
        "Weakest assumption", ""
    )
    state.current_diagnosis["model_inferences_used"] = diagnosis.get("Evidence", "")
    state.current_diagnosis["if_we_re_wrong"] = diagnosis.get("If we're wrong", "")
    state.current_diagnosis["recommended_next_command"] = diagnosis.get(
        "Recommended next command", ""
    )

    state.company_assessments = _parse_legacy_scores(sections.get("Company Scores", []))
    state.assessment_history = _parse_legacy_assessment_history(
        sections.get("Score History", [])
    )
    return state


def _parse_markdown_log(path: Path, log_name: str) -> List[LogRecord]:
    sections = _split_h2_sections(path.read_text(encoding="utf-8"))
    entries = []
    for heading, lines in sections.items():
        date, title = _parse_log_heading(heading)
        fields = _parse_bullet_map(lines)
        entries.append(
            LogRecord(
                log_name=log_name,
                title=title,
                created_at=date,
                fields=fields,
            )
        )
    return entries


def _split_h2_sections(text: str) -> Dict[str, List[str]]:
    sections: Dict[str, List[str]] = {}
    current = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip("\n")
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line.rstrip())
    return sections


def _parse_bullet_map(lines: List[str]) -> Dict[str, str]:
    data: Dict[str, str] = {}
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        item = stripped[2:]
        if ":" not in item:
            continue
        key, value = item.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def _parse_bullet_list(lines: List[str]) -> List[str]:
    items = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- "):
            value = stripped[2:].strip()
            if value:
                items.append(value)
    return items


def _parse_numbered_list(lines: List[str]) -> List[str]:
    items = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^\d+\.\s+", stripped):
            items.append(re.sub(r"^\d+\.\s+", "", stripped))
    return items


def _mapped_section(
    raw_map: Dict[str, str],
    labels: Dict[str, str],
    warnings: List[str],
    errors: List[str],
    section_name: str,
    required: Tuple[str, ...] = (),
) -> Dict[str, str]:
    reverse = dict((label, key) for key, label in labels.items())
    mapped = dict((key, "") for key in labels.keys())
    for label, value in raw_map.items():
        key = reverse.get(label)
        if key is None:
            warnings.append("%s contains an unmapped field: %s" % (section_name, label))
            continue
        mapped[key] = value
    for label in required:
        if not raw_map.get(label, "").strip():
            errors.append("%s is missing required field: %s" % (section_name, label))
    return mapped


def _parse_evidence(lines: List[str]) -> List[EvidenceItem]:
    items = []
    bucket_map = {
        "Observed fact": "observed_fact",
        "Founder assertion": "founder_assertion",
        "Model inference": "model_inference",
    }
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        text = stripped[2:]
        if ":" not in text:
            continue
        label, value = text.split(":", 1)
        bucket = bucket_map.get(label.strip())
        if bucket:
            items.append(EvidenceItem(bucket=bucket, text=value.strip()))
    return items


def _parse_assessments(lines: List[str]) -> List[AssessmentEntry]:
    results = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        body = stripped[2:]
        if ":" not in body:
            continue
        label, remainder = body.split(":", 1)
        status, evidence = remainder.strip(), ""
        if "| Evidence:" in remainder:
            status, evidence = remainder.split("| Evidence:", 1)
        results.append(
            AssessmentEntry(
                dimension=label.strip(),
                status=status.strip(),
                evidence=evidence.strip(),
            )
        )
    if not results:
        return [AssessmentEntry(dimension=dimension) for dimension in ASSESSMENT_DIMENSIONS]
    return results


def _parse_assessment_history(lines: List[str]) -> List[AssessmentHistoryEntry]:
    rows = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        columns = [column.strip() for column in stripped.strip("|").split("|")]
        if len(columns) != 8:
            continue
        if columns[0] in ("Date", "------"):
            continue
        rows.append(
            AssessmentHistoryEntry(
                date=columns[0],
                wedge=columns[1],
                icp=columns[2],
                recurrence=columns[3],
                trust=columns[4],
                evidence=columns[5],
                velocity=columns[6],
                trigger=columns[7],
            )
        )
    return rows


def _parse_experiments(lines: List[str]) -> List[ExperimentEntry]:
    experiments: List[ExperimentEntry] = []
    current: Dict[str, str] = {}
    label_map = {
        "Name": "name",
        "Status": "status",
        "Linked dimension": "linked_dimension",
        "Hypothesis": "hypothesis",
        "Falsifier": "falsifier",
        "Owner": "owner",
        "Deadline": "deadline",
        "Success threshold": "success_threshold",
        "Failure threshold": "failure_threshold",
        "Ambiguous threshold": "ambiguous_threshold",
        "Decision rule": "decision_rule",
        "Latest result": "latest_result",
        "Next decision": "next_decision",
    }
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        item = stripped[2:]
        if ":" not in item:
            continue
        label, value = item.split(":", 1)
        field_name = label_map.get(label.strip())
        if not field_name:
            continue
        if field_name == "name" and current:
            experiments.append(ExperimentEntry.from_dict(current))
            current = {}
        current[field_name] = value.strip()
    if current:
        experiments.append(ExperimentEntry.from_dict(current))
    return experiments


def _parse_decision_log(lines: List[str]) -> Tuple[str, List[DecisionEntry]]:
    summary = ""
    decisions: List[DecisionEntry] = []
    current = None
    for line in lines:
        if line.startswith("- Older decisions summary:"):
            summary = line.split(":", 1)[1].strip()
            continue
        if line.startswith("- ") and line.endswith(":"):
            date = line[2:-1].strip()
            current = {"date": date}
            decisions.append(DecisionEntry.from_dict(current))
            continue
        if line.startswith("  - ") and decisions:
            key, value = line[4:].split(":", 1)
            entry = decisions[-1]
            normalized_key = key.strip().lower().replace(" ", "_")
            if hasattr(entry, normalized_key):
                setattr(entry, normalized_key, value.strip())
    return summary, decisions


def _parse_legacy_scores(lines: List[str]) -> List[AssessmentEntry]:
    mapping = []
    qualitative_map = {
        "1": "weak evidence",
        "2": "weak evidence",
        "3": "validated",
        "4": "strong",
        "5": "strong",
    }
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        key, value = stripped[2:].split(":", 1)
        mapping.append(
            AssessmentEntry(
                dimension=key.strip(),
                status=qualitative_map.get(value.strip(), "weak evidence"),
                evidence="Imported from legacy numeric score.",
            )
        )
    return mapping or [AssessmentEntry(dimension=dimension) for dimension in ASSESSMENT_DIMENSIONS]


def _parse_legacy_assessment_history(lines: List[str]) -> List[AssessmentHistoryEntry]:
    qualitative_map = {
        "1": "weak evidence",
        "2": "weak evidence",
        "3": "validated",
        "4": "strong",
        "5": "strong",
    }
    rows = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        columns = [column.strip() for column in stripped.strip("|").split("|")]
        if len(columns) != 8 or columns[0] == "Date":
            continue
        rows.append(
            AssessmentHistoryEntry(
                date=columns[0],
                wedge=qualitative_map.get(columns[1], columns[1]),
                icp=qualitative_map.get(columns[2], columns[2]),
                recurrence=qualitative_map.get(columns[3], columns[3]),
                trust=qualitative_map.get(columns[4], columns[4]),
                evidence=qualitative_map.get(columns[5], columns[5]),
                velocity=qualitative_map.get(columns[6], columns[6]),
                trigger=columns[7],
            )
        )
    return rows


def _parse_log_heading(heading: str) -> Tuple[str, str]:
    match = re.match(r"^(\d{4}-\d{2}-\d{2})\s*-\s*(.+)$", heading)
    if match:
        return match.group(1), match.group(2).strip()
    return "", heading.strip()


def _split_sentences(value: str) -> List[str]:
    return [piece.strip() for piece in re.split(r";\s+|\.\s+", value) if piece.strip()]
