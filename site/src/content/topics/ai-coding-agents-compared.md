---
title: "AI Coding Agents Compared: Claude Code, Codex, Cursor, Pi Agent, and the Rest"
description: "A practitioner's comparison of AI coding agents — what each tool actually does well, where they fall short, and why the moat might not be in the tooling."
slug: "ai-coding-agents-compared"
keywords: "Claude Code vs Cursor, AI coding agent comparison, best AI coding tool, Claude Code vs Codex, AI coding agent review 2026"
lastUpdated: "2026-04-10"
---

The AI coding agent market has a benchmarking problem: every tool claims SWE-bench superiority, every launch post uses the word "revolutionary," and the actual experience of using these tools day-to-day bears approximately zero resemblance to the marketing.

We've used Claude Code, Codex, Cursor, Pi Agent, Gas Town, Open Code, Gemini CLI, and Kiro CLI across 20 episodes of the ADI Pod. Not as reviewers testing features for a week. As practitioners shipping code on real projects. The differences between these tools are real, but they're not the differences the comparison posts focus on.

Here's what actually matters when choosing an AI coding agent.

## The Fundamental Split: Terminal vs. IDE vs. Cloud

Before comparing individual tools, the more important decision is which paradigm fits your workflow. The three paradigms aren't just UI preferences — they imply different models of human-agent interaction.

**Terminal agents** (Claude Code, Pi Agent, Codex CLI, Gemini CLI, Kiro CLI) run in your terminal. You interact through text. The agent reads files, runs commands, and makes changes directly on your filesystem. The workflow feels like pair programming with someone who happens to be very fast at typing.

**IDE agents** (Cursor, Copilot, Windsurf) embed in your editor. The agent sees what you see and suggests changes inline. The workflow feels like autocomplete on steroids — the agent is reactive, responding to what you're doing rather than pursuing independent tasks.

**Cloud agents** (Codex cloud mode, Devin) run asynchronously in sandboxed environments. You give them a task and come back later. The workflow feels like delegating to a remote contractor.

The hosts of this show strongly prefer terminal agents. Not because terminal agents are objectively better — because they match how we think about coding tasks. Your mileage will vary, and that's fine.

## [Claude Code](https://claude.ai/code)

We've covered Claude Code more than any other tool, so this section has the most nuance. See also the dedicated [Claude Code guide](/topics/claude-code-guide/) for deeper coverage.

### Strengths

**Initiative.** Opus 4.6 in Claude Code takes genuine initiative. It will run tests, interpret failures, fix issues, and present finished work — not just generate code and ask what to do next. In [Episode 13](/episodes/13-pi-coding-agent-dark-factories-the-furniture-makers-of-carolina/), the contrast with Codex was stark: "Instead of automatically releasing the coding swarm, [Codex] does a section of the work and asks me, do you want to continue? Whereas Claude Code with 4.6 just did the whole thing, beginning to end, and then verified its work."

**Permissions model.** The dual-track permission system (rule-based + ML classifier, revealed in the [source code leak](/episodes/20-claude-code-source-leak-emotion-concepts-in-llms-and-surprising-facts-ais-know-about-us/)) creates muscle memory. Martin Alderson noted in [Episode 16](/episodes/16-pentagon-anthropic-drama-verified-spec-driven-development-and-interview-with-martin-alderson/): "I've got so used to Claude Code and the permissions model. When I switched even to Codex, which has come on loads, I don't know, it just doesn't quite gel right."

**Skills ecosystem.** The ability to create and chain skills — covered in depth in [Episode 6](/episodes/6-gpt-5-2-claude-skills-and-hacker-hall-of-fame/) — extends Claude Code beyond a coding tool into a general-purpose agent framework. MCP integration, channels, scheduling, and the /insights command add more capability than most users will ever use.

**Plan mode.** Opus 4.6 proactively drops into plan mode for complex tasks, writes plan files that survive context resets, and follows them across sessions. This is the best answer to the context window problem that any tool currently offers.

### Weaknesses

**Context visibility.** You don't know how much context you've consumed until the model starts degrading. No progress bar, no warnings. Kiro CLI shows context usage from the start — Claude Code doesn't, and it matters.

**Token cost.** Upgrading from the $20/week plan to Max to access Opus 4.6 is a meaningful cost increase. Dan mentioned being "low on the Claude subscription totem pole" and rationing Opus usage in [Episode 13](/episodes/13-pi-coding-agent-dark-factories-the-furniture-makers-of-carolina/).

**Scaffolding overhead.** This is the philosophical critique: Claude Code has accumulated a lot of tooling infrastructure (MCP, skills, swarm mode, channels, plugins). When the model is intelligent enough, that scaffolding may hinder more than it helps. More on this in the Pi Agent section.

## [OpenAI Codex](https://openai.com/index/codex/) (GPT-5.x)

### Strengths

**SWE-bench scores.** GPT 5.3 Codex scored slightly higher than Claude on SWE-bench — "for the first time," as noted in [Episode 13](/episodes/13-pi-coding-agent-dark-factories-the-furniture-makers-of-carolina/). Whether SWE-bench scores predict real-world performance is a [separate question](/glossary/benchmaxxed/).

**Transparency about prompts.** OpenAI open-sourced their Codex model prompts as markdown in the Codex repo. The prompt is only 80 lines long. Notable instructions include: prefer rg over grep for speed, and avoid "AI slop" in frontend design. Covered in [Episode 11](/episodes/11-ai-fluency-pyramid-unrolling-the-codex-agent-loop-and-claude-code-s-secret-swarm-mode/).

**Convergence with Claude Code's UX.** The biggest compliment we can give Codex 5.3 is that it feels much more like Claude Code now. The gap has narrowed substantially.

### Weaknesses

**More hand-holding.** Codex asks for more feedback during execution. Claude Code will go beginning to end and verify; Codex pauses for confirmation. Whether this is a feature (safety) or a bug (friction) depends on your trust level.

**Less muscle memory.** Switching from Claude Code to Codex is higher-friction than expected, even when the capabilities are similar. The permissions model and interaction patterns are different enough that the transition cost is real.

### Harness Engineering

OpenAI's "harness engineering" blog post (covered in [Episode 17](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams/)) describes their philosophy of building structured harnesses around agent tool invocation — progressive tool access, structured documentation, and sandboxed environments. It's a sound approach, and the blog post is worth reading regardless of which tool you use.

## [Cursor](https://cursor.com/)

Cursor is the most prominent IDE-based agent and the one most people encounter first.

### Strengths

**Low barrier to entry.** If you already use VS Code, Cursor is the smallest conceptual leap. The agent is embedded in your editor, and the interaction model is familiar.

**Ambitious projects.** In [Episode 11](/episodes/11-ai-fluency-pyramid-unrolling-the-codex-agent-loop-and-claude-code-s-secret-swarm-mode/), Rahul mentioned Cursor's attempt to create an entire browser from scratch in a week — "and it took like a week or whatever." The project used significant open-source libraries (Servo's rendering code), but it demonstrates Cursor's capability for large-scope work.

### Weaknesses

**Funding concerns.** In [Episode 1](/episodes/1-ai-benchmarks-tech-radar-and-limits-of-current-llm-architectures/), the question was raised: "But will Cursor having no funding to do that?" — questioning Cursor's ability to compete with well-funded model providers like Anthropic and OpenAI who can bundle their own agents.

**IDE lock-in.** Terminal agents are editor-agnostic. Cursor ties you to their fork of VS Code. If you work across multiple editors or prefer Vim/Emacs/terminal workflows, Cursor doesn't fit.

The hosts don't use Cursor extensively. This section reflects that limited experience honestly rather than pretending to comprehensive coverage.

## [Pi Agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/) (Mario Zechner)

Pi Agent is the dark horse in this comparison, and the one that's most changed how I think about AI tooling.

### Architecture

Pi is radically minimal. Four layers: a unified model provider API, a terminal UI, a lightweight agent with a tiny system prompt, and a skills layer. The agent knows four things: read, write, bash, and skills. No MCP by default. No plan mode. Skills are built from markdown and bash scripts following Unix philosophy.

Compare this to Claude Code's feature list (MCP, skills, swarm mode, channels, scheduling, /insights, plugins, worktrees, coordinator mode, Kairos, dream mode) and the philosophical difference is stark.

### The foundation under OpenClaw

What most people don't realize is that Pi is the foundational layer that OpenClaw — the most widely adopted agentic coding framework, especially popular in China — is built on. OpenClaw wraps Pi's core with additional infrastructure: gateways, reverse proxies, management tooling, and a larger ecosystem of integrations. Pi is the heart and soul of OpenClaw, stripped down to its essentials.

I struggled with OpenClaw directly (covered in [Episode 13](/episodes/13-pi-coding-agent-dark-factories-the-furniture-makers-of-carolina/)): you have to set up gateways and reverse proxies and then all this other management stuff, and it comes with lots of code you're never going to use. Pi takes the opposite approach — start minimal, add what you need through skills. If you want the OpenClaw ecosystem without the overhead, Pi is the answer. And despite the ecosystem size, OpenClaw isn't really enterprise-ready either — its security model wasn't designed for that context, and bolting enterprise security onto a framework that wasn't built for it is its own category of risk.

NVIDIA built NemoClaw from scratch (covered in [Episode 18](/episodes/18-8-levels-of-ai-engineering-meta-ai-delays-and-llm-neuroanatomy/)) — not a fork of OpenClaw, but a signal that the agentic coding paradigm OpenClaw popularized is being adopted as a first-class interaction model by infrastructure companies. NemoClaw is designed to work with NVIDIA's Nemo local models and their AI stack, ushering in a mode where the GPU vendor also owns the agent layer.

### Why it works

I prefer Pi Agent over Claude Code for non-coding tasks. I've built a memory skill, a Telegram skill, a research agent using curl, a cron agent, and a Gmail agent. The line from workflow automation to agent is easier than the other way around. Claude Code is more specific — it's a coding tool that can do other things. Pi is a general-purpose agent that happens to be good at coding.

The philosophical point (from [Episode 13](/episodes/13-pi-coding-agent-dark-factories-the-furniture-makers-of-carolina/)): this may be the bitter lesson of AI tooling. When your agent becomes sufficiently intelligent, the additional scaffolding actually hinders it. Pi succeeds not despite its simplicity but because of it — less infrastructure means more of the context window is available for actual work.

### Limitations

Pi lacks the polish, community, and integration ecosystem of Claude Code. No built-in MCP support (you need a library). No plan mode (the model handles complexity through skills). No multi-agent coordination. For enterprise teams with established workflows, the setup cost is higher than Claude Code's.

## [GitHub Copilot](https://github.com/features/copilot)

### What it is now

Copilot occupies Level 1 (autocomplete) and Level 2 (chat-connected code) in the [8 Levels of Agentic Engineering](/episodes/18-8-levels-of-ai-engineering-meta-ai-delays-and-llm-neuroanatomy/) framework. Dan's assessment in Episode 18: "Copilot came out and it was like, oh my gosh, this is saving me so much time because I can have it write a whole function in one go." That was revolutionary in 2023. It's table stakes in 2026.

### The terms of service problem

In [Episode 20](/episodes/20-claude-code-source-leak-emotion-concepts-in-llms-and-surprising-facts-ais-know-about-us/), news broke that Copilot's terms classify it as "for entertainment purposes only." The response: "Copilot is about as useful for actual work as certain news channels are as good as for actual news." The legal positioning reflects the broader industry's unwillingness to accept liability for AI-generated code — but Copilot's explicit disclaimer is unusually candid.

### The NPU opportunity

Dan speculated that Microsoft could use on-device NPUs to run a portion of Copilot responses locally, dramatically reducing cloud costs at Microsoft's scale. If this happens, it would give Copilot a cost advantage that cloud-only agents can't match.

## [Gas Town](https://steveyegge.substack.com/p/the-gas-town-manual) (Steve Yegge)

Gas Town is less a tool and more a philosophy of multi-agent orchestration, wrapped in Mad Max theming.

### What it is

A Kubernetes-like workflow orchestrator for Claude Code agents. It requires Beads (a lightweight SQLite-based ticket tracking system), and it uses an elaborate vocabulary: Rigs (git repos), PoleCats (one-off agents), Mayor (main agent), Convoys (ticket series), Refineries (merge queue managers), Deacon (daemon that nudges stuck agents), Dogs (watchers that wake the Deacon). Covered in [Episode 10](/episodes/10-there-s-a-new-sherif-in-the-gas-town-of-ai-software-development/).

The pitch: parallelize development by running multiple Claude Code agents simultaneously, each working on a scoped ticket, merging results automatically.

### The reality

"Working in Gas Town can be chaotic and sloppy... you may not be a hundred percent efficient, but you are flying." That's the sales pitch from the blog post. The counter from Rahul: "you might get something with a ton of technical debt out of the box."

My experience (reported in [Episode 11](/episodes/11-ai-fluency-pyramid-unrolling-the-codex-agent-loop-and-claude-code-s-secret-swarm-mode/)): I tried doing less oversight and it didn't work nearly as well. Humans are still needed. Gas Town is a genuinely novel approach to multi-agent coding, but the management overhead is significant — and the [cognitive debt](/glossary/cognitive-debt/) risk is multiplied by the number of agents you're running.

The most interesting data point: Gas Town itself was "completely vibe coded using Beads. The author has not looked at the source code at any point."

## [Gemini CLI](https://github.com/google-gemini/gemini-cli) / [Google Stitch](https://stitch.withgoogle.com/) / [Antigravity](https://antigravity.withgoogle.com/)

### Where Gemini wins

Image generation and visual design. Dan was "literally stunned by the output" when using Gemini for web mockups from a mood board in [Episode 6](/episodes/6-gpt-5-2-claude-skills-and-hacker-hall-of-fame/). Google Stitch (covered in [Episode 17](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams/)) produces better visual output than Claude's attempts at UI design. Antigravity takes a different approach — a full-stack app builder that generates and deploys complete applications from prompts, leaning into Google's strength in infrastructure and deployment.

### Where it doesn't

Coding. "I'm sorry, Gemini. You're not doing great here" was the assessment in [Episode 13](/episodes/13-pi-coding-agent-dark-factories-the-furniture-makers-of-carolina/) when comparing it to Opus 4.6 and Codex 5.3.

The practical recommendation: use Gemini's ecosystem for image generation, visual design, and rapid app prototyping. Use Claude Code for writing code. Different models for different modes.

## [Open Code](https://github.com/opencode-ai/opencode)

Open Code is a headless/CI-focused alternative that Martin Alderson (from Catch Metrics) uses for automated PR review. "Using Open Code to run on your CI-CD pipelines to find issues — that's been awesome" (from [Episode 16](/episodes/16-pentagon-anthropic-drama-verified-spec-driven-development-and-interview-with-martin-alderson/)). He uses Claude Code for interactive work and Open Code for automated tasks. This split — interactive agent for development, headless agent for CI/CD — is a pattern worth watching.

## The Comparison That Actually Matters

Here's the comparison table the marketing posts won't give you:

| Factor | Claude Code | Codex 5.3 | Cursor | Pi Agent |
|--------|------------|-----------|--------|----------|
| **Best for** | Multi-file coding tasks with bash | Similar to Claude Code | Single-file editing, IDE users | General automation, non-coding |
| **Interaction model** | Terminal, autonomous | Terminal, asks for checkpoints | IDE inline | Terminal, minimal |
| **Context visibility** | None | Limited | Limited | N/A (minimal overhead) |
| **Initiative level** | High (does whole task, self-verifies) | Medium (pauses for confirmation) | Medium (suggests, waits) | High (skill-driven) |
| **Multi-agent support** | Swarm mode, worktrees | Cloud sandboxes | Limited | Manual (multiple instances) |
| **Ecosystem** | MCP, skills, plugins, channels | Harness engineering | VS Code extensions | Bash scripts, markdown skills |
| **Model lock-in** | Claude only | GPT only | Multi-model | Multi-model |
| **Philosophy** | Feature-rich tooling | Structured harnesses | IDE integration | Minimal scaffolding |

## Token Efficiency: The Hidden Variable

Martin Alderson's research (covered in [Episode 16](/episodes/16-pentagon-anthropic-drama-verified-spec-driven-development-and-interview-with-martin-alderson/)) tested 19 web frameworks for token efficiency when used by AI agents. The finding: minimal frameworks (Flask, Express) are significantly more token-efficient than larger frameworks (Rails, Next.js). The efficiency gap persists even on subsequent features.

This matters for tool selection because it reframes the question. It's not just "which agent is best?" but "which agent is most efficient with the framework I'm using?" If you're working in a token-heavy framework, you'll burn through context faster in any agent — but the agent's overhead (MCP tools, system prompts, skill definitions) compounds the problem.

## The Moat Question

The most important insight from 20 episodes of agent comparison: **the moat is in the model, not the tooling**.

Claude Code's feature velocity is impressive. But competitors are converging on similar features. Codex feels like Claude Code now. Cursor is adding agentic capabilities. Everyone is building MCP support. The tooling layer is commoditizing.

What isn't commoditizing — at least not yet — is model quality. Claude's reasoning capability is what makes Claude Code effective, not Claude Code's skill system or MCP integration. Pi Agent's success with radically minimal tooling proves this: when the model is good enough, you don't need elaborate scaffolding.

The practical implication for tool selection: don't get too attached to any single tool's features. The features will converge. Pick the tool with the best underlying model for your use case, and build workflows that can survive a tool switch.

## Frequently Asked Questions

### Which AI coding agent should I use?

If you work primarily in a terminal and want an autonomous agent that handles multi-file tasks: Claude Code. If you're embedded in VS Code and want inline assistance: Cursor. If you want maximum flexibility and don't mind setup: Pi Agent. If you need headless CI/CD integration: Open Code.

### Is Claude Code worth the Max subscription?

If you're using it for professional work, yes. The gap between Opus 4.6 and smaller models for complex coding tasks is significant. If you're using it for personal projects or learning, the standard plan with smaller models may be sufficient.

### Should I use multiple agents?

Martin Alderson uses Claude Code for interactive work and Open Code for CI/CD. That split makes sense. Using multiple interactive agents simultaneously (à la Gas Town) is viable but creates management overhead and cognitive debt risk. Start with one agent, master the workflow, then consider parallelization.

### How do I compare tools fairly?

Run the same task in each tool. Not a benchmark task — a real task from your actual work. The SWE-bench comparison is meaningless for this purpose, because [most SWE-bench-passing PRs wouldn't survive human code review](/episodes/18-8-levels-of-ai-engineering-meta-ai-delays-and-llm-neuroanatomy/). Test on your code, with your conventions, on your timeline.

### Will these tools converge into one?

The tooling layer will converge. The model layer won't — at least not soon. Expect every agent to eventually have MCP support, multi-file editing, plan mode, and context management. The differentiation will be in the model's reasoning quality, the pricing model, and the ecosystem around enterprise features.

### What about Devin and other cloud agents?

We haven't covered Devin extensively because the hosts prefer interactive, terminal-based workflows. Cloud agents that run asynchronously solve a different problem — they're for delegation, not collaboration. If your workflow involves assigning tickets and reviewing PRs, cloud agents make sense. If you want to work alongside the agent, terminal or IDE tools are a better fit.

---

*This comparison reflects our hands-on experience through April 2026. The AI coding agent market moves fast — check the most recent episodes for updates on tools released after this guide was written.*
