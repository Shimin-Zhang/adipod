---
title: "Hallucination Neurons: What Happens When You Try to Turn Off LLM Lying"
description: "Researchers found specific neurons that activate when LLMs hallucinate. Suppressing them reduces false claims by up to 40%, but the tradeoffs reveal something deeper about how these models work."
date: "2026-04-11"
slug: "hallucination-neurons-llm"
keywords: "hallucination neurons LLM, LLM hallucination fix, H-neurons paper, AI hallucination research"
episodes: ["7"]
---

Only 0.1% of the neurons in a large language model are associated with hallucination. That is the headline finding from a [Tsinghua University paper](https://arxiv.org/pdf/2512.01797) published in December 2025. While 0.1% sounds trivial, in a model with billions of parameters, you are still talking about millions of neurons. The researchers called them H-neurons. What they found about where these neurons come from, and what happens when you suppress them, is more instructive than the number itself.

The paper, titled "H-Neurons: On the Existence, Impact, and Origin of Hallucination-Associated Neurons in LLMs," did something deceptively simple. They fed open-weight models a set of factual questions, separated the answers into correct and hallucinated, and then compared the neural activation patterns between the two groups. A small cluster of neurons lit up consistently during hallucinated responses and stayed relatively quiet during correct ones. That is the H-neuron population: a sparse, identifiable set of neurons that the model activates when it is generating information it does not actually have grounding for.

The natural question is: what makes these neurons special? Are they the model's imagination circuit? Its lying module? The answer the researchers found is less dramatic and more interesting. The H-neurons showed a high correlation with overcompliance (the model's tendency to answer your question even when it does not know the answer). Think less "deception" and more "over-eager student who would rather guess than say I don't know."

## Where Hallucination Neurons Come From

Here is where it gets counterintuitive. The obvious hypothesis is that H-neurons are an artifact of RLHF (reinforcement learning from human feedback), the fine-tuning stage where models are trained to be helpful, harmless, and honest. You teach a model to always be helpful, it overindexes on helpfulness, and hallucination is the side effect. Reasonable theory. Clean causal story. Wrong, apparently.

The Tsinghua team found that H-neurons were already present after pre-training, before any fine-tuning took place. The overcompliance was baked in from the start. Their explanation: during pre-training, the model is trained on a next-token-prediction objective across trillions of tokens. It learns to always complete the sequence, to always produce the next word, regardless of whether it has sufficient information to do so. In contexts where the training data was ambiguous, contradictory, or simply absent, certain neurons specialized in generating plausible-sounding continuations without factual grounding.

When [we discussed this on ADI Pod](/episodes/7-project-vend-update-hallucinating-neurons-and-year-end-reflections/), I found this explanation somewhat unsatisfying, even if it is probably directionally correct. Pre-training on next-token prediction does not inherently require fabrication. A model could, in principle, learn to express uncertainty. But the training objective does not reward uncertainty. It rewards fluent continuation. So the neurons that learned to generate confident-sounding text in the absence of knowledge were reinforced, not pruned. Rather than a bug introduced by fine-tuning, the H-neurons are a feature of the pre-training objective that fine-tuning fails to fully correct.

This connects to earlier work from Anthropic on what they informally described as [intrusive thoughts in language models](https://www.anthropic.com/research), experiments where perturbing certain neurons caused models to express something like involuntary ideation. The H-neuron finding is a more rigorous version of the same insight: specific, locatable neural populations are responsible for specific behavioral patterns, and those patterns are not uniformly distributed across the network. The model hallucinates with a tiny, identifiable sliver of its network, not with its whole brain.

## Can You Turn Off LLM Hallucination by Suppressing H-Neurons?

Once you have identified the H-neurons, the obvious next step is to turn them down and see what happens. The researchers did exactly that, reducing the activation of H-neurons during inference. The results were encouraging, up to a point.

Suppressing H-neuron activation reduced hallucination rates meaningfully. The paper reports reductions that, depending on the model and task, ranged up to roughly 40%. That is not nothing. For applications where factual accuracy matters (and that is most production applications), a 40% reduction in hallucinated outputs would be significant. It also came with a side benefit: reduced overcompliance meant the models became harder to jailbreak, because the same neurons that made the model eager to answer every question also made it susceptible to adversarial prompting that exploited that eagerness.

But the tradeoff was real, and this is the part that matters for practitioners. Suppressing H-neurons made the models less compliant overall, and not merely less overcompliant. Less compliant, period. The model became more likely to refuse questions it could have answered, more likely to hedge when directness was appropriate, more conservative in its outputs across the board. What you are doing is turning down a dial that controls a spectrum from "refuses to answer anything" to "answers everything, including things it made up," and there is no surgical removal of hallucination on offer. The dial does not have a notch labeled "answers correctly and only correctly."

This tradeoff is a version of a problem that shows up everywhere in machine learning: precision versus recall, false positives versus false negatives, sensitivity versus specificity. Reducing hallucination is reducing false positives (the model claiming something that is not true). But the mechanism also increases false negatives (the model declining to answer things it actually knows). For a chatbot, slightly more refusals might be acceptable. For an agentic coding tool, a model that second-guesses itself constantly is going to be less useful in practice.

## What This Means for Developers

If you are building applications on top of LLMs, the H-neuron paper offers three practical insights.

**First, hallucination is structural, not incidental.** It emerges from the fundamental training objective (always produce the next token) and it is encoded in identifiable neural pathways. This means bigger models or better data alone will not make it go away, because the training objective itself produces the behavior. Until that objective changes, or until inference-time interventions become standard, hallucination will remain a baseline property of autoregressive language models.

**Second, the fix is not free.** Every technique that reduces hallucination, whether it is H-neuron suppression, retrieval-augmented generation, chain-of-thought prompting, or constitutional AI, comes with a corresponding cost in capability, latency, or compliance. There is no costless solution to hallucination because the mechanism that produces hallucination is entangled with the mechanism that produces useful output. When my co-host Dan Lasky suggested adding a "certainty token" to the training data (a special token the model could output to signal low confidence), it captured the right intuition: the model needs a way to bail out gracefully. But that mechanism has to be trained in, and the current training paradigm does not naturally produce it.

**Third, the right response is verification, not trust.** The H-neuron finding reinforces what should already be standard practice: do not treat LLM output as ground truth. The neurons responsible for hallucination are active from pre-training onward. They are part of the model's basic architecture for handling uncertainty. Every time you consume LLM output without verification, whether it is a factual claim in a generated article or a function call in generated code, you are accumulating what amounts to [verification debt](/glossary/verification-debt/). The debt does not announce itself. It surfaces when a hallucinated API call hits production, when a [generated function introduces a logic error](/blog/ai-code-quality-bugs/) that nobody caught because the code looked plausible, or when a confident-sounding factual claim turns out to be fabricated.

## How Mechanistic Interpretability Could Fix Hallucination

The H-neuron paper is part of a broader wave of mechanistic interpretability research, the subfield that tries to understand what individual neurons and circuits inside neural networks actually do. This is important context because it suggests a future where hallucination mitigation goes beyond prompt engineering or fine-tuning to become an architecture-level intervention.

Today, the state of the art for reducing hallucination in production is layered defense: RAG to ground the model in retrieved facts, chain-of-thought to make the reasoning visible, output validation to catch obvious errors, and human review to catch the rest. These are all external interventions that work around the model's tendency to hallucinate rather than addressing it at the source.

Mechanistic interpretability offers, at least in theory, the possibility of internal intervention: modifying the model's behavior by directly adjusting the neural circuits responsible for specific failure modes. The H-neuron paper is an early proof of concept. It demonstrated that you can identify the relevant neurons, suppress them, and get measurable improvement. The tradeoff between hallucination reduction and general compliance is a real engineering constraint, not merely a theoretical objection.

Whether this becomes a practical tool depends on scaling. The Tsinghua team worked with relatively small open-weight models. Identifying H-neurons in models with hundreds of billions of parameters, let alone mixture-of-experts architectures where different experts activate for different inputs, is a substantially harder problem. And even if you identify them, the suppression tradeoff means you need fine-grained control, not a binary switch. The dial needs more notches.

## Why LLM Hallucination Cannot Be Fully Eliminated

The deepest takeaway from the H-neuron research concerns the nature of the problem itself, beyond any specific technique for reducing hallucination.

Hallucination is a failure of routing, not knowledge. The models often "know" the correct answer somewhere in their weights. What breaks down is the mechanism that decides between generating from knowledge and generating from pattern completion. The H-neurons are the circuit that tips the balance toward pattern completion: produce something fluent, even if it is not grounded. That circuit exists because the training process rewards fluency unconditionally. The model that always produces a confident next token gets a lower loss than the model that hesitates.

This means that hallucination and fluency share infrastructure. You cannot fully remove one without degrading the other, at least with current architectures. The more promising path is making hallucination legible rather than trying to eliminate it: building systems where you can detect when the model is in a low-confidence state and route accordingly. The H-neuron research suggests that the internal signals for this detection exist. The engineering challenge is extracting them reliably at inference time without tanking performance.

For now, the practical stance has not changed, even if the theoretical understanding has sharpened. Build your systems assuming the model will hallucinate. Design your verification layers to catch it. Allocate your review attention to the areas where hallucinated output would do the most damage. And keep an eye on mechanistic interpretability, because the first team to turn H-neuron suppression into a production-grade inference-time knob will have built something genuinely valuable. The dial exists. We just do not have a good enough grip on it yet.

For more on the [security and reliability implications of LLM failure modes](/topics/ai-security-developers/), the hallucination problem is one piece of a larger puzzle that includes jailbreaking, overcompliance, and the question of whether these models can ever be trusted in adversarial environments. The H-neuron paper does not answer that question. But it does suggest that the answer, when it comes, will be found inside the model, not wrapped around it.
