---
term: "Code Garbage Collection"
definition: "The practice of periodically using AI coding tools to identify and remove dead code, unused dependencies, stale configurations, and other accumulated cruft from a codebase -- the software equivalent of garbage collection in memory management."
slug: "code-garbage-collection"
episodes: ["17"]
aliases: ["code GC"]
---

## Context

The concept was discussed on [Episode 17](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams) of ADI Pod, where the hosts identified periodic AI-driven cleanup as an emerging best practice. Justin Jackson's ["Will Claude Code ruin our team?"](https://justinjackson.ca/claude-code-ruin) framed the broader concern: AI coding tools reshape team dynamics, and unchecked output accumulates fast. The episode title frames the response as "slop garbage collection" -- using AI tools to clean up the very mess that AI-assisted development can create. The term borrows from runtime garbage collection in programming languages, where the system automatically reclaims unused memory, and applies the same principle to source code.

## Why It Matters

AI coding tools make it trivially easy to generate code -- and to generate *too much* code. Unused utility functions, redundant abstractions, over-engineered configurations. Traditional codebases accumulated cruft over years. AI-assisted codebases can accumulate it in weeks. When the consequences get severe, organizations intervene: as [Ars Technica reported](https://arstechnica.com/ai/2026/03/after-outages-amazon-to-make-senior-engineers-sign-off-on-ai-assisted-changes/), Amazon now requires senior engineers to sign off on AI-assisted changes after outages linked to unreviewed AI-generated code.

The irony is that the same tools creating the problem are well-suited to solving it. OpenAI's ["Harness engineering"](https://openai.com/index/harness-engineering/) post explicitly references code garbage collection as a practice within their agent-first development model. AI agents can scan for dead code paths, flag unused imports, identify duplicated logic, and suggest removals with a patience that humans lack.

Code garbage collection pairs naturally with [prompt debt](/glossary/prompt-debt). As `agents.md` files and prompt templates rot, the code they produce degrades too. Regular cleanup passes address both the outputs (generated code) and the inputs (the prompts driving generation).

## Example

A team using AI pair programming notices their service has grown by 40% in three months, but feature count has not kept pace. They task an AI agent with auditing the codebase: it finds 12 unused helper modules, three deprecated API clients still imported everywhere, and a test utilities directory that nothing references. A single cleanup PR removes 3,000 lines. The build gets faster, onboarding gets simpler, and the next AI-assisted feature lands cleaner because the context window is no longer polluted with dead code.

## Related Concepts

- [Verification debt](/glossary/verification-debt) -- unreviewed AI output is a primary source of the cruft that code garbage collection targets.
- [Dark flow](/glossary/dark-flow) -- the false productivity that leads teams to ship more code than they audit, creating the need for periodic cleanup.
