---
episode: "3"
title: "Claude Opus 4.5, Olmo 3, and a Paper on Diffusion + Auto Regression"
date: "2025-11-28"
slug: "3-claude-opus-4-5-olmo-3-and-a-paper-on-diffusion-auto-regression"
description: "In this episode of Artificial Developer Intelligence, hosts Shimin and Dan explore the latest advancements in AI models, including the release of Claude Opus 4.5 and Gemini 3. They discuss the implications of these models on software engineering, the rise of open-source models like Olmo 3, and the enhancements in the Claude Developer Platform. The conversation also delves into the challenges of relying on AI for coding tasks, the potential pitfalls of the AI bubble, and the future of written exams in the age of AI."
keywords: "Claude Opus 4.5, GPT 5.1, Olmo 3, open-flow models, Nano Banana Pro, MCP context, tool search, diffusion-autoregression, SSRL, self-search, test coverage, AI bubble, Thinking Machines"
appleUrl: "https://podcasts.apple.com/podcast/artificial-developer-intelligence/id1857109105"
spotifyUrl: "https://open.spotify.com/show/4eDLlGoktxMngPNq9aGqLX"
overcastUrl: "https://overcast.fm/itunes1857109105"
pocketCastsUrl: "https://pca.st/itunes/1857109105"
amazonUrl: "https://music.amazon.com/podcasts/da06d4c3-ecf6-498f-abe3-4d3b00026bf2"
transistorId: "9d8ec5ad"
youtubeId: "VAqYyKyolxc"
---

In this episode of Artificial Developer Intelligence, hosts Shimin and Dan explore the latest advancements in AI models, including the release of Claude Opus 4.5 and Gemini 3. They discuss the implications of these models on software engineering, the rise of open-source models like Olmo 3, and the enhancements in the Claude Developer Platform. The conversation also delves into the challenges of relying on AI for coding tasks, the potential pitfalls of the AI bubble, and the future of written exams in the age of AI.

## Takeaways

- Claude Opus 4.5 setting benchmarks, enhance usability and reduce token consumption.
- The introduction of open-source models like Olmo 3 is a significant development in AI.
- The future of written exams may be challenged by AI's ability to generate human-like responses.
- Relying too heavily on AI can lead to a lack of critical thinking and problem-solving skills.
- The AI bubble is at 25s to midnight
- Recent research suggests that AI models can improve their performance through emulating query based search.
- The importance of prompt engineering in AI interactions is highlighted.

## Resources Mentioned

- [Introducing Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)
- [Build with Nano Banana Pro, our Gemini 3 Pro Image model](https://blog.google/technology/developers/gemini-3-pro-image-developers/)
- [Andrej Karpathy's Post about Nano Banana Pro](https://x.com/karpathy/status/1992655330002817095)
- [Olmo 3: Charting a path through the model flow to lead open-source AI](https://allenai.org/blog/olmo3)
- [Introducing advanced tool use on the Claude Developer Platform](https://www.anthropic.com/engineering/advanced-tool-use)
- [TiDAR: Think in Diffusion, Talk in Autoregression](https://arxiv.org/abs/2511.08923)
- [SSRL: SELF-SEARCH REINFORCEMENT LEARNING](https://arxiv.org/pdf/2508.10874)
- [Mira Murati's Thinking Machines seeks $50 billion valuation in funding talks, Bloomberg News reports](https://www.reuters.com/technology/mira-muratis-thinking-machines-seeks-50-billion-valuation-funding-talks-2025-11-13/)
- [Boom, bubble, bust, boom. Why should AI be different?](https://crazystupidtech.com/2025/11/21/boom-bubble-bust-boom-why-should-ai-be-different/)
- [Nvidia didn’t save the market. What’s next for the AI trade?](https://finance.yahoo.com/news/nvidia-didn-t-save-market-140007853.html)

## Chapters

- (00:00) - Introduction to Artificial Developer Intelligence
- (01:25) - Claude Opus 4.5
- (07:02) - Exploring Gemini 3 and Image Models
- (11:24) - Olmo 3 and The Rise of Open Flow Models
- (15:46) - Innovations in AI Tools and Platforms
- (19:33) - Research Insights: Diffusion and Auto-Regression Models
- (23:39) - Advancements in AI Output Efficiency
- (25:45) - Exploring Self Search Reinforcement Learning
- (27:48) - The Dilemma of Language Models
- (30:11) - Prompt Engineering and Search Integration
- (32:55) - Dan's Rants on AI Limitations
- (38:17) - 2 Minutes to Midnight
- (46:41) - Outro


## Transcript

<details>
<summary>Show full transcript</summary>

Shimin (00:10)
Hello, and welcome to Artificial Developer Intelligence, a podcast where two software engineers who are AI filthy casuals navigate the ever-changing AI enabled software engineering landscape. I'm Shemin Zhang, a software developer, and with me today is my co-host. He knows everything from his training data. All you gotta do is ask him to search for them nicely. Dan Lasky, Dan, what are you thinking about today?

Dan (00:35)
⁓ How many eggs I can fit into a basket?

Shimin (00:38)
You have to search for it multiple times and then get a majority vote.

Well.

Dan (00:42)
or write

some Python code.

And on deck today, we have our news treadmill where we're going to be going over yet more exciting model announcements. So can't wait to dig in there.

Shimin (00:52)
So many models. After that, we will be talking about the tool shed where we will cover some new Claude developer platform tools for its agents.

Dan (01:01)
next we'll be jumping into our deep dive where we look at some technical articles that one of the two of us understands.

Shimin (01:07)
After that, we have Dan's rant, a two-minute segment where Dan rants about something. What could it be this week?

Dan (01:14)
I promise you it'll be a bad one. Good one? Bad one? I don't know. That's part of the fun. And then finally, we have two minutes to midnight, where we figure out how close are we to the AI bubble bursting.

Shimin (01:25)
Well, let's get started. ⁓ Earlier this week, Anthropic released a Claude Opus 4.5, which is an upgrade of the old Opus 4.1, I believe. It is supposedly more intelligent, more efficient, and is the best model in the world for doing cognitive heavy tasks. On our favorite benchmark, the software engineering

SWE bench verified is scored 80.9 % beating even the Gemini 3 Pro at a mere 76.2%. I actually honestly haven't had much chance to use it yet other than I use it earlier today for some web UI tasks. I didn't notice a huge amount difference, but I think this is more of a coding centric.

model.

Dan (02:24)
I have

not used it for coding yet either, because I only have the pro plan for Claude I don't have the fancy one. ⁓ And at work, we don't have it yet on our allowed list. So hopefully that's coming soon. But ⁓ until then, I probably won't get a chance to really test it in depth. Although I think also, they also, part of the same announcement, said that the prices were going down on some of the other models too, I believe. So maybe I'll get to use it more than I might have hoped.

Shimin (02:30)
you

Yeah, I think the price has gone down and it's also available very wide compared to its usual kind of step introduction. Other than being better at logical tasks, the Claude Opus 4.5 is also...

introduced as being safer than its competitors. I think Anthropic has always been perhaps more heavily focused on AI safety than its competitors. I think that's their selling point. As part of this new models intro, ⁓ there's a chart here where it shows the various Anthropic models.

score when it comes to prompt injection and

having otherwise concerning behavior. And according to this chart, it is less susceptible to prompt injection style attacks, which I thought was also interesting. We still need a way for actual user-based vibes, but. ⁓

Dan (03:53)
As always. ⁓

Shimin (03:54)
Something to

look forward to in the next week or two. What is also really interesting is, according to OpenAI, it had a side-by-side comparison of Sonnet 4.5 versus Opus 4.5. And in their demo environment, where both agents were tasked to solve a puzzle, the Opus 4.5 escape room, yes.

Dan (04:17)
an escape room, specifically it looks like, escape

room challenge.

Shimin (04:22)
⁓ where they have to solve six locks before escaping. Opus used significantly fewer tokens. So even though both models were able to solve the entire tasks, Opus was much more efficient and therefore cheaper to run. And the one that probably most interests us when it comes to the eval of the model,

is Anthropic has

what they called a notoriously difficult take-home exam for their engineering candidates. Opus 4.5 did better in this two-hour take-home test than any human candidate ever.

So that begs the question, is Opus... How much are they gonna pay? Opus 4.5 to...

Dan (05:07)
they hire it? ⁓

I do always find it funny. Like, I don't know if you use the Claude mobile apps, but the release notes, like no one ever reads the release notes, but I'm the crazy person that reads the release notes on all iOS apps. So if you write an iOS app and you're listening to this podcast, I'm reading your notes if I'm using your app anyway. And, they always sign it as Claude, which kind of cracks me up. And like for the longest time, I'm like, yeah, Claude's not really doing that, but maybe he is. Maybe he works there now.

Shimin (05:21)
Mm-hmm.

Somebody is reading them, yeah.

Maybe Claude has a pension plan for Anthropic We can only hope.

Dan (05:51)
They just bam in ⁓ private stock.

Shimin (05:55)
Yeah, Opus

Dan (05:56)
It's a circular

payment deal, We'll get into that later.

Shimin (05:59)
We're all getting into that, yes.

speaking of change logs, ⁓ now Claude Code is available as part of the desktop app. There is a new code mode you can switch to, where you can have out of the box GUI for Claude Code. Yeah, it's pretty cool. I think it's very exciting. We had so many blockbuster models being released so shortly after each other. mean, we're not going to talk about those, but ⁓ OpenAI's

Dan (06:14)
Nice.

Shimin (06:27)
GPT 5.1 also came out in between last week and this week. So there's no shortage of new things to try. Little overwhelming actually.

Dan (06:36)
Yeah, it's like we're getting to have model releases and it seems like we're not to be outdone. Here's ours. Okay. But it's pretty cool. And it's definitely, it's definitely gotten me to try to like, given how good the benchmarks were on Gemini that we talked about last week, I was just curious about it. So I started playing around with it a little bit. ⁓ and so like, that's been the one cool outcome of all this for me personally is like, I've really just expanded my model horizons.

Shimin (06:43)
Yeah. Everyone's trying to beat it.

Dan (07:05)
in the past. ⁓

Shimin (07:05)
Model Horizon talk.

Yeah, speaking of Gemini and Gemini 3 in particular, ⁓ Gemini 3's image model, what they're calling Nano Banana Pro also came out in between last week and this week. This is the updated version of Nano Banana. is touted as having higher fidelity and control.

You have more control over the resolution and size of your images. And it is linked to.

web searches in real time, along with the ability to generate text very consistently, something that a lot of older image models really struggle with. ⁓

Dan (07:51)
Particularly B's and R's it seems like.

Shimin (07:53)
Yes. So for one thing, what you could do is use Nano Banana Pro to conduct web search and take the output of the web search and generate a infographic from it. That is one use case that I think really sets Nano Banana Pro ⁓ apart from its competitors. Just the ability to have clear text generated in the image. So.

Dan (08:17)
Yeah, it's

definitely an area that could use some improvement generally. Not that I do a ton of image gen stuff compared to code ⁓ generation, but the times that I've messed around with it, it's been like, ooh, yeah, OK. We mastered the number of fingers, but letters are still a little challenging.

Shimin (08:36)
not just letters, it could do interesting font stacks. And for example, it could generate graphic novels. ⁓ As one of its demo app is a ⁓ Google Studio applet called Infinite Heroes, where you can generate a comic book of a specific style using ⁓ two character or two persons images. So.

Yeah, so I sent one over, I played around with it over the weekend and I sent over to Dan. And Dan, what do you think? How are we as action detective?

Dan (09:06)
I was pretty impressed. mean, you only sent me two panels, so I don't know what the plot was or anything, but like, it really got, it captured my essence, let's put it that way. Definitely drive super aggressively and have like, ⁓ just absolutely white-knuckled grip on the steering wheel while I'm doing so, so, you know.

Shimin (09:26)
I have been in the vehicle with you. I agree. It captures. You're driving us very well.

Dan (09:28)
you ⁓

Shimin (09:32)
yeah. So another thing that this new ability to generate texts opens up is, Andre Karapathy had a thread that blew up over the, over the weekend, where he asked, ⁓ Nano Banana Pro to fill out some college level exams, ⁓ using pen and paper or pen quote pen and paper. Yeah. Emulating a handwritten answer.

Dan (09:51)
Emulating that style, yeah.

Shimin (09:57)
And it did a really good job, as far as I can tell. ⁓ I haven't taken chemistry 1, 2, 1, at least not in a long time. So I couldn't quite figure out if all the molecular structures are correct. ⁓ But assuming they are, I think the age of written exams may be over.

Dan (10:17)
Assuming you can somehow print it.

without anyone noticing and then handed it.

Shimin (10:22)
Yeah, we just need like a mechanical pen that can trace the output and like move your hand. ⁓

Dan (10:25)
Yeah.

Have you ever seen

those like full size plotters that they used to, yeah, so this is, I had been in some architectural offices in like the eighties, ⁓ because, people in my family were architects in, they used to have these like mechanical plotter. They may still have them for like really large format stuff that'll do drafting. And it was literally like a, an arm, like a horizontal arm. And, ⁓ it had a little grabber that could pick one of four pens.

And it would pick the pen and just like the paper would go in and out across the arm, then the arm would go left and right. And it would like literally just plot the thing.

Shimin (11:05)
I can see theory that's

not so different from like a CNC machine, right? You have an X axis and all that. Yeah. Yeah.

Dan (11:08)
Yeah, I mean, you're basically for drafting, you're just drawing pretty much straight lines, right, for a

plan. yeah, ⁓ just need to hook that up to Claude and ship it. Or, sorry, ⁓ everything's Claude to me now.

Shimin (11:17)
which we just need to bring it.

You're a Claude man.

Dan (11:24)
I know. There's stickers now. got real excited when I saw that.

Shimin (11:27)
Well, they had it. They had it as like a hidden feature in Claude Code when it first came out, right? was like, get us to send you a stick. I really should have been on the hype train from day one. But not all models are these closed source, of, closed weight models. I want to point out that this week was also the release of Olmo 3, a new

Dan (11:33)
Yep, slash tickerings.

Shimin (11:54)
state-of-the-art ⁓ open flow model released by the Allen Institute of AI right here in Seattle. I'm AI.

Dan (12:03)
What is an open

flow model?

Shimin (12:05)
So we know that, say, Claude is closed source. You have no access to the source code at all whatsoever. And then you have the open weighted models, where you have the model weights and you have the architecture. So you can use the model under MIT license or Apache or whatnot.

Dan (12:23)
You

can in theory run it on your own machine if you have a big enough box.

Shimin (12:27)
Right. ⁓

Open flow or what I really just consider to be truly, open models are models where you know the architecture of the model, you know the weights, but you also have access to the full training data. So you can in theory, reproduce the entire model from scratch if you were given the right hardware. And I think.

Dan (12:43)
⁓ okay.

Shimin (12:51)
⁓ it, is an area that I am really looking forward to, ⁓ being kind of industry default, right? So Olamo three is a seven and 32 billion parameter model released with its training data, along with, snapshots of various stages of training. So.

Along with the release of the model, they've also released their training data, which is called

DOMA 3, a 9.3 trillion token corpus ⁓ that was used to train the model. And I should add the model itself has a fairly state of the open art.

Dan (13:33)
comparable.

Shimin (13:33)
It's comparable

to say the Quinn 332, which is kind of the state of the art open weight model of a similar size. And of course, the closed source models are much bigger, but we don't have the training process for any of them. So not only do we have the pre-training data, we have

the pre-trained foundational model along with the instruction sets and the instruct the RL models and the thinking models. ⁓ And I think it's something that we should celebrate is no longer our models truly limited to the big players that we can actually also train our own models. ⁓

is I've been using their playground a little bit. And they also have a piece of technology called open trace, where when the model answers your question, you can open up the Olmo or trace to find out which source documents from its training model was being used to generate.

Dan (14:40)
⁓ wow.

Shimin (14:43)
the answer that spits out. So I know we sometimes talk about LLMs as being, you know, like a lossy compression of its underlying training data. So it'd really cool to see both the training data and what it's outputting.

Dan (14:44)
Huh, that's fascinating.

Mm-hmm.

It's fascinating too, because a lot of the current stuff is really essentially retrieval-augmented generation, meaning it's leveraging external sources to some degree to be smart in the way that like, mean, rarely do I ask Claude something and I'm not like, search for this thing, right? Because I don't necessarily care what it generates by itself. But ⁓ that is pretty fascinating, especially if you could like...

you know, show your work essentially, ⁓ which is pretty cool. Huh, I'll have to check that out. It's fascinating.

Shimin (15:29)
Yeah, so a

full transparency model. ⁓ Really great. It's local. ⁓ Hire me no ⁓ Anywho, moving on to the tool shed. This week we have an article from Anthropic again. ⁓ You know, I just think...

Dan (15:40)
You

They're not sponsoring us yet.

Shimin (15:52)
they write really cool blog posts, and they have more transparency. Yeah. So good job, Anthropic. The article is titled Introducing Events to Use on the Claude Developer Platform. So we have a lot of issues when it comes to MCPs. We've talked a lot about why do MCPs take up ⁓ so much context length, just loading the MCPs.

Dan (15:54)
They do, yeah, their blog is pretty great.

Shimin (16:16)
we also talk about how, maybe not explicitly on the podcast, but, ⁓ it is an issue where if we have a large amount of task, ⁓ that we are passing through an MCP, then every single other call in the same chat chain would contain that very large piece of text, essentially eating into your context for, for really no benefit. ⁓ and of course

any kind of intermediary data being generated by Claude would also be sent repeatedly, unless it's KV cached. But that's a different story. So ⁓ apparently, we're not the only ones complaining about this. Anthropic also sees this as a big issue. So they've introduced ⁓ the tool search tool, where the agent can use tool search to look for the right tool to use at a given time.

Here they talk about a typical five MCP server set up, you know, with GitHub 35 tools, Slack 11 tools, Sentry five tools, or Fauna five tools and Splunk two tools. That's 58 tools altogether. And that seems like a pretty typical MCP stack if you were doing some sort of a full stack web development. Just the 58 tools together.

were consuming around 55,000 tokens before the conversation even starts. And they really only have around, you know, 200,000 usable tokens for context length. ⁓ that's, ended up.

Dan (17:39)
And not

only that, but when you turn on that much MCP, the chances of it actually calling the most helpful tool drops precipitously, at in my experience as well.

Shimin (17:50)
Yeah, my Claude.md file is just lost in between the MCP tool calls. So with this new tool search tool, the agent is able to look for the tools when they need it and also to call it programmatically so as to not have all the intermediary tokens being sent back.

The other thing that it allows you to do is you can use this new

tool, which is overusing tool. We need to cut those at some point. Yeah, this meta tool, tool search ⁓ tool, to provide examples of how to use any of these MTPs, which I think is a really nice thing. Provide best usage examples.

it reduces tokens, it improves accuracy. I think this is something that we've complained about and it's good to see that that is something that is being worked on.

Dan (18:52)
Yeah, in real time.

Shimin (18:54)
every week something, something new.

Dan (18:54)
pretty fascinating. Yeah,

it's not surprising to me either because we've also, as part of our section, we read a bunch of different articles every week about how to try to use some of these tools more effectively. And the overarching theme has been for probably a couple of weeks now, maybe even a month, be careful with how many MCPs you use. Use them judiciously and ⁓ only turn on the tools you need. And I feel like there's two facets to that, so it's cool that there

attacking one of those two head-on. And the other one I've already sort of mentioned in this is like tool call spam, right? There's too many tools. ⁓ okay. But yeah, that's pretty cool.

Shimin (19:33)
All right, onto deep dive. What do we have here? Dan, T-dar.

Dan (19:37)
We got a lot of stuff.

Yeah. So this is one that I scooped off of probably Hacker News, I'm accurate, which is a new ⁓ paper that is Think in Diffusion, Talk in Auto-Regression. So if I try to take a swing at it, then you can make fun of me. ⁓

Shimin (19:44)
being honest, yeah.

I would never make fun of you then.

Dan (20:00)
You should. ⁓ So if I understand it correctly, it's like, you know, a lot of the reasoning models, right? Have like the sort of thinking stage where it's talking to itself. And essentially for that part of the process, they're suggesting using a diffusion model, which like, as we talked about previously, my understanding of it is it basically starts with the full

Shimin (20:13)
Mm-hmm.

Dan (20:25)
block of text that it intends to create, but it's kind of like, it's not real text. It's just like gibberish. And then it essentially works through it until it becomes the real text. That's a very layman's thing, but that's why I'm on this podcast. then, so that's the diffusion part. And then autoregression is next token prediction, which is how most LLMs work today. So it's the, you know, everyone's.

Hopefully familiar with that by now, but it's basically like you type in T and it's like, hmm, maybe H based on the words ahead of it. yeah. And then probably an E, it's the.

Shimin (20:56)
Mm-hmm.

Dan (20:59)
So that was my takeaway from it. It's interesting because I don't think anyone to date has considered mixing entire modes in that way.

Shimin (21:07)
Yeah. I've only ever seen, ⁓ pure diffusion or pure other regressive approaches. It's really cool that Nvidia is doing this research. They have a, they have a pretty strong, research arm kind of publishing lots of state of the art results and the

approach here as far as I understand it is it is taking advantage of essentially the fact that auto regression is so slow is because you are spending so much time loading in your KV cache or the large

Attention matrix where you want to try to figure out in a very long, string of texts, you know, how each token relates to another token, right? ⁓ given that so much time is being spent loading and unloading these large matrices, the amount of time to kind of tack on a couple more tokens

at the end of the text string, if the whole thing is 200,000 tokens long, as we're just talking about in the case of Claude you know, having five more tokens at the end is really not going to make much of a difference. So what it does is It takes a diffusion pass. It tries to generate say a couple of tokens, five tokens at a time, but these five tokens are not.

generated all the regressively. So they cannot say, the fifth token is dependent on the first four that I generated.

it's not conditioned on the previous tokens. So it just says, Hey, given, given the last, you know, 200,000 tokens here are five tokens that would go along with the one I just generated. So for cat, it may generate a dog, fish, feline tiger. So it may not make sense.

for all five of those to be in a sentence. Cause for it to make sense, you must look at every single token before it. And so it does two passes. generates a set of probable tokens via diffusion. And then at the same time, it uses the autoregressive approach to say, Hey, given everything that came before it, it's probably going to be tiger and not feline.

so that generates the next token, but at the same time produces another batch of candidates. Now it's another set of dog flowers, et cetera. that's what makes diffusion fast but

the quality takes a hit. So therefore it does two passes and it's somehow doing all this because of how slow it takes to load the KV cache into memory. Doing all this work still takes less time than ⁓ generating it one at a time. The memory swap, yeah.

Dan (23:49)
Memory swap, yeah.

That part doesn't surprise me from my understanding of traditional computer science and the fact that everything I know about even just doing inference, right, is it's incredibly ⁓ memory bandwidth limited. So that actually makes a lot of sense to me.

Shimin (24:09)
Yeah. And the, the really cool thing is that they're to do all this in a single pass. And of course they have a, ⁓ I think a significant speed up

4.725 to 5.9 times faster.

Dan (24:21)
I wonder too, and this really brings home the filthy casual in me, my understanding is diffusion models operate closer to doing what would be running LLMs and batches. Sorry, autoregression models and batches, which is why all the big providers batch their stuff. So I wonder if you're getting some of that same kind of efficiency there. But again, this stuff is so far over my head. I'm just here for the...

Shimin (24:35)
Mm-hmm.

We're both just filthy casuals. We're doing the filthy casual things. ⁓ and seeing these new papers that can, ⁓ output tokens much faster without a degradation in quality. That's definitely exciting. Cause I, I do think this is one thing that I Gemini three does particularly well. Gemini three is much faster in inferencing my experience than 2.5 and its competitors. I'm always surprised how quickly.

Dan (24:50)
the wells.

Shimin (25:15)
Gemini is able to come up with a pretty good output at a significantly faster runtime.

Dan (25:23)
And cheaper too, I'd imagine.

Shimin (25:25)
and cheaper, yeah, because of TPUs. Maybe, maybe not. I know nothing about TPUs. This is a furshey casual part. ⁓ The second paper we have this week is titled SSRL, Self Search Reinforcement Learning.

It's coming out of Qinghua, which if you do not know, Qinghua is the Harvard or Yale of China. So it's one of the biggest oldest universities in China.

Dan (25:57)
I thought I was here to learn about AI, but instead I'm learning about Chinese universities.

Shimin (25:57)
you

The fundamental breakthrough of this paper is the insight that almost everything that is knowable is already in the pre-training data of a large language model. It's being trained on trillions of texts. So it probably knows more than it lets on. And so if you asked the large language model,

to answer a question once, it probably isn't as good if you had asked it to generate K number of answers. And then based on these K answers, choose the best one. So if the model already knows the correct answer, why doesn't it just say the correct answer the first time? That is the key dilemma that this paper is trying to solve.

Dan (26:52)
I have a fun layman's theory about that that I'll spit out before you know. Think about how much of the training data on the internet is likely old school forum posts where it's like, hi, I'm Dan. I have this problem. This has gone wrong. And then the second person's like, it's this. And then they're like, no, that didn't work. And then they're like, but it's this. And they're like, no, that didn't work. And then finally they're like, ⁓ it's that.

Shimin (26:55)
Yeah, it doesn't like us.

Dan (27:20)
So who's to say that it didn't just like bake that into the model?

Shimin (27:25)
Mm-hmm. It sounds like you've like hacked my computer and found my chat history with

Dan (27:31)
Yeah.

Shimin (27:31)
with Claude ⁓

Dan (27:34)
But I mean, that was like Stack Overflow back in the day, It's like, you know, the accepted answer. No, it's this one. and then you come back and someone updates the answer 20 years later because, you know, it turns out we don't use jQuery anymore or something like that. But... ⁓

Shimin (27:48)
Yeah, Ajax.

Yeah, Ajax is no longer a thing. I used Ajax at work the other day and I felt instantly 20 years older. ⁓

Dan (27:56)
Nice.

Shimin (27:57)
So that is in line with the hypothesis of this paper, which is ⁓ the answer is there, but there's so much noise that it doesn't always find it. ⁓ And so the goal of the paper is to train the large language model to find the correct path by using a specific ⁓ formatted search or

Dan (28:02)
Ha!

Shimin (28:21)
prompt engineering essentially. in the prompt template, I'll read the prompt template ⁓ to see what it's trying to do here. The prompt template says, answer the given question. You must conduct reasoning insight.

tag think and slash think first every time you get new information. Outer reasoning, if you find you lack knowledge, you can call a search engine by tag search query, close tag search, and you should return the top search result between tag information and slash information. You can search as many times as you want. For multi-hop Q and A, you can break it down into pieces and search one by one.

If you find no further external knowledge needed, you can directly provide the answered inside answer tag without detailed illustrations. For example, answer Beijing question, blah, blah. ⁓ It is essentially training the model

examining the search query result workflow to find a better answer then it would have come up with by yourself, either on the first try or according to this paper, better than it would have come up with via thinking models. And the explanation the authors gave for why this approach works better

Dan (29:32)
Hmm.

Shimin (29:38)
that reasoning models is since these are not logical thinking problems, it all is trying to do is figure out which pieces knowledge it already knows and then determining what the best one is. Kind of like if I was to try and answer a

math problem I've never seen before, I may go back and say, hey, what do I remember about algebra from high school? And then like I would dribble down a few things and then look through it and then try to deduce what the answer might be.

Dan (30:09)
least you remember algebra.

Shimin (30:10)
I think I remember algebra.

Well, and of course the breakthrough here is the models are not actually connected to the internet. So it is not conducting an external knowledge search. It is doing search just from its internal memory banks. And it's still somehow able to outperform ⁓ a non-search model. And when you do hook it up to an external tool calling for search, it is of course able to get that. ⁓

Dan (30:19)
Mm-hmm.

super effectively

I'd imagine. Yeah, makes sense. That's pretty cool.

Shimin (30:37)
Yeah, exactly.

Yeah. I,

I find that I do this naturally when I'm, ⁓ working with large, large language models. I will usually ask for it to present me a few different potential solutions and then talk through the benefits and trade-offs. ⁓ cause they already knows more than you think it does. Right. ⁓ so perhaps even just by reasoning out.

here are five different ways to do this or here are five different answers and then talk me through which one it prefers. ⁓ We're already getting some sort of performance gain.

Dan (31:16)
I also wonder if that some of that isn't already built into some of the agent scripts and in Claude code too. Cause I see frequently it'll be like, if you ask it a pretty open-ended question about something like, how do I get this, you know, whatever to not be broken. It'll be like, well, we could do it this way, this way, this way, this way. Which option would you prefer? know, it's always like, hmm.

Shimin (31:34)
Mm-hmm.

Yeah, it's always sad when my own little hacks gets ⁓ baked into the tool itself. ⁓ I remember the day when Claude, when its deep search started asking me for clarifying my search parameters. Like the exact day when it went from I would just take this and run with it to like, ⁓ but before I start searching, can you clarify this, here are five questions, answer it for me. ⁓

Dan (31:53)
No.

Shimin (32:04)
But you know, these are, these are becoming best practices, I think just ⁓ industry wide and yeah.

Dan (32:09)
Yeah, we'd already talked about that before too around like

when you're writing a big spec upfront for something, like often it's surprisingly useful to just say, do you have any questions before we get started? And usually will, and it might not be things that you would have necessarily thought to put in the original prompt.

Shimin (32:20)
Yep,

Yeah, use it more as a pair programming buddy than underling for you to just go and bring me coffee. ⁓ Yeah, so that was my paper of the week

Dan (32:37)
You're a better person than me for reading all of that, because I didn't read that one. I did read the previous one, but not this one. It's pretty wild.

Shimin (32:46)
It's cause you're too busy, too busy ranting what, what got you so angry this week that you didn't have time to read the paper?

Dan (32:51)
I have to say,

first of all, in my defense, think you think that I'm much angrier person than I actually am, as evidenced by the fact that we even have this segment in here. ⁓ no.

Shimin (33:06)
This is all getting cut. No one's hearing this.

Dan (33:10)
Okay, well, yeah, so this week it's gonna be, you in the past I've done some sort of general ones where we've talked, you know, about things like context and stuff like that, but this week is a very specific problem that I ran into that kind of pissed me off while it was happening. So I regularly work in a code base now that has 90 % test coverage.

requirement. more interestingly than that, they also have 90 % branch coverage, meaning ⁓ if you have something like an if in your code, both branches of the if need to get extra set. Well, not both. 90 % of the both, throughout the delta of the change set that you're committing needs to be ⁓ covered by the test, which is fair, I suppose. I mean, you could go back and forth about what's a good number and whatever. But like,

That's not the point of this podcast. anyway, ⁓ I was using Claude to hit that 90 % number. ⁓ And particularly, I had done something rather simple, which was adding a button, which I didn't think would be all that controversial. But ⁓ surprisingly, it made a pretty huge impact on my branch coverage. So I started. ⁓

Shimin (34:19)
Mm-hmm.

Dan (34:28)
working with Claude a little bit and I was prompting it and I'm like, okay, so here's the coverage report where we're at today. Here's what the uncovered lines are. what are your, actually it's exactly like we just talked about. Like what, how do you think we should fix this? Like, and so it came up with four options and I'm like, cool. So I picked one and gave it a little bit more specificity and we started rolling and it goes cranking and like, I think it's pretty quick, but it's probably like maybe 10 minutes of

a little bit of back and forth, mostly just changing things and rerunning the test suites that take a while to run. It goes, OK. And I go look at what it did. And it had completely rewritten the component under test and ⁓ to a fair degree, the entire test suite. And really, it just drastically reduced the quality of it. And so I'm like, OK, screw all this. Control C twice. I'm done with it.

dumping all the context. don't even care. Reset everything in Git. I looked at it, and I realized that basically all I had to actually do was change some filter params in a URL, and it was covered because it was like two-turn areas that weren't being covered. so I guess one of the previous things I talked about was AI making us stupid. It's like maybe, but also there's still no real substitute for just like

you're leaning on it so much they don't actually just like look at what the problem is yourself and spend that time to do that. And I think that's a way that at least in this week AI has made me a little bit stupid. So that was my rant is it's really just, I was upset about wasting 40 minutes, probably total on something that was really trivial and I could have done myself in about five minutes. So hopefully lesson learned. We'll see next week. Come back to see if there's another rant about.

Shimin (35:54)
Mm-hmm.

Dan (36:18)
The same topic.

Shimin (36:19)
Right. We're all about giving out free business ideas on this podcast. And ⁓ here's a new business idea. ⁓ Create an agent that will reliably tell you when you should give up on using agents and do the work yourself, like a meta agent.

Dan (36:38)
It's just one of those websites that always says yes

Shimin (36:43)
I don't think it's always

yes, but that's certainly a problem because agents aren't good enough to do 100 % of the task. the mental challenge of, clearly this thing isn't solvable in the current conversation with the agent and I should just do it myself. That is a skill. I think that is a skill that I think the entire industry is

dealing with right now. I've had similar issues this past week too. It's like you just had so many back and forth that you decide screw it I'm gonna do it myself. ⁓ The upfront

Dan (37:19)
Yep. But it is

also interesting that my first instinct was just be like, have Claude do it. And I guess that partially is because, okay, fine, I'll rant a little bit. I think 90 % test coverage is quite high in my opinion. think 80 is fine. But I'm definitely leaning on Claude for that a little bit more than I would in other scenarios, right? So that was definitely my go-to. was just, just fix it. Come on.

Shimin (37:44)
Yeah, 90 % branches is stricter than ⁓ any place I've ever worked at, think. 90 % code, yes. Especially those exceptions and, well, really, yes, just exceptions that are fairly hard to test.

Dan (37:59)
It is

some well-tested code if you ignore the fact that Claude doesn't write the best tests.

Shimin (38:07)
Well, I think that's a very good rant.

Dan (38:08)
Thanks. Come back next week to see if it continues. Well, maybe not next week because we got holidays coming up here, but... ⁓

Shimin (38:08)
Yeah, we'll see. We'll see more. Yeah. ⁓

Yeah. Okay. On to our final segment. Two minutes to midnight where we have a conversation.

Dan (38:21)
Two minutes

to midnight. Yeah, they see we don't have the actual music, but they can't stop me from singing it.

Shimin (38:29)
They cannot. I might have to listen to you provide a little background. Boombox. ⁓ Yes, where we discover ⁓ where we are in the current AI industry bubble, if there is a bubble.

Dan (38:33)
The actual song. ⁓

slow motion pop

that's happening in real time.

Shimin (38:47)
Is it happening? Let's find out. All right. So I got a piece from Reuters here ⁓ titled, Mira Morati's Thinking Machine Seeks $50 Billion Valuation in Funding Talk Bloomberg News Report. ⁓

Dan (39:07)
So Mira was

the former CTO of... Yeah, okay. That's what I thought. I wasn't sure.

Shimin (39:11)
Yep. Of open AI. Yes.

After the whole, ⁓ kerfuffle with the Sam. Yes. ⁓ Sam. she left and her new lab, thinking machine is seeking a 55 or 60 billion evaluation. ⁓ deals have not been finalized, but on the other hand, the company also hasn't really had any product. ⁓ it did launch a product called

Dan (39:17)
The Sam. Yeah.

Shimin (39:39)
Tinker to help fine tune language models back in October, but I haven't heard anything about it. So, ⁓ so I think this.

Dan (39:47)
How long has

the company been around? it say? Last valued at 12 billion in July after raising two.

Shimin (39:52)
It did not say.

July.

Right. I don't think it's been around for that long. Are these the the web van or pets.com over our age? Is my open question.

Dan (40:04)
You

It's not a bad question because, you know, what is their output unless maybe it's, yeah, okay, so here we go too. February, 2025, it's nine months old, this company.

Shimin (40:22)
Okay, so it's actually that's older than I thought.

Dan (40:24)
Right, but also no surprise they haven't made any kind of like financial impact because it's nine months old, right? And it's not like the type of research that they're doing is easy or whatever, but still you do have to wonder like, what is the business model?

Shimin (40:31)
Right.

But 50 billion, which is...

Dan (40:40)
Yeah, definitely ⁓ too damn high. Yeah, that's fair. Okay, so we got one data point. What else we got?

Shimin (40:41)
I know inflation is high, but that's...

we got a article from crazy stupid tech called boom, bubble burst boom. Why should AI be different?

Dan (40:59)
Right. So this is a pretty fascinating read where it's actually a fairly lengthy article, but ⁓ to summarize it a little bit, they took a very hard look at actually what we were just talking about, which was the original .com implosion of the 1990s. And ⁓ kind of looked at some of the key contributing factors to that, and then looked at what's happening today in AI and like try to draw.

comparisons between them. And one of the things I found pretty fascinating about the article was ⁓ they were really looking at what are, assuming that we are in a bubble, they're looking at what were the weaknesses that would ⁓ trigger the market to ⁓ have sudden shifts that would trigger the collapse of the bubble. So I thought that was pretty interesting. And just to summarize really quickly, ⁓ they're

Big four ⁓ weaknesses were too much spending, which I think we've sort of covered a little bit in this segment, too much leverage, which we've definitely covered in this segment, disappointing that they don't have too many space station data centers on the list, but that should have made the list, ⁓ crazy deals, and then China, China, China.

Shimin (42:15)
Right.

Dan (42:15)
So yeah, it was just interesting take to see what someone else's analysis is, because we always sort of do our own in the segment. So ⁓ it was pretty fascinating. And their overall conclusion is, yes, we're in a bubble. And it's much, much larger and much, much worse than the dot com one predicated on the fact that the US economy today is almost entirely based on AI, meaning it's overall less stable and less

Shimin (42:41)
Right.

Dan (42:43)
robust than it was in the 90s. So that's kind of terrifying to think about.

Shimin (42:48)
Right. Cause the

dot-com bubble happened after a very long period of economic growth. ⁓ Whereas we are probably in a much shakier foundations this time around. And the last article we have here is from Bloomberg called, NVIDIA didn't save the market. What's next for the AI trade. But this is really just a, just a occasional talk about the NVIDIA earnings last week.

Dan (42:54)
Mm-hmm.

For sure. Yeah.

two, three earnings. Yeah. ⁓

Shimin (43:16)
It beat all the top line numbers and the price jumped by 5 % on opening and then the market closed ⁓ down 3.2 % by the end of the day, which is not what one would expect for such rosy earnings.

I think if there is a moment of kind of the top of the market, that might be it. This is not financial advice. No one should buy or sell stocks based on two dudes, two filthy AI casuals talking on the podcast. But I wonder if looking back, we'll see this Nvidia Q3 earning as the top of the bubble, ⁓ the initial drop. Yeah.

Dan (43:47)
You

The high water mark. Yeah, it could

be.

Shimin (44:00)
So taking all that into consideration, how do we feel about our little AI bubble clock? I think we were at 20 seconds last week.

Dan (44:09)
I, you know, honestly, I'm maybe more optimistic than I should be because of the Nvidia earnings.

Shimin (44:17)
Say more.

Dan (44:17)
because I

think that like...

If

If it really scared people, like you could look at like a 2 % drop. Sure. It's, it's a big deal, but, ⁓ it's also people like worried that it's the top. So they're trying to get out, you know? And so I think you'll see, I mean, again, not a trader. I've zero experience, any of this. I don't even do day trading for the record. but like, yeah, for sure.

Shimin (44:40)
I feel like day trading is hard. Day trading is like for experts.

Dan (44:47)
or large language models. ⁓ But at the end of the day, I feel like that could just trigger sort of volatility bounces more than it would the overall thing. We definitely haven't seen the market collapse. So I think overall, I see it as actually kind of a sign of sure, things are happening, but we're not there yet. So I would actually argue for setting us back a little bit. Maybe I'm just feeling optimistic this week.

Shimin (45:11)
Wow.

You're feeling very out. So you're basically you're saying maybe the bubble is deflating a little bit ⁓ before it goes to the top.

Dan (45:18)
No, I think we're still

very much in a bubble, but I don't think we're so close to it collapsing necessarily. Because we saw a of a shallow dip, but it wasn't aiming down. Yeah, exactly. But that's my take. I don't know. What do you think?

Shimin (45:26)
Interesting.

Like a cliff. All right. that's

job security for another week. ⁓

Dan (45:41)
Always a good thing.

Shimin (45:42)
I'm kind of leaning towards just keeping it at 20. ⁓ but I could also go to 25.

Dan (45:49)
Okay, I'm fine with 25. Yeah. I also just looking at their valuation and it's like the high watermark was 11.3 so far. They've actually been down since then, which is interesting.

Shimin (45:49)
Alright, 25? 25 seconds.

Yeah, but not very quickly.

Dan (46:04)
I don't know. You're not here for the armchair financial

analysis.

Shimin (46:10)
Yeah, before I pull out the candle charts and the

PE graphs and all of that, is thankfully we don't get paid for our financial insights.

on that note, that's another podcast in the can. Why do they call it in the can?

Dan (46:24)
Yeah, don't forget to...

Because probably you put film or tape in the can like to protect it. I guess No, no, it was like the you've ever seen like really old-school Like yeah film capture. Yeah, it's the can I don't know

Shimin (46:30)
Uhhh, okay. It's not the trashcan, I was thinking.

Film canisters. Yeah, it's

the can.

Shimin (46:41)
And that's a wrap for this week's episode of Artificial Developer Intelligence. Thank you so much for tuning in and spending time with us, AI Filthy Casuals. If you enjoyed this week's show, the best way you can support us is by sharing it with a friend who you think will give value from it. And if you really liked the show, please leave us a rating or review on Apple podcasts or Spotify. It honestly helps more people to discover the show and we read every single review. Do you have a question?

feedback or a topic you want us to cover, we would love to hear from you. Shoot us an email at humans at adipod.ai. Again, that is humans at adipod.ai. You can find full show notes, transcripts, and links to everything we mentioned today over at our website, www.adipod.ai. Thank you again for listening. We'll catch you on next week's episode.

</details>
