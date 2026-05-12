---
name: episode-site-update
description: Use whenever the user wants to publish or thread a new ADI Pod episode into the site — phrases like "add the latest episode", "update the site for ep-N", "publish ep-N", "thread the new episode in", "the new ep dropped", "ep-24 is out", or "what's new on the pod". Two-pass workflow: writes `episodes/ep-N.md` first, then proposes threading edits into topics/blog/glossary pages. Auto-fetches Transistor + YouTube metadata and pings the user about anything missing rather than fabricating IDs or URLs.
---

# Episode → Site Update

Publish the latest ADI Pod episode and thread it into the rest of the site. **Run as two passes — never bundle them.** Pass 2 depends on the user reviewing Pass 1's output (frontmatter, takeaways, resources) before threading edits propagate the same framing into half a dozen other pages.

## Inputs (where the data lives)

All under `~/agents/podcast-agent/workspace/.pi/skills/`:

| File | What's in it |
|------|--------------|
| `podcast-transcripts/transcripts/ep-N.md` | Full transcript (source of truth) |
| `podcast-transcripts/summaries/ep-N-summary.md` | Hosts/guests, key topics, keywords, notable insights |
| `youtube-advertising/output/ep-N-description.md` | Polished YouTube description, title options, "In this episode" bullets |
| `youtube-advertising/output/ep-N-youtube.md` | YouTube-specific copy (sometimes present, sometimes not) |

The site repo is `~/projects/adi_pod`. **Episode markdown files live in `episodes/` at the repo root**, not under `site/src/content/episodes/` — the Astro `episodes` collection loader reads from `../episodes` (see `site/src/content.config.ts`).

## Step 0: Pick the episode

1. Find the highest N: `ls ~/agents/podcast-agent/workspace/.pi/skills/podcast-transcripts/transcripts/ep-*.md`.
2. Check if `episodes/ep-N.md` already exists in the repo. If yes, ask the user whether to overwrite (re-publish) or skip to Pass 2 (re-thread only).
3. Read the transcript, summary, and youtube-description files. **If any of the three are missing, ping the user before continuing** — these are the canonical sources and the skill can't fabricate them.

## Step 1: Fetch external metadata

The skill needs two IDs that aren't in the podcast-agent workspace:

- **`transistorId`** — Transistor's internal episode ID (e.g. `687e6e6f`). The show is at `https://adipod.transistor.fm`. Try WebFetch on the show home page, find the episode by title, and follow to its permalink — the ID lives in the embed iframe `src` (e.g. `https://share.transistor.fm/e/687e6e6f`). If the page structure has changed or the episode isn't yet live, ping the user.
- **`youtubeId`** — YouTube video ID (e.g. `sFu49z2iQEc`). Channel: `https://www.youtube.com/channel/UCF2uGjtrCXh5u7ec8ckQCuQ`. Try WebFetch on `/videos` and match the latest upload to the episode title. YouTube often blocks scraping — if the fetch returns nothing useful, ask the user to paste the video URL.

**Do not invent IDs.** If either fetch fails, ping the user with what you tried and what specifically is missing.

The boilerplate platform URLs (Apple / Spotify / Overcast / PocketCasts / Amazon) are identical across episodes — copy them verbatim from the previous episode's frontmatter rather than refetching.

## Pass 1: Write `episodes/ep-N.md`

Use the most recent prior episode (`episodes/ep-(N-1).md`) as the structural template. The schema is defined in `site/src/content.config.ts` under the `episodes` collection — `episode`, `title`, `date`, `slug` are required; the rest are optional but should all be present for a complete page.

### Frontmatter rules

- `episode`: string, number only (`"24"`)
- `title`: match the YouTube/Transistor title — typically a 3-segment headline joined by commas
- `date`: publish date `YYYY-MM-DD`. Pull from the summary file's frontmatter or YouTube description header
- `slug`: `N-kebab-cased-title` (must be URL-safe and match prior-episode pattern)
- `description`: 1–2 sentence hook — expanded from the YouTube lead paragraph, mentioning the guest if any
- `keywords`: comma-separated, 30–60 entries. Combine the summary file's `Keywords:` line with guest names and product names. Drives SEO; bias toward inclusion.
- `transistorId` / `youtubeId`: from Step 1

### Body sections (in this order)

Mirror the structure of ep-22 / ep-23:

1. **Lead paragraph** — same content as `description` but expanded with guest mention and the list of topics covered.
2. **`## Takeaways`** — 5–7 bullets. Each one is a complete claim with substance, not a teaser. Draw from the summary's "Notable Insights" plus a close read of the transcript.
3. **`## Resources Mentioned`** — every link discussed in the episode, as `- [Title — Source](URL)`. Sources: scan the transcript for URLs, paper titles, product names, books, blog posts. Cross-check against the YouTube description's "In this episode" bullets. If a resource was clearly discussed but no URL is findable, list it in the user ping (don't omit silently).
4. **`## Chapters`** — `- (HH:MM) - Section Title`. Pull from the YouTube description or Transistor show notes when available; otherwise derive from transcript transitions (look for host phrases like "alright, next up...", "moving on to...", segment names like "Post-Processing", "Deep Dive", "Two Minutes to Midnight").
5. **`## Transcript`** — wrap the full transcript verbatim in `<details><summary>Show full transcript</summary>` ... `</details>`. Copy directly from the transcript file; do not edit or summarize.

### Verify

- Run `cd site && npx astro build` to catch frontmatter schema errors.
- Show the user the new file's frontmatter, Takeaways, and Resources Mentioned (collapse the transcript) for sign-off **before** moving to Pass 2.

## Pass 2: Thread the episode into related pages

**Wait for the user to approve Pass 1 first.** Threading edits propagate the episode's framing across many files — if Pass 1's takeaways are wrong, Pass 2 amplifies the error.

### Find threading candidates

List existing pages and match by keyword:

```bash
ls site/src/content/topics/
ls site/src/content/blog/
ls site/src/content/glossary/
```

Match the new episode's `keywords` against these slugs/titles. The recent pattern (ep-22, ep-23):

- **Topics pages** (`site/src/content/topics/*.md`) — extend a running narrative with a new section or paragraph (e.g. `ai-bubble-tracker` gained Phase 6 in ep-23).
- **Blog posts** (`site/src/content/blog/*.md`) — inline mention in a relevant section, usually a paragraph or sentence with the article URL inline.
- **Glossary terms** (`site/src/content/glossary/*.md`) — append an episode-N paragraph extending the definition with new context the episode added.

The canonical model is the prior episode's threading commit:

```bash
git log --oneline --grep "thread ep-" -3
git show <commit> --stat
```

Read those diffs to see the *shape* of a good threading edit (length, voice, where in the file it lands).

### Frontmatter bumps

- **Blog and topic pages**: bump `lastUpdated:` to today's date on every edit. The Zod schema includes this field; the sitemap uses it for freshness.
- **Glossary pages have no `lastUpdated` field** — do not add one; the schema rejects it.
- **`episodes:` array**: if a page already has this field, append the new episode number (e.g. `["20", "22"]` → `["20", "22", "24"]`). Don't add the field where it's absent unless the schema includes it.

### Propose, don't bulk-apply

For each candidate page, present:
- File path
- One-sentence reason the episode actually adds something ("ep-24's goblin problem is a concrete RLHF reward-hacking case that the AI fluency pyramid post currently lacks" — not "ep-24 mentions RLHF")
- The proposed edit (full text of new section / paragraph / inline link)

Wait for user accept/reject per page. After all decisions, apply edits and stage them. Commit shape should match prior threading commits — one commit for the new episode file, a second commit for the threading edits.

## When to ping the user

- Transcript / summary / YouTube-description file is missing for the episode you'd otherwise pick.
- `transistorId` couldn't be fetched (login wall, page structure changed, episode not yet live on Transistor).
- `youtubeId` couldn't be determined (channel feed didn't return matching video, multiple ambiguous matches).
- A resource was clearly discussed in the transcript but no URL was findable — list each unresolved item.
- A threading candidate looks plausible but you're not sure whether the episode adds new substance vs. a passing mention — let the user decide rather than force a thin edit.

## Reference: prior-episode commits

The canonical pattern (one "add" commit, one "thread" commit, optionally a "resources" follow-up):

```bash
git log --oneline --grep "ep-2[2-3]"
```

Match the commit message format and granularity.
