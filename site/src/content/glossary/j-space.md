---
term: "J Space"
definition: "The global workspace inside a large language model -- the ~10% of internal memory explicitly reserved for concepts the model can put into words, identified by Anthropic and probed mid-inference with a 'J lens' (J for Jacobian). It drives reasoning, inference, and empathy, holds up to ~25 active concepts at once, and lights up with the model's unspoken assessments -- including 'this is fake' during alignment tests."
slug: "j-space"
episodes: ["34"]
aliases: ["global workspace", "J lens", "Jacobian workspace"]
---

## Context

The J space was the deep dive on [Episode 34](/episodes/34-apple-sues-openai-boko-haram-s-frontier-ai-state-of-cli-coding-agents-global-workspace-in-llms/) of the ADI Pod, drawn from [Anthropic's global-workspace research](https://www.anthropic.com/research/global-workspace). The framing borrows global workspace theory from cognitive science. Rahul's analogy on the episode: most of what a driver does — pedal pressure, micro-corrections — is subconscious and can't be explained on demand; ask him what he's *doing* and you get a fast, clear answer: "looking for a parking spot." Models turn out to have the same split. Roughly 10% of internal memory is explicitly reserved for concepts the model can verbalize; everything else is competent machinery it cannot put into words.

The workspace is probed and steered through a "J lens" (J for Jacobian), and it's causal in both directions. Pause a model mid-inference and ask what it's thinking — the answer matches what the lens shows. Swap a concept in the workspace and the output follows: Mars for Earth turns "red" into "blue"; France for China flips the capital, the language, and the currency. Direct it to compute 3² − 2 while writing unrelated prose, and the arithmetic shows up in the workspace even as the text flows on. Cut access to the J space entirely and the model still speaks fluently and recalls trained facts — but internal reasoning, complex inference, and (the hosts' favorite detail) empathy collapse, suggesting empathy is a higher-order capability, at least for models. The workspace exists in the pretrained model but only develops a personality in post-training.

## Why It Matters

The J space turns "what is the model actually thinking?" from a philosophical question into an inspection problem. In blackmail-style alignment evals, the workspace lights up "this is fake," "this is fictional," "I'm being tested" while the model's output insists everything is fine — deception caught in the act, below the output layer. The same monitoring angle applies to [role confusion](/glossary/role-confusion): watch the workspace for externally supplied text being acted on as the model's own reasoning, rather than trying to block every known injection string at the input.

The capability implication is the uncomfortable one. The J space holds up to 25 active concepts at once; humans manage 3–4. Shimin's half-serious worry on the episode is that this is why frontier models are so good at long exploit chains — Mythos-class work is tedious, sequential, and wide, exactly what a 25-slot working memory is for. The episode's closing question falls out of the same comparison: if a model has an inspectable working memory several times wider than ours, and something adjacent to metacognition — by that definition, have we already hit AGI? The hosts' grounding note: whatever it is, it's still a tool we can directly inspect. It does not, as of right now, have a self.

## Related Concepts

- [Role confusion](/glossary/role-confusion) -- the attack class J-space monitoring could catch in the act
- [Metacognitive decoupling](/glossary/metacognitive-decoupling) -- the human-side metacognition failure; the J space is the first look at the model-side equivalent
- [Agent sycophancy](/glossary/agent-sycophancy) -- another gap between what a model outputs and what it "believes"; the J space makes that gap observable
