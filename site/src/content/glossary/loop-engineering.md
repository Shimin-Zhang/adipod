---
term: "Loop Engineering"
definition: "Building out the supporting infrastructure around a bare agent loop -- scheduled automations, worktrees, skills, plugins, subagents, and memory -- so that a simple 'run until the goal is reached' loop becomes a dependable, self-correcting coding harness."
slug: "loop-engineering"
episodes: ["30"]
aliases: ["loop engineering", "agent loop engineering"]
---

## Context

Loop engineering was named by Addy Osmani in his essay "Loop Engineering" and covered on [Episode 30](/episodes/30-fable-5-ban-metas-ai-gulag-elias-thorne-loop-engineering/) of the ADI Pod. It starts from the Ralph loop -- a `/loop` that runs an agent over and over until a goal is reached -- and names the pieces that turn that bare loop into a real harness:

- **Scheduled automations** (the "heartbeat") that run on a timer and do discovery and triage on their own.
- **Worktrees** so multiple agents can work the same repo without stepping on each other. The industry consolidated here after early Gas Town used multiple full copies of the repository.
- **Skills** that write down project knowledge the agent would otherwise guess at -- the main defense against hallucination and against an agent thrashing without learning from past mistakes.
- **Plugins and connectors** so the agent can reach past the local filesystem to external systems.
- **Subagents**, where the load-bearing move is to split the agent that *does* the work from the agent that *reviews* it.
- **Memory** -- a markdown file, a ticket board, anything that persists outside the core loop.

By this definition, both the Codex app and Claude Code are already full loop-engineering harnesses; the term is more generic than any one implementation.

## Why It Matters

Shimin's framing on the show traces a progression in how developers direct agents: prompt engineering (tell the agent what to do) → [spec-driven development](/blog/spec-driven-development-ai/) (define the end goal precisely) → loop engineering (keep the goal looser, but bake your judgment into reusable skills and tools). Because the loop turns out so much more code, it *amplifies* whatever judgment you implant: the metaphor on the episode ran handsaw → table saw ("watch your fingers") → tree-harvesting heavy machinery, where a mistake risks far more.

The drawbacks Osmani names are the ones the show keeps returning to: verification still falls on the developer (skip it and the output drifts), and [cognitive debt](/glossary/cognitive-debt) bites hardest when a self-running loop breaks at 3am and no one understands the repo anymore.

## Related Concepts

- [The middle loop](/glossary/the-middle-loop) -- the human work of overseeing agents, parts of which loop engineering automates
- [Cognitive debt](/glossary/cognitive-debt) -- the accumulating risk when a loop produces code no human has read
- [Workflow automation convexity](/glossary/workflow-automation-convexity) -- the economic backdrop: workflows that approach full automation flip suddenly, not gradually
