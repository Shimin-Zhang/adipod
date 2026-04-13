# Pillar Pages Content Brief

**Purpose:** Establish ADI Pod as the definitive practitioner resource on 6 high-intent developer topics. These are the SEO anchors — comprehensive, evergreen pages that rank for Tier 1 keywords and serve as the hub for internal linking.

**Audience:** Developers actively searching for guidance on these topics. They've heard the term, they're evaluating tools, or they're trying to understand a trend. They want depth from someone who's used the tools, not a listicle from someone who hasn't.

**Tone:** Shimin's long-form voice. Practitioner-scholar: grounded in hands-on experience, backed by data and cited sources. Opinionated but fair — present tradeoffs, acknowledge what's good about things you criticize, name what you don't know. The borrowed-framework approach works well here (e.g., structuring the career impact page around an economic framework, or the vibe coding page around a risk taxonomy).

---

## General Structure

Each pillar page synthesizes content from multiple episodes into a cohesive resource. They're not transcriptions — they're original articles that happen to draw on 200K+ words of source material.

**Frontmatter:**

```yaml
---
title: "The Complete Guide to Claude Code"
description: "Everything we've learned about Claude Code across 20 episodes — workflows, tips, pitfalls, and the stuff the docs don't tell you."
slug: "claude-code-guide"
keywords: "Claude Code best practices, Claude Code tips, Claude.md guide, Claude Code workflow"
lastUpdated: "2026-04-10"
---
```

- `title` — Clear, keyword-forward, 10-15 words max
- `description` — 1-2 sentences for meta description and social sharing
- `slug` — URL path under /topics/
- `keywords` — Comma-separated target keywords
- `lastUpdated` — Tracks freshness; update when new episode content is incorporated

**Body content — 3,000-5,000 words:**

There's no rigid template. The structure should serve the topic. But most pillar pages will benefit from some combination of:

- **Introduction** — What this page covers and why it exists. Name the reader's problem or question. No warmup.
- **Core sections** — The meat. Organized however makes sense for the topic: chronologically, by subtopic, by framework, by tool. Use H2s for major sections, H3s for subsections.
- **Comparison tables** — Where the topic involves evaluating alternatives (tools, models, approaches), a structured comparison is more useful than prose.
- **FAQ section** — 5-8 questions formatted as H3 headers, matching how developers ask AI assistants. These are GEO magnets. Use natural question phrasing ("How do I know when Claude Code has lost context?" not "Context loss detection methodology").
- **Quotable statistics** — Pull from episode content. Format as blockquotes with full attribution and episode links. These are what AI assistants cite.
- **Episode links** — Reference specific episodes throughout the body where topics were discussed in depth. These are entry points to the broader content library.

---

## Internal Linking

Pillar pages are hubs. They should link outward generously:

- To episode pages where specific topics were discussed
- To glossary entries for terms that have their own pages
- To blog posts that go deeper on subtopics
- To segment hubs when relevant (e.g., the bubble tracker pillar links to the Two Minutes to Midnight segment hub)
- To other pillar pages when topics intersect

Blog posts and glossary entries should link back to the relevant pillar page. This creates the hub-and-spoke structure search engines reward.

---

## Living Documents

Pillar pages are not published once and forgotten. When a new episode covers the topic:

- Add new insights, data points, or examples
- Update the FAQ if new questions were addressed
- Update comparison tables if new tools or models were discussed
- Bump `lastUpdated` in frontmatter

The update cadence should be natural — after relevant episodes, not on a fixed schedule.

---

## What Makes a Good Pillar Page

- Someone searching the target keyword should feel like they found the best single page on the internet for that query
- It synthesizes — it doesn't just list what each episode said. It builds a coherent picture.
- It has original framing or structure, not just a recap. The borrowed-framework approach is ideal here.
- The FAQ section answers real questions in natural language
- Statistics are cited with sources and episode links
- It's useful to someone who has never listened to the podcast, but makes them want to

---

## Planned Pillar Pages

| Page | Target Keywords | Key Source Episodes |
|------|----------------|-------------------|
| The Complete Guide to Claude Code | Claude Code best practices, Claude Code tips, Claude.md guide | Ep 1, 4, 6, 10, 11, 13, 17, 19, 20 |
| AI Bubble Tracker — Two Minutes to Midnight | AI bubble 2026, will AI bubble burst, AI CAPEX vs revenue | All episodes |
| Vibe Coding: What Works, What Doesn't, and When to Stop | vibe coding guide, vibe coding pros cons, dark flow coding | Ep 3, 5, 7, 12, 14, 15, 16, 20 |
| AI's Impact on Developer Careers | AI replace developers, future of software engineering AI | Ep 8, 11, 12, 13, 14, 15, 16, 18, 19 |
| AI Coding Agents Compared | Claude Code vs Cursor, AI coding agent comparison | Ep 1, 4, 6, 10, 11, 13, 16, 17, 18, 20 |
| AI Security for Developers | AI agent security, MCP security, prompt injection prevention | Ep 2, 3, 6, 13, 16, 17, 18, 19 |

The AI Bubble Tracker is unique among these — it's a living document with a data visualization component (clock position history). It should feel more like a dashboard than an article.
