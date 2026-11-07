---
name: frame-critic
description: Watch a rendered video like a director before you ship it. Builds a contact sheet, scores every sampled frame out of 10 and boxes the bugs (cropped text, overlapping captions, covered subjects). Use after rendering any AI-made video, cartoon, or motion graphic.
---

# frame-critic (lite)

The model that writes your animation code never sees the result. This skill makes it look.

## Steps

1. Make a contact sheet of the render:
   `python3 scripts/contact_sheet.py out/video.mp4 review/sheet.jpg --n 12 --cols 4`
   (a folder of stills works too; it samples 12 evenly)
2. Open `review/sheet.jpg` and look at every cell. For each frame give 1–10 on:
   - **hook**: first frame only. Would a stranger stop scrolling? Is there text that says what this is?
   - **read**: can every word be read on a phone in one second? Nothing stacked, nothing cut off.
   - **comp**: is the subject in frame and not covered by a caption, a character or a sticker?
   - **bugs**: anything cropped, overlapping, glitched, misspelled or in the wrong place.
   The frame's score is its lowest axis. One bad axis sinks the frame.
3. Write `review/critique.json` (format in `scripts/annotate.py`) with a box around each bug as 0..1 coordinates and a one-line note.
4. Burn the critique onto the stills:
   `python3 scripts/annotate.py review/critique.json review/annotated`
5. Report the worst three frames first, each with frame number, timestamp, score and the exact fix.

## Rules

- Score what is on screen, not what the code intended.
- Be specific: "caption covers the moth's head at 12.7s", never "improve composition".
- A video ships only when no frame is below 7.

The full version (automatic fix loop until every frame is 8+, format presets for Shorts, Reels and X, before/after reports) is in the X Creator Pack: f0rgent.github.io
