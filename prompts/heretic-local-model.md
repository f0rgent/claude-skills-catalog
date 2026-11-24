# Heretic setup prompt for Claude Code

Changes how an open model you already run locally behaves, without retraining: less slop, less sycophancy, shorter answers, fewer refusals, and more. Uses [p-e-w/heretic](https://github.com/p-e-w/heretic) (AGPL-3.0). Idea and the "check KL" tip via [@0xCodila](https://x.com/0xCodila/status/2124927759310848452).

Paste into Claude Code on the machine with the GPU. Change only the PARAMETERS block.

No Claude yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).

```
You are setting up Heretic (github.com/p-e-w/heretic) on my machine to modify one open-weight model I run locally.

PARAMETERS
MODEL     = ask             # a Hugging Face id (e.g. Qwen/Qwen3-4B-Instruct-2507), a model I already run in Ollama / LM Studio, or "ask"
GOAL      = ask             # noslop | nosyco | terse | nohumor | emotions | refusals | ask
RUNTIME   = ollama          # ollama | lmstudio | none (just save the folder)
WORKDIR   = ~/heretic-runs

HOW TO WORK
1. Read the Heretic README and the config file for GOAL before doing anything. Use only the commands the README documents. Never invent flags.
2. Check my hardware: GPU, VRAM, RAM, free disk, Python and PyTorch versions. If MODEL = ask, suggest 3 models that fit my VRAM, with size and why, and wait for my pick.
3. If GOAL = ask, explain each config in one line (what it changes, what it can break) and wait for my pick.
4. Make a fresh Python 3.10+ venv in WORKDIR, install PyTorch for my hardware, then `pip install -U heretic-llm`. Show me what you installed.
5. Put the chosen config in WORKDIR as config.toml (or point HERETIC_CONFIG_FILE at it). Tell me the expected run time from the README before starting (a 4B model is about 30 to 45 minutes on a strong GPU).
6. Start `heretic <MODEL>` in a new terminal window so I can watch it. Do not touch other files on my machine.

PICKING THE RESULT
7. When the trials finish, show the candidates as a table: score for GOAL, KL divergence, and anything else Heretic reports.
8. Recommend one. Do not just take the best GOAL score: the lower the KL, the less the model got dumber. Prefer a row that is close to the best score with a much lower KL, and say why.
9. Let me test it in Heretic's chat first. Wait until I type "saved".

INSTALL
10. Save the chosen model in WORKDIR. If RUNTIME = ollama, convert and import it with a clear name (e.g. qwen3-4b-noslop) and show me `ollama run <name>`. If lmstudio, put it where LM Studio finds it.
11. Never upload the model anywhere (no Hugging Face push) unless I ask.
12. Write WORKDIR/README.md: model, goal, chosen row with its numbers, date, how to run it, how to delete it.

RULES
- Only open-weight models I already have the right to run. Keep the original model's license with the new one.
- The modified model is mine to use responsibly. If GOAL = refusals, remind me once that it will also answer things the original would refuse, and that I am responsible for how it is used.
- Everything stays local.
```

Don't have Claude Code yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).
