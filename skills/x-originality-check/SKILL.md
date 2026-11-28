---
name: x-originality-check
description: Check your own X posts for originality before you apply for X monetization (Original Content Rewards). Finds earlier word-for-word matches, reworded retellings of the same story, and people who copied you, with links and timestamps. Text only. Use before applying, or when a monetization application was rejected for originality.
---

# x-originality-check

X can reject a monetization application if your posts don't look original. This skill checks your recent posts before you apply, so you can rewrite or remove the risky ones first.

The tool and the method are not ours. They come from **CoolerRadar** by Cooler ([@coolerwave](https://x.com/coolerwave)), a free open-source browser extension:
- https://github.com/Coolerwave/coolerradar (MIT)

This skill is the agent side: it runs the same checks for you with a browser agent, reads the results and writes a short report.

No Claude yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).

## Two ways to run it

**1. Fastest: install CoolerRadar itself (recommended)**
1. Download https://github.com/Coolerwave/coolerradar as a ZIP and unzip it.
2. Open `chrome://extensions`, turn on Developer mode, click **Load unpacked**, pick the folder with `manifest.json`.
3. Open x.com logged in, go to your profile, click **Quick check** (10 posts) or **Full check** (25).
4. Paste the results to Claude and ask: "Which of these should I rewrite or delete before I apply, and why?"

**2. Agent mode: Claude does the checks in your browser**
Needs a browser tool (Claude in Chrome or similar) logged into your own X account. Claude only reads search pages. It never posts, reports or deletes anything.

## Agent mode steps

1. **Collect posts.** Open your own profile. Take the newest 10 (quick) or 25 (full) original posts. Skip replies, reposts and posts under ~12 words. For a quote post, keep only your own text, never the quoted text.
2. **Clean the text.** Remove links, @mentions, hashtags, emoji and extra spaces. Lowercase.
3. **Build up to 3 searches per post** on x.com search, tab Latest (`f=live`):
   - the most distinctive exact phrase of 6 to 10 words, in quotes;
   - up to two keyword searches from names, numbers and rare words, joined with OR, e.g. `name (number OR rareword OR place)`. These find retellings where every sentence was reworded.
   Wait 3 to 6 seconds (random) between searches. If X asks you to slow down, pause and tell the user.
4. **Compare each result with the post.**
   - **Exact match:** 70% or more shared word pairs (Jaccard on word bigrams). A result cut at "Show more" still counts if it starts the same way and almost all visible text matches.
   - **Same story:** below 70%, but it shares enough names, numbers and content words with the post, ignoring order. Sharing only one person's name does not count.
   - Ignore your own other accounts if the user lists them.
5. **Who was first.** Get each post's time from its id: `timestamp_ms = (id >> 22) + 1288834974657` (use BigInt). The earlier post counts as first.
6. **Label every post:**
   - ✅ Original: nothing similar found.
   - ⚠️ Earlier match: same text posted before yours. X may not count it. Rewrite in your own words or delete before applying.
   - 📰 Same story, earlier: someone told the same story first. Add your own angle and a source, or remove it. Could just be the same public news.
   - 🚨 Copied from you: someone posted your text after you. Keep both links and times for an appeal.
   - 📰 Same story, later: a later post retells yours.
7. **Report.** A table: post link, label, matching post link, both timestamps, similarity, one-line advice. Then the profile score: share of checked posts that are not an earlier match, not an earlier same story, and not a repeat of your own older post.

## Limits (say these in the report)
- Text only. Videos and images are not checked.
- Translations are not detected. Retellings are found only when they keep names, numbers or rare words.
- X search misses things, especially older posts. A clean result doesn't guarantee approval.
- A match is not proof of copying.
- Monetization also needs X Premium, 500 verified followers and 500K verified home timeline impressions in 90 days. This check covers only originality.

## Rules
- Check only the user's own profile.
- Read only. No posting, no replies, no reports, no deletes. Offer a "reply with original link" text the user sends themselves.
- Keep results local. Don't send the user's posts to any other service.

---

Don't have Claude Code yet? [Get Claude here](https://claude.ai/referral/IL0FPScZCw).
