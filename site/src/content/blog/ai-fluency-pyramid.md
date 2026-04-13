---
title: "The AI Fluency Pyramid: 5 Levels of Developer AI Skill"
description: "Most developers are stuck at level 2 of AI fluency. Here is the full pyramid, what each level looks like, and how to move up."
date: "2026-04-11"
lastUpdated: "2026-04-12"
slug: "ai-fluency-pyramid"
keywords: "AI fluency framework, AI fluency pyramid, AI developer levels, AI-native development"
episodes: ["11"]
---

Brex cut 20% of its staff in 2024, reoriented the entire company around AI, and got acquired by Capital One for over $5 billion. Before that happened, they did something that most companies skip entirely: they defined what AI competence actually looks like at each level of their engineering career matrix. They called it the [AI fluency pyramid](/glossary/ai-fluency-pyramid/), and when Brex CTO James Reggio described it on the [Latent Space podcast](https://www.latent.space/p/brex), it was the single detail from the interview that stuck with me, and with both of my co-hosts on [episode 11 of ADI Pod](/episodes/11-ai-fluency-pyramid-unrolling-the-codex-agent-loop-and-claude-code-s-secret-swarm-mode/).

The reason it stuck is that most conversations about AI adoption are binary. Either you are "using AI" or you are not. Either you have drunk the Kool-Aid or you are drinking hop water. The AI fluency pyramid is a framework for measuring a developer's progression from casual AI user to AI-native practitioner, originally developed at Brex and expanded here to five levels. Each level describes a qualitatively different relationship with AI tooling, and the jump between levels is not about effort. It is about changing the kind of work you do.

| Level | Name | What It Looks Like | Key Transition |
|:---:|---|---|---|
| 1 | User | AI as faster Stack Overflow | Install an AI tool |
| 2 | Advocate | Designing workflows around AI | Configure persistent context (CLAUDE.md) |
| 3 | Builder | Building tooling on top of agents | Create tools others use |
| 4 | Orchestrator | Running multi-agent systems | Coordinate agents, not individual prompts |
| 5 | AI-Native | Setting AI vision and strategy | Strategic judgment on what AI should and shouldn't do |

Here is the framework, applied specifically to software developers. For each level: what it looks like, how to get there, and what is still missing.

## Level 1: User

**What it looks like.** You have a ChatGPT or Claude subscription and you use it to answer questions. You paste in error messages. You ask it to explain a regex. Maybe you use Copilot for autocomplete in your editor. AI is a faster Stack Overflow, a lookup tool that saves you a few minutes on tasks you could have done yourself.

Getting here is trivial: install any AI tool and start using it. This is the default state for most developers who have interacted with an LLM at all. Brex defined this level as someone who "uses available AI tools to assist with simple processes and their defined responsibilities." If you understand basic prompting and have a rough sense of what the model is good and bad at, you are here. But the ceiling is low. AI at this level is an add-on to your existing workflow, not a part of it. You switch between your IDE and a chat window. There is no feedback loop, no persistent context, no compounding effect. Every interaction starts from zero.

According to [GitHub's 2025 developer survey](https://github.blog/news-insights/research/survey-ai-wave-grows/), 97% of developers reported using AI coding tools at work, but most of that usage is exactly this level. Chat-based Q&A. One-shot code generation. The tool is adjacent to the work, not embedded in it.

## Level 2: Advocate

**What it looks like.** You have moved beyond one-off queries. You are designing small workflows around AI: using it for code review, generating test scaffolds, maintaining a CLAUDE.md file that gives the agent persistent context about your project. You have opinions about which models are better for which tasks. When a teammate says "I just wrote that by hand," you wince a little.

**How to get here.** The transition from User to Advocate is about intentionality. You stop treating AI as a search engine and start treating it as a collaborator with memory and preferences. Concretely, this means adopting a tool like Claude Code or Cursor that operates inside your development environment rather than in a separate browser tab, and investing time in configuring it. That means writing [CLAUDE.md files](/blog/claude-md-best-practices/), creating custom instructions, building prompt templates for recurring tasks. Brex described this level as "actively integrating AI into independent or team workflows" and being able to "design or manage small to medium human-in-the-loop AI workflows."

**What is missing.** You are still the bottleneck. The agent does what you tell it, one task at a time. You review everything manually. Your workflow is faster than it was without AI, but it is fundamentally the same shape. You are just moving through it with a better assistant. The leverage is linear: one developer plus one agent equals roughly 1.5 developers, maybe 2 on a good day.

## Level 3: Builder

**What it looks like.** You are building tooling on top of AI agents, not just using them. Maybe you have written a custom orchestrator. Maybe you have built internal tools that wrap LLM APIs for your team's specific workflows (code migration scripts, automated changelog generators, domain-specific review bots). You think in terms of agent pipelines, not individual prompts. You might be practicing [spec-driven development](/blog/spec-driven-development-ai/) without anyone having told you to.

**How to get here.** This is where the Brex pyramid gets interesting, and where my co-host Dan Lasky pushed back. His hot take during [episode 11](/episodes/11-ai-fluency-pyramid-unrolling-the-codex-agent-loop-and-claude-code-s-secret-swarm-mode/) was blunt: "No one's hit level three yet." I think that is too strong, but he is pointing at something real. The jump from Advocate to Builder requires you to stop using AI tools as given and start composing them into novel systems. Brex defined it as being able to "proactively build, design, refine, or manage AI-driven solutions or tools that create significant business value."

The key word is "significant." Plenty of developers have written wrapper scripts around GPT APIs. The Builder level means those wrappers solve real problems for people other than you. It means understanding the agent loop deeply enough to intervene in it. Consider how [OpenAI's Codex structures its agent execution](https://openai.com/index/unrolling-the-codex-agent-loop/) so that each tool call appends the full call chain to the next API request, and knowing where to insert custom tooling into that chain.

**What is missing.** Scale. You are building for your team, maybe your department. The tools work because you are there to maintain them and intervene when they break. You understand the agent loop, but you are still a single point of coordination.

## Level 4: Orchestrator

Here is the gap that separates Orchestrator from everything below it: vision. You can run the machine at this level, but you are not yet setting the direction for where the machine should point. That said, what the machine looks like at this level is qualitatively different from anything before it.

The original Brex pyramid did not name this level separately (they folded it into "Native"), but I think it deserves its own tier. You are running multi-agent systems. You have a lead agent that creates plans, delegates to worker agents, and synthesizes their output. You are thinking about agent coordination patterns, not individual agent performance.

This is where the Claude Code swarm mode that Dan surfaced on episode 11 becomes relevant. Someone had reverse-engineered hidden feature flags from the Claude Code binary, and the internal architecture matched what the open-source community was already building: a lead agent that does not write code itself but creates plans, delegates to sub-agents, maintains a task board, and coordinates execution. The lead agent in the swarm architecture is essentially a project manager: it breaks down the work, assigns it, tracks progress, and resolves conflicts between agents.

I have been running a similar setup using Gas Town, an open-source multi-agent orchestrator. The experience is instructive. When I invested heavy effort in prompt engineering and oversight, the results were genuinely impressive: parallel agent execution across multiple files, coherent architecture emerging from distributed work. When I backed off and let the agents run with less supervision, quality dropped noticeably. Humans are still needed as of right now, as I noted during the episode. The orchestration layer demands a kind of architectural thinking that is different from writing code or even writing specs. You are designing the workflow that produces the code, not the code itself.

## Level 5: AI-Native

**What it looks like.** You set the AI vision and strategy for a team, department, or organization. You pioneer novel applications of AI that others adopt. You understand not just how to use AI tools or build with them or orchestrate them, but where the entire practice is heading, and you position your organization to be there when it arrives.

**How to get here.** Honestly, I am not sure I know. Brex defined this as their highest level ("can set the AI vision and strategy for a team or department, can pioneer novel applications of AI"), and when I said during the episode that I am definitely not level four (now level five in my expanded version), I meant it. There are people on Twitter claiming this level. I have not personally encountered anyone who I would confidently place here, though I suspect a handful exist at companies like Anthropic, OpenAI, and Google DeepMind where the tool and the product are the same thing.

What I think distinguishes this level from Orchestrator is not technical skill but strategic judgment. It is the difference between knowing how to run a multi-agent pipeline and knowing which problems should be solved with a multi-agent pipeline versus which should not. Dario Amodei's essay "The Adolescence of Technology" (which we also covered on episode 11) frames AI as powerful but not yet mature, and the AI-Native developer operates with that maturity. They know what AI cannot do as well as what it can, and they build organizational strategy around both.

**What is missing.** This is the honest part: nobody fully knows yet. The field is moving too fast for anyone to have a stable, proven playbook at this level. Anyone who claims otherwise is selling something.

## Where Are You, and Does It Matter?

I think most working developers are at Level 1, with a significant minority at Level 2. Level 3 is rare. Levels 4 and 5 are vanishingly so. And this distribution is fine, for now.

Here is the counterargument to the entire pyramid: maybe fluency levels are a corporate HR artifact that does not map to individual career outcomes. Brex built their pyramid into a career matrix, which means it was tied to promotions and compensation. When you attach levels to incentives, you get people optimizing for the appearance of the level rather than the substance. Someone who forces a multi-agent pipeline into a problem that needed a simple script is not Level 4; they are Level 2 with bad judgment.

I think that is a fair concern, and it is the reason I would not use the pyramid as a performance review tool. But as a self-assessment framework (a way to name where you are, identify the next step, and recognize what kind of learning that step requires), it is more useful than anything else I have seen. The transitions between levels are real. Moving from User to Advocate means changing your tools and habits. The jump to Builder is harder because it demands a different kind of work entirely. And once you reach Orchestrator territory, the challenge shifts again: you have to think about systems of agents rather than individual agents. Each transition is a qualitative shift, not just more of the same.

The practical question is not "how do I get to Level 5" but "what is the next level for me, and what is one concrete thing I can do to start the transition?" If you are at Level 1, that thing is writing a [CLAUDE.md file](/blog/claude-md-best-practices/) and committing to using an embedded AI tool for a full week. If you are at Level 2, it is building one internal tool that wraps an LLM API for a specific workflow. If you are at Level 3, it is running two agents in parallel on a real task and figuring out how to coordinate their output.

The pyramid is not a destination. It is a map of [how developer careers are being reshaped](/topics/ai-developer-careers/) by tools that did not exist two years ago. You do not need to reach the top. You need to know where you are and what the next step looks like, and you need to be honest about whether you are actually climbing or just standing on the same step with a fancier title.
