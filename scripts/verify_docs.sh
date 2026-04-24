#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  exit 1
}

assert_file() {
  local path="$1"
  [[ -f "$repo_root/$path" ]] || fail "missing file: $path"
}

assert_contains() {
  local path="$1"
  local pattern="$2"
  if ! rg -Fq -- "$pattern" "$repo_root/$path"; then
    fail "$path is missing expected text: $pattern"
  fi
}

assert_not_contains() {
  local path="$1"
  local pattern="$2"
  if rg -Fq -- "$pattern" "$repo_root/$path"; then
    fail "$path contains forbidden text: $pattern"
  fi
}

assistant_block_text() {
  local path="$1"
  local index="$2"
  local output
  local status

  set +e
  output="$(
    awk -v target="$index" '
      BEGIN {
        assistant_count = 0
        in_block = 0
      }
      $0 == "## Assistant" {
        assistant_count++
        if (in_block) {
          exit
        }
        if (assistant_count == target) {
          in_block = 1
        }
        next
      }
      $0 == "## Founder" && in_block {
        exit
      }
      in_block {
        print
      }
      END {
        if (assistant_count < target) {
          exit 42
        }
      }
    ' "$repo_root/$path"
  )"
  status=$?
  set -e

  if [[ "$status" == "42" ]]; then
    fail "$path is missing assistant block $index"
  fi
  [[ "$status" == "0" ]] || exit "$status"

  printf '%s' "$output"
}

assert_assistant_block_count() {
  local path="$1"
  local expected_count="$2"
  local count
  count="$(rg -c '^## Assistant$' "$repo_root/$path" | tr -d ' ')"
  [[ "$count" == "$expected_count" ]] || fail "$path should contain $expected_count assistant block(s), found $count"
}

assert_assistant_block_contains() {
  local path="$1"
  local index="$2"
  local pattern="$3"

  if ! assistant_block_text "$path" "$index" | rg -Fq -- "$pattern"; then
    fail "$path assistant block $index is missing expected text: $pattern"
  fi
}

assert_assistant_block_not_contains() {
  local path="$1"
  local index="$2"
  local pattern="$3"

  if assistant_block_text "$path" "$index" | rg -Fq -- "$pattern"; then
    fail "$path assistant block $index contains forbidden text: $pattern"
  fi
}

assert_assistant_question_count() {
  local path="$1"
  local index="$2"
  local expected_count="$3"
  local count

  count="$(assistant_block_text "$path" "$index" | tr -cd '?' | wc -c | tr -d ' ')"
  [[ "$count" == "$expected_count" ]] || fail "$path assistant block $index should contain $expected_count question mark(s), found $count"
}

assert_file "README.md"
assert_file "AGENTS.md"
assert_file "CLAUDE.md"
assert_file "SKILL.md"
assert_file "references/rubrics.md"
assert_file "references/conversation-protocol.md"
assert_file "references/state-system.md"
assert_file "references/commands/kickoff.md"
assert_file "references/commands/help.md"
assert_file "examples/golden/kickoff-bare.md"
assert_file "examples/golden/kickoff-discovery.md"
assert_file "examples/golden/kickoff-readback.md"
assert_file "examples/golden/help.md"
assert_file "examples/golden/implicit-kickoff-story.md"
assert_file "examples/golden/progress-routes-to-kickoff.md"
assert_file "examples/golden/wedge-diagnosis.md"
assert_file "agents/openai.yaml"
assert_file "install.sh"

assert_contains "README.md" "Paste your messy founder story"
assert_contains "README.md" "optional shortcuts for power users"
assert_contains "README.md" "In repo mode, it works in both Codex and Claude Code. The installed session-skill packaging remains Codex-specific."
assert_contains "README.md" "### Option 2: Claude Code Repo Mode"
assert_contains "README.md" 'This repo already includes `CLAUDE.md`, which imports `AGENTS.md`, so Claude Code uses the same repo-local coaching instructions as Codex repo mode.'
assert_contains "README.md" 'The `./install.sh` flow and `agents/openai.yaml` are Codex-only packaging, not Claude Code setup.'
assert_contains "README.md" '| `autonomy` | Alias of `trust` | Same as `trust` |'
assert_contains "README.md" '| `market` | Alias of `research` | Same as `research` |'
assert_not_contains "README.md" "### Planned Commands"
assert_not_contains "README.md" '| `signals` |'
assert_not_contains "README.md" '| `objections` |'
assert_not_contains "README.md" '| `pivot` |'
assert_not_contains "README.md" '| `evals` |'
assert_contains "AGENTS.md" 'Codex can read this file directly. Claude Code should load it via `CLAUDE.md`.'
assert_contains "AGENTS.md" "Founders do not need to learn the command model before they get value."
assert_contains "AGENTS.md" 'only working commands or aliases belong in `help`, startup menus, and `**Recommended next**` guidance'
assert_not_contains "AGENTS.md" "Planned stubs:"
assert_contains "CLAUDE.md" "@AGENTS.md"
assert_contains "CLAUDE.md" "Codex-specific session-skill packaging, not Claude Code setup."
assert_contains "SKILL.md" "These are internal working modes and optional shortcuts for power users."
assert_contains "SKILL.md" "Hidden compatibility redirects:"
assert_contains "SKILL.md" 'Do not list these in `help`, startup menus, or `**Recommended next**` guidance.'
assert_contains "references/conversation-protocol.md" "ask exactly one best next question"
assert_contains "references/conversation-protocol.md" "use a consent-first transition, not a menu recommendation"
assert_not_contains "references/conversation-protocol.md" "Phase: [current phase]"
assert_contains "references/state-system.md" "Founder-facing replies do not need to mirror this schema"
assert_contains "references/state-system.md" "Next coach-led move:"

for path in \
  "references/commands/kickoff.md" \
  "references/commands/wedge.md" \
  "references/commands/icp.md" \
  "references/commands/trust.md" \
  "references/commands/research.md" \
  "references/commands/experiment.md" \
  "references/commands/progress.md" \
  "references/commands/help.md"; do
  assert_not_contains "$path" "## Output Schema"
  assert_not_contains "$path" "Return exactly:"
done

assert_contains "references/commands/kickoff.md" "use this exact opener:"
assert_contains "references/commands/help.md" 'Keep `help` short and story-first.'
assert_contains "references/commands/help.md" 'Do not append a diagnosis, recommendation, or next-move block to `help`.'
assert_contains "references/commands/signals.md" '`signals` is a hidden compatibility shortcut.'
assert_contains "references/commands/objections.md" '`objections` is a hidden compatibility shortcut.'
assert_contains "references/commands/pivot.md" '`pivot` is a hidden compatibility shortcut.'
assert_contains "references/commands/evals.md" '`evals` is a hidden compatibility shortcut.'
assert_contains "agents/openai.yaml" "default to kickoff when the wedge is still fuzzy or state is missing"
assert_contains "install.sh" "This installs the Codex session skill for this repo."
assert_contains "install.sh" 'For Claude Code, open the repo directly so `CLAUDE.md` can load `AGENTS.md`.'

assert_contains "examples/golden/kickoff-bare.md" 'Command: `kickoff`'
assert_not_contains "examples/golden/kickoff-bare.md" "## Diagnosis"
assert_assistant_block_count "examples/golden/kickoff-bare.md" "1"
assert_assistant_block_contains "examples/golden/kickoff-bare.md" "1" "Let's make this concrete fast."
assert_assistant_block_contains "examples/golden/kickoff-bare.md" "1" "Rough bullets are fine."
assert_assistant_question_count "examples/golden/kickoff-bare.md" "1" "1"

assert_contains "examples/golden/kickoff-discovery.md" 'Command: `kickoff`'
assert_not_contains "examples/golden/kickoff-discovery.md" "## Diagnosis"
assert_assistant_block_count "examples/golden/kickoff-discovery.md" "2"
assert_assistant_block_contains "examples/golden/kickoff-discovery.md" "1" "Let's make this concrete fast."
assert_assistant_block_contains "examples/golden/kickoff-discovery.md" "2" "That gives us a product shape and an AI role."
assert_assistant_question_count "examples/golden/kickoff-discovery.md" "1" "1"
assert_assistant_question_count "examples/golden/kickoff-discovery.md" "2" "1"

assert_contains "examples/golden/kickoff-readback.md" 'Command: `kickoff`'
assert_not_contains "examples/golden/kickoff-readback.md" "## Diagnosis"
assert_assistant_block_count "examples/golden/kickoff-readback.md" "1"
assert_assistant_block_contains "examples/golden/kickoff-readback.md" "1" "## Kickoff Readback"
assert_assistant_block_contains "examples/golden/kickoff-readback.md" "1" "## What Looks Promising"
assert_assistant_block_contains "examples/golden/kickoff-readback.md" "1" "## What Needs Validation"
assert_assistant_block_contains "examples/golden/kickoff-readback.md" "1" "## Plan Of Attack"
assert_assistant_block_contains "examples/golden/kickoff-readback.md" "1" 'Next best move is `research`.'
assert_assistant_block_contains "examples/golden/kickoff-readback.md" "1" "Want me to validate buyer ownership, urgency, and substitute behavior now?"
assert_assistant_question_count "examples/golden/kickoff-readback.md" "1" "1"

assert_contains "examples/golden/help.md" 'Command: `help`'
assert_not_contains "examples/golden/help.md" "## Diagnosis"
assert_assistant_block_count "examples/golden/help.md" "1"
assert_assistant_block_contains "examples/golden/help.md" "1" "You can just paste the messy founder story."

assert_contains "examples/golden/implicit-kickoff-story.md" "I'm treating this as kickoff because the wedge is still fuzzy."
assert_not_contains "examples/golden/implicit-kickoff-story.md" "## Diagnosis"
assert_assistant_block_count "examples/golden/implicit-kickoff-story.md" "1"
assert_assistant_question_count "examples/golden/implicit-kickoff-story.md" "1" "1"

assert_contains "examples/golden/progress-routes-to-kickoff.md" 'Command: `progress`'
assert_contains "examples/golden/progress-routes-to-kickoff.md" 'State: placeholder-only state.md'
assert_not_contains "examples/golden/progress-routes-to-kickoff.md" "## Diagnosis"
assert_assistant_block_count "examples/golden/progress-routes-to-kickoff.md" "1"
assert_assistant_block_contains "examples/golden/progress-routes-to-kickoff.md" "1" "Let's make this concrete fast."
assert_assistant_question_count "examples/golden/progress-routes-to-kickoff.md" "1" "1"

assert_contains "examples/golden/wedge-diagnosis.md" 'Command: `wedge`'
assert_contains "examples/golden/wedge-diagnosis.md" "## Diagnosis"
assert_contains "examples/golden/wedge-diagnosis.md" 'Next best move is `trust`.'
assert_not_contains "examples/golden/wedge-diagnosis.md" "## Scorecard"
assert_assistant_block_count "examples/golden/wedge-diagnosis.md" "1"
assert_assistant_block_contains "examples/golden/wedge-diagnosis.md" "1" "## Diagnosis"
assert_assistant_block_contains "examples/golden/wedge-diagnosis.md" "1" "Want me to map that now?"
assert_assistant_question_count "examples/golden/wedge-diagnosis.md" "1" "1"

printf 'verify_docs.sh: OK\n'
