export type RadarEvent = {
  id: string
  at: number
  tool: string
  target: string
  risk?: string
  blocked?: boolean
  isDone: boolean
  isError?: boolean
}

export type RadarStats = {
  startedAt: number
  calls: number
  bash: number
  alerts: number
  blocked: number
  files: string[]
}

declare module 'claude-code' {
  interface PluginState {
    'agent-radar': {
      events: Shaped<RadarEvent[]>
      stats: Shaped<RadarStats>
      guard: Shaped<boolean>
    }
  }
}
