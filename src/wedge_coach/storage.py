from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional

from wedge_coach.models import CoachConfig, CoachState, LogRecord, SessionTurn, now_iso


class Workspace:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.workspace_dir = self.root / ".wedge-coach"
        self.logs_dir = self.workspace_dir / "logs"
        self.sessions_dir = self.workspace_dir / "sessions"
        self.exports_dir = self.root / "exports"
        self.state_path = self.workspace_dir / "state.json"
        self.config_path = self.workspace_dir / "config.toml"
        self.import_report_path = self.workspace_dir / "import-report.json"

    def ensure(self) -> None:
        self.workspace_dir.mkdir(parents=True, exist_ok=True)
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        self.sessions_dir.mkdir(parents=True, exist_ok=True)
        if not self.state_path.exists():
            self.save_state(CoachState.empty())
        if not self.config_path.exists():
            self.save_config(CoachConfig())

    def load_state(self) -> CoachState:
        if not self.state_path.exists():
            return CoachState.empty()
        return CoachState.from_dict(_read_json(self.state_path))

    def save_state(self, state: CoachState) -> None:
        state.touch()
        _write_json(self.state_path, state.to_dict())

    def load_config(self) -> CoachConfig:
        if not self.config_path.exists():
            return CoachConfig()
        config = CoachConfig.from_dict(_read_toml(self.config_path))
        provider_name = os.environ.get("WEDGE_COACH_PROVIDER", "").strip()
        model = os.environ.get("WEDGE_COACH_MODEL", "").strip()
        scripted_responses = os.environ.get("WEDGE_COACH_SCRIPTED_RESPONSES", "").strip()
        if provider_name:
            config.provider_name = provider_name
        if model:
            config.model = model
        if scripted_responses:
            config.scripted_responses_path = scripted_responses
        return config

    def save_config(self, config: CoachConfig) -> None:
        _write_text(self.config_path, _render_toml(config.to_dict()))

    def append_log(self, record: LogRecord) -> None:
        path = self.logs_dir / ("%s.jsonl" % record.log_name)
        _append_jsonl(path, record.to_dict())

    def read_log(self, log_name: str, limit: Optional[int] = None) -> List[LogRecord]:
        path = self.logs_dir / ("%s.jsonl" % log_name)
        if not path.exists():
            return []
        records = [LogRecord.from_dict(item) for item in _read_jsonl(path)]
        if limit is None:
            return records
        return records[-limit:]

    def read_recent_logs(self, limit_per_log: int = 3) -> Dict[str, List[Dict[str, Any]]]:
        recent = {}
        for path in sorted(self.logs_dir.glob("*.jsonl")):
            log_name = path.stem
            recent[log_name] = [
                record.to_dict() for record in self.read_log(log_name, limit=limit_per_log)
            ]
        return recent

    def save_import_report(self, report: Dict[str, Any]) -> None:
        _write_json(self.import_report_path, report)

    def latest_session_path(self, command: str) -> Optional[Path]:
        candidates = sorted(self.sessions_dir.glob("*-%s.jsonl" % command))
        if not candidates:
            return None
        return candidates[-1]

    def ensure_session(self, command: str, new_session: bool = False) -> Path:
        if not new_session:
            latest = self.latest_session_path(command)
            if latest is not None:
                return latest
        filename = "%s-%s.jsonl" % (now_iso().replace(":", "").replace("-", ""), command)
        path = self.sessions_dir / filename
        path.touch()
        return path

    def append_session_turn(self, session_path: Path, role: str, content: str) -> None:
        _append_jsonl(
            session_path,
            SessionTurn(timestamp=now_iso(), role=role, content=content).to_dict(),
        )

    def read_session_turns(self, session_path: Path, limit: Optional[int] = None) -> List[SessionTurn]:
        if not session_path.exists():
            return []
        turns = [SessionTurn.from_dict(item) for item in _read_jsonl(session_path)]
        if limit is None:
            return turns
        return turns[-limit:]


def _read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("Expected JSON object at %s" % path)
    return data


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=str(path.parent), delete=False
    ) as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        temp_path = Path(handle.name)
    temp_path.replace(path)


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=str(path.parent), delete=False
    ) as handle:
        handle.write(text)
        temp_path = Path(handle.name)
    temp_path.replace(path)


def _append_jsonl(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True))
        handle.write("\n")


def _read_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def _read_toml(path: Path) -> Dict[str, Dict[str, Any]]:
    current_section = None
    data: Dict[str, Dict[str, Any]] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current_section = line[1:-1]
            data[current_section] = {}
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        target = data.setdefault(current_section or "root", {})
        target[key.strip()] = _parse_toml_value(value.strip())
    return data


def _parse_toml_value(value: str) -> Any:
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.lower() in ("true", "false"):
        return value.lower() == "true"
    try:
        return int(value)
    except ValueError:
        return value


def _render_toml(data: Dict[str, Dict[str, Any]]) -> str:
    lines: List[str] = []
    for section_name, section in data.items():
        if section_name != "root":
            lines.append("[%s]" % section_name)
        for key, value in section.items():
            lines.append("%s = %s" % (key, _toml_literal(value)))
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def _toml_literal(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    escaped = str(value).replace('"', '\\"')
    return '"%s"' % escaped
