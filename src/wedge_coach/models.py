from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional

COMMAND_NAMES = (
    "kickoff",
    "wedge",
    "icp",
    "trust",
    "research",
    "experiment",
    "progress",
    "help",
)

COACHING_COMMANDS = (
    "kickoff",
    "wedge",
    "icp",
    "trust",
    "research",
    "experiment",
)

LOG_NAMES = (
    "interview_log",
    "objection_log",
    "experiment_log",
    "market_research_log",
    "wedge_graveyard",
)

EVIDENCE_BUCKETS = (
    "observed_fact",
    "founder_assertion",
    "model_inference",
)

ASSESSMENT_STATUSES = (
    "",
    "untested",
    "weak evidence",
    "validated",
    "strong",
)

CURRENT_THESIS_FIELDS = (
    "company",
    "product_one_liner",
    "current_workflow_wedge",
    "primary_user",
    "economic_buyer",
    "trigger",
    "current_workaround",
    "trust_boundary",
    "current_bottleneck",
)

CURRENT_THESIS_LABELS = {
    "company": "Company",
    "product_one_liner": "Product one-liner",
    "current_workflow_wedge": "Current workflow wedge",
    "primary_user": "Primary user",
    "economic_buyer": "Economic buyer",
    "trigger": "Trigger",
    "current_workaround": "Current workaround",
    "trust_boundary": "Trust boundary",
    "current_bottleneck": "Current bottleneck",
}

NEXT_MOVE_FIELDS = (
    "immediate_action",
    "why_this_now",
    "recommended_next_command",
)

NEXT_MOVE_LABELS = {
    "immediate_action": "Immediate action",
    "why_this_now": "Why this now",
    "recommended_next_command": "Recommended next command",
}

MARKET_REALITY_FIELDS = (
    "claims_tested",
    "strongest_external_validation",
    "biggest_external_contradiction",
    "visible_substitutes",
    "buyer_procurement_clues",
    "trust_deployment_clues",
)

MARKET_REALITY_LABELS = {
    "claims_tested": "Claims tested",
    "strongest_external_validation": "Strongest external validation",
    "biggest_external_contradiction": "Biggest external contradiction",
    "visible_substitutes": "Visible substitutes",
    "buyer_procurement_clues": "Buyer / procurement clues",
    "trust_deployment_clues": "Trust / deployment clues",
}

FOUNDER_HANDLING_FIELDS = (
    "current_archetype",
    "coaching_posture",
    "why_this_posture",
    "what_the_coach_should_do_next",
)

FOUNDER_HANDLING_LABELS = {
    "current_archetype": "Current archetype",
    "coaching_posture": "Coaching posture",
    "why_this_posture": "Why this posture",
    "what_the_coach_should_do_next": "What the coach should do next",
}

CURRENT_DIAGNOSIS_FIELDS = (
    "primary_bottleneck",
    "confidence",
    "observed_facts_used",
    "founder_assertions_carrying_load",
    "model_inferences_used",
    "if_we_re_wrong",
    "recommended_next_command",
)

CURRENT_DIAGNOSIS_LABELS = {
    "primary_bottleneck": "Primary bottleneck",
    "confidence": "Confidence",
    "observed_facts_used": "Observed facts used",
    "founder_assertions_carrying_load": "Founder assertions carrying load",
    "model_inferences_used": "Model inferences used",
    "if_we_re_wrong": "If we're wrong",
    "recommended_next_command": "Recommended next command",
}

ACCELERATOR_OPS_FIELDS = (
    "partner_briefing",
    "weekly_company_status_delta",
    "red_flag_memo",
    "needs_human_help_now",
    "triggers",
    "suggested_human_owner",
    "suggested_intervention",
    "by_when",
)

ACCELERATOR_OPS_LABELS = {
    "partner_briefing": "Partner briefing",
    "weekly_company_status_delta": "Weekly company status delta",
    "red_flag_memo": "Red-flag memo",
    "needs_human_help_now": "Needs human help now",
    "triggers": "Trigger(s)",
    "suggested_human_owner": "Suggested human owner",
    "suggested_intervention": "Suggested intervention",
    "by_when": "By when",
}

COHORT_COMPARISON_FIELDS = (
    "similar_failed_wedge_patterns",
    "repeated_objection_patterns",
    "relevant_trust_boundary_patterns",
    "segment_benchmark_read",
    "where_this_company_is_above_cohort",
    "where_this_company_is_below_cohort",
    "cohort_sample_caveat",
)

COHORT_COMPARISON_LABELS = {
    "similar_failed_wedge_patterns": "Similar failed wedge patterns",
    "repeated_objection_patterns": "Repeated objection patterns",
    "relevant_trust_boundary_patterns": "Relevant trust-boundary patterns",
    "segment_benchmark_read": "Segment benchmark read",
    "where_this_company_is_above_cohort": "Where this company is above cohort",
    "where_this_company_is_below_cohort": "Where this company is below cohort",
    "cohort_sample_caveat": "Cohort sample caveat",
}

ASSESSMENT_DIMENSIONS = (
    "Wedge Sharpness",
    "ICP Focus",
    "Value Recurrence",
    "Trust Architecture",
    "Evidence Quality",
    "Learning Velocity",
)


def now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def _text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _text_list(values: Any) -> List[str]:
    if not values:
        return []
    if isinstance(values, list):
        return [_text(item) for item in values if _text(item)]
    return [_text(values)] if _text(values) else []


def _section(raw: Any, keys: List[str]) -> Dict[str, str]:
    if not isinstance(raw, dict):
        raw = {}
    normalized = {}
    for key in keys:
        normalized[key] = _text(raw.get(key, ""))
    return normalized


def blank_section(keys: List[str]) -> Dict[str, str]:
    return dict((key, "") for key in keys)


@dataclass
class EvidenceItem:
    bucket: str = ""
    text: str = ""

    def __post_init__(self) -> None:
        self.bucket = _text(self.bucket)
        self.text = _text(self.text)
        if self.bucket and self.bucket not in EVIDENCE_BUCKETS:
            raise ValueError("Unsupported evidence bucket: %s" % self.bucket)

    @classmethod
    def from_dict(cls, raw: Any) -> "EvidenceItem":
        if not isinstance(raw, dict):
            raise ValueError("Evidence item must be an object.")
        return cls(bucket=raw.get("bucket", ""), text=raw.get("text", ""))

    def to_dict(self) -> Dict[str, str]:
        return {"bucket": self.bucket, "text": self.text}


@dataclass
class AssessmentEntry:
    dimension: str = ""
    status: str = ""
    evidence: str = ""

    def __post_init__(self) -> None:
        self.dimension = _text(self.dimension)
        self.status = _text(self.status)
        self.evidence = _text(self.evidence)
        if self.status and self.status not in ASSESSMENT_STATUSES:
            raise ValueError("Unsupported assessment status: %s" % self.status)

    @classmethod
    def from_dict(cls, raw: Any) -> "AssessmentEntry":
        if not isinstance(raw, dict):
            raise ValueError("Assessment entry must be an object.")
        return cls(
            dimension=raw.get("dimension", ""),
            status=raw.get("status", ""),
            evidence=raw.get("evidence", ""),
        )

    def to_dict(self) -> Dict[str, str]:
        return {
            "dimension": self.dimension,
            "status": self.status,
            "evidence": self.evidence,
        }


@dataclass
class AssessmentHistoryEntry:
    date: str = ""
    wedge: str = ""
    icp: str = ""
    recurrence: str = ""
    trust: str = ""
    evidence: str = ""
    velocity: str = ""
    trigger: str = ""

    @classmethod
    def from_dict(cls, raw: Any) -> "AssessmentHistoryEntry":
        if not isinstance(raw, dict):
            raise ValueError("Assessment history entry must be an object.")
        return cls(
            date=_text(raw.get("date", "")),
            wedge=_text(raw.get("wedge", "")),
            icp=_text(raw.get("icp", "")),
            recurrence=_text(raw.get("recurrence", "")),
            trust=_text(raw.get("trust", "")),
            evidence=_text(raw.get("evidence", "")),
            velocity=_text(raw.get("velocity", "")),
            trigger=_text(raw.get("trigger", "")),
        )

    def to_dict(self) -> Dict[str, str]:
        return {
            "date": self.date,
            "wedge": self.wedge,
            "icp": self.icp,
            "recurrence": self.recurrence,
            "trust": self.trust,
            "evidence": self.evidence,
            "velocity": self.velocity,
            "trigger": self.trigger,
        }


@dataclass
class ExperimentEntry:
    name: str = ""
    status: str = ""
    linked_dimension: str = ""
    hypothesis: str = ""
    falsifier: str = ""
    owner: str = ""
    deadline: str = ""
    success_threshold: str = ""
    failure_threshold: str = ""
    ambiguous_threshold: str = ""
    decision_rule: str = ""
    latest_result: str = ""
    next_decision: str = ""

    @classmethod
    def from_dict(cls, raw: Any) -> "ExperimentEntry":
        if not isinstance(raw, dict):
            raise ValueError("Experiment entry must be an object.")
        return cls(
            name=_text(raw.get("name", "")),
            status=_text(raw.get("status", "")),
            linked_dimension=_text(raw.get("linked_dimension", "")),
            hypothesis=_text(raw.get("hypothesis", "")),
            falsifier=_text(raw.get("falsifier", "")),
            owner=_text(raw.get("owner", "")),
            deadline=_text(raw.get("deadline", "")),
            success_threshold=_text(raw.get("success_threshold", "")),
            failure_threshold=_text(raw.get("failure_threshold", "")),
            ambiguous_threshold=_text(raw.get("ambiguous_threshold", "")),
            decision_rule=_text(raw.get("decision_rule", "")),
            latest_result=_text(raw.get("latest_result", "")),
            next_decision=_text(raw.get("next_decision", "")),
        )

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "status": self.status,
            "linked_dimension": self.linked_dimension,
            "hypothesis": self.hypothesis,
            "falsifier": self.falsifier,
            "owner": self.owner,
            "deadline": self.deadline,
            "success_threshold": self.success_threshold,
            "failure_threshold": self.failure_threshold,
            "ambiguous_threshold": self.ambiguous_threshold,
            "decision_rule": self.decision_rule,
            "latest_result": self.latest_result,
            "next_decision": self.next_decision,
        }


@dataclass
class DecisionEntry:
    date: str = ""
    source_experiment: str = ""
    decision: str = ""
    why: str = ""
    evidence: str = ""
    revisit_when: str = ""

    @classmethod
    def from_dict(cls, raw: Any) -> "DecisionEntry":
        if not isinstance(raw, dict):
            raise ValueError("Decision entry must be an object.")
        return cls(
            date=_text(raw.get("date", "")),
            source_experiment=_text(raw.get("source_experiment", "")),
            decision=_text(raw.get("decision", "")),
            why=_text(raw.get("why", "")),
            evidence=_text(raw.get("evidence", "")),
            revisit_when=_text(raw.get("revisit_when", "")),
        )

    def to_dict(self) -> Dict[str, str]:
        return {
            "date": self.date,
            "source_experiment": self.source_experiment,
            "decision": self.decision,
            "why": self.why,
            "evidence": self.evidence,
            "revisit_when": self.revisit_when,
        }


def default_assessments() -> List[AssessmentEntry]:
    return [AssessmentEntry(dimension=dimension) for dimension in ASSESSMENT_DIMENSIONS]


@dataclass
class CoachState:
    schema_version: int = 1
    updated_at: str = field(default_factory=now_iso)
    current_thesis: Dict[str, str] = field(
        default_factory=lambda: blank_section(list(CURRENT_THESIS_FIELDS))
    )
    open_questions: List[str] = field(default_factory=list)
    evidence_collected: List[EvidenceItem] = field(default_factory=list)
    next_move: Dict[str, str] = field(
        default_factory=lambda: blank_section(list(NEXT_MOVE_FIELDS))
    )
    market_reality: Dict[str, str] = field(
        default_factory=lambda: blank_section(list(MARKET_REALITY_FIELDS))
    )
    founder_handling: Dict[str, str] = field(
        default_factory=lambda: blank_section(list(FOUNDER_HANDLING_FIELDS))
    )
    current_diagnosis: Dict[str, str] = field(
        default_factory=lambda: blank_section(list(CURRENT_DIAGNOSIS_FIELDS))
    )
    company_assessments: List[AssessmentEntry] = field(default_factory=default_assessments)
    assessment_history: List[AssessmentHistoryEntry] = field(default_factory=list)
    active_experiments: List[ExperimentEntry] = field(default_factory=list)
    decision_log_summary: str = ""
    decision_log: List[DecisionEntry] = field(default_factory=list)
    accelerator_ops: Dict[str, str] = field(
        default_factory=lambda: blank_section(list(ACCELERATOR_OPS_FIELDS))
    )
    cohort_comparison: Dict[str, str] = field(
        default_factory=lambda: blank_section(list(COHORT_COMPARISON_FIELDS))
    )

    @classmethod
    def empty(cls) -> "CoachState":
        return cls()

    @classmethod
    def from_dict(cls, raw: Any) -> "CoachState":
        if not isinstance(raw, dict):
            raw = {}
        assessments = raw.get("company_assessments") or []
        if not assessments:
            assessments = [entry.to_dict() for entry in default_assessments()]
        return cls(
            schema_version=int(raw.get("schema_version", 1)),
            updated_at=_text(raw.get("updated_at", now_iso())),
            current_thesis=_section(raw.get("current_thesis"), list(CURRENT_THESIS_FIELDS)),
            open_questions=_text_list(raw.get("open_questions")),
            evidence_collected=[
                EvidenceItem.from_dict(item) for item in raw.get("evidence_collected", [])
            ],
            next_move=_section(raw.get("next_move"), list(NEXT_MOVE_FIELDS)),
            market_reality=_section(raw.get("market_reality"), list(MARKET_REALITY_FIELDS)),
            founder_handling=_section(
                raw.get("founder_handling"), list(FOUNDER_HANDLING_FIELDS)
            ),
            current_diagnosis=_section(
                raw.get("current_diagnosis"), list(CURRENT_DIAGNOSIS_FIELDS)
            ),
            company_assessments=[AssessmentEntry.from_dict(item) for item in assessments],
            assessment_history=[
                AssessmentHistoryEntry.from_dict(item)
                for item in raw.get("assessment_history", [])
            ],
            active_experiments=[
                ExperimentEntry.from_dict(item) for item in raw.get("active_experiments", [])
            ],
            decision_log_summary=_text(raw.get("decision_log_summary", "")),
            decision_log=[
                DecisionEntry.from_dict(item) for item in raw.get("decision_log", [])
            ],
            accelerator_ops=_section(
                raw.get("accelerator_ops"), list(ACCELERATOR_OPS_FIELDS)
            ),
            cohort_comparison=_section(
                raw.get("cohort_comparison"), list(COHORT_COMPARISON_FIELDS)
            ),
        )

    def to_dict(self) -> Dict[str, Any]:
        self.updated_at = _text(self.updated_at) or now_iso()
        return {
            "schema_version": self.schema_version,
            "updated_at": self.updated_at,
            "current_thesis": dict(self.current_thesis),
            "open_questions": list(self.open_questions),
            "evidence_collected": [item.to_dict() for item in self.evidence_collected],
            "next_move": dict(self.next_move),
            "market_reality": dict(self.market_reality),
            "founder_handling": dict(self.founder_handling),
            "current_diagnosis": dict(self.current_diagnosis),
            "company_assessments": [item.to_dict() for item in self.company_assessments],
            "assessment_history": [item.to_dict() for item in self.assessment_history],
            "active_experiments": [item.to_dict() for item in self.active_experiments],
            "decision_log_summary": self.decision_log_summary,
            "decision_log": [item.to_dict() for item in self.decision_log],
            "accelerator_ops": dict(self.accelerator_ops),
            "cohort_comparison": dict(self.cohort_comparison),
        }

    def touch(self) -> None:
        self.updated_at = now_iso()

    def has_material_state(self) -> bool:
        if any(value for value in self.current_thesis.values()):
            return True
        if self.open_questions or self.evidence_collected:
            return True
        if any(value for value in self.current_diagnosis.values()):
            return True
        return False


@dataclass
class LogRecord:
    log_name: str = ""
    title: str = ""
    created_at: str = ""
    fields: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, raw: Any) -> "LogRecord":
        if not isinstance(raw, dict):
            raise ValueError("Log record must be an object.")
        fields = raw.get("fields")
        if not isinstance(fields, dict):
            fields = {}
        return cls(
            log_name=_text(raw.get("log_name", "")),
            title=_text(raw.get("title", "")),
            created_at=_text(raw.get("created_at", "")),
            fields=dict((str(key), _text(value)) for key, value in fields.items()),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "log_name": self.log_name,
            "title": self.title,
            "created_at": self.created_at,
            "fields": dict(self.fields),
        }


@dataclass
class SessionTurn:
    timestamp: str = ""
    role: str = ""
    content: str = ""

    @classmethod
    def from_dict(cls, raw: Any) -> "SessionTurn":
        if not isinstance(raw, dict):
            raise ValueError("Session turn must be an object.")
        return cls(
            timestamp=_text(raw.get("timestamp", "")),
            role=_text(raw.get("role", "")),
            content=_text(raw.get("content", "")),
        )

    def to_dict(self) -> Dict[str, str]:
        return {
            "timestamp": self.timestamp,
            "role": self.role,
            "content": self.content,
        }


@dataclass
class CoachTurn:
    assistant_message: str
    state: CoachState
    new_log_entries: List[LogRecord] = field(default_factory=list)
    end_session: bool = False

    @classmethod
    def from_dict(cls, raw: Any) -> "CoachTurn":
        if not isinstance(raw, dict):
            raise ValueError("Coach turn must be an object.")
        assistant_message = _text(raw.get("assistant_message", ""))
        if not assistant_message:
            raise ValueError("Coach turn is missing assistant_message.")
        log_entries = [
            LogRecord.from_dict(item) for item in raw.get("new_log_entries", [])
        ]
        state = CoachState.from_dict(raw.get("state", {}))
        state.touch()
        return cls(
            assistant_message=assistant_message,
            state=state,
            new_log_entries=log_entries,
            end_session=bool(raw.get("end_session", False)),
        )


@dataclass
class CoachConfig:
    provider_name: str = "openai"
    model: str = "gpt-5.2"
    api_key_env: str = "OPENAI_API_KEY"
    max_output_tokens: int = 2000
    recent_turn_limit: int = 12
    scripted_responses_path: str = ""

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]) -> "CoachConfig":
        provider = raw.get("provider", {})
        session = raw.get("session", {})
        return cls(
            provider_name=_text(provider.get("name", "openai")) or "openai",
            model=_text(provider.get("model", "gpt-5.2")) or "gpt-5.2",
            api_key_env=_text(provider.get("api_key_env", "OPENAI_API_KEY"))
            or "OPENAI_API_KEY",
            max_output_tokens=int(provider.get("max_output_tokens", 2000) or 2000),
            recent_turn_limit=int(session.get("recent_turn_limit", 12) or 12),
            scripted_responses_path=_text(
                provider.get("scripted_responses_path", "")
            ),
        )

    def to_dict(self) -> Dict[str, Dict[str, Any]]:
        return {
            "provider": {
                "name": self.provider_name,
                "model": self.model,
                "api_key_env": self.api_key_env,
                "max_output_tokens": self.max_output_tokens,
                "scripted_responses_path": self.scripted_responses_path,
            },
            "session": {
                "recent_turn_limit": self.recent_turn_limit,
            },
        }


@dataclass
class PromptBundle:
    instructions: str
    input_items: List[Dict[str, str]]
