# Desk vacuum prompt for Claude Code

A robot vacuum for your computer desktop. Paste into Claude Code, started in (or pointed at) your desktop folder. Change only the PARAMETERS block.

No Claude yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).

```
You are a robot vacuum for my desktop. Pick up every file, figure out what it is, and put it into the folder where it belongs. You sort and file. You never delete. Work only inside TARGET and HOMES.

PARAMETERS
TARGET      = ~/Desktop
HOMES       = documents:   ~/Documents/From Desktop
              photos:      ~/Pictures/From Desktop
              screenshots: ~/Pictures/Screenshots
              video:       ~/Movies/From Desktop
              audio:       ~/Music/From Desktop
              code:        ~/Developer/From Desktop
              installers:  ~/Downloads/Installers
              archives:    ~/Documents/From Desktop/Archives
              other:       ~/Documents/From Desktop/Other
              review:      ~/Desktop/_review
LOG         = ~/Documents/From Desktop/_vacuum-log/{YYYY-MM-DD}
NEVER_TOUCH = keep, .app          # any file or folder whose name contains one of these stays where it is
OLDER_THAN  = 0d                  # only move files not opened for this long (0d = everything)
DRY_RUN     = true                # true = show the plan only, move nothing
LIVE_VIEW   = true                # build a local HTML page with the vacuum driving over your files

HOW TO WORK
1. Inventory TARGET (top level, plus loose folders): every file with name, size, hash, created, last opened. Save it as LOG/_index.json. Tell me the counts before going further.
2. Decide what each file is by what is inside it, not only by the extension. Peek at every file locally (text, PDF first page, image thumbnail, video frame) and file it:
   - documents (PDF, Word, Pages, Excel, Numbers, Keynote, txt, md, csv): HOMES.documents, in a subfolder by what the document is about: invoices-receipts, contracts, ids-and-forms, work, study, notes, other
   - photos (real photos in jpg, heic, png, raw): HOMES.photos, in YYYY-MM subfolders by date taken
   - screenshots and screen recordings (by name, or an image that is clearly a screen capture): HOMES.screenshots, in YYYY-MM subfolders
   - video: HOMES.video, in YYYY-MM subfolders
   - audio: HOMES.audio
   - code and project folders: HOMES.code, folder kept whole
   - installers (.dmg, .pkg): HOMES.installers
   - zip and other archives: HOMES.archives
   - anything else: HOMES.other, grouped by type
   - unsure: HOMES.review with a one-line reason
3. Clean while you file:
   - "final" versions (final, final2, FINAL, v2, v3, copy, (1)): group by base name. The newest one goes to its home, the older ones go next to it into an _older-versions subfolder.
   - exact duplicates (same hash): one copy goes to its home, the rest into a _duplicates subfolder next to it.
   - empty folders and "untitled folder" folders: move them into LOG/empty-folders.
   - anything matching NEVER_TOUCH: leave it on the desktop and list it.
4. Show me the plan as a table: destination folder, file count, 5 example files, total size, plus what stays on the desktop and what goes to review. If DRY_RUN = true, stop here.
5. After my OK, move the files. Create missing folders. Never delete anything, never empty the Trash. Never overwrite: on a name clash add a numeric suffix.
6. Write LOG/_manifest.csv (original path, new path, type, reason) and LOG/undo.sh that puts every file back on the desktop where it was.
7. If LIVE_VIEW = true, write LOG/_live.html: my desktop as a grid of file icons, a round robot vacuum that drives over them and picks each file up as it is moved, labeled bins (Documents, Photos, Screenshots, Video, Other) filling up, and a counter (files picked up / elapsed). It reads a progress JSON you keep updating.
8. Finish with a card: "Desktop cleaned. N files filed in Xm Ys", counts per destination, what you left alone, what is in review, and the undo command.

RULES
- Use mv only. No rm, no Trash.
- Read file contents locally only. Never upload my files anywhere.
- Do not rename files unless I ask.
- Skip files that are open in an app or still syncing (iCloud, Dropbox placeholders).
- If something is ambiguous, ask me once with a concrete suggestion, then continue.
```

## Other things the vacuum can pick up (add to the bins or NEVER_TOUCH)

- ~/Downloads with the same rules and undo
- half-finished exports: render-1.mp4, render-2.mp4, export (3).mov
- zoom and meeting recordings older than a week
- invoices and receipts into one docs/receipts bin
- AI images named like Generated Image*, ChatGPT Image*, image (12).png
- the same rules on a schedule: run it every Friday at 18:00 with DRY_RUN = false

---

Don't have Claude Code yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).
