---
term: "Token-Maxing"
definition: "The practice of measuring or incentivizing AI-era engineering productivity by raw token consumption -- leaderboards, spend targets, and tokens-per-PR ratios -- on the assumption that more tokens burned means more value produced."
slug: "token-maxing"
episodes: ["32"]
aliases: ["token maxing", "tokens per PR", "token leaderboards"]
---

## Context

Token-maxing had a short life as a management fad: companies ran internal leaderboards ranking engineers by AI spend, and token budgets started showing up in compensation conversations. By [Episode 32](/episodes/32-glm-5-2-undercuts-opus-self-rewriting-harness-ai-out-persuades-humans-prompt-injection-as-role-confusion/), the hosts' read was that the fad had already died — "token maxing is out, token efficiency is in" framed the whole episode, from GLM 5.2's cost-per-build economics to Dan's closing rant — but its successor repeats the same mistake at one remove: comparing token spend to pull requests opened or lines of AI-written code accepted.

Dan's rant traced the lineage directly: this is the lines-of-code fallacy with a new denominator. Engineering managers spent decades failing to reduce keyboard output to business impact — lines of code, PR counts, commit velocity — and tokens-per-PR inherits every one of those failure modes plus a new one: it penalizes exactly the work agents are best at.

## Why It Matters

The counterexample from the episode kills the metric cleanly. Dan's boss asked him a set of heavy technical questions; answering them properly required building a large amount of throwaway code. He pointed an LLM at it, burned an enormous number of tokens in 45 minutes on work that would have taken him a week by hand, explored three primary approaches, found the flaws in each — and threw all of the code away. Zero pull requests. The output was a recommendations document: human judgment applied to LLM output, which is supposedly what engineers are still paid for. On a tokens-per-PR leaderboard, the most valuable work of the project scores zero.

The deeper point is the one that predates AI: a 10x engineer was never the one who typed ten times the code — it's the one who finds the approach ten 1x engineers wouldn't. Metrics that count output artifacts (lines, PRs, now tokens) systematically misprice the exploration, verification, and thrown-away prototypes where that judgment actually gets exercised. Token spend is a cost to account for, not a proxy for value in either direction.

## Related Concepts

- [Verification debt](/glossary/verification-debt) -- what accumulates when the incentive is to push tokens through rather than to verify what they produced
- [Cognitive debt](/glossary/cognitive-debt) -- the comprehension gap that token-volume incentives widen
- [Dark flow](/glossary/dark-flow) -- the felt-productivity trap; token-maxing is the same illusion institutionalized as a metric
