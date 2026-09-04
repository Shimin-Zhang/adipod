---
term: "Two-Acre Test"
definition: "Shimin Zhang's standby personal benchmark: ask a model what it should do with two (and a half) acres of land in Washington State to make money, then grade the plan's economic and physical groundedness. A probe for real-world reasoning that public leaderboards don't measure — and can't be trained against."
slug: "two-acre-test"
episodes: ["27", "29", "39"]
aliases: ["two and a half acres benchmark", "two acres in Washington", "the acreage benchmark"]
---

## Context

The test first surfaced on air in [Episode 27](/episodes/27-openai-beats-musk-gemini-3-5-flash-and-ai-burnout-mitigation/), already billed as "my usual what-should-I-do-with-two-and-a-half-acres-in-Washington benchmark, my very unscientific one," and reappeared in [Episode 29](/episodes/29-fable-5-mythos-5-launch-meta-ai-hack-llms-as-black-boxes-future-of-agents/) as a launch-day check on Fable 5. By [Episode 39](/episodes/39-metas-ai-backfires-glm-5-3-flash-openais-jalapeno-chip-the-end-of-programming/) it had graduated into a fixture of the show's new Model Review segment: every model under review gets the same plot of land.

The prompt is simple — what should I do with two acres somewhere in Washington to make money? — and the grading is where the benchmark lives. Plans are judged on whether the economics and the physical world check out. The canonical failure mode: models proposing agricultural side hustles priced as if farm labor paid $50 an hour.

## Why it matters

Public benchmarks are saturated and, worse, trainable-against — a lab can tune for MMLU; it cannot tune for a plot of land in Washington State. A private, unpublished eval with a fixed grader (Shimin) gives the show a consistent yardstick across model generations, and the question's open-endedness surfaces exactly the failure the leaderboards hide: fluent, confident plans that dissolve on contact with prices, seasons, zoning, and labor. It's the Model Review counterweight to spec-style capability claims — less "can it code" and more "does it know how the world works."

## Example

In [Episode 39](/episodes/39-metas-ai-backfires-glm-5-3-flash-openais-jalapeno-chip-the-end-of-programming/)'s review of ZAI's GLM 5.3 Flash, the model scored "middling, maybe sub-Sonnet" on the two-acre test — while acing the companion nth-order-effects test, chaining from "you can't sue an agent" to agent-liability insurance to legal systems formalizing that insurance. Shimin also put the same two acres to his self-hosted DeepSeek for comparison. One plot of land, a growing panel of models.
