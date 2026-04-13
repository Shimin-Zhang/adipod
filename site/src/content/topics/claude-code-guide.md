---
title: "The Complete Guide to Claude Code: Workflows, Tips, and the Stuff the Docs Don't Tell You"
description: "Everything we've learned about Claude Code across 20 episodes — context management, CLAUDE.md, plan mode, multi-agent workflows, and the pitfalls nobody warns you about."
slug: "claude-code-guide"
keywords: "Claude Code best practices, Claude Code tips, Claude.md guide, Claude Code workflow, Claude Code context management, Claude Code plan mode"
lastUpdated: "2026-04-10"
ogImage: "/og/claude-code-guide"
---

Claude Code is Anthropic's terminal-based AI coding agent that uses Claude models to read files, write code, and execute commands directly in your development environment. This guide covers the practical workflows, context management strategies, and configuration patterns we've learned from using Claude Code across 20 episodes of the ADI Pod — the tips the official documentation doesn't cover.

Most Claude Code guides read like product documentation wearing a blog post costume. Here's what they leave out: the moment your agent silently burns through 80% of its context window on MCP tool discovery before touching your actual task, or the slow realization that your carefully crafted CLAUDE.md file has been rotting for three weeks and nobody noticed.

We've spent 20 episodes using Claude Code on real projects — from solo side projects to multi-agent orchestration systems — and the gap between "how to use Claude Code" and "how Claude Code actually behaves in practice" is wide enough to park a data center in.

This guide covers what we've actually learned. Not the features list. The workflows, the failure modes, and the mental models that make the difference between productive AI-assisted development and expensive context window tourism.

## How to Manage Claude Code's Context Window

If there's one thing we'd tattoo on the forehead of every new Claude Code user, it's this: **context management is the central unsolved problem of agentic coding**.

Claude Code doesn't show context usage by default — there's no persistent progress bar on screen. You can check it manually with the `/context` command, and you should do so often. But in practice, most people don't, and then — without warning — the model starts repeating itself, missing obvious connections, or suggesting changes to files it read forty messages ago. Make `/context` a habit, not an afterthought. Dan put it well in [Episode 6](/episodes/6-gpt-5-2-claude-skills-and-hacker-hall-of-fame/): "You really don't have an indicator of where you're at while you're doing whatever that process is... it could be using a ton of context."

Some CLI alternatives like Kiro show you exactly how much context is consumed from the start — including what your MCP servers eat before you've typed a word. Claude Code doesn't, and that gap matters more than any individual feature.

### What actually eats context

Three things consume context faster than you'd expect:

1. **MCP tool discovery.** Every MCP server you configure injects its tool definitions into the context window at session start. Connect a Playwright server, a database server, and a file system server, and you've burned hundreds of tokens before asking your first question.

2. **File reads without specificity.** Asking Claude Code to "look at the codebase" is an invitation to read every file it can find. Be surgical: name the files, specify the line ranges, point it at the right directory.

3. **Conversation drift.** The longer a session runs, the more the context fills with intermediate reasoning, failed approaches, and tool call results you no longer need. There's no way to selectively prune this.

### Plan mode as context management

One of Opus 4.6's less-discussed behaviors is that it will proactively drop into plan mode and offer to write a `plan.md` file when it senses a task is complex enough to exceed a single context window. This is not a bug — it's the model managing its own limitations.

The plan file becomes a persistent artifact that survives context resets. You can clear the context, start a fresh session, and tell Claude Code to read `plan.md` and continue from step 4. We covered this in [Episode 13](/episodes/13-pi-coding-agent-dark-factories-the-furniture-makers-of-carolina/), and it's become one of our most-used patterns. The key insight: **let the agent write the plan, then use the plan to outlive the agent's context**.

## What to Put in Your CLAUDE.md File

Your CLAUDE.md file is not a README. It's a system prompt extension, and it deserves the same maintenance discipline as any other configuration file in your repository.

### What belongs in CLAUDE.md

The effective pattern we've converged on across episodes:

- **Project architecture in one paragraph.** What framework, what patterns, where things live. Not a tutorial — a map.
- **Commands that matter.** How to run tests, how to build, how to deploy. The things you'd tell a new team member on day one.
- **Conventions the model can't infer from code.** Naming patterns, file organization rules, import ordering preferences. If it's in your linter config, you don't need to repeat it here.
- **What not to do.** Explicit prohibitions save more time than positive instructions. "Never modify the migration files directly" prevents more damage than "use the migration generator."
- **Progressive disclosure through linked prompts.** Keep your CLAUDE.md lean — project overview, key commands, hard constraints. Then link out to separate prompt files for specific areas of work: a `FRONTEND.md` for UI conventions, a `DATABASE.md` for migration rules, a `TESTING.md` for test patterns. The agent pulls in the relevant prompt when it's working in that area, rather than loading everything into context upfront. This keeps your base context small and your domain-specific instructions detailed without the tradeoff.

### What doesn't belong

- Documentation of obvious language features
- Lengthy architectural decision records (link to them instead)
- Instructions so detailed they consume significant context before the model starts working

### Prompt debt is real

We coined the term [prompt debt](/glossary/prompt-debt/) in [Episode 17](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams/) to describe what happens when your CLAUDE.md and agents.md files rot. Dan's reaction captured it perfectly: "We have prompt debt now too? In addition to technical debt?"

Yes. Yes we do. Your CLAUDE.md references a testing framework you migrated off of two sprints ago. Your agents.md describes a directory structure that was reorganized last week. The model follows these stale instructions faithfully, producing technically correct code that's architecturally wrong.

The fix is boring but necessary: treat CLAUDE.md updates as part of your PR process. Changed the test runner? Update CLAUDE.md. Moved the API routes? Update CLAUDE.md. It's configuration as code, and configuration that lies is worse than no configuration at all.

## How to Run Multiple Claude Code Agents

Claude Code's multi-agent capabilities have evolved from a hidden feature to a core workflow, and the progression tells you something about where agentic coding is headed.

### Swarm mode

[Episode 11](/episodes/11-ai-fluency-pyramid-unrolling-the-codex-agent-loop-and-claude-code-s-secret-swarm-mode/) covered Claude Code's swarm mode — the ability to run multiple Claude Code instances concurrently, typically using git worktrees to avoid file conflicts. The promise: parallelize independent tasks the way a well-organized team would.

The reality is more nuanced. When I tried running multiple agents through Gas Town (Steve Yegge's Kubernetes-like orchestrator for Claude Code agents, covered in [Episode 10](/episodes/10-there-s-a-new-sherif-in-the-gas-town-of-ai-software-development/)), the results were mixed. In [Episode 11](/episodes/11-ai-fluency-pyramid-unrolling-the-codex-agent-loop-and-claude-code-s-secret-swarm-mode/), I reported going back to being the overseer and trying to do less prompt engineering and less oversight — and it didn't work nearly as well. Humans are still needed as of right now.

The problem isn't the agents. It's the management overhead. [Context switching burnout from running multiple agent instances](/glossary/cognitive-bankruptcy/) is an emerging occupational hazard. You're not coding anymore — you're project-managing four agents who each need context, direction, and review. The [everyone is a manager now](/episodes/13-pi-coding-agent-dark-factories-the-furniture-makers-of-carolina/) framing resonates because it describes the dopamine loss accurately: you're doing more, but it doesn't feel like building.

### Worktrees are non-negotiable

If you're running concurrent agents without git worktrees, you're going to have a bad time. Two agents editing the same file is a merge conflict factory. Worktrees give each agent an isolated copy of the repository, and Claude Code's worktree support makes this nearly seamless.

The pattern: create a worktree per agent, assign each agent a scoped task (one feature, one bug fix, one refactor), and merge the results. The key constraint is that the tasks must be genuinely independent — two agents touching the same module's internals will produce conflicts regardless of worktrees.

## The Source Code Leak and What It Revealed

In March 2026, Claude Code's entire source code leaked via an exposed source map file — a Bun bundling bug that left the internals readable. We covered it extensively in [Episode 20](/episodes/20-claude-code-source-leak-emotion-concepts-in-llms-and-surprising-facts-ais-know-about-us/), and several findings were genuinely surprising.

### Dual-track permission system

Claude Code doesn't just pattern-match against a list of dangerous commands. It runs a **dual-track system**: rule-based permissions for known patterns, plus a machine learning classifier that evaluates whether arbitrary bash commands could be destructive. The ML classifier is the interesting part — it means Claude Code is making judgment calls about command safety, not just string matching.

### Frustration regexes

The source revealed that Claude Code uses regex pattern matching — not the model itself — to detect when users are frustrated. There's something deeply ironic about a state-of-the-art language model's tooling using regex for sentiment analysis.

### Hidden features

The leak exposed several unannounced features: **Kairos** (persistent mode with memory consolidation between sessions), **Dream mode** (automatic memory consolidation), and the coordinator mode for multi-agent orchestration. It also revealed anti-distillation protections — if Claude Code detects you're trying to distill its behavior, it generates fake tools.

## The Pi Agent Alternative: Less Scaffolding, More Intelligence

Not everything we've learned about Claude Code is about Claude Code itself. In [Episode 13](/episodes/13-pi-coding-agent-dark-factories-the-furniture-makers-of-carolina/), we did a deep dive on Mario Zechner's Pi coding agent, and it reshaped how I think about AI tooling.

Pi is radically simple. Four layers of abstraction: a unified model provider API, a terminal UI, a lightweight agent with a tiny system prompt, and a skills layer built from markdown and bash scripts. No MCP by default. No plan mode. The agent knows four things: read, write, bash, and skills.

I actually prefer Pi Agent over Claude Code for non-coding tasks. I've built a memory skill, a Telegram skill, a research agent using curl, a cron agent, and a Gmail agent. The line from workflow automation to agent is probably easier than the other way around. And Claude Code is more specific.

The philosophical takeaway — and this may be controversial — is that Pi represents what Rich Sutton called the "bitter lesson" of AI: when your agent becomes sufficiently intelligent, the additional scaffolding actually hinders it. Claude Code's feature velocity (skills, swarm mode, channels, scheduling, /insights, plugins) is impressive, but the [moat may only be in the general model capabilities, not the tooling](/episodes/19-thinking-fast-slow-and-artificial-meta-s-trouble-with-rogue-agents-and-fomo-in-the-age-of-ai/).

## Verification and Guardrails

Claude Code can write a lot of code very fast. The question is whether anyone understands what it wrote.

### Verification debt

We introduced the concept of [verification debt](/glossary/verification-debt/) in [Episode 6](/episodes/6-gpt-5-2-claude-skills-and-hacker-hall-of-fame/) — the accumulated cost of AI output that was never meaningfully reviewed. Every diff you approve without understanding adds to the balance. The interest compounds when new code builds on top of code nobody grasped in the first place.

### VSDD: Verified Spec-Driven Development

[Episode 16](/episodes/16-pentagon-anthropic-drama-verified-spec-driven-development-and-interview-with-martin-alderson/) introduced VSDD — a methodology combining spec-driven development, TDD, and adversarial verification gates at each phase. I tested it on a side project using Claude Code, and while it's heavier than just prompting and accepting, the code quality difference is meaningful. The adversarial verification step is the key innovation: after the agent generates code, you systematically try to break it before moving on.

### Architectural guardrails as agent multipliers

In human workflows, linters and invariant checks might feel pedantic or constraining. With agents, they become multipliers. An agent that runs into a linter error will fix it. An agent working without guardrails will cheerfully generate code that passes tests but violates every architectural convention your team spent months establishing.

The practical advice from [Episode 17](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams/): enforce architectural boundaries, invariants, and custom linters before giving agents free rein. The five minutes spent configuring a linter rule saves hours of reviewing agent output that technically works but doesn't belong.

## Team Dynamics: AI as Force Multiplier

AI is a force multiplier for your team culture. The good teams move faster. The bad teams explode faster.

This is probably the most underappreciated insight from our coverage. Claude Code doesn't create team problems — it amplifies existing ones. A team with clear conventions, good test coverage, and healthy review practices will use Claude Code to ship faster. A team with tribal knowledge, inconsistent patterns, and review rubber-stamping will use Claude Code to generate technical debt at unprecedented velocity.

### The review fatigue problem

Amazon now requires senior engineers to sign off on AI-assisted changes after a series of AI-caused outages. The intention is sound. The execution is unsustainable. Senior engineers will not just become code review machines all day, because that is unsustainable. It will burn developers out.

The alternative: invest in automated guardrails (linters, tests, invariant checks) that catch the mechanical problems, and reserve human review for architectural decisions and business logic. Let machines review machine output where possible.

### Cross-functional pair programming

The bright spot: cross-functional pair programming with AI — a PM and an engineer working with Claude Code together — represents a genuinely new collaboration pattern. The PM provides context and requirements in natural language, the engineer provides architectural guidance, and Claude Code handles implementation. When it works, it collapses the spec-to-implementation cycle from days to hours.

## Practical Workflow Tips

These are the patterns we've converged on after 20 episodes of daily Claude Code usage:

**Start sessions with scope.** Tell Claude Code what you're doing, what files matter, and what you're not touching. A focused agent is a productive agent.

**Use plan mode for anything longer than 20 minutes.** If the task is complex enough that you'd break it into subtasks for a human, break it into a plan for the agent. The plan file survives context resets.

**Audit your MCP connections.** Every MCP server you connect eats context. If you're not actively using a server, disconnect it for the session.

**Treat CLAUDE.md like a config file.** Review it in PRs. Update it when architecture changes. Delete instructions that reference removed features.

**Use [code garbage collection](/glossary/code-garbage-collection/).** Periodically point Claude Code at your codebase and ask it to identify dead code, unused dependencies, and stale configurations. AI is good at finding the cruft that AI-assisted development creates.

**Don't fight the permissions model.** The dual-track permission system exists for good reasons. If you find yourself wanting to bypass it, you're probably about to do something you should think about more carefully.

## Frequently Asked Questions

### How do I know when Claude Code has lost context?

The symptoms: repetitive suggestions, asking about information it already received, proposing changes to files it read earlier in the session but now seems to have forgotten, or generating code that contradicts its own plan. When you see these, it's time to write a plan file and start a fresh session.

### Should I use Claude Code or an IDE-based agent like Cursor?

They're different tools for different workflows. Claude Code is terminal-native and excels at tasks that span multiple files, require bash commands, or involve system-level operations. IDE-based agents are better when you're editing a single file and want inline suggestions. Martin Alderson noted in [Episode 16](/episodes/16-pentagon-anthropic-drama-verified-spec-driven-development-and-interview-with-martin-alderson/) that the permissions model creates muscle memory — switching between tools is higher friction than you'd expect.

### Is Claude Code the right tool for non-coding tasks?

It can work, but the Pi Agent or similar minimal frameworks are often better suited. Claude Code's tooling infrastructure is optimized for software engineering workflows. For general automation, a lighter agent that lets you build skills from markdown and bash may be more flexible.

### How much context does Claude Code actually have?

The exact number varies by model, but the practical limit is lower than the theoretical maximum because of MCP tool definitions, system prompts, conversation history, and file reads. Plan for your actual task to have roughly 60-70% of the advertised context window available after overhead.

### What's the best way to handle multiple concurrent tasks?

Git worktrees with one agent per worktree, scoped to genuinely independent tasks. Use a plan file to coordinate across agents, and merge results via pull requests. Don't try to run multiple agents in the same worktree — the file conflicts aren't worth the saved setup time.

### Is the model or the tooling more important?

Based on everything we've covered: the model. Claude Code's feature velocity is impressive, but competitors are converging on similar tooling. The biggest compliment for Codex 5.3, as we noted in [Episode 13](/episodes/13-pi-coding-agent-dark-factories-the-furniture-makers-of-carolina/), is that it feels like Claude Code now. The differentiation is in the model's reasoning, not the wrapper. Pi Agent's success with minimal tooling reinforces this — when the model is good enough, elaborate scaffolding can be a hindrance rather than a help.

### How do I avoid accumulating cognitive debt with Claude Code?

Read every diff before approving it. If you don't understand a change, don't merge it — ask the agent to explain it or rewrite it more simply. Use [VSDD](/episodes/16-pentagon-anthropic-drama-verified-spec-driven-development-and-interview-with-martin-alderson/) for anything going to production. And periodically, close Claude Code and read your own codebase without AI assistance. The moment you can't trace a data flow through your own code, you're approaching [cognitive bankruptcy](/glossary/cognitive-bankruptcy/).

---

*This guide is a living document. We update it as new episodes cover Claude Code developments. Last updated April 2026 based on content through [Episode 20](/episodes/20-claude-code-source-leak-emotion-concepts-in-llms-and-surprising-facts-ais-know-about-us/).*
