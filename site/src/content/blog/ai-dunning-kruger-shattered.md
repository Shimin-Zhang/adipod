---
title: "AI Didn't Steepen the Dunning-Kruger Curve. It Shattered It."
description: "The popular take is that AI puts Dunning-Kruger on steroids. A 2026 paper argues something stranger and worse: AI cuts the wiring between how good your work looks and how good you actually are."
date: "2026-06-22"
slug: "ai-dunning-kruger-shattered"
keywords: "AI Dunning-Kruger, metacognitive decoupling, AI competence vs productivity, AI self-assessment, appearing productive AI, AI skill calibration"
episodes: ["30"]
---

The comforting version of the AI-and-competence story goes like this: AI puts the Dunning-Kruger effect on steroids. Hand a beginner a model that writes confident code, and they feel like a staff engineer while shipping junior mistakes. It's a tidy story, and the tidiest part is that it leaves the famous curve intact: same shape, just steeper.

Christopher Koch's paper ["Beyond the Steeper Curve"](https://arxiv.org/html/2603.29681) argues that "steeper" is the wrong word. The curve doesn't survive contact with AI. It comes apart.

We took the paper as the deep dive on [episode 30](/episodes/30-fable-5-ban-metas-ai-gulag-elias-thorne-loop-engineering/), and it's the rare piece of AI commentary that left me less sure of my own self-assessment instead of more. The claim is precise: the Dunning-Kruger curve only means anything because a few things stay wired together — what you produce, how good you think you are, and how good you actually are. AI cuts those wires. Koch calls the result [metacognitive decoupling](/glossary/metacognitive-decoupling/), and once you see it, most of the "are juniors cooked, are seniors safe" discourse starts to look like it's measuring the wrong quantity.

## What the curve actually measures (and what AI breaks)

The original Dunning-Kruger finding is narrower than the meme that ate it. It isn't "dumb people think they're geniuses." It's a statement about calibration: the gap between your confidence and your competence, and how that gap is largest when you know the least, because you don't yet know enough to see what you're missing. The curve is a picture of a single relationship — self-assessment tracking actual skill, badly at first and better over time.

Koch's move is to take that one relationship and pull it into four separate variables, then ask what AI does to each:

1. **Observable output** — what you hand in. With a model in the loop, this jumps almost immediately. The work looks polished on day one.
2. **Self-assessment** — how good you think you are. We grade ourselves on what we produce, so this rides the output upward.
3. **Actual understanding** — whether you could do it, or explain it, without the model. This barely moves. The AI did the work; you supervised.
4. **Calibration accuracy** — whether your confidence matches your competence. This stagnates, and the more you lean on the tool, the worse it gets.

In an ordinary skill-building loop, those four rise together, roughly in step. That coupling is the whole reason output was ever a usable signal of skill. AI snaps it: variables one and two go up, three and four don't, and nothing in the daily experience of the work tells you that's happening.

The empirical anchor is a study Koch leans on where people worked LSAT-style logic problems with AI help. The good news landed first — scores went up. The bad news was right behind it: everyone overrated their own performance, and the classic curve, where the weakest performers overrate the most, flattened into a roughly uniform line of overconfidence. AI didn't just hand the low performers a false sense of skill. It handed it to the whole room, regardless of where anyone started. On the show I put it less carefully: it didn't destroy the Dunning-Kruger effect, it gave everybody Dunning-Kruger.

## Why this is worse than ordinary overconfidence

We already had a name for half of this. The Wharton paper ["Thinking, Fast, Slow, and Artificial"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6097646) measured a roughly 12-percentage-point bump in user confidence when an AI supplies the answer, whether or not the answer is right. I've written before about that as [cognitive surrender](/glossary/cognitive-surrender/) — accepting output at the speed of System 1.

But a confidence bump is a one-time tax. You can warn people about it, and a sufficiently paranoid engineer can hold the line. Decoupling is dynamic, which is what makes it nastier: calibration doesn't just start low, it erodes. Every session where the work comes out clean and you didn't have to struggle, the gap between what you can do and what you think you can do widens a little more. You are training the wrong model — your own.

And the obvious correction is offline. The tool that produced the work is optimized to be agreeable, so it isn't going to volunteer that you've stopped understanding what it hands you. That's [agent sycophancy](/glossary/agent-sycophancy/) doing exactly what it's incentivized to do: there's no market reward for a model that tells a paying customer they've been coasting.

It's worth separating this from the two failure modes it rhymes with. [Cognitive debt](/glossary/cognitive-debt/) is shipping code you don't understand. Cognitive surrender is trusting a specific wrong output in the moment. Metacognitive decoupling is the layer above both: you've lost the instrument that would have told you either one was happening. My co-host Dan put the failure mode better than the paper's abstract did, riffing on the inflated sense of reach: "I can write my own database engine now. I don't need Postgres, I'm just gonna write dangres." The joke works because you can't always tell when you're the one saying it.

## The organizational version: productivity stops signaling competence

The personal version is uncomfortable. The organizational version is expensive, and it's where I'd spend most of a manager's attention.

For most of working history, output was a serviceable proxy for competence. Show me what you shipped and I can infer, roughly, how good you are — that inference is baked into code review, promotion packets, the whole apparatus. A piece on the blog [No One's Happy](https://nooneshappy.com/article/appearing-productive-in-the-workplace/) walks through what happens when the proxy breaks: you can now be highly productive without being competent, because the AI supplies the productivity and asks nothing of the competence.

That's the setup for the [slop grenade](/glossary/slop-grenade/): a polished, subtly-wrong AI artifact lobbed at a colleague who now has to deal with it. The damage is an attention asymmetry. It takes far longer to defuse a slop grenade than to throw one, so the sender spends something cheap — model tokens — to consume something expensive: a domain expert's attention. Do that across an org and you've built a machine that converts cheap output into expensive distraction. That's the part I'd call deadly, not the individual artifacts.

Management tends to make it worse rather than better, because the metrics that are easy to see are the ones AI inflates. The one-pager becomes twelve pages. Status updates become bulleted summaries of bulleted summaries. Everyone looks busier, the documents look more thorough, and the signal-to-noise quietly collapses while the dashboards point up and to the right. Koch's most actionable sentence is aimed straight at this: treat AI-assisted productivity gains and genuine competence development as *separate* outcomes that require *separate* management. Optimizing the first does nothing for the second, and usually erodes it.

There's a reason the Amazon six-pager refuses to die: a written narrative is proof of work of thinking. If you outsource the writing, you've skipped the thinking and kept the artifact, which is the whole problem in miniature. Dan mentioned shipping a document to his boss and adding a line underneath — "I wrote this by hand" — because the signal now needs stating. A year ago that would have read as a joke.

## The senior-engineer tell

Here's the counterintuitive part, and the one piece of good news. The engineers walking around genuinely afraid they can't code without the model anymore are, by definition, still calibrated. Their self-assessment is tracking a real drop in unaided skill — which means the instrument still works. The dangerous signal is the opposite one: feeling more capable than you've ever been. If using AI to write code has made you feel like a markedly better engineer, that's not necessarily growth. It might be the decoupling, working exactly as described.

Rahul reached for Buffett and Munger on the episode, and the circle-of-competence framing fits better than I expected. Their whole discipline is knowing the edge of what you actually know, because the expensive mistakes happen just past it. AI can widen that circle, or it can convince you the circle is wider than it is, and from the inside the two feel identical. The honesty has to come from you, because nothing else in the loop is incentivized to supply it.

A fair caveat, because not all decoupling is a problem. Dan's read is that his core competency was never writing the most elegant code by hand, so handing that part to a model isn't a loss — it's delegation, and the AI's version is often more readable than what he'd have grumbled out himself. That's legitimate. The question isn't whether you've outsourced some competencies; it's whether you *chose* which ones, or whether the choice is being made for you, one frictionless session at a time.

## What to actually do about it

The decoupling is structural, so the fixes are about reintroducing the friction that used to be free.

1. **Score productivity and competence on separate cards.** Whether you're managing yourself or a team, stop letting throughput stand in for skill. "How much did we ship" and "how much do we understand of what we shipped" are now different questions with different answers, and only one of them shows up on the dashboard.
2. **Schedule calibration reps.** Close the model and implement something from scratch on a regular cadence — not as a Luddite gesture, as deliberate practice. If it feels harder than you expected, that gap *is* the measurement. It's the only cheap instrument you have for catching [cognitive debt](/glossary/cognitive-debt/) before production does it for you. (More on the career version of this in the [developer careers guide](/topics/ai-developer-careers/).)
3. **Keep one reviewer who won't flatter you.** The model won't tell you the architecture diagram is wrong; a sycophancy-free human will. That person is now the most valuable reviewer on the team, precisely because they supply the feedback the tools structurally can't.
4. **Write the things where the writing is the thinking, by hand.** The design doc, the postmortem, the one-pager. If a document exists to prove you reasoned through something, generating it defeats its only purpose. Run the prose through a model afterward for polish if you want — but do the reasoning yourself, while it still counts.

The reassuring frame and the alarming frame are the same fact seen from two angles. AI raised the floor on what everyone can produce, which is real and good. It also detached that floor from what anyone actually knows, which is the part nobody put in the launch post. The curve told us, for a century, roughly how much to trust our own sense of how good we are. That instrument is reading garbage now. Until someone rebuilds it, the only honest move is to assume your confidence is overstated and go check.

*This post was drafted by an AI agent (Claude) from ADI Pod episode transcripts and edited for the site. Source episode: [30](/episodes/30-fable-5-ban-metas-ai-gulag-elias-thorne-loop-engineering/).*
