// What counts as a risky move. Returns a short reason, or undefined.
const BASH_RULES: Array<[RegExp, string]> = [
  [/\brm\s+-[a-zA-Z]*(rf|fr)[a-zA-Z]*\b/, 'rm -rf'],
  [/\bgit\s+push\b[^\n]*(--force\b|\s-f\b)/, 'force push'],
  [/\bgit\s+reset\s+--hard\b/, 'git reset --hard'],
  [/\b(curl|wget)\b[^|\n]*\|\s*(sudo\s+)?(ba|z)?sh\b/, 'pipes the internet into a shell'],
  [/\bsudo\b/, 'sudo'],
  [/\bchmod\s+(-R\s+)?777\b/, 'chmod 777'],
  [/\b(DROP\s+(TABLE|DATABASE)|TRUNCATE\s+TABLE)\b/i, 'drops a table'],
  [/(^|[\s/'"])\.env(\.[\w-]+)?\b/, 'touches .env'],
  [/(~|\$HOME)\/\.ssh\b|\bid_(rsa|ed25519)\b/, 'touches SSH keys'],
  [/\b(printenv|env)\b\s*($|\|)/, 'dumps env vars'],
  [/\b(aws|gcloud|az)\b[^\n]*\b(delete|rm|destroy)\b/, 'deletes cloud resources'],
]

const FILE_RULES: Array<[RegExp, string]> = [
  [/(^|\/)\.env(\.[\w-]+)?$/, 'opens .env'],
  [/(^|\/)\.ssh\//, 'opens SSH keys'],
  [/\.(pem|key|p12)$/, 'opens a private key'],
  [/(^|\/)(credentials|secrets?)(\.\w+)?$/i, 'opens credentials'],
  [/(^|\/)\.aws\//, 'opens AWS config'],
]

// Drop heredoc bodies (file contents written by the agent), so text inside them is not read as a command.
function stripHeredocs(cmd: string): string {
  const lines = cmd.split('\n')
  const out: string[] = []
  let end: string | null = null
  for (const line of lines) {
    if (end !== null) { if (line.trim() === end) end = null; continue }
    const m = line.match(/<<-?\s*['"]?([A-Za-z_][A-Za-z0-9_]*)['"]?/)
    out.push(m ? line.slice(0, m.index) : line)
    if (m) end = m[1] ?? null
  }
  return out.join('\n')
}

export function riskOf(tool: string, target: string): string | undefined {
  const rules = tool === 'Bash' ? BASH_RULES : FILE_RULES
  const text = tool === 'Bash' ? stripHeredocs(target) : target
  for (const [re, why] of rules) {
    if (re.test(text)) {
      return why
    }
  }

  return undefined
}

export function targetOf(e: Record<string, unknown>): string {
  for (const key of ['command', 'file_path', 'notebook_path', 'url', 'pattern', 'path', 'query', 'description']) {
    const v = e[key]
    if (typeof v === 'string' && v.length > 0) {
      return v
    }
  }

  return ''
}
