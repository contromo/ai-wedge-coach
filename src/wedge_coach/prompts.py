from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from wedge_coach.models import CoachState, PromptBundle, SessionTurn

SHARED_SPEC_FILES = (
    "SKILL.md",
    "references/conversation-protocol.md",
    "references/state-system.md",
)

COMMAND_SPEC_FILES = {
    "kickoff": ("references/guided-flow.md", "references/commands/kickoff.md"),
    "wedge": ("references/rubrics.md", "references/commands/wedge.md"),
    "icp": ("references/commands/icp.md",),
    "trust": ("references/commands/trust.md",),
    "research": ("references/market-research.md", "references/commands/research.md"),
    "experiment": ("references/commands/experiment.md",),
}


def bundle_prompt(
    repo_root: Path,
    command: str,
    state: CoachState,
    recent_logs: Dict[str, List[Dict[str, object]]],
    recent_turns: List[SessionTurn],
) -> PromptBundle:
    spec_parts = []
    for relative_path in SHARED_SPEC_FILES + COMMAND_SPEC_FILES.get(command, ()):
        path = repo_root / relative_path
        spec_parts.append("=== %s ===\n%s" % (relative_path, path.read_text(encoding="utf-8")))

    state_json = json.dumps(state.to_dict(), indent=2, sort_keys=True)
    logs_json = json.dumps(recent_logs, indent=2, sort_keys=True)

    instructions = "\n\n".join(
        [
            "You are the standalone AI Agent Wedge Coach running inside a local CLI.",
            "Follow the bundled repo spec exactly. Preserve the one-question cadence, evidence discipline, and command-specific output contracts.",
            "Return valid JSON only. Do not wrap it in markdown.",
            "The JSON object must contain: assistant_message (string), state (full canonical state object), new_log_entries (array), and end_session (boolean).",
            "assistant_message must be the exact founder-facing response. It should be concise, direct, and structurally aligned with the active command spec.",
            "Carry forward existing state unless the user explicitly falsified it. Do not erase useful fields just because they were not mentioned in the latest turn.",
            "Do not invent observed facts. Keep observed facts, founder assertions, and model inferences separate.",
            "When ambiguity still matters, assistant_message should ask exactly one best next question and the state should preserve open questions rather than forcing diagnosis.",
            "When the command has enough evidence for diagnosis, include the command's required diagnosis structure inside assistant_message and update state accordingly.",
            "Use the current structured state below as canonical memory. Update it into a fresh full snapshot in the state field.",
            "Current structured state JSON:\n%s" % state_json,
            "Recent structured log excerpts:\n%s" % logs_json,
            "Bundled coaching spec:\n%s" % "\n\n".join(spec_parts),
        ]
    )

    input_items = []
    for turn in recent_turns:
        if not turn.role or not turn.content:
            continue
        input_items.append({"role": turn.role, "content": turn.content})
    return PromptBundle(instructions=instructions, input_items=input_items)


def repo_root_from_package() -> Path:
    return Path(__file__).resolve().parents[2]
