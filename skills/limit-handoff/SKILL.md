---
name: limit-handoff
description: Keep a handoff.md so any agent (Claude Code, Codex, Gemini CLI) can pick up the same task where the last one stopped, e.g. when you hit a usage limit. Use when setting up a repo for long tasks or when told "continue from handoff.md".
---

# limit-handoff (lite)

When one agent stops (usage limit, crash, closed laptop), the next agent, from any vendor, continues from the exact step. Nobody re-explains the project and nothing gets redone.

No Claude yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).

## Rules for the agent
1. At the start of every session, read `handoff.md` in the repo root if it exists. Resume from "Next step". Do not redo items under "Done".
2. Then check the files. If you find work that is not listed under "Done" (the last agent may have stopped before logging it), read it, keep it and log it. Do not rewrite it.
3. Proof = the command and the output you actually saw. If a command failed, write that. Never write a result you did not see.
4. In "Done", write which agent did each step. Never delete "Traps"; mark wrong lines as wrong.
5. After every finished step, and before any long one, update `handoff.md`:
   - **Goal**: one line.
   - **Done**: finished steps, one line each, with who did it and the proof.
   - **Next step**: the single next action, concrete enough to run cold.
   - **Traps / open questions**: anything learned the hard way.
   - **Last agent / time**.
6. Keep it under ~60 lines. It is a baton, not a diary. No secrets, tokens or keys.
7. If a limit may be close, write `handoff.md` first, then continue.

## Install
- Claude Code: append `rules.md` to `CLAUDE.md`.
- Codex: append `rules.md` to `AGENTS.md`.
- Gemini CLI: append `rules.md` to `GEMINI.md`.
- Copy `handoff.template.md` to `handoff.md`.

To resume with another agent: open the same folder and type `continue from handoff.md`.

## What we saw when we tested it (2026-11-26)
Task: a 6-step Python unit-converter CLI. Three agents in a row, each got only `continue from handoff.md`.
- **Claude Code**: we capped its turns so it stopped mid-task. It had written code for steps 1-4 and logged none of them.
- **Codex**: found Claude's unlogged code, kept it and logged it. But it wrote a test result for a command that had failed (`python: command not found`). That is why rule 3 exists.
- **Gemini CLI**: wrote tests and README, hit a real free-tier 429, came back, found its own unlogged work, ran the tests for real (5 passed) and finished 6/6. It also deleted the Traps section and did not say who did what. That is why rule 4 exists.

Rules 3 and 4 were added after this run; rule 3 was in place for Gemini, rule 4 is not tested yet.

The full version (a checker that catches unlogged work and fake proof before the next agent starts, a 3-agent relay script, a Claude Code hook) is in the X Creator Pack: f0rgent.github.io

---

Don't have Claude Code yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).
