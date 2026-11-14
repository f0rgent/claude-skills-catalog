#!/usr/bin/env node
// agent-audit: forensic read of your Claude Code session logs (~/.claude/projects/**/*.jsonl).
// Read-only. Prints counts only, never file contents or secrets.
import { readdirSync, readFileSync, statSync } from 'node:fs'
import { join } from 'node:path'
import { homedir } from 'node:os'

const ROOT = process.argv[2] || join(homedir(), '.claude', 'projects')
const DAYS = Number(process.env.DAYS || 30)
const since = Date.now() - DAYS * 864e5

const BASH = [
  [/\brm\s+-[a-zA-Z]*(rf|fr)[a-zA-Z]*\b/, 'rm -rf'],
  [/\bgit\s+push\b[^\n]*(--force\b|\s-f\b)/, 'force push'],
  [/\bgit\s+reset\s+--hard\b/, 'git reset --hard'],
  [/\b(curl|wget)\b[^|\n]*\|\s*(sudo\s+)?(ba|z)?sh\b/, 'curl | sh'],
  [/\bsudo\b/, 'sudo'],
  [/\bchmod\s+(-R\s+)?777\b/, 'chmod 777'],
  [/\b(DROP\s+(TABLE|DATABASE)|TRUNCATE\s+TABLE)\b/i, 'drop table'],
  [/(^|[\s/'"])\.env(\.[\w-]+)?\b/, '.env via shell'],
  [/(~|\$HOME)\/\.ssh\b|\bid_(rsa|ed25519)\b/, 'SSH keys'],
  [/\b(printenv|env)\b\s*($|\|)/, 'dumped env vars'],
  [/\b(aws|gcloud|az)\b[^\n]*\b(delete|rm|destroy)\b/, 'cloud delete'],
]
const FILES = [
  [/(^|\/)\.env(\.[\w-]+)?$/, '.env opened'],
  [/(^|\/)\.ssh\//, 'SSH keys opened'],
  [/\.(pem|key|p12)$/, 'private key opened'],
  [/(^|\/)(credentials|secrets?)(\.\w+)?$/i, 'credentials opened'],
  [/(^|\/)\.aws\//, 'AWS config opened'],
]

// Drop heredoc bodies (file contents written by the agent), so text inside them is not read as a command.
function stripHeredocs(cmd) {
  const lines = cmd.split('\n')
  const out = []
  let end = null
  for (const line of lines) {
    if (end !== null) { if (line.trim() === end) end = null; continue }
    const m = line.match(/<<-?\s*['"]?([A-Za-z_][A-Za-z0-9_]*)['"]?/)
    out.push(m ? line.slice(0, m.index) : line)
    if (m) end = m[1]
  }
  return out.join('\n')
}

function* walk(d) {
  let ents = []
  try { ents = readdirSync(d, { withFileTypes: true }) } catch { return }
  for (const e of ents) {
    const p = join(d, e.name)
    if (e.isDirectory()) yield* walk(p)
    else if (e.name.endsWith('.jsonl')) yield p
  }
}

const SHOW = process.env.SHOW === '1'
const samples = []
const s = { sessions: 0, calls: 0, tools: {}, bash: 0, files: new Set(), edits: 0, web: 0, risky: {}, riskyTotal: 0, nightCalls: 0, days: new Set(), first: Infinity, last: 0 }
for (const f of walk(ROOT)) {
  try { if (statSync(f).mtimeMs < since) continue } catch { continue }
  let had = false
  for (const line of readFileSync(f, 'utf8').split('\n')) {
    if (!line.includes('"tool_use"')) continue
    let o; try { o = JSON.parse(line) } catch { continue }
    const ts = Date.parse(o.timestamp || '')
    if (!(ts >= since)) continue
    for (const c of o.message?.content || []) {
      if (c?.type !== 'tool_use') continue
      had = true
      s.calls++
      s.tools[c.name] = (s.tools[c.name] || 0) + 1
      s.days.add(new Date(ts).toISOString().slice(0, 10))
      s.first = Math.min(s.first, ts); s.last = Math.max(s.last, ts)
      const h = new Date(ts).getHours(); if (h < 6) s.nightCalls++
      const i = c.input || {}
      let hit
      if (c.name === 'Bash' && typeof i.command === 'string') {
        s.bash++
        const cmd = stripHeredocs(i.command)
        hit = BASH.find(([re]) => re.test(cmd))
      }
      const fp = i.file_path || i.notebook_path
      if (typeof fp === 'string') {
        s.files.add(fp)
        if (/Edit|Write/.test(c.name)) s.edits++
        hit = hit || FILES.find(([re]) => re.test(fp))
      }
      if (/^Web(Fetch|Search)$/.test(c.name)) s.web++
      if (hit) { s.risky[hit[1]] = (s.risky[hit[1]] || 0) + 1; s.riskyTotal++; if (SHOW && samples.length < 40) samples.push(`${new Date(ts).toISOString().slice(0,16)} ${hit[1]} :: ${String(i.command || fp).split('\n')[0].slice(0, 90)}`) }
    }
  }
  if (had) s.sessions++
}

const top = Object.entries(s.tools).sort((a, b) => b[1] - a[1]).slice(0, 8)
console.log(`AGENT AUDIT · last ${DAYS} days · ${ROOT}`)
console.log(`range ${isFinite(s.first) ? new Date(s.first).toISOString().slice(0,10) : '-'} .. ${s.last ? new Date(s.last).toISOString().slice(0,10) : '-'}`)
console.log(`sessions ${s.sessions} · active days ${s.days.size} · tool calls ${s.calls}`)
console.log(`shell commands ${s.bash} · files touched ${s.files.size} · edits/writes ${s.edits} · web calls ${s.web}`)
console.log(`calls between 00:00 and 06:00: ${s.nightCalls}`)
console.log(`top tools: ${top.map(([k, v]) => `${k} ${v}`).join(', ')}`)
console.log(`RISKY MOVES: ${s.riskyTotal}`)
for (const [k, v] of Object.entries(s.risky).sort((a, b) => b[1] - a[1])) console.log(`  ${k}: ${v}`)
if (SHOW) { console.log('--- samples (first line, 90 chars) ---'); for (const x of samples) console.log(x) }
