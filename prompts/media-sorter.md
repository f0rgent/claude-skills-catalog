# Media sorter prompt for Claude Code

Paste into Claude Code, started in (or pointed at) the folder with your photos and videos. Change only the PARAMETERS block.

```
You are sorting my photo and video library into folders. Work only inside SOURCE and DEST.

PARAMETERS
SOURCE      = ~/Pictures/unsorted
DEST        = ~/Pictures/sorted
SORT_BY     = category            # category | location | season | people | date | custom
THEN_BY     = none                # optional second level, same options (e.g. location then season)
CATEGORIES  = auto                # auto, or my list: talking-head, golden-hour, city-night, food, nature, ocean, pets
CUSTOM_RULE = none                # used when SORT_BY = custom, in plain words
MODE        = copy                # copy | move | symlink
MIN_CONFIDENCE = 0.7              # anything below goes to DEST/_review
DRY_RUN     = true                # true = show the plan only, change nothing
LIVE_VIEW   = true                # build a local HTML page that shows the sort as it runs

HOW TO WORK
1. Inventory SOURCE recursively: every image and video, with size, hash, EXIF/metadata (date taken, GPS, camera, lens, duration, resolution, orientation). Save it as DEST/_index.json. Tell me the counts before going further.
2. Make a small preview for each file with local tools only: a downscaled thumbnail for photos, 3 evenly spaced frames for videos (ffmpeg). Never upload my files anywhere.
3. Classify each file according to SORT_BY:
   - category: look at the previews. If CATEGORIES = auto, first look at a 300-file sample, propose 8 to 15 folder names that fit this library, and wait for my OK.
   - location: use GPS from metadata, reverse-geocode offline to country/city. Files without GPS go to _no-location, do not guess from the picture.
   - season: from date taken (ask me which hemisphere once). No date goes to _no-date.
   - people: group similar faces with a local face-clustering library into person-01, person-02, and so on. Do not try to identify anyone. Show me one contact sheet per group so I can name the folders myself. No faces goes to _no-people, several people goes to _groups.
   - date: YYYY/MM folders.
   - custom: follow CUSTOM_RULE.
   Record a confidence for every decision. Below MIN_CONFIDENCE the file goes to _review.
4. Show me the plan as a table: folder, file count, 5 example files, plus the _review count. If DRY_RUN = true, stop here.
5. After my OK, apply it with MODE. Never delete anything. Never overwrite: on a name clash add a numeric suffix. Exact duplicates (same hash) go to _duplicates and are listed, not removed.
6. Write DEST/_manifest.csv (original path, new path, reason, confidence) and DEST/undo.sh that restores everything.
7. If LIVE_VIEW = true, write DEST/_live.html: a dark grid of all thumbnails that fly into labeled folder boxes as files are placed, with a counter (placed / to review / elapsed). It reads a progress JSON you keep updating.
8. Finish with a short report: counts per folder, what went to _review and why, anything you could not read.

RULES
- Batch the work and checkpoint to _index.json so a crash or a stop can resume without redoing files.
- Do not rename original files unless I ask.
- If something is ambiguous, ask me once with a concrete suggestion, then continue.
```

## Other things you can sort by (put into SORT_BY or CUSTOM_RULE)

- b-roll use: talking head, establishing shot, close-up detail, hands at work, screen recording, transition filler
- time of day and light: golden hour, blue hour, night, harsh noon, indoor
- orientation and format: vertical 9:16 for Reels/Shorts, horizontal 16:9, square
- quality: sharp vs blurry, shaky, overexposed, best shot out of each burst
- video specs: duration buckets (under 5s, 5 to 15s, long), resolution, frame rate (slow-mo ready)
- event or trip: auto-group by gaps in time plus location ("Lisbon, May 2026")
- content type: screenshots, documents and receipts, memes, selfies, real photos
- camera or device: phone, drone, action cam, mirrorless
- color and mood: warm, cold, dark, bright, dominant color
- has speech or not (videos), language spoken, music vs silence
- text on screen: signs, slides, whiteboards (searchable by the text)
- motion: static, pan, drone flyover, fast action
- duplicates and near-duplicates, kept vs rejected
- ready to post vs raw: already edited/exported files vs originals
