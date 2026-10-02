---
title: "Build As If Tokens Were 1000x Cheaper: What the Plunging Price of AI Means for Developers"
description: "Epoch AI finds the cost of a fixed level of AI performance falling about 13x a year, faster than compute, batteries, or electricity ever fell. Here's what three years of that curve, and a year of podcast arguments about it, suggest you should build, learn, and stop worrying about."
date: "2026-10-02"
slug: "plunging-price-of-ai-tokens"
keywords: "AI inference cost falling, cost of AI tokens 2026, LLM price trend, price of intelligence, Epoch AI plunging price of thought, AI cost per task, cheap LLM tokens, Jevons paradox AI, good enough AI models, theory of constraints AI, verifiable vs unverifiable work, taste and judgment developers, AI token budget, inference subsidy, GLM 5.3 Flash price, Fable 5 usage share, build for future models, developer career AI cost"
episodes: ["5", "13", "14", "15", "24", "26", "27", "28", "29", "30", "33", "38", "39", "41"]
---

Whatever you're building with AI right now, you're probably pricing it wrong. The tokens will cost about a tenth as much next year, and a hundredth the year after.

That's my compressed read of [The Plunging Price of Thought](https://epoch.ai/publications/the-plunging-price-of-thought), a report by Luke Emberson and David Roodman at Epoch AI that Rahul brought to [Episode 41](/episodes/41-meta-muses-0-day-dhhs-rails-world-keynote-gpt-6-astra-the-llmentalist-effect/). They measured what it actually costs a model to reach a fixed score on five benchmarks covering math, hard science, and games of skill. Since 2023, that cost has fallen about 47% per quarter, or 13x per year.

The comparison chart is the part that sticks. That rate is four times faster than DNA sequencing got cheaper, six times faster than compute, 18 times faster than lithium batteries, and 54 times faster than electricity did over the century to 1973. Their concrete example: in January 2025, o3 scored 75% on GPQA Diamond for about 30 cents a question. Under 18 months later, GPT-5.6 Luna matched it for $0.0004. That's a 725-fold drop. Epoch compares it to the sticker price of a new car falling from $50,000 to $69.

On the show I said we should treat tokens as if they're already a thousand times cheaper than they are, because soon enough they will be. This post is me trying to work out what that means in practice. It draws on a year of arguments with Dan and Rahul, because it turns out we'd been circling this curve long before Epoch gave it a number.

## First, the Caveats Epoch Puts on Its Own Data

The report is admirably honest about its limits, and three of them matter for anyone building on it.

**Benchmarks aren't work.** Labs may be training against these benchmarks ([benchmaxxing](/glossary/benchmaxxed/)), and a benchmark score isn't the same thing as useful output. Epoch's secret-game benchmark, designed to resist that, declines a bit slower than average. Their verdict is "consistent with the benchmaxxing critique being valid but not fatal."

**Nobody lives on the cost frontier.** The 13x figure assumes a user who constantly shops for the cheapest model that can do each task. Real teams pick a model and stay there for months, so they don't capture the full decline. I'd argue this is the most actionable caveat in the report, and I'll come back to it.

**The decline isn't uniform.** Math gets cheaper fastest (50–52% a quarter), game-style puzzles slowest (39–43%). And a level of performance gets cheaper fastest right after it first becomes state of the art, about 66% a quarter, then the decline halves over the next two years. The premium on a brand-new capability is real, and it doesn't last.

There's also a paradox Epoch flags right at the top: the AI boom is pushing *up* the price of everything it consumes (chips, power, even electricians) while the price of what it produces collapses. If you follow our [bubble tracker](/topics/ai-bubble-tracker/), that's the whole story in one sentence.

## Three Things That Happen When Something Gets Cheap

We've seen this movie before, just never at this speed. History gives three reasonably reliable predictions for what happens when a core input collapses in price, and each one has already shown up in our episode archive.

### 1. You use far more of it (Jevons)

The Jevons paradox says that making a resource cheaper to use increases total consumption. Coal-efficient steam engines led to more coal burned, not less. We've reached for it repeatedly on the show. In [Episode 5](/episodes/5-how-anthropic-engineers-use-ai-spec-driven-development-and-llm-psychological-profiles/), Dan flagged the number from Anthropic's internal survey: 27% of Claude-assisted work "consists of tasks that wouldn't have been done otherwise." My analogy at the time was Excel. In theory it made accounting easier, and the number of accountants exploded anyway.

In [Episode 24](/episodes/24-openais-goblin-problem-10-lessons-when-code-is-cheap-ai-addiction-loop/), Dan traced the same curve from punch cards to COBOL to LLMs. Each step made software cheaper to apply, so it got applied to more things. Rahul's caveat from [Episode 26](/episodes/26-llm-neural-anatomy-with-david-noel-ng-forward-deployed-everybody-running-llms-at-home/), via Jasmine Sun, is worth keeping in your pocket: Jevons says you get more of the thing. It doesn't promise that *humans* get more of it.

### 2. Good enough wins most of the calls

When the price of "pretty good" collapses, the market discovers it didn't need "best" for most jobs. My go-to analogy is Xiaomi. Its first phones were "this thing sucks" cheap, then they were good-enough cheap, and now Xiaomi is one of the largest smartphone makers in the world.

The AI version showed up in [Episode 38](/episodes/38-ai-homework-atrophy-github-commits-double-nick-muy-sit-down-ai-sandbagging/), when the [Financial Times reported](https://archive.ph/iaSsq) that Fable 5 was only about 11% of Anthropic's usage two months after launch. Dan's summary: "You don't even necessarily need Opus for most of your stuff. You just need it for like ten percent and a good router." A week later, in [Episode 39](/episodes/39-metas-ai-backfires-glm-5-3-flash-openais-jalapeno-chip-the-end-of-programming/), ZAI shipped [GLM 5.3 Flash](https://z.ai/blog/glm-5.3-flash) at $0.075 per million input tokens, against Sonnet 5's $2. It's not frontier intelligence, but it's good-enough intelligence at basement prices.

Rahul's framing from [Episode 33](/episodes/33-gpt-5-6-sol-meta-s-video-game-gulags-know-your-unknowns-the-permanent-underclass/) is the one I keep coming back to: "If you compare everything we have today to what was the frontier last year, it's a commodity today. And that's just going to keep happening." Or, as the line he was quoting put it, you don't need a Nobel laureate to generate a slide deck for you.

### 3. The constraint moves somewhere else

This is the one that matters for careers. Eliyahu Goldratt's *Theory of Constraints*, which Rahul brought up in [Episode 30](/episodes/30-fable-5-ban-metas-ai-gulag-elias-thorne-loop-engineering/), says every system has exactly one bottleneck, and the whole system's output is set by it. Speed up anything else and nothing changes. Remove the bottleneck and a new one appears somewhere else.

For most of software history, the bottleneck was typing the code. Cheap tokens are removing it, and the system's output is now set by whatever comes next. Rahul's list in that episode: "trust amongst humans, our coordination costs, our judgment." He also made the accountability point, which I think is underrated: "you can't really bring a system to court."

I made a related argument back in [Episode 14](/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt/), via David Oks: in any workflow, the bottleneck ends up being the most valuable part. If AI becomes cheap and commoditized and humans become the bottleneck, that's where the bargaining power goes.

## So Where Does the Value Go?

My working answer from Episode 41: anything with an objective, verifiable answer is on a short clock. Math and code got cheap first for a reason. Reinforcement learning from verifiable rewards, the technique behind reasoning models since DeepSeek R1, needs a checker that says right or wrong, and math and code come with one. Epoch's data agrees: math is where prices fall fastest.

What stays scarce is the work with no answer key: taste, judgment, creativity, deciding what to build and for whom. Dan put it more concisely in [Episode 28](/episodes/28-claude-opus-4-8-undocumented-claude-code-features-eval-harness-for-ai-skills-pope-on-ai/) when we were discussing Jamie Hurst's "Is This Sustainable?". I asked what isn't perishable. He said taste, I said judgment, and then he said the thing I've repeated to a lot of people since: "You were always hired for those things."

There's a structural reason this holds, too. As I put it in Episode 24, a model by definition produces the most likely code, the median. Your expertise is a different distribution sitting on top of that median. When the median costs almost nothing, the value is in the difference.

Rahul's counterweight deserves equal billing, because it keeps this from becoming a "just be creative" platitude. Intelligence is rarely the bottleneck in the real world. Pick almost anyone who changed things. They usually weren't the smartest person in the room. They knew how to play to their strengths and get things done. A genius in a data center at a penny an hour doesn't change that. If anything, it makes it more true.

## The Counterarguments (Tokens Aren't Free Yet)

I'd be overselling this if I stopped here. The archive has plenty of evidence that the *price you pay* doesn't follow the *cost Epoch measures*, at least not smoothly.

- **The subsidy is ending.** In Episode 30, Dan called it: "the age of not free but heavily subsidized inference is drawing to a close." Around the same time, Fable 5 moved off subscriptions to usage-based pricing ([Episode 29](/episodes/29-fable-5-mythos-5-launch-meta-ai-hack-llms-as-black-boxes-future-of-agents/)).
- **Frontier work is still expensive.** The Bun rewrite we covered in Episode 39 was 11 days and about 7,000 commits, and it would have cost roughly $165K at API prices. As I said on the show, we don't have a hundred thousand to spend on tokens. StrongDM's dark-factory benchmark of $1,000 in tokens per engineer per day ([Episode 13](/episodes/13-pi-coding-agent-dark-factories-the-furniture-makers-of-carolina/)) works out to a few hundred thousand dollars a year.
- **The bill gets noticed.** In [Episode 27](/episodes/27-openai-beats-musk-gemini-3-5-flash-and-ai-burnout-mitigation/), Microsoft reportedly cancelled Claude Code licenses for many engineers once the token costs exceeded the cost of the engineers.
- **Power is a hard floor.** Power keeps showing up in our Two Minutes to Midnight segment, most recently with Oracle invoking force majeure on a data center it can't get enough electricity to.

None of this contradicts Epoch. The cost of a *fixed* level of performance falls. But the frontier keeps moving, and most of us want the frontier. I think the honest synthesis is that last year's frontier gets very cheap, very fast, and this year's frontier stays expensive. So the strategic question becomes which of your workloads actually need this year's frontier. Per the FT data, the market's answer so far is "about 11% of them."

## How to Build As If Tokens Were 1000x Cheaper

Here's what I think the curve suggests, in rough order from "this week" to "this career."

1. **Price features against next year's tokens, not today's.** If a feature is great but costs too much per call, it's worth prototyping now. Thirteen-x a year means it probably pencils out within a product cycle or two. I said a version of this in [Episode 15](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/), after seeing a custom chip run a small model at 17,000 tokens a second: if you're building today, build for a world where model throughput isn't the issue.

2. **Get on the cost frontier on purpose.** Epoch's biggest caveat is your biggest opportunity: nobody switches models often enough to capture the full decline. Route by task. Re-run your evals every time a cheaper model ships. Rahul's rule from Episode 29 is a good default: try the job on the cheapest model first and only climb when it fails.

3. **Expect your scaffolding to expire.** Cheap, smarter models make yesterday's careful workarounds a liability. In Episode 13 I called this the bitter lesson of AI tooling: once the agent is smart enough, the extra scaffolding gets in its way. The practical version from Episode 41 is to prune your skills and CLAUDE.md files on a schedule (I wrote more about that in [CLAUDE.md best practices](/blog/claude-md-best-practices/)).

4. **Take on the right kind of debt.** Rahul's Episode 14 point: if inference gets cheaper every quarter, AI-fixable tech debt gets cheaper to pay down later. He called it "the United States approach to debt applied to software." Dan's caveat is the important half: only take on debt that's cheap to reverse. A messy function is fine to leave for later. A messy database migration is not.

5. **Invest in the skills with no answer key.** Verification, direction, taste, and judgment about what's worth building are the new constraint. If your job is mostly turning well-specified tickets into code, I'd treat that as the part of the work on the steep side of the price curve. For the longer version of this argument, see our living guide on [how software engineers should adapt to AI](/topics/ai-developer-careers/).

The hosts disagree about how fast this all happens, and I'm still torn myself. But I think the direction is about as settled as anything in this field gets. A resource that gets 13 times cheaper every year doesn't stay a line item for long. It becomes plumbing. The developers who do well will be the ones who stopped asking what the tokens cost and started asking what's still worth a human's attention.

Gen Z, it turns out, was right to forget the math and focus on the rizz.
