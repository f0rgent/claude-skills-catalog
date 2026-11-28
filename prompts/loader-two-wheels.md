# 5-tonne loader on two wheels: Fable 5.2 prompt for Claude Code

One prompt that makes Fable 5.2 build a browser simulator of a 5-tonne skid-steer loader, then train an AI from scratch to pop it up and balance it on the rear or the front wheels, drive 20 m, take a hard shove and land soft. No balance rule is written by hand. Everything (physics, learning, tests) lives in one HTML file. Inspired by the ETH Zurich Robotic Systems Lab "Heavy Metal Acrobatics" paper (Science Robotics, 2026).

No Claude yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).

Paste into Claude Code and pick Fable 5.2:

```
Build a single-file browser simulation (index.html, no build step, plain JS + canvas) of a 5-tonne skid-steer loader that learns to drive balanced on two wheels, both ways, like the ETH Zurich "Heavy Metal Acrobatics" paper (Science Robotics, Nov 2026).

Physics:
- 2D side view. Chassis + lift arm + bucket as rigid bodies, real-ish numbers: 5,000 kg total, wheelbase ~1.1 m, gravity 9.81.
- Two balance modes:
  1. REAR wheels only (front lifted, a wheelie).
  2. FRONT wheels only (rear lifted, nose down, the lift arm and bucket shift the weight forward).
- Safety catches like the real machine: a rear wheelie bar, and small wheels on the bucket that touch the ground if it tips too far forward.
- Controls: wheel torque (forward/back) and lift-arm angle. Both have a delay and limited rate, because the real machine is hydraulic and slow.

Learning:
- Train a small policy from scratch in the browser (PPO or a simple evolution strategy, your choice, explain why). Inputs: pitch, pitch rate, wheel speed, arm angle, last action, target mode and target speed. No hand-written balance rule.
- Skills to learn: pop up onto the rear wheels, pop up onto the front wheels, hold either balance while driving forward and backward at a commanded speed, and come back down to four wheels softly.
- Randomize mass, center of mass and arm position each episode so it does not overfit.
- Show live: episode number, current mode (REAR / FRONT / 4 WHEELS), best balance time per mode, current pitch.

Test:
- After training, run 20 test episodes with new random settings: 10 on the rear wheels, 10 on the front wheels. Each one: pop up, drive 20 m on two wheels, land. Print how many succeeded per mode and the pitch range (± degrees).
- One combo run: rear wheels, drive forward, land, then front wheels, drive back, land.
- One push test: a hard forward-and-back shove mid-balance. Does it recover?

At the end, write a short honest report: what worked, what failed (per mode), how many training episodes it took, wall-clock time, and how this differs from the real paper.
```

Our run: 1,036,800 practice runs in about 7 minutes, then 16 of 20 test machines it never saw (9/10 rear, 7/10 front). Your numbers will differ.

Credit: the real machine and the method are ETH Zurich's. This is a simulation, not a controller for a real loader.

---

Don't have Claude Code yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).
