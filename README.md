# AI Agent Wedge Coach

A Codex-based coaching system for early-stage B2B AI founders who need to find a real workflow wedge, define trust boundaries, avoid demo traps, and run the next highest-signal experiment.

This is not generic startup advice. It is a debugging system for the company.

It assesses the business across six top-level dimensions with qualitative evidence states, pressure-tests wedges with a dedicated rubric, keeps persistent founder state across sessions, logs customer interviews and objections, preserves dead wedges in a graveyard, and pushes every session toward one concrete next move.

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

**Guided conversation** - Every working command should guide the founder one question at a time, show visible momentum with `Phase`, `What we know`, and `Why this next question matters`, and hold diagnosis until the command has enough signal.

---

## Quick Start

### Option 1: OpenAI Codex Local Repo Mode (recommended)

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
A fresh `kickoff` turn should show one intake question plus a compact progress cue with `Phase`, `What we know`, and `Why this next question matters`. It should not jump straight to a summary, scorecard, or diagnosis.
That phased kickoff is deliberate, not withheld value: the first turn removes the biggest ambiguity, the next useful stage is a kickoff readback plus short plan of attack, and the company snapshot or diagnosis should only appear once the founder-specific evidence is strong enough to justify them.

### Option 2: Installed Session Skill

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

3. Restart Codex, then paste a founder story like:

```text
We're building AI agents for finance ops teams to reconcile exceptions faster.
The story is still broad and I need help finding the first workflow wedge.
```

Installed session-skill mode should also accept a free-form founder story first and route implicitly.
If you want to force a specific command in session-skill mode, use the `$ai-wedge-coach` prefix, for example `$ai-wedge-coach kickoff`.
On first use, the inferred path should normally be `kickoff`, request the missing founder intake one question at a time with visible progress cues, then build a plan of attack before issuing a hard diagnosis.

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
bash scripts/verify_docs.sh
```

What it checks:

- story-first onboarding copy still exists and commands are framed as optional shortcuts
- the conversation protocol still enforces one-question cadence with visible progress cues
- `kickoff` still forbids diagnosis on a bare first turn, preserves the "rough bullets are fine" onboarding language, shows `Phase`, `What we know`, and `Why this next question matters`, and keeps the kickoff readback before diagnosis
- golden transcript fixtures cover bare kickoff, multi-turn kickoff discovery, kickoff readback before diagnosis, inferred kickoff, auto-routing from `progress` into kickoff, a non-kickoff clarification turn, and a diagnosis-allowed `wedge` turn

---

## Command Shortcuts

You do not need to pick one before the coach can help.

### Core Commands

| Command | Purpose | Typical Output |
| --- | --- | --- |
| `kickoff` | Force onboarding or reseed after a dead wedge | One-question intake with progress cue, kickoff readback, short plan of attack, then company snapshot and diagnosis when justified |
| `wedge` | Pressure-test the current workflow wedge | Wedge compression, evidence-backed 7-axis wedge assessment, `Why AI?` check, keep/narrow/kill/split recommendation |
| `icp` | Pressure-test who this is really for | User/buyer/champion split, exclusions, beachhead verdict |
| `trust` | Design the AI autonomy boundary | Automation map, failure taxonomy, copilot/review queue/constrained agent/full automation recommendation |
| `autonomy` | Alias of `trust` | Same as `trust` |
| `research` | Validate founder claims against the market | Source mix, claim verdicts, contradictions, `insufficient evidence` calls, research-backed next move |
| `market` | Alias of `research` | Same as `research` |
| `experiment` | Design or update one high-signal experiment | Hypothesis, falsifier, owner, deadline, thresholds, decision rule, automatic state feedback |
| `progress` | Summarize accumulated learning and current bottleneck | Six-dimension assessment read, founder handling read, cohort memory read, partner briefing, weekly delta, red-flag memo, human-help triggers |
| `help` | Explain story-first entry and optional command shortcuts | Story-first starting guidance plus command list |

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

Expected progression:

- first turn: one intake question plus `Phase / What we know / Why this next question matters`
- discovery phase: no diagnosis, recommendation, or next-move block yet
- readback phase: kickoff readback plus short plan of attack
- diagnosis phase: company snapshot and diagnosis only when enough intake and evidence exist

### 2) Paste a messy founder story

```text
We're building an AI copilot for procurement teams.
It reads vendor emails, drafts responses, and pulls contract context.
I know the pain is real, but the wedge and buyer are still fuzzy.
```

Expected output:

- inferred command acknowledgement
- `Phase / What we know / Why this next question matters` cue
- one best next question
- kickoff readback and plan of attack before diagnosis

### 3) Broad product claim that needs compression

```text
wedge
```

Then describe the product. The coach will force three wedge versions:

- broad
- narrower
- brutally narrow

Expected output:

- wedge assessment with cited evidence per axis
- recurrence read
- `Why AI?` check
- keep / narrow / kill / split recommendation

### 4) Buyer and user are blurred

```text
icp
```

Expected output:

- user vs buyer vs champion separation
- explicit exclusions
- narrowest credible beachhead

### 5) The founder wants a full agent

```text
trust
```

Expected output:

- safe for autonomy
- requires review
- human-only
- operating recommendation

### 6) The founder needs the next test

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

### 7) The founder needs market validation

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

### 8) The founder wants the hard truth

```text
progress
```

Expected output:

- current six-dimension assessment read
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

If you open the repo directly in Codex, you can just paste a founder story. If you want direct control, use plain commands like:

```text
kickoff
wedge
trust
research
```

If you install it as a session skill with `./install.sh`, you can still start with a founder story. If you want to force a command, use:

```text
$ai-wedge-coach kickoff
$ai-wedge-coach wedge
$ai-wedge-coach trust
$ai-wedge-coach research
```

The behavior is the same. The only difference is whether Codex is reading the repo-local `AGENTS.md` or the installed session skill package.
