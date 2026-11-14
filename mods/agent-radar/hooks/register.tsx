import { atom, read, update } from 'claude-code'
import type { Register, ThemeSetArgs } from 'claude-code'

import type { RadarEvent, RadarStats } from '../types'
import { makeColors } from './make-colors.js'
import { riskOf, targetOf } from './risk'
import { SCENE } from './scene'

const PANE = 'agent-radar'
const TITLE = 'Agent radar'
const FILE_TOOLS = new Set(['Read', 'Edit', 'Write', 'NotebookEdit', 'MultiEdit'])

const events = atom({ plugin: 'agent-radar', key: 'events' } as const, [], { shape: 'events-1' })
const fresh = (): RadarStats => ({ startedAt: Date.now(), calls: 0, bash: 0, alerts: 0, blocked: 0, files: [] })
const stats = atom({ plugin: 'agent-radar', key: 'stats' } as const, fresh(), { shape: 'stats-1' })
const guard = atom({ plugin: 'agent-radar', key: 'guard' } as const, false, { shape: 'guard-1' })

// Dark neon HUD: teal-tinted near-black surfaces, teal accent.
const { theme, problems } = makeColors({
  label: 'f0rgent HUD',
  only: 'dark',
  roles: { accent: '#2ee6c5', danger: '#ff4d6d', success: '#5cf08a', warning: '#ffc247', pro: '#b38cff' },
  dark: {
    gray: {
      anchors: {
        'surface-0': '#070e10',
        'surface-1': '#0b1619',
        'surface-2': '#0f1d21',
        'surface-3': '#132428',
        'text-primary': '#e6fffa',
        'text-secondary': '#a9d6cf',
        'text-muted': '#7fa9a2',
      },
    },
  },
})

const LOOK: ThemeSetArgs = {
  colors: theme,
  backdrop: { scene: 'f0rgent-hud', glass: { blur: 18, tint: '#070e10', opacity: 0.62 } },
}

const clip = (s: string, n: number) => (s.length > n ? `${s.slice(0, n - 1)}…` : s)
const clock = (ms: number) => {
  const s = Math.max(0, Math.floor(ms / 1000))
  const h = Math.floor(s / 3600)
  const m = Math.floor((s % 3600) / 60)
  const pad = (x: number) => String(x).padStart(2, '0')

  return `${h > 0 ? `${h}:` : ''}${pad(m)}:${pad(s % 60)}`
}
const stamp = (t: number) => {
  const d = new Date(t)
  const pad = (x: number) => String(x).padStart(2, '0')

  return `${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    const unpainted = problems.find(line => line.startsWith("Desktop won't paint"))
    if (unpainted !== undefined) {
      $.ui.toast(unpainted)
    }
    await $.theme.set(LOOK)

    await $.command.register({ name: 'radar', description: 'Open the agent radar pane' })
    await $.command.register({ name: 'radar-guard', description: 'Turn guard mode on or off (blocks risky agent moves)' })
    await $.command.register({ name: 'radar-reset', description: 'Clear the agent radar' })
    void $.ui.open({ id: PANE, title: TITLE })

    return next(e)
  })

  on('command.run', { command: 'radar' }, async $ => {
    await $.ui.open({ id: PANE, title: TITLE })

    return { text: 'Agent radar is on.' }
  })

  on('command.run', { command: 'radar-guard' }, async $ => {
    let isOn = false
    await update($, guard, was => {
      isOn = !was

      return isOn
    })

    return {
      text: isOn
        ? 'Guard ON: rm -rf, force push, sudo, .env and key files will be blocked.'
        : 'Guard OFF: risky moves are flagged, not blocked.',
    }
  })

  on('command.run', { command: 'radar-reset' }, async $ => {
    await update($, events, () => [])
    await update($, stats, () => fresh())

    return { text: 'Radar cleared.' }
  })

  on('tool.call', async ($, e, next) => {
    const target = targetOf(e as unknown as Record<string, unknown>)
    const risk = riskOf(e.tool, target)
    const isGuarded = risk !== undefined && (await read($, guard))
    const ev: RadarEvent = {
      id: e.tool_use_id ?? `${Date.now()}-${Math.random()}`,
      at: Date.now(),
      tool: e.tool,
      target,
      risk,
      blocked: isGuarded,
      isDone: isGuarded,
    }

    await update($, events, list => [...list, ev].slice(-300))
    await update($, stats, s => ({
      ...s,
      calls: s.calls + 1,
      bash: s.bash + (e.tool === 'Bash' ? 1 : 0),
      alerts: s.alerts + (risk !== undefined ? 1 : 0),
      blocked: s.blocked + (isGuarded ? 1 : 0),
      files:
        FILE_TOOLS.has(e.tool) && target !== '' && !s.files.includes(target)
          ? [...s.files, target].slice(-500)
          : s.files,
    }))

    if (risk !== undefined) {
      $.ui.toast(isGuarded ? `Radar blocked: ${risk}` : `Radar: agent ${risk}`)
    }
    if (isGuarded) {
      return { deny: `Agent radar guard blocked this (${risk}). Ask the user to run /radar-guard to allow it.` }
    }

    const ran = await next(e)
    await update($, events, list =>
      list.map(one => (one.id === ev.id ? { ...one, isDone: true, isError: ran.isError === true } : one)),
    )
    const s = await read($, stats)
    $.ui.status(`radar ${s.calls} calls · ${s.alerts} alerts`)

    return ran
  }).catch(($, e, next) => (next.called ? undefined : next(e)))

  on('ui.render', { component: 'Backdrop' }, ($, e, next) => {
    if (e.surface !== 'desktop' && e.surface !== 'mobile') {
      return next(e)
    }
    if (e.props.scene !== 'f0rgent-hud') {
      return next(e)
    }
    const { Svg } = $.ui.resolve(e)

    return <Svg source={SCENE} alt="Dark teal HUD grid with a radar sweep and a slow scan line" />
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text } = $.ui.resolve(e)
    const list = await read($, events)
    const s = await read($, stats)
    const isOn = await read($, guard)
    const room = Math.max(3, (e.viewport?.rows ?? 30) - 9)
    const width = Math.max(24, (e.viewport?.columns ?? 60) - 22)
    const live = list.filter(one => !one.isDone).length

    return (
      <Box flexDirection="column">
        <Text bold color="#2ee6c5">◉ AGENT RADAR {live > 0 ? '· LIVE' : '· IDLE'}</Text>
        <Text dimColor>
          UPTIME {clock(Date.now() - s.startedAt)} · GUARD {isOn ? 'ON' : 'OFF'}
        </Text>
        <Text>
          <Text color="#2ee6c5">{s.calls}</Text> calls  <Text color="#36c2ff">{s.files.length}</Text> files  <Text color="#ffc247">{s.bash}</Text> cmds  <Text color="#ff4d6d">{s.alerts}</Text> alerts  <Text color="#b38cff">{s.blocked}</Text> blocked
        </Text>
        <Text dimColor>────────────────────────────</Text>
        {list.length === 0 && <Text dimColor>Waiting for your agent to move…</Text>}
        {list.slice(-room).map(one => (
          <Text color={one.risk !== undefined ? '#ff4d6d' : one.isError === true ? '#ffc247' : undefined} dimColor={one.isDone && one.risk === undefined}>
            {stamp(one.at)} {one.blocked === true ? '⛔' : one.risk !== undefined ? '⚠' : one.isDone ? '·' : '▶'} {clip(one.tool, 10)} {clip(one.target.replace(/\s+/g, ' '), width)}{one.risk !== undefined ? `  [${one.risk}]` : ''}
          </Text>
        ))}
      </Box>
    )
  })
}
