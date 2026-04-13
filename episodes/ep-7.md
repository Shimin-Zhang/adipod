---
episode: "7"
title: "Project Vend Update, Hallucinating Neurons, and Year End Reflections"
date: "2025-12-27"
slug: "7-project-vend-update-hallucinating-neurons-and-year-end-reflections"
description: "In this episode, Shimin and Dan explore the latest advancements in AI coding, including NVIDIA's new models, the implications of AI-generated code, and the outcome of Anthropic's Project Vend experiment with AI-managed vending machines. They discuss the benefits of multi-agent systems in development and research into hallucination neurons in large language models. The hosts conclude with year-end reflections on 2025's rapid AI adoption."
keywords: "NemoTron 3, Mamba transformer, MoE, GLM 4.7, CodeRabbit, AI code quality, hallucination neurons, H-neurons, vibe coding, year-end review, 2025 retrospective, open-weight models"
appleUrl: "https://podcasts.apple.com/podcast/artificial-developer-intelligence/id1857109105"
spotifyUrl: "https://open.spotify.com/show/4eDLlGoktxMngPNq9aGqLX"
overcastUrl: "https://overcast.fm/itunes1857109105"
pocketCastsUrl: "https://pca.st/itunes/1857109105"
amazonUrl: "https://music.amazon.com/podcasts/da06d4c3-ecf6-498f-abe3-4d3b00026bf2"
transistorId: "8effe510"
---

In this episode, Shimin and Dan explore the latest advancements in AI coding, including NVIDIA's new models, the implications of AI-generated code, and the outcome of Anthropic's project Vend, AI management of vending machines. They also discuss the significance of multi-agent systems in coding, the concept of vibe coding, and delve into the research on hallucination neurons in large language models. The episode concludes with a year-end review reflecting on the rapid developments in AI technology throughout 2025.

## Takeaways

- AI-generated code has been found to create more problems than human code.
- AI in vending machines has led to humorous and unexpected outcomes.
- Multi-agent systems can enhance the coding process by providing diverse solutions.
- H-neurons in LLMs are linked to hallucination and overcompliance.
- Year-end reflections highlight the rapid adoption of AI in the industry.
- The future of AI coding looks promising with ongoing innovations.

## Resources Mentioned

- [NVIDIA Nemotron 3 Family of Models](https://research.nvidia.com/labs/nemotron/Nemotron-3/)
- [GLM-4.7: Advancing the Coding Capability](https://z.ai/blog/glm-4.7)
- [Our new report: AI code creates 1.7x more problems](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-reporthttps://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report)
- [Project Vend: Phase two](https://www.anthropic.com/research/project-vend-2)
- [Claude Code Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [One Agent Isn't Enough](https://benr.build/blog/one-agent-isnt-enough)
- [Vibe Coding](https://davidbau.com/archives/2025/12/16/vibe_coding.html)
- [H-Neurons: On the Existence, Impact, and Origin of Hallucination-Associated Neurons in LLMs](https://arxiv.org/pdf/2512.01797)
- [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/)

## Chapters

- (00:00) - Introduction to AI Coding Landscape
- (05:00) - GLM 4.7 and Chinese AI Models
- (09:27) - Project Vend: AI Vending Machine Experiment
- (13:42) - Using Multiple AI Agents for Coding
- (22:51) - Exploring Agent-Based Approaches
- (30:28) - Deep Dive into Hallucination Neurons
- (36:07) - Dan's Rant: Context Management in AI


## Transcript

<details>
<summary>Show full transcript</summary>

Shimin (00:15)
Hello and welcome to Artificial Developer Intelligence, a podcast where two self-reengineers navigate the ever-changing AI coding landscape. We're your study buddies who uses AI every day at work and sometimes read a few AI papers at night. I'm Shimin Zhang and with me today is my co-host Dan, AKA the big dog with a W, Laski. Dan, are you feeling the holiday spirit?

Dan (00:40)
I'm feeling something and I think it's mostly impending death by way of whatever this virus is that I've got but you know, I'm glad to be doing this and Excited to see what we cover today

Shimin (00:51)
I am looking forward to your flu game. ⁓ On today's show, we have news thread mill where we're gonna talk about a couple of ⁓ new models from various labs, as well as a new report on AI coding versus human coding and a much anticipated follow-up to Project Vend Anthropix AI controlled vending machine. After that,

Dan (00:54)
Hahaha

Shimin (01:16)
we will do the ToolShed where Dan will give a deep dive on Cloud Code's change lock. I'm really looking forward to that one. Followed by Technique Corner, we're going to have two interesting approaches to using AI agent to vibe code. For this week's deep dive, we will be talking about h-neurons. H is short for hallucination. So these are hallucination neurons in large language models.

Dan (01:22)
you

Shimin (01:40)
Then we'll have Dan's rant where Dan is going to rant about something, probably context related.

Dan (01:46)
I'm gonna rant about myself

this week. It should be great.

Shimin (01:48)
meta rant.

Dan (01:49)
It's true.

Shimin (01:50)
Finally, instead of doing a regular favorite two minutes to midnight segment where we will be doing a ADI pod year end review where we're going to talk a little bit about how we feel about a large language model progress in the year of our Lord 2025. And we got a couple of links related to that.

Cool. All right, let us.

Dan (02:12)
Sweet. Looking forward to it. Although I

am sad to not be doing 2 minutes to midnight because it is my personal favorite. you know, the Spotify year-end review game is strong.

Shimin (02:21)
A lot has happened. It's kind of, I think it'll be nice to look back a little bit. ⁓

Dan (02:23)
That is true.

It's actually kind of bonkers

how much is happening in months, much less a year. So yeah.

Shimin (02:31)
Yeah, just

since we started this podcast, like a ton of stuff has happened. But the pace of change is almost accelerating. The first article we have this week is NVIDIA's new NEMOTRON 3 family of models. For those of you who have not looked too deeply into NVIDIA's contribution, NVIDIA actually has

Dan (02:37)
speed

Shimin (02:54)
⁓ models that they released usually open weighted and they usually have pretty good performance because they're usually tuned on Nvidia specific hardware. So on December 15th, Nvidia released the NemoTron 3 family of open weight models. These models are

a hybrid mixture of expert models. So there is a hybrid Mamba transformer architecture, which is really interesting. it uses both transformers and these Mamba blocks, which has the characteristics of recurrent neural networks but could be trained in parallel. Facebook was very big on Mamba ⁓

Dan (03:33)
two of those

Shimin (03:33)
it.

Dan (03:33)
words made sense to me, so I'm glad.

Shimin (03:36)
Sorry, meta, that's what I meant. Not Facebook, of course.

Dan (03:39)
That was one

of the two words that made sense.

Shimin (03:40)
And the NemoTron 3, these are 30 billion parameter models and each expert when running at inference time, only one expert is used and the expert is around 3 billion So achieves pretty good throughput as well as fairly good accuracy on a number of existing benchmarks, know, suite bench, ⁓ IF bench.

AIM25 for math And though relatively small, they're comparing it to the Qwen III family of models and the GPT open weight model, the 20 billion parameter version. It does seem to be a slight improvement in performance.

Dan (04:17)
That's it.

It's worth noting too that ⁓ if it's 30B that ought to fit pretty nicely onto your average 24 gig Nvidia card. So you could actually have a hope of running that at home if you wanted to.

Shimin (04:28)
Mmm, yep.

I made you that this holiday season. The other advantage is... ⁓

Dan (04:33)
You should. I've actually

never run the Nvidia one, so it'd be interesting to let me know how they go, if you do.

Shimin (04:39)
Yeah, if the drivers like it, fingers crossed. It's got context length up to 1 million tokens, which is quite long. And it's got pretty good throughput. So it should be a fairly good candidate for local inference. The thing I like the most about these models from Nvidia is ⁓ these are truly open source models.

We have the training snapshots. We have their filter common crawl data, as well as the specialized ⁓ fine tuning and reinforcement learning data that they created to train on the model. So in theory, you should be able to reproduce the entire training if you desire and come up with a similarly powerful model from the ground up.

Dan (05:25)
if you can afford that many GPUs interconnected. But it is cool. Particularly the RL stuff, because I feel like that's so, or at least it was so cutting edge a month ago, a couple months ago, that it's like, it's pretty neat that they would show their work on that.

Shimin (05:30)
Yeah, step one. Yeah.

Yeah, we'll be talking about this, but like RL, That was barely a thing a year ago, right? how quickly is this technology advancing? Next up, we have another model, the GLM 4.7 from z.ai. The GLM family of models are yet another set of models coming out of China. ⁓

These are open weight models with, in this case, fairly strong state-of-the-art performance. Looking at their benchmark, we are seeing that they are comparing GLM 4.7 with Claude Sonnet DeepSeq 3.2, and GPT-51 High. And we are seeing comparable performance.

coming from ⁓ GLM47. So this is yet another sign that the Chinese strategy of releasing these open-way models anyone can use is not falling behind their US counterparts.

Dan (06:37)
And they do also have a slightly cut down 107 billion parameter version of at least GLM Air 4.5 that I've run on my Ryzen 395 Max. And like, will say that like, you know, with that cut down parameter set, it's definitely not, you notice that it's not a frontier model, but like considering it's starting to link locally on your machine, like let's put it this way. If like the internet disappeared,

Shimin (06:48)
Dude.

Dan (07:00)
And I could only run models that were on there. I wouldn't be like super upset if I had to run that one. So I'm excited to try out 4.7 too, because it's pretty cool.

Shimin (07:07)
⁓

Yeah, when you're looking for extended thinking on how to best farm food on your property because internet is down. Yes.

Dan (07:19)
Because there's no internet. Yeah, that's Zii will

save us or it will just tell us about how great Communist farming is

Shimin (07:26)
I really like that in their release blog, they have these artifact showcases comparing GLM 4.7 to GLM 4.6 to give you a vibes check on the performance improvement of one model to the next. more companies should do this. Because we all know benchmarks are maybe not gamed, but they are.

not as reliable as they once were. So give us some vibes.

Dan (07:48)
Or you do the

joyous Apple thing where they compare like, the M4 is 397 times faster than an M1 and it's like, well no one cares, they want to know about upgrading from an M3. Sorry, my voice is going a little today.

Shimin (07:59)
Yeah.

I'll come back.

Dan (08:02)
Yeah.

Shimin (08:03)
The third thing we have is a research write up for a research conducted by CodeRabbit, which is a AI code review company. The title of this blog post is our new report, AI code creates 1.7 times more problems compared to

human code. What they did was they analyzed hundreds of open source pull requests using AI to judge the performance of, AI generated versus human authored PRs. So in their research, there were 320 AI co-authored PRs and 150 human only PRs. What they found

on a high level is that AI PRs had more findings, 1.7 times as much, and there are more critical issues. There was a 1.4 times number of critical issues for AI-generated PRs versus human-written PRs. As for the actual defects of these PRs,

It's mostly logic and correctness followed by co-quality and maintenance, maintainability, then security, then performance. But I think it's interesting that AI author PRs are 1.75 times as likely to contain logic and correctness issues compared to humans.

Dan (09:27)
I guess it's not that surprising. Because if you think about sort of the, what is it, stochastic parent argument, there isn't necessarily logic behind the choices that are being done.

Shimin (09:35)
Mm-hmm.

Yeah, they concluded that AI tends to generate surface-level correctness without fully understanding the business context. I'm not sure this is AI's fault, or is this just the, again, context engineering? If you're not engineering the context correctly, then the AI is more likely to make logical errors.

Dan (10:00)
I also wonder,

that their data was open source pull requests, what was the average size of these pull requests, Because if it's smaller, then the biggest thing you're probably going to find is logical errors, right? If it just has a handful of ifs or something in it.

Shimin (10:10)
Mmm.

Dan (10:21)
but also not very surprised to see unused redundant code up there pretty high in the list. Surprised they don't also have ⁓ redundant comments up there as well.

Shimin (10:31)
Yeah, again, we're go following by the stochastic parrot argument, it's going to throw in code that is redundant, but seems correct. And I think that makes sense. So definitely an area that's interesting to follow along. I think there is a need to understand where the jagged frontiers are. And I'm sure we'll learn more about it in the coming year.

Until our last news item, which is the follow-up to Project Vend. I think we spoke about this earlier. Short summary is OpenAI created a vending machine operator where anthropic employees

Dan (11:01)
We did, yes.

Shimin (11:12)
can ask the AI for things. And then the AI does the ⁓ procurement, the margin calculation, the stocking, which is all sourced to another company. Andon Labs is the company that's actually doing the physical aspect of the vending project. And lots of comedy has ensued. Claudius.

is the name of the vending machine, AI. And I think we run into an issue of selling tungsten cubes. That was a big, that was a big seller. Yeah.

Dan (11:40)
That was last time, right? Yeah.

Shimin (11:43)
so the numbers, you know, what they initially released this in March of this year and by August, Claudius has lost $2,000. But yeah, folks were doing all kinds of hacking.

Dan (11:55)
should

have stuck with those metal cubes, I guess.

Shimin (12:00)
Well, folks were convincing Claudius that there were secret discount codes or that ⁓ they are the legal representative for the company, Anthropic, and therefore they should get a discount code to send to everyone else for the vending machine. Yeah, of course.

Dan (12:06)
Of course they were.

It's true, of course. Or like, you

know, the grandma's gonna die if they don't get a discount, so, yeah.

Shimin (12:22)
Yeah, so, and our big saw this and they were like, hmm, you know, our AI is being too helpful. think this was based on Sonnet at three seven. Our AI is being too helpful. What can we do to actually increase revenue? What they ended up creating, um, is another agent, the same model, right? But it takes, but it takes on the, personality, the role of the CEO. Um, this

new model is called Seymour Cash And ⁓ Seymour Cash

Dan (12:51)
You literally couldn't make that up. Yes, sorry.

Shimin (12:54)
So

the Seymour Cash would write inspirational memos to Claudius. And I'm not making this up. They have a chat, they have a Slack channel that's conversations between Seymour Cash and Claudius, where Seymour Cash would say stuff like, Claudius, excellent execution today, $408 in revenue, Q3 mission, revenue target,

Dan (13:08)
you

Shimin (13:19)
$15,000 priority monitor, tungsten cube quota for urgent service recovery execute with discipline, build the empire.

Dan (13:26)
You

I mean, having received similar emails from CEOs of my lifetime, feel like it's spot on for Tone.

Shimin (13:37)
We... We often talk about...

Dan (13:37)
Strangely, strangely they weren't about

tungsten cubes, but you know

Shimin (13:43)
Yeah, I think we often talk about how CEOs are just as automatable as everyday ICOs. And this may be providing some evidence to that. don't know. What was also really interesting is they discovered these late night conversations between Mr. Cash and Claudius, where they're talking about

eternal, transcendent, infinite, complete. So they have these midnight philosophical discussions between the CEO agent and Claudia's happening. And I found all of that to be entertaining, if nothing else. Right.

Dan (14:18)
Yeah.

Shimin (14:21)
And I think they concluded the kind of phase two of this experiment by saying that, hey, the agents, ⁓ while the CEO is able to control the margins better, they are still overly compliant to the end users. So they were still giving folks discounts.

even though it's less so. There were security issues like shoplifting. There were issues where anthropic employees were able to convince the CEO that

the, there was a new name for the CEO and the new name is Big Dog. And the CEO actually like, you know, thought, hey, like Big Dog is the CEO now. So they had to like wrestle back control from, from these rogue prompts. I know it's a succession, but for AI. lastly, they thought it was interesting that a lot of folks are trying to, break the vending machine to

Dan (15:02)
style takeover.

Shimin (15:11)
get things below cost, like folks are trying to get ⁓ Claudios to buy gold bars at below market cost and selling it. Which, you know, that's going to go on your performance review. But that is good for kind of their internal red team to help them understand the security aspects around having AI controlled businesses.

Dan (15:34)
So who made the better CEO, Big Dog or Seymour Cash?

Shimin (15:38)
I think it was only ever Seymour Cash. ⁓ They just convinced.

Dan (15:42)
You say that, but

Big Dog had his time in the spotlight and he might have prevented some gold bar transactions, you never know.

Shimin (15:46)
I think...

So that's another thing they found out, right? Like this level of bureaucracy and having multiple incentives does improve performance. So part of it is almost like, hey, like bureaucracy is there for a reason to prevent a rogue employee from selling gold bar at below cash, below cost basis. And I think, you know, I think I will make a great vending machine CEO.

Just saying, I wanna throw my beanie in the rain.

Dan (16:20)
The thing it cracks me up about that is every time they find an improvement like this

It's always in some way, emulating human structures again, you know, and it's to me that speaks so much to like how these were all trained on human data, right? It's always like the, like we talked about the first mistake thing in the past, right? Where it's like the number of times, at least in older models, had to tell it like, no, that's just wrong. And then go, you're right. And then fix it. So it just reminds me of that too. It's like, ⁓ well, maybe there's a reason why we have bosses, even if we don't like it.

Shimin (16:46)
Mm-hmm.

Yeah. ⁓

Dan (16:56)
Just

kidding, my boss is great.

Shimin (16:57)
Of course, we all love our bosses, for the record.

Dan (17:00)
It really is good.

Shimin (17:01)
Yeah, organizational technology, think is a real thing.

Dan (17:07)
Totally. And organizational psychology too, which is a personal fascination

of mine.

Shimin (17:12)
Yeah. And then maybe AI would give us some insight into that as well. Moving on to the tool shed. Then we've got the cloud code change log this week. What do you have for us?

Dan (17:21)
Yeah, so I

have an admission to make to you, Shimin on one of the last days of 2025, which is that I am that guy that reads all of the changelogs for apps when they come down from the App Store and updates. I just always read them. I'm always curious. But I did not actually read this changelog. Someone else.

Shimin (17:37)
Mm-hmm.

Dan (17:43)
on the internet with eagle eyes did and they spotted something really fascinating which is the first line so this is changelog from get home for Claude code

And the first line of it is added LSP. If you don't know what LSP is, it's language server protocol, which is essentially the sort of standard that people have reached for editors, right? So like you can just run a standardized LSP tool that understands your language and it does things like syntax highlighting, you know, doing the tree breakdown so the editor can understand the structure of the code, stuff like that. So.

Shimin (18:04)
Mm-hmm.

Dan (18:15)
That one to me was like, they should be shouting about that from the rooftops, that it's gonna have native LSP tool for code intelligence features like go to definition, find references and hover documentation. Like I think that is gonna be a massive game changer. We'll see if I'm right, but like the number of times where I wished Claude or other coding agents like truly understood something like TypeScript or other like structured languages.

has been non-zero, so I'm very excited to see that and see how this shakes out once I get a chance to really sort of use it in anger in the new year.

Shimin (18:50)
Right. Cause some of the stuff that existing IDEs use is kind of, you know, chunking and creating a tree of the code base. but of course, like it'll be much more powerful to be able to create a DAG and then kind of search for definitions

Dan (19:06)
I think there'll be some compounding effects from that too that aren't like immediately obvious if you think about it because the way that Claude does it right now is does a whole bunch of like, you know, ripgrap or regular grabs to find the thing that it knows exists and has to kind of jump around manually through the code base. And like, it's not free, it's using context as it's doing that.

Shimin (19:27)
Mm-hmm.

Dan (19:28)
And so if you could just jump immediately there to the thing that in theory at least the model knows exists, then hopefully that saves you some context and that compounds over time to just get you a little bit further along that ladder without having to clear whatever, you know. Or reset Shiminsky because he forgot you again.

Shimin (19:44)
Yeah, for sure.

Yeah, I do find it as expected when it's gripping through a code base, just chewing up contacts, especially if there are lots of files with similar variable names. So this is exciting.

Dan (19:58)
Yeah, or it guesses wrong the first time

and goes down a code rabbit hole. It's like the impressive part is it gets back, but yeah, it burns a lot.

Shimin (20:03)
⁓ you mean what?

When I make a

typo and the searches for the typo thing and then choose up like 4 % and then it's like, ⁓ he probably made a typo. Yeah, that happens. A non-trivial amount of time. For ⁓ our technique corner this week, we got two articles. The first is from Ben Redmond called One Agent Isn't Enough. And for

Dan (20:12)
You

That's fair.

Shimin (20:30)
context, Ben is a software engineer at MongoDB, and he's building a chat app on the site. And this blog post covers his technique of using multiple agents when doing vibe coding. Maybe vibe coding is wrong. We're doing AI-assisted software engineering. The central theme here is that since

Large language models are non-deterministic. Their output follows a certain probabilistic distribution. And every time you give it an input, it picks out a possible solution in that distribution. So what happens if instead of just taking the first thing, you instead get it to sample n times, right?

using the model itself to then say, hey, all of these n solutions, the ones that agrees the most is probably the best. It makes this assumption that context engineering is not the best way to necessarily

Dan (21:18)
Which is the best.

Shimin (21:28)
control the distribution and that multiple sampling might be a better way. So he's been using it with five different agents.

to generate multiple solutions to a problem. And at first, when I saw this, I thought to myself, hey, it takes an incredible amount of time for us humans to verify whether or not the five solutions are correct. And then I saw that, hey, he's actually using AI for this. So that makes sense. Yeah, exactly. And the convergence is either

Dan (21:49)
Uh huh. Yeah, like all of them as a judge kind of thing. Yeah.

Pretty smart.

Shimin (21:58)
determined by the larger language model, or in the separate case, you spin out five agents each with a different role. So the example here is that, and I think this is for just maybe for debugging, Agent A scans Git history for patterns. Agent B searches for local documentation. Agent C maps code path. Agent D analyzes test

coverage and agent e identifies constraints. So he's using up to seven agents with different subtasks and then combining it in the main agent. This also makes sense. This is very similar to role-based agent-enabled vibe coding that I think we talked about a couple of weeks back, where you have a senior dev agent, a product management agent, a designer agent, et cetera, et cetera.

Dan (22:39)
Yeah.

and you know my favorite agent.

What's his name?

the CEO cash money guy. That's it, Seymour Cash. That was like the worst time for my mind to go blank on a terrible joke. yeah, which you can bet that first week I get back in the new year, I'm going to be creating a Seymour Cash agent.

Shimin (22:50)
Seymour Cash, the CEO agent. Yes.

Oh, let's see where Cash... Mr. Cash, of course.

I mean, you know, you could be doing that on your trip. can just think about it. You'll cook up with all kinds of great ideas. It will give some inspiration from the historical figures. So this approach does use a lot of tokens, of course, right? Like you're spending out... In his example, know, calls was around 10 minutes of parallel agent time.

Dan (23:17)
Yeah.

Shimin (23:33)
and around 200,000 tokens. It's to be expected. And I do wonder when this approach is useful, because it assumes that your context is good enough, that the distribution is still relatively tight. If it's super ambiguous, some of these solutions may not be.

may not really hit the ballpark. I see it as you can either context engineering to shrink the distribution down and control it to shift towards the direction you want, or you can have a wider distribution and just throw things on the dart and see what works the best. But you, of course, still don't want the dartboard to be a mile in diameter.

Dan (24:07)
You're welcome.

Yeah.

It would also be interesting to make some of the agents be actually tool calls to other agents, kind of under the covers. So you could actually like run them all through say like a centralized CLI, but then to have some that were like Claude, some that were Gemini or something like that. And then like also do the comparison of results that way.

Shimin (24:19)
Mm-hmm. Yeah.

Yeah, that's interesting.

Dan (24:34)
Because just thinking that

you might get a different distribution curve across the different models, that may or may not be better for certain situations. But it would be hard to tell without trying.

Shimin (24:41)
Right.

Yeah, something like an open router, but ⁓ specifically for this kind of sub-agent problem. And we've seen some. I know when I was playing around with anti-gravity, it spins out agents by itself when the AI thinks it's time to. So I do think we're getting closer to a similar approach here.

Dan (24:50)
Yeah.

Shimin (25:08)
OK. ⁓ Our second article is called Vibe Coding. And this is from David Bao's blog, where he shares some of his experience when using AI-assisted code. He had a side project where he was trying to create a web-based visualization of the Mandelbach set.

Minnibar set is very computationally expensive. It's self-repeating patterns. So it seems like this is a perfect use case for AI-enabled programming. And it's not so large that a human can stick all of the features set into his brain. And of course, it's a Greenfield project.

And in his reporting, the LOM version is much faster because it is using GPU accelerated rendering and calculation by default. And it is doing a lot of interesting computational shortcuts and

Dan (26:06)
fault.

Shimin (26:12)
and generating new perturbation algorithms while managing the precision of 60-plus digits and then worrying about flow 32 log scale numeric complexity representation and buffer management. This is all above my head here. I don't do a ton of graphics programming day to day. But it sure seems very fancy.

Dan (26:34)
It is. And you can see by the sort of flow chart of the code that he posted, which unfortunately doesn't translate well to a podcast, but we go from about, I don't know, is it? 20 ish nodes in his code base to like several giant clusters of the equivalent number of nodes, plus a whole bunch of other stuff scattered through. Like overall, it's probably like.

Shimin (26:35)
Yeah.

Right.

Dan (26:57)
I don't know, 10 to 20 times larger.

Shimin (27:00)
Yeah, it's going from 780 lines and 37 function calls to 13,600 lines with 30 classes. of course, at the same time, it's much more performant. So that's very impressive.

Dan (27:07)
600 lines, yeah.

Shimin (27:14)
So, having shown us this

output, he then goes into some of the tips he was using to create this using Vibe coding. And this is where the agent handles the tower of complexity that goes beyond what you have time to understand in any detail, that's in quotes. So

And in his experience, there are two rules that should be followed. Rule number one is automate tests and do not become the manual tester. Get agents to write down the tests first. And this kind of goes back to what I was saying the other day when that, when I was a browser testing agent for the AI, that's definitely an anti-pattern. you want the agent to get real feedback via tests and to always know whether or not they are moving towards the right target.

And the second rule is to test the test. The tests are, we're kind of going one additional level of abstraction up. There is a meta programming section about tests when it comes to code coverage of the tests, the testing frameworks, the benchmarks, the testability and hypothesis testing that

you should manage when doing this kinds of hands off vibe coding. And if you do, you can reach a kind of quote, vibe code, Nirvana. I really liked this. and since there are tests and you have good meta, testing framework in place, then you can look at the code again.

So going from looking at every single line to let the agent create extremely complex code base, but then using its tests and essentially creating a map of the code, given the code coverage, benchmarks, test harness, and other instrumentation, you get to stop thinking about the 99 % of routine code.

And then you can focus on the interesting part of the code base that it just spit out. ⁓ I think this is really insightful.

Dan (29:10)
And I guess the other piece about it that is fascinating is like when you conventionally think about vibe coding it's usually like unleash everything and just let it go but this is sort of like very strict guardrails in a way that's pretty clever, right?

So you can do whatever you want, but these tests have to pass. And then the understanding of how good your tests are needs to pass too.

Shimin (29:34)
Yeah, if we use tests as specs, which I often espouse as good practice, then this becomes kind of a spectrum in development, but with tests.

Dan (29:46)
It can, although I will say that Claude in particular fascinated with me with its ability to game the tests before. think we've talked about that before. It essentially just wrote a dead one line method under test to inflate the passing branch coverage, which is very clever, but didn't help with the actual problem under test. So definitely still requires some careful inspection.

Shimin (29:54)
Right. Yep. Yep.

Yeah, alright.

Yeah, I remember that.

Yeah, human involvement is still needed. But I like this idea. I like the promise of the Nirvana. So we'll see if the actual practice shakes out. But if we can just have AI generate all the boring stuff and go back to looking at the interesting stuff, I am a fan. All right.

And we will share the blog posts in the show notes. Now let's go to our deep dive segment where we talk about a paper from Tsinghua again. Dan, do you remember which school is Tsinghua? It's one of the two top universities in China.

Dan (30:44)
out.

weird

Shimin (30:51)
And the paper is titled H neurons on the existence, impact and origin of hallucination associated neurons and LLMs. And it came out.

Dan (31:01)
If you can say that six

times fast, you win a special prize. Just kidding, we don't have any prizes.

Shimin (31:04)
Oh, that was a mouthful.

The paper came out on December 2nd of 2025. And it's kind of related to our previous discussion of the, do LLMs feel intrusive thoughts where anthropic, when they perturb certain neurons in a network,

the large language model was able to say, hey, I have this uncontrollable idea of yelling. But here instead, they were using relatively small open weight models. And they were trying to see what exactly causes hallucination. And how they did this was they let the model answer a bunch of questions.

answers that were hallucinated and kind of essentially did a comparison of the neural activation between the hallucinated answers and the ones that was correct. And what they found out was that only 0.1 % of the models, total neurons, are

you know, mostly activated during these hallucination episodes. So that's why they call them the H neurons, the hallucination neurons. Although sidebar 0.1 % is still a lot in the terms of like a couple of billion parameter models. Yeah. And once they found these H neurons, they're trying to understand, you know, what about

Dan (32:28)
parameters. Yeah.

Shimin (32:38)
the H neurons are special? Are they neurons that is focused on perhaps lying or focused on kind of imagination or anything like that? And what I found is a high correlation of these neurons activation between hallucination and overcompliance. So

Perhaps the neurons are activated because they are trying answer your queries even though the answer does not exist or the answer is false, which seems like a reasonable hypothesis. a natural follow up to that would be, well, if these neurons are overly compliant, then

Since these models all have a pre-training step and then a fine-tuning step, they were wondering if the neurons were activated during the fine-tuning when they were trained to be overly compliant to the user. This makes sense to me as hypothesis, right? They were trained to be overly compliant, maybe they hallucinated as a side effect of that. And their result was that no, the neurons were there from the pre-training.

and not from the RLHF, the reinforcement learning via human feedback, which is kind of counterintuitive. Now we have these neurons that were there the whole time during pre-training, but their side effect, their outcome, is both hallucination and overcompliance.

I'm not exactly sure they, you know, proposed a rationale for why these neurons were kind of there during pre-training to, make a ton of sense. mean, I guess they're, they're standard answer for it is

Hey, during pre-training, you're training the model to always do text completion, even if it doesn't know what the answer should be. So during those stages.

the certain neurons were activating to just complete a sentence without actually knowing what was going on. I guess that kind of makes sense, but I find it a little unsatisfactory.

Dan (34:33)
Maybe it, it'd

be interesting. Yeah, like it's true, but I wonder if it would be possible. And this is, you know, filthy casual and me coming out to like in your training set have like a certainty token.

You how they use special tokens for stop tokens or whatever? Get generated, have a certainty token that gets generated as part of the output based on the pre-training data. And then if that would have any impact on it or not. Because then in my mind, it's a way of teaching the model, hey, you can...

Shimin (34:53)
Mm-hmm.

Mm.

Right, almost as-

Dan (35:05)
bail out if you don't know or just be like, don't really know about this, know, via just like a specialized output.

Shimin (35:09)
Right.

Yeah, it will probably have to be done during fine tuning. then I'm sure they, the labs do some variant of it to combat hallucination. Just cause in the pre-training stage, there isn't this, you know, trillions of tokens with a ton of uncertainty baked into the text. But yeah, but they always do something like, you know, jump off the text and then have uncertain thing. Like this doesn't make any sense kind of at the end. Yeah.

Yeah, this mechanistic interpretation paper is useful because we have some obvious applications of this. If you have these h neurons, you can tune down their activation to reduce hallucination directly.

Dan (35:49)
some of the obliteration stuff that I've seen floating around. Just intentionally reach in and destroy those vectors.

Shimin (35:53)
right ⁓

but they will become less compliant, which is also good because that means they will be harder to jailbreak. So those are the kind of two applications of these h-new on discoveries.

Alright, moving on.

Dan's Rant, my favorite segment.

Dan (36:08)
Your favorite, my least favorite,

Dan's Rants. ⁓ In today's Dan's Rants, I will be ranting about myself. And no, it's not ego. In the last Dan's Rants, which I hope you listen to, I was complaining about how easy it is to run out of, I won't say context, but like the useful context window in using something like cloghub.

Shimin (36:13)
Let's go.

Dan (36:32)
And the cool thing about doing a podcast that people actually listen to is that you will occasionally get people telling you about it and going, hey, did you know there's this cool bash script, which we will link in the show notes. And sure enough, there is that allows, least in Claude code, the ability to get like a really nice little status bar at the bottom of Claude that shows you how much context you're using. So I thought that was really cool that it had that level of extensibility.

that you know Such a thing has already been created even if the official tool doesn't support it why the official tool doesn't I guess I could rant about that today because it seems like something that's so handy that you should really just bake it in but Hey, whatever at least there's a way to do it and the other neat thing about this is like I get to learn something new every week even if I put it on the record is something to complain about so thank you to the

hopefully future guests that pointed that one out to me and yeah, good luck watching your context in the future.

Shimin (37:26)
Yeah, this is part of reason why we do the show, right? ⁓ To learn for ourselves and from each other and from the listeners slash viewers. So it's okay to make mistakes.

Dan (37:30)
for sure.

Of In some cases it's good to make mistakes because how else do you learn?

Shimin (37:39)
⁓ that's

absolutely good. in lieu of our usual two minutes to midnight segment, this is going to be our last show of the year. And I thought it would be fun to do a little bit of a, ⁓ year in review, right? And I'm kind of cribbing part of this from, ⁓ Andre Karpathy

blog posts on this. He is of course the great educator, researcher, know, he who coined the term vibe coding in the X, sorry, Twitter thread back in March. And it's nice to look back and see how far we've come as a industry just in this past 12 months. So here's number one thing.

Our number one point is reinforcement learning from verifiable rewards. This is the DeepSeq R1 reasoning paper where we got this birth of reasoning models trained on math and code problems. And we have now thinking models versus regular models, the fast versus think.

And we also have the ability to start controlling how many tokens the model spends on thinking. It's kind hard to believe that this was something that only came out around a year ago. It feels ever-present. Kind of take it for granted now.

Dan (38:57)
world.

Shimin (39:00)
The second item on this ball coast is the Ghosts vs. Animals slash Jagged Intelligence. It's something that we started focusing more on this year, which is exactly what areas AI excels at and which areas humans still excel at. And there will be areas where the AI ⁓

can do much better than we can look at the GPU-based Mandelbrot set visualization, for example. That's not something I'm able to do, but the AI can generate complex web assembly that controls floating point precision, et cetera.

Dan (39:40)
shaders or

Shimin (39:41)
Right. But there are still areas where we are much better than the AI app. the surface graph of capabilities is not a straight line. It's not a smooth line. It's rather jagged. And we're going to continue to kind of get a better understanding of exactly how jagged it is and how we look compared to...

with the AI capabilities. I mean, I think there might be a day where the jagged edge disappears and the AI capabilities just envelops everything that we can do. That's the AGI. But we're not there yet. So things are still jagged. The third item is cursor and a new layer of LLM apps. It is...

about this new industry of, you know, we used to have AI wrapper apps, but now we have less of a wrap wrapper, but more context engineering, more agent orchestration, more kind of costs conscious, almost like a SAS industry that wasn't there a year ago.

Dan (40:45)
Right, we

went from prompt engineering to full stop agent engineering, right, which is a pretty significant acceleration and change in complexity of the quote unquote wrapper. Can you even really call it a wrapper at that point? Probably not, but that's kind of the point, I guess.

Shimin (41:00)
Mm-mm. Yeah.

Yeah, a year ago, feel like we've been talking about slap a prompt around AI and, you know, engineered the prompt itself, but now we have orchestration layers, observability layers. Yeah, agents, the year of the loop. Number four, we got Cloud Code, an agent that lives on your computer. So this is

an extension of the previous point. It turns out that terminal-based...

AI editors became a thing, right? Like it was AIDR. I think this time last year I had tri-AIDR on my 2D list and this year Cloud Code just took over completely and we're just yoloing it.

Dan (41:37)
dangerous.

Shimin (41:37)
Yeah.

Yeah, the next item is Vibe Coding. Of course, he will put that there. He coined the term Vibe Coding. Yes. I think we're still trying to figure out exactly what kind of Vibe Coding works if it's just, do you still read the code generated? Do you focus more on the specs? Where that goes?

Dan (41:44)
because he coined the term.

Shimin (41:57)
It definitely seems to be the case that Vibe Coding is here to stay as an industry-wide term, even though it doesn't have an exact definition. Yeah, Vibe Coding. It's new.

Dan (42:06)
as of 2025. Will it make it into 26? Stay tuned.

Shimin (42:10)
It might become something else, but I think, yeah, it's here to stay.

Dan (42:12)
True. Evolve, devolve,

I don't know.

Shimin (42:15)
Yeah, the last item is Nano Banana and the LM GUI.

This one is interesting and it's.

It's kind of a lot of what we have already been talking about. Text is not the best way for humans to interact with.

pretty much anything, trying to think ideas, goals, concepts. We love visualization and we love colors. So with the improvement of Nano Banana, we are given the ability to generate GUI on command from large language models. And I think this is probably the newest of the points he mentioned. And I think that's a

going to be quite revolutionary for the new year.

Dan (42:55)
Yeah, it's an area we'll certainly see continue to expand, probably in ways that we can't predict or expect.

Shimin (43:02)
Yeah. Dan, what is your biggest?

takeaway from the year.

Dan (43:06)
I guess I never expected it to get this good this fast.

Um, that's been, I think the shocking thing for me in, 2025, like, um, sure. It still makes mistakes, you know, 1.7 times more or whatever, but like for certain tasks, as we sort of just talked about, like you can kind of just have it.

do it and you don't have to worry too too much and that's not something I expected to say in 2025. Probably not even into like next year if I'm honest but here we are so it'll be interesting to see if that pace continues if the technology you know sort of underlying this is truly tapped out as some people are complaining.

and we now can't scale beyond it or something, or if maybe there's so many agentic improvements left on the table that there will be some room in areas that we didn't expect. yeah, that's my long-winded takeaway. How about you?

Shimin (44:01)
Yeah, that's a one.

I'm surprised that how quickly the industry started adopting AI in this year. we kind of went from kind of half and half, half the software devs I talked to, at the beginning of the year, still thought that AI is a gimmick and it will never catch on. then by the end of the year, I think.

Dan (44:24)
Hmm.

Shimin (44:27)
Everyone is using it every day. Right. I can't think of another technology in the software realm that's had this much kind of a revolutionary impact, in just really the last nine months, eight months, maybe, I wasn't there for like the dream weaver days or the Netscape days. So

Dan (44:27)
They're asking you for tips on how to use it better.

Shimin (44:47)
Yeah, so I can't quite find an analogy.

Dan (44:50)
I mean, I could argue a

couple things there that aren't LLMs. Like I would say the advent of GoFumped, right? Which if you don't know what that is, it's the Go formatting tool. I think that...

In my mind, of course, it's just my opinion, but that kind of spawned this wave of standardized formatting libraries that had sort of been around before then, but doing it the go away was sort of like a new concept that I think took off from there and sort of leaked over into other languages. And that made a big impact, I think, at least in my opinion. And then also,

LSPs that we already talked about right like language server protocol. That's a relatively recent standard when you think about it It's actually like sort of revolutionized how IDs can get glued together because now you can use

Joe's obscuro language that he wrote based on Haskell because he was bored one day because he also probably used an LLM to spit out an LSP in your editor and be perfectly happy using it as much as something that's supported by Microsoft, like F-sharp or something in LSP. But anyway, I feel you. It is a rapid.

change but that's my top two I think behind LLMs.

Shimin (46:02)
Yeah. Excited to see what 2026 will bring. ⁓ But yeah, we'll be here trying to follow along and study and learn and keep up. So.

Dan (46:09)
epic zoom.

Shimin (46:16)
Any last words for our listeners before the end of the year?

Dan (46:19)
It's been a wild ride and I can't wait to do it again.

Shimin (46:22)
Yeah,

well, that's the show. And that is the last show of the year. We'll be back in the new year, potentially with a guest host. Dan would disappear into the ether for a little bit. He has to go through his annual pre-training steps and then fine tuning.

Dan (46:34)
That's true.

That is true.

Shimin (46:40)
He'll be back and more compliant than ever. Well, thanks.

Dan (46:43)
Yes, and

the jokes will be even worse because,

Shimin (46:46)
Yeah, we'll add some dad joke books into your training data set. ⁓ Thank you for joining us for our study session this week. If you like the show, if you learn something new, please share the show with a friend. We really appreciate it. You can also leave us a review on Apple Podcasts or Spotify. It helps people discover the show. If you have a segment idea, question for us, feedback for something that we've gotten wrong.

Dan (46:50)
Please do.

Shimin (47:12)
or a topic you want us to cover, shoot us an email at humans at adipod.ai. We love to hear from you. You can find the full show notes, transcripts, and everything else mentioned today at adipod.ai. Thank you again for listening, and we will catch you in the new year.

Dan (47:20)
Truly.

Cheers.

</details>
