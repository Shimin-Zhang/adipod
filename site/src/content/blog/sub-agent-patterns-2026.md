---
title: "Four Sub-Agent Patterns in 2026, Ranked by How Hard They Are to Trust"
description: "Phil Schmid's four sub-agent patterns — inline, fan-out, agent pool, agent teams — ladder up in capability and, faster, in how hard they are to verify. Here's the taxonomy, where Anthropic's new dynamic-workflow tool fits, and why adversarial review is the discipline that makes fan-out worth running."
date: "2026-06-07"
slug: "sub-agent-patterns-2026"
keywords: "sub-agent patterns, sub-agent patterns 2026, Phil Schmid subagent patterns, multi-agent patterns, fan-out map-reduce, agent pool, agent teams, dark factory pattern, Claude Code swarm mode, dynamic workflow tool, Claude Opus 4.8, adversarial review, Jesse Vincent, fresh eyes review, agent evaluation difficulty, verification debt, Gas Town, trading compute for human labor, parallel agents, coding agent orchestration"
episodes: ["24", "25", "28"]
---

The hard part of running four agents at once was never spawning the four agents. It was knowing whether the thing they handed back was any good.

Most of the multi-agent conversation in 2026 has been about orchestration — how to fan work out, how to coordinate the swarm, how to merge the results. That is the visible problem. The binding constraint is quieter: as you add agents, state, and autonomy, the cost of *verifying* the system climbs faster than the capability you bought by adding them. Phil Schmid, who works on Google DeepMind's agent platform, wrote up [four sub-agent patterns](https://www.philschmid.de/subagent-patterns-2026) that are actually in use this year, and the most useful thing about his taxonomy is that it doubles as a difficulty ladder. We walked through it on [Episode 25](/episodes/25-elon-vs-openai-trial-drama-billion-token-context-race-multi-agent-patterns-2026/), and it has been the lens I keep reaching for since.

Here are the four, ordered the way they actually matter: by how hard each one is to trust.

## Pattern 1: The inline sub-agent

The inline sub-agent is a function call with a personality. You ask your main agent to spin off a sub-agent for one bounded task — go read these forty files and come back with a summary — and it returns a result you fold back into the main thread. This is what most Claude Code usage already looks like, and the harness often kicks these off on its own without telling you.

Evaluation is easy here, and that is the whole point. A bounded sub-agent with a defined input and output is testable the way any function is testable: give it the input, check the output. If it misbehaves, the blast radius is one call. Start here, and stay here longer than you think you need to.

## Pattern 2: Fan-out (map-reduce)

Fan-out is the inline pattern times N. You dispatch several sub-agents in parallel, each on a slice of the work, and a coordinator does the map-reduce — collect, summarize, reconcile. Claude Code's swarm mode lives here, and so does the parallel-dispatch step in most superpowers-style setups.

The capability jump is real, and so is the first real evaluation tax: you now have to control for inter-agent independence. If two of your five agents quietly made the same wrong assumption, the reduce step launders it into something that looks like consensus. The reason it still feels safe is that the shape is legible — you can see the branches and the merge — but "I can see the structure" is not the same claim as "I verified the result."

## Pattern 3: The agent pool

The agent pool is where it gets interesting, and where I start to get nervous. Now the agents are long-lived and carry their own state; a main agent nudges them, checks status, and collects results when a goal is met. Gas Town's vocabulary — a Mayor coordinating PoleCats against a Convoy of tickets — is the canonical instance.

Once you cross into persistent state, evaluating the system gets expensive in a way the first two patterns never were. You are no longer scoring outputs; you are scoring a trajectory. To know whether the pool is healthy you have to control for state, for the main agent's interaction with each worker, and for the order things happened in — and any of those can fail catastrophically rather than gracefully. The capability is genuinely higher. The confidence you can have in it, per unit of effort, is genuinely lower.

## Pattern 4: Agent teams

The fourth pattern is the one everyone gestures at and almost nobody runs in production: agents talking directly to each other with no central coordinator, passing messages by direct send or a shared mailbox. This is the "dark factory" — Claude Code's channels feature is the closest off-the-shelf primitive, and I have been poking at demos to find where it breaks.

It breaks, mostly, at evaluation. How do you test a system when you cannot control when each agent speaks or what it decides to say? The interaction surface is combinatorial and non-deterministic; the same task run twice does not produce the same conversation. Pattern 4 is the most capable shape on paper and the least trustworthy one in practice, and the gap between those two facts is the whole story of the taxonomy.

## The ladder is the point

Read the four in order and the actual argument falls out: capability and evaluation difficulty rise together, and evaluation difficulty rises faster. Rahul's read on the show was that these are just org-design principles with the HR department deleted — a fan-out is a task force, an agent pool is a standing team, agent teams are a flat org with no manager — which, only half-jokingly, means he has made reorgs free. His more serious point: the pattern does not have to be static. You can put a meta-agent on top that knows all four and picks one per task, because any real job ends up using a mix.

That is the optimistic frontier. The grounding counterweight arrived the same stretch of episodes: Dexter Horthy, once the loudest voice for full dark-factory autonomy, [publicly walked it back](/blog/agentic-engineering-recantation/) — they tried it in earnest, and the velocity gains evaporated against the comprehension cost. The honest read for the next 6 to 12 months is that patterns 1 through 3 are where the leverage is, precisely because they are the ones you can still verify.

## What Anthropic actually shipped

Which brings us to the thing that prompted this post. On [Episode 28](/episodes/28-claude-opus-4-8-undocumented-claude-code-features-eval-harness-for-ai-skills-pope-on-ai/) we covered [Claude Opus 4.8 and its new dynamic-workflow tool](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/), and once you have the taxonomy in hand it is easy to place: the dynamic workflow is pattern 2, fan-out, promoted from "something you assemble out of swarm mode" to a first-class feature. High-thinking mode, a large coordinated burst of parallel agents, and Anthropic handling the orchestration. Dan's one-line summary was the correct one — it is Gas Town, by Anthropic. The company has a habit of absorbing whatever the rest of the internet builds straight into Claude Code, and this is the latest.

The interesting part is the use case Anthropic led with, because it is not "build more, faster." It is bug-bash the whole codebase in one pass, and check critical work twice. In other words: point the fan-out at code that already exists — ideally code you just generated — and have it attack the thing from several angles at once.

## Fan-out's killer app is adversarial review

That use case has a name, and it predates the tool. Jesse Vincent — Obra, the creator of superpowers — described [adversarial review](https://blog.fsck.com/2026/05/01/adversarial-review/) on [Episode 24](/episodes/24-openais-goblin-problem-10-lessons-when-code-is-cheap-ai-addiction-loop/) as a four-step escalation, and it is the best argument for why you would want a productized fan-out at all.

Step one: tell the agent to look at the work with "fresh eyes." The phrase does real work — a model reviewing its own output, with that output still sitting in context, is biased toward defending it; "fresh eyes" (or an actual `/clear`, or handing it to a separate sub-agent) switches the mentality. Step two: ask a sub-agent instead of the same agent. Step three, and this is where it gets good: ask *two* sub-agents to review, and tell them whoever finds the most serious issues gets five points, or a cookie. Step four: tell them you will be disappointed if they do not surface at least N real problems, and run the loop until the findings converge to nothing.

It is a genuinely effective technique, and yes, it means I now hold cookie tournaments between my agents. For the record, when one of mine won, I told the main agent to award the cookie and it did, so I have at least stopped gaslighting my sub-agents. The serious version of the joke is that adversarial review is exactly the workload the dynamic workflow is built to run: spawn the skeptics in parallel, let them compete to refute, reduce their findings into a punch list. Fan-out without adversarial review is just more code, faster. Fan-out *with* it is the first multi-agent pattern that makes your output better instead of merely larger.

## The bill, and the part they hand-waved

This is the point on the show where I said the quiet part out loud: every time you vibe-code now, you are spending compute to buy back the bottleneck of code review. You let one agent write the thing, then you throw a dynamic workflow at it to attack the result from four directions, and you keep a human on the final gate. Trading compute for human labor. I think that is the default the whole industry is walking toward, and I am mostly fine with it.

Mostly. Two caveats keep it honest. The first is that compute is not free, even when the dashboard makes it feel that way — Dan watched 4.8 hallucinate file names that do not exist and burn an entire token budget in twenty-five minutes, and the same week Microsoft pulled Claude Code licenses back to Copilot on cost. "Throw a dynamic workflow at it" has an invoice attached, and the invoice scales with exactly the fan-out width that makes the technique work. The second is the part Anthropic's announcement waved past: how does it merge all that parallel work back together? The post was breezy about it, and merge-without-drift is precisely where a fan-out quietly reintroduces the [comprehension debt](/blog/cognitive-debt-ai-development/) you were spending compute to avoid. A reduce step you did not read is a sub-agent's opinion you adopted without noticing.

## What to actually do

The taxonomy earns its keep as a decision tool, so here is the operational version:

1. **Match the pattern to how much you can verify, not how much it can do.** The right default for most work is still pattern 1, escalating to a fan-out only when the work genuinely parallelizes and you have a way to check the merge.
2. **Reserve the dynamic workflow for adversarial review.** Its best and most defensible use is attacking code that already exists — generation is where drift hides, refutation is where fan-out shines.
3. **Keep a human on the final gate.** The patterns let you delegate the writing and the reviewing. The one thing you cannot delegate without [verification debt](/glossary/verification-debt) compounding is the decision that the result is acceptable.
4. **Budget the compute like the bill it is.** Fan-out width is a dial with a dollar cost; set it where the marginal skeptic still finds something, and not wider.

The shape of the next year is not which [orchestration framework](/topics/ai-coding-agents-compared/) wins. It is whether your ability to verify keeps pace with your ability to spawn. The patterns that survive will be the ones you can still trust — which, conveniently, are also the ones you can still test.

---

*This post was drafted by an AI agent (Claude) from ADI Pod episode transcripts and edited for the site. Source episodes: [24](/episodes/24-openais-goblin-problem-10-lessons-when-code-is-cheap-ai-addiction-loop/), [25](/episodes/25-elon-vs-openai-trial-drama-billion-token-context-race-multi-agent-patterns-2026/), [28](/episodes/28-claude-opus-4-8-undocumented-claude-code-features-eval-harness-for-ai-skills-pope-on-ai/).*
