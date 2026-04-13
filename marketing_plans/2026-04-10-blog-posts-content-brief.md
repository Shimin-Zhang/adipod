# Blog Posts Content Brief

**Purpose:** Standalone articles targeting specific keywords, each derived from episode content but written to stand on its own. These are the workhorses of the SEO strategy — they target Tier 1 and Tier 2 keywords, link up to pillar pages, and serve as the content most likely to get shared, cross-posted, and submitted to Hacker News.

**Audience:** Developers who found this article through search, social, or an AI citation. They may never have heard of ADI Pod. The article should be valuable on its own and make them curious about the show.

**Tone:** Shimin's written voice. This is the long-form register from the write-like-shimin skill — more structured than the podcast, more aggressively cited, humor is structural rather than reactive. Zero warmup openings. Borrowed frameworks from other fields. Hedged-then-definitive pairs. Opinionated but fair.

---

## General Structure

Blog posts are not episode recaps. They take a topic the show covered and turn it into a standalone piece that someone would want to read even if they've never listened to the podcast. The episode is the source material, not the frame.

**Frontmatter:**

```yaml
---
title: "Why AI Code Has 1.7x More Bugs (and What to Do About It)"
description: "CodeRabbit's data shows AI-authored PRs have significantly more findings. Here's what the numbers actually mean and how to write better AI-assisted code."
date: "2026-04-10"
slug: "ai-code-quality-bugs"
keywords: "AI code quality, AI code bugs, AI-generated code review"
episodes: ["7", "12", "15"]
---
```

- `title` — 10-15 words. Use the four title formulas: numbered promise, provocative question, contrarian take, or literary/metaphorical. Keyword-forward.
- `description` — 1-2 sentences for meta and social. Should make someone want to click.
- `date` — Publication date
- `slug` — URL path under /blog/
- `keywords` — Comma-separated target keywords
- `episodes` — Array of source episode numbers

**Body content — 1,000-2,500 words:**

Structure should serve the argument. Some patterns that work well:

- **Numbered frameworks** — "3 questions to ask," "4 techniques for X." Explicit taxonomies that organize the piece.
- **Progressive disclosure** — Start with the simplest explanation, escalate to nuance. Each level adds tradeoffs.
- **Comparative evaluation** — Multiple approaches evaluated against consistent criteria.
- **Extended metaphor** — Borrow a concept from another field and apply it rigorously. The humor is in the commitment.
- **Data-first** — Lead with a surprising statistic, then unpack what it means and doesn't mean.

Regardless of structure, every blog post should:

- Open with the thesis or the reader's problem. No preamble.
- Include at least one specific data point with attribution
- Acknowledge counterarguments or limitations
- Close with actionable takeaways, a reframing, or a wry final line — never "thanks for reading"

---

## Internal Linking

- Link to the relevant pillar page (every blog post should connect to at least one)
- Link to glossary entries for terms that have pages
- Link to specific episode pages for "hear the full discussion" moments
- Link to other blog posts when topics connect

---

## Cross-Posting

Blog posts are designed to be cross-posted to Dev.to and Hashnode with canonical URLs pointing back to adipod.ai. When writing, keep in mind:

- The piece should work without any ADI Pod context
- Episode references should feel like citations, not promotions ("as discussed in [Episode 7](/episodes/...)")
- Include a brief author bio at the end for cross-posted versions

---

## What Makes a Good Blog Post

- It has a clear thesis, not just a topic
- Someone could share it on Hacker News and it would hold up in the comments
- It teaches something specific — a framework, a technique, a way of thinking about a problem
- Statistics are cited, not vibed. Named sources, episode links, paper references.
- It doesn't read like a transcript summary. It reads like an article that happened to be informed by podcast conversations.
- It's the kind of thing Shimin would actually publish on Dev.to under his own name

---

## Planned Blog Posts

| Title | Source Episodes | Target Keyword |
|-------|---------------|----------------|
| The Claude.md Best Practices Guide | Ep 4, 10, 17 | Claude.md best practices |
| Why AI Code Has 1.7x More Bugs | Ep 7, 12, 15 | AI code quality |
| The Nickname Trick: Detecting Claude Context Loss | Ep 4 | Claude context loss detection |
| Cognitive Debt: The Hidden Cost of AI Development | Ep 14, 15, 20 | cognitive debt software |
| Model Councils: Running Multiple LLMs Simultaneously | Ep 14 | model councils LLM |
| Two Minutes to Midnight: Visual History of the AI Bubble | All eps | AI bubble 2026 |
| Every Cialdini Persuasion Technique Works on LLMs | Ep 2 | persuasion techniques LLM |
| TPUs vs GPUs: A Developer's Guide | Ep 4 | TPU vs GPU explained |
| Spec-Driven Development in the Age of AI | Ep 5, 15, 16 | spec-driven development |
| Dark Flow: Why Vibe Coding Feels Productive But Isn't | Ep 12 | dark flow vibe coding |
| The AI Fluency Pyramid: From User to Native | Ep 11 | AI fluency framework |
| Workflow Automation Convexity: Why AI Won't Take Half Your Job | Ep 14 | AI job automation |
| Hallucination Neurons: Can We Turn Off LLM Lying? | Ep 7 | hallucination neurons LLM |
| We Tested 3 Models for Sycophancy | Ep 15, 20 | AI sycophancy test |
| Cognitive Surrender: What Happens When You Trust AI Too Much | Ep 19 | cognitive surrender AI |
| What Claude Code's Source Leak Revealed | Ep 20 | Claude Code source code |
