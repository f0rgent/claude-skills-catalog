---
name: tail-check
description: Check whether a phone or car is following you, using the open-source Chasing Your Tail tool on a Raspberry Pi. Walks through passive setup, reads the logs, builds per-device timelines across places, and writes a timestamped report for a lawyer or the police. Use when someone thinks they are being followed or surveilled.
---

# tail-check

Prove you're being followed, or rule it out, with logs instead of a gut feeling.

The tool is not ours. It's **Chasing Your Tail** by Matt Edmondson, a former Homeland Security agent, shown at Black Hat USA 2022:
- original: https://github.com/azmatt/chasing_your_tail
- maintained version (NG): https://github.com/ArgeliusLabs/Chasing-Your-Tail-NG (MIT)

This skill is the agent side: setup, log analysis and the report.

## What you need
- A Linux box you can keep in the car (a Raspberry Pi works) with a power source
- A Wi-Fi adapter that supports monitor mode
- Kismet and Python 3
- Optional: a GPS source, so each sighting gets a place

## Rules
- Passive logging only. Never connect to, probe, deauth or interfere with anyone's device.
- Use it to protect yourself, never to track someone. Check the laws where you live.
- If nothing looks suspicious, say so. Don't guess dramatically.

## Steps

1. **Setup.** Walk the user through installing Chasing Your Tail NG with Kismet and the monitor-mode adapter, step by step. Confirm logging works before they drive anywhere.
2. **Collect.** Have them run it for several days across normal routes (home, work, school, stores). Each sighting needs a time and, if GPS is on, a place.
3. **Find repeats.** When they upload the logs, list every device seen near them in 3 or more different places. Ignore their own devices (ask for their phone, watch, earbuds, car).
4. **Timeline.** For each repeat device: where, when, how long, how close (signal strength).
5. **Saved networks.** List the Wi-Fi network names each repeat device asked for (probe requests) and say what they might suggest. Treat names as hints, not proof.
6. **Weak spots.** Flag matches that rely on randomized MAC addresses, short sightings or busy places (malls, highways). Say how much each one weakens the case.
7. **Report.** Write a clean, timestamped report the user can hand to a lawyer or the police:
   - summary in 3 lines
   - table: device, sightings, places, first/last seen, saved networks
   - map or list of places per device
   - a section "What this data cannot prove"

## Copy-paste prompt (any chat model)

```
I think I'm being followed. Help me prove it or rule it out.

1. Walk me through setting up Chasing Your Tail NG (github.com/ArgeliusLabs/Chasing-Your-Tail-NG) on a Raspberry Pi in my car, step by step. Passive logging only, nothing that connects to or interferes with anyone's device
2. When I upload the logs, find every device seen near me in 3+ different places
3. For each one, build a timeline: where, when, how long, how close
4. List the Wi-Fi networks those devices have saved and tell me what they suggest
5. Turn it into a clean, timestamped evidence report I can hand to my lawyer

If nothing looks suspicious, say so. Don't guess dramatically.
```

## Limits
- Most modern phones randomize their Wi-Fi MAC, so one device can look like several. Strong cases need many sightings in many places.
- Many phones no longer broadcast the names of saved networks.
- Logs give a lawyer questions to ask. They are not automatic evidence.
