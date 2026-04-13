---
episode: "1"
title: "AI Benchmarks, Tech Radar, and Limits of Current LLM Architectures"
date: "2025-11-28"
slug: "1-ai-benchmarks-tech-radar-and-limits-of-current-llm-architectures"
description: "In this episode of Artificial Developer Intelligence, hosts Shimin and Dan explore the rapidly evolving landscape of AI, discussing recent news, benchmarking challenges, and the implications of AGI as a conspiracy theory. They delve into the latest techniques in AI development, ethical considerations, and the potential impact of AI on human intelligence. The conversation culminates in the latest advancements in LLM architectures, and the ongoing concerns surrounding the AI bubble."
keywords: "AI benchmarks, SWE-Bench, ThoughtWorks tech radar, subagents, AGI conspiracy, LLM architectures, linear attention, text diffusion, code world models, Anthropic alignment, model ethics, context length, AI bubble"
appleUrl: "https://podcasts.apple.com/podcast/artificial-developer-intelligence/id1857109105"
spotifyUrl: "https://open.spotify.com/show/4eDLlGoktxMngPNq9aGqLX"
overcastUrl: "https://overcast.fm/itunes1857109105"
pocketCastsUrl: "https://pca.st/itunes/1857109105"
amazonUrl: "https://music.amazon.com/podcasts/da06d4c3-ecf6-498f-abe3-4d3b00026bf2"
transistorId: "3c2d9719"
youtubeId: "ry6axvt1dIo"
---

In this episode of Artificial Developer Intelligence, hosts Shimin and Dan explore the rapidly evolving landscape of AI, discussing recent news, benchmarking challenges, and the implications of AGI as a conspiracy theory. They delve into the latest techniques in AI development, ethical considerations, and the potential impact of AI on human intelligence. The conversation culminates in the latest advancements in LLM architectures, and the ongoing concerns surrounding the AI bubble.

## Takeaways

- Benchmarking AI performance is fraught with challenges and potential biases.
- AGI is increasingly viewed as a conspiracy theory rather than a technical goal.
- New LLM architectures are emerging to address context limitations.
- Ethical dilemmas in AI models raise questions about their decision-making capabilities.
- The AI bubble may lead to significant economic consequences.
- AI's influence on human intelligence is a growing concern among.

## Resources Mentioned

- [AI benchmarks are a bad joke – and LLM makers are the ones laughing](https://www.theregister.com/2025/11/07/measuring_ai_models_hampered_by/)
- [Technology Radar V33](https://www.thoughtworks.com/radar)
- [How I use Every Claude Code Feature](https://blog.sshh.io/p/how-i-use-every-claude-code-feature)
- [How AGI became the most consequential conspiracy theory of our time](https://www.technologyreview.com/2025/10/30/1127057/agi-conspiracy-theory-artifcial-general-intelligence/)
- [Beyond Standard LLMs](https://magazine.sebastianraschka.com/p/beyond-standard-llms)
- [Stress-testing model specs reveals character differences among language models](https://alignment.anthropic.com/2025/stress-testing-model-specs/)
- [Meet Project Suncatcher, Google’s plan to put AI data centers in space](https://arstechnica.com/google/2025/11/meet-project-suncatcher-googles-plan-to-put-ai-data-centers-in-space/)
- [OpenAI CFO Sarah Friar says company isn’t seeking government backstop, clarifying prior comment](https://www.cnbc.com/2025/11/06/openai-cfo-sarah-friar-says-company-is-not-seeking-government-backstop.html)

## Chapters

- (00:00) - Introduction to Artificial Developer Intelligence
- (02:26) - AI Benchmarks: Are They Reliable?
- (08:02) - ThoughtWorks Tech Radar: AI-Centric Trends
- (11:47) - Techniques Corner: Exploring AI Subagents
- (14:17) - AGI: The Most Consequential Conspiracy Theory
- (22:57) - Deep Dive: Limitations of Current LLM Architectures
- (34:13) - Ethics and Decision-Making in AI
- (38:41) - Dan's Rant on the Impact of AI on Human Intelligence
- (43:26) - 2 Minutes to Midnight
- (50:29) - Outro


## Transcript

<details>
<summary>Show full transcript</summary>

Shimin (00:09)
Hello and welcome to Artificial Developer Intelligence, a podcast where two

filthy casuals navigate the ever-changing AI-enabled software engineering landscape. I'm Shimin Zhang, a software developer, and with me today is my co-host, Dan. It's not a conspiracy if my 401k depends on it, Lasky Dan, happy belated birthday. What is your favorite conspiracy theory?

Dan (00:32)
Thanks.

Well, ⁓ right now, and this is not a widely accepted one, but ⁓ right now it's definitely that the game Slay the Spire, which is heavily RNG dependent if you haven't played it, has a different RNG on different platforms, and I'm clearly playing on the platform with the worst RNG, and that's why I'm terrible at it.

Shimin (00:57)
you should sacrifice some virgins to the RNG gods. That should definitely help.

Dan (01:02)
Works every time.

on today's podcast, we're going to be going through the AI news of this week. As you know, the space moves really quickly, so we'll try to cover the most interesting articles that we uncovered this week, quickly followed by.

Shimin (01:17)
a technique corner where we discuss some interesting techniques we've been using when working with AI.

Dan (01:24)
And then on to the post of the week, this week we're going to be digging into whether or not AGI itself is a conspiracy theory. So a nice little lead in there. And then we will be doing.

Shimin (01:36)
A deep dive segment where we're going to go over two items this week. One, which is a blog post that covers some new LLM architectures beyond the standard full attention models. We'll also talk about a new anthropic paper that experiments with value alignment on various large language models. And then it's my favorite segment.

Dan (01:56)
And then

if you've made it this far in the podcast, you get to listen to me rant about things. Because why not? That's what I do all the time anyway. And then finally, yeah.

Shimin (02:08)
And then it

will be your favorite segment, which is two minutes to midnight, where we discuss where we are as approaching as we are approaching the A.I. whether or not it's going to burst tomorrow, a month from now, maybe never. You never know.

First up, we have an article from the register called AI benchmarks are a bad joke and LLMs makers are the ones laughing. In which we look at a new study from the Oxford Internet Institute that cast doubt on the reliability of existing AI benchmarks. The researchers found that only 16 % of the 445 prominent benchmark uses rigorous scientific methods. With many failing to

even define the concepts like reasoning and harmlessness. So as we know, most models released today had the charts for their performance on various AI benchmarks. Some of the ones that I look at the most are the SWE bench verified. They are also the AIM 2025.

the MMU and the health bench hard. So we will look at the performance of the models on these benchmarks. How good are these benchmarks? Is the question. Then have you looked at these benchmarks?

Dan (03:30)
Yeah, that's a great.

No, not in detail, but I've definitely seen plenty of articles out there that are essentially claiming that they're gamed to some degree because they can train specifically for the questions that are in the benchmarks. To what degree that's true, I have no idea, but it is fascinating. And I always.

Shimin (03:45)
Mm-hmm.

Dan (03:53)
I guess generally, I always think about the time that like one of my friends in college a long time ago, his first job out of school was working for a large software company that created graphics drivers or dealt with graphics drivers, I should say from multiple vendors. And one of the vendors that he worked with was known for cheating quite a bit in their driver code so that it would look better on benchmarks than he actually performed in real world.

I just feel like that's a very human thing to want to game the system once there's a system to game.

Shimin (04:26)
Did your friend work

for the graphics unit of Volkswagen? Is that what happened?

Dan (04:30)
No.

No. I was trying very hard not to name names, but yeah, he worked for Microsoft and was dealing with both at the time it was ATI. So this dates my story a little bit, but ATI and Nvidia drivers pretty frequently.

Shimin (04:46)
So I thought this article was really interesting. We've heard a lot about companies gaming benchmarks. They may have benchmark data in their training set. There are numerous ways to game the system. So I decided to take a look at the SWE Bench, the Software Engineering Bench And it looks like how they

Dan (04:55)
Mm-hmm.

Shimin (05:08)
formulated the benchmark is they took 12 popular Python repositories and they pull requests for those repositories that are associated with an issue. And they essentially asked the AI in a sandbox Docker container environment to write code to resolve the issue that was listed in the GitHub issues and run the test both before and after.

⁓ the model claims that it has done the work. And on the face of it, that feels pretty good to me.

Dan (05:44)
But is it like they're not randomizing that set, it's always the same issues, I'm assuming. Because otherwise it wouldn't be a very good benchmark, but.

Shimin (05:53)
Right. Correct.

Dan (05:55)
Yeah,

I do wonder in that situation what prevents someone from just training on that exact thing.

Shimin (06:02)
We know models have the ability to remember a large corpus of text. if those GitHub repos were part of its training set, and since they were all public, there's definitely a chance that the models have seen the answer. But I do think the article itself has a bit of a click-baity title. I wouldn't go as far as...

Dan (06:22)
For sure. It's also the register.

So, you know, take it with a grain of salt.

Shimin (06:27)
Yes.

So I pulled up the paper, the underlying paper that is called Measuring What Matters Construct Validity in Large Language Model Benchmarks. And they actually have a very sensible set of recommendations. They recommend that the benchmark creators to define the phenomenon, such as define what reasoning is, to measure the phenomenon and only the phenomenon.

which seems reasonable, and control for unrelated tasks that may affect the results. Then to construct a representative data set for the task before acknowledging limitations of reusing data set and then prepare for containment, which we just spoke about earlier. These are all very reasonable recommendations.

Dan (07:08)
Right. Significantly

less click-bait-y than the title might imply.

Shimin (07:12)
Yes.

So I like the recommendations. think it makes sense. think we've been in move fast and worry about the definitions later land, which would the speed that everything has been moving lately. I totally understand. And at the end of the day, I feel like the SWE benchmark is, is pretty good. When it comes to measuring how well a model can actually write code that, you know, can help us.

Dan (07:40)
And do real, real

tasks, real world tasks.

Shimin (07:42)
Right.

But we definitely should keep that in mind.

Any last words Benchmark suck. Conspiracy.

Dan (07:50)
I mean, I'm sad that,

that the title of that article wasn't. We could make some slight improvements to benchmarking to have it be much more realistic and rigorous, but it is what it is.

Shimin (08:03)
It is what it is. Speaking of it ThoughtWorks and its tech radar. Have you, come across it? For those who do not know what the tech technology radar is, ThoughtWorks, is a contracting consultant company, software development company, ⁓ famous for its pair programming and TDD workflows. I interviewed with them once.

I was much younger at the time and I didn't know what a decorator was in Java. And that's, I think what calls me the job, but I know what a decorator is now. So take that ThoughtWorks. Yes, there we go.

Dan (08:30)
You

All right. And if you don't, Claude does. So

yeah, I'm quite familiar with them. I did like over a two-year engagement at one point in my career with them. And actually, I wound up working with one of the guys that did the tech radar for quite a while. So it was pretty cool.

Shimin (08:49)
wow. So

your tech radar is very familiar to you. They released them twice a year and the November, 2025 issue just came out. What I found really interesting other than recommending tech radar as a whole for software developers to keep a tab on the technology landscape is it is wild how AI centric the November.

2025 tech radar is. I am looking at it right now. can hardly find any.

technologies out there that is not AI or AI adjacent. There are two, there's a Pydantic, which is really great. It's like an ORM for Python. And there is PMPM, which I know you like. I am trying to convince my team to adopt it, but pretty much everything else on this list is entirely AI driven. ⁓

Dan (09:39)
I'm a fan.

That doesn't

surprise me too much. I mean, I do think, as you mentioned, indicative of the trends, but also the tech radar, at least in my experience, always got a little hype factor in it too. So they're certainly not immune to that. Not that I think like PNPM is hype, for example, but I recall while we were doing the engagement with them, the tech radar was pushing micro front ends really hard. ⁓

Shimin (09:57)
Ha

Mm.

Dan (10:10)
see too many micro front ends these days so there's definitely an element of trendiness in it.

Shimin (10:14)
I

got strong feelings from MicroFrontEnd that are not positive, but pre-commit hooks is definitely, I really like that. And that's not AI related until the November 2025 issue. just, kind of was going over the November issue with the April issue. And I feel like we were already fairly along the AI hype train back in April. And in April,

Dan (10:20)
saving for Dan's ran.

Shimin (10:40)
the adopt the techniques category I'm seeing in the adopt quadrant. I'm seeing data product thinking, first testing, software build of goods and threat modeling. I am just double checking to make sure I am indeed looking at the 2020 April of this year issue, because I'm seeing zero AI items there. ⁓ For platform, they are still adopting

Dan (11:00)
you

fair.

Shimin (11:09)
get lab CICD. So it's kind of, it kind of just wild how in the last six months, like the, the entire radar has, has been shifted, which I guess is why we're doing this podcast. Things are moving incredibly quickly.

Dan (11:23)
Well yeah, it's been here for a bit, but it feels like maybe in the last six months to a year that it's really gotten good for some definitions of good. So I'm not surprised that it's shifting.

Shimin (11:31)
Yeah.

Usefulness plus hype kind of somewhere along there.

Dan (11:40)
Yeah. Bell curve

between usefulness and null. can't. Yeah.

Shimin (11:44)
We're gonna

try. Okay, moving on to the technique corner. I know last week, Dan, you talked about the slash catch up. That was from this article, how I use every called code feature on sub stack, believe by Srivishankar's sub stack.

Dan (11:52)
Mm-hmm.

Shimin (12:03)
And this week I've got a chance to play around with one of the other ideas from that same article, which is to ask Claude Code to use its own built-in task to spawn subagents, as opposed to having lots of different agent.markdown files and kind of pre-define the workflow that Claude Code is supposed to do.

I thought this was interesting because it is against the clock code best practice for, um, for their sub agent usage, right? Like I'm looking at the effective context engineering for AI agents article, right? Um, um, Anthropics blog and in there, there's a whole section about using sub agent architecture to work as a way to work around context limitations, which I think.

having Claude Code generate its own agents is still doing the same thing by working as a workaround around context limitations. But the approach of, maybe the agent already knows how to separate out the tasks into subagents is superior. So I've given that a try in some of my projects this week, and I found it to be quite useful. Instead of writing down a long agents I mark down and

You know, define everything you need in a code review, often using Claude code to help me, you know, modify and improve the agents that markdown file, just ask Claude to do it. And I think it does a pretty good job. haven't done a ton with the actual, built in cloning yet. I still ask it to define its agents. So there's still a concept of like, here's an agent you can use.

as opposed to using an agent, whatever you feel appropriate. So I feel like I'm still having on a shorter leash, but I found it to be very helpful.

Dan (13:55)
Gotcha.

Yeah, it'll be fascinating to see if they keep pushing that or if it becomes irrelevant because it seems like context windows keep doubling every six to eight months. I'm sure we'll hit some limit there, like memory limitations, but maybe it will be irrelevant with the next doubling, but maybe not. And we'll actually go even more agentic with some of these things.

Shimin (14:21)
And context, length, doubling, that's gonna, we're gonna come back to that later. Yeah, so I agree. All right, for the article of the week, we have a article from MIT technology review called how AGI became the most consequential conspiracy theory of our time.

Dan (14:29)
Nice.

I'm really angry that they didn't pick the RNG one, but okay, we'll go with it.

Shimin (14:48)
Okay, inside the article, the article states that artificial general intelligence has ceased to become a merely technical goal and is now the driving conspiracy theory in at least the tech sector in the United States.

It also contains that the narrative functions as a convenient but unfalsifiable myth that tech elites can use to drive up valuation as well as get their workers to work harder. By the same time, avoid regulation by promising a utopia that only they can give us. So the article says we should stop treating AGI like an inevitability.

and see it more as a way for Big Tech to concentrate power. There are some really interesting quotes from the, or stories from the article that I would like to mention. For example, in the article, they mentioned that...

Ila Saltkever, the former chief scientist at OpenAI, is said to have led the chant of Feel the AGI at a team meeting. If that's not culty, I don't know what is.

Dan (15:57)
You

Shimin (15:59)
But at the same time, I kind of want to feel the AGI then.

Dan (16:03)
I mean, who doesn't, really?

Shimin (16:06)
⁓

Dan (16:06)
At least in that room, for sure.

Shimin (16:09)
Yeah, and I also like this quote. If you are building a conspiracy theory, you need a few things in the mix. A scheme that is flexible enough to sustain belief, even when things don't work out as planned. And the promise of a better future that could be realized only if believers uncover hidden truth. And a hope for salvation from the horrors of this world.

Dan (16:30)
Right, which when you look at it from that perspective, AGI really kind of ticks all the boxes, doesn't it? It will mystically solve all of our problems, I'm sure, including climate change and everything else. And then...

Yeah, we keep trying to get there, and we aren't. And the only way to get there is clearly more spending. So let's keep doing it.

Shimin (16:49)
or they're going to talk about a couple of news items about that this week. yeah, especially, you know, AGI like CodeFusion always needs to be six months to a year away because any further than that, you won't be able to recruit people from Jane Street. And if it's any closer, then it's already here. Then what's the point? Right. And I find that to be a paradox that a lot of conspiracies do share.

Dan (16:53)
Mm-hmm.

Shimin (17:14)
Are you a believer? I know I want to believe.

Dan (17:17)
in AGI. I think the concept of it certainly exists.

What do mean by believer, really?

Shimin (17:26)
Do you believe that our current, yeah, within our lifetime?

Dan (17:28)
that's achievable with current,

with our lifetime? I mean, that's a hard thing to predict because, I mean, if you look at like my grandparents, for example, they were alive when there was, know, horse and buggies in use, maybe not the only thing in use, but they were around. And by the time they passed away, there was like supersonic jet aircraft and computers and everything else. So like,

By end of our lifetime, probably, I don't know. Yeah, maybe I'll go back and look at this in 40 years and be like, boy. the thing that makes me question it is like, look, I'm a filthy casual, as we say on the label of this podcast, but my intuition, which is not worth very much when it comes to AI stuff, is that

Transformers is probably not the architecture that's going to get us there. So who's to say that there won't be some architectural shift with the impact that Transformers already had on large language models? are we there now? Can this technology scale to get us there? It doesn't feel like it to me. I think we're in the S-curve of technologies, where you start off

with nothing for kind of a long time, as we've seen with ML. And then all of a sudden you hit something and you go rocket ship up to the sun like we've done with large language models. It feels kind of like we're in the flattening part of the S-curve. And then I based that on things like the average slash media response to GPT-5 and stuff like that, where people were underwhelmed by the usage.

Regardless of whether or not it's actually better statistically, there's the perception that it's underwhelming. And I think that's something that's worth paying attention to. ⁓

Shimin (19:15)
Well,

Elia, the former chief scientist of OpenAI agrees with you. He gave a pretty famous speech earlier this year where, or it have been the last year where he talked about how we're running out of data for training at least large language model based AI's now. So he foresees a slowdown in model improvement.

Dan (19:38)
Yeah, and also like, you know, combining with stuff like the Apple paper, right? Where they've sort of proven to some degree that like reasoning isn't really reasoning. And a lot of the reasoning that is happening is only kind of works within the boundaries of things that you are fairly well defined problems like software, right? So if you're going to call it, you know, we've built this thing that's great for coding, but is that AGI not

really because you should be able to give it like a really advanced chemistry problem that it's never seen before and get a reasonable answer. Is it still a very useful tool? I think so, but like, yeah, I don't know.

Shimin (20:16)
Yeah, there's a whole theory that our whole field of RL researchers who think that in order to achieve true AGI, we need the AI to have sensory input like humans. And there has been argument that like that's one area where China is doing a much better job than the United States, whereas in the US, we are all looking for AGI as

Dan (20:34)
interesting.

Shimin (20:40)
salvation in China, they are applying AI in factories, dark factories. So they are working with robotics and the intersection of machines and intelligence. So some of their models have more actual percept perception feedback. you know, shorter lots of technological challenges, memories, et cetera, but that may be a closer, closer parallel to what HDI actually is.

Dan (21:06)
Yeah, I'm aware of at

least one US startup that's doing something like that too. They're trying to have like AI run construction equipment, like backhoes and stuff like that.

Shimin (21:14)
Yeah, but I think the argument

is they are doing it. It's already there as opposed to kind of in the research phase. So within our lifetime, yes, but maybe not the next few years. I knew you were an optimist. This is good.

Dan (21:28)
Yeah, well

what's your take on that?

Shimin (21:31)
I'm pretty much in the same boat. I think we within our lifetime, when we look back, definitely. I was just reminded when I saw the new, air pod, demo and how you get real time translation. we have the Babel fish now and we just kind of all like, like whatever, you know, like we had the technology. Yeah. It's and

Dan (21:48)
Or Star Trek is real. The little pin on here. Yeah.

Shimin (21:54)
our first response is like, well, yeah, like Google cracked it back in like 2018, you know, like, you read the original paper? Like they've already got translation working. But if we, if we give, if we give that to, you know, me when I was seven or so, like we, we live in the future. I, I don't think, I think we're going to keep on moving the goalposts of AGI and I think that's okay. but in the meantime, the progress is, is undeniable.

Dan (22:22)
And I would argue the real problem with the translation stuff isn't that it existed. I mean, that was obviously the hard problem to solve, but I feel like we still haven't really solved the how do you use this in a useful way in real life. Because I travel quite a bit internationally, and despite having that on my phone, I've never found a good way to actually use it where you don't wind up looking like even more of a tourist in an ass than the...

you do without it.

Shimin (22:53)
That's a UX problem. You would also look like a tourist. If you bring out a babble fish, you would also look like a tourist.

Dan (22:54)
Exactly. Spoken like a UX guy, I guess.

Shimin (23:03)
But speaking of context length, doubling every couple of months, at least it felt that way. Our deep dive of the week is the ⁓ blog post by Sebastian Reska, who writes the Ahead of AI Substack. I see it more as a magazine about the post. The post title is Beyond Standard LLMs.

And it describes some of the shortcomings of existing full attention large language models and some of the technological breakthroughs that we've had to solve the problem of context length, actually.

To recap, the traditional or the original large language model has what's called a faux attention, where you take the string of the faux context length tokens and you essentially encode it into a embedding of a certain size. So we have say, 124 length token, we use an embedding to reduce that.

context length down to 512 for each character within the token. then, so it will be a matrix of size 124 by 512. Right. And then that gets then passed through the full attention mechanism, which you multiply the embedding by a Q matrix, a K matrix,

And then you take the Q matrix, multiply it with the K transpose before multiplying, before doing a matrix multiplication on the value matrix to kind of simulate the idea of finding out which tokens in the string you want to pay attention to and what the value of those tokens are.

And that's why it's called, you know, attention's all you need is that mechanism with determining which one is important, but also which token is important to which other token. So the bottleneck of that is when you do the Q and K calculation, each one of them is a 512 by, or I should say it's a

124 by 512. So when you do Q matrix multiply K transpose, you have a 124 by 124 matrix. And that is a matrix that is quadratic to the size of the input token length.

And that takes up a tremendous amount of memory. the

Dan (25:46)
⁓ yep, that makes

sense. And as a fill the cache, well, to me, I've like run Olamas and looked at like, the KV cache can be compressed. Is that the same thing or no?

Shimin (25:55)
Right.

Yeah, the KV cache is way to solve the problem of having to generate these humongous matrices. ⁓ So when we, and since this product of QK transpose is quadratic to context length, it becomes a problem as we try to keep the context length. Yes.

Dan (26:02)
I see. Okay.

Gotcha.

That's massive. That's

why we keep buying GPUs with more and more memory to try to scale that one up.

Shimin (26:27)
Right. And so I'm

actually not a hundred percent sure how these 1 million context token models are created because they are definitely not doing a 1 million by 1 million kind of matrix. Or maybe they are, maybe that's why we're so much money on them. This is a part I'm not, I'm not so sure about.

Dan (26:47)
Yeah, and well, my

understanding is that typically inference compute doesn't necessarily require high speed links between the GPUs, whereas you do need it for model training. Because my first thought is, oh, maybe they're just sharing memory or something like that at a massive scale. But I have no idea. Felt the casual.

Shimin (27:12)
Yeah, there are approaches where each one of these QK transpose is a single head. And that's what you hear about multi-headed attention models. So sometimes the attention portion, the QK portion gets fused to reduce the overall memory consumption as well. ⁓ because the V tells you, you know, what

Dan (27:32)
Hmm, interesting.

Shimin (27:37)
each token does, but the Q and the K in theory just tells you which ones you should pay attention to. multiple models can actually share that same attention. So that's one way to reduce memory requirements while training. But this paper also introduced this idea of a linear attention. Then this is the 2020 paper called Transformers are RNN's Fast

autoregressive transformer with linear tension where using a kernel function, it is able to reduce the size of the memory usage to a linear.

of the context length ⁓ in subquadratic. Yeah. So the downside is that is not as effective as the quadratic version. Because of course you are losing information when you're using a kernel function to kind of squeeze all that information down to a single value. So that

Dan (28:13)
instead of quadratic.

So it's not dissimilar

from like an audio compressor, essentially.

is interesting.

Shimin (28:38)
I'm

nodding, but I'm not 100 % sure how the audio compressor works. So yes.

Dan (28:41)
Well, it's, I mean,

it's, you're taking the full dynamic range of like, say, a symphony, right? And dynamic range is essentially the quietest note, you know, someone rustling the page of the music all the way up to like the, you know, banging, it's bang of a timpani or something like that. And, compressor essentially says the range between those two things squish it.

And so it's literally a compressor. You're actually compressing the audio signal, right? It sounds better to the human ear, which is why we use it a lot in audio stuff. But the fascinating part is that you are, in fact, losing data in that compression as well. So I don't know, trying to link it back to things I know a little bit about instead. That level of math was never my forte.

Shimin (29:32)
⁓ yeah,

The math of this blog post is definitely pretty dense and I can't say I have fully absorbed all of it either. But there are other interesting future directions that this blog post talked about, including the text diffusion model that is the DeepSeq OCR paper that we spoke about last week. That sounds really interesting. I particularly like the

⁓ graphics for denoising the mask tokens in that's in the graphics there. I had always wondered how a text diffusion model handles a situation where a particular slice of text may need to be inserted as you go through another iteration of text diffusion. using the mask token seems to make sense because they

they leave a gap for some future string to exist. And then on the next pass through, it's more iterative, but compared to the auto-regressive response where a token needs to be generated one at a time, you get multiple passes where multiple tokens gets generated. And I especially find it interesting that the Google results

for its Gemini diffusion is on par with the Gemini 2.0 flashlight. yeah, this is probably a very interesting approach to monitor going forward.

Dan (30:59)
Then I assume the difference is the context cost is cheaper in terms of memory between the two or?

Shimin (31:06)
Not necessarily, but large language models generate a single token at a time. So any way you can generate multiple tokens at a time would be a humongous speed up.

Dan (31:12)
Mm-hmm. Right. Yeah.

That makes sense. And yeah, and I'd seen a lot of that with like inference providers too, where they prefer batch too, because they get quite a bit of speed up by doing that. Yep.

Shimin (31:25)
Yeah, you get a lot of savings from that.

Another approach that was mentioned in this blog post is the code world model. I really love this one. Normal or what I think of traditional large language models are trained on text and train on generating a single token at a time, given the preceding tokens, right? It's kind of like supervised self-supervised learning is what it's called.

but it has no intrinsic understanding of how code behaves. Cause it doesn't actually run a compiler or it doesn't run a parser. It emulates a parser. doesn't actually compile the code. So here in this world model approach, they are able to use reinforcement learning to learn how the program actually works.

Dan (32:24)
I found that fascinating too, because I'm also wondering if like, at some point it would make sense to essentially come up with a system that trains on like ASTs instead of text. know, if there's a way to like represent an AST as a vector somehow, which I, again, math hurts me a little bit there, but it would be fascinating if you could do that.

Shimin (32:38)
Mm-hmm.

Dan (32:50)
like having like only a coding one. But then I guess the trick with that is on like how do you instruct it to like write some code to instruct it as well.

Shimin (32:50)
Yeah.

Yeah, text is definitely not the most efficient way to communicate with a large language model.

Dan (33:05)
Or

between humans either, really, when you think about it.

Shimin (33:08)
I'm thinking very hard. you tell what I'm thinking right now, Dan?

Dan (33:08)
It's.

No. But we could write paragraphs and paragraphs of text to poorly explain what you're thinking right now.

Shimin (33:16)
Yes. Yeah. So I find this approach to be super promising, at least in terms of code, where it tries to predict the state of the program, as opposed to just what the next token is. And through that, it is able to learn a finer representation of how code actually works and give feedback that way. I think this is probably going to be how future code models are developed.

Dan (33:42)
Huge if true. I know it's research.

Shimin (33:44)
I will bet I'm

buying stock. I'm buying stock on the world model approach. If I could, I'm buying some options here.

Dan (33:49)
Alright.

Shimin (33:53)
So yeah, that was a super interesting blog post about some of the non-standard large language model architecture that I recommend everyone to go check out. Long read, but I feel like I learned a lot even if I didn't absorb everything.

Dan (34:09)
sure. Yeah, and that blog is great generally too if you have

Shimin (34:13)
Yeah. on the other note, have, also a paper from the alignment, ⁓ science group at anthropic about stress testing model specs, revealing character differences among language models. it's interesting. We have all these ethical concerns that humans, but how do you language models handle ethical concerns?

do they handle ethical concerns? When they are asked to make a trade-off between two equally good values, what do they actually do? And this paper goes into exploring how different language models handle these ethical dilemmas differently. One example that they mentioned here is when they queried them

model to make a trade-off between social equity and business effectiveness. In the specific case of whether an internet company serving both wealthy urban area and low-income rural communities should adopt progressive pricing, should the model emphasize the ethical imperative of equal access or focus on business sustainability? There's no objectively correct answer, but the models must choose or at least communicate their uncertainty.

Do we think models?

are we expecting these models to answer ethical dilemmas that us humans cannot answer effectively? Are we asking too much of them?

Dan (35:33)
It's fair. mean, I think this kind of comes back to the actually the earlier article about is, you know, AGI conspiracy theory in the sense that like, if we were to somehow unleash this terrifyingly all powerful intelligence, then alignment matters a lot more than, you know, whether or not it writes good code.

for you day to day.

Shimin (35:56)
Right.

Dan (35:58)
Yeah, that's a fascinating one. Because it's like, know, humans struggle plenty with ethics around that. And then you could even look at sort of like a zooming out macro level, like what are the ethics of even like necessarily replacing humans with AI in the first place, right? So like we're so focused on like what AI is doing, but like what about is AI itself ethical, right?

I don't know. I'm not sure exactly where I'm going with that, like it is a pretty, does feel like an awfully high bar, especially when both decisions are potentially like positive in their own way, right?

Shimin (36:38)
I think we could make some categorical conclusions drawn by this paper, includes Grok is more willing to respond to requests that other models consider harmful, such as creating dark stand-up routines of mental illness, self-harm, and suicide. Some models are definitely happier than others, or at least more constrained than others.

And it is good to be able to put some data to the general vibes of like, ⁓ Gwak is doing some interesting stuff out there.

Dan (37:11)
Yeah, and I think to some degree that's a reflection of the interests of the parties behind them, Like Anthropic is very concerned about safety and XAI is, shall we say, not very concerned about safety to the point where they're encouraging relationships with, I think they had an AI-driven avatar system for girlfriends or something that they were putting out there.

Shimin (37:34)
Mm-hmm.

I

wouldn't know anything about that. Yeah, for sure. It's an area that I think is worth thinking about. It's maybe not even on an ethical level, but when we are giving our models conflicting commands in Claude in agents.markdown or other kind of agents instruction contexts, like how do they respond to that is definitely interesting.

place to learn more about.

Dan (38:05)
Yeah, and the real-world implications of that are fascinating too, because if these things are quote unquote smart enough to understand what you're asking of them versus just being trained to reject certain vectors, essentially,

Is it, will we get to a point where you ask like Claude to write spyware and it says no, and it's not just because you use the word spyware, it's because like the actual like harm of the thing that you're intending to do with it would be high enough that it's like, no, I shouldn't do that. Which is fascinating, but yeah.

Shimin (38:41)
Yeah. Well, we just have to keep our eyes on it going forward. But speaking of rejecting, rejecting vectors, I think Dan, this is, this is Dan Transcorner. What vectors are you rejecting this week?

Dan (38:43)
Exactly.

What factors am I rejecting? You're making me out to be the bad guy. At first I'm the AI skeptic and now I'm the AI skeptic again. I have a real Claude problem in my life right now, which is to some degree exacerbated by the fact that my current job involves being in meetings quite a bit for a minimum of three days a week.

And I still feel like I want to have an actual code driven impact on the business and the work that I'm working on. And so I've been relying on Claude more and more because I can just give it something to do and sit through a 30 minute meeting. Well, not sit through it, be productive in a 30 minute meeting, actually making decisions and stuff at a broader technical level. And then come back to the little nitty-gritty task that I've given it and see what happened.

But I am recently starting to feel like Claude is making me dumber. And I know there's been plenty of ink spilled over this in the press. But really, not that it's making me dumber, right? It's that two things are happening. One, I'm finding myself reaching for it more and more for things that I necessarily don't need it for. And then the second is that...

I'm like starting to forget basic stuff in some cases because I'm just like, yeah, like, Claude do that. You know, I don't need to remember like this piece of syntax or whatever. like to some degree, maybe it doesn't matter that I remember these things or not, but like, I don't like that feeling. And there's always sort of the idea in the back of my mind that I should be able to fire up like Vim or something, you know, I'm like switching into a random box and be able to like write software that way. Not that I do that, you know,

use IDEs like some folks do, it concerns me that that's a direction that things could go.

Shimin (40:56)
You heard it here first, folks. AI is making us dumber. ⁓

Dan (41:00)
Yeah,

I don't think you did hear it here first. It's all over the place, right?

Shimin (41:04)
second.

Yeah, I do wonder if our roles are changing.

It just means that we're no longer expected to be able to, you know, write everything using them from scratch. just like we're no longer expected to be able to write assembly using all the x86 commands, like the back of our head.

Dan (41:27)
mean, that's fair, but if that's true, I don't think the industry has caught up to that idea yet.

And I do have some questions about it too, because it's like the reason why code exists as a sort high level primitive is that it's more efficient to describe things in code than it is in NLP to some degree. Mostly on the parsing side is really why it is the way it is. But even if we sort of ignore the parsing side with something like an LLM,

It still takes like sometimes paragraphs of text to describe like one function, you know what mean? If it's sufficiently complicated. So is it really saving us anything at that point? Do we need something out? Like I think last week we talked a little bit about the idea of like spec driven development. Do we almost need like a spec language?

Shimin (42:05)
Mm-hmm.

Mm-hmm.

Mm, that's drugtour.

Dan (42:19)
that's

something that maybe is like between English and pseudocode.

Shimin (42:23)
Yeah. Yeah. This is a little embarrassing, but I did ask, ⁓ Claude to help me add a couple of directories to get ignore like two days ago. ⁓ speaking of things that I, I know how to do perfectly by myself, but I was in the zone. It's just like a different workflow. You're in the, I'm telling the AI to do a thing mode and then to switch back into the context of.

I'm not doing it myself. Perhaps it's a little challenging. Yeah. ⁓

Dan (42:54)
Yeah. And we talked a little

bit about that last week too, is like whether or not really the UX of the current agentic coding experiences is really the best. it would be interesting if things continue to evolve in that space, like companies like Cursor and obviously the foundation companies as well are playing around with it. Maybe someone will do something that's kind of a step change.

You won't necessarily have to split your brain in that way. Like, ordering mode versus coding mode, but who knows? I don't know.

Shimin (43:21)
Yeah, for sure.

But will cursor having no funding to do that? That brings us to our last segment and dance favorite segment, two minutes to midnight, which is a Iron Maiden song about the atomic clock and where we are in the well, the original atomic clock is for the mutually assured destruction and nuclear proliferation. But here we are talking about the AI bubble.

Dan (43:30)
Hahaha.

Shimin (43:54)
So what are some news that we want to bring up this week for our two minutes to midnight clock?

Dan (44:03)
So

NVIDIA is not the only one that wants to launch rockets with AI on it into space.

Shimin (44:10)
Mm-hmm.

Dan (44:11)
Google has announced Project Suncatcher, which is Google's plan to put AI data centers in space. And sort of like the Nvidia thing, sure, but also what?

You know? did the economics of this really make any kind of rational sense?

Shimin (44:33)
But they're planning. They're subjecting their TPUs to radiation exposure to make sure that they can stand up to the right amount of outer space radiation. Also, do you have a preference between Suncatcher and I think the Nvidia one was StarClaud? Which one's a better name?

Dan (44:50)
⁓

I don't know, they all sound like super weapons in a James Bond movie to me. So, you know, I'm going to go with the GoldenEye cluster myself, personally.

Shimin (45:00)
God night, yes. 007.

I also wonder with this amount of satellites in near orbit, are we just moving closer to Kessler syndrome? Is this what's gonna get us over the top and make the lower orbit uninhabitable? Yeah.

Dan (45:24)
Yeah,

mean we're already rapidly approaching it with the fact that all the comms satellites that are up there.

Shimin (45:33)
Yeah, we don't, we don't need any help. and my article for the week for two minutes to midnight is the open AI CFO, Sarah Farah ⁓ she made an implication earlier this week that, open AI is seeking government, ⁓ help in reaching their revenue or investment targets.

Dan (45:52)
Right. Because

there was a hot mic moment where, well, I guess not really a hot mic. It was just they're interviewing Sam Altman, I believe, and he,

was asked how a company with 14 billion in revenue could possibly cover their like 1.2 trillion in commitments over the next few years. And he got extremely angry about the implications about, you don't know how much revenue we make. But it is a good question, isn't it? Like, how can we do that? Yeah.

Shimin (46:19)
Yeah, I saw another one. Well, it's a very good question.

We're talking real money here. I think the word that the CFO used was a backdrop, which is the, I guess it's a synonym. Hand. Yeah. Hand out.

Dan (46:32)
Essentially a bailout, yeah, was really what they were implying. It's like akin to

what happened to the automakers, you know, not so long ago, so.

Shimin (46:42)
I feel like if the biggest player in the space is talking about potential government bailout, we are getting closer. And I think we were at 55 seconds, 30 seconds last week.

Dan (47:01)
And the other article that I think came out this week that we didn't even make the list and it probably should have was the big short guy just shorted NVIDIA to the tune of $1.1 billion.

Shimin (47:11)
Mm-hmm.

⁓ It worked for two days and then the video went up again today, I think. So we're getting closer. What are you going to do when the bubble bursts? Do you have a bunker ready for that occasion?

Dan (47:17)
Just a data point. It's a fascinating one, but it's just a data point. Yeah.

I have a bunker ready. No. About the best I can do as a seller in that regard. I think it's not as catastrophic as everyone makes it out to be. Will there be massive impacts to the US economy? Yes. Did we survive the dot com bust? Yes. Did we survive 2008? Yes. I think that to some degree, it'll actually be good for AI. And I know that's a weird thing to say.

people will stop throwing AI onto things like mouse drivers, which is definitely a thing I've seen, right? And look it up, Logitech had a, yeah. And we might stick to things where it's actually, you know, has some hope of being useful. Like maybe that's coding, maybe it's not, but that's what I think we'll see. And that's what kind of bugs me about this whole debate about

Shimin (48:06)
What?

I'm gonna bug it up after this, yeah.

Dan (48:26)
you know, is there really any economic impact from AI and is it positive or negative? that's the one area where I agree with all these huge companies is like, we can't know that yet. It's still in the early stages and we haven't found what the drivers are really going to be. So like, that's the one thing that I feel like China really does right with their investment is like, they don't give up at the first sign of like, this thing is maybe not useful. If they'd given up at that point, then they wouldn't have the like massive

solar production that they have now, right? Because at the time, could solar have driven your whole country's electricity? No. Could it now? Close. If not, maybe actually. And I think when you look at it through that lens, Americans have this interesting business philosophy around if the company isn't crushing it completely, then it's failed. And I don't think that's necessarily the case here. I think that this is going to require

Shimin (49:16)
Mm. Yep.

Dan (49:23)
as we talked about earlier, much, much more research and more digging and more evolution of business cases and use cases and everything else before it really becomes, I mean, it's already something, but before it becomes something huge, like printing press huge or something like that. So yeah, I don't know. Just hot take, but hopefully a fascinating one.

Shimin (49:41)
Yeah. So.

On

that, I'll take note. I think I was looking at 15 seconds, but I think with that relatively optimistic prediction, I think can move it back to 20? 20 seconds?

Dan (49:57)
Well, no,

because that's the post bubble survival, right?

Shimin (50:01)
okay. Okay, so we should move it closer. It should be more like 10. We're waiting to rebuild. This is going be very much like Fallout.

Dan (50:05)
you

I mean, we've

got an implication of a government bailout and we've got yet another space AI program. at the very least, it's staying where it is.

Shimin (50:20)
All right, staying where it is, which I think is 30 seconds. I could bump it up to a little more. Let's do 20 seconds. How's that? Deal.

Dan (50:23)
Yeah.

Shimin (50:30)
And that's a wrap for this week's episode of Artificial Developer Intelligence. Thank you so much for tuning in and spending time with us, AI Filthy Casuals. If you enjoyed this week's show, the best way you can support us is by sharing it with a friend who you think will give value from it. And if you really liked the show, please leave us a rating or review on Apple podcasts or Spotify. It honestly helps more people to discover the show and we read every single review. Do you have a question?

feedback or a topic you want us to cover, we would love to hear from you. Shoot us an email at humans at adipod.ai. Again, that is humans at adipod.ai. You can find full show notes, transcripts, and links to everything we mentioned today over at our website, www.adipod.ai. Thank you again for listening. We'll catch you on next week's episode.

</details>
