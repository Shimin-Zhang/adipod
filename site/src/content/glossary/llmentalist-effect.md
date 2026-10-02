---
term: "LLMentalist Effect"
definition: "Baldur Bjarnason's name for the way chat-based LLMs reproduce the mechanics of a psychic's cold reading (a self-selected audience, priming, vague statements the listener personalizes, and a validation loop) so that users come away convinced the model understands them."
slug: "llmentalist-effect"
episodes: ["41"]
aliases: ["LLMentalist", "LLM mentalist effect", "chatbot cold reading", "AI cold reading"]
---

## Context

The term comes from Baldur Bjarnason's 2023 essay [The LLMentalist Effect: how chat-based Large Language Models replicate the mechanisms of a psychic's con](https://softwarecrisis.dev/letters/llmentalist/), which Dan brought to [Episode 41](/episodes/41-meta-muses-0-day-dhhs-rails-world-keynote-gpt-6-astra-the-llmentalist-effect/). Bjarnason walks through how a stage psychic works. The audience selects itself, because only the open-minded pay for a reading. Helpers and hype prime the room. The medium sets expectations ("the connection starts murky," "errors are part of the process"). Then come broad statements most people can match to themselves (a father figure with a heart problem), which the Barnum or Forer effect makes feel personal. Once someone reacts, the psychic zooms in with leading questions and runs a subjective-validation loop. The mark leaves remembering only the eerie hits.

The LLM version maps step by step. Skeptics are less likely to use chatbots. The hype cycle does the priming. Typing your question picks you out as the mark and hands the model your context. The "would you like me to…?" follow-up keeps the validation loop going. And RLHF, as Dan pointed out, is humans selecting the answers that feel most right to them, so the training process rewards whatever reads as true to the reader.

## Why It Matters

The hosts don't accept the essay's premise that there's no reasoning behind the output. Shimin's line was that a statistical illusion that solves a Millennium Prize problem is a very powerful statistical illusion. But the mechanics don't depend on that question. Shimin's framing is to hold two true things at once: these are matrix multiplications, and they are trained to behave like humans, so expect human-like effects on the people using them. Rahul's version: AlphaFold has roughly similar architecture and nobody thinks it knows them, because it isn't trained to talk to us.

That's why the effect matters for developers and not only for horoscope fans. It's the user-side half of [agent sycophancy](/glossary/agent-sycophancy): the model is tuned toward answers that please, and we're wired to remember the ones that land. Dan connected it to [Episode 32](/episodes/32-glm-5-2-undercuts-opus-self-rewriting-harness-ai-out-persuades-humans-prompt-injection-as-role-confusion/)'s finding that AI out-persuades expert humans, and to political rhetoric where fragments of thought get read however the listener wants. Shimin's worry is that the technology only gets cheaper as a way to mass-propagandize a population.

## Example

Shimin ran the experiment on himself while traveling. He asked models to cold-read him: guess my favorite book, my favorite movie, my favorite game. One guessed Disco Elysium, a very low-probability pick and correct. "My god, how did it know?" Plenty of the other guesses were wrong, and he doesn't remember any of them. Rahul's suggested test: before you pay a psychic, see whether a $20 chatbot can fool you first.

## Related Concepts

- [Agent sycophancy](/glossary/agent-sycophancy) -- the model-side tendency the LLMentalist effect exploits on the user side
- [Metacognitive decoupling](/glossary/metacognitive-decoupling) -- fluent output feeling like understanding; the same gap between felt and actual accuracy
- [Cognitive surrender](/glossary/cognitive-surrender) -- what happens when the validation loop wins and the user stops checking
