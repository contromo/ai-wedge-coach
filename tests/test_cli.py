from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from wedge_coach.markdown_state import import_markdown_workspace
from wedge_coach.models import CoachState, EvidenceItem
from wedge_coach.storage import Workspace

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"


def _run_cli(cwd: Path, *args: str, env: dict = None) -> subprocess.CompletedProcess:
    merged_env = os.environ.copy()
    merged_env["PYTHONPATH"] = str(SRC_ROOT)
    if env:
        merged_env.update(env)
    return subprocess.run(
        [sys.executable, "-m", "wedge_coach", *args],
        cwd=str(cwd),
        env=merged_env,
        text=True,
        capture_output=True,
        check=False,
    )


def _build_state_payload() -> dict:
    state = CoachState.empty()
    state.current_thesis["company"] = "Acme AI"
    state.current_thesis["product_one_liner"] = (
        "AI-generated customer onboarding briefs for B2B finance teams."
    )
    state.current_thesis["current_workflow_wedge"] = (
        "Prepare a source-linked onboarding brief for a finance ops manager before a customer handoff."
    )
    state.current_thesis["primary_user"] = "Finance ops manager"
    state.current_thesis["economic_buyer"] = "Head of finance operations"
    state.current_thesis["trigger"] = "New enterprise customer handoff"
    state.current_thesis["current_workaround"] = "Manual note stitching across CRM and spreadsheets"
    state.current_thesis["trust_boundary"] = "AI drafts the brief; manager reviews before sending"
    state.current_thesis["current_bottleneck"] = "Buyer path is still inferred"
    state.open_questions = [
        "Will onboarding managers trust a source-linked draft enough to use it as the starting point?"
    ]
    state.evidence_collected = [
        EvidenceItem(bucket="observed_fact", text="Two onboarding leads said the handoff brief takes 90 minutes."),
        EvidenceItem(bucket="founder_assertion", text="Ops leadership will pay if time savings are obvious."),
        EvidenceItem(bucket="model_inference", text="The wedge survives only if the draft becomes the default starting artifact."),
    ]
    state.next_move["immediate_action"] = (
        "Test the source-linked brief with three onboarding managers this week."
    )
    state.next_move["why_this_now"] = "The buyer story is too thin to expand the wedge yet."
    state.next_move["recommended_next_command"] = "progress"
    state.current_diagnosis["primary_bottleneck"] = "The workflow is plausible, but the buyer path is still mostly assertion."
    state.current_diagnosis["confidence"] = "Medium-low"
    state.current_diagnosis["observed_facts_used"] = "Two onboarding leads described a 90-minute manual brief workflow."
    state.current_diagnosis["founder_assertions_carrying_load"] = "Ops leadership owns the budget."
    state.current_diagnosis["model_inferences_used"] = "Source-linked drafting is the surviving wedge."
    state.current_diagnosis["if_we_re_wrong"] = "The user may be strong but the true buyer could sit in customer success."
    state.current_diagnosis["recommended_next_command"] = "progress"
    state.company_assessments[0].status = "weak evidence"
    state.company_assessments[0].evidence = "Specific workflow exists but switching proof is thin."
    state.company_assessments[1].status = "weak evidence"
    state.company_assessments[1].evidence = "Buyer path is inferred."
    state.company_assessments[2].status = "validated"
    state.company_assessments[2].evidence = "Workflow recurs on each enterprise handoff."
    return state.to_dict()


class WorkspaceTests(unittest.TestCase):
    def test_state_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workspace = Workspace(root)
            workspace.ensure()

            state = workspace.load_state()
            state.current_thesis["company"] = "Round Trip Inc."
            state.open_questions.append("What is the buyer path?")
            workspace.save_state(state)

            loaded = workspace.load_state()
            self.assertEqual(loaded.current_thesis["company"], "Round Trip Inc.")
            self.assertIn("What is the buyer path?", loaded.open_questions)

    def test_import_current_markdown_workspace(self) -> None:
        source = REPO_ROOT / "examples" / "cuibono"
        state, logs, report = import_markdown_workspace(source)
        self.assertEqual(state.current_thesis["company"], "Cui Bono")
        self.assertEqual(report["state_source"], "state.md")
        self.assertTrue(any(record.log_name == "interview_log" for record in logs))
        self.assertFalse(report["errors"])


class CliIntegrationTests(unittest.TestCase):
    def test_scripted_kickoff_progress_and_export(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script_path = root / "script.json"
            script = {
                "kickoff": [
                    {
                        "assistant_message": "## Kickoff Readback\n- What you're building: Source-linked onboarding briefs.\n\n**Recommended next**: `progress` - Review the imported thesis and run the first test.",
                        "state": _build_state_payload(),
                        "new_log_entries": [
                            {
                                "log_name": "experiment_log",
                                "title": "Source-linked onboarding brief test",
                                "created_at": "2026-03-31",
                                "fields": {
                                    "Status": "planned",
                                    "Owner": "Founder",
                                },
                            }
                        ],
                        "end_session": False,
                    }
                ]
            }
            script_path.write_text(json.dumps(script), encoding="utf-8")
            env = {
                "WEDGE_COACH_PROVIDER": "scripted",
                "WEDGE_COACH_SCRIPTED_RESPONSES": str(script_path),
            }

            result = _run_cli(root, "kickoff", "--message", "We draft onboarding briefs.", env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Kickoff Readback", result.stdout)

            progress = _run_cli(root, "progress")
            self.assertEqual(progress.returncode, 0, progress.stderr)
            self.assertIn("## Current Thesis", progress.stdout)
            self.assertIn("Finance ops manager", progress.stdout)

            export = _run_cli(root, "export", "--format", "html")
            self.assertEqual(export.returncode, 0, export.stderr)
            report_path = root / "exports" / "wedge-coach-report.html"
            self.assertTrue(report_path.exists())
            self.assertIn("Acme AI", report_path.read_text(encoding="utf-8"))

    def test_resume_session_uses_next_scripted_response(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script_path = root / "script.json"
            script = {
                "kickoff": [
                    {
                        "assistant_message": "First question?",
                        "state": CoachState.empty().to_dict(),
                        "new_log_entries": [],
                        "end_session": False,
                    },
                    {
                        "assistant_message": "Second question?",
                        "state": CoachState.empty().to_dict(),
                        "new_log_entries": [],
                        "end_session": False,
                    },
                ]
            }
            script_path.write_text(json.dumps(script), encoding="utf-8")
            env = {
                "WEDGE_COACH_PROVIDER": "scripted",
                "WEDGE_COACH_SCRIPTED_RESPONSES": str(script_path),
            }

            first = _run_cli(root, "kickoff", "--message", "Story one", env=env)
            second = _run_cli(root, "kickoff", "--message", "Story two", env=env)

            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertIn("First question?", first.stdout)
            self.assertIn("Second question?", second.stdout)

            session_files = list((root / ".wedge-coach" / "sessions").glob("*-kickoff.jsonl"))
            self.assertEqual(len(session_files), 1)
            transcript = session_files[0].read_text(encoding="utf-8")
            self.assertIn("Story one", transcript)
            self.assertIn("Story two", transcript)


if __name__ == "__main__":
    unittest.main()
