---
title: "Almost Nobody Reads the PRs Anymore: Field Notes from Seattle Tech Week"
description: "I spent Seattle Tech Week asking founders and engineers whether they still read AI-generated pull requests line by line, and how they hire now. The gap between stated policy and revealed practice was the real finding."
date: "2026-08-07"
slug: "seattle-tech-week-ai-survey"
keywords: "AI code review survey, do developers read AI generated code, AI pull request review, Seattle Tech Week 2026, AI hiring interviews, whiteboard interviews AI, vibe coded take home, AI fluency hiring, stated vs revealed preferences, flesh robot, reverse centaur"
episodes: ["36"]
---

Your company's engineering policy says every pull request gets reviewed. I spent a week asking engineers whether that's true, and the answer is: for some definition of "reviewed."

Seattle Tech Week (formerly Seattle Startup Week) is a week of panels, networking events, and variations on the question "what does AI mean for software engineering." Instead of collecting swag, I collected answers. I asked roughly the same two questions of every founder, hiring manager, and engineer who would talk to me: do you still read your AI-generated PRs line by line, and — for the people doing the hiring — what are you actually hiring for now?

Methodology caveats up front, because this is field notes, not a study. The sample is startup-heavy — mostly founders, some engineers at large companies — so it is not an unbiased slice of the industry. Nobody was answering under oath. And exactly one person refused a question, on the grounds that which model is best at visioning tasks was their secret sauce. Everyone else opened up with surprising ease. It turns out developers are dying to tell someone how they actually work, as long as that someone isn't their employer.

The useful frame for what I heard is one we covered back in [Episode 26](/episodes/26-llm-neural-anatomy-with-david-noel-ng-forward-deployed-everybody-running-llms-at-home/): stated versus revealed preferences. Ellis and Huang showed that an AI trained on what people *say* they want underperforms one trained on what they *do*. The same gap runs straight through how our industry talks about AI-assisted engineering. What follows is organized around it.

## Stated: We Review AI Code. Revealed: One in Ten.

Almost nobody I spoke to still reads AI-generated PRs line by line. The exception rate was maybe one out of ten. This includes people who ship to production, at companies whose policies assume line-by-line review is happening.

The quote that stuck with me came from a developer at a large company, offered unprompted: if their employer knew how little they actually review, the company would not be happy. That's the finding in miniature. What devs do on the ground and what company policy assumes have started to diverge, and the divergence is entirely bottom-up. No VP announced the end of code review. It just quietly stopped happening, one 14,000-line PR at a time.

There's also a class of founders who never had the option: non-engineers vibe-coding their way to a product. They aren't reading the PRs because they can't. The interesting part is that most of them know it — they usually have a technical friend or mentor sanity-checking the high-level decisions. Nobody I met claimed software engineering is dead. The claim is narrower and more uncomfortable: reading every line is dead, and we're improvising what replaces it.

## Stated: Nothing Replaced Review. Revealed: The Artifacts Moved.

The natural follow-up — if you're not reading the code, what *are* you reading? — got the most interesting spread of answers.

**Specs and plans.** The most common answer, which will please the [spec-driven development](/blog/spec-driven-development-ai/) camp. Though I've also had people tell me you shouldn't be reading your specs and plans either, so there is healthy diversity in how far ahead of the code people are willing to stop reading.

**Architecture diagrams and boundary conditions.** Often in mermaid. The idea: if you no longer read every function, at least hold the function signatures and make sure the agents don't blur your layered architecture. We haven't agreed on a single best way to document architecture — we never have — but "keep the boundaries clean and legible" came up again and again.

**The tests.** A few people read tests instead of implementation, on the theory that good tests tell you more than the code. The theory holds right up until the agent games it. Dan's favorite specimen: 90% coverage achieved by one passing function called in a loop, dwarfing the failures. Somebody still has to be able to tell a test suite from a coverage costume, and that somebody has to understand the system.

Which is the real pattern under all three answers. There was plenty of talk of review agents, and review agents genuinely help. But every artifact people named — spec, diagram, boundary, test — is a comprehension layer, a way for a human to keep a mental model without reading the diffs. The review didn't disappear. It moved up a level of abstraction, exactly where [cognitive debt](/blog/cognitive-debt-ai-development/) is hardest to see accumulating.

## Stated: We Hire for Product Obsession. Revealed: Nobody Asks Product Questions.

The hiring answers ranked cleanly. Technical skill is still first — but it has moved from LeetCode to architecture and system design, ideally with scar tissue: hiring managers want the story of the technically-correct-but-practically-flawed decision that burned you. (One founder noted the catch honestly: old battle scars may not transfer to the new world.) Product and customer obsession came second — can you talk about a time you shaped product direction, not just executed it. AI fluency was third; some call it being "AI-pilled," which I am choosing to read as a warning label. Mission alignment and don't-be-a-jerk round out the list. You should still shower, though one founder conceded that remote work makes this unverifiable.

Then I asked about process, and the revealed preferences got louder than the stated ones.

Despite everyone naming product obsession as a top criterion, nobody could point to an actual product question in their interview loop. It sometimes gets rolled into the design question. Mostly it's vibes.

Despite AI fluency ranking third, nobody has a rubric for grading it. The problem is structural: the senior engineer evaluating your AI usage has their own AI usage, and "are you using AI the way I use AI" is the new tabs-versus-spaces. We've reinvented the Vim-versus-Emacs tribal check and given it hiring authority.

And despite take-homes being everywhere, almost nobody examines how the candidate worked — the prompts, the AI interaction history, the pushback. Everyone grades outputs. The cost of that showed up in the week's best cautionary tale: a founder hired a principal engineer off a take-home the candidate had vibe-coded, and fired them inside two months. Costly and embarrassing, in the founder's own words. This is why in-person whiteboarding is coming back, and I'm honestly glad — the two-way design conversation is where you see how someone drives with a team. A few companies now provide model access during take-homes, which answers the equity concern [Nathan Lubchenco raised on Episode 23](/episodes/23-why-models-over-edit-your-code-meta-keystroke-surveillance-interviewing-engineers-in-the-ai-age/): not everyone has had a $200-a-month harness to practice on.

One CTO ran the exception to all this uncertainty: a hiring process that's continuously updated and benchmarked against batches of candidates, maintaining a live distribution of how developers actually perform. It's HackerRank as a hiring philosophy — a little brutal, but at least it's an honest, calibrated brutality, which puts it ahead of vibes.

The big companies, for what it's worth, know they're behind. The FAANG-level hiring managers I spoke to said some version of "we don't really know; the ship is slow to turn" — LeetCode persists partly because some engineers resist replacing it.

## The Flesh Robot

The moment I will remember from the week came at ten o'clock on Monday morning. A multi-time founder — a couple of highly rated repos to his name — proclaimed on a panel that he is happy to be a reverse centaur, a [minotaur](/glossary/minotaur/), or, in his own words, a flesh robot: the AI is the number-one brain, and he happily does its bidding. Tongue-in-cheek, yes. But it was the first time I've heard the minotaur position claimed as an identity rather than diagnosed as a failure mode, in person or anywhere else.

Two smaller vibes from the same panel, for the record. Every panelist reported using voice mode more and more; I was behind the pack here, having quit after one garbled Gemini session, and I'm now a convert after a week of philosophical arguments with Claude while driving. And when the AGI question came up, everybody on the panel agreed we already have it — for some definition of it. The qualifier is doing a lot of work in that sentence, which I believe makes it the most honest AGI take currently available.

## What I'd Standardize First

Reframing the week: the industry's stated preferences describe a world where humans review code and hire for product sense. Its revealed preferences describe a world where humans maintain comprehension layers and hire by tribal recognition. Closing that gap is more tractable than it sounds, and I think the order is:

1. **Make the comprehension layer explicit.** If specs, diagrams, and boundary conditions are what people actually read, treat them as first-class artifacts with owners and reviews — the [steel-threads and program-design discipline](/glossary/steel-threads/) is the closest thing to a written standard so far.
2. **Review the AI interaction history, not just the output.** In take-homes especially: when did the candidate tell the agent it was wrong, and why? That one artifact would have saved a principal engineer's salary and a founder's two months.
3. **Write down the AI-fluency rubric.** Any rubric. A bad one that's written down can be argued with and improved; "use AI like me" cannot.

If you run a hiring process or an engineering org and your answers differ from what I heard, I'd genuinely like to know — the sample needs more than one week of Seattle. Email us at humans@adipod.ai. The full survey discussion is in [Episode 36](/episodes/36-pacing-the-frontier-anthropic-models-go-rogue-why-software-factories-fail-math-in-the-age-of-ai/), where it sits alongside Terence Tao on what mathematicians are for now — a question our field should probably stop assuming it has already answered.
