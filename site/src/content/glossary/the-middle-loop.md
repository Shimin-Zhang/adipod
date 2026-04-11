---
term: "The Middle Loop"
definition: "The emerging developer workflow layer concerned with overseeing and orchestrating AI agent work -- situated between the inner loop of writing code and the outer loop of product-level planning."
slug: "the-middle-loop"
episodes: ["15"]
aliases: ["middle loop"]
---

## Context

The term comes from the [ThoughtWorks Future of Software Engineering retreat](https://www.thoughtworks.com/content/dam/thoughtworks/documents/report/tw_future%20_of_software_development_retreat_%20key_takeaways.pdf), a gathering that included original Agile Manifesto signers reflecting on how AI agents are reshaping software development. It was discussed on [Episode 15](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age) of the ADI Pod.

Software engineering has long been described in terms of two loops. The **inner loop** is the tight cycle a developer works in while writing code: edit, compile, test, debug. The **outer loop** covers the broader product lifecycle: planning, release, deploy, measure. The middle loop names a workflow layer that did not meaningfully exist before AI coding agents: the work of directing, reviewing, and course-correcting autonomous agents as they operate within the inner loop on the developer's behalf.

## Why It Matters

As agents take on more of the inner loop -- generating code, running tests, fixing errors -- a new category of developer labor emerges that is neither writing code nor managing a product backlog. Someone has to define the spec the agent works against, decide when its output is good enough, catch the failure modes it cannot see, and manage the cognitive overhead of code they did not write. That is the middle loop. Steven Sinofsky's [Jevons paradox argument](https://hardcoresoftware.learningbyshipping.com/p/238-death-of-software-nah) reinforces why this layer grows: making code cheaper to produce increases demand for software, which means more agent output to oversee, not less total developer work.

The ThoughtWorks retreat identified several adjacent concerns that cluster around this layer: spec-driven development as a replacement for verbal instructions, risk tiering to decide which agent output needs human review and which can ship, and the loss of mentoring that happens when code review shifts from human-to-human to human-to-agent. The middle loop is where these problems converge.

Without naming it, teams default to treating agent oversight as an afterthought -- a quick glance at a diff before merging. The concept argues that this layer deserves its own practices, tooling, and skills, just as the inner and outer loops each developed theirs. Chris Roth's [blueprint for elite AI engineering culture](https://www.cjroth.com/blog/2026-02-18-building-an-elite-engineering-culture) explores what those practices look like in high-performing teams.

## Related Concepts

- [Verification debt](/glossary/verification-debt) -- the cost that accumulates when the middle loop is performed poorly or skipped entirely
- [Cognitive debt](/glossary/cognitive-debt) -- the broader risk of code that no developer holds a mental model of, a natural byproduct of delegating the inner loop to agents
