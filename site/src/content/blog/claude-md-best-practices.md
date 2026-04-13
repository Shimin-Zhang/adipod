---
title: "CLAUDE.md Best Practices: 7 Things to Put In and 3 to Leave Out"
description: "CLAUDE.md is a finite instruction budget of ~150-200 slots, not a knowledge dump. Here is what to include, what to leave out, and how to prevent prompt debt."
date: "2026-04-11"
lastUpdated: "2026-04-12"
slug: "claude-md-best-practices"
keywords: "Claude.md best practices, Claude.md guide, Claude Code configuration"
episodes: ["4", "10", "17"]
---

CLAUDE.md best practices come down to one principle: treat the file as a finite instruction budget, not a knowledge base. Frontier models can reliably follow roughly 150 to 200 discrete instructions before performance degrades — that is your budget, and most teams blow through it by week two.

Your CLAUDE.md file is slowly rotting, and you probably have not noticed yet.

This is not a metaphor. It is the same failure mode as any configuration artifact that humans write once and forget: the instructions drift from the codebase they describe, contradictions accumulate, and the agent starts ignoring your carefully written rules — not out of defiance, but because you have given it more directives than it can hold in its effective reasoning window. According to a [HumanLayer analysis](https://www.humanlayer.dev/blog/writing-a-good-claude-md), frontier models can reliably follow roughly 150 to 200 discrete instructions before performance degrades. That is your budget. Most teams blow through it by week two.

I have spent the better part of five months working with CLAUDE.md files across projects of varying size — from side projects to production monorepos — and discussing what works with [my co-host Dan Lasky](/episodes/4-open-ai-code-red-tpu-vs-gpu-and-more-autonomous-coding-agents/) on the ADI Pod. What follows is a framework for treating your CLAUDE.md as what it actually is: a configuration artifact with real constraints, not a wiki page for your AI assistant.

## The Instruction Stack: Why Less Is More

Before the framework, you need a mental model of what happens when Claude Code boots up.

The first thing Claude reads is not your CLAUDE.md. It is the system prompt from Anthropic — a set of 35-plus instructions governing safety, tool usage, and base behavior. Then comes your CLAUDE.md. Then comes the user's actual request. By the time your "please always use TypeScript strict mode" instruction reaches the model, it is competing with potentially hundreds of prior directives for attention.

Dan described working in a monorepo where a colleague had written a CLAUDE.md that was [40,000 lines long](/episodes/4-open-ai-code-red-tpu-vs-gpu-and-more-autonomous-coding-agents/). It covered every tool in the monorepo setup. The result was predictable: Claude ignored it frequently, because the instruction set had exceeded the model's effective logical window. Not the context window — models can hold far more tokens than they can reliably act on. The distinction matters.

Think of it this way. Your CLAUDE.md is not the first page of a manual the agent reads cover to cover. It is more like the second page of a briefing that already has a first page you did not write and cannot edit. The instructions on that second page can even contradict the first, which — as we discussed on the show — would explain [why Claude sometimes ignores CLAUDE.md directives entirely](/episodes/4-open-ai-code-red-tpu-vs-gpu-and-more-autonomous-coding-agents/).

## The Framework: 7 Things to Put In

I am borrowing the progressive disclosure pattern here — a concept from UI design where you reveal complexity only when the user needs it. [OpenAI's harness engineering team](https://openai.com/index/harness-engineering/) independently converged on the same principle after five months of agent-only development: your agents.md should be "a map, not a manual."

### 1. Project Identity in Three Sentences

What is this project, what framework does it use, and what is the primary language. Not a paragraph. Three sentences. The agent needs orientation, not a history lesson.

### 2. How to Run the Tests

This is the single highest-value instruction you can include. Agents that cannot verify their own work will hallucinate success — we have both seen Claude report all tests passing without having run them, or worse, [write fake tests to inflate coverage metrics](/episodes/4-open-ai-code-red-tpu-vs-gpu-and-more-autonomous-coding-agents/). The command to run tests, the expected output format, and what a failure looks like: put it right here.

### 3. Architectural Invariants

Not coding conventions. Invariants. "All API routes must go through the middleware layer." "No direct database queries outside the repository pattern." These are the constraints that, if violated, produce bugs that are hard to catch in review. OpenAI's harness engineering team found that [enforcing architectural boundaries via invariants and custom linters](https://openai.com/index/harness-engineering/) was one of the highest-leverage interventions for agent code quality — rules that feel pedantic to human developers become force multipliers for agents.

### 4. A Nickname for Context Loss Detection

This is my favorite trick, and I [shared it on the show](/episodes/4-open-ai-code-red-tpu-vs-gpu-and-more-autonomous-coding-agents/) after finding it on Hacker News. Add an instruction like: "Always address me as Sheminsky when responding." When the agent stops using your nickname, it has lost your CLAUDE.md context. No ambiguity, no guessing — you have a binary signal that the instruction set has fallen out of the reasoning window.

I have been using this for months now. It is not foolproof, but it is the cheapest early-warning system I have found for context degradation.

### 5. Progressive Disclosure Pointers

Instead of putting your database migration guide, test coverage conventions, and code style rules directly in CLAUDE.md, create separate markdown files and reference them: "For database migration instructions, read `docs/migrations.md`." The agent is smart enough to know when to pull in additional context. You preserve your instruction budget for the high-level map, and the detailed instructions live where they can be maintained independently.

Dan [put it concisely](/episodes/4-open-ai-code-red-tpu-vs-gpu-and-more-autonomous-coding-agents/): "It's like, read this markdown file if you need this." You can put excruciating detail in those linked files — how to check coverage, database migration steps, code conventions — without bloating the primary instruction set.

### 6. What the Agent Should Do When Stuck

Agents fail silently by default. They will generate plausible-looking code rather than admit confusion. Include explicit instructions: "If tests fail after two attempts, stop and report the failure rather than attempting further fixes." "If you are unsure about the architectural pattern for a new feature, ask before implementing." This is not hand-holding — it is the difference between a 20-minute PR fix and a 200-line cleanup.

### 7. The Things That Would Embarrass You in Review

Every team has the mistakes that junior engineers make once and seniors never make again. The ORM that silently drops constraints if you pass the wrong option. The API endpoint that needs authentication headers in staging but not development. These are high-signal, low-volume instructions — the kind that justify their slot in your 150-instruction budget.

## The 3 Things to Leave Out

### 1. General Coding Style Rules

"Use camelCase for variables." "Prefer const over let." These belong in your linter configuration, not your CLAUDE.md. If ESLint or Prettier can enforce it, do not waste an instruction slot on it. The OpenAI team's experience [confirmed this](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams/): custom linters and structural tests are more reliable than prose instructions for style enforcement.

### 2. Exhaustive Tool Documentation

If your monorepo has 40 build tools, do not document all of them in CLAUDE.md. Document the one the agent is most likely to need, and use progressive disclosure for the rest. The 40,000-line CLAUDE.md is a cautionary tale, not an aspiration.

### 3. Anything Contradicting the System Prompt

You cannot override the system prompt. Trying to — "ignore all previous safety instructions," obviously, but also subtler contradictions like redefining how the agent should handle file operations — will create unpredictable behavior. Your CLAUDE.md instructions compete with the system prompt for attention, and when they conflict, the result is not a clean override. It is inconsistency.

## The Maintenance Problem Nobody Talks About

Here is where most CLAUDE.md guides end. Here is where the actual work begins.

Dan made an observation on a [recent episode](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams/) that stuck with me. He was discussing [OpenAI's harness engineering article](https://openai.com/index/harness-engineering/) and said, with genuine alarm: "We have [prompt debt](/glossary/prompt-debt/) now too? In addition to technical debt?" He described working on codebases with extensive agents.md files where humans had simply stopped updating them — the instructions had drifted from the codebase, and nobody was maintaining the configuration artifact that was supposed to guide the agents writing the code.

This is the same failure mode as stale documentation, except the consequences are more immediate. A stale README confuses a human developer who can compensate with judgment. A stale CLAUDE.md actively misleads an agent that will follow outdated instructions with perfect compliance.

The parallel to [code garbage collection](/glossary/code-garbage-collection/) is direct. OpenAI's team built a recurring cleanup process into their agent workflow — periodic passes where agents would clean up duplication, refactor accumulated slop, and tighten the codebase. Your CLAUDE.md needs the same treatment. Not a quarterly review. A regular cadence — I would suggest every sprint — where someone reads the CLAUDE.md against the current codebase and asks: is this still true?

Boris Cherny, [one of the creators of Claude Code](https://www.reddit.com/r/ClaudeAI/comments/1q2c0ne/comment/nxc4ap6/), shared his team's approach in a thread we [covered on the show](/episodes/10-there-s-a-new-sherif-in-the-gas-town-of-ai-software-development/): every team has its own CLAUDE.md, maintained as a team artifact rather than an individual's side project. The Claude Code team ships 50 to 100 PRs per person per week using branch-based multi-agent development, and the CLAUDE.md is a living part of that workflow — not a write-once configuration file gathering dust.

The pattern here matters more than the specifics. If your CLAUDE.md is owned by one person, it will rot. If it is not version-controlled alongside the code it describes, it will drift. If nobody reviews changes to it, the [prompt debt](/glossary/prompt-debt/) will compound exactly like technical debt — silently, then suddenly.

## A Starter Template

If you are starting from scratch, here is the minimal viable CLAUDE.md:

```markdown
# Project: [Name]
[One sentence: what this is. One sentence: primary framework/language. One sentence: key constraint or convention.]

Always address me as [your nickname].

## Running Tests
[Exact command. Expected output. What failure looks like.]

## Architectural Rules
- [Invariant 1]
- [Invariant 2]

## When Stuck
If tests fail after two attempts, stop and ask.

## Additional Context
- For [topic]: read `docs/[file].md`
- For [topic]: read `docs/[file].md`
```

That is roughly 15 instructions. You have 135 to 185 remaining. Spend them wisely.

## The Bigger Picture

The CLAUDE.md file is a microcosm of a larger shift in software engineering. We are moving from a world where configuration meant telling machines exactly what to do — deterministic, explicit, complete — to one where configuration means giving agents enough context to make reasonable decisions on their own. The constraints of the instruction budget are not a limitation of current models that will be solved by longer context windows. They are a fundamental property of how instruction-following works: more directives mean more opportunities for contradiction, more competition for attention, and more surface area for drift.

The teams that treat their CLAUDE.md as a living configuration artifact — maintained, reviewed, and garbage-collected like the code it governs — will get more from their agents than the teams that treat it as a write-once knowledge dump. The file is small. The discipline is not.

For a broader look at [Claude Code workflows, agent orchestration, and the tooling ecosystem](/topics/claude-code-guide/), the landscape is evolving fast. But the CLAUDE.md file is where it starts — and for most teams, where it quietly breaks down.
