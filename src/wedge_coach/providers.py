from __future__ import annotations

import json
import os
from pathlib import Path
from typing import List

from wedge_coach.models import CoachConfig, CoachTurn, PromptBundle, SessionTurn


class ProviderError(RuntimeError):
    pass


class Provider:
    def generate_turn(
        self,
        command: str,
        prompt: PromptBundle,
        session_turns: List[SessionTurn],
        config: CoachConfig,
    ) -> CoachTurn:
        raise NotImplementedError


class OpenAIProvider(Provider):
    def generate_turn(
        self,
        command: str,
        prompt: PromptBundle,
        session_turns: List[SessionTurn],
        config: CoachConfig,
    ) -> CoachTurn:
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise ProviderError(
                "The openai package is not installed. Run `python3 -m pip install -e .` first."
            ) from exc

        api_key = os.environ.get(config.api_key_env, "").strip()
        if not api_key:
            raise ProviderError(
                "Missing %s. Export it before running coaching commands."
                % config.api_key_env
            )

        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model=config.model,
            instructions=prompt.instructions,
            input=prompt.input_items,
            text={"format": {"type": "json_object"}},
            max_output_tokens=config.max_output_tokens,
        )
        payload_text = getattr(response, "output_text", "")
        if not payload_text:
            raise ProviderError("OpenAI returned an empty response body.")
        try:
            payload = json.loads(payload_text)
        except json.JSONDecodeError as exc:
            raise ProviderError("OpenAI returned invalid JSON: %s" % exc) from exc
        return CoachTurn.from_dict(payload)


class ScriptedProvider(Provider):
    def generate_turn(
        self,
        command: str,
        prompt: PromptBundle,
        session_turns: List[SessionTurn],
        config: CoachConfig,
    ) -> CoachTurn:
        script_path = config.scripted_responses_path or os.environ.get(
            "WEDGE_COACH_SCRIPTED_RESPONSES", ""
        )
        if not script_path:
            raise ProviderError(
                "Scripted provider selected but no scripted response file was configured."
            )
        payload = json.loads(Path(script_path).read_text(encoding="utf-8"))
        command_responses = payload.get(command)
        if not isinstance(command_responses, list):
            raise ProviderError(
                "Scripted response file does not define a response list for %s." % command
            )
        assistant_turn_count = len(
            [turn for turn in session_turns if turn.role == "assistant"]
        )
        if assistant_turn_count >= len(command_responses):
            raise ProviderError(
                "No scripted response left for %s at turn index %s."
                % (command, assistant_turn_count)
            )
        return CoachTurn.from_dict(command_responses[assistant_turn_count])


def create_provider(config: CoachConfig) -> Provider:
    if config.provider_name == "scripted":
        return ScriptedProvider()
    return OpenAIProvider()
