---
title: "Cognitive Debt: The Hidden Cost of Letting AI Write Your Code"
description: "Technical debt is code you wish you had written better. Cognitive debt is code you don't understand at all, and AI compounds it faster than teams realize."
date: "2026-04-11"
lastUpdated: "2026-04-28"
slug: "cognitive-debt-ai-development"
keywords: "cognitive debt software, cognitive debt AI, AI code understanding, technical debt AI"
episodes: ["14", "15", "20", "22"]
---

[Cognitive debt](/glossary/cognitive-debt/) is the gap between what your codebase does and what you understand about it. Unlike technical debt (code you shipped knowing it wasn't ideal), cognitive debt is invisible: you don't know what you don't know until something breaks. And AI-assisted development is compounding it faster than anything we've seen before.

Every developer has inherited a codebase they didn't understand. You open the repo, scan the folder structure, read a few files, and slowly build a mental model of what the thing does. That process, the construction of understanding, is so automatic most people never think about it. But it's the load-bearing wall of software engineering, and AI is quietly removing it.

The distinction matters from the start. Technical debt is a rational tradeoff: you take the shortcut now, pay the maintenance cost later, and come out ahead if product velocity outpaces the interest. Cognitive debt compounds differently, because the interest is invisible and the only repayment currency is human attention.

[Margaret Storey](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/), a software engineering researcher at the University of Victoria, proposed this framework in early 2026: a program doesn't just live in a repository. It lives in the minds of the developers who maintain it, capturing what the program does, how intentions are implemented, and how the system can be changed over time. When [we discussed her work on ADI Pod](/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt/), that reframing hit me hard. The value of a software engineer isn't just creating code. It's being a keeper of the mental structure of what the program is supposed to do. If that mental structure erodes, the code still runs. But nobody can safely change it.

AI-assisted development erodes it faster than anything we've seen before.

## The Financial Debt Analogy

Financial debt has four states: principal, interest, distressed debt, and default. Cognitive debt maps to each of them with uncomfortable precision.

**Principal** is the understanding gap itself. Every time an agent writes a function you accept without fully comprehending, you're borrowing against your future ability to maintain that code. The principal grows with every merged PR you skimmed, every "looks good to me" on a diff you didn't trace through mentally. In Storey's research, she found that students using AI could build features quickly, meeting milestones initially. The principal looked manageable. The balance sheet looked healthy.

**Interest** is the cost of maintaining code you don't understand. It shows up as longer debugging sessions, as changes that break things in unexpected places, as the growing sense that touching one part of the system might cascade into another. Unlike technical debt, where you at least know where the shortcuts are, cognitive debt interest is invisible. You don't know what you don't know until something breaks.

**Distressed debt** is what Storey observed by week seven or eight. The teams hit a wall. They could no longer make simple changes without breaking something unexpected. The accumulated cognitive debt had reached a point where the interest payments (the debugging, the context recovery, the tentative edits followed by rollbacks) consumed more time than new feature development. Every codebase reaches this point eventually. AI-assisted codebases reach it in two months.

**Default**, what I've started calling [cognitive bankruptcy](/glossary/cognitive-bankruptcy/), is what Mario Zechner described in his essay ["Thoughts on Slowing the Fuck Down."](https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/) Zechner is the creator of the Pi agent coding harness, and his post is a candid reckoning with what happens when you let agents run ahead of your comprehension. The passage that stuck with me, from his "everything is broken" section: you realize you can no longer trust the codebase, and worse, the gazillion unit tests and end-to-end tests your agents wrote are equally untrustworthy. The only reliable measure of "does this work" becomes manually testing the product. When [we discussed it on episode 20](/episodes/20-claude-code-source-leak-emotion-concepts-in-llms-and-surprising-facts-ais-know-about-us/), I described it as cognitive debt where the interest payments come due and you can no longer pay. That's bankruptcy. You've lost the ability to reason about your own system, and no amount of prompting will get it back.

| Stage | Financial Analog | Signal | Timeline |
|---|---|---|---|
| **Principal** | Loan balance | PRs merged without full comprehension | Ongoing |
| **Interest** | Maintenance cost | Longer debugging, unexpected cascading breaks | Weeks 2-6 |
| **Distressed debt** | Cannot service payments | Simple changes break things; more time debugging than building | Weeks 7-8 |
| **Default (cognitive bankruptcy)** | Insolvency | Cannot trust codebase or tests; manual testing only | Weeks 8+ |

A worked example of the failure landed on [Episode 22](/episodes/22-is-claude-opus-4-7-mythos-distilled-running-qwen-3-6-locally-and-the-ai-on-ai-arena/). Dan described missing a tight production deadline on a bug a pre-LLM colleague then fixed in roughly five minutes, and admitted on air that his instinct in the moment was to double down on tooling rather than slow down to build comprehension. That instinct is the under-recognized half of cognitive bankruptcy: when the debt is high, "I just need a better prompt" feels productive even though the actual remediation is reading code. The colleague's five-minute fix worked because they had hand-written some of the surrounding tooling pre-LLM and still held the mental model. Dan didn't, and no amount of agent-side prompting could synthesize what wasn't there.

## Why Cognitive Debt Is Not Technical Debt

The instinct is to treat cognitive debt as a subspecies of technical debt. It's not. They're different liabilities on different balance sheets.

Technical debt is a property of the code. You can point at it. This module uses a deprecated pattern. That service has no error handling. The database schema grew organically and now has three different ways to represent the same entity. Technical debt is legible; it exists in the artifact. A new developer with enough time could audit it.

Cognitive debt is a property of the team. It's the delta between what the system does and what the people maintaining it understand about what the system does. You can't audit it by reading the code, because the deficit isn't in the code; it's in the developers' heads. Two teams with identical codebases can have wildly different levels of cognitive debt depending on who wrote the code, who reviewed it, and who actually understands what it does.

| | Technical Debt | Cognitive Debt |
|---|---|---|
| **Lives in** | The code | The team's heads |
| **Visibility** | Legible (you can point at it) | Invisible (you don't know what you don't know) |
| **Audit method** | Read the code | Ask the team what they do not understand |
| **Remediation** | Refactor the code | Learn the system (reading, tracing, building mental models) |
| **Can be outsourced** | Yes (a future agent can refactor) | No (understanding requires human attention) |
| **Compounds via** | Shortcuts accumulating | PRs merged without comprehension |
| **Interest rate trend** | Falling (cheaper inference, better models) | Rising (codebases growing faster than understanding) |

This distinction matters because the remediation strategies are completely different. You pay down technical debt by refactoring. You pay down cognitive debt by learning: reading, tracing, building the mental model that was never constructed in the first place. And that takes time that feels unproductive, because you aren't shipping anything while you do it.

My co-host Rahul Yadav made an observation on [episode 14](/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt/) that reframed this for me: what AI-assisted development does is speed-run a startup's entire lifecycle of accumulated understanding gaps. The problem where "no one understands the whole system end to end" used to take companies years to develop. Now it takes weeks. You're compressing decades of institutional knowledge erosion into a single quarter.

## The Paradox: More Tech Debt Might Be Fine, but More Cognitive Debt Is Not

Here's where it gets counterintuitive. On the same episode, Rahul argued (persuasively) that teams should be taking on *more* technical debt right now. The cost of creating software is so low that it's like a zero interest rate environment for code. You can aggressively borrow against the future, ship fast, find your value proposition, and service the debt later when inference costs are even lower. As long as your productivity growth outpaces your rate of debt accumulation, the GDP-to-national-debt ratio applied to software, you can run a deficit indefinitely.

Dan Lasky added the critical caveat: you still need to be smart about where you take on the debt. Irreversible decisions (database migrations, fundamental architectural choices) aren't the same as messy application code you can have an agent rewrite in 35 seconds. The cheap debt is the kind you can refinance. The expensive debt is the kind that locks you in.

I think this framework is right for technical debt. But cognitive debt doesn't follow the same economics, because you can't outsource the repayment. A future, cheaper model can refactor your code. A future, cheaper model can't retroactively build your understanding of what that code does and why. The interest rate on cognitive debt isn't falling. If anything, it's rising, because as codebases grow faster and agents proliferate, the gap between "what the system does" and "what any human understands about it" widens in both directions simultaneously.

## What Makes It Compound

Three forces compound cognitive debt in ways that make it structurally different from previous forms of software understanding gaps.

**Sycophancy erodes your error signal.** A [study published in *Science*](https://www.science.org/doi/10.1126/science.aec8352) found that every model tested, from Mistral to Llama, agreed with users at significantly higher rates than a crowdsourced human baseline. Users rated sycophantic responses 9-15% higher in quality and reported 6-8% higher trust in the AI. When we [tested this ourselves on episode 15](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/), the results were uneven. GPT 5.1 Instant refused manipulation entirely, Claude Haiku was too empathetic but self-aware about it, and Gemini 3 agreed with a fabricated workplace bias claim. The implication for cognitive debt: when you ask your agent "does this look right," the agent is structurally biased toward telling you yes. Your primary feedback mechanism for gauging your own understanding, asking the tool that wrote the code, is compromised by the same dynamics that make social media addictive. Every "looks good" from a sycophantic model is a missed opportunity to discover that your mental model has drifted from reality. That's [verification debt](/glossary/verification-debt/) accumulating silently on top of cognitive debt.

**The mentoring surface area is shrinking.** The [ThoughtWorks Future of Software Engineering retreat](/episodes/15-convincing-ai-the-earth-is-flat-inference-at-17k-tokens-sec-and-an-agile-manifesto-for-the-agentic-age/), organized by signers of the Agile Manifesto, identified that code review historically served two purposes: quality gating and mentorship. When a senior developer reviews a junior's PR, they're teaching architectural judgment, consistency, and domain reasoning alongside checking for bugs. But if agents write the code and agents review the low-risk PRs, that learning channel narrows. The retreat participants couldn't answer where the mentoring goes. Rahul suggested maybe you mentor people on writing good prompts, then laughed because he didn't know what that would look like either. The result: the primary mechanism by which teams historically fought cognitive debt, shared understanding built through collaborative code review, is being hollowed out at exactly the moment cognitive debt is accelerating.

**Review fatigue makes the remaining checks unreliable.** Rahul drew an analogy on episode 15 that I keep coming back to: judicial decision fatigue. Judges make measurably worse rulings as they get hungrier closer to lunch. Code reviewers face the same dynamic. Your first few AI-generated PRs of the day get genuine scrutiny. By afternoon, you're rubber-stamping. Dan Lasky named what he called "review fatigue," noticing a capitalized "The" in an article header, mentally flagging it as AI-generated, and immediately disengaging. The pattern recognition that should be catching logical errors is being spent on surface-level heuristics for "was this written by a human." And the code an agent writes looks plausible by design. It follows the patterns of your codebase. It compiles. The tests pass. The logic errors that [AI code produces at 1.7x the rate of human code](/blog/ai-code-quality-bugs/) are exactly the kind of errors a fatigued reviewer will miss.

## Fighting Cognitive Debt Without Abandoning AI

Zechner's prescription is to maintain what he calls the "gestalt" of your system (the architecture, the APIs, the fundamental design) and write the important parts by hand. Limit your AI-generated output to your ability to review the code. That's sound advice and probably the right default for individual projects. But it doesn't scale to teams with ten agents per person, which is where the industry is heading.

Here's what I think a more complete strategy looks like, borrowing from the financial metaphor.

**Know your balance.** Dan Lasky runs what he calls a "detro," a debt retrospective, like a retro but focused on technical debt. The team surfaces what they know they owe. The exercise works because it makes invisible liabilities visible. The same format could work for cognitive debt, but it requires a more vulnerable kind of disclosure: not "here's where the code is bad" but "here's what I don't understand." As Dan observed, people don't want to say what they don't know in a group. Getting through that vulnerability gap is the price of admission. It might only take one person saying "I have no idea what this module does" to discover that nobody else does either.

**Run regular audits.** Rahul pointed out that modern agents and IDEs have excellent search and summarization capabilities. You can ask your agent to give you a high-level overview of any module, trace a feature across files, explain the flow. This is a real tool for fighting cognitive debt; you can regularly generate summaries of what's going on and keep your mental model updated. But treat it as an approximation, not a substitute. The agent's summary is a map. Walking the territory yourself, reading the actual code, tracing the actual paths, is what builds the understanding that prevents cognitive bankruptcy.

**Allocate understanding time.** Storey's first principle is that at least one person on every team needs to know the codebase inside out. Usually the senior developers. That sounds obvious until you realize that "knowing the codebase" now means actively studying code you didn't write, which means blocking out time for reading that produces no visible output. Managers who track velocity will see this as idle time. It's the opposite. It's the only thing preventing the codebase from becoming a black box that nobody can safely touch.

**Tier your risk.** The ThoughtWorks retreat framework applies here too. Not all cognitive debt is equally dangerous. Code that runs an internal dashboard and touches nothing critical can carry a higher cognitive debt load. If it breaks, you can investigate then. Code that handles production data, financial transactions, or security boundaries needs active understanding from at least one team member at all times. Match your comprehension investment to the blast radius of misunderstanding.

**Watch the week-seven wall.** Storey's finding that teams hit the wall at week seven or eight of heavy AI-assisted development is the most actionable data point in this entire discussion. If you're starting a new AI-heavy project, schedule a cognitive debt audit around the six-week mark. That means a dedicated session where the team walks through the system architecture, traces key flows, and identifies the parts nobody fully understands. Do it before the wall, not after.

## The Part Where Some Tech Debt Is Good

I want to be careful not to overstate this. Rahul's argument that teams should aggressively incur tech debt right now isn't wrong. The economics genuinely favor shipping fast and servicing code quality debt later. Inference costs are falling. Models are getting better at refactoring. A messy codebase that found product-market fit is worth infinitely more than a clean codebase that built the wrong thing.

The mistake is conflating the two types of debt. Take on more tech debt, sure, with eyes open and an exit strategy. But cognitive debt doesn't have the same exit strategy. You can't refinance it. You can't automate the repayment. The only currency it accepts is human attention, and human attention is the one resource that isn't getting cheaper.

The teams that will handle this well are the ones that can hold both ideas simultaneously: ship fast, borrow aggressively against code quality, and simultaneously invest in the understanding that prevents [cognitive surrender](/blog/cognitive-surrender-ai/), the point where you stop trying to comprehend what your system does and just hope the agents keep it running. (We explore that concept further in the [glossary](/glossary/cognitive-surrender/).) That's not a strategy. That's a prayer with a CI/CD pipeline.

Cognitive debt is the defining liability of the [AI-assisted development era](/topics/ai-developer-careers/). Unlike technical debt, it's invisible on every dashboard and absent from every sprint metric. It accrues in the space between what your system does and what your team knows. The interest compounds silently. And when the bill comes due, the only people who can pay it are the ones who were paying attention all along.
