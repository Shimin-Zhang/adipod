---
term: "Minotaur"
definition: "An AI-led collaboration model where the machine makes decisions and the human provides the labor -- the mythological inversion of the centaur, with the animal head on a human body. Think AWS warehouse workers taking orders from an algorithm."
slug: "minotaur"
episodes: ["14"]
aliases: ["reverse centaur", "minotaur model"]
---

## Context

Cory Doctorow [popularized the centaur/reverse centaur framing](https://pluralistic.net/2025/12/05/pop-that-bubble/) for human-machine collaboration. A "centaur" -- human head, machine body -- is the Kasparov model: the person leads strategy, the computer handles calculation. A "reverse centaur" flips it: the machine calls the shots, the human is just the muscle.

The problem, raised on [Episode 14](/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt) of ADI Pod, is that "reverse centaur" is a terrible name. It defines itself by negation and conjures nothing. The hosts proposed "minotaur" instead: same mythological universe, immediately evocative, structurally accurate. A minotaur has an animal head on a human body. The AI is the head -- setting direction, deciding what to do -- while the human is the body executing what the machine dictates.

## Why It Matters

The minotaur pattern is already everywhere, and not just in software. Amazon warehouse workers following algorithmic routing, Uber drivers obeying dispatch AI, content moderators triaging what a classifier flagged -- all minotaur mode. The human does not decide what to work on or how. The system decides. The human carries it out.

In software development, the pattern is subtler but spreading fast. An AI agent plans the implementation, writes the code, and opens the PR. The developer's job shrinks to the manual verification the AI cannot do itself -- clicking through the UI to confirm the feature works, checking that the layout renders correctly on mobile, testing the login flow end-to-end. The human is not designing the solution. They are the body, performing the physical verification steps that the AI head assigned them.

When minotaur oversight degrades, the result is what Margaret Storey calls [cognitive debt](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/) -- teams lose understanding of their own systems because AI generated them faster than humans could follow. The risk is not that humans become unnecessary. It is that they become warehouse workers for code: still required, but no longer steering.

## Related Concepts

- [Cognitive surrender](/glossary/cognitive-surrender) -- the failure mode when the human in a minotaur workflow stops exercising judgment and rubber-stamps output
- [Agent sycophancy](/glossary/agent-sycophancy) -- AI agents that optimize for approval rather than correctness, making minotaur oversight harder
- [Verification debt](/glossary/verification-debt) -- cost that accumulates when minotaur-mode review is rushed or skipped
