---
term: "Superposition"
definition: "The hypothesis that a neural network represents more features than it has neurons by packing them into overlapping directions. It is the standard explanation for polysemantic neurons, which fire for unrelated concepts, and the reason interpretability researchers decompose activations with sparse autoencoders. In October 2026, Goodfire's Nick Cammarata argued that most apparent polysemanticity has ordinary causes and that superposition should be the last explanation, not the first."
slug: "superposition"
episodes: ["44"]
aliases: ["superposition hypothesis", "polysemanticity", "polysemantic neurons"]
---

## Context

Superposition was the setup for the deep dive on [Episode 44](/episodes/44-how-anthropic-works-in-2026-the-most-important-mech-interp-paper-of-the-year/). The story starts with a confusing neuron. Distill's 2020 ["Zoom In"](https://distill.pub/2020/circuits/zoom-in/), co-written by Nick Cammarata, found that neuron 4e:55 in the vision model InceptionV1 responds to cat faces, fronts of cars, and cat legs. A neuron like that is polysemantic: one unit, several unrelated meanings. (The hosts' theory that it was really a "boots and cats" neuron remains unreviewed.)

Anthropic's 2022 ["Toy Models of Superposition"](https://transformer-circuits.pub/2022/toy_model/index.html) offered the explanation. In small networks trained on sparse synthetic features, models represented "more features than they have dimensions," compressing them into overlapping directions at the cost of interference. The paper's hypothesis was that real networks are "noisily simulating larger, highly sparse networks." Shimin's version on the episode: GPT-2 small has a 768-dimensional residual stream, and it clearly knows more than 768 things.

If features are smeared across neurons, reading neurons directly is hopeless, so the field turned to sparse autoencoders. An SAE projects a model's activations into a much larger space and looks for clean features there. Anthropic's largest, on Claude 3 Sonnet, had about 34 million features, and one of them became [Golden Gate Claude](https://www.anthropic.com/research/golden-gate-claude) when it was clamped to 10x its maximum activation. As Shimin admitted on air, he spent a long time thinking Golden Gate was a neuron. It was an SAE feature, a combination of neurons.

## The Challenge

Cammarata's 2026 essay, ["Neural Networks Are Already Clean"](https://already-clean.goodfire.com/), argues the field reached for superposition too early. His list of reasons a neuron can look polysemantic, which he calls "Superposition of the Gaps," puts superposition last. Bad tools, bad explanations, bad learning (architecture and data), and recursive generalization come first. Some of the evidence: with modern architectural fixes, 99–100% of neurons in InceptionV1's last layer become easy to interpret. A frontier-model neuron that fires on "pr," on Base64 strings, and on Bengali turns out to mean "pr" in all three once you decode them. One neuron that detected "iy" grew over training to detect "diy," then "do it yourself." In a preliminary audit of Qwen3-32B, about 90% of neuron poles have one main job. He calls it a working hypothesis and doesn't claim every neuron is clean. A technical companion paper is promised, and Shimin's read is that the reception so far is mixed.

## Why It Matters

If most neurons are readable, you can trace a concept through a model neuron by neuron instead of decomposing everything first. The essay walks a "Miyazaki" circuit layer by layer through Qwen3-32B. That makes steering and auditing cheaper. On the episode, Shimin demoed steering on [Neuronpedia](https://www.neuronpedia.org/), where a "cat mode" preset turns Gemma 2 9B's suggestion for a podcast mascot into a cat. He'd like the same tools to trace where a model decided to do something bad anyway, or to tune down sycophancy. Dan's interest is architectural: looking under the hood beats trying an idea and checking whether the output got worse.

## Related Concepts

- [J Space](/glossary/j-space/) -- another case of interpretability turning "what is the model thinking?" into something you can inspect
- [Hallucination neurons](/blog/hallucination-neurons-llm/) -- what becomes possible when a single failure mode maps to identifiable neurons
