# AI Agent Wedge Coach

A repo-driven coaching system for early-stage B2B AI founders who need to find a real workflow wedge, define trust boundaries, avoid demo traps, and run the next highest-signal experiment.

In repo mode, it works in both Codex and Claude Code. The installed session-skill packaging remains Codex-specific.

This is not generic startup advice. It is a debugging system for the company.

It assesses the business across six top-level dimensions with qualitative evidence states, pressure-tests wedges with a dedicated rubric, keeps persistent founder state across sessions, logs customer interviews and objections, preserves dead wedges in a graveyard, and carries each session toward one concrete next move without turning the product into a command menu.

Behavior follows the instructions in `SKILL.md` and `AGENTS.md`, not a hardcoded engine. In Codex repo mode, the app reads `AGENTS.md` directly. In Claude Code repo mode, `CLAUDE.md` imports the same `AGENTS.md`. The `./install.sh` flow and `agents/openai.yaml` are Codex-only packaging, not Claude Code setup.

Paste your messy founder story and the coach will infer the right mode, explain the route, and start narrowing the wedge immediately. Commands like `kickoff` or `wedge` remain available as optional shortcuts for power users.

See `examples/` for a worked coaching session.

---

## What It Does

**Wedge diagnosis** - Forces workflow compression, assesses the wedge across seven rubric axes, surfaces recurrence as a first-class concern, and recommends `keep`, `narrow`, `kill`, or `split`.

**ICP pressure-testing** - Separates user, buyer, and champion, forces explicit exclusions, and identifies the narrowest credible beachhead instead of letting the founder hide in a broad market story.

**Trust architecture** - Maps what can run autonomously, what needs review, and what must stay human-only. Routes founders away from "full agent" theater when the trust boundary is still incoherent.

**Experiment design** - Turns the current diagnosis into one 7-day or 14-day falsifiable experiment with an owner, a deadline, a falsifier, and a decision rule.

**Progress and continuity** - Starts with one `state.md`, then creates interview, objection, experiment, research, and wedge-death logs only when the workflow actually produces that detail.

**Accelerator ops handoff** - Produces partner briefings, weekly company status deltas, red-flag memos, and `needs human help now` triggers so human operators know when to step in.

**Cohort memory** - Tracks common failed wedges, repeated objections, trust-boundary patterns, and segment-specific benchmarks across companies when shared cohort memory is available.

**Experiment quality control** - Requires every experiment to carry an owner, deadline, falsifier, thresholds, and a decision rule, then pushes the result back into active state automatically.

**Pattern recognition** - Detects founder archetypes like Premature Scaler, Demo Polisher, Feature Hoarder, Data Avoider, Pivot Junkie, and Services-in-Denial, then changes the coaching posture accordingly: some founders need compression, others contradiction, proof, or containment.

**Market reality checking** - Runs market research against founder claims with a minimum source mix, explicit contradiction handling, and an `insufficient evidence` outcome when the proof is weak.

**Evidence discipline** - Separates observed facts, founder assertions, and model inferences so the coach does not smuggle guesses into the evidence base.

**Guided conversation** - Every working command should guide the founder one question at a time, force clarity step by step, and hold diagnosis until the command has enough signal. Founder-facing replies stay conversational; the durable structure lives in the runtime files and command logic. When a deeper mode switch is needed, the coach should usually use a consent-first handoff like `Next best move is trust. Want me to map that now?`

---

## Quick Start

### Option 1: Standalone Python CLI

1. Clone the repo:

```bash
git clone https://github.com/contromo/ai-wedge-coach.git
cd ai-wedge-coach
```

2. Install the CLI:

```bash
python3 -m pip install -e .
```

3. Set your OpenAI API key:

```bash
export OPENAI_API_KEY=...
```

4. Start a structured workspace and run the coach:

```bash
wedge-coach init
wedge-coach kickoff
```

You can also run single turns non-interactively:

```bash
wedge-coach kickoff --message "We're building AI-generated onboarding briefs for finance ops teams."
wedge-coach progress
wedge-coach export --format html
```

The CLI stores canonical state in `.wedge-coach/state.json`, writes append-only JSONL logs under `.wedge-coach/logs/`, keeps session transcripts under `.wedge-coach/sessions/`, and exports advisor-ready reports to `exports/`.

If you already have a markdown-based founder workspace, import it once:

```bash
wedge-coach import --from-markdown .
```

### Option 2: OpenAI Codex Local Repo Mode (recommended for doc-first use)

1. Clone the repo:

```bash
git clone https://github.com/contromo/ai-wedge-coach.git
cd ai-wedge-coach
```

Or download it as a ZIP and unzip it.

2. Open the folder in Codex.

This repo already includes `AGENTS.md`, so no rename step is needed.

3. Paste your founder story:

```text
We're building an AI copilot for security questionnaires.
It drafts first-pass answers from our prior responses and evidence base.
The wedge still feels fuzzy and I'm not sure which team we should own first.
```

Local repo mode uses the instructions in `AGENTS.md` and `SKILL.md` directly. You can start with a free-form story and the coach will infer the right command, say which one it chose, and stay in that mode until an intentional handoff or explicit command switch.
Plain commands like `kickoff`, `wedge`, `icp`, `trust`, `research`, `experiment`, and `progress` still work as direct shortcuts.
On a fresh repo with no founder-specific state yet, the inferred path should default to `kickoff`, guide the founder one question at a time, run a market-reality check, and only then settle into diagnosis.
A fresh `kickoff` turn starts with one intake question, not a summary, scorecard, or diagnosis.
That phased kickoff is deliberate, not withheld value: the first turn removes the biggest ambiguity, the next useful stage is a readback plus short plan of attack, and scores or diagnosis only appear when the founder-specific evidence is strong enough to justify them.

### Option 2: Claude Code Repo Mode

1. Clone the repo:

```bash
git clone https://github.com/contromo/ai-wedge-coach.git
cd ai-wedge-coach
```

Or download it as a ZIP and unzip it.

2. Open the folder in Claude Code.

This repo already includes `CLAUDE.md`, which imports `AGENTS.md`, so Claude Code uses the same repo-local coaching instructions as Codex repo mode.

3. Paste your founder story:

```text
We're building AI workflow tooling for vendor onboarding.
The pain feels real, but the first wedge and trust boundary are still fuzzy.
```

Claude Code repo mode should behave the same as Codex repo mode because both paths resolve to the same underlying coaching instructions.
You can start with a free-form story and the coach will infer the right command, say which one it chose, and stay in that mode until an intentional handoff or explicit command switch.

### Option 3: Installed Session Skill (Codex only)

1. Clone the repo:

```bash
git clone https://github.com/contromo/ai-wedge-coach.git
cd ai-wedge-coach
```

Or download it as a ZIP and unzip it.

2. Install the skill:

```bash
./install.sh
```

By default this installs a symlink into Codex's skill directory. If `$CODEX_HOME` is unset, the installer uses `~/.codex/skills`.
This packaging is Codex-only. It depends on Codex session-skill loading plus `agents/openai.yaml`; it does not configure Claude Code. For Claude Code, use repo mode instead.

3. Restart Codex, then paste a founder story like:

```text
We're building AI agents for finance ops teams to reconcile exceptions faster.
The story is still broad and I need help finding the first workflow wedge.
```

Installed session-skill mode should also accept a free-form founder story first and route implicitly.
If you want to force a specific command in session-skill mode, use the `$ai-wedge-coach` prefix, for example `$ai-wedge-coach kickoff`.
On first use, the inferred path should normally be `kickoff`, request the missing founder intake one question at a time, then build a plan of attack before issuing a hard diagnosis.

Installer options:

```bash
./install.sh --force
./install.sh --copy
./install.sh --no-restart
```

---

## Runtime Files

The coach writes persistent state into the founder's current working directory.

Default mode starts with:

- `state.md`

Expanded mode creates these on demand:

- `interview_log.md`
- `objection_log.md`
- `experiment_log.md`
- `market_research_log.md`
- `wedge_graveyard.md`

These files are created and updated automatically when the workflow justifies them. If you test the skill from this repo root, they are gitignored.
They hold the durable structure; founder-facing replies do not need to mirror the file schemas.

Optional shared accelerator memory:

- `cohort_memory/wedge_failures.md`
- `cohort_memory/objection_patterns.md`
- `cohort_memory/trust_patterns.md`
- `cohort_memory/segment_benchmarks.md`

If you want cross-company memory, point each founder workspace at the same `cohort_memory/` directory, usually by symlink.

---

## Verification

This repo is still doc-driven, but it now includes lightweight checks so the protocol can drift less silently as the spec grows.

Run:

```bash
./scripts/verify_docs.sh
```

What it checks:

- story-first onboarding copy still exists and commands are framed as optional shortcuts
- the conversation protocol still enforces one-question cadence
- `kickoff` still forbids diagnosis on a bare first turn, preserves the "rough bullets are fine" onboarding language, and keeps the kickoff readback before diagnosis
- golden transcript fixtures cover bare kickoff, multi-turn kickoff discovery, kickoff readback before diagnosis, inferred kickoff, auto-routing from `progress` into kickoff, a lean `help` reply, and a diagnosis-allowed `wedge` turn

---

## Command Shortcuts

You do not need to pick one before the coach can help.
The coach should usually carry the conversation forward with a lightweight consent question instead of telling the founder to type the next command.

### Core Commands

| Command | Purpose | Typical result |
| --- | --- | --- |
| `kickoff` | Force onboarding or reseed after a dead wedge | One-question intake, short readbacks, and a plan of attack before any hard diagnosis |
| `wedge` | Pressure-test the current workflow wedge | A compressed wedge read, recurrence callout, main bottleneck, and keep/narrow/kill/split verdict |
| `icp` | Pressure-test who this is really for | A narrow beachhead read with user/buyer/champion separation and exclusions |
| `trust` | Design the AI autonomy boundary | A concise autonomy boundary, key risk, and operating recommendation |
| `autonomy` | Alias of `trust` | Same as `trust` |
| `research` | Validate founder claims against the market | A focused market read showing what supports, weakens, and changes the thesis |
| `market` | Alias of `research` | Same as `research` |
| `experiment` | Design or update one high-signal experiment | One compact experiment brief with a falsifier and decision rule |
| `progress` | Summarize accumulated learning and current bottleneck | A concise trajectory read with explicit recurrence guidance and the next move |
| `help` | Explain story-first entry and optional command shortcuts | A lean start-here reply plus shortcut guidance |

---

## Assessment System

Assessment discipline:

- use only `untested`, `weak evidence`, `validated`, or `strong`
- every assessment must cite observed evidence or explicitly stay `untested`
- do not add numeric totals, bands, or confidence overlays to rubric outputs

### Company-Level Progress Rubric

Every `progress` run assesses:

- `Wedge Sharpness`
- `ICP Focus`
- `Value Recurrence`
- `Trust Architecture`
- `Evidence Quality`
- `Learning Velocity`

### Wedge-Specific Rubric

The `wedge` command assesses:

- `Specificity`
- `Pain`
- `Recurrence`
- `Buyer Alignment`
- `Trust Fit`
- `Value Realization`
- `Deployment Fit`

It also runs a non-rubric `Why AI?` check to make sure the product actually benefits from AI rather than just wearing the label.

---

## Fast Workflow Examples

### 1) Direct `kickoff` on a fresh workspace

```text
kickoff
```

Typical progression:

- first turn: one intake question
- discovery phase: no diagnosis, recommendation, or next-move block yet
- readback phase: kickoff readback plus short plan of attack
- diagnosis phase: company snapshot and diagnosis only when enough intake and evidence exist

### 2) Paste a messy founder story

```text
We're building an AI copilot for procurement teams.
It reads vendor emails, drafts responses, and pulls contract context.
I know the pain is real, but the wedge and buyer are still fuzzy.
```

Typical result: the coach infers `kickoff`, says why, asks one best next question, and keeps the conversation in discovery mode until it can give a short readback and plan of attack.

### 3) Broad product claim that needs compression

```text
wedge
```

Then describe the product. The coach will force three wedge versions:

- broad
- narrower
- brutally narrow

Typical result: the coach compresses the wedge, calls out recurrence explicitly, explains the main weakness, and lands on `keep`, `narrow`, `kill`, or `split`.

### 4) Buyer and user are blurred

```text
icp
```

Typical result: the coach names the narrowest credible beachhead, separates user from buyer and champion, and makes the exclusions explicit.

### 5) The founder wants a full agent

```text
trust
```

Typical result: the coach draws the autonomy boundary, names the highest-risk failure, and recommends the safest operating mode.

### 6) The founder needs the next test

```text
experiment
```

Typical result: the coach gives one compact experiment brief with a falsifier, owner, deadline, thresholds, and a decision rule.

### 7) The founder needs market validation

```text
research
```

Typical result: the coach gives a focused market read that shows what supports the story, what weakens it, and what should happen next.

### 8) The founder wants the hard truth

```text
progress
```

Typical result: the coach gives a concise progress read, explicitly calls out recurrence, and names the next critical move.
- red-flag memo
- `needs human help now` triggers

---

## Local Repo Mode vs Installed Skill Mode

If you open the repo directly in Codex or Claude Code, you can just paste a founder story. If you want direct control, use plain commands like:

```text
kickoff
wedge
trust
research
```

If you install it as a session skill with `./install.sh`, that path is Codex-only. You can still start with a founder story. If you want to force a command, use:

```text
$ai-wedge-coach kickoff
$ai-wedge-coach wedge
$ai-wedge-coach trust
$ai-wedge-coach research
```

In repo mode, Codex reads the repo-local `AGENTS.md` directly and Claude Code reads `CLAUDE.md`, which imports the same `AGENTS.md`.
Installed session-skill mode is only for Codex and uses the packaged skill metadata instead of the repo-local Claude entrypoint.
