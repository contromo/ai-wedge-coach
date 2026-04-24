from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from wedge_coach.markdown_state import import_markdown_workspace
from wedge_coach.models import COACHING_COMMANDS, COMMAND_NAMES
from wedge_coach.prompts import bundle_prompt, repo_root_from_package
from wedge_coach.providers import ProviderError, create_provider
from wedge_coach.render import render_progress_markdown, render_report_html, render_report_markdown
from wedge_coach.storage import Workspace


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wedge-coach",
        description="Standalone CLI for the AI Agent Wedge Coach.",
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("help", help="Show CLI usage and commands.")

    init_parser = subparsers.add_parser("init", help="Initialize the structured workspace.")
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Rewrite default config even if the workspace already exists.",
    )

    import_parser = subparsers.add_parser(
        "import", help="Import existing markdown runtime files into the structured workspace."
    )
    import_parser.add_argument(
        "--from-markdown",
        dest="source",
        default=".",
        help="Path containing state.md or founder_state.md plus optional logs.",
    )

    progress_parser = subparsers.add_parser(
        "progress", help="Render the current structured progress summary."
    )
    progress_parser.add_argument(
        "--workspace",
        default=".",
        help="Workspace root. Defaults to the current directory.",
    )

    export_parser = subparsers.add_parser(
        "export", help="Export a shareable advisor/co-founder report."
    )
    export_parser.add_argument(
        "--format",
        choices=("html", "md"),
        default="html",
        help="Export format. Defaults to html.",
    )
    export_parser.add_argument(
        "--output",
        default="",
        help="Optional output path. Defaults to exports/wedge-coach-report.<ext>.",
    )

    for command_name in COACHING_COMMANDS:
        command_parser = subparsers.add_parser(
            command_name, help="Run the %s coaching command." % command_name
        )
        command_parser.add_argument(
            "--message",
            default="",
            help="Run one turn non-interactively with this founder message.",
        )
        command_parser.add_argument(
            "--new-session",
            action="store_true",
            help="Start a fresh session transcript for this command.",
        )

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    command = args.command or "help"

    if command == "help":
        print(_help_text())
        return 0
    if command == "init":
        return handle_init(Path.cwd(), force=args.force)
    if command == "import":
        return handle_import(Path.cwd(), Path(args.source))
    if command == "progress":
        return handle_progress(Path(args.workspace))
    if command == "export":
        return handle_export(Path.cwd(), export_format=args.format, output=args.output)
    if command in COACHING_COMMANDS:
        return handle_coaching_command(Path.cwd(), command, args.message, args.new_session)

    parser.print_help()
    return 1


def handle_init(root: Path, force: bool = False) -> int:
    workspace = Workspace(root)
    workspace.ensure()
    if force:
        workspace.save_config(workspace.load_config())
    print("Initialized structured workspace at %s" % workspace.workspace_dir)
    return 0


def handle_import(root: Path, source: Path) -> int:
    workspace = Workspace(root)
    workspace.ensure()
    state, log_records, report = import_markdown_workspace(source)
    if report["errors"]:
        workspace.save_import_report(report)
        print("Import failed:\n", file=sys.stderr)
        for item in report["errors"]:
            print("- %s" % item, file=sys.stderr)
        print(
            "\nSaved import report to %s" % workspace.import_report_path,
            file=sys.stderr,
        )
        return 1

    workspace.save_state(state)
    for record in log_records:
        workspace.append_log(record)
    workspace.save_import_report(report)
    print("Imported %s into %s" % (report["state_source"], workspace.workspace_dir))
    for log_name, count in sorted(report["imported_logs"].items()):
        print("- %s: %s entries" % (log_name, count))
    if report["warnings"]:
        print("\nWarnings:")
        for item in report["warnings"]:
            print("- %s" % item)
    print("\nImport report: %s" % workspace.import_report_path)
    return 0


def handle_progress(root: Path) -> int:
    workspace = Workspace(root)
    if not workspace.state_path.exists():
        print("No structured state yet.\n\nRun `wedge-coach kickoff` or `wedge-coach import --from-markdown .` first.")
        return 0
    state = workspace.load_state()
    print(render_progress_markdown(state))
    return 0


def handle_export(root: Path, export_format: str, output: str) -> int:
    workspace = Workspace(root)
    if not workspace.state_path.exists():
        print("No structured state to export. Run `wedge-coach kickoff` or import existing markdown state first.", file=sys.stderr)
        return 1
    state = workspace.load_state()
    logs = workspace.read_recent_logs(limit_per_log=5)
    generated_at = state.updated_at
    workspace.exports_dir.mkdir(parents=True, exist_ok=True)

    if output:
        output_path = Path(output)
        if not output_path.is_absolute():
            output_path = root / output_path
    else:
        output_path = workspace.exports_dir / (
            "wedge-coach-report.%s" % ("html" if export_format == "html" else "md")
        )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if export_format == "html":
        output_path.write_text(
            render_report_html(state, logs, generated_at),
            encoding="utf-8",
        )
    else:
        output_path.write_text(
            render_report_markdown(state, logs, generated_at),
            encoding="utf-8",
        )
    print("Exported %s report to %s" % (export_format, output_path))
    return 0


def handle_coaching_command(
    root: Path, command: str, message: str, new_session: bool
) -> int:
    workspace = Workspace(root)
    workspace.ensure()
    config = workspace.load_config()
    provider = create_provider(config)
    session_path = workspace.ensure_session(command, new_session=new_session)
    repo_root = repo_root_from_package()

    if message:
        return _run_single_turn(
            workspace=workspace,
            provider=provider,
            repo_root=repo_root,
            config=config,
            command=command,
            session_path=session_path,
            message=message,
        )

    print("Starting `%s`. Type /exit to finish.\n" % command)
    while True:
        try:
            founder_message = input("You: ").strip()
        except EOFError:
            print("")
            break
        if not founder_message or founder_message == "/exit":
            break
        exit_code = _run_single_turn(
            workspace=workspace,
            provider=provider,
            repo_root=repo_root,
            config=config,
            command=command,
            session_path=session_path,
            message=founder_message,
        )
        if exit_code != 0:
            return exit_code
    return 0


def _run_single_turn(
    workspace: Workspace,
    provider,
    repo_root: Path,
    config,
    command: str,
    session_path: Path,
    message: str,
) -> int:
    state = workspace.load_state()
    workspace.append_session_turn(session_path, "user", message)
    all_turns = workspace.read_session_turns(session_path)
    recent_turns = all_turns[-config.recent_turn_limit :]
    prompt = bundle_prompt(
        repo_root=repo_root,
        command=command,
        state=state,
        recent_logs=workspace.read_recent_logs(limit_per_log=3),
        recent_turns=recent_turns,
    )

    try:
        coach_turn = provider.generate_turn(command, prompt, all_turns, config)
    except ProviderError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    workspace.save_state(coach_turn.state)
    for record in coach_turn.new_log_entries:
        workspace.append_log(record)
    workspace.append_session_turn(session_path, "assistant", coach_turn.assistant_message)

    if sys.stdout.isatty():
        print("\nAssistant:\n%s\n" % coach_turn.assistant_message)
    else:
        print(coach_turn.assistant_message)
    return 0


def _help_text() -> str:
    lines = [
        "wedge-coach",
        "",
        "Structured workspace:",
        "- `wedge-coach init` - create `.wedge-coach/` with state.json, logs, sessions, and config.toml.",
        "- `wedge-coach import --from-markdown .` - import state.md or founder_state.md plus optional logs.",
        "- `wedge-coach export --format html` - generate a shareable report in `exports/`.",
        "",
        "Coaching commands:",
    ]
    for command in COACHING_COMMANDS:
        lines.append("- `wedge-coach %s`" % command)
    lines.extend(
        [
            "",
            "Shortcuts:",
            "- Add `--message \"...\"` to run one non-interactive turn.",
            "- Add `--new-session` to start a fresh transcript for a command.",
            "- `wedge-coach progress` prints the current structured summary without calling a model.",
            "",
            "Provider defaults:",
            "- Uses the bundled repo docs as the coaching spec.",
            "- Defaults to the OpenAI provider with `OPENAI_API_KEY` and model `gpt-5.2`.",
            "- For tests, set `WEDGE_COACH_PROVIDER=scripted` and `WEDGE_COACH_SCRIPTED_RESPONSES=/path/to/script.json`.",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
