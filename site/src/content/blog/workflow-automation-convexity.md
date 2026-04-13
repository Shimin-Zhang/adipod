---
title: "Workflow Automation Convexity: Why AI Will Not Take Half Your Job"
description: "Every AI job prediction assumes automation scales linearly. It does not. The concept of convexity explains why 'AI will do 50% of coding' is not half as useful as it sounds."
date: "2026-04-11"
slug: "workflow-automation-convexity"
keywords: "AI job automation, workflow automation convexity, AI replacing developers, AI coding automation"
episodes: ["14"]
---

"AI will automate 50% of coding within two years." You have seen some version of this claim from every major AI CEO, from analyst reports with confident-looking bar charts, and from that one person on your team who just discovered agentic workflows. The number varies — 30%, 50%, 80% — but the underlying assumption is always the same: automation scales linearly. If AI can do half the tasks, it will do half the job. If it can do 80% of the tasks, you are 80% replaced.

This assumption is wrong, and a [paper by Philip Trammell](https://philiptrammell.com/static/Workflows_and_Automation.pdf) called "Workflows and Automation" offers the clearest framework I have encountered for understanding why. The concept is [workflow automation convexity](/glossary/workflow-automation-convexity/) — the idea that the relationship between task automation and job automation is not a straight line but a convex curve. A long, flat plateau of minimal impact followed by a steep cliff of total displacement. Not 50% automated. Either barely automated or fully automated, with very little stable ground in between.

When [we discussed this on episode 14 of ADI Pod](/episodes/14-crabby-rathbun-model-councils-why-you-want-more-tech-debt/), the framework clicked because it explained something we had all observed but could not quite articulate: why the PwC case studies keep reporting underwhelming results, why "AI will do X% of Y" predictions from 2024 have not materialized proportionally, and why certain roles feel immune to AI disruption while others feel precarious despite similar task-level benchmark scores. The answer is that jobs are not bags of independent tasks. They are connected workflows, and the connections are load-bearing.

## Jobs Are Not Task Lists

Open any job description for a software engineer. It will mention writing code, reviewing code, debugging, communicating with stakeholders, writing documentation, attending design reviews, estimating effort, mentoring junior developers. The standard approach to AI job displacement analysis is to take each of these tasks, measure how well AI performs at it in isolation, sum the percentages, and declare the job X% automatable.

Trammell's central argument is that this approach is structurally flawed because it ignores what he calls *learning spillovers* — the knowledge transfer that occurs between connected tasks within a single role. The developer who writes the code is better at reviewing that code because the act of writing it built a mental model of the system. The developer who debugs an issue is better at estimating future work because the debugging process revealed hidden complexity. The developer who attends the design review is better at writing the code because the review surfaced constraints and intentions that would not appear in any spec document.

These spillovers are not a nice-to-have. They are the reason the tasks are bundled into a single role in the first place. If writing code and reviewing code had zero spillover — if someone who only writes code and never reviews it would produce the same quality as someone who does both — then companies would have already split them into separate roles long before AI entered the picture. They did not, because the spillovers are where a large fraction of the value lives.

My co-host Rahul Yadav put it concisely on the episode: "It's never like you will just do this one task over and over again for the rest of your career. They're connected because from the process of doing one activity, you actually have a better model, and it feeds into the other activity." That is the mechanism. And once you see it, the math changes.

## The Shape of the Curve

Here is where convexity becomes concrete.

If a job consists of tasks A, B, C, D, and E — all with significant learning spillovers — then automating task C alone does not give you 20% automation. It gives you something closer to 5%, because the human still needs to do A, B, D, and E, and removing C from the human's loop actually degrades their performance on the other tasks by eliminating the spillover that C provided. The human who no longer debugs is a worse estimator. The human who no longer reviews code understands the codebase less deeply. You have not removed 20% of the work. You have removed 20% of the tasks and added friction to the remaining 80%.

This is the convex deployment Trammell describes. On a graph where the x-axis is "percentage of tasks AI can handle" and the y-axis is "actual job displacement," the curve hugs the bottom for a long time. At 30% task automation, job displacement might be near zero. At 50%, it might be 10%. At 70%, still only 20%. Then somewhere around 85-90% — the point where AI can handle enough interconnected tasks to capture the spillover effects — the curve goes vertical. Displacement jumps from marginal to total.

The practical implication is binary in a way that the linear models are not. Under convexity, you do not get a smooth transition where developers gradually do less coding and more "higher-level" work. You get a long period where AI tools make developers somewhat more productive but do not eliminate roles, followed by a relatively rapid shift where entire workflows become fully automatable and roles disappear in clusters rather than fractions.

## Why the PwC Reports Keep Disappointing

This framework explains something that has puzzled observers for over a year. Companies adopt AI tools, run pilots, measure the results, and report numbers that look underwhelming relative to the hype. Rahul brought up the PwC case study from a few episodes prior: "People say, yeah, we tried it, but it didn't really make any significant dent in what we're trying to do."

Under the linear model, this is confusing. AI demonstrably performs well on isolated coding benchmarks. It can write functions, generate tests, produce boilerplate. Why does not that translate into proportional business impact?

Under convexity, it makes perfect sense. The company automated a slice of a workflow. The slice that is easiest to automate — repetitive code generation, boilerplate, pattern-matching tasks — is also the slice with the most spillover to other tasks. The developer who used to write that boilerplate was also building context about the system while doing it. Removing that step saved time on the task but eroded performance on adjacent tasks. Net productivity gain: modest. Nowhere near the benchmark scores implied.

Then, as Rahul noted, "someone just throws their hands up and says 'I can just do this whole thing myself. Why are we wasting our time on this?'" That is the convexity plateau. AI is doing 30% of the tasks and delivering 5% of the value, because the tasks are not independent and the spillovers are not transferable.

## The Verification Problem

My co-host Dan Lasky added a dimension to this that I think is underappreciated. Beyond the spillover issue, there is the question of measurability. Software development adopted AI faster than other knowledge work in part because code has a built-in verification mechanism: it compiles or it does not. Tests pass or they fail. There is a feedback loop.

"Where is that in a Word doc?" Dan asked. "There's style and all these intangibles. You might agree with it, but what if your boss doesn't agree with it and they're judging your output?" The tasks within a workflow that are hardest to automate are not just the ones that are technically difficult. They are the ones where the quality criteria are ambiguous, socially negotiated, and require the kind of judgment that comes from — there it is again — learning spillovers.

Writing code is measurable. Deciding what code to write is not, at least not in any way that benchmarks capture. The estimation, the scoping, the architectural judgment, the "this approach will create a maintenance nightmare in six months" pattern recognition — these are the tasks that resist automation precisely because they depend on accumulated context from performing the other tasks. They are the bottom of the convex curve, and they are where most of the actual engineering judgment lives.

## What Convexity Predicts

If Trammell's framework is right — and the PwC-style underwhelming results suggest it is at least directionally correct — then several things follow.

**Partial automation is an unstable equilibrium.** The "AI will do 50% of the job and humans will do the rest" scenario is not a steady state. It is a transition period that resolves in one of two directions: either the human reclaims the automated tasks because the spillover loss is too costly (companies stop using the tool), or AI capabilities advance to the point where the entire connected workflow can be automated and the human is removed from the loop entirely. The middle ground — where AI does exactly half and humans do exactly half, indefinitely — is the scenario that convexity specifically rules out.

**Job loss will be clustered, not gradual.** The convex curve predicts a long plateau followed by a steep cliff. During the plateau, AI improves developer productivity by some percentage — probably 20-40% in the most favorable cases — without eliminating roles. Developer hiring might slow, or the same team might handle more features, but headcount stays roughly stable. Then, when AI can handle a sufficiently large connected subgraph of the workflow, displacement happens quickly. Entire function areas go from "humans with AI assistance" to "AI with minimal human oversight" within a product cycle. If you are looking for a framework for which roles are safe and which are not, the question is not "can AI do any of these tasks" but "can AI do enough of the connected tasks to capture the learning spillovers."

**Benchmarks will continue to mislead.** Current AI coding benchmarks — SWE-bench, HumanEval, MBPP — measure performance on isolated tasks. Trammell's point is that task-level performance is a poor predictor of job-level impact because it ignores the workflow structure. A model that scores 90% on generating individual functions might contribute 15% to actual developer productivity, because function generation is one node in a graph of interdependent activities. Benchmarks that measure end-to-end workflow completion — from spec interpretation through code generation, testing, review, deployment, and debugging in context — would be far more informative. I have not seen anyone building those yet.

## Where This Gets Uncomfortable

There is a version of this argument that is comforting for developers: AI cannot take your job because jobs are too complex and interconnected for partial automation to work. I would not lean too hard on that conclusion. Convexity does not say AI will never automate your role. It says the timeline is longer than the linear predictions suggest — but that when it happens, it will be faster and more complete than anyone expects.

The honest read of the paper is closer to this: there will be a longer period of relative safety than the hype suggests, followed by a shorter period of more total disruption than anyone is preparing for. (If you are thinking about [how AI reshapes developer careers](/topics/ai-developer-careers/) more broadly, this is the structural force to watch.) That is not "AI won't take your job." It is "AI won't gradually erode your job into a diminished version of itself — it will either not be able to do your job or it will be able to do all of it."

As I noted on the episode: the moral might be that developers should join more meetings, because meetings involve the kind of cross-functional learning spillovers that are hardest to automate. The human who holds the [cognitive structure](/glossary/cognitive-debt/) of the codebase in their head — who understands not just what the code does but why, and how it connects to the business domain and the team's intentions — is the person at the bottom of the convex curve. That understanding is built by doing the connected work, not by having an AI do parts of it for you.

## The Practical Takeaway

If convexity is the right model, then the common advice to "learn to work alongside AI" is incomplete. It is not wrong — the productivity gains during the plateau are real and worth capturing. But it misses the strategic question, which is whether the plateau or the cliff comes first for your specific workflow.

Here is how I think about it:

**Audit your spillovers.** Map the tasks in your role and identify which ones share significant learning spillovers. Writing code and debugging code have high spillover. Writing code and writing technical documentation have lower spillover. The tasks with low spillover between them are the ones most likely to be automatable in isolation without degrading your performance elsewhere. Those are the tasks to aggressively delegate to AI now. The [AI fluency pyramid](/blog/ai-fluency-pyramid/) framework is relevant here — as you climb the levels, you are building the judgment skills that sit at the bottom of the convex curve.

**Invest in the connective tissue.** The tasks that make you better at other tasks are the ones with the highest option value. Design reviews, cross-functional conversations, debugging sessions where you learn about adjacent systems — these are not overhead. Under convexity, they are your primary source of non-automatable value. This is the part of your job to protect, not the part to delegate.

**Watch for the vertical.** The cliff, when it comes, will not announce itself through gradually diminishing task lists. It will look like a new model generation that suddenly handles not just one task but an entire connected workflow. When AI can go from reading a spec to shipping tested, reviewed, deployed code in the context of an existing codebase — with the judgment that currently requires human understanding of the system — that is the vertical portion of the curve. We are not there yet. Whether "not there yet" means two years or ten years is the question that nobody can honestly answer.

The prediction factory will keep producing confident numbers. AI will automate 50% of coding by 2027. AI will handle 80% of customer service by 2028. These numbers assume a line where the data shows a curve. The curve is more interesting, more honest, and considerably less comfortable — because it says the people telling you that half your job will be automated are not wrong about the direction. They are wrong about the shape. And the shape is the part that matters.
