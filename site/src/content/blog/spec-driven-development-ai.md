---
title: "Spec-Driven Development: Why Writing Specs Matters More When AI Writes the Code"
description: "If AI generates code from prompts, the spec is the product. Here is how spec-driven development works, why it matters more than ever, and what a good spec actually looks like."
date: "2026-04-11"
slug: "spec-driven-development-ai"
keywords: "spec-driven development, spec-driven development AI, verified spec-driven development, VSDD"
episodes: ["5", "15", "16"]
---

The shift happened so gradually that most developers missed it. You used to be the person who wrote the code. Now you are increasingly the person who describes the code you want an agent to write. And if the description is vague, the code will be too — except it will compile, pass superficial tests, and look plausible enough that you merge it anyway. The bottleneck has not disappeared. It has moved upstream, from implementation to specification.

Spec-driven development is the idea that you write a detailed specification before asking an AI agent to implement anything. It is not new — anyone who has written a design document before opening an IDE has done a version of it. What is new is that the quality of your spec now determines the quality of your output with a directness that did not exist when you were the one translating intent into code. When you write the code yourself, a vague spec produces a slow start — you figure it out as you go. When an agent writes the code, a vague spec produces a confident, plausible, subtly wrong implementation that you may not catch until it is in production.

This is the argument I keep returning to across [several episodes of ADI Pod](/episodes/5-how-anthropic-engineers-use-ai-spec-driven-development-and-llm-psychological-profiles/): as the landscape of [AI coding agents](/topics/ai-coding-agents-compared/) matures, spec-driven development is not an optional productivity hack. It is the core engineering discipline.

## A Taxonomy of Spec-Driven Development

[Birgitta Bockeler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html), a distinguished engineer at ThoughtWorks, published a taxonomy of spec-driven development approaches that we [covered on episode 5](/episodes/5-how-anthropic-engineers-use-ai-spec-driven-development-and-llm-psychological-profiles/) and that I have been thinking about ever since. She identified three levels, each representing a deeper commitment to the spec as a first-class artifact.

**Spec-first** is the most familiar: write a well-considered specification, then use an AI-assisted workflow to build to that spec. You open a markdown file, describe the feature — inputs, outputs, edge cases, constraints — and hand it to your agent. The spec guides the initial implementation but does not persist as a maintained artifact. Once the code works, the spec is often abandoned.

**Spec-anchored** development keeps the spec alive after the task is complete. The specification is persisted alongside the code and updated as the feature evolves, serving as a living reference for future maintenance and iteration. If you have ever maintained a design doc that actually stayed current with the implementation, you have done spec-anchored development. If you have ever maintained a design doc, period, you know how rare that is.

**Spec-as-source** is the radical end of the spectrum. The spec becomes the primary source file. Humans only edit the specification — never the code. The code is treated like a compiled binary: generated from the spec, disposable, regenerable. A colleague at Dan's company had independently pioneered something close to this approach, and when we discussed it on the show, the concept sounded both thrilling and a little unsettling. If the model does not get it right, you do not fix the code. You fix the spec and regenerate.

Bockeler raised a question about spec-as-source that I think is underappreciated: is it actually easier to review a markdown specification than to review the code it produces? Code is a precise definition of behavior. Natural language is lossy by definition. She drew a parallel to model-driven development, which promised similar benefits in the 2000s and never caught on because it was the wrong level of abstraction for both business stakeholders and engineers. Spec-as-source might have the same problem — or it might succeed where MDD failed because natural language is a more universal interface than UML diagrams ever were.

I am still torn on where the sweet spot is. Spec-first is clearly table stakes at this point. Spec-anchored feels like the right default for durable code. Spec-as-source is probably the future for certain categories of work — disposable internal tools, prototypes, anything where regeneration is cheaper than maintenance — but I would not bet my production system on it yet.

## Where the Rigor Goes

The [ThoughtWorks Future of Software Engineering retreat](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/) — organized on the 25th anniversary of the Agile Manifesto, with original signers in the room — surfaced a question that I think is the most important framing for understanding why specs matter more now: where does the rigor go?

Before agents, the rigor was in the act of writing code. Every character you typed engaged your brain. As my co-host Rahul Yadav put it during [our discussion of the retreat findings](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/): "The rigor was, I'm writing code, every single character that I'm typing, it's like I'm doing it with my own hands. So my brain is also engaged. But if AI takes away that part, the rigor moves to other places."

The retreat participants identified spec-driven development as one of the primary destinations for that displaced rigor. The other was red-green testing — writing failing tests first, then having agents write code until the tests pass. Both approaches share the same underlying logic: if you are not writing the code, you need to be more precise about defining what the code should do. The engineering discipline does not vanish. It migrates to a different artifact.

[Chris Roth](https://www.cjroth.com/blog/2026-02-18-building-an-elite-engineering-culture) reinforced this in his article on building elite AI engineering culture, which Rahul brought to [the same episode](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/). Roth found that spec-driven development was a defining pattern among high-performing teams — "a new pattern that has emerged that wasn't there," as Rahul summarized it. The reasoning is straightforward: agents that receive specs with the why behind the design decisions, not just the what, produce better output. The spec gives the agent context that a bare prompt cannot.

There is an irony here worth naming. The Agile Manifesto famously valued "working software over comprehensive documentation." Twenty-five years later, the retreat convened by its own signers concluded that comprehensive documentation — in the form of specs — is precisely where engineering rigor needs to go in the agentic age. The manifesto was reacting to a world where specs were written for humans to implement. In a world where specs are written for agents to implement, the spec is not bureaucratic overhead. It is the engineering artifact.

## Verified Spec-Driven Development

On [episode 16](/episodes/16-pentagon-anthropic-drama-verified-spec-driven-development-and-interview-with-martin-alderson/), I introduced a methodology called [verified spec-driven development](https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00) (VSDD) by DollSpace-Gay. VSDD takes the spec-first approach and adds adversarial verification gates at each phase — essentially, a convergence test for your spec and your implementation.

The pipeline has four roles: the architect (you), the builder (your AI coding agent), the tracker (a ticket management system), and the adversary (a critique-generating agent).

**Phase one: spec crystallization.** The builder creates a spec, but instead of just describing the feature, the spec must include provable properties, purity boundary maps, and verification tool links. It is more demanding than a typical spec-first document — you are not just saying what the code should do, but what properties the code should provably have.

**Phase two: adversarial spec review.** The adversary — a separate agent, ideally a different model — conducts a critique of the spec. Missing edge cases, underspecified boundaries, ambiguous requirements. You iterate until the adversary is satisfied.

**Phase three: test-first development.** Standard red-green-refactor TDD, but with another adversarial gate. After the tests pass and the code works, the adversary reviews both the tests and the implementation against the spec. If something is not covered, the builder goes back to refactor. If the spec itself was wrong, you go back to phase one.

I tried VSDD on a side project using Claude Code. I had it generate a skill for the VSDD workflow and then apply it as it developed the project. The result: the final product had fewer bugs than it would have if I had used my regular plan-and-implement workflow. There were still bugs — this is not a silver bullet — but the adversarial gates caught issues that I would have missed in a single-pass review.

One detail that surprised me: about 80% of the time, Claude kicked off an Opus agent for the verification gate. But roughly 20-25% of the time, it used Sonnet as the adversary, reasoning that the methodology recommends using a different model for verification. The agent was smart enough to apply the cross-model verification principle on its own. That is a small thing, but it points toward a future where agents can self-organize verification workflows without manual orchestration.

## The CLAUDE.md Connection

There is a version of spec-driven development that most developers are already practicing without calling it that: maintaining a [CLAUDE.md file](/blog/claude-md-best-practices/).

Your CLAUDE.md is a specification. It describes what the project is, how it should be built, what constraints the agent should follow, and what the expected behavior looks like. It is not a feature spec — it is an environmental spec, the equivalent of describing the workshop before describing the furniture you want built. And like any spec, its quality determines the quality of the agent's output.

[Martin Alderson](https://martinalderson.com), who we [interviewed on episode 16](/episodes/16-pentagon-anthropic-drama-verified-spec-driven-development-and-interview-with-martin-alderson/), made a practical recommendation that connects directly to the spec maintenance problem: schedule a task that goes through your repo and updates your CLAUDE.md files. Look at recent commits, flag anything out of date, open a PR. Martin's reasoning was simple — CLAUDE.md files drift out of sync with the codebase, and "that's where a lot of issues start coming." It is the same maintenance burden that kills design docs and feature specs, applied to the most basic specification artifact in your agentic workflow.

Martin also kept his setup deliberately minimal: Claude Code with minimal plugins, custom CLIs wrapping internal APIs for agent access. When I asked about parallel agent workflows, he was skeptical — the coordination overhead often exceeds the productivity gains. Keep it simple, keep your spec files current, give the agent what it needs. The fact that this works better than elaborate multi-agent orchestration says something about where the actual leverage is.

## What a Good Spec Actually Looks Like

Based on the taxonomy from Bockeler, the VSDD framework, the ThoughtWorks retreat findings, and my own experience across projects, here is what I think separates a spec that produces good agent output from one that produces plausible garbage.

**It names the why, not just the what.** "Add a caching layer" is a prompt. "Add a caching layer because the API has a 100ms p95 latency and we need sub-20ms for the autocomplete feature, using Redis with a 5-minute TTL" is a spec. Rahul observed that elite teams include the thinking behind design decisions, giving agents enough context to make reasonable choices when they encounter ambiguity. An agent working from rationale will make different — and better — tradeoff decisions than one working from a feature list.

**It defines boundaries, not just features.** What the code should not do is as important as what it should do. In VSDD, the adversary specifically looks for underspecified boundaries. Every boundary you do not define is a decision you are delegating to the model's training data, and training data does not know your system.

**It includes verification criteria.** How will you know the implementation is correct? If the answer is "I'll review the PR," you do not have a spec — you have a wish. VSDD makes this explicit by requiring provable properties and test specifications upfront. Even outside VSDD, adding a "how to verify" section forces you to think about correctness before the agent starts writing. Same principle as TDD, applied one level up.

**It is appropriately sized.** Not everything warrants a spec. A bug fix where the solution is obvious does not need a crystallized specification with adversarial review gates. Spec-driven development is most valuable for features, architectural changes, and anything where the implementation involves genuine ambiguity. Applying it uniformly is the same mistake as applying any process uniformly — it becomes ritual rather than engineering.

## The Part That Should Worry Us

Here is the counterargument I cannot dismiss. If code is a precise language and natural-language specs are inherently lossy, then spec-driven development might be creating a new category of [verification debt](/glossary/verification-debt/). You verify the spec against intent. You verify the implementation against the spec. But you have introduced an additional translation layer — intent to spec, spec to code — and each translation is a surface for errors that did not exist when intent went directly to code through a human's fingers.

Bockeler named this concern when she asked whether reviewing markdown is actually harder than reviewing code. I think the answer depends on the reviewer. A senior engineer can catch spec-level errors that a junior might miss. But a junior reviewing a spec might pass something that would have been caught if they had been forced to implement it themselves — because implementation is itself a form of verification that spec-driven development removes from the loop.

This is not a reason to abandon spec-driven development. It is a reason to pair it with strong verification practices — adversarial review, red-green testing, the VSDD gates — and to recognize that writing the spec is necessary but not sufficient. The [middle loop](/glossary/the-middle-loop/) of overseeing agents, maintaining specs, and verifying output is where engineering judgment lives now. Dedicating time to it is not overhead. It is the job.

## The Reframing

Software engineers have always written specs. We called them design documents, technical proposals, architecture decision records, even just well-written Jira tickets. What has changed is not the practice but the stakes. When you were the one implementing the spec, a gap in the specification was a gap you filled with your own judgment in real time. When an agent implements the spec, a gap is filled with whatever the model's training data suggests — confidently, silently, and often plausibly enough to survive review. This is the central question facing [developer careers in the AI era](/topics/ai-developer-careers/): not whether you can still write code, but whether you can define what the code should do with enough precision that a machine gets it right.

Spec-driven development in the agentic age is not a new discipline. It is the old discipline of defining what you want before you build it, elevated from a best practice to a load-bearing requirement. The spec is not documentation. The spec is the product. And if you are spending more time writing specs than writing code, that is not a sign that something has gone wrong with your workflow. That is the workflow working as intended.

The Agile Manifesto signers, twenty-five years on, arrived at the same conclusion from the opposite direction. They spent a career fighting against excessive upfront specification. Now they are advocating for it — because the alternative is not "working software" but "plausible software that nobody fully understands." The rigor has to go somewhere. The spec is where it lands.
