---
term: "Prompt Debt"
definition: "The accumulated maintenance burden of AI agent instructions -- such as agents.md files, system prompts, and coding guidelines -- that rot over time just like the code they govern, creating a parallel layer of technical debt."
slug: "prompt-debt"
episodes: ["17"]
aliases: []
---

## Context

The concept surfaced in [Episode 17](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams) of ADI Pod during a discussion prompted by Justin Jackson's post ["Will Claude Code ruin our team?"](https://justinjackson.ca/claude-code-ruin), which examined how AI coding tools affect team dynamics. As teams increasingly rely on agent configuration files -- `agents.md`, `CLAUDE.md`, `.cursorrules`, and similar instruction sets -- those files become load-bearing infrastructure. They encode architectural decisions, style preferences, and behavioral constraints that shape every line an agent produces. When those instructions drift out of sync with the actual codebase, the agent starts generating code that conflicts with current patterns or silently violates conventions the team has since adopted.

## Why it matters

Traditional technical debt is well-understood: shortcuts in code that cost more to fix later. Prompt debt is its shadow in the AI-assisted workflow. The instructions you give your agents are themselves artifacts that require maintenance, review, and versioning. An `agents.md` file written during project setup may reference directory structures that no longer exist, testing frameworks that were swapped out, or patterns the team abandoned. Unlike stale documentation, which developers can ignore, stale agent instructions actively produce wrong output -- the agent follows them faithfully.

The insidious part is that prompt debt is often invisible. A developer who inherits a project may never read the agent configuration. They invoke the agent, get plausible-looking code, and merge it -- not realizing it was shaped by outdated instructions. This makes prompt debt a direct contributor to [verification debt](/glossary/verification-debt), since the generated code looks correct but was built on false premises. Amazon confronted this directly: after AI-related outages, it began [requiring senior engineers to sign off on AI-assisted changes](https://arstechnica.com/ai/2026/03/after-outages-amazon-to-make-senior-engineers-sign-off-on-ai-assisted-changes/).

## Mitigation

Treat agent instruction files like code: put them in version control, review them in PRs, and schedule periodic audits. OpenAI's ["Harness engineering"](https://openai.com/index/harness-engineering/) framework advocates structuring agent workflows so that guardrails stay aligned with evolving codebases -- the same discipline applies to prompt files. Some teams extend [code garbage collection](/glossary/code-garbage-collection) practices -- periodic AI-driven sweeps that flag stale patterns -- to their agent configurations. If your `agents.md` has not been updated since the project's architecture last changed, it is already accruing interest.

## Related concepts

- [Verification debt](/glossary/verification-debt) -- the cost of shipping AI-generated code without adequate review, compounded when the agent's own instructions are stale
- [Cognitive bankruptcy](/glossary/cognitive-bankruptcy) -- the failure state that prompt debt accelerates, where no one understands the system well enough to maintain it
