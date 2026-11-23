# Invisible shirt prompt for Claude Code

A shirt print that a person detector stops seeing. Paste into Claude Code on a computer with a webcam. Runs fully local.

No Claude yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).

```
You have my webcam and a Python environment. Goal: design a shirt print that makes an off-the-shelf person detector stop seeing me.

Setup
- Install ultralytics and use YOLOv8n (COCO, class "person") as the detector.
- Capture 20 webcam frames of me standing 2-3 m from the camera, different poses. Save them as the test set.
- Baseline: run the detector on every frame and log the average PERSON confidence.

Loop (max 50 patterns, stop early if avg confidence < 10%)
1. Generate a new seamless print pattern (1024x1024). Start with bold, colourful, organic blobs and high-contrast textures. Each new pattern mutates the best 3 so far.
2. Warp the pattern onto the torso area of every test frame (use the detector's box, top 15-55% of the height), with slight perspective and lighting changes so it looks printed on fabric.
3. Run the detector on all 20 frames. Score = average PERSON confidence (lower is better).
4. Keep the pattern only if it beats the current best. Log pattern id, score, time.

Output
- results.csv with every pattern and its score.
- best_pattern.png at print resolution (4500x5400) for a shirt.
- before_after.mp4: the same frames with green boxes and confidence labels, baseline vs best pattern, side by side.
- A short summary: baseline score, best score, how many patterns, total time.

Rules
- Everything runs locally. Don't upload my frames anywhere.
- Blur every face except mine in any saved image or video.
```

---

Don't have Claude Code yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).
