---
term: "Steel Threads"
definition: "A development approach where you build one thin, end-to-end vertical slice of a system first — a single working path from UI to data layer — then weave additional slices alongside it, instead of laying complete horizontal layers. Also called vertical slices or tracer bullets; the counter-pattern to AI agents' default 3D-printer layering."
slug: "steel-threads"
episodes: ["36"]
aliases: ["steel thread", "vertical slices", "tracer bullet", "tracer bullets"]
---

## Context

Steel threads entered the show's vocabulary in [Episode 36](/episodes/36-pacing-the-frontier-anthropic-models-go-rogue-why-software-factories-fail-math-in-the-age-of-ai/) via Dex of HumanLayer's ["Why Software Factories Fail"](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md). His observation: ask a coding agent for a CRUD feature and it paints horizontal layers like a 3D printer — database migration, then domain logic, then the API, then the frontend, each layer laid across the whole feature at once. Human engineers never worked that way in the pre-AI software factory: they get one tiny end-to-end piece working (a steel thread), then extrapolate to the next slice, weaving the threads into an application. Shimin traced the same idea to the "tracer bullet" approach in Steve Yegge and Gene Kim's AI engineering book — and it's older than that; The Pragmatic Programmer named tracer bullets in 1999.

## Why It Matters

The reason to constrain an agent to one steel thread is steering leverage. When the agent lays down a full horizontal layer and the approach is wrong, your correction arrives after the whole layer exists — you're arguing with a finished floor. When it builds one thin vertical slice, your feedback lands early and propagates to every subsequent slice. Dex's companion practice is program design — interface pseudocode and call-stack diffs, one level below system architecture — so the consistency an agent can't learn from its two-line RL training examples is specified before the loop runs, not discovered after it. The hosts' addendum: these artifacts do double duty as the human-comprehension layer — the thing you actually read now that, [per the same episode's Seattle Tech Week survey](/episodes/36-pacing-the-frontier-anthropic-models-go-rogue-why-software-factories-fail-math-in-the-age-of-ai/), almost nobody reads the PRs line by line.

## Related Concepts

- [Loop engineering](/glossary/loop-engineering) -- the harness discipline steel threads slot into; the slice is what the loop should be pointed at
- [Cognitive debt](/glossary/cognitive-debt) -- what horizontal layering accumulates when no human can follow the layers
- [The middle loop](/glossary/the-middle-loop) -- steering the agent is middle-loop work; steel threads are how you keep the steering leverage
