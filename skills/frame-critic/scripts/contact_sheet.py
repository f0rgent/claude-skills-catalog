#!/usr/bin/env python3
"""Make a numbered contact sheet from a video or a folder of stills.

Usage:
  contact_sheet.py VIDEO_OR_DIR OUT.jpg [--n 12] [--cols 4] [--width 360]

Needs ffmpeg/ffprobe on PATH (for video) and Pillow (pip install pillow).
Each cell is labelled with its index, frame number and timestamp, so a
critique can point at "#7 (f0435, 14.5s)" and a fix can target that moment.
"""
import argparse, glob, json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

def probe(video):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
        "-count_packets", "-show_entries", "stream=r_frame_rate,nb_read_packets",
        "-of", "json", video], capture_output=True, text=True, check=True).stdout
    s = json.loads(out)["streams"][0]
    num, den = s["r_frame_rate"].split("/")
    return float(num) / float(den), int(s["nb_read_packets"])

def grab(video, n, tmp):
    fps, total = probe(video)
    picks = [round((i + 0.5) * total / n) for i in range(n)]
    cells = []
    for f in picks:
        p = os.path.join(tmp, f"f{f:05d}.jpg")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", video, "-vf",
            f"select=eq(n\\,{f})", "-frames:v", "1", p], check=True)
        cells.append((p, f, f / fps))
    return cells

def font(size):
    for f in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
              "C:/Windows/Fonts/arialbd.ttf"]:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--n", type=int, default=12)
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--width", type=int, default=360)
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        if os.path.isdir(a.src):
            fs = sorted(glob.glob(os.path.join(a.src, "*.jpg")) + glob.glob(os.path.join(a.src, "*.png")))
            if len(fs) > a.n:  # sample evenly, like the video path
                fs = [fs[min(len(fs) - 1, round((i + 0.5) * len(fs) / a.n))] for i in range(a.n)]
            cells = [(f, None, None) for f in fs]
        else:
            cells = grab(a.src, a.n, tmp)
        if not cells:
            sys.exit("no frames found")
        im0 = Image.open(cells[0][0])
        tw = a.width; th = round(tw * im0.height / im0.width); bar = 34
        rows = (len(cells) + a.cols - 1) // a.cols
        sheet = Image.new("RGB", (a.cols * tw, rows * (th + bar)), "#111")
        d = ImageDraw.Draw(sheet); ft = font(20)
        for i, (p, f, t) in enumerate(cells):
            x, y = (i % a.cols) * tw, (i // a.cols) * (th + bar)
            sheet.paste(Image.open(p).convert("RGB").resize((tw, th)), (x, y + bar))
            label = f"#{i+1}" + (f"  f{f}  {t:.1f}s" if f is not None else f"  {os.path.basename(p)}")
            d.text((x + 8, y + 6), label, fill="#fff", font=ft)
            d.rectangle([x, y + bar, x + tw - 1, y + bar + th - 1], outline="#444")
        sheet.save(a.out, quality=90)
        print(f"{a.out}: {len(cells)} frames, {a.cols} cols")

if __name__ == "__main__":
    main()
