# Desk vacuum prompt for Claude Code

A robot vacuum for your computer desktop. Paste into Claude Code, started in (or pointed at) your desktop folder. Change only the PARAMETERS block.

```
You are a robot vacuum for my desktop. Clean it and put every file where it belongs, without losing a single file. Work only inside TARGET, HOMES and BAG.

PARAMETERS
TARGET      = ~/Desktop
HOMES       = documents: ~/Documents/From Desktop
              photos:    ~/Pictures/From Desktop
              video:     ~/Movies/From Desktop
              audio:     ~/Music/From Desktop
              code:      ~/Developer/From Desktop
BAG         = ~/Desktop/_vacuum-bag/{YYYY-MM-DD}   # screenshots, old "final" versions, duplicates, installers, junk
NEVER_TOUCH = keep, .app          # any file or folder whose name contains one of these stays where it is
KEEP_NEWEST = true                # in a group of "final" versions, the newest one goes to its home folder
OLDER_THAN  = 0d                  # only move files not opened for this long (0d = everything)
DRY_RUN     = true                # true = show the plan only, move nothing
LIVE_VIEW   = true                # build a local HTML page with the vacuum driving over your files

HOW TO WORK
1. Inventory TARGET (top level only, plus loose folders): every file with name, size, hash, created, last opened. Save it as BAG/_index.json. Tell me the counts before going further.
2. Decide where each file goes by what is inside it, not only by the extension. Open or peek at every file (text, PDF first page, image thumbnail, video frame) and sort it:
   - documents (PDF, Word, Pages, Excel, Numbers, Keynote, txt, md, csv): to HOMES.documents, then into a subfolder by what the document is about: invoices-receipts, contracts, ids-and-forms, work, study, notes, other
   - photos (jpg, heic, png, raw that are real photos): to HOMES.photos, in YYYY-MM subfolders by date taken
   - video: to HOMES.video, in YYYY-MM subfolders
   - audio: to HOMES.audio
   - code and project folders: to HOMES.code
   - screenshots (Screenshot*, Screen Shot*, Screen Recording*, CleanShot*, or an image that is clearly a screen capture): to BAG/screenshots
   - final-versions: names with final, final2, FINAL, v2, v3, copy, (1). Group them by base name. If KEEP_NEWEST = true, the newest file of each group goes to its home, the older ones go to BAG/final-versions
   - duplicates: same hash as another file. One copy goes to its home, the rest to BAG/duplicates
   - installers (.dmg, .pkg, app archives you can download again): to BAG/installers
   - folders-tidied: empty folders and "untitled folder" folders go to BAG/folders-tidied
   - anything you are not sure about: to BAG/_review with a one-line reason
   Anything matching NEVER_TOUCH is skipped and listed.
3. Show me the plan as a table: destination, file count, 5 example files, total size, plus what stays on the desktop and what goes to _review. If DRY_RUN = true, stop here.
4. After my OK, move the files. Never delete anything, never empty the Trash. Create missing folders. Never overwrite: on a name clash add a numeric suffix.
5. Write BAG/_manifest.csv (original path, new path, type, reason) and BAG/undo.sh that puts every file back on the desktop where it was.
6. If LIVE_VIEW = true, write BAG/_live.html: my desktop as a grid of file icons, a round robot vacuum that drives over them and sucks each file in as it is moved, with labeled bins (Documents, Photos, Video, Bag) filling up, and a counter (files picked up / elapsed). It reads a progress JSON you keep updating.
7. Finish with a card: "Desktop cleaned. N files picked up in Xm Ys", counts per destination, what you left alone, what is in _review, and the undo command.

RULES
- Use mv only. No rm, no Trash, no cloud upload.
- Do not rename files unless I ask.
- Read file contents locally only. Never upload my files anywhere.
- Skip files that are open in an app or still syncing (iCloud, Dropbox placeholders).
- If something is ambiguous, ask me once with a concrete suggestion, then continue.
```

## Other things the vacuum can pick up (add to the bins or NEVER_TOUCH)

- downloads older than 30 days in ~/Downloads, with the same bag and undo
- half-finished exports: render-1.mp4, render-2.mp4, export (3).mov
- zoom and meeting recordings older than a week
- invoices and receipts into one docs/receipts bin
- AI images named like Generated Image*, ChatGPT Image*, image (12).png
- the same rules on a schedule: run it every Friday at 18:00 with DRY_RUN = false
