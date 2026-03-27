# AI Agent Wedge Coach

A Codex-based coaching system for early-stage B2B AI founders who need to choose the right workflow wedge, define trust boundaries, avoid demo traps, and run the next highest-signal experiment.

This is not generic startup advice. It is a debugging system for the company.

It scores the business across six top-level dimensions, pressure-tests wedges with a dedicated rubric, keeps persistent founder state across sessions, logs customer interviews and objections, preserves dead wedges in a graveyard, and pushes every session toward one concrete next move.

Say `kickoff`, describe what you're building, and the coach will start narrowing the wedge immediately.

---

## What It Does

**Wedge diagnosis** - Forces workflow compression, scores the wedge across seven dimensions, surfaces recurrence as a first-class concern, and recommends `keep`, `narrow`, `kill`, or `split`.

**ICP pressure-testing** - Separates user, buyer, and champion, forces explicit exclusions, and identifies the narrowest credible beachhead instead of letting the founder hide in a broad market story.

**Trust architecture** - Maps what can run autonomously, what needs review, and what must stay human-only. Routes founders away from "full agent" theater when the trust boundary is still incoherent.

**Experiment design** - Turns the current diagnosis into one 7-day or 14-day falsifiable experiment with an owner, a deadline, a falsifier, and a decision rule.

**Progress and continuity** - Maintains `founder_state.md`, `interview_log.md`, `objection_log.md`, `experiment_log.md`, and `wedge_graveyard.md` so the system compounds over time instead of restarting every session.

**Accelerator ops handoff** - Produces partner briefings, weekly company status deltas, red-flag memos, and `needs human help now` triggers so human operators know when to step in.

**Cohort memory** - Tracks common failed wedges, repeated objections, trust-boundary patterns, and segment-specific benchmarks across companies when shared cohort memory is available.

**Experiment quality control** - Requires every experiment to carry an owner, deadline, falsifier, thresholds, and a decision rule, then pushes the result back into active state automatically.

**Pattern recognition** - Detects founder archetypes like Premature Scaler, Demo Polisher, Feature Hoarder, Data Avoider, Pivot Junkie, and Services-in-Denial, then changes the coaching posture accordingly: some founders need compression, others contradiction, proof, or containment.

**Market reality checking** - Runs market research against founder claims with a minimum source mix, explicit contradiction handling, and an `insufficient evidence` outcome when the proof is weak.

**Evidence discipline** - Separates observed facts, founder assertions, and model inferences so the coach does not smuggle guesses into the evidence base.

**Guided conversation** - Every working command should guide the founder one question at a time, force clarity step by step, and hold diagnosis until the command has enough signal.

---

## Quick Start

### Option 1: OpenAI Codex Local Repo Mode (recommended)

1. Clone the repo:

```bash
git clone https://github.com/<your-org-or-user>/ai-wedge-coach.git
cd ai-wedge-coach
```

Or download it as a ZIP and unzip it.

2. Open the folder in Codex.

This repo already includes `AGENTS.md`, so no rename step is needed.

3. Say:

```text
kickoff
```

Local repo mode uses the instructions in `AGENTS.md` and `SKILL.md` directly. You talk to the coach with plain commands like `kickoff`, `wedge`, `icp`, `trust`, `research`, `experiment`, and `progress`.
On a fresh repo with no founder-specific state yet, `kickoff` should guide the founder one question at a time, force clarity step by step, run a market-reality check, and only then settle into diagnosis.

### Option 2: Installed Session Skill

1. Clone the repo:

```bash
git clone https://github.com/<your-org-or-user>/ai-wedge-coach.git
cd ai-wedge-coach
```

Or download it as a ZIP and unzip it.

2. Install the skill:

```bash
./install.sh
```

By default this installs a symlink into Codex's skill directory. If `$CODEX_HOME` is unset, the installer uses `~/.codex/skills`.

3. Restart Codex, then say:

```text
$ai-wedge-coach kickoff
```

For installed session-skill mode, use the `$ai-wedge-coach` prefix.
On first use, `kickoff` should request the missing founder intake one question at a time, then build a plan of attack before issuing a hard diagnosis.

Installer options:

```bash
./install.sh --force
./install.sh --copy
./install.sh --no-restart
```

---

## Runtime Files

The coach writes persistent state into the founder's current working directory:

- `founder_state.md`
- `interview_log.md`
- `objection_log.md`
- `experiment_log.md`
- `market_research_log.md`
- `wedge_graveyard.md`

These files are created and updated automatically. If you test the skill from this repo root, they are gitignored.

Optional shared accelerator memory:

- `cohort_memory/wedge_failures.md`
- `cohort_memory/objection_patterns.md`
- `cohort_memory/trust_patterns.md`
- `cohort_memory/segment_benchmarks.md`

If you want cross-company memory, point each founder workspace at the same `cohort_memory/` directory, usually by symlink.

---

## Commands

### Core Commands

| Command | Purpose | Typical Output |
| --- | --- | --- |
| `kickoff` | Initialize founder state or reseed after a dead wedge | Company snapshot, evidence-backed baseline scores or suppressions, initial diagnosis, recommended next command |
| `wedge` | Pressure-test the current workflow wedge | Wedge compression, evidence-backed 7-axis scorecard or suppressions, `Why AI?` check, keep/narrow/kill/split recommendation |
| `icp` | Pressure-test who this is really for | User/buyer/champion split, exclusions, beachhead verdict |
| `trust` | Design the AI autonomy boundary | Automation map, failure taxonomy, copilot/review queue/constrained agent/full automation recommendation |
| `research` | Validate founder claims against the market | Source mix, claim verdicts, contradictions, `insufficient evidence` calls, research-backed next move |
| `experiment` | Design or update one high-signal experiment | Hypothesis, falsifier, owner, deadline, thresholds, decision rule, automatic state feedback |
| `progress` | Summarize accumulated learning and current bottleneck | Six-dimension scoreboard with score evidence or suppressions, founder handling read, cohort memory read, partner briefing, weekly delta, red-flag memo, human-help triggers |
| `help` | Show the command menu and starting points | Command list plus recommended entry point |

### Planned Commands

| Command | Current Behavior |
| --- | --- |
| `signals` | Redirects to `progress` for evidence weighting |
| `objections` | Redirects to `icp` or `trust` depending on the root cause |
| `pivot` | Redirects to `wedge` kill-path review or `kickoff` reseed mode |
| `evals` | Redirects to `experiment` to define real proof and thresholds |

---

## Scoring System

Score discipline:

- every numeric score must include a confidence label and cited observed evidence
- if the evidence is mostly assertion or inference, suppress the score instead of guessing
- wedge totals and bands should be suppressed if any underlying wedge axis is suppressed

### Company-Level Progress Rubric

Every `progress` run scores:

- `Wedge Sharpness`
- `ICP Focus`
- `Value Recurrence`
- `Trust Architecture`
- `Evidence Quality`
- `Learning Velocity`

### Wedge-Specific Rubric

The `wedge` command scores:

- `Specificity`
- `Pain`
- `Recurrence`
- `Buyer Alignment`
- `Trust Fit`
- `Value Realization`
- `Deployment Fit`

It also runs a non-scored `Why AI?` check to make sure the product actually benefits from AI rather than just wearing the label.

---

## Fast Workflow Examples

### 1) Initial setup

```text
kickoff
```

Expected output:

- company snapshot
- current thesis
- baseline 6-dimension scores with confidence and evidence, or suppressions where proof is weak
- primary bottleneck
- recommended next command

### 2) Broad product claim that needs compression

```text
wedge
```

Then describe the product. The coach will force three wedge versions:

- broad
- narrower
- brutally narrow

Expected output:

- wedge scorecard with confidence and cited evidence per axis, or suppressions where proof is weak
- recurrence read
- `Why AI?` check
- keep / narrow / kill / split recommendation

### 3) Buyer and user are blurred

```text
icp
```

Expected output:

- user vs buyer vs champion separation
- explicit exclusions
- narrowest credible beachhead

### 4) The founder wants a full agent

```text
trust
```

Expected output:

- safe for autonomy
- requires review
- human-only
- operating recommendation

### 5) The founder needs the next test

```text
experiment
```

Expected output:

- one hypothesis
- one falsifier
- one owner
- one deadline
- one threshold set
- one decision rule
- automatic state feedback when results are reported

### 6) The founder needs market validation

```text
research
```

Expected output:

- observed facts vs founder assertions vs model inferences
- source types reviewed and whether the threshold was met
- founder claims to validate
- claim verdicts: supported / mixed / contradicted / insufficient evidence
- what the market evidence supports
- what contradicts the story
- substitutes and competitors
- research-backed next move

### 7) The founder wants the hard truth

```text
progress
```

Expected output:

- current six-dimension scoreboard
- value recurrence read
- primary archetype
- coaching posture
- current best thesis
- cohort memory read
- partner briefing
- weekly company status delta
- red-flag memo
- `needs human help now` triggers

---

## Local Repo Mode vs Installed Skill Mode

If you open the repo directly in Codex, use plain commands like:

```text
kickoff
wedge
trust
research
```

If you install it as a session skill with `./install.sh`, use:

```text
$ai-wedge-coach kickoff
$ai-wedge-coach wedge
$ai-wedge-coach trust
$ai-wedge-coach research
```

The behavior is the same. The only difference is whether Codex is reading the repo-local `AGENTS.md` or the installed session skill package.
