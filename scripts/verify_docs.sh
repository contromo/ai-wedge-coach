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

assert_question_count() {
  local path="$1"
  local expected="$2"
  local count
  count="$(awk '/^## Assistant$/ {in_block=1; next} /^## / && in_block {exit} in_block {print}' "$repo_root/$path" | tr -cd '?' | wc -c | tr -d ' ')"
  [[ "$count" == "$expected" ]] || fail "$path should contain $expected question mark(s) in the assistant block, found $count"
}

assert_file "README.md"
assert_file "AGENTS.md"
assert_file "SKILL.md"
assert_file "references/rubrics.md"
assert_file "references/conversation-protocol.md"
assert_file "references/commands/kickoff.md"
assert_file "references/commands/help.md"
assert_file "references/commands/signals.md"
assert_file "references/commands/objections.md"
assert_file "references/commands/pivot.md"
assert_file "references/commands/evals.md"
assert_file "examples/golden/kickoff-bare.md"
assert_file "examples/golden/implicit-kickoff-story.md"
assert_file "examples/golden/wedge-diagnosis.md"
assert_file "agents/openai.yaml"

assert_contains "README.md" "Paste your messy founder story"
assert_contains "README.md" "optional shortcuts for power users"
assert_contains "README.md" '| `autonomy` | Alias of `trust` | Same as `trust` |'
assert_contains "README.md" '| `market` | Alias of `research` | Same as `research` |'
assert_not_contains "README.md" "### Planned Commands"
assert_not_contains "README.md" '| `signals` |'
assert_not_contains "README.md" '| `objections` |'
assert_not_contains "README.md" '| `pivot` |'
assert_not_contains "README.md" '| `evals` |'
assert_contains "AGENTS.md" "Founders do not need to learn the command model before they get value."
assert_contains "AGENTS.md" 'only working commands or aliases belong in `help`, startup menus, and `**Recommended next**` guidance'
assert_not_contains "AGENTS.md" "Planned stubs:"
assert_contains "SKILL.md" "These are internal working modes and optional shortcuts for power users."
assert_contains "SKILL.md" "Hidden compatibility redirects:"
assert_contains "SKILL.md" 'Do not list these in `help`, startup menus, or `**Recommended next**` guidance.'
assert_contains "references/conversation-protocol.md" "ask exactly one best next question"
assert_contains "references/conversation-protocol.md" "Routing precedence:"
assert_contains "references/conversation-protocol.md" "I'm treating this as [command] because [brief reason]."
assert_contains "references/commands/kickoff.md" "Rough bullets are fine."
assert_contains "references/commands/kickoff.md" 'If `kickoff` was inferred from a founder story'
assert_contains "references/commands/help.md" "Commands are optional shortcuts for direct control."
assert_contains "references/commands/help.md" '- `help` - Show story-first starting guidance and the optional command shortcuts.'
assert_not_contains "references/commands/help.md" '- `signals` - Planned.'
assert_not_contains "references/commands/help.md" '- `objections` - Planned.'
assert_not_contains "references/commands/help.md" '- `pivot` - Planned.'
assert_not_contains "references/commands/help.md" '- `evals` - Planned.'
assert_contains "references/commands/signals.md" '`signals` is a hidden compatibility shortcut.'
assert_contains "references/commands/objections.md" '`objections` is a hidden compatibility shortcut.'
assert_contains "references/commands/pivot.md" '`pivot` is a hidden compatibility shortcut.'
assert_contains "references/commands/evals.md" '`evals` is a hidden compatibility shortcut.'
assert_contains "agents/openai.yaml" "default to kickoff when the wedge is still fuzzy or state is missing"

assert_contains "examples/golden/kickoff-bare.md" 'Command: `kickoff`'
assert_contains "examples/golden/kickoff-bare.md" "Rough bullets are fine."
assert_not_contains "examples/golden/kickoff-bare.md" "## Diagnosis"
assert_question_count "examples/golden/kickoff-bare.md" "1"

assert_contains "examples/golden/implicit-kickoff-story.md" "I'm treating this as kickoff because the wedge is still fuzzy."
assert_not_contains "examples/golden/implicit-kickoff-story.md" "## Diagnosis"
assert_not_contains "examples/golden/implicit-kickoff-story.md" "what are you building, in one sentence?"
assert_question_count "examples/golden/implicit-kickoff-story.md" "1"

assert_contains "examples/golden/wedge-diagnosis.md" 'Command: `wedge`'
assert_contains "examples/golden/wedge-diagnosis.md" "## Diagnosis"
assert_contains "examples/golden/wedge-diagnosis.md" "**Recommended next**:"

printf 'verify_docs.sh: OK\n'
