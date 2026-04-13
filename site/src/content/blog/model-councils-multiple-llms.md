---
title: "Model Councils: Why Running Multiple LLMs Beats Trusting Just One"
description: "A single AI model has blind spots it cannot see. Running two or three in parallel — a model council — turns those blind spots into signal. Here is how to set one up."
date: "2026-04-11"
slug: "model-councils-multiple-llms"
keywords: "model councils LLM, multiple AI models, multi-model workflow, AI coding workflow"
episodes: ["14"]
---

Every model you use has a failure mode you have never noticed. Not because you are careless, but because the model's blind spots are invisible when it is the only one talking. You ask Claude a question, get a confident answer, and move on. You ask GPT the same question, get a different confident answer, and now you have information. That gap between two confident answers is where the signal lives.

This is the core argument for model councils: not running multiple models as a benchmark exercise, not for evaluation theater, but as a practical development workflow that surfaces disagreement you would otherwise ship as fact. If you are [comparing AI coding agents](/topics/ai-coding-agents-compared/) and trying to figure out which one to commit to, councils offer a different answer — maybe commit to several.

[Perplexity formalized this in early 2026](https://www.perplexity.ai/hub/blog/introducing-model-council) with their Model Council feature, which runs Opus, GPT-5.2, and Gemini 3 simultaneously on a query and synthesizes the results. When [we discussed it on ADI Pod episode 14](/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt/) — prompted by a listener email, no less — it became clear that the interesting part is not the product. The interesting part is the pattern.

## The Problem: Confident Errors Look Identical to Correct Answers

The fundamental issue with single-model workflows is not that models are wrong often. It is that when they are wrong, they sound exactly like when they are right. This is the [sycophancy](/glossary/agent-sycophancy/) problem turned sideways — and if you want to see how deep it goes, we built a [practical test for it](/blog/ai-sycophancy-test/). A model will not flag its own uncertainty unless you specifically architect for it, and even then its self-assessment is unreliable. Models are, to borrow a phrase we use on the show, [benchmaxxed](/glossary/benchmaxxed/) — optimized for looking good on evaluations, not for knowing when they do not know.

A second model does not solve hallucination. But a second model that disagrees with the first model gives you a clear signal that further investigation is warranted. That signal — the disagreement itself — is the value.

## A Three-Level Framework for Multi-Model Workflows

Not every task justifies the overhead of running multiple models. The cost scales linearly with the number of models you invoke, and the latency penalty is real unless you run them in parallel. Based on what we discussed in [episode 14](/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt/) and my own experimentation since, here is a rough framework for when multi-model approaches earn their keep.

### Level 1: Manual Cross-Check (Cost: Minutes)

The simplest version is what I was already doing before model councils had a name: copy the same prompt into two or three chat windows and compare outputs. No tooling required. No API costs beyond what you are already paying.

This is worth the effort when the question is open-ended, requires deep world knowledge, or when you need to make a decision that is hard to reverse. Architecture choices, API design decisions, choosing between competing approaches — these are cases where a single model's framing can quietly lock you into a suboptimal path. I have caught Sonnet confidently recommending patterns that Gemini flagged as deprecated, and vice versa. Neither was wrong in a way I could have spotted without the other.

The limitation is obvious: it is tedious. When I admitted on the podcast that I was doing this manually rather than through OpenRouter, Rahul was not impressed.

### Level 2: Automated Council with Synthesis (Cost: 3-5x Tokens)

This is the Perplexity approach, and it is also what Andrej Karpathy built with his [llm-council](https://github.com/karpathy/llm-council) repo. You define which models participate, route the same prompt to all of them in parallel, and then have a synthesizer model — ideally your strongest available model — produce a combined answer with attribution.

I tested Karpathy's LLM Console with Gemini 3 Pro, Claude Sonnet, and GPT-5.2. The results were immediately informative, though not in the way I expected. The synthesizer does not just merge answers — it provides a rubric showing where each model's strengths and weaknesses lie. You can see, off the bat, that Sonnet was the weakest of the three on my particular queries. The synthesis layer turns three mediocre data points into a genuinely useful map of confidence.

The key insight from testing: the strongest model should be the judge, not necessarily the one generating answers. In my experience, Gemini 3 Pro was the strongest synthesizer for that particular comparison. I would probably use Opus for high-stakes reasoning tasks. The choice of judge model matters more than the choice of participant models.

### Level 3: Agent-Level Verification (Cost: Architectural Complexity)

This goes beyond councils into agent design patterns, but it is the logical extension. As Rahul described it on the episode: the agent doing the task is different from the agent verifying that the doer did the job. They work off the same spec, but the verifier has no access to the generator's reasoning — only the output and the original requirements.

Combined with TDD — write the tests first, then let the agent satisfy them — you get a workflow where the generator cannot simply match its tests to its implementation. The tests exist independently. The verifier exists independently. The council pattern, at this level, becomes an architectural principle rather than a prompting trick.

## What Patterns Emerge

After running multi-model comparisons for several months, three consistent patterns have surfaced.

**Pattern 1: Disagreement clusters around ambiguity.** When models agree, the question was usually well-specified. When they disagree, the question was under-specified or genuinely ambiguous. This is useful information even if you never read the actual responses — the disagreement itself tells you your prompt needs work.

**Pattern 2: The strongest model is not always the most useful participant.** The model that contributes the most to a council is often not the one that would score highest on a benchmark. A weaker model that makes a different kind of error than the strong model is more valuable than a slightly-less-strong model that makes the same errors. Diversity of failure modes matters more than average quality.

**Pattern 3: Self-verification is cheaper and surprisingly effective.** Before setting up a multi-model council, try asking the same model to check its own work iteratively. I first read about this approach on Steve Yegge's blog: run the model, ask it to review and improve, repeat up to five times. The output converges, and the converged solution is usually meaningfully better than the initial one. This is not as robust as cross-model verification — a model's blind spots tend to persist across iterations — but it captures maybe 60-70% of the value at a fraction of the cost.

## When It Is Not Worth the Overhead

Model councils have a clear failure mode: using them on tasks where a single model is already reliable enough. If you are generating boilerplate CRUD endpoints, writing unit tests for well-specified functions, or doing straightforward code transformations, the council adds latency and cost without meaningful signal. The disagreements you surface will be stylistic, not substantive.

The overhead is also harder to justify as individual model quality improves. The gap between Sonnet, GPT-5.2, and Gemini 3 on most coding tasks is smaller than the gap between any of them and the models we were using eighteen months ago. If the models all converge on the same answer — and they increasingly do for well-defined tasks — the council tells you nothing you did not already know.

The sweet spot remains tasks with genuine ambiguity: architectural decisions, open-ended research, any question where "it depends" is the honest answer. Those are exactly the cases where a single model's confident framing is most dangerous, and where a second or third perspective is most likely to surface something you would have missed.

## Setting One Up

If you want to try this without a $200/month Perplexity Max subscription, the practical path is Karpathy's [llm-council](https://github.com/karpathy/llm-council) repo with an OpenRouter API key. Configure two or three models — I would suggest picking models from different providers rather than different tiers from the same provider, since models from the same family tend to share blind spots. Set your strongest available model as the synthesizer.

For the quick-and-dirty version: open two chat windows. Ask the same question. Read both answers. When they agree, proceed with confidence. When they disagree, you have just saved yourself from shipping a mistake.

The real value of model councils is not the synthesized answer. It is the discipline of treating any single model's output as a hypothesis rather than a conclusion. Once you internalize that frame, you start noticing the moments where you were about to trust a confident response without verification — and those moments, it turns out, are where most of the quiet errors live.
