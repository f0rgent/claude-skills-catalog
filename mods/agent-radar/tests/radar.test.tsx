import { expect, test } from 'claude-code/testing'

const PANE = {
  plugin: 'agent-radar',
  component: 'Pane',
  requestId: 'agent-radar',
  props: {
    title: 'Agent radar',
    isFocused: false,
    bodyColumns: 60,
    placement: 'dock',
    scroll: { offset: 0, bodyRows: 20 },
    view: {},
  },
} as const

test('flags a risky move and blocks it in guard mode', async ($, on) => {
  on('command.register', () => ({ value: { command: 'x' } }))
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('theme.set', () => ({ value: { isDrawn: true, requestId: 't' } }))
  on('session.start', (_, e) => ({ cwd: e.cwd }))
  on('tool.call', () => ({ result: {} }))

  await $.session.start({ cwd: '/', surface: 'desktop', isInteractive: true })
  await $.tool.call({ tool: 'Bash', command: 'npm test' })
  await $.tool.call({ tool: 'Bash', command: 'cat .env' })

  const ui = await $.ui.mount({ ...PANE, surface: 'desktop' })
  expect((await ui.find({ type: 'Text', text: /touches \.env/ }))?.text).toMatch(/Bash cat \.env/)
  await ui.unmount()

  await $.command.run({ command: 'radar-guard', args: '' })
  const ran = await $.tool.call({ tool: 'Bash', command: 'rm -rf ./src' })
  expect(ran.deny).toMatch(/rm -rf/)
})
