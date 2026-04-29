---
title: "Why AI Code Has 1.7x More Bugs (and What to Do About It)"
description: "CodeRabbit's data shows AI-authored PRs have 1.7x more findings. The number alone misses the real story, so here's what it means for your team."
date: "2026-04-11"
lastUpdated: "2026-04-28"
slug: "ai-code-quality-bugs"
keywords: "AI code quality, AI code bugs, AI-generated code review, CodeRabbit AI report"
episodes: ["7", "12", "15", "22"]
---

AI-generated code has measurably more defects than human-written code. That's not hype, conjecture, or vibes; it's what the data says. The question worth asking isn't whether the number is real, but what it actually tells you about the failure mode and whether your team is set up to catch it.

In late 2025, [CodeRabbit](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report) (an AI code review company) published their "State of AI vs Human Code Generation" report. They analyzed hundreds of open-source pull requests: 320 AI co-authored PRs and 150 human-only PRs. The headline finding was stark. AI-authored PRs had 1.7x more review findings than their human-written counterparts, and 1.4x more critical issues. The dominant category wasn't formatting, style, or naming. It was logic and correctness: AI-authored PRs were 1.75x more likely to contain logical errors.

When [we covered this on ADI Pod](/episodes/7-project-vend-update-hallucinating-neurons-and-year-end-reflections/), my co-host Dan Lasky made a point that stayed with me: "If you think about the stochastic parrot argument, there isn't necessarily logic behind the choices that are being made." CodeRabbit's own conclusion reinforced this. AI tends to generate surface-level correctness without fully understanding the business context. The code compiles. The tests might even pass. But the logic is wrong in ways that require domain knowledge to detect.

That's a specific kind of failure, and specificity matters here. Because the 1.7x number, taken without context, can lead you in exactly the wrong direction.

## What the Numbers Actually Mean

The CodeRabbit data points to a pattern that's more interesting than "AI writes buggier code." It suggests that AI code fails differently than human code, and that the failure mode has implications for how you structure your review process.

Human bugs tend to cluster around oversight: a missed edge case, a forgotten null check, a race condition introduced under time pressure. These are errors of omission. The developer knew the domain but missed a detail. AI bugs, by contrast, cluster around logic and correctness. The code looks plausible. It follows the patterns of the codebase. But it doesn't actually implement the intended behavior, because the model was pattern-matching rather than reasoning about business requirements.

This distinction maps cleanly to something the [ThoughtWorks Future of Software Engineering retreat](https://www.thoughtworks.com/content/dam/thoughtworks/documents/report/tw_future%20_of_software_development_retreat_%20key_takeaways.pdf) identified, a concept they call [cognitive debt](/glossary/cognitive-debt/). As we [discussed on the show](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/), when agents are writing the code and humans are reviewing it all day, your brain eventually stops being fully engaged. The first few PRs get rigorous scrutiny. By the afternoon, you're rubber-stamping. Same phenomenon as judicial decision fatigue: judges' rulings measurably deteriorate as they get closer to lunch.

So the 1.7x finding isn't just about the AI producing more bugs. It's about the combination: AI produces a specific type of bug (logic errors that look correct on the surface) and humans are reviewing under conditions that make those exact bugs harder to catch. The failure is systemic, not attributable to one side.

| | Human-Written Code | AI-Generated Code |
|---|---|---|
| **Dominant bug type** | Oversight (missed edge cases, forgotten checks) | Logic errors (plausible but incorrect behavior) |
| **Failure signature** | Obviously wrong when found | Looks correct on the surface |
| **Root cause** | Developer knew the domain, missed a detail | Model pattern-matched without business context |
| **Detection method** | Standard code review catches most | Requires domain knowledge and active reasoning |
| **Review risk** | Fatigued reviewers still spot obvious gaps | Fatigued reviewers rubber-stamp plausible code |

## What the Numbers Don't Mean

Three caveats before anyone concludes that AI coding is a net negative.

**First, the data source matters.** CodeRabbit analyzed open-source pull requests. As Dan pointed out, what was the average size of these PRs? If they skew smaller (a handful of if statements and a function) logic errors would naturally dominate the finding categories. The distribution of defect types might look different in larger, more complex PRs where architectural mistakes matter more. The 1.7x number is a signal, not a universal constant.

**Second, the comparison isn't apples to apples.** The study compared AI-authored PRs to human-authored PRs, but it didn't control for the difficulty of the task, the experience of the contributor, or the quality of the prompts that produced the AI code. A senior engineer with deep domain context and a well-crafted prompt workflow is going to produce different AI output than someone who typed "fix the login bug" and hit enter. CodeRabbit acknowledged this: AI without business context produces surface-level correctness. But that's a context engineering problem as much as a model capability problem.

**Third, the number will change.** Models are improving at agentic tasks measurably. Between 2025 and 2026, we saw Sonnet 4.6 outperform Opus 4.6 on agentic benchmarks, with a smaller, cheaper model beating the flagship on real-world tasks. The 1.7x figure is a snapshot, not a trend line. What matters more than the current number is the structural pattern: AI fails in ways that are qualitatively different from how humans fail, and your processes need to account for that regardless of the magnitude.

## The Skill Formation Problem

The CodeRabbit data is a measurement of output quality. But there's a deeper concern that shows up when you look at the process, not just the product.

Anthropic published [research on how AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills). In the study, 52 junior developers were split into two groups, one with AI assistance and one without, and given 35 minutes to complete tasks using an unfamiliar Python library. Everyone finished. But when quizzed afterward, the developers who had fully delegated their thinking to the AI scored only 39% on comprehension. The ones who generated code first and then asked focused questions about what the code did scored 86%.

The most damaging pattern was what Anthropic called iterative AI debugging, where developers repeatedly used AI to troubleshoot errors without understanding them. Those developers scored just 24% on the quiz and took the longest to finish. They were stuck in a loop: the AI would fix one thing and break another, and the developer lacked the mental model to tell the difference.

This connects directly to the CodeRabbit finding. If the developers writing AI-assisted code aren't building mental models of what the code does, they're unlikely to catch the logic errors that the AI produces. The 1.7x gap isn't just about AI capability. It's about the human's capacity to verify the output. What you might call [verification debt](/glossary/verification-debt/): the accumulated cost of accepting AI output without sufficient comprehension.

Fast.ai described a related concept called [dark flow](/glossary/dark-flow/), the opposite of the flow state. Where flow produces deep engagement with a challenging but manageable task, dark flow is the trance of pulling the slot machine lever. Vibe coding feels productive. The code appears. The terminal is green. But the sense of progress is partly illusory. Like a slot machine showing three sevens and a lemon, it feels almost right, so you pull the lever again. As [we discussed on the show](/episodes/12-the-openclaw-saga-how-ai-affects-programming-skills-and-how-vibe-coding-is-addictive-like-gambling/), the bar feels low because "the computer is writing its own code" and the novelty is still doing real work on our perception of quality.

The interaction between these findings is what makes the problem structural. AI produces more logic errors. Developers who over-delegate lose the ability to catch logic errors. And the experience of using AI coding tools actively discourages the deep engagement that builds the skill to catch them. Each piece reinforces the others.

## The Review Bottleneck

If writing code is no longer the constraint, then code review becomes the bottleneck. [Chris Roth's "Building An Elite AI Engineering Culture" article](https://www.cjroth.com/blog/2026-02-18-building-an-elite-engineering-culture) named this the productivity paradox: the bottleneck always moves. Automate the writing, and now your team spends all day reviewing. As Rahul Yadav observed on [episode 15](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/): you can use AI agents for code review too, but the question becomes one of risk profiling.

The ThoughtWorks retreat arrived at a framework for this that I find genuinely useful: risk tiering. Not all code deserves the same review scrutiny. An internal tool that touches nothing critical can get a lighter pass. Production code that handles financial transactions needs the full rigor. The key insight is that this isn't about cutting corners; it's about allocating a finite resource (your attention and judgment) to where the consequences of failure are highest.

The practical implication is scheduling. If your peak cognitive hours are 9 to 11 AM, that's when you review the high-risk PRs. The lower-risk agent output gets batched for the afternoon. You're optimizing your review process the same way you'd optimize a database query: not by doing less work, but by putting the expensive operations where they have the most impact.

There's a human cost here too, and it's worth naming. Code review has historically served two purposes: quality gating and mentorship. When a senior developer reviews a junior's PR, they aren't just checking the code. They're teaching architectural judgment, naming conventions, design patterns. If agents are writing the code and other agents are reviewing the low-risk PRs, that mentoring surface area shrinks. As Rahul put it: "Do you mentor people on how to write good prompts? I don't know what that looks like."

The ThoughtWorks retreat identified this loss explicitly. The human activities that code review supported (mentoring, consistency enforcement, knowledge sharing) need to migrate somewhere else. Where they go is still an open question.

## What to Do About It

The answer isn't to stop using AI for coding. The answer is to recognize that AI changes the type of work, not the amount, and to restructure accordingly. Here's what that looks like in practice.

**Tier your reviews by risk.** Adopt the ThoughtWorks risk tiering model. Classify code by blast radius (what breaks if this is wrong) and match review rigor to consequence. Low-risk internal tooling gets a lighter pass. Anything touching production data, financial transactions, or security boundaries gets the full review from a fresh pair of eyes during peak hours.

**Invest in your middle loop.** The ThoughtWorks retreat named a concept they call the [middle loop](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/), the layer between your local development work and your CI/CD pipeline where you're orchestrating agents, maintaining context files, and building the scaffolding that makes agents effective. This is unglamorous work that doesn't show up in any ticket. Dedicate a recurring block of time (weekly, at minimum) to sharpening your agent workflows, writing skills, and building the infrastructure that reduces the surface area for logic errors.

**Use AI to learn, not just to produce.** Anthropic's research showed that the developers who scored highest were the ones who generated code and then asked the AI to explain it. Not the ones who delegated everything, and not the ones who ignored AI entirely. The highest-performing pattern was generate first, comprehend second. Build this into your workflow: after the agent writes a non-trivial function, ask it why it chose that approach, what the tradeoffs are, and where it's least confident.

**Watch for [dark flow](/blog/dark-flow-vibe-coding/).** If you find yourself pulling the lever, regenerating, re-prompting, iterating without pausing to understand what changed, you're in dark flow. The slot machine metaphor isn't cute. It's describing a real cognitive pattern where the feeling of productivity substitutes for actual comprehension. When you notice it, stop. Read the diff. Build the mental model. The two minutes you spend understanding the code will save you twenty minutes debugging the logic error it introduced.

**Don't treat the 1.7x number as permanent.** Models are improving. Tooling is improving. But the structural pattern (AI failing differently than humans, verification requiring active comprehension, review attention being a finite resource) is unlikely to change even as the specific numbers do. Build your processes around the pattern, not the point estimate. And don't assume the more capable model is the lower-defect one for your task: in [Episode 22](/episodes/22-is-claude-opus-4-7-mythos-distilled-running-qwen-3-6-locally-and-the-ai-on-ai-arena/) we covered Simon Willison's pelican-on-a-bicycle benchmark breaking for the first time, with a much smaller open-weight model (Qwen 3.6 35B A3B) producing a better drawing than Claude Opus 4.7 — a small reminder that capability ranking does not automatically translate into per-task output quality.

## The Uncomfortable Middle Ground

The honest assessment of AI code quality in early 2026 is that it's simultaneously worse than its advocates claim and better than its critics suggest. The 1.7x finding is real and meaningful. It's also a single study, from a company that sells AI code review, based on open-source PRs that may not represent your production codebase. Hold all of that at once.

What the data does establish, beyond reasonable doubt, is that AI code requires a different kind of scrutiny than human code. Not more scrutiny, but different scrutiny. The bugs are logic errors, not typos. The failure mode is surface-level plausibility, not obvious wrongness. And the human reviewers are subject to cognitive fatigue that makes exactly those bugs harder to catch.

The teams that will handle this well aren't the ones that ban AI coding tools or the ones that adopt them uncritically. They're the ones that restructure their review processes around the specific failure mode, invest in maintaining their own comprehension, and resist the pull toward what you might call [cognitive surrender](/blog/cognitive-surrender-ai/), the gradual outsourcing of judgment to a system that can't exercise it. The gap between AI output and verified correctness is a form of debt that compounds if you ignore it. [Verification debt](/glossary/verification-debt/) accumulates silently until something breaks in production and nobody on the team can explain why.

The 1.7x number is a useful alarm bell. What you build in response to it matters more than the number itself. For a broader look at how [AI coding agents compare](/topics/ai-coding-agents-compared/) and where the tooling is headed, things are changing fast. But the fundamentals (verify what you ship, understand what you merge, allocate your attention where the stakes are highest) are older than any of us, and no amount of new tooling changes that.
