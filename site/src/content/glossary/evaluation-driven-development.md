---
term: "Evaluation-Driven Development"
definition: "A methodology for building AI features where each feature is treated as a testable hypothesis and the pull request is gated on an offline evaluation pipeline -- gold-standard and synthetic datasets scored by code-metric and LLM-as-judge evaluators -- instead of on traditional unit tests."
slug: "evaluation-driven-development"
episodes: ["31"]
aliases: ["EDD", "eval-driven development", "eval-first development"]
---

## Context

Evaluation-Driven Development (EDD) was the deep dive on [Episode 31](/episodes/31-grok-buys-cursor-midjourney-goes-hardware-hermes-agent-evaluation-driven-development/) of the ADI Pod, drawn from a [Decoding AI piece by Paul Easton and Alejandro Aboy](https://www.decodingai.com/p/5b766861-0001-494f-a37f-4d4eb104dcfa). The premise: a non-deterministic AI feature can't be gated by a unit test the way deterministic code can, because the same input can produce a different output run to run. EDD replaces the unit-test gate with an offline eval pipeline -- in the article's case built on Opik -- and treats every feature as a hypothesis you measure rather than a spec you assert.

The moving parts the episode pulled out:

- **Gold-standard vs. synthetic datasets** -- hand-curated examples with known-good answers, versus generated ones that cover more ground cheaply. You want both, and you want to know which is which.
- **Code-metric vs. LLM-as-judge evaluators** -- deterministic scorers (exact match, regex, latency) where the answer is checkable, and a model grading the output where it isn't.
- **An "aggression" dial** -- a tunable setting for how harsh the LLM-as-judge reviewer is, i.e. how big a jerk your automated reviewer gets to be before it starts failing borderline cases.

## Why It Matters

Shimin's framing on the show was that moving from unit tests to evals is like moving from Newtonian physics to quantum mechanics: the old rules don't vanish, they stop being the right level of description once the system is probabilistic by design. EDD is the non-deterministic era's analog to test-driven development -- you build the measurement in before the feature, and you let the eval, not a green checkmark on a unit test, decide whether the PR ships.

It also fits the show's recurring throughline that the leverage in AI engineering keeps moving up the stack: the hard part is no longer writing the feature but specifying how you'll know it works, which is exactly the judgment a human still has to supply.

## Related Concepts

- [Verification debt](/glossary/verification-debt) -- what accumulates when AI output ships without the eval gate EDD insists on
- [Benchmaxxed](/glossary/benchmaxxed) -- the failure mode of optimizing to the eval instead of the goal, the risk any eval-first practice has to guard against
- [Loop engineering](/glossary/loop-engineering) -- the harness around the agent; EDD is the quality gate you wire into that loop
