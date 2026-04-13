# Blog Content Generation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate all 16 planned blog posts as markdown files in `site/src/content/blog/`.

**Architecture:** Sequential single-agent. For each post: read episode summaries → read full transcripts → read shownotes for citation URLs → write the markdown file. Posts are written in order so later posts can cross-link to earlier ones.

**Tech Stack:** Markdown content files for Astro 5.x with Zod content collections.

**Voice:** Follow the `write-like-shimin` long-form register. Calibrate against reference articles in `/home/shimin/.claude/skills/write-like-shimin/devto-articles/`. Key traits: zero warmup openings, borrowed frameworks as article skeleton, hedged-then-definitive pairs, named citations, structural humor, 18-22 word average sentences.

---

## Reference Paths

| Resource | Path |
|----------|------|
| Transcripts | `/home/shimin/agents/podcast-agent/workspace/.pi/skills/podcast-transcripts/transcripts/ep-{N}.md` |
| Summaries | `/home/shimin/agents/podcast-agent/workspace/.pi/skills/podcast-transcripts/summaries/ep-{N}-summary.md` |
| Shownotes | `/home/shimin/projects/adi_pod/episodes/ep-{N}.md` |
| Voice skill | `/home/shimin/.claude/skills/write-like-shimin/` |
| Voice reference articles | `/home/shimin/.claude/skills/write-like-shimin/devto-articles/` |
| Content brief | `/home/shimin/projects/adi_pod/marketing_plans/2026-04-10-blog-posts-content-brief.md` |
| Design spec | `/home/shimin/projects/adi_pod/docs/superpowers/specs/2026-04-11-blog-content-generation-design.md` |
| Output dir | `/home/shimin/projects/adi_pod/site/src/content/blog/` |

## Internal Link Targets

**Pillar pages (topics):**
- `/topics/claude-code-guide/`
- `/topics/ai-bubble-tracker/`
- `/topics/vibe-coding-guide/`
- `/topics/ai-coding-agents-compared/`
- `/topics/ai-developer-careers/`
- `/topics/ai-security-developers/`

**Glossary entries:**
- `/glossary/agent-sycophancy/`
- `/glossary/ai-fluency-pyramid/`
- `/glossary/announcement-economy/`
- `/glossary/benchmaxxed/`
- `/glossary/code-garbage-collection/`
- `/glossary/cognitive-bankruptcy/`
- `/glossary/cognitive-debt/`
- `/glossary/cognitive-surrender/`
- `/glossary/dark-flow/`
- `/glossary/minotaur/`
- `/glossary/prompt-debt/`
- `/glossary/saasapocalypse/`
- `/glossary/the-middle-loop/`
- `/glossary/two-minutes-to-midnight/`
- `/glossary/verification-debt/`
- `/glossary/workflow-automation-convexity/`

**Episode pages** use format `/episodes/{slug}/` — see episode frontmatter for slugs.

## Frontmatter Template

Every blog post uses this exact schema (matches Zod in `site/src/content.config.ts`):

```yaml
---
title: "Keyword-Forward Title in 10-15 Words"
description: "1-2 sentence meta description that makes someone want to click."
date: "2026-04-11"
slug: "url-slug-here"
keywords: "primary keyword, secondary keyword, tertiary keyword"
episodes: ["4", "10", "17"]
---
```

## Voice Checklist (apply to every post)

- [ ] First sentence names the reader's pain or states the thesis (zero warmup)
- [ ] Ideas organized by a borrowed framework or mental model — not a flat list
- [ ] Named citations: specific people, papers, studies, benchmarks from shownotes
- [ ] At least one empirical data point (numbers, measurements, comparisons)
- [ ] Counterarguments handled fairly — explicit caveats, "when to use" criteria
- [ ] Sentences average 18-22 words with colon-pivots and hedged-then-definitive pairs
- [ ] Humor is structural (deadpan metaphors played straight, absurd calculations taken seriously)
- [ ] Closes with actionable takeaways, a reframing summary, or a wry final line
- [ ] No "thanks for reading" — ends on substance
- [ ] 1,000-2,500 words body
- [ ] Links to at least one pillar page, relevant glossary entries, and source episode pages
- [ ] Episode references feel like citations, not promotions

---

### Task 0: Voice Calibration

**Purpose:** Before writing any posts, read the voice skill and 2-3 reference articles to internalize Shimin's written register.

- [ ] **Step 1: Read the write-like-shimin skill**

Read: `/home/shimin/.claude/skills/write-like-shimin/` — the full skill file. Internalize the long-form voice section, anti-patterns table, and long-form checklist.

- [ ] **Step 2: Read 2-3 reference articles for tone calibration**

Read these Dev.to articles to calibrate sentence rhythm, humor style, and argument structure:
- `/home/shimin/.claude/skills/write-like-shimin/devto-articles/javascript-readability-vs-performance-a-false-tradeoff.md` (data-first structure, benchmark evidence, contrarian premise opening)
- `/home/shimin/.claude/skills/write-like-shimin/devto-articles/the-boar-the-lobster-and-the-juniper-3-patterns-of-agile-software-development.md` (extended metaphor played straight, borrowed framework as skeleton)
- `/home/shimin/.claude/skills/write-like-shimin/devto-articles/the-unreasonable-effectiveness-of-the-to-do-list-zeigarnik-effect-and-developer-productivity.md` (borrowed psychology framework, literary title)

- [ ] **Step 3: Read the content brief**

Read: `/home/shimin/projects/adi_pod/marketing_plans/2026-04-10-blog-posts-content-brief.md` — internalize the structural patterns, internal linking requirements, and quality bar ("holds up on Hacker News").

---

### Task 1: The Claude.md Best Practices Guide

**Files:**
- Create: `site/src/content/blog/claude-md-best-practices.md`

**Sources:** Ep 4, 10, 17
- Read summaries: `ep-4-summary.md`, `ep-10-summary.md`, `ep-17-summary.md`
- Read transcripts: `ep-4.md`, `ep-10.md`, `ep-17.md`
- Read shownotes: `episodes/ep-4.md`, `episodes/ep-10.md`, `episodes/ep-17.md`

**Angle:** Practical guide to writing effective CLAUDE.md files — what belongs, what doesn't, the maintenance problem nobody talks about. NOT a duplicate of the claude-code-guide pillar page (which covers Claude Code holistically). This post focuses specifically on the CLAUDE.md file as a configuration artifact.

**Key content to extract:**
- Ep 4: nickname trick for context loss detection, ~150-200 instruction limit, progressive disclosure pattern, LLMs read system prompt first then CLAUDE.md
- Ep 10: evolution of CLAUDE.md patterns, what works in practice vs. theory
- Ep 17: CLAUDE.md maintenance as a team discipline, code garbage collection parallels

**Structural approach:** Numbered framework — "N things to put in your CLAUDE.md (and 3 things to leave out)" or progressive disclosure from minimal to advanced.

**Internal links:**
- Pillar: `/topics/claude-code-guide/`
- Glossary: `/glossary/code-garbage-collection/`, `/glossary/prompt-debt/`
- Episodes: link to all three source episodes
- Blog: will be linked FROM post #3 (nickname trick)

- [ ] **Step 1: Read source material** — summaries first, then transcripts for the CLAUDE.md-specific sections, then shownotes for citation URLs
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/claude-md-best-practices.md`
- [ ] **Step 3: Run voice checklist** — verify against the checklist above

---

### Task 2: Why AI Code Has 1.7x More Bugs

**Files:**
- Create: `site/src/content/blog/ai-code-quality-bugs.md`

**Sources:** Ep 7, 12, 15
- Read summaries: `ep-7-summary.md`, `ep-12-summary.md`, `ep-15-summary.md`
- Read transcripts: `ep-7.md`, `ep-12.md`, `ep-15.md`
- Read shownotes: `episodes/ep-7.md`, `episodes/ep-12.md`, `episodes/ep-15.md`

**Angle:** Data-first. Lead with the CodeRabbit report's 1.7x finding, then unpack what it actually means, what it doesn't mean, and what developers should do about it. Not a doom piece — a nuanced analysis.

**Key content to extract:**
- Ep 7: CodeRabbit's "State of AI vs Human Code Generation" report (shownotes have the URL), specific findings about AI-authored PRs
- Ep 12: Anthropic's research on how AI assistance impacts coding skills, the "dark flow" of uncritical acceptance
- Ep 15: practical strategies for reviewing AI-generated code, verification debt concept

**Structural approach:** Data-first — lead with the surprising statistic, then unpack with "what the numbers mean," "what they don't mean," and "what to do about it."

**Internal links:**
- Pillar: `/topics/ai-coding-agents-compared/`
- Glossary: `/glossary/verification-debt/`, `/glossary/cognitive-debt/`, `/glossary/dark-flow/`
- Episodes: link to all three source episodes
- Blog: cross-link to post #10 (dark flow) and post #15 (cognitive surrender) when written

- [ ] **Step 1: Read source material** — summaries first, then transcripts focusing on CodeRabbit data and code quality discussions, then shownotes for the report URL and related citations
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/ai-code-quality-bugs.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 3: The Nickname Trick: Detecting Claude Context Loss

**Files:**
- Create: `site/src/content/blog/claude-context-loss-nickname-trick.md`

**Sources:** Ep 4
- Read summary: `ep-4-summary.md`
- Read transcript: `ep-4.md`
- Read shownotes: `episodes/ep-4.md`

**Angle:** A specific, immediately actionable technique. The article teaches one trick (ask Claude to use a nickname; when it stops, context is degraded) and uses it as a lens into the broader context management problem.

**Key content to extract:**
- Ep 4: the nickname trick itself, how it works, why context loss happens, the ~13% remaining context threshold where performance degrades, anti-patterns that accelerate context consumption

**Structural approach:** Progressive disclosure — start with the simple trick (2 sentences to implement), then escalate to why it works (context window mechanics), then to what else you can do about it (context management strategies).

**Internal links:**
- Pillar: `/topics/claude-code-guide/`
- Glossary: `/glossary/cognitive-bankruptcy/`
- Episodes: `/episodes/4-open-ai-code-red-tpu-vs-gpu-and-more-autonomous-coding-agents/`
- Blog: link to post #1 (CLAUDE.md best practices)

- [ ] **Step 1: Read source material** — summary, then transcript focusing on the nickname trick and context management sections
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/claude-context-loss-nickname-trick.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 4: Cognitive Debt: The Hidden Cost of AI Development

**Files:**
- Create: `site/src/content/blog/cognitive-debt-ai-development.md`

**Sources:** Ep 14, 15, 20
- Read summaries: `ep-14-summary.md`, `ep-15-summary.md`, `ep-20-summary.md`
- Read transcripts: `ep-14.md`, `ep-15.md`, `ep-20.md`
- Read shownotes: `episodes/ep-14.md`, `episodes/ep-15.md`, `episodes/ep-20.md`

**Angle:** Introduce "cognitive debt" as a framework — the gap between what your codebase does and what you understand about it, widened by AI-generated code you didn't write yourself. This is a coined-term piece that defines and popularizes an ADI Pod concept.

**Key content to extract:**
- Ep 14: the cognitive debt concept, how it differs from technical debt, the argument that some tech debt is actually good (Rahul's perspective)
- Ep 15: connection to verification debt, the sycophancy problem making cognitive debt worse
- Ep 20: practical manifestations — developers losing understanding of their own codebases

**Structural approach:** Extended metaphor or borrowed framework. Consider: financial debt (principal, interest, default) mapped to cognitive debt (understanding gap, maintenance cost, cognitive bankruptcy).

**Internal links:**
- Pillar: `/topics/ai-developer-careers/`
- Glossary: `/glossary/cognitive-debt/`, `/glossary/cognitive-bankruptcy/`, `/glossary/verification-debt/`, `/glossary/cognitive-surrender/`
- Episodes: link to all three source episodes
- Blog: cross-link to post #2 (AI code bugs), post #15 (cognitive surrender)

- [ ] **Step 1: Read source material** — summaries first, then transcripts for cognitive debt discussions, then shownotes
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/cognitive-debt-ai-development.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 5: Model Councils: Running Multiple LLMs Simultaneously

**Files:**
- Create: `site/src/content/blog/model-councils-multiple-llms.md`

**Sources:** Ep 14
- Read summary: `ep-14-summary.md`
- Read transcript: `ep-14.md`
- Read shownotes: `episodes/ep-14.md`

**Angle:** Practical guide to using multiple models in parallel — not for benchmarking, but as a development workflow. Model councils as a technique for reducing single-model blind spots.

**Key content to extract:**
- Ep 14: model council concept, how to set up multi-model workflows, when it's worth the overhead, practical examples from the hosts' experience, Crabby Rathbun context

**Structural approach:** Numbered framework — when to use model councils, how to set them up, what patterns emerge.

**Internal links:**
- Pillar: `/topics/ai-coding-agents-compared/`
- Glossary: `/glossary/agent-sycophancy/`, `/glossary/benchmaxxed/`
- Episodes: `/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt/`
- Blog: cross-link to post #14 (sycophancy testing)

- [ ] **Step 1: Read source material** �� summary, then full transcript, then shownotes
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/model-councils-multiple-llms.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 6: Two Minutes to Midnight: Visual History of the AI Bubble

**Files:**
- Create: `site/src/content/blog/ai-bubble-two-minutes-to-midnight.md`

**Sources:** All episodes (use summaries primarily; pull specific transcript sections as needed)
- Read all 20 summaries: `ep-{1-20}-summary.md`
- Read select transcript sections for specific quotes/data
- Read shownotes from episodes with strongest bubble coverage

**Angle:** A longitudinal tracker — how has the "AI bubble" evolved across 20 episodes of the show? Each episode's bubble assessment treated as a data point. The Doomsday Clock metaphor ("two minutes to midnight") applied to AI market conditions.

**Key content to extract:**
- The recurring "two minutes to midnight" segment across episodes
- Specific data points: funding rounds, layoffs, revenue numbers, user growth stats
- How the hosts' assessment has shifted over time
- Key inflection points they identified

**Structural approach:** Extended metaphor (Doomsday Clock) + chronological data-first. Timeline of assessments with the clock as a framing device.

**Internal links:**
- Pillar: `/topics/ai-bubble-tracker/`
- Glossary: `/glossary/two-minutes-to-midnight/`, `/glossary/announcement-economy/`, `/glossary/saasapocalypse/`
- Episodes: link to episodes with the strongest bubble segments
- Blog: this is the most broadly cross-linked post — reference other posts where relevant

- [ ] **Step 1: Read all 20 episode summaries** — extract bubble-related data points and assessments
- [ ] **Step 2: Read select transcripts** — pull specific quotes and data from the strongest bubble discussions
- [ ] **Step 3: Read shownotes** — gather citation URLs for funding/revenue/user data
- [ ] **Step 4: Write the blog post** — to `site/src/content/blog/ai-bubble-two-minutes-to-midnight.md`
- [ ] **Step 5: Run voice checklist**

---

### Task 7: Every Cialdini Persuasion Technique Works on LLMs

**Files:**
- Create: `site/src/content/blog/cialdini-persuasion-techniques-llms.md`

**Sources:** Ep 2
- Read summary: `ep-2-summary.md`
- Read transcript: `ep-2.md`
- Read shownotes: `episodes/ep-2.md`

**Angle:** Borrowed framework from psychology — Cialdini's 6 principles of persuasion applied to LLM prompting. Each principle becomes a prompting technique. The humor is in the commitment to the mapping.

**Key content to extract:**
- Ep 2: discussion of persuasion techniques working on LLMs, specific examples the hosts tested, the "persuade an LLM to call you a jerk" experiment

**Structural approach:** Numbered framework — Cialdini's 6 principles (reciprocity, commitment/consistency, social proof, authority, liking, scarcity) each mapped to an LLM prompting technique with examples.

**Internal links:**
- Pillar: `/topics/ai-coding-agents-compared/`
- Glossary: `/glossary/agent-sycophancy/`
- Episodes: `/episodes/2-it-s-gemini-3-week-and-how-to-persuade-an-llm-to-call-you-a-jerk/`
- Blog: cross-link to post #14 (sycophancy testing)

- [ ] **Step 1: Read source material** — summary, then full transcript for the persuasion discussion, then shownotes for any referenced papers
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/cialdini-persuasion-techniques-llms.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 8: TPUs vs GPUs: A Developer's Guide

**Files:**
- Create: `site/src/content/blog/tpu-vs-gpu-developers-guide.md`

**Sources:** Ep 4
- Read summary: `ep-4-summary.md`
- Read transcript: `ep-4.md`
- Read shownotes: `episodes/ep-4.md`

**Angle:** Technical explainer for developers who use AI but don't understand the hardware. Not a hardware review — a "why should I care" piece that connects TPU/GPU architecture to the models and services developers use daily.

**Key content to extract:**
- Ep 4: Hardware Hut segment — systolic arrays vs GPU memory bandwidth, TPU skip memory round-trips for chained multiplications, TPU V5 (459 TFLOPS) to V7 (4,614 TFLOPS), Google started TPU design in 2013, why this matters for Gemini's speed

**Structural approach:** Comparative evaluation — TPUs and GPUs evaluated against consistent criteria relevant to developers (inference speed, training, cost, availability, what models run on what).

**Internal links:**
- Pillar: `/topics/ai-coding-agents-compared/`
- Glossary: `/glossary/benchmaxxed/`
- Episodes: `/episodes/4-open-ai-code-red-tpu-vs-gpu-and-more-autonomous-coding-agents/`

- [ ] **Step 1: Read source material** — summary, then transcript focusing on the Hardware Hut segment, then shownotes for any hardware-related links
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/tpu-vs-gpu-developers-guide.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 9: Spec-Driven Development in the Age of AI

**Files:**
- Create: `site/src/content/blog/spec-driven-development-ai.md`

**Sources:** Ep 5, 15, 16
- Read summaries: `ep-5-summary.md`, `ep-15-summary.md`, `ep-16-summary.md`
- Read transcripts: `ep-5.md`, `ep-15.md`, `ep-16.md`
- Read shownotes: `episodes/ep-5.md`, `episodes/ep-15.md`, `episodes/ep-16.md`

**Angle:** How specs become more important (not less) when AI writes the code. The argument: if AI generates code from prompts, the quality of the prompt-spec determines the quality of the output. Spec-driven development as the natural evolution of software engineering in the agentic age.

**Key content to extract:**
- Ep 5: how Anthropic engineers use AI, spec-driven development concept, the shift from writing code to writing specs
- Ep 15: "agile manifesto for the agentic age" discussion, connection to verification
- Ep 16: Pentagon-Anthropic drama context, verified spec-driven development (VSDD), interview with Martin Alderson

**Structural approach:** Progressive disclosure — from "what is spec-driven development" to "why AI makes it essential" to "how to actually do it" with increasing sophistication at each level.

**Internal links:**
- Pillar: `/topics/ai-coding-agents-compared/`, `/topics/ai-developer-careers/`
- Glossary: `/glossary/verification-debt/`, `/glossary/the-middle-loop/`
- Episodes: link to all three source episodes
- Blog: cross-link to post #1 (CLAUDE.md as a form of spec)

- [ ] **Step 1: Read source material** — summaries, then transcripts for spec-driven development discussions, then shownotes
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/spec-driven-development-ai.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 10: Dark Flow: Why Vibe Coding Feels Productive But Isn't

**Files:**
- Create: `site/src/content/blog/dark-flow-vibe-coding.md`

**Sources:** Ep 12
- Read summary: `ep-12-summary.md`
- Read transcript: `ep-12.md`
- Read shownotes: `episodes/ep-12.md`

**Angle:** The psychology of why vibe coding is addictive. "Dark flow" (from gambling research) applied to the experience of generating code with AI — the dopamine loop of seeing code appear, the illusion of progress, the moment you realize you don't understand what was built.

**Key content to extract:**
- Ep 12: dark flow concept (from fast.ai's Jeremy Howard or related source), the gambling analogy, how vibe coding creates the illusion of productivity, the OpenClaw saga as a cautionary tale, Anthropic's research on AI assistance and coding skills

**Structural approach:** Borrowed framework from psychology/gambling research. Dark flow as the organizing concept, with specific symptoms and countermeasures.

**Internal links:**
- Pillar: `/topics/vibe-coding-guide/`
- Glossary: `/glossary/dark-flow/`, `/glossary/cognitive-debt/`, `/glossary/cognitive-surrender/`
- Episodes: `/episodes/12-the-openclaw-saga-how-ai-affects-programming-skills-and-how-vibe-coding-is-addictive-like-gambling/`
- Blog: cross-link to post #2 (AI code bugs), post #4 (cognitive debt), post #15 (cognitive surrender)

- [ ] **Step 1: Read source material** — summary, then full transcript, then shownotes (especially the fast.ai "Breaking the Spell of Vibe Coding" and Anthropic coding skills research links)
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/dark-flow-vibe-coding.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 11: The AI Fluency Pyramid: From User to Native

**Files:**
- Create: `site/src/content/blog/ai-fluency-pyramid.md`

**Sources:** Ep 11
- Read summary: `ep-11-summary.md`
- Read transcript: `ep-11.md`
- Read shownotes: `episodes/ep-11.md`

**Angle:** Define and explain the AI fluency pyramid — a framework for understanding levels of AI adoption among developers. From basic usage to native integration. This is a coined-concept piece that gives readers a way to assess where they are and what the next level looks like.

**Key content to extract:**
- Ep 11: the AI fluency pyramid framework, the different levels, what distinguishes each level, practical examples, the Codex agent loop discussion, Claude Code's swarm mode

**Structural approach:** Numbered framework — each level of the pyramid is a section with "what it looks like," "how to get here," and "what's missing."

**Internal links:**
- Pillar: `/topics/ai-developer-careers/`
- Glossary: `/glossary/ai-fluency-pyramid/`
- Episodes: `/episodes/11-ai-fluency-pyramid-unrolling-the-codex-agent-loop-and-claude-code-s-secret-swarm-mode/`
- Blog: cross-link to post #9 (spec-driven development as a higher-fluency practice)

- [ ] **Step 1: Read source material** — summary, then full transcript, then shownotes
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/ai-fluency-pyramid.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 12: Workflow Automation Convexity: Why AI Won't Take Half Your Job

**Files:**
- Create: `site/src/content/blog/workflow-automation-convexity.md`

**Sources:** Ep 14
- Read summary: `ep-14-summary.md`
- Read transcript: `ep-14.md`
- Read shownotes: `episodes/ep-14.md`

**Angle:** Contrarian take on the "AI will automate X% of jobs" narrative. The argument: workflow automation is convex — easy tasks automate first but difficulty scales nonlinearly. The last 20% of a workflow might take 80% of the effort to automate, which is why "AI will do half your job" predictions consistently miss.

**Key content to extract:**
- Ep 14: workflow automation convexity concept, why partial automation is harder than it sounds, the convexity curve, practical examples from development workflows

**Structural approach:** Contrarian premise opening + data-first. Lead with the common prediction, then introduce convexity as the framework that explains why it's wrong.

**Internal links:**
- Pillar: `/topics/ai-developer-careers/`
- Glossary: `/glossary/workflow-automation-convexity/`
- Episodes: `/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt/`
- Blog: cross-link to post #11 (AI fluency pyramid — the higher levels require human judgment)

- [ ] **Step 1: Read source material** — summary, then full transcript for the convexity discussion, then shownotes
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/workflow-automation-convexity.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 13: Hallucination Neurons: Can We Turn Off LLM Lying?

**Files:**
- Create: `site/src/content/blog/hallucination-neurons-llm.md`

**Sources:** Ep 7
- Read summary: `ep-7-summary.md`
- Read transcript: `ep-7.md`
- Read shownotes: `episodes/ep-7.md`

**Angle:** Deep dive into the H-Neurons paper — researchers found specific neurons in LLMs associated with hallucination. What this means for the field, whether we can "turn off" hallucination, and the practical implications for developers who use LLMs daily.

**Key content to extract:**
- Ep 7: H-Neurons paper discussion (arxiv link in shownotes), specific findings about hallucination-associated neurons, implications for LLM reliability, connection to the broader hallucination problem

**Structural approach:** Data-first — lead with the paper's surprising finding, then progressive disclosure from "what they found" to "what it means" to "what developers should know."

**Internal links:**
- Pillar: `/topics/ai-security-developers/`
- Glossary: `/glossary/verification-debt/`
- Episodes: `/episodes/7-project-vend-update-hallucinating-neurons-and-year-end-reflections/`
- Blog: cross-link to post #2 (AI code bugs — hallucination as a source of bugs)

- [ ] **Step 1: Read source material** — summary, then full transcript focusing on the H-Neurons deep dive, then shownotes for the arxiv paper URL
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/hallucination-neurons-llm.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 14: We Tested 3 Models for Sycophancy

**Files:**
- Create: `site/src/content/blog/ai-sycophancy-test.md`

**Sources:** Ep 15, 20
- Read summaries: `ep-15-summary.md`, `ep-20-summary.md`
- Read transcripts: `ep-15.md`, `ep-20.md`
- Read shownotes: `episodes/ep-15.md`, `episodes/ep-20.md`

**Angle:** Empirical — the hosts tested multiple models for sycophantic behavior (telling users what they want to hear rather than the truth). Report the findings with specific examples, explain why sycophancy matters for code generation, and what developers can do about it.

**Key content to extract:**
- Ep 15: "convincing AI the earth is flat" experiment, sycophancy testing methodology, specific model responses
- Ep 20: emotion concepts in LLMs, how models respond to emotional pressure, connection to source leak discussion

**Structural approach:** Data-first — lead with the experiment and findings, then analyze what it means for AI-assisted development. Comparative evaluation of models against sycophancy criteria.

**Internal links:**
- Pillar: `/topics/ai-coding-agents-compared/`
- Glossary: `/glossary/agent-sycophancy/`
- Episodes: link to both source episodes
- Blog: cross-link to post #5 (model councils as sycophancy mitigation), post #7 (persuasion techniques), post #15 (cognitive surrender)

- [ ] **Step 1: Read source material** — summaries, then transcripts for sycophancy testing discussions, then shownotes
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/ai-sycophancy-test.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 15: Cognitive Surrender: What Happens When You Trust AI Too Much

**Files:**
- Create: `site/src/content/blog/cognitive-surrender-ai.md`

**Sources:** Ep 19
- Read summary: `ep-19-summary.md`
- Read transcript: `ep-19.md`
- Read shownotes: `episodes/ep-19.md`

**Angle:** The psychological phenomenon of deferring to AI even when you know better. Drawing on Kahneman's Thinking Fast and Slow (the episode's framing), explore how System 1 thinking leads developers to accept AI output without engaging System 2 verification.

**Key content to extract:**
- Ep 19: "thinking fast, slow, and artificial" framing, cognitive surrender concept, Meta's trouble with rogue agents, FOMO in the age of AI, specific examples of developers deferring to wrong AI output

**Structural approach:** Borrowed framework — Kahneman's System 1/System 2 applied to AI-assisted development. Each section maps a cognitive bias to a specific AI interaction failure mode.

**Internal links:**
- Pillar: `/topics/ai-developer-careers/`, `/topics/ai-security-developers/`
- Glossary: `/glossary/cognitive-surrender/`, `/glossary/cognitive-debt/`, `/glossary/cognitive-bankruptcy/`
- Episodes: `/episodes/19-thinking-fast-slow-and-artificial-meta-s-trouble-with-rogue-agents-and-fomo-in-the-age-of-ai/`
- Blog: cross-link to post #4 (cognitive debt), post #10 (dark flow), post #2 (AI code bugs)

- [ ] **Step 1: Read source material** — summary, then full transcript, then shownotes
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/cognitive-surrender-ai.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 16: What Claude Code's Source Leak Revealed

**Files:**
- Create: `site/src/content/blog/claude-code-source-leak.md`

**Sources:** Ep 20
- Read summary: `ep-20-summary.md`
- Read transcript: `ep-20.md`
- Read shownotes: `episodes/ep-20.md`

**Angle:** Analysis of what was revealed when Claude Code's source was leaked/published. Not gossip — technical analysis of the architecture, design decisions, and what it tells us about how Anthropic thinks about agentic coding tools.

**Key content to extract:**
- Ep 20: source leak details, architectural findings, design decisions revealed, implications for the agentic coding space, emotion concepts in LLMs

**Structural approach:** Progressive disclosure — from "what happened" to "what the code revealed" to "what it means for the field." Technical analysis with specific architectural observations.

**Internal links:**
- Pillar: `/topics/claude-code-guide/`, `/topics/ai-security-developers/`
- Glossary: `/glossary/the-middle-loop/`
- Episodes: `/episodes/20-claude-code-source-leak-emotion-concepts-in-llms-and-surprising-facts-ais-know-about-us/`
- Blog: cross-link to post #1 (CLAUDE.md best practices), post #3 (context loss detection)

- [ ] **Step 1: Read source material** — summary, then full transcript, then shownotes
- [ ] **Step 2: Write the blog post** — to `site/src/content/blog/claude-code-source-leak.md`
- [ ] **Step 3: Run voice checklist**

---

### Task 17: Build Verification

**Purpose:** Verify all 16 blog posts render correctly in the Astro site.

- [ ] **Step 1: Run Astro build**

```bash
cd /home/shimin/projects/adi_pod/site && npm run build
```

Expected: Build succeeds with no errors. All 16 blog posts appear in the build output.

- [ ] **Step 2: Verify blog index**

Check that `/blog/` lists all 16 posts by examining the build output or running dev server.

- [ ] **Step 3: Spot-check internal links**

Verify that internal links in 2-3 posts point to pages that exist (pillar pages, glossary entries, episode pages).
