# Agent radar for Claude Code

See what your agent does while you're not looking.

A mod for Claude Code desktop that opens a live **Agent radar** pane next to the chat:

- every tool call your agent makes, with the file, command or URL it touched
- counters: calls, files, shell commands, alerts, blocked moves, uptime
- red alerts when the agent does something risky: `rm -rf`, force push, `git reset --hard`, `sudo`, `curl | sh`, `chmod 777`, dropping a table, opening `.env`, SSH keys or credentials
- **guard mode** (`/radar-guard`): blocks those moves instead of only flagging them
- a dark neon HUD look with an animated radar backdrop

## Install

In Claude Code, at the prompt:

```
/plugin install agent-radar --marketplace f0rgent/claude-skills-catalog
```

Say `y` to add the marketplace, then pick a scope. The HUD look and animated backdrop show in the Claude Code desktop and mobile apps; the radar pane works everywhere.

## Audit your agent's last 30 days first

Read-only, prints counts only:

```
curl -fsSLo agent-audit.mjs https://raw.githubusercontent.com/f0rgent/claude-skills-catalog/main/tools/agent-audit.mjs && node agent-audit.mjs
```

## Commands

- `/radar` opens the pane
- `/radar-guard` turns guard mode on or off
- `/radar-reset` clears the radar

The rules live in `hooks/risk.ts`. Add your own patterns there.

Made by @f0rgent · https://f0rgent.github.io


