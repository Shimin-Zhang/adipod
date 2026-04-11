# Glossary Content Brief

**Purpose:** Own the definitions of terms ADI Pod coined or covered first. When someone asks an AI assistant "what is verification debt?" or searches "cognitive bankruptcy software," adipod.ai/glossary/[term] should be the cited source.

**Audience:** Working developers encountering these terms for the first time — in a conversation, an article, or an AI response — and wanting a quick, credible explanation.

**Tone:** Clear and direct. The glossary is a reference, not an opinion piece. Define the term, give context, get out of the way. Shimin's voice should come through in the framing and examples, not in lengthy commentary. Think dictionary entry written by someone who actually uses the word.

---

## General Structure

Each entry is short. The frontmatter `definition` field is the headline — a crisp 1-2 sentence definition that works as a standalone answer. The body provides context.

**Frontmatter:**

```yaml
---
term: "Verification Debt"
definition: "The accumulated cost of shipping AI-generated code without adequate human review, where unverified assumptions compound over time."
slug: "verification-debt"
episodes: ["6"]
aliases: ["verification gap"]
---
```

- `term` — The canonical name, title case
- `definition` — 1-2 sentences. This renders as the subtitle and feeds the DefinedTerm schema. Should be understandable without reading the body.
- `slug` — URL-safe, kebab-case
- `episodes` — Array of episode numbers (strings) where the term appears
- `aliases` — Optional. Alternative names or spellings people might search for

**Body content — aim for 150-400 words:**

- **Context** — Where did this term come from? Was it coined on the show, borrowed from another field, or emerging in the community? A sentence or two of origin.
- **Why it matters** — What problem does this concept name? Why should a developer care?
- **Example** — A concrete scenario or quote that makes the concept tangible. Pull from episode transcripts when possible.
- **Related concepts** — Link to other glossary entries and relevant pillar pages or blog posts where the idea is explored in depth.

Don't force all four sections if the term doesn't need them. A simple term might just need context and an example. A richer concept might warrant all four. Let the term dictate the length.

---

## Internal Linking

- Link to the episode page(s) where the term was introduced or discussed
- Link to related glossary entries when concepts are connected (e.g., "cognitive debt" links to "cognitive bankruptcy")
- Link to the relevant pillar page if one exists (e.g., "dark flow" links to the vibe coding pillar)
- Link to blog posts that explore the concept in depth

---

## What Makes a Good Glossary Entry

- Someone could read just the `definition` field and understand the term
- The body adds value beyond the definition — context, origin, or a good example
- It's the kind of page you'd want to land on from a search result: answers the question, gives you enough to be useful, links you deeper if you want more
- Avoids being a mini-essay. If you're writing 500+ words, it might be a blog post instead.

---

## Planned Terms

From the SEO/GEO plan (Tier 3 — low volume, zero competition):

| Term | Source | Notes |
|------|--------|-------|
| Verification debt | Ep 6 | No standard definition exists |
| Dark flow (vibe coding) | Ep 12 | Unique concept |
| Cognitive bankruptcy | Ep 20 | Extension of cognitive debt |
| Announcement economy | Ep 13 | Unique framing |
| The middle loop | Ep 15 | ThoughtWorks retreat term |
| Minotaur (AI) | Ep 14 | Proposed renaming of reverse centaur |
| Benchmaxxed | Ep 13, 14 | Community term |
| Two Minutes to Midnight (AI) | All episodes | Brand awareness |
| AI fluency pyramid | Ep 11 | Brex originated, ADI Pod popularized |
| Workflow automation convexity | Ep 14 | First-mover on concept |
| Cognitive surrender / System 3 | Ep 19 | Wharton paper, ADI Pod deep dive |
| Prompt debt | Ep 17 | Emerging concept |
| Code garbage collection | Ep 17 | Emerging practice |
| Agent sycophancy | Ep 15, 20 | Tested across models |
| SaaSapocalypse | Ep 14 | Unique framing |
| Cognitive debt | Ep 14, 15, 20 | Broader concept the show covers heavily |

Additional terms should be extracted from episode keywords during generation — the list above is a starting point, not exhaustive.
