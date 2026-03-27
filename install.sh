#!/usr/bin/env bash

set -euo pipefail

SKILL_NAME="ai-wedge-coch"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR"
CODEX_HOME_DIR="${CODEX_HOME:-$HOME/.codex}"
SKILLS_DIR="$CODEX_HOME_DIR/skills"
TARGET_DIR="$SKILLS_DIR/$SKILL_NAME"
INSTALL_MODE="symlink"
FORCE=0
RESTART=1

usage() {
  cat <<'EOF'
Usage: ./install.sh [--force] [--copy] [--no-restart]

Options:
  --force       Replace an existing install at the target path.
  --copy        Copy the repo into the Codex skills directory instead of symlinking it.
  --no-restart  Skip the best-effort Codex relaunch step on macOS.
  -h, --help    Show this help text.
EOF
}

die() {
  printf 'Error: %s\n' "$1" >&2
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --force)
      FORCE=1
      ;;
    --copy)
      INSTALL_MODE="copy"
      ;;
    --no-restart)
      RESTART=0
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "Unknown argument: $1"
      ;;
  esac
  shift
done

[[ -f "$SOURCE_DIR/SKILL.md" ]] || die "Missing SKILL.md in $SOURCE_DIR"
[[ -f "$SOURCE_DIR/agents/openai.yaml" ]] || die "Missing agents/openai.yaml in $SOURCE_DIR"

mkdir -p "$SKILLS_DIR"

source_real="$(cd "$SOURCE_DIR" && pwd -P)"
already_installed=0

if [[ -e "$TARGET_DIR" || -L "$TARGET_DIR" ]]; then
  target_real=""
  if [[ -d "$TARGET_DIR" ]]; then
    target_real="$(cd "$TARGET_DIR" && pwd -P)"
  fi

  if [[ "$target_real" == "$source_real" ]]; then
    already_installed=1
  else
    [[ "$FORCE" -eq 1 ]] || die "Target already exists at $TARGET_DIR. Re-run with --force to replace it."
    rm -rf "$TARGET_DIR"
  fi
fi

if [[ "$already_installed" -eq 0 ]]; then
  if [[ "$INSTALL_MODE" == "copy" ]]; then
    cp -R "$SOURCE_DIR" "$TARGET_DIR"
  else
    ln -s "$SOURCE_DIR" "$TARGET_DIR"
  fi
fi

restart_message="Restart Codex manually to pick up the new skill."

if [[ "$RESTART" -eq 1 && "$(uname -s)" == "Darwin" ]]; then
  restarted=0
  for app_name in "Codex" "OpenAI Codex"; do
    if osascript -e "id of application \"$app_name\"" >/dev/null 2>&1; then
      osascript -e "tell application \"$app_name\" to quit" >/dev/null 2>&1 || true
      sleep 1
      open -a "$app_name" >/dev/null 2>&1 || true
      restarted=1
      restart_message="Codex was relaunched. If it was not running, open it normally."
      break
    fi
  done
fi

cat <<EOF
Installed $SKILL_NAME into:
  $TARGET_DIR

Install mode:
  $INSTALL_MODE

$restart_message

Then run:
  \$ai-wedge-coch kickoff

Other useful commands:
  \$ai-wedge-coch wedge
  \$ai-wedge-coch icp
  \$ai-wedge-coch trust
  \$ai-wedge-coch experiment
  \$ai-wedge-coch progress
EOF
