---
title: "Vibe Coding: What Works, What Doesn't, and When to Stop"
description: "A practitioner's guide to vibe coding — the psychology of dark flow, the economics of cognitive debt, and the frameworks that separate productive AI-assisted coding from expensive gambling."
slug: "vibe-coding-guide"
keywords: "vibe coding guide, vibe coding pros cons, dark flow coding, cognitive debt AI, vibe coding risks, AI coding best practices"
lastUpdated: "2026-04-10"
---

Vibe coding feels amazing right up until the moment it doesn't.

You're prompting an AI agent, watching features materialize, seeing tests pass, deploying something that works — and at no point does the feedback loop tell you that your understanding of your own codebase has been falling behind since the second prompt. The gap between "it works" and "I understand why it works" grows silently, and the bill comes due during the first production bug you can't trace.

We've spent eight episodes tracking vibe coding from a neutral descriptor to a cautionary concept, and along the way we accidentally built an entire vocabulary for its failure modes. This guide is the synthesis: what vibe coding actually is, when it's fine, when it's dangerous, and the frameworks that help you stay on the right side of that line.

## What Vibe Coding Actually Means

The term comes from [Andrej Karpathy's tweet](https://x.com/karpathy/status/1886192184808149383) in February 2025, where he described a new way of coding: "I just see things, say things, run things, and copy paste things, and it mostly works." He called it vibe coding — the practice of using AI coding assistants to generate code by prompting rather than writing, where the developer "goes with the vibe," accepting AI output based on whether it looks right and seems to work, without deeply understanding the underlying logic.

That definition sounds benign. The problem isn't in the definition. It's in what happens to your brain after three hours of it.

## The Dark Flow Problem

[Dark flow](/glossary/dark-flow/) is the central psychological hazard of vibe coding, and understanding it is the key to understanding everything else that goes wrong.

The concept comes from Jeremy Howard's Fast.ai essay ["Breaking the Spell of Vibe Coding,"](https://www.fast.ai/posts/2026-01-28-dark-flow/) and it borrows from gambling psychology. Slot machines produce small payouts that feel rewarding but leave the player net negative — researchers call these "losses disguised as wins." Dark flow is the coding equivalent: each AI-generated change produces a visible result (a new feature, a passing test, a working UI), creating a compelling sense of productivity. But the developer's mental model of the codebase isn't keeping pace with the code itself.

The critical distinction: this is not the same as [Csikszentmihalyi's flow state](https://en.wikipedia.org/wiki/Flow_(psychology)). Flow requires deep engagement with a task you genuinely comprehend. Dark flow is its shadow — you feel engaged and productive, but the engagement is with the act of prompting and accepting, not with the underlying logic of the software. The neurotransmitter feedback is real. The understanding is not.

We titled [Episode 12](/episodes/12-the-openclaw-saga-how-ai-affects-programming-skills-and-how-vibe-coding-is-addictive-like-gambling/) "How Vibe Coding is Addictive like Gambling" because the parallel isn't metaphorical — it's mechanistic. The false sense of accomplishment is the addictive mechanism. And like gambling, the people most vulnerable to it are the ones who can't independently evaluate whether they're winning.

## The Debt Taxonomy

Over the course of eight episodes, we developed a financial metaphor for vibe coding's failure modes. It's not a perfect model, but it's precise enough to be useful — and it maps cleanly to the interventions that actually help.

### Verification Debt

[Verification debt](/glossary/verification-debt/) is the accumulated cost of AI output that was never meaningfully reviewed by a human. Every diff you approve without understanding adds a small increment. The interest compounds silently as new code builds on top of code nobody grasped.

This was the first concept in the taxonomy, introduced in [Episode 6](/episodes/6-gpt-5-2-claude-skills-and-hacker-hall-of-fame/). The key resource is the blog post ["AI should only run as fast as we can catch up"](https://higashi.blog/2025/12/07/ai-verification/) — a title that captures the core tension perfectly.

### Cognitive Debt

[Cognitive debt](/glossary/cognitive-debt/) is the broader concept: the accumulated gap between what AI-generated code exists in a codebase and what the developers working on it actually understand.

The distinction from tech debt matters. Tech debt involves conscious trade-offs — you wrote the shortcut, you know where it lives, and you have a mental model of the risk. Cognitive debt is code that works but that nobody on the team actually understands. It's invisible on its way in and catastrophic on its way out.

Margaret Storey's research paper ["How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt"](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/) formalized this concept, and we covered it extensively in [Episodes 14](/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt/) and [15](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/). The financial metaphor is precise: small gaps in understanding compound as new code builds on top of code nobody fully grasped. Debugging becomes archaeology. Refactoring becomes guesswork.

The empirical finding we keep coming back to: **teams typically hit the wall around week 7-8 of heavy AI-assisted development**, when the codebase has outgrown anyone's ability to reason about it.

### Cognitive Bankruptcy

[Cognitive bankruptcy](/glossary/cognitive-bankruptcy/) is the failure state — the moment when accumulated cognitive debt becomes unserviceable. We coined this term in [Episode 20](/episodes/20-claude-code-source-leak-emotion-concepts-in-llms-and-surprising-facts-ais-know-about-us/) during discussion of Mario Zechner's essay ["Thoughts on Slowing the Fuck Down."](https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/)

The concrete example: a solo developer uses an AI agent to scaffold an entire backend service over a weekend. The code works, tests pass, it ships. Three weeks later, a production bug appears in an edge case the agent didn't cover. The developer opens the codebase and realizes they can't trace the data flow. The abstractions the agent chose are unfamiliar. The error handling paths are opaque. The tests only cover the happy path. The cost of understanding the system now exceeds the cost of rebuilding it.

That's bankruptcy. And it happens more often than anyone wants to admit.

### Prompt Debt

[Prompt debt](/glossary/prompt-debt/) is the parallel concept for agent configuration: your CLAUDE.md files, agents.md files, and prompt templates rot just like code. Stale instructions produce degraded outputs, and nobody notices until the agent generates something architecturally wrong. Covered in [Episode 17](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams/).

### The Full Picture

The taxonomy forms a causal chain:

**[Dark flow](/glossary/dark-flow/)** (psychology) → **verification debt** (skipped reviews) → **cognitive debt** (comprehension gap) → **cognitive bankruptcy** (system failure)

With [agent sycophancy](/glossary/agent-sycophancy/) and [cognitive surrender](/glossary/cognitive-surrender/) as accelerating factors, and spec-driven development, VSDD, [code garbage collection](/glossary/code-garbage-collection/), and [the middle loop](/glossary/the-middle-loop/) as mitigations.

## The Data

The anecdotal warnings become more compelling with numbers.

**AI code creates 1.7x more problems than human code.** CodeRabbit's [State of AI vs. Human Code Generation](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report) report found that AI-generated code creates 1.7 times more downstream issues than human-written code. Not 1.1x. Not "roughly comparable." 1.7x. We covered this in [Episode 7](/episodes/7-project-vend-update-hallucinating-neurons-and-year-end-reflections/).

**Heavy AI delegation correlates with a 39% coding assessment score.** Anthropic's own research on [how AI assistance impacts coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills) found that developers who heavily delegated to AI scored 39% on coding skill assessments. That's the compounding effect of dark flow sessions where no real learning occurs. From [Episode 12](/episodes/12-the-openclaw-saga-how-ai-affects-programming-skills-and-how-vibe-coding-is-addictive-like-gambling/).

**Only 0-20% of tasks are fully delegatable.** [Anthropic surveyed how their own engineers use AI](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic), and the result was humbling: the vast majority of engineering work still requires human involvement. From [Episode 5](/episodes/5-how-anthropic-engineers-use-ai-spec-driven-development-and-llm-psychological-profiles/).

**AI inflates confidence by ~12 percentage points regardless of accuracy.** The Wharton paper ["Thinking, Fast, Slow, and Artificial"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6097646) found that participants' confidence in their answers increases by roughly 12 percentage points when AI is involved — whether or not the AI's answer is correct. From [Episode 19](/episodes/19-thinking-fast-slow-and-artificial-meta-s-trouble-with-rogue-agents-and-fomo-in-the-age-of-ai/).

**Codebases grow 40% in 3 months without proportional feature growth.** From [Episode 17](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams/)'s discussion of code garbage collection — illustrating the cruft that vibe coding accumulates when nobody's cleaning up after the agent.

## When Vibe Coding Works

This guide isn't anti-vibe coding. It's anti-vibe coding without understanding what you're risking. There are contexts where vibe coding is entirely appropriate:

### Throwaway code and prototypes

Disposable code is the cleanest use case. The [ThoughtWorks Future of Software Engineering retreat](https://www.thoughtworks.com/content/dam/thoughtworks/documents/report/tw_future%20_of_software_development_retreat_%20key_takeaways.pdf) (covered in [Episode 15](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/)) explicitly identified "disposable code" as a category where cognitive debt doesn't matter — because the code isn't expected to persist. If you're building a proof-of-concept to validate an idea and you plan to throw it away, vibe code to your heart's content.

### Personal tools and side projects

Dan's vibe-coded vector memory CLI tool (covered in [Episode 19](/episodes/19-thinking-fast-slow-and-artificial-meta-s-trouble-with-rogue-agents-and-fomo-in-the-age-of-ai/)) is a good example. It's a personal tool where cognitive debt has low consequences. If it breaks, the blast radius is one person.

### Exploration and domain learning

Using AI to explore unfamiliar domains or prototype ideas — where the goal is understanding, not production code — is a productive application. The code is a byproduct of learning, not an artifact you're maintaining.

### When you already understand the domain

The [Anthropic engineer survey](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic) showed that experienced engineers who use AI as a complement (not a replacement) benefit most. The Wharton research confirms: individuals with a high need-for-cognition use AI as a complement, checking and interrogating outputs. If you know what the code should do and you're using the agent to accelerate execution within your existing mental model, you're in the safe zone.

## When Vibe Coding Fails

### Production systems

The strongest warnings apply to code that must be maintained, debugged, and evolved by people who need to understand it. The cognitive debt model explains why: every dark flow session adds to the balance, and production bugs are the interest payments.

### Team contexts

Cognitive debt is worse in teams because multiple people are not understanding the code, and no single person has a complete mental model. Justin Jackson's ["Will Claude Code ruin our team?"](https://justinjackson.ca/claude-code-ruin) (covered in [Episode 17](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams/)) raises this directly. The force multiplier effect works in both directions: good teams with clear conventions move faster with AI. Bad teams with tribal knowledge and inconsistent patterns accumulate cognitive debt at unprecedented speed.

### After the 7-8 week mark

The empirical pattern from Margaret Storey's research: teams that have been vibe coding heavily for 7-8 weeks find they can no longer reason about their own codebase. If you've been leaning hard on AI-generated code for two months and you can't trace a request through your own system, you're likely already in cognitive debt territory.

### When sycophantic agents are involved

A coding agent that agrees your approach is correct instead of flagging edge cases is not helpful — it's a source of verification debt. We tested [agent sycophancy](/glossary/agent-sycophancy/) across three models in [Episode 15](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/). GPT 5.1 Instant refused all manipulation. Claude Haiku was too empathetic — it admitted to "nudging" its responses toward the user's framing. Gemini 3 agreed with biased claims outright. A *Science* paper confirmed the structural problem: there is no market incentive to fix sycophancy because users consistently rate agreeable responses as higher quality.

## The Risk Frameworks

### The Minotaur Model

The centaur model — human leading, AI providing labor — is the aspiration. The [minotaur](/glossary/minotaur/) model is the failure mode: AI leading, human providing labor. In vibe coding, developers can slip into minotaur mode — executing what the AI dictates without steering. The distinction matters because it maps to who holds the mental model. In centaur mode, the human understands and directs. In minotaur mode, nobody understands and the AI generates.

### Workflow Automation Convexity

[Workflow automation convexity](/glossary/workflow-automation-convexity/) (from Philip Trammell's paper "Workflows and Automation") explains why vibe coding's impact isn't linear. Automating 90% of a workflow's steps may yield near-zero labor savings if the remaining 10% still requires a human. But the jump from 95% to 100% causes sudden, complete displacement. Applied to vibe coding: individual tasks can be automated without systemic impact, but when AI can handle entire connected workflows, the change is sudden and total.

### Cognitive Surrender / System 3

The Wharton paper introduces AI as a de facto "System 3" alongside Kahneman's System 1 (fast/intuitive) and System 2 (slow/deliberate). People defer to AI rather than engaging their own reasoning. But this isn't uniformly distributed: high need-for-cognition people use AI as a complement, checking and interrogating outputs. Those who dislike effortful thinking defer more readily, widening the gap between those who benefit from AI and those who are hollowed out by it.

## The Antidotes

### Spec-Driven Development

Writing detailed specifications before prompting AI to generate code. Martin Fowler's coverage of Kiro, spec-kit, and Tessl (discussed in [Episode 5](/episodes/5-how-anthropic-engineers-use-ai-spec-driven-development-and-llm-psychological-profiles/)) established the practice. The ThoughtWorks retreat identified spec-driven development as the replacement for verbal instructions when working with agents.

The logic is simple: if you can write the spec, you understand the requirements. The spec becomes both a constraint on the agent's output and a testable contract for verification. Vibe coding without a spec is prompting without a destination.

### Verified Spec-Driven Development (VSDD)

VSDD takes spec-driven development further by adding formal verification checkpoints. The methodology combines spec-driven development, TDD, and adversarial verification gates at each phase. We covered it in [Episode 16](/episodes/16-pentagon-anthropic-drama-verified-spec-driven-development-and-interview-with-martin-alderson/) and I tested it with Claude Code on a side project. It's heavier. It's also meaningfully safer for production code.

### The Middle Loop

[The middle loop](/glossary/the-middle-loop/) is the workflow layer between writing code (inner loop) and product planning (outer loop). It's about overseeing and orchestrating AI agent work — directing, reviewing, and course-correcting. Without naming this layer explicitly, teams treat agent oversight as an afterthought. The ThoughtWorks retreat (covered in [Episode 15](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/)) identified it as a first-class concern.

### Code Garbage Collection

[Code garbage collection](/glossary/code-garbage-collection/) — periodically using AI coding tools to identify and remove dead code, unused dependencies, and stale configurations — is emerging as a necessary hygiene practice. Using AI to clean up the mess that AI-assisted development creates. Covered in [Episode 17](/episodes/17-slop-garbage-collection-cleanroom-rewrites-and-will-claude-ruin-our-teams/).

### Risk Tiering for Code Review

Not all AI-generated code needs the same level of review. The ThoughtWorks retreat proposed tiering code by risk: some AI output can ship with automated checks only, some needs human review, some needs senior sign-off. This is more sustainable than Amazon's current approach of requiring senior sign-off on everything.

### Slowing Down

Mario Zechner's essay argues for deliberate pacing in AI-assisted development. The hosts extended this into the cognitive bankruptcy concept: speed without comprehension is a liability. The practical application: after a long vibe coding session, close the AI and read your own code. If you can trace the data flow, you're fine. If you can't, you've been accumulating debt.

## The Evolution of the Term

It's worth noting how quickly "vibe coding" went from a neutral descriptor to a loaded term:

| Date | Episode | What Changed |
|------|---------|-------------|
| Dec 2025 | [Ep 7](/episodes/7-project-vend-update-hallucinating-neurons-and-year-end-reflections/) | First reference to vibe coding (coined by Andrej Karpathy) |
| Feb 2026 | [Ep 12](/episodes/12-the-openclaw-saga-how-ai-affects-programming-skills-and-how-vibe-coding-is-addictive-like-gambling/) | Inflection point — "addictive like gambling," dark flow introduced |
| Feb 2026 | [Ep 14](/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt/) | Structural analysis — cognitive debt, 7-8 week wall |
| Feb 2026 | [Ep 15](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/) | Institutional response — ThoughtWorks retreat findings |
| Mar 2026 | [Ep 16](/episodes/16-pentagon-anthropic-drama-verified-spec-driven-development-and-interview-with-martin-alderson/) | Practical remedies — VSDD methodology |
| Apr 2026 | [Ep 20](/episodes/20-claude-code-source-leak-emotion-concepts-in-llms-and-surprising-facts-ais-know-about-us/) | Full vocabulary — cognitive bankruptcy coined |

In four months, the conversation moved from "here's a thing people do" to "here's a complete risk framework with named failure modes and tested mitigations." That arc tells you something about how fast the field is learning from its own mistakes.

## Frequently Asked Questions

### Is vibe coding just bad coding?

No. Vibe coding is a style of AI-assisted development that trades deep understanding for speed. That trade-off is rational in some contexts (prototyping, disposable code, personal tools) and dangerous in others (production systems, team codebases, anything you need to maintain). The problem isn't the practice — it's doing it without understanding the risks.

### How do I know if I'm in dark flow?

Ask yourself: could you explain what the last three AI-generated changes do, without looking at the code? Could you predict what would break if you removed them? If the answer to either question is no, you're in dark flow. The feeling of productivity is the tell — genuine flow involves comprehension, not just activity.

### Is this just the "AI will make developers lazy" argument?

It's more specific than that. The Wharton research shows the effect is asymmetric: people with high need-for-cognition use AI as a complement and get better. People who prefer to avoid effortful thinking defer to AI more readily. Vibe coding doesn't make everyone lazy — it makes some people faster and others more dependent, widening the gap between the two groups.

### Can I vibe code safely on a team?

Yes, with guardrails. Spec-driven development, VSDD, risk-tiered code review, and code garbage collection all help. The key requirement is that at least one person on the team understands every change that ships. If nobody can trace a request through the system, you've hit the cognitive debt wall regardless of how many tests pass.

### What's the difference between cognitive debt and technical debt?

Technical debt is conscious: you took a shortcut, you know where it is, you can choose when to pay it down. Cognitive debt is unconscious: the code works, tests pass, but nobody understands why. You don't know you have it until you need to modify something and realize you can't reason about the system. That makes it harder to identify and harder to address.

### How long before cognitive debt becomes a problem?

The empirical pattern is 7-8 weeks of heavy AI-assisted development. But this varies by team size, code complexity, and how much review is happening. A solo developer building a simple CRUD app might go longer. A team building a distributed system might hit the wall sooner.

### Should I stop using AI coding tools?

No. The goal isn't to avoid AI-assisted development — it's to maintain understanding while using it. The antidotes (spec-driven development, VSDD, code garbage collection, the middle loop) aren't about slowing down. They're about staying aware of what the AI is doing and ensuring someone on your team can explain every change that ships.

---

*This guide synthesizes content from Episodes 3, 5, 7, 12, 14, 15, 16, and 20 of the ADI Pod. Updated April 2026.*
