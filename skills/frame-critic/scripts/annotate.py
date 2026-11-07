#!/usr/bin/env python3
"""Burn a critique onto stills: score badge, red boxes on bugs, one-line note.

Usage:
  annotate.py critique.json OUT_DIR

critique.json:
{
  "frames": [
    {"image": "stills/f0252.jpg", "label": "#4 f252",
     "scores": {"hook": null, "read": 7, "comp": 3, "motion": 7, "bugs": 2},
     "boxes": [[0.30, 0.0, 1.0, 0.22]],          # x0,y0,x1,y1 as 0..1 of the frame
     "note": "FINE stamp covers a third of the frame"}
  ]
}
The overall score is the lowest non-null score (one bad axis sinks the frame).
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

def font(size):
    for f in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
              "C:/Windows/Fonts/arialbd.ttf"]:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()

def overall(s):
    v = [x for x in s.values() if x is not None]
    return min(v) if v else None

def color(x):
    return "#2fbf71" if x >= 8 else "#f2b632" if x >= 6 else "#e5484d"

def main():
    spec = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
    base = os.path.dirname(os.path.abspath(sys.argv[1]))
    for fr in spec["frames"]:
        im = Image.open(os.path.join(base, fr["image"])).convert("RGB"); W, H = im.size
        d = ImageDraw.Draw(im); u = W / 1080
        for b in fr.get("boxes", []):
            x0, y0, x1, y1 = b[0]*W, b[1]*H, b[2]*W, b[3]*H
            for k in range(int(8*u)):
                d.rectangle([x0+k, y0+k, x1-k, y1-k], outline="#e5484d")
        sc = overall(fr["scores"])
        if sc is not None:
            r = int(95*u); cx, cy = W - r - int(30*u), r + int(30*u)
            d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color(sc), outline="#111", width=int(6*u))
            t = f"{sc}"; f1 = font(int(92*u)); w = d.textlength(t, font=f1)
            d.text((cx - w/2, cy - 58*u), t, fill="#111", font=f1)
            f2 = font(int(28*u)); w2 = d.textlength("/10", font=f2)
            d.text((cx - w2/2, cy + 40*u), "/10", fill="#111", font=f2)
        if fr.get("note"):
            f3 = font(int(40*u)); pad = int(24*u)
            words, lines, cur = fr["note"].split(), [], ""
            for wd in words:
                t = (cur + " " + wd).strip()
                if d.textlength(t, font=f3) > W - 2*pad - 40*u: lines.append(cur); cur = wd
                else: cur = t
            lines.append(cur)
            hbox = len(lines) * int(52*u) + 2*pad; y = int(250*u)
            d.rounded_rectangle([pad, y, W - pad, y + hbox], radius=int(20*u), fill="#111111e6")
            for i, ln in enumerate(lines):
                d.text((2*pad, y + pad + i*int(52*u)), ln, fill="#fff", font=f3)
        if fr.get("label"):
            d.text((int(30*u), int(30*u)), fr["label"], fill="#fff", font=font(int(36*u)), stroke_width=int(4*u), stroke_fill="#111")
        im.save(os.path.join(out, os.path.basename(fr["image"])), quality=92)
        print(fr["image"], sc)

if __name__ == "__main__":
    main()
