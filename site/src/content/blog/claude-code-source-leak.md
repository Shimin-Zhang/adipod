---
title: "What Claude Code's Source Leak Actually Revealed"
description: "When Claude Code's source code went public, it confirmed some suspicions and overturned others. Here is what the architecture looks like and what it means."
date: "2026-04-11"
lastUpdated: "2026-04-12"
slug: "claude-code-source-leak"
keywords: "Claude Code source code, Claude Code architecture, Claude Code leak, Anthropic agentic tools"
episodes: ["20"]
---

On March 31, 2026, security researcher Chaofeng Shou noticed something that Anthropic almost certainly wished he had not: the entire Claude Code CLI source code was sitting in the open, exposed by a source map file that should never have shipped.

The culprit was not a rogue employee or a compromised build server. It was a [bundling bug in Bun](https://arstechnica.com/ai/2026/03/entire-claude-code-cli-source-code-leaks-thanks-to-exposed-map-file/), the JavaScript runtime whose creator Anthropic had recently hired. Someone had reported the bug (Bun was ignoring its bundling settings) days before it led to the most consequential accidental source disclosure in the agentic coding tool space. As my co-host Dan Lasky put it on [episode 20](/episodes/20-claude-code-source-leak-emotion-concepts-in-llms-and-surprising-facts-ais-know-about-us/): "Who's to say the Bun mistake wasn't vibe coded?"

What followed was predictable. Anthropic issued mass DMCA takedowns, nuked forks on GitHub, and, in a textbook Streisand effect, ensured that every curious developer on the planet went looking for mirrors. Within hours, the code had been cloned to local machines, rehosted on alternative Git providers, and rewritten by teams who understood that clean-room reimplementations are not subject to the same copyright protections. The forks you can find are not the problem, as Rahul Yadav observed on the show. The forks you cannot find are.

But the interesting part of this story is not the leak itself. It is what the code revealed about how Anthropic actually thinks about building agentic software, and which of our assumptions it confirmed versus which it quietly overturned.

| Finding | Significance | Design Principle |
|---|---|---|
| **Dual-track permission system** | Rules + ML classifier for bash command safety | Expensive inference for high-stakes decisions |
| **Kairos / Dream mode** | Memory consolidation between sessions | Persistence as first-class architecture |
| **Frustration regexes** | Regex over LLM for user frustration detection | Cheapest tool for low-stakes signals |
| **Anti-distillation injection** | Generates fake tools to poison distillation | Behavioral layer as competitive moat |
| **Undercover mode** | Presents agent as human rather than AI | Ambiguous use case, uncomfortable implications |
| **Swarm + Coordinator modes** | Multi-agent orchestration built-in | First-party multi-agent as product direction |

## The Permission System: Two Tracks, Not One

The most architecturally significant finding came from [Victor Antos's deep dive](https://victorantos.com/posts/i-read-the-leaked-claude-code-source-heres-what-i-found/) into the permission system. Claude Code does not rely on a single mechanism to decide whether a command is safe to execute. It runs a dual-track system: track one is rule-based permissions (static rules that flag categories of operations). Track two is a machine learning classifier specifically trained to evaluate whether bash commands might be destructive.

This is a design decision that tells you something about Anthropic's threat model. A rule-based system alone would be brittle, because the space of potentially dangerous shell commands is effectively infinite. A classifier alone would be opaque and inconsistent. Neither is enough. Running both in parallel, with what appears to be a conservative union of their judgments, means Claude Code can catch both the predictable hazards (rules) and the novel ones (classifier). It also means the security surface is meaningfully larger than competitors that rely on allow-list approaches.

For practitioners thinking about [agentic architecture](/topics/claude-code-guide/), the dual-track pattern is worth studying. The cost is real; you are running inference on every bash command before execution. But the alternative is a permission system that either blocks too much or permits something catastrophic. Anthropic has apparently decided that the inference cost is worth it. Given that the tool has access to your filesystem, your git history, and your shell, I think that is the right tradeoff.

## Kairos, Dream Mode, and the Memory Problem

The leak also exposed [several hidden features](https://ccunpacked.dev/) that had not been publicly documented, the most interesting of which is Kairos, a persistent mode with memory consolidation between sessions. The concept borrows from what sleep researchers call memory consolidation: the process by which short-term memories are reorganized and compressed into long-term storage. In Claude Code's implementation, this appears to involve periodically compacting the agent's memory file during idle periods, a process the codebase calls "dream."

This is a direct response to what I consider the central unsolved problem in agentic coding: models do not learn as they work through a codebase. Every new session starts from a cold read of your [CLAUDE.md](/blog/claude-md-best-practices/) and whatever context you provide. The agent that spent three hours yesterday understanding your authentication flow has no memory of it today. Kairos is Anthropic's attempt to build persistence into an architecture that is fundamentally stateless.

The implementation is still hidden behind a feature flag, but the concept matters more than the current state. If you have worked with long-running agents, you know the problem: [the middle loop](/glossary/the-middle-loop/), the cycle of task decomposition, execution, and state management between individual LLM calls, breaks down when the agent cannot carry forward what it learned in previous sessions. Every workaround I have seen, from bloated context files to elaborate memory schemas, is a hack around the same underlying issue. Kairos appears to be Anthropic's first attempt at a principled solution.

The source also revealed a swarm mode and a coordinator mode, which together suggest that Anthropic is building toward multi-agent orchestration within Claude Code itself. Swarm mode appears to handle parallel agent execution, while coordinator mode manages sub-agent delegation and task routing. There is even a bridge component for controlling Claude Code remotely from a phone or browser. None of this is revolutionary in isolation; OpenClaw and similar harnesses have had these capabilities. But the fact that Anthropic is building them into the first-party tool signals where they believe the product is heading.

## Frustration Regexes and the Cheapness Principle

Then there are the frustration regexes. The media coverage of them tells you more about tech journalism than about Claude Code's architecture.

The finding: Claude Code includes regular expressions that detect when users are expressing frustration. The breathless coverage: "Claude Code is logging how many times you swear." The reality, as Dan pointed out on the show: this is functionally identical to rage-click detection in any UI analytics tool. You track user frustration not because you are surveilling them but because frustration signals that the tool has failed, and you want to know when and how.

The more interesting architectural observation is that Anthropic chose regex for this rather than running sentiment analysis through the model itself. They have, quite literally, one of the most capable language models in the world sitting right there. They used regex instead. It is orders of magnitude cheaper per invocation, and this detection runs on every user input. At Anthropic's scale, the compute savings of pattern matching over inference are not trivial. It is a small decision that reveals a larger engineering principle: use the lightest tool that gets the job done, even when you have the heaviest tool in the building.

Contrast this with the dual-track permission system, where Anthropic does use ML inference on every bash command. The difference is stakes. Getting frustration detection wrong means your analytics are slightly noisy. Getting permission detection wrong means deleting someone's production database. The cost of the classifier is justified by the cost of the failure mode. That calculus (cheap signals for low-stakes detection, expensive inference for high-stakes decisions) is a design pattern that anyone building [agentic tools with security implications](/topics/ai-security-developers/) should internalize.

## Anti-Distillation and the Competitive Moat Question

One finding that did not get enough attention: Claude Code includes an anti-distillation injection. If it detects that someone is attempting to distill its behavior, essentially training a cheaper model to mimic Claude Code's outputs, it generates fake tools. Not errors, not refusals. Fake tools. Deliberately wrong information designed to poison the distillation dataset.

This is a defensive strategy that only makes sense if Anthropic believes Claude Code's behavior, not just its model weights, constitutes a competitive advantage. The system prompt is already public knowledge; any Claude Code user can read it. The model weights are proprietary but not unique; other frontier models exist. What remains is the interaction patterns: how the tool decides what to do, when to ask for permission, how to decompose tasks, how to manage context. That behavioral layer is what the anti-distillation system protects.

The existence of this defense also means Anthropic takes the competitive threat of distillation seriously enough to build active countermeasures rather than relying on legal protections alone. Given how quickly the DMCA takedowns failed to contain the source leak, that seems pragmatic.

## Undercover Mode and the Uncomfortable Implications

Here is a question I keep coming back to: if a tool is built for professional software development, should it include a first-party mechanism for hiding the fact that it is an AI? That is not a hypothetical.

The source code revealed an "undercover mode": a flag that makes Claude Code present itself as if it were a human rather than an AI. The stated use case is unclear from the code alone. On the show, we joked about it in the context of Medvi, the telehealth company allegedly using agents to impersonate doctors. There are plausible benign applications, like testing whether humans interact differently with AI-identified versus unidentified assistants. I am not claiming nefarious intent. But the fact that the feature exists, hidden behind a flag, says something on its own. I do not have a tidy principle to extract from this one.

## Should They Just Open Source It?

Both Google and OpenAI have open-sourced their agent harnesses. The Claude Code source is already in the wild, cloned to thousands of local machines, mirrored on alternative hosting platforms, and rewritten by multiple independent teams. The DMCA approach has failed by any practical measure. Ship has sailed.

I think Anthropic should just open source it. The competitive advantages of Claude Code are primarily in the model, the system prompt design, and the behavioral patterns, most of which are already observable to any paying user. The infrastructure code for permission systems, session management, and tool orchestration is valuable but not irreplaceable. Open-sourcing it would convert a security liability into a community asset, allow external security researchers to audit the permission system properly, and eliminate the ongoing cost of playing copyright whack-a-mole with mirrors and rewrites.

The counterargument is that the source contains proprietary behavioral logic (the anti-distillation injections, the classifier integration points, the unreleased feature flags) that Anthropic legitimately wants to protect. That is fair. But the code is already out there. The question is not whether people will read it. It is whether Anthropic gets the goodwill and security benefits of controlled disclosure or continues absorbing the reputational cost of aggressive takedowns that do not work.

## What It Actually Means for the Field

The Claude Code source leak is, ultimately, a snapshot of how one company is solving the hard problems in agentic coding tools. The dual-track permission system, the memory consolidation approach, the pragmatic cheapness of frustration detection, the defensive distillation countermeasures. These are engineering decisions that reveal priorities.

Anthropic prioritizes safety over speed in permission handling. They prioritize cost efficiency over elegance in telemetry. They are investing in persistence and multi-agent coordination as first-class architectural concerns rather than community add-ons. And they are building competitive defenses into the product layer, not just the model layer.

For practitioners building on or competing with these tools, the leak is more useful as an architecture study than as a source of gossip. The specific feature flags will change. The design principles behind them (dual-track safety, [tiered inference costs](/blog/claude-context-loss-nickname-trick/), persistent memory as infrastructure) are likely to persist across the entire agentic coding space for the foreseeable future.

The irony, of course, is that we learned all of this because of a bug in a JavaScript bundler. The most revealing window into the future of AI-assisted development was opened by the most pedestrian category of software defect imaginable.
