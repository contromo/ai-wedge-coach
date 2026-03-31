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
assert_file "examples/golden/kickoff-discovery.md"
assert_file "examples/golden/kickoff-readback.md"
assert_file "examples/golden/implicit-kickoff-story.md"
assert_file "examples/golden/progress-routes-to-kickoff.md"
assert_file "examples/golden/wedge-clarify.md"
assert_file "examples/golden/wedge-diagnosis.md"
assert_file "agents/openai.yaml"

assert_contains "README.md" "Paste your messy founder story"
assert_contains "README.md" "optional shortcuts for power users"
assert_contains "README.md" 'A fresh `kickoff` turn starts with one intake question'
assert_contains "README.md" 'Phase`, `What we know`, and `Why this next question matters`'
assert_contains "README.md" "That phased kickoff is deliberate, not withheld value:"
assert_contains "README.md" '| `kickoff` | Force onboarding or reseed after a dead wedge | One-question intake with progress cue, kickoff readback, short plan of attack, then company snapshot and diagnosis when justified |'
assert_contains "README.md" "Expected progression:"
assert_contains "README.md" "- readback phase: kickoff readback plus short plan of attack"
assert_contains "README.md" "- diagnosis phase: company snapshot and diagnosis only when enough intake and evidence exist"
assert_contains "README.md" '| `autonomy` | Alias of `trust` | Same as `trust` |'
assert_contains "README.md" '| `market` | Alias of `research` | Same as `research` |'
assert_not_contains "README.md" '| `kickoff` | Force onboarding or reseed after a dead wedge | Guided intake, plan of attack, then company snapshot and diagnosis when justified |'
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
assert_contains "references/conversation-protocol.md" "Phase: [current phase]"
assert_contains "references/conversation-protocol.md" "What we know: [running readback in 1-2 concrete clauses]"
assert_contains "references/conversation-protocol.md" "Why this next question matters: [the decision, assessment, or diagnosis that is still blocked]"
assert_contains "references/commands/kickoff.md" "Rough bullets are fine."
assert_contains "references/commands/kickoff.md" 'If `kickoff` was inferred from a founder story'
assert_contains "references/commands/kickoff.md" "Phase: Founder narrative"
assert_contains "references/commands/wedge.md" "Why this next question matters:"
assert_contains "references/commands/icp.md" "Why this next question matters:"
assert_contains "references/commands/trust.md" "Why this next question matters:"
assert_contains "references/commands/research.md" "Why this next question matters:"
assert_contains "references/commands/experiment.md" "Why this next question matters:"
assert_contains "references/commands/progress.md" "Why this next question matters:"
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
assert_not_contains "examples/golden/kickoff-bare.md" "## Diagnosis"
assert_not_contains "examples/golden/kickoff-bare.md" "## Recommendation"
assert_not_contains "examples/golden/kickoff-bare.md" "## Next Move"
assert_assistant_block_count "examples/golden/kickoff-bare.md" "1"
assert_assistant_block_contains "examples/golden/kickoff-bare.md" "1" "Phase: Founder narrative"
assert_assistant_block_contains "examples/golden/kickoff-bare.md" "1" "What we know: No founder-specific context yet."
assert_assistant_block_contains "examples/golden/kickoff-bare.md" "1" "Why this next question matters: I need the product shape before I can narrow the workflow wedge."
assert_assistant_block_contains "examples/golden/kickoff-bare.md" "1" "Rough bullets are fine."
assert_assistant_question_count "examples/golden/kickoff-bare.md" "1" "1"

assert_contains "examples/golden/kickoff-discovery.md" 'Command: `kickoff`'
assert_contains "examples/golden/kickoff-discovery.md" 'State: missing founder-specific intake'
assert_not_contains "examples/golden/kickoff-discovery.md" "## Diagnosis"
assert_not_contains "examples/golden/kickoff-discovery.md" "## Current Thesis"
assert_assistant_block_count "examples/golden/kickoff-discovery.md" "2"
assert_assistant_block_contains "examples/golden/kickoff-discovery.md" "1" "Phase: Founder narrative"
assert_assistant_block_contains "examples/golden/kickoff-discovery.md" "1" "Rough bullets are fine."
assert_assistant_question_count "examples/golden/kickoff-discovery.md" "1" "1"
assert_assistant_block_contains "examples/golden/kickoff-discovery.md" "2" "Phase: Workflow extraction"
assert_assistant_block_contains "examples/golden/kickoff-discovery.md" "2" "What we know: You help compliance teams answer security questionnaires faster by drafting from prior responses and evidence."
assert_assistant_block_contains "examples/golden/kickoff-discovery.md" "2" "Why this next question matters: I need the day-to-day owner before I can narrow the wedge and buyer path."
assert_assistant_block_not_contains "examples/golden/kickoff-discovery.md" "2" "## Diagnosis"
assert_assistant_question_count "examples/golden/kickoff-discovery.md" "2" "1"

assert_contains "examples/golden/kickoff-readback.md" 'Command: `kickoff`'
assert_contains "examples/golden/kickoff-readback.md" 'State: discovery sufficient for readback but not diagnosis'
assert_not_contains "examples/golden/kickoff-readback.md" "## Diagnosis"
assert_not_contains "examples/golden/kickoff-readback.md" "## Recommendation"
assert_assistant_block_count "examples/golden/kickoff-readback.md" "1"
assert_assistant_block_contains "examples/golden/kickoff-readback.md" "1" "## Current Thesis"
assert_assistant_block_contains "examples/golden/kickoff-readback.md" "1" "## Open Questions"
assert_assistant_block_contains "examples/golden/kickoff-readback.md" "1" "## Evidence Collected"
assert_assistant_block_contains "examples/golden/kickoff-readback.md" "1" "## Next Move"
assert_assistant_block_contains "examples/golden/kickoff-readback.md" "1" "**Recommended next**:"
assert_assistant_question_count "examples/golden/kickoff-readback.md" "1" "0"

assert_contains "examples/golden/implicit-kickoff-story.md" "I'm treating this as kickoff because the wedge is still fuzzy."
assert_not_contains "examples/golden/implicit-kickoff-story.md" "## Diagnosis"
assert_not_contains "examples/golden/implicit-kickoff-story.md" "what are you building, in one sentence?"
assert_assistant_block_count "examples/golden/implicit-kickoff-story.md" "1"
assert_assistant_block_contains "examples/golden/implicit-kickoff-story.md" "1" "Phase: Workflow extraction"
assert_assistant_block_contains "examples/golden/implicit-kickoff-story.md" "1" "Why this next question matters: I need the day-to-day owner before I can narrow the wedge and buyer path."
assert_assistant_question_count "examples/golden/implicit-kickoff-story.md" "1" "1"

assert_contains "examples/golden/progress-routes-to-kickoff.md" 'Command: `progress`'
assert_contains "examples/golden/progress-routes-to-kickoff.md" 'State: placeholder-only state.md'
assert_not_contains "examples/golden/progress-routes-to-kickoff.md" "## Diagnosis"
assert_not_contains "examples/golden/progress-routes-to-kickoff.md" "## Current Scoreboard"
assert_assistant_block_count "examples/golden/progress-routes-to-kickoff.md" "1"
assert_assistant_block_contains "examples/golden/progress-routes-to-kickoff.md" "1" "I'm treating this as kickoff because there is no usable founder-specific state yet."
assert_assistant_block_contains "examples/golden/progress-routes-to-kickoff.md" "1" "Phase: Founder narrative"
assert_assistant_block_contains "examples/golden/progress-routes-to-kickoff.md" "1" "Rough bullets are fine."
assert_assistant_question_count "examples/golden/progress-routes-to-kickoff.md" "1" "1"

assert_contains "examples/golden/wedge-clarify.md" 'Command: `wedge`'
assert_not_contains "examples/golden/wedge-clarify.md" "## Diagnosis"
assert_assistant_block_count "examples/golden/wedge-clarify.md" "1"
assert_assistant_block_contains "examples/golden/wedge-clarify.md" "1" "Phase: Workflow clarification"
assert_assistant_block_contains "examples/golden/wedge-clarify.md" "1" "Why this next question matters: I need one specific recurring workflow before I can assess pain, recurrence, or buyer fit."
assert_assistant_question_count "examples/golden/wedge-clarify.md" "1" "1"

assert_contains "examples/golden/wedge-diagnosis.md" 'Command: `wedge`'
assert_contains "examples/golden/wedge-diagnosis.md" "## Diagnosis"
assert_contains "examples/golden/wedge-diagnosis.md" "**Recommended next**:"
assert_assistant_block_count "examples/golden/wedge-diagnosis.md" "1"
assert_assistant_block_contains "examples/golden/wedge-diagnosis.md" "1" "## Diagnosis"
assert_assistant_block_contains "examples/golden/wedge-diagnosis.md" "1" "**Recommended next**:"

printf 'verify_docs.sh: OK\n'
