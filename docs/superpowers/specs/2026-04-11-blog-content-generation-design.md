# Blog Content Generation Design

**Date:** 2026-04-11
**Status:** Approved
**Scope:** Generate all 16 planned blog posts for adipod.ai

---

## Overview

Generate 16 standalone blog posts derived from ADI Pod episode transcripts. Each post targets a specific keyword, stands alone without podcast context, and is written in Shimin Zhang's long-form voice. Posts are the primary SEO workhorses — designed for search, social sharing, cross-posting, and Hacker News submission.

## Approach

**Sequential single-agent.** One agent writes all 16 posts in order. This ensures voice consistency across posts, allows later posts to cross-link to earlier ones, and avoids redundant transcript reads when multiple posts share source episodes.

## Source Material

For each post, the agent reads three layers:

1. **Episode summaries** (~400 words each) at `/home/shimin/agents/podcast-agent/workspace/.pi/skills/podcast-transcripts/summaries/ep-{N}-summary.md` — for topic orientation and identifying relevant transcript sections
2. **Full transcripts** (~12K words each) at `/home/shimin/agents/podcast-agent/workspace/.pi/skills/podcast-transcripts/transcripts/ep-{N}.md` — for arguments, quotes, data points, and Shimin's actual phrasing
3. **Episode shownotes** at `/home/shimin/projects/adi_pod/episodes/ep-{N}.md` — for citation URLs (Resources Mentioned sections)

## Output

Markdown files written to `site/src/content/blog/{slug}.md`.

### Frontmatter Schema

Matches the Zod schema in `site/src/content.config.ts`:

```yaml
---
title: "10-15 word keyword-forward title"
description: "1-2 sentence meta description"
date: "2026-04-11"
slug: "url-slug"
keywords: "comma, separated, target, keywords"
episodes: ["7", "12", "15"]
---
```

### Body Content

1,000–2,500 words following the write-like-shimin long-form register:

- **Opening:** Zero warmup. First sentence names the reader's pain or states the thesis.
- **Structure:** Organized by a borrowed framework, numbered taxonomy, progressive disclosure, comparative evaluation, or extended metaphor — never a flat list of tips.
- **Sentences:** 18–22 word average. Hedged-then-definitive pairs. Colon pivots. Em-dash parentheticals.
- **Evidence:** Named citations from shownotes (specific people, papers, benchmarks). At least one empirical data point per post.
- **Counterarguments:** Handled fairly with explicit caveats and "when to use" criteria.
- **Humor:** Structural — deadpan analogies played straight, absurd calculations taken seriously. Never forced.
- **Closing:** Actionable takeaways, a reframing summary, or a wry final line. Never "thanks for reading."

### Internal Linking

Each post links to:

- **Pillar pages** — at least one from the 6 existing topics at `/topics/{slug}/`:
  - claude-code-guide, ai-bubble-tracker, vibe-coding-guide, ai-coding-agents-compared, ai-developer-careers, ai-security-developers
- **Glossary entries** — for terms that have pages at `/glossary/{slug}/` (16 entries exist)
- **Episode pages** — at `/episodes/{slug}/` for "hear the full discussion" moments
- **Other blog posts** — where topics connect (later posts can reference earlier ones)

## Post Order

Written sequentially in the content brief order:

| # | Title | Source Episodes | Target Keyword | Slug |
|---|-------|----------------|----------------|------|
| 1 | The Claude.md Best Practices Guide | 4, 10, 17 | Claude.md best practices | claude-md-best-practices |
| 2 | Why AI Code Has 1.7x More Bugs | 7, 12, 15 | AI code quality | ai-code-quality-bugs |
| 3 | The Nickname Trick: Detecting Claude Context Loss | 4 | Claude context loss detection | claude-context-loss-nickname-trick |
| 4 | Cognitive Debt: The Hidden Cost of AI Development | 14, 15, 20 | cognitive debt software | cognitive-debt-ai-development |
| 5 | Model Councils: Running Multiple LLMs Simultaneously | 14 | model councils LLM | model-councils-multiple-llms |
| 6 | Two Minutes to Midnight: Visual History of the AI Bubble | All (use summaries primarily; pull specific transcript sections as needed) | AI bubble 2026 | ai-bubble-two-minutes-to-midnight |
| 7 | Every Cialdini Persuasion Technique Works on LLMs | 2 | persuasion techniques LLM | cialdini-persuasion-techniques-llms |
| 8 | TPUs vs GPUs: A Developer's Guide | 4 | TPU vs GPU explained | tpu-vs-gpu-developers-guide |
| 9 | Spec-Driven Development in the Age of AI | 5, 15, 16 | spec-driven development | spec-driven-development-ai |
| 10 | Dark Flow: Why Vibe Coding Feels Productive But Isn't | 12 | dark flow vibe coding | dark-flow-vibe-coding |
| 11 | The AI Fluency Pyramid: From User to Native | 11 | AI fluency framework | ai-fluency-pyramid |
| 12 | Workflow Automation Convexity: Why AI Won't Take Half Your Job | 14 | AI job automation | workflow-automation-convexity |
| 13 | Hallucination Neurons: Can We Turn Off LLM Lying? | 7 | hallucination neurons LLM | hallucination-neurons-llm |
| 14 | We Tested 3 Models for Sycophancy | 15, 20 | AI sycophancy test | ai-sycophancy-test |
| 15 | Cognitive Surrender: What Happens When You Trust AI Too Much | 19 | cognitive surrender AI | cognitive-surrender-ai |
| 16 | What Claude Code's Source Leak Revealed | 20 | Claude Code source code | claude-code-source-leak |

## Out of Scope

- Cross-posting versions (Dev.to/Hashnode formatting) — canonical adipod.ai markdown only
- Images, diagrams, or visual assets
- FAQ schema sections
- Author bio blocks (for cross-posted versions only)
