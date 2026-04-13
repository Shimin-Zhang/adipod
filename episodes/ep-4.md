---
episode: "4"
title: "Open AI Code Red, TPU vs GPU and More Autonomous Coding Agents"
date: "2025-12-05"
slug: "4-open-ai-code-red-tpu-vs-gpu-and-more-autonomous-coding-agents"
description: "In this episode of Artificial Developer Intelligence, hosts Shimin and Dan discuss the evolving landscape of AI in software engineering, touching on topics such as OpenAI's recent challenges, the significance of Google TPUs, and effective techniques for working with large language models. They also delve into a deep dive on general agentic memory, share insights on code quality, and assess the current state of the AI bubble."
keywords: "OpenAI Code Red, TPUs, systolic arrays, GPU memory bandwidth, Claude.md, anti-patterns, long-running agents, feature JSON, Puppeteer MCP, agentic memory, GAM, RAG, code reviews, small PRs"
appleUrl: "https://podcasts.apple.com/podcast/artificial-developer-intelligence/id1857109105"
spotifyUrl: "https://open.spotify.com/show/4eDLlGoktxMngPNq9aGqLX"
overcastUrl: "https://overcast.fm/itunes1857109105"
pocketCastsUrl: "https://pca.st/itunes/1857109105"
amazonUrl: "https://music.amazon.com/podcasts/da06d4c3-ecf6-498f-abe3-4d3b00026bf2"
transistorId: "62fec857"
---

In this episode of Artificial Developer Intelligence, hosts Shimin and Dan discuss the evolving landscape of AI in software engineering, touching on topics such as OpenAI's recent challenges, the significance of Google TPUs, and effective techniques for working with large language models. They also delve into a deep dive on general agentic memory, share insights on code quality, and assess the current state of the AI bubble.

## Takeaways

- Google's TPUs are designed specifically for AI inference, offering advantages over traditional GPUs.
- Effective use of large language models requires avoiding common anti-patterns.
- AI adoption rates are showing signs of flattening out, particularly among larger firms.
- General agentic memory can enhance the performance of AI models by improving context management.
- Code quality remains crucial, even as AI tools make coding easier and faster.
- Smaller, more frequent code reviews can enhance team communication and project understanding.
- AI models are not infallible; they require careful oversight and validation of generated code.
- The future of AI may hinge on research rather than mere scaling of existing models.

## Resources Mentioned

- [OpenAI Code Red](https://arstechnica.com/ai/2025/12/openai-ceo-declares-code-red-as-gemini-gains-200-million-users-in-3-months/)
- [The chip made for the AI inference era – the Google TPU](https://www.uncoveralpha.com/p/the-chip-made-for-the-ai-inference)
- [Anti-patterns while working with LLMs](https://instavm.io/blog/llm-anti-patterns)
- [Writing a good claude md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [General Agentic Memory Via Deep Research](https://arxiv.org/pdf/2511.18423)
- [AI Adoption Rates Starting to Flatten Out](https://www.apolloacademy.com/ai-adoption-rates-starting-to-flatten-out/)
- [A trillion dollars is a terrible thing to waste](https://garymarcus.substack.com/p/a-trillion-dollars-is-a-terrible)


## Transcript

<details>
<summary>Show full transcript</summary>

Shimin (00:16)
Hello and welcome to Artificial Developer Intelligence, a podcast where two software engineers navigate the ever-changing AI-enabled software engineering landscape. We are your AI study buddies who use AI every day at work and sometimes we even read papers at night. I'm Shimin Zhang and with me today is my co-host Dan. He's got the memorizer in the closet recording every single conversation. Lasky. Dan, how was your Thanksgiving?

Dan (00:44)
Why is my middle name a nightmare? Is that my first question?

Shimin (00:47)
It's like a elf,

Dan (00:48)
I just yeah anyway, how was my thanksgiving? It was alright. I ⁓ I did the thing where you eat turkey and I ate some ham and in this case the ham has more syllables than you might expect. ham and it was it was pretty delicious and yeah did family stuff. How was yours?

Shimin (00:59)
Is it hot? am.

It was a lowkey, but good. We murdered our own rooster for Thanksgiving. Like the pilgrims, we killed. Well, on today's podcast...

Dan (01:10)
He deserved it.

Shimin (01:15)
We have one item for our news thread mail titled OpenAI Code Red.

Dan (01:20)
followed by a new section and uh...

Look, I'll just say it. It's the hardware hut. It's kind of like RadioShack, but it's a little bit better. In this episode of the hardware hut, we're going to be talking about TPUs, which is the chip made for AI inference era, specifically the Google TPU. And also doing a little bit of coverage about what makes TPUs different.

GPUs. So pretty exciting. And then we'll be following that up with...

Shimin (01:47)
the technique corner where we have ⁓ two interesting techniques this week, one titled anti-patterns while working with large language models and another one about how to write a good Claude dot markdown.

Dan (02:00)
Next up, we'll go to post of the week, where we're going to talk about yet another Anthropic article. They're near and dear to our hearts with their post. This one is effective harnesses for long running agents. And I found that one really fascinating. So probably get into some good stuff there. ⁓

Shimin (02:15)
Yep.

Then we will do a deep dive paper. This week's paper is called general agentic memory via deep research. It is about some of the context issues that we'd run into with our agents and a potential way for resolving them.

Dan (02:32)
And then finally, if you've made it that far into the podcast without taking a nap, I will wake you up with Dan's rants where this week I will be complaining about, well, you just have to wait and see, won't you? That's right.

Shimin (02:42)
I hope you're surprised.

Lastly, as always, we will have two minutes to midnight where we talk about the state of things as we are heading into the end of the year, whether or not the AI bubble will burst before the new year.

All right, let's get started. First up, we have the article, OpenAI Code Red From Ars-Technica. Yeah, this article is about the OpenAI CEO, Sam Altman, our favorite Sam.

Dan (03:00)
Maybe not supposed to be us.

Shimin (03:09)
declaring a code red at a company to improve chat GPT based on reported and leaked internal memo. This is following, of course, the Google release of Gemini 3 and Gemini has been good.

Dan (03:22)
Yep. So yeah, it seems like it's a combination of sort of word on the street. People are overall pretty happy, which I guess you did not quite get that same type of buzz when five one came out for ⁓ open AI's GPT model. then, additionally that the leaked information from the, think it was the, the information claimed that he was concerned about like how well it had bunch benchmarked.

Shimin (03:33)
Mm-hmm.

Dan (03:46)
versus.

chat GPT as well. So pretty fascinating to see the sort of about face that happened too, because, you know, it's only what two or three years ago when Google was having their own internal code red all hands where they were reassigning people to try to make their AI products shine. So it's fun to see how quickly things change.

Shimin (04:07)
Yeah, OpenAI has, of course, chat GPT, is kind of the Kleenex or Xerox of the chat usage of large language models. But according to this article, Google is quickly catching up to chat GPT in user numbers. Chat GPT has more than 800 million weekly use, while the Gemini app has grown from 450 million active monthly users in July to 650.

in October. You can count me in as one of the 650. I've finding I've gemini's my default go-to. It's just so fast.

Dan (04:38)
Is it Gemini user? Yeah.

It's not my default, but I have been using it quite a bit more since the release. It also helped that, frankly, for doing this podcast, I wanted to get more exposure to other stuff. so I've been trying to use more models than I normally do. And that's gotten me using it a bit more than I did. And it turns out that I also, like, they're very, very generous with their usage tiers right now compared to some of the other models. So that helps quite a bit, you know? It's like, okay.

Shimin (05:07)
Yeah, it's a top line model that basically has unlimited usage. I have a pro account and I've not hit any kind of bottlenecks, so I'm very happy with that. And that's interesting, Because OpenAI has been working on the revenue. Or at least the latest feature seems to be revenue targeted with shopping with Sora, which is taking on meta in.

social media and also they're looking, I don't know if this is official or this is just another leak, but they are working on a advertisement integration for chat GPT.

Dan (05:39)
It actually

is somewhat supported by this article as well, the Ars technical one, because supposedly as part of the code red all hands, they paused the ad work. So it got another little mention there on top of the leaks that had happened. I guess that was also this week, wasn't it? That some of the, yeah, somebody had like torn apart the Android app, I think, and found references to ads unreleased in there. So.

Shimin (05:55)
It was this week.

interesting.

Yeah, so I guess they're pulling back on monetization and then focus on having a top-of-the-line model again, which seems reasonable.

Dan (06:13)
Yeah.

At end of the day, it's the model that matters really. Everything else is just glorified agentic flows,

Shimin (06:19)
But also maybe there is no moat right? Because if there was a real moat Google wouldn't be able to catch up so quickly.

Dan (06:26)
Did you learn nothing from DeepSeek

Shimin (06:28)
Right. Oh, that was only I don't know when when the deep seek anniversary was. I wasn't that long ago for sure.

Dan (06:29)
You

298

years ago in AI time, which was like three days in actual real world.

Shimin (06:38)
And I,

so speaking of Google and catching up, I think one area where Google has always had an advantage is in they have their own chips, the Google TPU.

Dan (06:50)
Mm-hmm.

That is true.

Shimin (06:53)
And what exactly is a TPU? I think we referenced it last week and I was like, I know Google has its own TPU, but what is it? Yeah.

Dan (06:59)
I see we're skipping ahead to hardware hot. That's where a small gnome

tells us about the electrons flowing through the heart. Yeah. So this is a really fascinating article. And it was so fascinating that we decided to give it its own segment. it's by a blog I hadn't turned up before uncover alpha. And it's the, the chip made for that, for the AI inference, which is kind of a weird slug, if I'm honest, but for the AI inference era, the Google TPU.

And so one of the first things that I personally didn't really know going into it is what is the difference between a TPU and a GPU? So just a little bit of background It like if you don't know what a GPU is its graphics processing unit ⁓ Started off as like a weird kind of sidecar thing that you would slot in alongside your normal 2d video card and it basically like accelerated 3d Calculations that you needed to render like very early 3d games

Shimin (07:46)
Mm-hmm.

Dan (07:53)
And then that sort of evolved over time into like the massive beasts that you see today that take up like three slots in a computer and use like hundreds of Watts. Um, but right. Yeah. How many FPS do you get? Yeah. So, um, but the GPUs are kind of interesting because, um, they're really great at like massively parallel calculations because you need to do that. So it's sort of.

Shimin (08:02)
And they still couldn't play Crysis. Am I right?

Dan (08:19)
like render a 3D world, right? You think about like, if you turn left or right in a 3D world, you're rotating thousands of points that exist in the point cloud to kind of make it exist in space. And all of those like vector multiplications are, you know, not dissimilar from the type of math that, well, I'll rely on Shimin to tell us the truth there, but like that you're doing when you're doing a inference or other, you know, ML related stuff. But.

The interesting thing about that is that there's also a bunch of like very specific hardware in a GPU that's baked in just for graphics, right? So they have texture mapping and a bunch of other things that are like very specific to, to rendering like games for the most part, or like, I guess you could use it for 3d rendering too. And, ⁓ so when you think about it for machine learning in particular, especially like large language models, most of that Silicon is essentially.

Wasting space And then the other thing that I found really interesting is that when every time you go to do a aforementioned multiply Right. So really when you come down to it both 3d graphics and large language modules They're just multiplying like floating point numbers together, right? So like big decimals And if you don't like this is I guess where my original major in

hardware engineering comes into play a little bit in the hardware. Multiplication is pretty expensive to do on a chip as compared to like, especially integer versus floating point multiplication. Floating point is much more complex to implement in Silicon. And it's also much more costly in terms of machine time than just like purely doing adds. So a lot of times the way multiplication works internally is like, it actually does a series of adds.

over and over, right? You'd think if you're like, you know, three times three, it's like three plus three plus three, right? It's actually what it's doing on the chip. So I know. Yeah. So the thing that I found fascinating is that when on a GPU, when you're doing that, you basically aren't just doing three plus three plus three. You are saying, hey, memory, where's the first three? here it is. Here's the number you're looking for and we'll shove it into the multiplier unit.

Shimin (10:06)
Yep. ⁓ this feels like I'm back in school. Yeah.

Dan (10:26)
what's the second number that I'm multiplying by like the range, right? How many times are we going to do it? ⁓ here we go. That's in a second slot somewhere in memory. Let's pull that out. Unfortunately, the cost of pulling those two things out is quite high in some way. Times it's actually slower than doing the multiplication itself. and so that's really when you hear particularly around if we're

go to Dan's rant from a couple of times earlier about running your own models. One of the things that matters a ton when you're running on your own hardware is like, what is your overall memory bandwidth? And that's why it matters so much, right? Cause you're doing all that fetching. So what is a TPU? So we covered GPUs in probably more depth than we really need to, but yeah, TPU is tensor processing unit. Couldn't actually tell you what tensor means even after reading the article, maybe you know.

Shimin (11:05)
It's always good.

⁓

tenser, tensor just it's a matrix with more than two dimension. So anytime you have dimension of more than two, it's a tensor.

Dan (11:17)
Thank God someone knows what they're talking about in this podcast. It's not me. But the thing they do that's a little different is, well, first of all, they don't have all the extra hardware that we talked about. So there's no texture rendering pipeline. There's no anything related to purely graphics. It's basically just vector multiplication. And then the other thing they use is what they call a systolic array. And.

Essentially, if I understood it correctly, what that's doing is instead of doing that back and forth, like memory in, put it into the thing, do the multiply, put it back into memory, pull it back out of memory, put it back in, you know, and you're going back and forth and back and forth for every set of multiplications. What we're doing is directly going from one step to the next.

So that's what the systolic array goes. So instead of saying A and B and multiply them, it's A and B, and then the output is C, and C goes right into the next multiplication. So for those sort of chained multiplications that you're doing for things in ML, it's much more efficient because you don't have to do all the extra retrievals. So that's TPUs in a nutshell. That's the longest monologue you're going to get out of me today. Thanks, everyone.

Shimin (12:12)
you

Yeah, this reminds me

This is wonderful.

Dan (12:20)
Dance hardware hut deep dive

Shimin (12:21)
I learned a bunch.

Yeah, this is the hardware deep dive in the hardware hut. It's interesting, right? Because when ⁓ you have a whole hardware museum that we can't talk about.

Dan (12:26)
I actually live in the hardware hut.

Shimin (12:32)
So why did GPUs become such industry default when it comes to deep learning? It goes back to around, I want to say 2012-ish, when some labs discovered that when they were working on the ImageNet and ResNet challenges of identifying pictures of animals and birds and cars, cetera, they realized that GPUs are cheap.

for these kind of very parallelizable computation. And so because that discovery, AI labs were able to really drastically improve AI image recognition. And then that kind of just became a legacy part of the ML pipeline. And then they started building the libraries, the Cuda the kernels, all of that stuff.

And of course, like there's...

Dan (13:19)
Yeah, was going to say,

didn't that have a pretty big impact to you? Cause I feel like Nvidia was in this is, well outside of my wheelhouse, especially day to day. like, feel like they were pretty early into the game with CUDA around like running stuff, other other stuff on the GPU besides like purely graphics code.

Shimin (13:32)
Yeah.

Yeah, and Nvidia had the foresight of saying, we're getting these purchases. This is going to be a big thing. We should support it. But if you were to design a chip from the ground up for deep learning, it's definitely not going to be GPUs. And Google realized this pretty early on, because the TPU was started design in 2013. And it was actually released back in 2016.

This is way before chatGPT, even before even the OpenAI was founded.

Dan (14:09)
Yeah,

like Google had, according to the article, which I also found fascinating, they realized that just using traditional ML stuff, which is weird to call it traditional at this point, like real ML, don't know. Things like that they were already using for Google maps, et cetera, or like, you know, labeling content or other things they're doing. They are going to exceed their available compute because they were using CPUs for the compute at that point in time.

Shimin (14:20)
real ML.

Mm-hmm.

Dan (14:35)
in what is it, half a year or something like that. don't know if I remember the exact quote. ⁓ And so they're like, Ooh, we'd better do something about this. So they started something kind of fascinating for a software company, right? They'd started a whole hardware project and it worked.

Shimin (14:41)
Yeah, I think, ⁓

yet.

Now they're on version seven. I think the pull quote was, if every Android user utilizes Google's new voice search feature for just three minutes a day, the company will need to double its global data center capacity just to handle the compute load. ⁓ Yeah.

Dan (15:00)
That was it.

Yeah, which is horrifying.

Having done capacity planning before, yeah, you don't want that. Although I've never done capacity planning and then gone, you know what we need to do is build the chip, but I guess that's why it's good to be the king.

Shimin (15:19)
Yeah, apparently we had Google money. You can build a chip from the ground up. And now they're on version seven, which I think is a huge strength of Google that may or may not be kind of reflected in the way we think about Google's place in the ecosystem. At least not until they came out with Gemini 3. And now we're like, yeah, wait, hold on. Google actually has their own chip, has their own model, has

So many data centers and capacity and some of the best engineers in the world. So how can they possibly lose this fight?

Dan (15:45)
Yep.

Well, it's, you know, kind of tiling to look at the numbers for their performance on the TPUs too, right? Like, so they have TPU V5, which was 459, what, teraflops, is that right? So it's like how many floating point multiplications essentially you're doing per second. And then the jump from V5 to V7, we go from 459 to 4,614.

which is just wild. And then, you you could see the memory scaling up too. So V5, 96 gigs, memory capacity, V7, 192 gigs. But really the overall takeaway from the article out was fascinating was that Google is really well positioned for large language models because of the investment that they've made into hardware that a lot of people haven't had or haven't made themselves, right?

Shimin (16:22)
Mm-hmm. Yeah.

Yeah, definitely explains why Gemini 3 is so fast, in my experience. But just because a large language model is fast doesn't mean you're using it effectively. What are some dos and don'ts when working with large language models? I'm going move on to our technique corner. Here we have.

Dan (16:55)
Alright, that's where you live. I live

in the hardware hut, you can hang out in the technique corner. Or you're put there for punishment, I'm not sure which. We'll see.

Shimin (16:59)
Hang on, Technique Corner. ⁓

We

have an article from Manish, and this is from the instaVM.io blog about some anti-patterns while working with large language models. And by anti-pattern, Manish meant that these are patterns or behaviors we should avoid

Dan (17:19)
which is why Shimin is in the technique corner. He was told to go stand in the technique corner for five minutes because he was doing anti-patterns with his alums.

Shimin (17:24)
because

⁓

exactly. I got to time out because I keep on telling the model that I already told it what it should already know. I personally have done all seven of these, or all five of these, so I can talk about them at length. The very first... just... wrong notes. is not...

Dan (17:31)
You

One, I forgot how to count. Two, I used my context.

Shimin (17:49)
My context was full and again, just like a large language model, sometimes I have trouble counting. Yes. ⁓

Dan (17:52)
Which is why I forgot how to count, I'm... How many Rs was that in

the Raspberry?

Shimin (17:58)
strawberries or raspberries or blueberries. ⁓ The first anti-pattern is, did I tell you that already? So I think sometimes when we get frustrated with large language models, we try to say, hey, remember, we already told you this, or refer back to a previous part of the context. But because a model has a limited amount of context, we should use it wisely.

Dan (17:59)
strawberry yeah sorry one of these days

Shimin (18:19)
never tell your model that you've already told them that.

And the best way to do that is by not sending the same information. And we kind of talked a little bit about this the other week when it comes to code use for Claude is you don't want to repetitively send the same piece of context into the model and back. Try to find good abstractions for them if possible. Yeah. Yeah.

Dan (18:40)
Not similar with MCP as well, right? Cause that's one of the

drawbacks is here's 600 tokens of purely MCP stuff that we're injecting frequently.

Shimin (18:51)
Yeah,

because JSON is the best way to represent any data, of course, with all the brackets. The second anti-pattern is asking a fish to climb a tree. And what this is trying to

Dan (19:01)
I just call that Tuesday.

Shimin (19:03)
Do you have a... Do you climb a tree every Tuesday?

Dan (19:06)
No, I telephish to climate tree every Tuesday. It's complicated.

Shimin (19:08)
Ah yes, your pet fish.

Yeah, I know, I've met him.

Dan (19:14)
His is Gilbert. He doesn't actually exist.

Shimin (19:15)
Surgey.

Well, back to not counting how many times the letter R is in blueberry, you should not ask the large language model to do a thing that it isn't good at doing just because of the way it is trained. So similarly, do not ask Gemini Banana to generate a thing that may be outside of its training context. So rare.

Unlikely things it is going to make assumption based on its training data for the most likely thing, because it is trained to predict the next token and the next token is for the most part the thing that's seen in its training data the most often. So do not ask it to generate an image with a prefix of 1AA because you're going to end up with 1A because 1A is the most likely next token prediction.

Dan (20:06)
Right. Well, and because of tokens, it doesn't really understand the concept of a single A, right?

Shimin (20:06)
And likewise.

Yes, that too. OI!

Dan (20:13)
I guess it's more of an advanced topic.

Shimin (20:15)
It might,

depending on how that A is tokenized, but it is unlikely to tokenize one AA into a token for one, a token for A and then token for another A. It's probably going to do like one A and then a token just for A.

All right, the next Anti pattern is asking LLM to speak when it is drowning. And this is basically...

since the full context of a model is anywhere from 128 to 200,000 tokens in the case of Claude

Dan (20:46)
And what is a token?

Shimin (20:47)
token is on average three letters. That's my way of thinking about like how long a token is. So try to

Um, make sure that you do not use up, um, the entire full context when you're having a single chat session. For example, we, we often talk about, Hey, start a new, uh, Claude code conversation and don't let it compress. Cause when it compresses information gets lost, but even when it gets near that, like you have 13 % context remaining.

performance already degrades. So we would try and just try and use that context wisely and start a new session before performance degrades.

Dan (21:29)
interesting.

Shimin (21:40)
All right, the next anti-pattern titled the squeaky wheel gets the grease.

is another anti-pattern related to how the large language models are trained. So they are trained on a large corpus of very generic text data. So it doesn't know about obscure topics. It does not have data for the latest documentations. So do not ask it for data that is after its training cut-off date.

Do not ask for something that's too obscure. If you want something very specific, maybe like give it documentation or have some sort of a rag set up. So don't rely on it to be an expert for the latest news.

Dan (22:25)
Or even like somewhat more esoteric languages in some cases. We talked about that a little bit in the past as well, where like even something like I'd talked about, I think I chatted about that in here where you use like, I was looking at building some stuff with Pixie JS, which is like old, weird kind of, well it's not old, but it's like based on the old like flash stuff, like Adobe flash back in the day. And,

Shimin (22:31)
Right.

Dan (22:46)
It's not React, right, for building a UI. I was just curious about how well Claude would do with it. And like, it was able to write the code reasonably well. But the thing that was funny was it didn't understand the concept of a scene graph, right, because it's not actually truly reasoning. And at the end of the day, Pixie.js is using a scene graph. So you have essentially children that are like, you know, rendered underneath a parent object. That's sort of whole thing it needs to know.

Shimin (22:59)
Mm-hmm. Nope.

Dan (23:11)
So it would write all this code, but then it would put the add child stuff in the wrong place or omit it completely. And then lie about it being on screen, which I thought was pretty funny. No use, use your, use your MCP to tell me what's on the screen. I can clearly see the red box that I added right there. And I'm like,

Shimin (23:16)
Mm-hmm. Yep.

Wow, that's very funny.

Dan (23:28)
There's no red box, but thank you. Good effort.

Shimin (23:31)
Hallucination is still problem, which is why the last tip is you don't want to be a Vibe coder. It's so easy for us to get into the tell the agent to do the thing mode and not check the work. because these are still, at least as of right now, they are still not actual software engineer level coders. They will hallucinate. ⁓

They will write code that makes sense to someone for some interpretation, but they could be actual security vulnerabilities. So always read the code that it generates. Unless you're vibe coding for a throwaway project, in which case, like, go for it. Have fun. It's fun.

Dan (24:07)
Even then if it's off you

should you should at least look at it. I I actually did some stuff this weekend where I I tried to do like a one-shot full Prompted setup where it built like a very simple I don't know if you're familiar with IndieWeb or not It's kind of outside the scope of this podcast, but pretty cool movement. Check it out IndieWeb pretty fascinating It's basically like small self publishing kind of stuff. Yeah similar and

Shimin (24:23)
Is that the blog rings

Yeah, yeah, yeah, yeah. BlockRings, I've

gotten my share of invitation to blog rings Just saying, I'm cool.

Dan (24:34)
Yeah.

But, um, so I was looking at like having it essentially vibe club coded Indie web servers. So I tried to crank it out and then I read the auth code that it wrote for like Indie auth. And I was like, I am definitely not an expert in auth too, but like, this does not seem right to me at all. So read the code friends.

Shimin (24:55)
always read the code. So yeah, I thought this was a helpful article about what to avoid when dealing with large language models. And we have not one, but two technique corner articles this week. ⁓

Dan (25:08)
Yeah,

so this one was my humble submission this week, which is from HumanLayer, and it is writing a good Claude MD. And I found this one really fascinating because I work in a rather large code base pretty frequently at work using LLM tools. And one of the folks in that

codebase has taken it upon themselves to write a massive Claude MD file. Like the thing is like 40,000 lines. It covers pretty much every single tool that's possible in this monorepo setup, you know, to do all these things. So the number one principle of this blog post was, well, I guess actually the first one is that LMs are mostly stateless. So you really need to,

Shimin (25:32)
Mm.

Dan (25:50)
manage their memory explicitly because they start off not knowing anything. So kind of outside the scope of the Claude, but it's helpful for the rest of the article. And theoretically, the first thing that Claude does, or other agentic systems will frequently read like an agents MD, so pretty similar there, is you're sort of onboarding it to your code base. And I think the key mistake that people make is that really that onboarding is meant to be high level.

Shimin (26:15)
Mm-hmm.

Dan (26:15)
and

not necessarily meant to get into that level of detail. And so as they kind of go deeper into the article, you see that pattern appear more and more and more. And so really they come up with one of the things I found fascinating, is that less, and they have in parentheses, instructions, less instructions is more. So it's very tempting to stuff every single command in there. Um, but their recommendations in this article was that, um, you know, overall frontier models aren't truly

reasoning and so They they can only fit a finite number of actual instructions sort of into Not into context per se but like into the usable Logical window that it's operating on if that makes sense. So it's like sort of like meta context I don't know to describe that better

Shimin (26:55)
Yeah, I like that they actually.

Yeah, I like that they actually have a number here that they can follow about 150 to 200 instructions. So that's a good rough ballpark, I think, to follow.

Dan (27:08)
Yeah. And then the other thing to remember is that the first set of instructions is not even your agents or Claude MD. It's actually the system prompt coming from the frontier provider. then, so that can be 35 plus instructions, you know, maybe even a few hundred lines as well right there. And then you're attacking potentially thousands on, on top of it. And then on, after all of that, you're like,

and also, can you do this thing like adding a text field to this? It's like, yeah. So it's actually kind of miraculous when you think about it that it manages to do that with all the other sort of cruft, with not actually cruft, well-intentioned cruft. Yeah, exactly.

Shimin (27:47)
And I bet a lot of times they are contradictory. Yeah. The

instructions could be contradictory, which would also explain why Claude sometimes ignored, Claude.md Cause it already has all those contacts coming from just the base agent and then the context file. Right. So, at least I run into an issue where it ignores Claude MD pretty frequently. I've, don't know if you've seen, this is a bonus technique.

I saw this on Hacker News the other day and I've actually tried it. Give it a nickname to call you and when it stops calling you that nickname.

Dan (28:15)
What?

then you know it's lost the plot.

Shimin (28:19)
Yes. So

I've actually tried this this past week. I tell the

Dan (28:22)
Well, first of all, most

important question, what was your nickname?

Shimin (28:25)
it's my old Twitter handle. It's also a nickname at work. It's a Sheminsky. It's not cultural appropriation, is it? But it's just a thing. So if it doesn't say very well, Sheminsky, I see you're trying to do this, then I know it's lost the plot.

Dan (28:31)
OK. I don't know. It's just your.

fascinating. That's a good one, I'll have to try that.

Shimin (28:44)
⁓ the other, the other thing I like from this article is the idea of progressive disclosure. I kind of just stumble upon it the other day, or I just diffusing to my brain, but give it additional context for specific areas of the code base to dig into if it's relevant. I find that to be useful.

Dan (29:03)
Right, so it's like read this markdown file if you need this. Yeah.

Shimin (29:08)
Yeah.

And it's smart enough to know when to use it.

Dan (29:10)
Yeah, which is pretty cool. So you can do stuff like how to run the tests in excruciating detail, like how to check coverage, what are the code conventions that we follow, like how to do database migration, whatever.

Shimin (29:21)
Yeah. And you can,

if the test is failing, can tell it to refer to the test markdown and pick up the full context as needed before doing work, which is very nice.

Dan (29:35)
Yeah, so overall nothing really super earth-shattering in this article, but like I thought it was a really nice sort of primer on that topic generally, and I definitely learned a couple things from reading it. Which is what you hope for out of Technique Corner, right? You hope for two things. One, that Shemin is sitting in Technique Corner off by himself, and two, that you learned something. And we hope you learned a valuable lesson about not doubling up your context this week, Shemin.

Shimin (29:49)
I learn something every time.

with my own tin foil hat on.

⁓ I'm still writing. I shall not double my context in the blackboard there.

Dan (30:03)
You

Shimin (30:05)
But sometimes you don't want to use an agent as a code assistant. Sometimes you just want it to do the whole thing as a one shot. How will we go about doing that?

Dan (30:16)
Well,

if only there was this little company you've probably never heard of called Anthropic that loves to blog about their small product. You've probably never heard of, especially if you don't listen to this podcast called Claude. So they wrote yet another, yet another. They've also been writing in their blackboard, um, effective harnesses for long running agents.

Shimin (30:30)
What have those rascals? What have those rascals at Claude did again this week?

Dan (30:42)
So you can kick it off. I've talked too much.

Shimin (30:45)
All right, so the article is kind of a description for a demo that they've released as part of the ⁓ Claude I think, quick start demo repo. That contains all the code to repo the technique or the agent setup that they have. So what the?

Demo does is it generates a frontend and backend for the Claude web UI from scratch. That is the headline news is they are able to get Claude to build Claude autonomously without human intervention. It's pretty cool. But first, they recognize

Dan (31:21)
It's happening.

Shimin (31:27)
the shortcomings of the existing approach for, ⁓ for a one shot kind of code generation, right? There are a couple of problems that they've also run into. we are familiar with these. one called declares victory on the entire project too early. They do this all the time, right? They was, they will see some code being, yeah. Or they, they see, there's a file for integrating API. I guess API was done. Check.

Dan (31:44)
You can clearly see the red box. Okay, Claude.

Yeah.

Shimin (31:56)
even though it is not at all finished.

Dan (31:57)
Green, not just check green check mark emoji in a list of like six things that it came up with. And it will also tell you, this is now production ready, which I also really appreciate. Even if you didn't ask it to write production ready code.

Shimin (32:01)
Yes, always say much.

Yes. ⁓

Everything is always production ready with all the AI agents. This is not anthropic specific. Yes. And the other issue that agents can run into is they will leave the environment in kind of a broken state. As in,

Dan (32:14)
true. I know. And your ideas are always the best.

especially

if you ran out of context and died halfway through. Which they actually kind of cover in this article too, which I thought was kind of funny.

Shimin (32:31)
They do,

yes. They will fail to document the process or they will have some tests broken, but then they will tell you this thing is production ready.

So this demo is there to work through a new approach that they've used to get an agent to clone Claude, essentially. And the ⁓

⁓ and there's actually one more issue that it tries to solve, which is the agent spends too much time trying to figure out how to set up the repo. And this is something that I think we also run into pretty frequently. would spend a lot of time reading the entire repo just to find out how everything works, right? Cause a lot of times, you you have to, you start a new session. If it, if you don't already have it in your

Dan (33:13)
⁓ yeah.

Shimin (33:19)
markdown file about like, here's how to run your test. Here's how you start a server. It will try a lot of different things. It will make assumptions. It will think this is a Angular project when it is not. It will think the build tool is completely...

Dan (33:26)
Mm-hmm.

I never had that happen, but

I've definitely had it like try to run things like the tests and like come up with some pretty fascinating arguments to the test runner that definitely aren't approved. Right.

Shimin (33:43)
Yeah, it still hallucinates at the end of the

day. So their approach is to have a two-phased agent. The first agent prompt sets up the environment and creates a full feature list. Looking at their source code, it asked

the agent to create a feature list of at least 200 features. There's actually a note in there saying you should reduce the number of features if your project is easier. But that's kind of a hyperparameter, which is like a meta parameter when you're training a model. Not just what should be in the prompt, but for a specific project, how many tickets should you create?

Dan (34:22)
I need that hyper parameter for the product people I work with on the regular too. 200 features, are you sure? Couldn't we just do like five?

Shimin (34:29)
200 features.

Yeah. Why don't we just squeeze it up? Just do five big ones. Come on. How hard can it be? So that is the first step. And after creating the 200 features and setting up the environment, then the second agent kicks in. And the second agent has additional instructions in the prompt to get it up to speed.

Dan (34:32)
You

Shimin (34:55)
which includes like look over the features that JSON that is in the directory, see what the progress is are. And also when you're working, after you finished a step, write a short project update document in the base to kind of get the next agent up to track.

Dan (35:11)
the other piece that's

worth noting, I feel like about the feature JSON that I found fascinating was they use JSON apparently because their own internal testing showed that the models were less likely to like mess up or mess with JSON files than they were markdowns. So they store the features in JSON and they also start with every feature having like a pass fail Boolean and they're all set to failing.

Shimin (35:37)
Yep.

Dan (35:38)
So it's sort of

Shimin (35:38)
Yep.

Dan (35:39)
like almost TDD for features. Start red and then go green.

Shimin (35:41)
Yeah.

I've been, I feel like we've been making fun of how context heavy JSONs are, but you know, that actually, is, this, is a point for JSON.

Dan (35:49)
Here we are. the

fascinating thing is the reason for the JSON was that they didn't want the models to mess with it arbitrarily, either declaring victory prematurely as they were talking about earlier. So to me, I found that interesting and fascinating. I wonder how exactly they figured out that that was the thing that made it more reliable. yeah. sorry. ahead.

Shimin (36:02)
Mm-hmm. Yep.

That is interesting. I

was going say it's a combination of JSON and Markdown, right? Because the project progress doc is actually Markdown. So you kind of have the best of both worlds there.

Dan (36:20)
Yep. Right.

But the other thing that was running through my mind as I was reading this too, was ⁓ sort of the technique corners from earlier podcasts were two things I've talked about on there that really resonated with me to being like extremely similar to this. One was using that beads plugin that we talked about, like the Steve Ague one, where like, it's essentially this list, except it's being run by an MCP instead of just like a straight JSON file. And then,

Shimin (36:39)
Mm-hmm.

Dan (36:48)
The second was the catch up command that I talked about where it was basically like, read git, look at the commits that have been done on this branch instead of like overwhelming yourself with the entire code base and like figure out where you're at in the tasks that you've been assigned in beads. So anyway, it's not a hundred percent one-to-one, but I just like definitely seeing some themes there that I think would be good for people to take away as a pattern for how to use these tools effectively.

Shimin (36:53)
Mm-hmm.

Yeah, it's almost like the,

it's almost like Claude is also reading or Anthropic is also reading these blog articles and taking industry best practices and pulling it into their apps and demos. Yeah, that's true too. Yeah.

Dan (37:19)
Or you know using it a lot too, right? I'm sure they

do internally especially when it's internally free, right? It's never free but

Shimin (37:31)
⁓

the other thing that this demo has is they do use, a puppeteer MCP to actually physically open the browser for testing. And I feel like this is part of, at least in the web world, I think this is kind of the direction that we're going to go to is, anti-gravity has this built in as well. which kind of we talked about last week is nothing.

nothing like having the actual feedback of a web browser and be able to interact with it when it comes to testing the features you've built to verify that everything is correct. And speaking of which, there is a section in the prompt to tell the agent that, hey, always run the tests. Yes. If anything is broken, stop immediately and go back and fix things, which is fascinating.

Dan (38:08)
Always run the tests.

Which it's surprisingly

bad at. So I feel like I always have to include that too. Otherwise it assures you that it's all working and production ready. Green check part.

Shimin (38:19)
⁓ yeah. And,

Or it would

just come in all the texts, the tests and say everything, everything's passing now. Or it will read, the tests and then tell you everything is passing. I've seen that happen as well.

Dan (38:34)
My favorite is still

the one where I was trying to get to 90 % branch coverage and Claude took the most fascinating approach possible to getting me to 90 % branch coverage, which frankly I didn't even think of, but it was basically like right a fake test that exercise the function with 100 % branch coverage, like a hundred thousand times to raise the overall average.

Shimin (38:58)
that's smart.

Dan (38:59)
the numerator

essentially. And it worked great, but it wasn't something I wanted to commit for test coverage. But it was a rather creative implementation of tests.

Shimin (39:04)
Yeah, it doesn't actually test the right thing. We will. ⁓

I've also found the code and especially the prompts that ⁓ is listed in the quick start repo to be interesting references when it comes to like, Hey, what are the devs at the big AI companies doing when it comes to prompts? think we don't talk perhaps enough about like if to become a better developer, you should probably read a lot of good quality code.

And maybe to become a better prompt engineer, should read the prompts that the biggest AI companies are out there producing. I especially like that, maybe not like, but it's slightly different. In the prompt for this particular demo, there is a very specific step-by-step guide of what the agent should do.

So for example, you first read the project specifications, and then second, you create the init.shell script. Third, you initialize Git. Fourth, you create project structure. So it's almost ⁓ like a step-by-step recipe as opposed to you are this, you should try and do these things and then let Claude figure out how everything works. Yeah. I wonder if that is something that will become more popular.

Dan (40:16)
Mm-hmm. The order, yeah.

Shimin (40:23)
kind of going forward.

Dan (40:24)
The other part that's fascinating too is that if you look at the sort of fine print on the articles, there were two teams that collaborated internally at Anthropic to write this. And one of them was the RL team. for RL for agents, I guess. it makes me, and the cloud team, cloud code team was the second one. So it makes me wonder too, if like they weren't taking some little bits from RL and applying it there too, which I've long wondered about like the reason if

why Claude did so well with Beads plugin, for example, is because they've already done a fair amount of tuning to make to-do lists important, I guess, in terms of the overall context and flow of things. So be that deterministic or model-level tuning, I don't know. But either way, seems like it has a sort of outsized effect. And so ⁓ it makes me wonder if they'd

Shimin (40:58)
yeah, that makes sense.

Right.

Dan (41:14)
didn't already know that too, know, just from being involved in that team. We're like, aha, well, if we list things out explicitly, we'll have much better results than.

Shimin (41:21)
Yeah, and of course RAL stands for reinforcement learning as opposed to supervised learning or in the case of large language models, self-supervised learning where the answer is immediate, right? We have a string of text. It's trying to predict what the next word would be and the next word, whether or not the model gets it correct, gets immediate feedback that gets back propagated into its weight. But in the case of reinforcement learning,

You don't get any reward ⁓ until the very end, essentially. So for example, if they were to fine tune cloud code for a app creation task, the agent will get no feedback until maybe the entire app has been created. Maybe they have like another agent that calculates the similarity between the actual Claude service and the code that this agent generated and use that as feedback.

Lots of possibilities there, but that is, yeah, that's a very interesting call out.

Dan (42:16)
is RL itself, which in an alternate universe, RL might stand for rarely lackadaisical.

Shimin (42:16)
Alright.

I always like to think that RL models are always flailing around a bit, because that's what you usually see with trying to teach an RL animal how to run, for example. They're always flailing around. I could check him with his head cut off. Cool. Moving on to deep dive. This week, we have a paper called

general agentic memory via deep research, mostly from Beijing Academy of Artificial Intelligence and Peking University, Dan our journey to the best colleges in China continues. Peking, unlike Tsinghua from the last episode, is the other one. If one is Yale, the other is Harvard.

Dan (42:59)
learning so much about.

Shimin (43:05)
And the problem they're trying to solve here is, again, we have an issue of context being a major limitation of our models. If you have too much context, not only does performance degrade, but also you just eventually have to compact things. we all know compaction is terrible for model performance. On the other hand, you have a rag approach.

Dan (43:29)
Not to mention,

task performance. Yeah.

Shimin (43:31)
or task performance.

On the other hand, you have the RAG approach, which is.

Dan (43:37)
Retrieval augmented generation. See, I know some things.

Shimin (43:39)
Good,

because I just blanked out there for a second. And with reg...

Dan (43:43)
Good thing I knew one

thing about this stuff. so what what those quickly go into what that is I know it's for some people that's probably well understood at this point before others might not be so Rag is essentially like you do what? Essentially you can think of it as like hooking Google up to a large language model, right? So you give it the ability to like search a corpus of usually it's some documents that you've prepped ahead of time I'll kind of gloss over the search because we're already gonna get pretty deep into

some other stuff here, but TLDR, it's essentially a search engine for context. So usually when you're measuring performance of, rag applications, you'll typically look at how well does the rag perform versus having the entire document in context, right? So if you were to take like a 47 page legal document about, I don't know, municipal sewer laws in, in Shimin punishment corner, and then compare that to

basically a search tool that says, I want to know specifically about how much sewage is allowed in shimmin's punishment corner. Do you get the same answer? Is it correct? And how well did it score against those two things? So anyway, sorry.

Shimin (44:44)
Yeah, you're making a huge

assumption that I require sewage in my corner, because I don't believe I do. Now, one thing that's well, we need to know about Rag is what Rack does is essentially it does a similarity search like Google. It looks for keywords, but keywords in some embedding space.

Dan (44:47)
It's

tried so hard not to get into

cosine similarity, but here we are.

Shimin (45:03)
⁓ there we go. We're not going to talk about cosine similarity, but it basically finds the query and finds documents that are most similar to it. There we go. Cosine similarity. That's another deep dive corner. the approach here, and they are calling it general agentic memory or GAM. The analogy they have here is it's similar to just-in-time compilation.

So it is a two-step process where step one, you have a agent that acts as a memorizer that takes every single long session you have. It writes a short memo for the session, but also stores the entire context of the session into essentially a database, a page in a database. And then when user is interacting,

with the agent, there's another, sub agent called a researcher that takes the user request. And, and this part is kind of similar to rag, but, instead of just doing a similarity search, it creates a plan. So it creates a plan of this is what, what these are the kind of information I may need. I'm going to search through the memos and search through the page for context related.

to the specific plan and then lastly writes the results out. So it's kind of like a rag but with agent, if you want to think of it that way.

Dan (46:26)
I'm kind of surprised this paper wasn't coming from one of the frontier labs to get you to use more agent calls. Yeah, use more tokens.

Shimin (46:32)
to use more agents.

they were using open source models for this. So maybe it wasn't that expensive at the end of the day. I believe it was using Quen 2.5 and also GPT 4.0 mini. So actually, GPT 4.0, it was using a fairly powerful model. And this was just published. So I guess they had pretty good funding.

Dan (46:43)
Yeah, that's why you use them.

Shimin (47:00)
Overall, it seems to be fairly effective, at least more effective than just a pure rag or just the pure ⁓ context stuffing approaches. Let's see, in the hotpot QA.

Dan (47:12)
Is that the whole document?

Context stuffing?

Shimin (47:15)
context of yes, with ⁓ either the whole document. That, yeah. Or chunking even. It also did. It also has a chunking as one of the other.

Dan (47:16)
Put the whole PDF in there. Yeah, okay, got it.

I actually legitimately didn't know that, so...

Shimin (47:27)
methods where it chunks the full context into 14 agents and then ⁓ each agent produces an answer and see which one is the best. I mean, that's pretty obviously not as good as this approach. So I think really the comparison here is like, it better than rag? Which according to them on their benchmarks, hop-hop QA.

⁓ as an example, it, 64 versus 49 and 51. So better, but not like an order of magnitude better. we'll see how, this approach, if it does make it into, the various AI lamps, but it seems like a fairly low hanging fruit, if I'm going to be honest, like use agent to, to do the one thing in, in rag that is.

just the weakest, that's the weakest part. The cosine similarity, which we're not gonna explain, is the crappiest part about using rag. There, I said it.

Dan (48:22)
so much so that

we could do an entire deep dive on it. Hint, hint, hint.

Shimin (48:25)
Yes. Yeah, I just thought it's interesting that we can trade additional compute for better performance essentially, right? And that's kind of similar. It's the compute time versus memory trade off here. If you're willing to pay for more agents, you can get better performance.

Dan (48:45)
I that's not surprising if you boil it down to that and think about it from that angle.

Shimin (48:49)
simplifying it here. And that's that. If you're interested, take a look. The paper will be linked in the show notes.

Yeah, that's a deep dive corner. And now comes my favorite part of the show. Dan, what are you ranting about? Yeah, because we all know how much it hurts you to rant about something.

Dan (49:03)
Your favorite part.

What am I ranting about?

You know, this one actually really does hurt me. Kind of like right here, like I just feel it in the middles. So on this episode of Dan's Rants, do I say that? I probably don't say that. On this rant of Dan's Rants, I don't know. On this rant, I'm gonna be talking about the fact that code is cheap, inference is cheap.

relatively speaking, but you know what is not cheap Shimin Your time. Your time is not cheap. So what do I mean by all that? it's really the like code reveals still hard, right? And we sort of hinted at that in both past rants and just generally on the show, but what does it mean in the day and age where code has essentially become free, especially if you are a senior.

Shimin (49:34)
Whoa.

Dan (49:52)
for some definition of senior developer. And you are not only creating a whole bunch of code with LLMs, but also in many cases responsible for reviewing a whole bunch of LLM created code that your team is creating. And ultimately, while it's a team sport, to some degree, the buck stops with you in terms of quality, right? As a senior. Not always, but that's sometimes what it boils down to.

The thing that really worries me about all this is that I feel like as an industry, because code has gotten so cheap in the past six months even really, we're losing sight of the fact that code is still a liability. It doesn't matter if you wrote the code. It doesn't matter if an alum wrote the code. Doesn't actually even matter how good the code is to some degree, right? The more code you have in a working application at the end of the day,

increases the surface area for things like bugs for stuff like you know in the distributed system like Contract problems between different systems etc. Like, you know metastatic failures all kinds of stuff can happen in distributed systems. So I Guess my point really boils down to Be kind and just because you have an LLM spitting out this stuff for you or like assisting in your efforts to spit it out

doesn't mean we should throw out good software development practices in general. So like, what's an example of that? Well, like in the teams that I mentor or work with, one of the things I really care a lot about is like getting the team into a daily rhythm where they're pushing out lots and lots of small code reviews. And why I think that's important is actually kind of twofold. And the second one is probably not as intuitive as you might think. So the first thing is maybe pretty obvious, right? Smaller,

Shimin (51:34)
you

Dan (51:34)
PRs

are easier to review. And so I can jump in and look at something and I don't necessarily have to have, you know, consume 70 pages of context, just like an LLM to understand what the heck you're trying to do with this code review. And because it's 70 pages, it's easier for me to miss things. Not that like code reviews are necessarily going to catch bugs, but like might. And even if it doesn't, it's definitely harder for me to consume and contextualize like format and everything else, right? Where I just might miss stuff that,

trying to actually cover in a code review. But the second one, and this is the thing that I feel is personally can be very valuable for at least certain types of high performing teams are when you're doing lots of small code reviews, ideally throughout the day, and you're sort of round robin-ing who's getting them, like to other folks on the team, you're sort of accidentally creating a

shared context about what the entire team is working on. So it's a way of like sort of a sneaky way of reducing the bus factor for any given thing and keeping the entire team sort of aware about what everyone else is doing. So it's almost like if you're doing it right, in my opinion, it's sort of like a continuous ongoing standup where everybody knows what everyone else is doing because you've seen this flow of PRs and they're small enough that if you're curious, you can just click on it and consume it and maybe even review it without having to like, you know,

Shimin (52:40)
Hmm.

Alright.

Dan (52:50)
drastically alter the flow of your day. ⁓

Shimin (52:53)
Mm-hmm.

Dan (52:54)
Just because you have LLM spitting out code doesn't mean you shouldn't still do things like that if that's the way that you're running your team, right? Keep your PRs concise, targeted, small, and human readable because at the end of the day, code is cheap, but your time is not, right? So that context matters. And it can matter a lot in terms of your overall team flow, too. So that's my rant. It's more about software than really.

purely AI, but I think it's sort of, can see where the intersection of the two things hits. And there was actually some really great examples of this on Hacker News this week where this dude opened it like, he like basically vibe coded a feature to OCaml, if I recall. And like the team was so incredibly nice. And keep in mind this is an open source project. No one's getting paid for it.

Like it was like a case study in like how to politely tell someone like, Hey, have you really thought about what you're doing here? Like they were, no one was like, this is slop. No one was any, you know, any comments like that. They were just like, this is going to be very hard to test. If you thought about this, like this is pretty hard to get context on. It's pretty big. Like, you know, they just were very gentle and polite and all these things. And the dude was kind of glueless. And then there was another post that happened.

Shimin (53:42)
All right.

Dan (54:07)
I think that guy actually submitted like no shade to this dude. I don't know him or anything. But like the point is ⁓ gosh, I'm not trying to throw shade I'm just saying like be self-aware right especially when you're using these tools and Where he had submitted another thing like saying how great it was that he was able to like Make a huge change to a compiler himself and I'm like that part is actually true and I get it

Shimin (54:13)
We'll find him and publish his name in a little bit.

Dan (54:33)
But like my point that I'm trying to make in this rant is like, you know, engineering is a team sport always has been, and it's a people sport, right? So like have empathy for the people that are going to consume your stuff, over and above the benefit that you might get out of doing it. It's one thing if you're vibe coding, like a whole bunch of bash scripts that you're going to use on your laptop to whatever, but like, it's quite another, if you're doing something where it's going to impact like,

open source maintainers time like they're doing this for free so like Have a lot of respect for the amount of time and effort that goes into that

Shimin (55:05)
Yeah,

still be human. That's the weeks Dan's Rant right? Still be a human. ⁓ Enhanced. Yes. Yeah, like, it's still important to, especially as these PRs or MRs get longer, it's, I think, even more important to provide a roadmap of how to read the PR. Like, leave those comments now more than ever to help the reader.

Dan (55:10)
even if you're artificially enhanced.

Shimin (55:30)
get into the context to like fully review it. It's almost like

Dan (55:33)
versus just fence

throwing like, I made this. Okay, now it's up to you to tell me that it's terrible or not, you know? It's like, yep.

Shimin (55:38)
Yeah, like the tests are passing. I haven't read the tests,

but like it's, you know, we all know LLMs are great at creating tests. So yeah, no, don't, don't do that. It's almost like if all code is tech debt. And I think to some extent, all code is tech debt. It's almost like LLMs, large language models have reduced the interest rate. So money became cheaper and it's easier to borrow, but the debt is still there. Yeah.

Dan (55:59)
Mm-hmm. It's surf all over again. Yeah,

it's true. Yeah, now we're borrowing at a fantastic rate. you know, you might not see the consequences of that initially, but sometimes, not all the time, but sometimes that comes home to roost in a fantastically explosive way.

Shimin (56:06)
Yeah, I totally agree.

Yeah, and it may not be for a while, but eventually it will. Yeah.

Cool.

Dan (56:22)
So,

should we talk about my favorite Iron Maiden song? It's actually not my favorite Iron Maiden song, but that song is Two Minutes to Midnight, which is where we talk about how close are we to the bursting, not bursting, popping, un-popping, continued growth? Are we even in a bubble at all of the AI bubble?

Shimin (56:27)
LUT

If the Schrodinger's bubble is still alive, then we have news to talk about. I like to point out, well, before we start, actually, we should talk about where we are at our bubble watch. I believe we are at 25 seconds to midnight.

Dan (56:55)
Yes.

And just to reiterate, this is based on the atomic clock, or atomic countdown to annihilation clock that they used in the Cold War era, where midnight is when all the nukes got slung at each other. So typically it was measured in minutes. We're down to seconds. It tells you how optimistic we are right now. See where we wind up this week.

Shimin (57:18)
Yeah, the first piece of news we have is from Apollo, And the article is called AI Adoption Rate Starting to Flatten Out. And the data they're citing are pulled from both ⁓ the Federal Reserve and ⁓

from Ramp AI. And what is interesting here is, especially looking at the federal or the US Census Bureau data, the AI adoption rate by firm size for large firms defined as 250 or more employees, which is the largest band that they're tracking, has actually decreased since June. So the AI adoption rate rate

Um, has steadily increased from 2003 to about June, July of 2005. And it peaked at around 14 % and 25. Yes. Well, that's a 2005. Yeah. But we didn't have chat GPT back then. Come on. Uh, and it has dropped, um, from 14 to 12 % in September. Um, we see a similar trend for, um,

Dan (58:08)
25.

Yeah. No. If I didn't, you might have.

Shimin (58:27)
companies are in the 100 to 249 employee band as well, dropping from 10 to about 9%. With only some of the smaller companies continue to have a higher AI adoption rate. So that seems to not bode well for the valuations and the active user numbers. The second chart we have is from Ramp AI and it paints a

Definitely more rosy picture of AI adoption. All the business segments in Ramp AI's research have been gaining adoption rate, but they seem to have plateaued since around May or July of this year as well.

In the last three, four months, AI adoption rate has plateaued for least some segment of businesses.

Dan (59:14)
⁓ the, the other article that I want to look at this week, ⁓ kind of covers a lot of ground that we've already sort of talked about. so this is from Gary Marcus. It is a trillion dollars is a terrible thing to waste. If that's not a clickbait headline, I don't know what it is. and rather than sort of like give that anymore credence, the part that I found really interesting is I actually didn't.

know that, ⁓ gosh, this is, this is where I really show up as a filthy casual is like pronouncing Ilia's name. Ilia Stutzberg, whatever. So bad. I'm so bad. Yeah. This is where, yeah, we lose all credibility on this podcast. It's just pronouncing names. ⁓

Shimin (59:47)
So let's cover!

You know?

sidebar

since we've mentioned him a couple of times, I actually listened to the podcast that had him on that this interview was taken from. I started listening to the podcast going like, ⁓ I'm finally going to hear how his last name is supposed to be pronounced and the entire two hour podcast. It was not mentioned once. So I still don't know.

Dan (1:00:01)
least one of us does their homework.

Once, yeah. Maybe you know why,

now we know why.

Shimin (1:00:16)
I'm sure we can find it.

Dan (1:00:16)
You

can, of my making fun of my ever changing middle name, you can just try to pronounce my last name. I'll add some more. Why isn't it? cool. So the, the part that I found interesting was really the pull quote, from him that was we are no longer in the age of scaling. are back in the age of research. And I was actually frankly, a little bit.

shocked that he said that, but the more I think about it, the more I think that, well, he started his own lab, his own lab is doing research. So of course he's going to say that, which is I think something, it's a filter I need to apply more carefully to a lot of these sort of like big players in the space where they'll go out and say something kind of incendiary like that. And then if you actually go in and examine their motives, it usually supports

their new spin-off company trying to get a raise, know, their next round race. So that's fair. But you know, the reason why I paid attention to that is like he was on the record quite a bit talking about scaling. if he's saying it's over, to me that makes me stand up and listen a little bit. So I guess kind of on the fence about...

which direction to go from this one, I felt like it was an interesting data point nonetheless.

We see that.

Shimin (1:01:30)
Yeah. And for the

record, ⁓ I think we mentioned this, like two episodes ago, he, he's been on the scaling is over training for, I think like a year and a half. So this is not the first time he's had, he, he's, I think he's had this kind of, announcement, before he even left, open AI. So, yeah.

Dan (1:01:48)
So not a lot of data to go on this week compared to previous weeks, right? In the past weeks we've had earnings announcements and space stations being fired up into space with four kilometer solar arrays. This week feels kind of tame to me. And despite maybe scaling being over, that doesn't necessarily mean that the bubble's bursting in my mind.

Because if anything, means we need more money for the next research, right? So.

Shimin (1:02:15)
Yeah,

I almost want to move it back to two thirties. All right. Thirty seconds. We're getting more comfortable.

Dan (1:02:17)
Yeah, I think I'm actually with you on that. ⁓

Cause it,

yeah, it's that and it's also, you know, this is week to week, right? So it's fascinating to see where we wind up. I do in the back of my mind think that we're still sort of on this precipice, but like, you know, I'm an engineer. Part of my job is to, is to find problems with things. So I'm aware of my biases there.

Shimin (1:02:39)
Yeah, to look both sides when crossing a one-way street, yes.

Yeah, and of course this is not financial advice. You all should not be doing any kind of trading based on this news. We may or may not. Our opinions are our own. Yes.

Dan (1:02:53)
No, all opinions are our own. Don't trade on this. Don't trade in

general really, just buy index funds. That's not financial advice either.

Shimin (1:03:02)
Well, you know, unless you have you're able to get into some of these close rounds for the latest, hardest AI startup, right? In next fund, always safe. And with that, I think we're looking at 30 seconds and also the end of the podcast.

a wrap. Great.

Dan (1:03:15)
Yeah. Thanks again for listening,

everyone. And feel free to check us out on all of our socials. And now YouTube.

Shimin (1:03:20)
Yeah, thank you for joining in

YouTube, even the shorts. You can find us at adipod.ai and you can also email us if you have any feedback, if you have any questions, anything you would like us to talk about, email us at humans at adipod.ai.

Find us on YouTube if you liked it, leave us a review on the Apple podcast or Spotify. Kind of like and subscribe. Yeah. This is the number one developer focused AI podcast in the world. Right. ⁓ that works too.

Dan (1:03:48)
And if you didn't like it, email us and tell us why.

or have your LLM write us an email expanding

the three bullet points of why you didn't like it into six paragraphs.

Shimin (1:04:04)
All right, bye.

Dan (1:04:06)
Ciao.

</details>
