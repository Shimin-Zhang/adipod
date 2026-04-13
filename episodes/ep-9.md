---
episode: "9"
title: "Chinese Models 7 Months Behind US Labs, Token Efficient Languages, and LLM Problems Observed in Humans"
date: "2026-01-16"
slug: "9-chinese-models-7-months-behind-us-labs-token-efficient-languages-and-llm-problems-observed-in-humans"
description: "The podcast Artificial Developer Intelligence features hosts Shimin Zhang and co-host Dan Lasky discussing the evolving landscape of AI in programming, recent news, innovative tools, and the implications of AI on various sectors. They explore the partnership between Apple and Google, the concept of doom coding, and how humans make LLM-like mistakes. The conversation also delves into the efficiency of programming languages, a deep dive into dynamic large concept models, and the societal perceptions of AI, culminating in a discussion about the potential AI bubble."
keywords: "Apple Siri Gemini, Google Apple partnership, encrypted AI, Chinese AI gap, Epoch AI, Anthropic skills, token efficiency, programming languages, Dynamic Large Concept Models, concept embeddings, Egypt, AI travel"
appleUrl: "https://podcasts.apple.com/podcast/artificial-developer-intelligence/id1857109105"
spotifyUrl: "https://open.spotify.com/show/4eDLlGoktxMngPNq9aGqLX"
overcastUrl: "https://overcast.fm/itunes1857109105"
pocketCastsUrl: "https://pca.st/itunes/1857109105"
amazonUrl: "https://music.amazon.com/podcasts/da06d4c3-ecf6-498f-abe3-4d3b00026bf2"
transistorId: "b9a327ce"
---

The podcast "Artificial Developer Intelligence" features hosts Shimin Zhang and co-host Dan Lasky discuss the evolving landscape of AI in programming, recent news, innovative tools, and the implications of AI on various sectors. They explore the partnership between Apple and Google, the concept of 'doom coding', and how humans make LLM like mistakes. The conversation also delves into the efficiency of programming languages, a deep dive into dynamic large concept models, and the societal perceptions of AI, culminating in a discussion about the potential AI bubble.

## Takeaways

- Apple's partnership with Google marks a significant shift in AI development.
- Doom coding encourages productive use of time instead of doom scrolling.
- Public perception of AI is heavily influenced by marketing hype.
- Programming languages vary in token efficiency, affecting AI interactions.
- Dynamic large concept models offer a new approach to language processing.

## Resources Mentioned

- [Google’s Gemini to power Apple’s AI features like Siri](https://techcrunch.com/2026/01/12/googles-gemini-to-power-apples-ai-features-like-siri/))
- [Chinese AI models have lagged the US frontier by 7 months on average since 2023](https://epoch.ai/data-insights/us-vs-china-eci)
- [doom-coding](https://github.com/rberg27/doom-coding)
- [TimeCapsuleLLM](https://github.com/haykgrigo3/TimeCapsuleLLM)](https://github.com/haykgrigo3/TimeCapsuleLLM)
- [Emergent Behavior: When Skills Combine](https://vibeandscribe.xyz/posts/2026-01-07-emergent-behavior.html)
- [LLM problems observed in humans](https://embd.cc/llm-problems-observed-in-humans)
- [Which programming languages are most token-efficient?](https://martinalderson.com/posts/which-programming-languages-are-most-token-efficient/)
- [Dynamic Large Concept Models: Latent Reasoning in an Adaptive Semantic Space](https://arxiv.org/abs/2512.24617)
- [‘We’ve Done Our Country a Great Disservice’ by Offshoring: Nvidia’s Jensen Huang Says ‘We Have to Create Prosperity’ for All, Not Just PhDs](https://www.barchart.com/story/news/36862423/weve-done-our-country-a-great-disservice-by-offshoring-nvidias-jensen-huang-says-we-have-to-create-prosperity-for-all-not-just-phds)
- [Computer scientist Yann LeCun: “Intelligence really is about learning”](https://arstechnica.com/ai/2026/01/computer-scientist-yann-lecun-intelligence-really-is-about-learning/)
- [Are we in an AI bubble? What 40 tech leaders and analysts are saying, in one chart](https://www.cnbc.com/2026/01/10/are-we-in-an-ai-bubble-tech-leaders-analysts.html)


## Transcript

<details>
<summary>Show full transcript</summary>

Shimin (00:15)
Hello and welcome to Artificial Developer Intelligence, a podcast where two software engineers navigate the ever-changing AI enabled programming landscape. We are your study buddies who uses AI every day at work and sometimes read a few AI papers at night. I'm Shimin Zhang and with me today is my co-host Dan. He thinks the pyramids were definitely built by AI. Lasky. Dan, welcome back. Tell us about the pyramids.

Dan (00:40)
Thanks.

Yeah. So, ⁓ I was grateful to Rahul for covering for me last week cause I was gallivanting around in Egypt, which is pretty, pretty cool. Definitely a bucket list trip and

I actually don't think they were built by AI or aliens after seeing them. The scale is definitely staggering, for some reason, it humanized them, seeing it in person. It definitely was like, this is amazing engineering, but it was engineering. I just, I don't know, maybe it's because I'm an engineer that I felt that way, but it was like, yeah, I could kind of see how you do this. It's a huge project for sure.

Shimin (01:16)
you're gonna start building a mini pyramid in your backyard after you've been inspired by the great works.

Dan (01:22)
Have you seen that one just like really crazy TikTok where the lady's like mining and she got shut down for a while? think it's a freaking where it is. It's somewhere in the US actually, she's now she was building a castle and doing all this other crazy stuff. Yeah. So I don't know. It's possible, but yeah.

Shimin (01:30)
No.

⁓ I have seen, yeah, heard about this, yeah.

Seems like very calm hobby. I kind of wanted to get into the mining bit.

Dan (01:44)
Wait till I'm not in a rental before

I start my pyramid building.

Shimin (01:47)
All right. Well, on the this week's show, as always, we're going to start with news, the red mail, where we're to talk about a couple of news items in the AI space. And then we're going to move on to the tool shed where we have a few cool new tools to share. Followed by post processing. We've renamed it with a post pun. We're going to talk about, anthropics skills and also

an interesting post about comparing humans to large language models, followed by Technique Corner, where we're going to debate which programming languages are most token efficient and if it matters, followed by Dan you're going to do a vibe and tell about your experience with Gemini in Egypt.

Dan (02:28)
Yes,

while on vacation or AI on vacation generally, which is a first for me. So that's kind of fun.

Shimin (02:35)
Yeah. And then we'll do a deep dive on dynamic large concept models, a new architecture for large language models. And then comes my favorite segment, Dan's rant, where you're going to rant about something. We'll find out what it is. And then lastly, as always, we'll be doing two minutes to midnight, where we talk about where we are in the AI bubble. Dan, I don't know if you

Dan (02:48)
Mm-hmm.

Shimin (02:58)
Listen to the podcast, wear your way, but we are still at a minute 30 in our AI clock. All right. So let us get started. The very first news article we have today is from TechCrunch titled Google's Gemini to power Apple's AI feature like Siri. So this came out and TechCrunch is not the only one who's reported this, but ⁓ Apple has...

Dan (03:03)
All right.

Yeah, it's quite a few articles.

Shimin (03:23)
Yeah, this is big industry news. Apple has chosen to work with Google for powering its new generation of AI products. I think that's really it. This is a non-exclusive licensing, and Apple would be paying Google about $1 billion to access its AI technology, which I assume is the Gemini family of models.

Dan (03:43)
imagine although I don't think they actually specify that do they in the release

Shimin (03:47)
Yeah. And then the multi-year partnership will involve Apple using Google's Gemini models and cloud technologies for future Apple foundation models. So it sounds like, you know, they still want to have Apple's own foundation model, but in the meantime, while they're building out their data centers and waiting to play catch up, they'll be using Google's software.

Dan (04:11)
The

other part that I found curious about the wording in this is that they don't really specify who's going to be running it, you know, like actually doing execution. So it makes me wonder if they're not just like essentially licensing Gemini to run on their own hardware too. So I don't know. It'll be interesting to see if they talk more about it or more openly about it, depending on, cause you know, like Apple's stance.

Shimin (04:26)
Mm.

Dan (04:35)
particularly on privacy is something they use to try to like differentiate themselves in the industry. And they've also mentioned that a couple of times in the context of AI, particularly like, we do as much on device as we can, but then when we don't, we can't be on device, then we go to our secure, you know, fancy cloud, which is kind of an evolving space. Like I was actually just reading another article, it didn't make the cut today, but about,

Shimin (04:51)
Right.

Dan (04:58)
What is that guy's name? Marlin Spike, the dude that wrote Signal, or Pioneered Signal. Moxie Marlin Spike, there we go. And I guess they're starting a new encrypted AI startup where all your data is encrypted at rest and on the CPU while it's being evaluated, which is kind of an interesting thing. So it's supposed to be like a secure chatbot style.

Shimin (05:04)
Yep.

Yeah, I would definitely be interested in that.

Dan (05:25)
Yeah, I mean, to their point, like so much of your data goes in there, right? Like you could really generate an excellent marketing profile on someone based on the questions they're asking.

Shimin (05:35)
Yeah, and always, know, especially if you're constantly asking AI, you know, how to make a bomb or I know, know healthcare questions have also been the privacy of ⁓ using AI for healthcare questions. I definitely do a double take whenever I, you know, trying to ask the AI for something health related. It's like, is this a HIPAA violation? Yeah.

Dan (05:41)
You

Mm-hmm.

Yeah, is yeah,

is chat GPT or is HIPAA compliant? Probably not.

Shimin (06:01)
Right.

Dan (06:02)
Do they need to be as soon

as you start asking that question? I don't know.

Shimin (06:06)
But yeah, I also think I haven't heard much about Apple partnering with data center companies similar to we have with especially OpenAI and Anthropic and GROK for that matter.

Dan (06:17)
Yeah,

there was a little bit about like they were talking about using, I think it was like the M4 chip in like a custom rig that they were building. Like purely when it went back when they were like convincing everyone that Apple Intelligence was going to be a thing that they were going to be doing their own like build outs using Apple hardware for it too. And it's like, I mean, I know people are that are doing

Shimin (06:29)
Interesting.

Right.

us.

Dan (06:45)
like open-weight stuff or even training are using like Mac studios for it. Like I've seen rigs that have like four Mac studios stacked on top of each other. like quickly you can use it for that stuff. They got pretty good memory bandwidth.

Shimin (06:50)
All right.

Yeah,

right. So I guess, yeah, this is evolving. So we'll keep on following the situation. yeah, also, is there, are there, like, antitrust implications with this? Like, I guess there are sufficient enough other AI model companies. But if Apple defaults to Google in the same way that it

Dan (07:04)
Yeah, we need to see where it goes, but good to see Apple getting in the game, you know.

Shimin (07:23)
the false Google for search. Our next item comes from Epoch AI, titled ⁓ Chinese AI models have lagged the US frontier by seven months on average since 2023. The main article is basically that, that according to your research, that the Chinese models have been on average. But.

Dan (07:39)
And title.

Shimin (07:42)
There's a nice chart comparing the models and they determined that the minimum gap is 4 months and the maximum is 14 months.

Dan (07:51)
Yeah, I also thought this was interesting because you can kind of compare the the chart compares like the generations of each of them to by name. So you've got like GPT-4 up against I don't I've never actually never heard of that one. How do you print it by by Chuan-2 13B? I don't know. Quen-14B I know. And some of these other ones I haven't heard of. And then like

Shimin (08:12)
Yes.

Dan (08:15)
They're saying like deep seek B2 up against like a one mini and one. So I don't know.

I'm not sure I 100 % agree with some of the chronology of the timeline, but it is fascinating and I think goes to confirm some of the, like, I guess, non-scientific thoughts that I had about open weight models. it's like, kind of what is their performance like? And they're pretty all right, but always behind, you know? So it's nice to see someone that is actually a scientist coming up with that info too.

Shimin (08:28)
Mm-hmm.

Yeah, I think there are talks that some of the Chinese models were being trained on the output of the proprietary models. If that goes into training data, I could see how they can catch up rapidly. But we've also talked about some of the new architectures coming out of the Chinese frontier labs. So they are doing frontier research. even if some of the training was from the closed-source models,

Dan (08:54)
Mm-hmm.

Shimin (09:12)
There's real innovation happening. If the line ever crosses though.

Dan (09:14)
Yeah,

and I don't know if they didn't, at the time that this was authored, if they didn't have that or not, but I don't see some of the big, like what people are considering state-of-the-art right now on there either, right? They pretty much stop at like Quinn 3 Max. And there's definitely been some of the that Xi company we were talking about a couple of weeks ago is making some pretty...

Shimin (09:31)
Alright.

Dan (09:38)
solid stuff that people are excited about in the open weights world.

Shimin (09:41)
Yeah. And then lastly, I didn't read into too much of the methodology of, what they're using for performance, right? Like, are we talking about benchmarking or something else? Yeah.

Dan (09:48)
Right. Yeah, that I didn't either. And the one thing I

did do that I was kind of curious about is like, is Epoch AI? Like, and do they have any motivation to be pushing US frontier models? So they do have an about section on their site and it's a nonprofit. and they're trying to, their mission statement is fostering a rigorous understanding of the future of AI. And if that means something to you, then ⁓ I can buy you a new car or something. don't know.

Shimin (10:14)
you

Dan (10:15)
But they did publish all their funding too, which I thought was kind of fascinating. I didn't see any like obvious conflicts of interest in the funding for it. But I don't know. It's kind of weird. Like part of me is like, how do get that job where I just work for a nonprofit and play around with models? Yeah, true.

Shimin (10:28)
They have a careers page. They're hiring

some contractors for design and data scientists for what that is worth, which we're not qualified to do, unfortunately. All right, let's move on to the tool shed. Our very first item is Doom coding.

Dan (10:35)
You

Doom coding.

Shimin (10:50)
Then why don't you introduce this item?

Dan (10:53)
So there's really nothing to, at least to me, not too new here. But I think it was useful to just sort of say some of it out loud. So the author of this somewhat funny GitHub Read Me, which the whole quote unquote article is basically a GitHub Read Me, was like, stop doom scrolling. Start doom coding. And the idea is essentially,

Instead of spending your idle time on your phone reading terrible news or whatever, could spend it massaging your favorite AI-based terminal program into writing some software for you. The gist of it is kind of straightforward. I'm sure everyone's probably already thought about this, but it's basically like, install

The reason why tail scale is that it's pretty easy to set up and get some sort of always on internet connected machine hooked up to your phone. then, so you're essentially on a LAN with each other and you can SSH into that machine and then run Claude or Gemini, whatever you want on there and basically vibe code on that machine. And then they had recommendations for like what terminal program to use stuff like that.

I have my own recommendations there. We can talk about it on a different show if you want. Or write us an email and I'll send you six paragraphs back about terminal stuff. But yeah, I think it's a cool idea, which is like, you know, the ability to kind of take this whole show that we've been talking about on the road, so to speak. like, you can do a lot more on your phone than in this environment than you.

Shimin (12:17)
Eh-heh.

Dan (12:22)
would have been able to struggling to try to like, you know, type out code on a terrible software keyboard. But it's pretty fine to type out prompts for, you know, an LLM.

Shimin (12:32)
Yeah, and like any real programmer, is a picture in the repo for Doom coding at the club. That sounds like something I would be interested in doing. ⁓

Dan (12:40)
Yeah, that was

pretty funny. The screenshots of where they're doing this. They're like not. It's like pictures of them holding their phone with Claude Kodana in different places. So we had code in the air and we have airplane windows like pretty good code on a run and there's like a crosswalk and stuff. And then there's Claude on his iPhone. And then, yes, even code at the cloud. It's like blurry cam of dark shapes of people and some

lights and then there's Claude Cote. It's pretty great.

Shimin (13:11)
Yeah,

I think it was the Hacker News discussion for this link. Folks also throw out the idea of maybe using terminal on your phone is not the right way to go. Maybe it should be email-based vibe coding, where you spend time composing an email to cloud code. This brings up a larger train of thought and set of tools that I haven't really spent too much experience

time experimenting, maybe just like how using your laptop and the physical keyboard may not be like the ideal way to conduct by coding sessions. Voice command based prompt generation or by coding is something that a lot of folks recommend.

Sometimes it's just way faster to say what you want rather than like typing out the whole thing. ⁓ like directory structures, not with sending.

Dan (13:55)
type it all out. I mean, I type pretty fast, yeah,

that's fair.

Shimin (14:01)
Yeah. And we can probably rethink our entire interface with code now that AI is a thing.

Dan (14:07)
Yeah, true. Well, I'm also just fascinated by the idea of like, I've always been fascinated by the, the, like mobile coding because you never know when an idea is going to hit you. Right. I mean, like there's a reason why shower thoughts are called shower thoughts, you know, and phones are waterproof these days. like whatever, but, you actually melt your phone, but I just think it's neat to, to have that capability. And I've long wanted like,

Shimin (14:14)
Mm-hmm.

Not if you don't take showers.

Ugh.

Dan (14:34)
the ability to write like real software on mobile. And I think this is kind of a cool unlock to be able to do that. There's also a couple other, I mean, just ball around the topic, couple other things I played around with. There's a app called happy. I believe it was open source and it basically wraps Claude code and lets you supposedly run multiple sessions. I've only used it twice because I found it to be pretty buggy. Like it's supposed to like ping you and send you a push notification when Claude wants input.

And it doesn't work particularly well, it's open source. you know, I guess we could fix it. And then there's two other ones that I've seen recently also on the hack and use there's like bit rig and I think there's one called like actually vibe code for iOS. And the whole idea is it's basically like, wrote a scripting environment for, or like a scripted

Shimin (15:05)
fix that.

Dan (15:25)
not explaining this well. Like typically Swift is compiled, right? But they basically made a Swift interpreter. That's what I'm trying to say. A little fuzzy coming back from vacation. And then hook that up to, it looks like, it feels like it's Glog code to me on the inside. And it can then run Swift code that's been essentially vibe coded.

Shimin (15:29)
Mm-hmm.

Gotcha.

Dan (15:47)
Locally on your phone via the interpreter so you can basically vibe code local apps to use for like whatever So it's like I've always wanted an app that like Combines a Pomodoro timer with an egg timer because I'm just not happy with it, you know, it's like, great you now you can vibe Good 15 seconds Yeah, it's pretty cool

Shimin (15:54)
that's super cool.

⁓ Yeah.

We're

seeing this Cambrian explosion of AI related apps, of ways to interact. So super cool.

Dan (16:13)
Yeah. And, you know, as

the article stated, better use your time than doom scrolling. Build something instead of consuming.

Shimin (16:20)
I

Agreed 100%. Yup. This is why I don't have an iPad. Okay, moving on. We have a tiny capsule LLM.

Dan (16:25)
You

time capsule.

Shimin (16:33)
Did I say tiny capsule? I meant time capsule. Yes. This is a large language model trained only on data from certain time periods to reduce modern bias. And I'm looking at the GitHub repo right now.

Dan (16:35)
You did. Yeah. Time capsule.

It's not just certain time periods, it's 1800s language and behavior.

Shimin (16:57)
Right.

It seems like a fun personal project by the user, HiKateGregor3. Sorry if I'm butchering that username there. But it is a large language model trained from scratch using the, yeah, like you said, data from 1800 and 1875. This person actually gone through three iterations, first via Nano GPT, then via the Microsoft Fee.

And lastly, with Lama for causal LLM. I think this is a really interesting experiment. I'm not exactly sure what kind of modern bias is removed by only training on old-timey data as opposed to fine-tuning on old-timey data.

Dan (17:36)
You

That's true. The part that I found fascinating about it is like, and maybe this is just because I've been spending a fair amount of time in, you know, 3000 plus year old structures in past two weeks, is that like, it really could make history accessible in a way that it kind of isn't.

Shimin (17:55)
Mm-hmm.

Dan (18:02)
right now to some people by literally just having a chat with historical figures, which I think would be kind cool. I mean, of course, all the typical stuff about AI applies. Half of what it's going to say is made up and blah, blah. But I don't know. I just thought it was neat. What if you could talk with Abe Lincoln or something like that?

Shimin (18:22)
But then you wouldn't be able to ask Abe Lincoln how he feels about the Twilight movies. I mean, I'm just saying. There's some fun stuff you can do with a fine-tuning approach.

Dan (18:30)
Well, you would get a historically accurate answer,

like what's a movie? Probably. I would hope anyway. I don't know.

Shimin (18:34)
that is true. That is true. Yeah.

⁓ it is, it is very cool that the dataset, ⁓ is also released. So you can do it, do it yourself, repo it if you were to want to do that.

Dan (18:47)
And I think that was the real reason why this like made tool shed is like, it's pretty cool that just like some random person can crank the tools exist now to be able to like crank out your own LM from scratch on such an oddly specific topic.

Shimin (19:03)
Yeah, I remember when I was working on my own version of ⁓ kind of like the nano GPT by use my own training version of the GPT. I was using like all of Jules Verne's novels from project Gutenberg as its training data. And, and, know, even though V1 and V2 were

trained on a 100 that were rented. It's still very much feasible with tools like Lambda lab. You know, it's, doesn't cost that much in the grand scheme of things.

Dan (19:25)
Mm-hmm.

Shimin (19:30)
All right, on to our post-processing segment. ⁓ Our first article here is from the blog Vibe and Scribe titled Emergent Behavior When Skills Combine. And the post essentially talks about the user's experience of creating one-off skills with Cloud Code.

Dan (19:39)
scrap.

Shimin (19:53)
And then seeing that clock code can invoke additional skills in the middle of utilizing one scale and crediting this as the emergent behavior. On the one hand, I think this is really cool. I think you may say, we already know LLMs can do...

But on the other hand, think this is what really separates human intelligence from what we think of as traditional machine learning, right? Like this general ability to have a set of tools and be able to kind of do a...

research of like, I'm gonna go down this path using this tool, but then halfway through, like maybe this tool isn't enough. Let's see if there's another one that can serve the process that really shows the power of skills.

Dan (20:28)
Mm-hmm.

Shimin (20:38)
What do you think of this?

Dan (20:38)
Bye!

I don't know.

I don't know where to go next with that. Yeah.

I guess I was hoping for it to be a lot more emergent than what they were kind of describing, if that made sense. Like really novel combinations of it. I guess it didn't come out to be. I didn't feel it. I was a little underwhelmed. I didn't feel like it was that novel. Maybe I've just been using that kind of stuff too much to.

Shimin (21:02)
I think the real hard part is large language models are probably not smart enough to effectively use the tools yet or know when to call the right scale.

Dan (21:11)
Yeah.

Shimin (21:12)
but we don't know where things might be three years down the line, right? So.

Dan (21:16)
And when we did that sort of skills architecture deep dive, I was really fascinated by how little information they're actually given about each skill. know, so it's also not super surprising to me. Like when you think about how verbose MCP is, which is like, know, why everyone's always complaining about the token usage, because of the definitions of the MCP stuff, right? It's like skills are much more bare bones. Like you basically get that like one line description. So it's like,

Shimin (21:40)
Mm-hmm.

Dan (21:42)
I don't know if I'd be able to choose which one to use from that either, see human. Yeah. Which.

Shimin (21:44)
Right.

Yeah, so if we can

do better, yeah.

Dan (21:49)
which kind of leads us into our next article, which I thought was just, there's a lot of ha ha com content this week I'm noticing. And this is one of the, which is LOM problems observed in humans. it's from a blog called embed without the missing some letters. That CC and

I just thought this was hilarious because like I've long mentioned this, like we've talked about like sometimes, you know, LM's will just get something wrong the first time. I've my personal hypothesis for that is like, well, if you train it on a whole bunch of human data and humans are frequently wrong the first time, like it's always going to be wrong too, right? Like it's monkey see, monkey do. So having someone else notice that and comment on it, it's sort of a broader scale was, I thought was kind of funny. So yeah.

Shimin (22:11)
Mm-hmm.

Alright.

Dan (22:36)
The first one really got me too, I'm not gonna lie. the first things that LLMs do that are observed in humans was don't know when to stop generating. there's probably a reason why you picked me as a podcast co-host. So guilty as charged.

Shimin (22:44)
Yep.

I thought about making a joke about, though that would just stop generating as our intro, but I thought that was too mean and I wouldn't do that, even as a joke. ⁓

Dan (23:00)
I mean, you'll be discharged,

you know.

Shimin (23:02)
So that's the first one, right? There's a bunch more. Yeah.

Dan (23:02)
It's fair.

Yep. Small context

window, which is funny. I guess, like, you kind of talking about humans, limited attention and everything else being very similar to narrow of a training set is interesting. I'm not sure I 100 % agree with that one because I know some like very polyglot people, but yeah, repeating the same mistakes.

Shimin (23:29)
Yeah, I'll agree with that one.

Dan (23:31)
Definitely guilty as charged. Failure to generalize, also probably guilty as charged.

Shimin (23:31)
That one absolutely. Yeah, definitely absolute.

Yeah, failure to apply to specific situations. You can have both. You can have failure generalized and then failure to apply to specific situations. Although I guess it depends on the RNG gods. And lastly, persistent hallucination.

Dan (23:55)
Yep, plenty of that going around.

Shimin (23:57)
Yeah, it's really easy to go into the, you know, what is truth kind of debate, right? Like you can't really remove hallucination unless you have some definition of objective truth. And large language models, which are essentially zipped up files of the web, like that's only going to be as good as what humans have generated.

I first read this article's title, I thought it might be talking about how humans have picked up certain failure modes from large language models. And then I thought about it, was like, yeah, surely that is coming in the next year or two once you kind of gather enough data points. I think that's more interesting.

Dan (24:40)
Especially as like it or not, it's very easy to outsource your thinking. Which I think there's many things that it's acceptable to outsource to LLMs, at least with today's stuff, but thinking is maybe not one of them.

Shimin (24:51)
Yeah, moral dilemmas, ⁓ which is why I think everyone's trying to grab as much market share as possible in the AI world. Yeah. All right.

Dan (24:54)
Mm-hmm.

them.

Shimin (25:03)
Anything else you have for this one?

Dan (25:04)
No, yeah, it wasn't super deep, again, just one of those articles where I just had some of these thoughts floating around and it's fun to see other people thinking the same thing. ⁓

Shimin (25:17)
I definitely

think it's a really interesting reconceptualization of the large language model issues that we run into. The comparison is not some sort of objective platonic truth for whatever AGI God, but it is like, how does it compare to other humans who we interact with every day? yeah. All right, onto our technique corner. We have an article from Martin.

Elderson titled, which programming languages are most token efficient? ⁓ Martin used a dataset called Rosetta code to do a comparison of how token efficient different languages implementation of the same program is. And some kind of top level highlights.

⁓ Closure is the most token efficient and C is the least token efficient. ⁓ Which is not that surprising. ⁓

Dan (26:11)
You

And interestingly, Python

just beat out Haskell.

Shimin (26:18)
Yes, that is interesting.

Dan (26:20)
⁓ yeah. And then there was a little bonus round where after publishing this, guess some folks wrote in and they're talking about APL, ⁓ cause it has, you know, it's very terse apparently, and apparently it uses unusual glyphs. I have never used APL heard of it, so I didn't know that. And, those glyphs don't encode particularly well to, to tokens. So it actually requires multiple.

Shimin (26:21)
Yeah.

Mm-hmm.

Yeah

Right.

Dan (26:47)
So that damages it, which is kind of funny.

Shimin (26:50)
So I was going to

mention this when we were talking about Python as well. Earlier versions of chat GPT was very bad at writing Python because of the spacing. Each space became its own token. But later on, they optimized the tokenizer so that 16 spaces or 18 spaces became a single token. So I wonder.

Dan (27:03)
Mm-hmm.

Shimin (27:13)
if the tokenizer also just made Python more terse as a language or more efficient.

Dan (27:19)
Yeah, so

they did list. So they used Zenova GPT-4 tokenizer from Hugging Face, which is a community port of OpenEyes GPT-4 tokenizer. So it's cool that they stated it, but...

Shimin (27:31)
But we still have to probably dig a little deeper into the actual tokenizer. There are few kind of broad strokes we can make about the chart. Like static languages are less efficient than dynamic languages. I was kind of surprised that JavaScript is the ⁓ least efficient of the dynamic languages. Maybe not that surprising.

Dan (27:46)
Mm-mm.

Shimin (27:55)
But Ruby came in third, which I love because I have great love for Ruby. And I think it's a beautiful language because it's so efficient. I'm going to use that for the language debate. And then Julia came in second. I haven't had too much experience with Julia. I think it's mostly used for data science work. But that's really all I know.

Dan (28:15)
And then out of the

sort of C shaped languages, generally PHP surprisingly came out ahead. Maybe not so surprisingly, because I feel like Long has had the most sensible naming of things, if you say what you want about the rest of the

And then so that, yeah, then followed by JavaScript, followed by Java, Rust, then go C sharp, C plus plus, and then last is C. yeah, kind of interesting. It makes me wonder like how far out we are from someone intentionally designing either like a new language or like a new language slash model pair where like they're both kind of like intertwined to be really efficient.

Shimin (28:37)
All right.

Yeah.

Dan (28:55)
writing it and then seeing where that takes us, right? Because where we are today is kind of this weird.

thing where we've taken all this existing stuff and just trained based on it. But I'm like, what if, what if you go truly special purpose with that game? Would we even gain anything from doing that? So.

Shimin (29:05)
Right.

The author also talked about maybe we would choose different languages based on how efficient they are for LLMs to use. But there's also the flip side of that coin, which is how much bad example of code there are in the training data for this particular language. I'm looking at you, JavaScript, and potentially probably Java too, and maybe PHP.

Dan (29:30)
Mm-hmm.

Shimin (29:35)
you know, to talk about a creating a new language that's just for AI, like you can create a language with only, only good code and only have training data of like beautiful language X and everything it writes. since if we're to no longer actually put hands on keyboard, we can emphasize readability, for example, in this new language.

I think that'll be really cool. I will be the first to learn that, but yeah, I'm not.

Dan (30:01)
If it works well,

yeah. Or you wouldn't need to learn it at all because the LLM would be so good at using it. You could just vibe your way to freedom.

Shimin (30:08)
⁓ I'll learn to read it. I'm not going learn to write it. Let's get real.

Dan (30:10)
Yeah.

Yeah, I mean, the only other thing that I think is worth chatting about there is that like, it's funny that we've reached the point in software engineering and I guess we're in 2026 now where you might actually stop to consider how token efficient is your language because you could get more done in a token window in a more efficient language before you have to.

sort of reset or clear or do any of the tricks that we've talked about before. So in practice, I don't think that matters that much because let's be real, you're probably a software engineer just like the rest of us that's working on a team and engineering is a team sport. And a lot of decisions went into those language choices to begin with. And there's probably a large established code base that you're working with. that's what's really dictating it, but just fun thought experiments.

Shimin (31:07)
Yeah, it is crazy how quickly things are developing that we're starting to optimize on the edge here. Instead of waiting for the context window to get larger, we're like, what if we make our code more efficient?

Dan (31:20)
Yeah.

Shimin (31:20)
You have some vibing.

Dan (31:20)
So

yeah, so this is maybe stretching the definition of vibe-thiving because we're not really vibe-coding anything. But as we mentioned at the top, I was spending some delightful vacation time in Egypt. this is really the first vacation I've been on where AI has been super accessible and has gotten really good. So I ran a couple of experiments. ⁓

On the very first day of my vacation, was in Cairo and we didn't have like a super solid plan for the first day. we wound up going to so this is maybe a little bit too much info, but like they opened this new museum called the Great Grand Egyptian Museum, which is great. There's like so many pieces in there. But the original one was, think, just called the Egyptian Museum. I know it's super confusing, but and it

Shimin (32:07)
Mm-hmm.

Dan (32:09)
is like older to the point where like the museum itself is almost a museum because like the display cases are like original like wood and stuff like that and there's like hand typed things and I don't know it's pretty cool but the weird part was like a lot of the stuff in there wasn't labeled so I was taking you know tons and tons of pictures of everything and I'm like

Like in particular, the one piece I was fascinated about is like there's this big hall in the middle and there's capstone. What it looked like to me, like capstones of pyramids in there. And I'm like, what is this? There's no label. There's not even a number to like look it up or anything. So I took a picture and I fired it into Gemini as one does. And Gemini not only identified it, but it told me which like historical side of

the pyramid I had taken the picture of, like, oh, that's the west face of the capstone. Would you like me to read the hieroglyphics? And I was just like, you know, normally it's like, OK, cool, whatever. And I'm like, you know, sure, let's just try it. Now, of course, I'm I can't read hieroglyphics. I have no way to fact check this whatsoever. But like it seemed like it did a pretty good job decoding it. I don't know. I thought that was fascinating. I never in a million years would have thought to like

Shimin (33:02)
wow.

Dan (33:24)
shoot hieroglyphics into Gemini, yeah, seemed like I did a good job. And then the other smaller and possibly way more apparent use of AI that I did was, so pretty decent time change between Egypt and the States. And so on the way back, I had a really convoluted flight schedule. was basically like three different flights or four to get.

Shimin (33:41)
Right.

Dan (33:47)
back home and I was like, how do I manage sleep, particularly trying to like with an eye towards trying to reset jet lag schedules, you know, around this. I took my entire flight or tinder and dumped it into Claude. And it was like, I suggest sleeping while you're in Paris from this time to this time. So I did that and I came home and I'm, I'm actually doing all right. Like I got back a few days ago and like,

Shimin (33:49)
Ew.

Uh-huh.

Huh.

Dan (34:15)
I'm not 100 % over jet lag, but I'm conscious enough to be able to do this podcast. So just different interesting little travel usages of AI.

Shimin (34:17)
Yeah.

Right. That's impressive.

We should use charship it here a little more. feel like.

Dan (34:33)
I heard

that. I was catching up. mean, I was, you know, didn't have access to unmetered data or anything while I was gone. So I'll admit to not pulling the latest episode until I was back in the US. I've listened to about 75 % of it and I've heard from our guest co-host that we have a pretty big bias towards Gemini and Claude, which is true. I mean, I think we're...

Shimin (34:58)
Which is true, yeah,

absolutely.

Dan (34:59)
We fully

acknowledge that on the show, but yeah, we should use chat.

Shimin (35:02)
That's my New Year's resolution.

I'm gonna throw a little more love to Chachi BT. But not Grok. I still refuse to use Grok. So there's that.

Dan (35:06)
He's trying to be funny.

especially after

the latest, which we did, you know, carefully did not cover and won't talk about right now in the news thread mill.

Shimin (35:18)
No, I don't want to put

an explicit tag on the podcast, that's for sure.

Dan (35:23)
Yeah

Shimin (35:23)
Having that powerful of a piece of technology in the hands of pretty much anyone on earth will do a great job in terms of raising the bar for everyone's educational attainment. Anyone can read hieroglyphics now. But, and this is the big one, just like...

how internet didn't actually raise the intellectual bar of everyone on the planet, arguably lowered it. ⁓ Yet you'd be seeing what the impact of that would be. But if you use it well, absolutely. Yeah, it's extremely powerful.

Dan (35:51)
You

Yeah. And it was, it was just, I don't know, something it kind of blew me. Like it was one of those like moments that I felt like I haven't had in a little while with AI where like, was just like, let's see what happens. know, it's, really, like if nothing else, just identifying the piece from the temple or the, which pyramid it was, um, I thought it was pretty cool. And it knew like where I'd taken the picture and everything too, which was interesting. Like, Oh, that's in the.

Shimin (36:07)
Mm-hmm.

That's.

Dan (36:25)
old Egyptian

museum like, yeah.

Shimin (36:27)
Yeah, that's kind of creepy. Maybe it has your location data. ⁓ All right, now.

Dan (36:32)
Could be, yeah.

Shimin (36:37)
Now we're going to move to deep dive.

All right, so this week's Deep Dive, we have a paper from researchers from ByteDance SEED, University of Manchester, Mila Quebec AI Institute, and Tsinghua University, MAP, titled, Dynamic Large Concept Models, Latent Reasoning in an Adaptive Semantic Space. So this is a proposal and an overview of a new large language

model architecture, where the key problem that they were trying to solve is the idea that language, even tokenized language, is not evenly information dense. So the example they gave of the cat set on the mat. In the traditional large language model, tokens like the

on A are given same amount of attention as any other token. But of course, that's not the case. So what they did was they trained another embedding to create a concept embedding, essentially. They take the tokens.

do a boundary detection and pooling. then DCAT becomes its own concept and then feed the newly created concept matrix to their cross-attention model, essentially. And they were able to generate better performance per compute, essentially. That's the short version of it.

Dan (38:10)
It's a pretty good summary. Better than I could do. I mean that's why we call it a D-type,

Shimin (38:10)
It gets deep. ⁓

So that's the overview. And it's interesting that there have been other architectures that tries to take advantage of the same kind of merging of tokens approach, something like a recurrent neural network

have this idea of like, let's not necessarily pay attention to every single token individually, which I thought was cool. Yeah.

Dan (38:38)
Mm-hmm.

And it makes, mean, as a layman looking at this, it feels like it makes more sense to me around like that's probably how, you know, if you were to read that sentence aloud, like the cat as the subject has a lot of weight, like mental weight to it, you know, so it's like, I don't know. It makes me wonder if people should be studying lexical structures a little bit too, be like actually coming up with things like attention.

What do I know? I'm a filthy cat.

Shimin (39:06)
speaking of lexical structures is like your boundary in the example are all words slash tokens right next to each other. Right. Decat is a single concept and they are together. What if you have words that are multiple spaces away from each other?

Right? Does that still capture the original, the single concept? And I think the answer is, is yes. Cause you are still encoding your input tokens, with their positional encoding. they've, they've already been kind of transformed into, space. so even though, even if the words are

not right next to each other, I think they can still be combined into a single concept. The other thing that they spoke about was there is another hyperparameter for the model, which is how much you want to essentially compress the tokens. So how many tokens should you combine into a single concept? And they ended up using R of four through their ⁓

empirical testing. on average, four tokens were compressed into a single concept, which reduced their total ⁓ flop cost by up to 34%. And they were able to relocate capacity from the compression of concept into the reasoning model itself. And that resulted in about 2%.

better performance on 12 zero-shot benchmarks. So it's...

a modest improvement, not groundbreaking, but I think it's a really interesting space of let's kind of address the fundamental shortcomings of the human language, right?

Dan (40:34)
Mm-hmm.

Well on the earlier topic I wonder how long until we have until there's a actually an LLM invented language to you have to speak not just for programming

Shimin (40:52)
All right. Yeah. And then they can design it to be, to be very, very terse and token efficient, then they will, but then we won't be able to read it. I think that's, that's kind of the give and take of it. Yeah. And they've also tested this on, ⁓ on the dataset has a hand be emphasis on Chinese and English text to give the model.

Dan (41:02)
Yeah, I know.

Shimin (41:13)
a multi-lingual bias, essentially, in their training data, and also on ⁓ math and coding to make sure that the algorithm works for both normal language and also highly technical reasoning work. Which I thought is also interesting because Chinese as a language is a lot denser than English to begin with.

almost every single character can be considered its own concept. And sometimes you have two characters in a single concept, but...

Dan (41:43)
Hmm,

that would make it, I assume, more efficient from a token perspective. I don't.

Shimin (41:50)
It would depend on the tokenizer. So I'm not exactly sure if, if Chinese, if each, if every single characters, it's

Dan (41:56)
character is what is a token or

if it's multiple or yeah. I've never really, you know, being very English, I've never really thought about it.

Shimin (42:00)
Yeah, yeah. So that was also interesting.

Yeah and some...

Dan (42:06)
Hieroglyphics was

really the first time I've thought about another language being applied.

Shimin (42:10)
Well, so hieroglyphics

is also very information dense, right? Every single glyph is super complicated, but can represent a lot of data.

Dan (42:13)
Mm-hmm.

Well, it changed over time too. That's the other sort of fascinating part there because it wasn't, you know, like most languages is not static. so when it, when they first came up with it, there was like a limited number of hieroglyphs. then as the Greeks came in, the number of them like exploded from like Greek influence on the language, which was kind of fascinating.

Shimin (42:35)
Hmm. Yeah.

Yeah, that's fascinating.

Dan (42:38)
And then there was even

like very much later instances of people writing the language that was used for the hieroglyphs in Greek.

Shimin (42:48)
Hmm.

Dan (42:48)
phonetically, which is kind like cool. It's pretty wild.

Shimin (42:51)
So what I'm hearing is one day we're all going to be reading and writing and learning a AI-generated language in class in K-12. That may not be the worst idea, honestly.

Dan (43:00)
Who's to say we aren't doing that already?

Shimin (43:02)
Yeah, if you're interested in some alternative architectural approaches for LLMs, I think this is an interesting paper to go through. there lots of technical details about the challenges they face while masking the concepts and how that was multiple tokens for the same concept is not GPU efficient. So they had to modify their masks.

to use existing kernel functions. That was highly technical.

Dan (43:29)
I'm glad you know what that means.

Shimin (43:31)
I skipped some of the math. not gonna lie. was like, oh, I gotta really sit down and read this thing.

Dan (43:38)
So this week's deep dive was a somewhat deep dive.

Shimin (43:42)
Yeah, somewhat deep dive.

Dan (43:44)
Yeah. Well, I know one thing we go really deep into and that is your favorite part of this podcast.

Shimin (43:51)
10.

Dans rants. You've had two and a half weeks of rants. like... Yeah. It's like a volcano.

Dan (43:58)
building up the intensity, just like

the green thing on this microphone. my God. ⁓ Yeah.

Shimin (44:03)
Yeah.

Or like the flood, like the flooding of the Nile, it's gonna blow the damn.

Dan (44:09)
Thanks

for that. yes, unsurprisingly, since everything else on this episode has been about my vacation, the rant is also a little bit about that. So one of the things that was kind of interesting is I went to Egypt, yes, but I also spent time in a tour group because that's not normally how I like to do my vacations, but like I just thought that

this location and everything else would be appropriate for it. So I was stuck with, I think, 82 other Americans from a large slice of Americana for the past two weeks. And of course, the topic of AI came up a lot in that conversation or in conversations, especially when they're like, what do you do is like the most popular question. you know, I was like software developer and they're like, what do you think about AI? Is it taking your job like?

Shimin (44:50)
Right.

Dan (45:01)
And the one thing that stood out to me, this is where I'm going to rant a little bit, that people, the general, this is sort me interfacing with the general public more than I typically do because I'm a developer. A lot of my friends are developers. A lot of my friends' friends are developer adjacent, so they're kind of influenced by how we're all thinking about things. People that just really didn't have that kind of background.

And like, holy have they bought the hype. I don't know how else to say it, but like. There are some of the stories that people were telling me about like, oh, yeah, I pasted this crap into chat, GBT and it like, oh, it was amazing. Like it did this, that and the other thing. And like at no point did anyone like really talk about negative experiences or like getting things wrong or anything like that. So I was just kind of like, hmm.

And I was thinking about it and I think part of it is the same reason why LLMs, when you talk about how well this stuff is moving the needle in terms of economic productivity, right? There's all those articles that we've talked about in the past about like, it's not really happening. that's because I think for the type of usage that quote unquote normal people that aren't software developers are doing, you can't quantify the output.

In the same way that I couldn't tell you whether Gemini correctly translated the hieroglyphics or not, right? Normal person can't tell you whether or not it's done a good job with like medical diagnostics or whatever. And so like, I think we're in a unique position as software developers where like we can very easily verify the outputs by

Shimin (46:23)
Mm-hmm.

Right.

Dan (46:41)
running it through a compiler, executing the code and being like, well, that's not right. Or having experience and looking at it and being like, oh, that's not right. it was just interesting to get that lack of any kind of skepticism just generally around it. And maybe that just points out that I'm a skeptic. I think there's more to it than that. One of the anecdotes that one of the people I talked to had mentioned was they had

They fed all their health information into like chat GPT and it goes, oh, you should get tested for vitamin D deficiency. And so then they mentioned it, their doctor and the doctor was like, that's a good idea. And it's like, well, yes, but also like something like 90 % of Americans have vitamin D deficiency because we spend all our time inside staring at screens and running clock code instead of like actually going outside, you know. So that's not surprising. Like I'm just.

Shimin (47:12)
Alright.

Right.

Dan (47:32)
I don't know. I was very underwhelmed by that and this person was like blown away by it. yeah, but TLDR, people are really buying the marketing hype and I feel like that's almost like dangerous to the point of being criminal. They're like, if you aren't aware of the shortcomings of these things, like just, it's very easy to fall into the trap of believing everything that it spits out.

Shimin (47:49)
Yep.

Dan (47:54)
I even find myself doing it sometimes and I'm, as I mentioned, a little bit skeptical. So I'm like, that worries me. Like I was really hoping to hear a range of opinions and instead I heard almost universally like, it's amazing. So, or people just didn't know. So those are really the two big ones I heard was like people that had used it. And then there's people that just had no clue and didn't care at all. And all of the people that had used it, was very much blown away.

Shimin (48:17)
You heard it here first, Dan thinks all AI companies should be thrown into jail for misleading the consumer. No, it's really expensive to determine what's true. I saw today that Gemini pulled their, or I should say Google pulled their AI summary related to health information because it was leading to some really crazy.

Dan (48:23)
Ha

Mm-hmm.

Mm-hmm.

Shimin (48:43)
Summaries like cockroaches can live in your body and it's normal to have cockroaches in your body. Like the average person ingest four or five cockroaches through their private parts every year, which is like just wild stuff. is it? Yeah, I guess the output is sufficiently close to what they expect a human to respond.

to any query and if you are in, if you're not in a situation where you can tell truth from fiction, it does seem like magic, that just works.

Dan (49:15)
Yeah. Except when you're consuming cockroaches, right? Which is the thing. It's like probably X percent of the time. It's great. It's it's that other, you know, 10 % or whatever that worries me. And the fact that like, it's sort of like any, you know, having, I'm sure you've probably been in a similar situation, right? Like you're the computer guy to some group of friends and or family, right? And

Shimin (49:19)
Yeah, yeah, exactly.

Dan (49:41)
to everyone that's in that group, the computer is this magical box that does things for you, but they don't actually understand how it works, really. And in that position, it's kind of weird because you kind of have to be like, well, it just does what you do to it. not like, you didn't break itself. You did something that caused it to.

wind up in this state. So I don't know.

Shimin (50:05)
Yeah, and that especially as it gets better and I argue it's pretty good already, right? Like if it's 90 % correct, it's even harder to be vigilant the entire time as it gets better. yeah.

Dan (50:10)
for sure.

Yeah. Yeah, exactly. It's like that

10%. And then if you really get caught in a doozy, then it's like, oof, you know.

Shimin (50:24)
And America is all in on AI, so maybe other countries are less so. But I don't think there's putting the Pandora back in the box. That is not how the saying goes. ⁓ It's Pandora's box. I don't think Pandora actually goes in the box. But what it's worth. Yeah.

Dan (50:32)
sure doesn't seem that way. Yeah.

Once it's

been opened, you can't close it again. think that's the thing. Yeah.

Shimin (50:44)
Yes, exactly.

But good rant think that's a, that's to bring some real world knowledge into this into this into this podcast.

Dan (50:47)
Thanks. had a while to, yeah, as you mentioned,

I had a while to come up with it.

Shimin (50:54)
Yeah. Okay. So onto your favorite segment then. Two minutes to midnight. We were still at a minute and 30 seconds last podcast. didn't, we didn't want to rock the boat too much as a guest host. And for, for those of you who are tuning in for the first time, this is the, our clock watch similar to the ⁓

Dan (51:08)
Gotcha.

Shimin (51:15)
nuclear clock during the Cold War where if the clock strikes midnight then the AI bubble is about to burst.

Well, that's not the right sound. Our first article from Bar Chart is an interview by Jensen Huang, the CEO of NVIDIA, saying we've done our country a great disservice by offshoring. And he also advocated for sharing the prosperity and...

growth, the productivity growth from AI throughout the entire society and not just have it be captured by the tech industry. Specifically, I have a quote here from him. The idea is simple. If there's no electricity to power America's manufacturing hubs, then there's no chance they can thrive. Simply building the manufacturing first and the electricity later will skyrocket costs, further making build-outs unsustainable.

he further extended that same argument to social and economic outcomes, adding that if we wanted to fix our social issues, domestic issues, we have to create prosperity, not just for people with PhDs and college degrees. have to create prosperity for every segment of the economy. The largest segment of the economy is manufacturing. And we've all short that for too long for 20 years, we got to bring that back. We have the ability to do so.

And this is the AI industrial revolution. On the surface, this isn't really related to the AI bubble, but I think what the underlying current here may be that Jensen is looking for more government help when it comes to building out the electricity.

capacity and some of that. ⁓

manufacturing base to sustain the AI efforts.

Dan (52:56)
Yeah. And you know, data centers and everything else too, right? And that's, that's an interesting point is like, if you think about it, like PhDs aren't physically wiring up the cables in a data center, right? It's, know, hopefully a union electrician or someone, maybe not. Um, and like that is an interesting thing that we haven't thought about or initially talked about a lot on this podcast is like, what is the broader impact to the

rest of the economy around like this huge investment that's being made. And we've talked to some degree about like, especially in this segment about how, you know, the American economy is being propped up by the high bubble right now, for better or for worse, but like.

A lot of that kind of comes through the lens of like the impact on software and like white collar jobs, but less so about like, what about blue collar jobs that are, you know, driving some of the like infrastructure builds that are happening behind this? ⁓ And I guess you could, you could look at this from through the lens of like, he's just trying to rationalize that spend this happening to some degree, but,

Shimin (53:51)
Mm-hmm.

Dan (54:01)
It is an interesting perspective on, you know, kind of broadening that to the masses. I will note that he didn't, you know, have a very precise plan for how that wealth would trickle down. And it feels a little bit like 80s trickle down economics,

Shimin (54:15)
Yeah, talking about the past is not a blueprint for fixing the issues of the present, I guess.

Dan (54:16)
⁓

Shimin (54:23)
And I'll do the next one.

Dan (54:23)
So

yeah, so.

Well, I actually, yeah, this one also feels kind of tenuous, honestly, really. think the bubble, but there was an interesting interview piece with our friend Jan Lacoon who said intelligence is really about learning. That was the pull quote that Arstakhnicka chose to run with as the title. And really, I thought it was a pretty fascinating interview in general.

Shimin (54:31)
Okay.

Dan (54:49)
with him about like, you know, little, they cover a little bit of his background, which I knew some of it, but not all of it. And went into a little bit about like why he left Metta and what's next. And the piece that I thought was particularly interesting that we've talked about in the past here is like, he believes very strongly in world models being the next big thing. And it

Shimin (55:08)
Mm-hmm.

Dan (55:09)
became very apparent through the context of the interview that Meta does not believe that in terms of their AI strategy. So it makes sense that they parted ways. But they also talked a little bit about Meta's continued investment in that area and how they're basically just doubling down on LLMs. So yeah, like they put 15 billion into scale AI.

Shimin (55:15)
Yep.

Dan (55:32)
and then hired... ⁓

the CEO to run things from now on.

Shimin (55:37)
Yeah, I thought this article has a few things that are related to the bubble. One being that Yonkun admitted that the reason why Llama 4 ⁓ did not have the impact that they hoped it would is because they fudged the results via benchmarking.

Dan (55:56)
Yeah.

Shimin (55:57)
I think the exact quotes for results were fudged a little bit and that the team used different models for different benchmarks to get better results. I feel like this is evidence that the underlying technology is really slowing down if they had to benchmark this hard. And the other area was he really did some trash talking of the other high profile ⁓

AI researchers, new startups, right? He cites and I quote, he cites OpenAI former chief technology officer, Miramarati's thinking machines, parentheses, I hope the investors know what they do. And OpenAI's co-founder and chief scientist, Ilastos Kivers, safe superintelligence, quote,

There I know the investors have no idea what they do as good examples of.

of how these new labs are maybe getting a lot of money, just based off of trust. Yeah.

Dan (56:49)
Yeah,

that is true. Yeah, I guess I had read that.

very much in the vein of like he was booking for one of the investors and not necessarily the researchers themselves, I guess. Like, I guess you read it a little bit more like he was throwing shade at both, yeah.

Shimin (57:01)
⁓

Well, he's throwing

shade at the investors where they're investing in things purely based on based on what what? Yeah, exactly. ⁓ There's no path to profitability if the investors have no idea what what they're doing.

Dan (57:09)
Reputation versus, yeah. Yeah, that's right. ⁓

Yeah. Yeah.

And the other piece that he dropped in there was the world models. Or actually it wasn't even him. It was the interviewer dropped the world models have already been of some interest to proper engineering companies, like physical engineering companies, not technical stuff. designing aircraft engines, I think was the example they gave where you need to have a

Shimin (57:35)
Mm-hmm.

Dan (57:42)
firm understanding of physics to be able to do that. so like world models being trained on video get the physics understanding and are therefore more useful for that kind of application. So I that was interesting because like Meta saw that and was like, cool, we don't care about Boeing or whatever, like Rolls Royce making aircraft engines.

Shimin (57:54)
Right.

Dan (58:03)
It's kind of interesting to see that split.

Shimin (58:03)
Yeah, so they went all in

language models instead. Yeah. Also, there's some great description of food in this article. I was kind of hungry after I read it.

Dan (58:12)
They're eating all this great French cuisine. Yeah, it's pretty good. Standard French behavior in my opinion. But yeah, so to bring it back a little bit because it kind of felt like sort of a slow news week in terms of bubble news, maybe a slow news week in general, because I feel like everyone's kind of coming off the holidays, myself included. But I

Shimin (58:15)
I know, he's living it up. Go for it.

Mm-hmm.

Dan (58:36)
went a little broader and just pulled an article that was from CNBC, is, we in an AI bubble? Tech leaders, analysts is what it's called. think it's at least I'm reading the slug. Yeah. So what 40 tech leaders and analysts are saying in one chart and of course, it's a podcast. So it's going to be great to visually, you know, audibly describe a visual chart to you, but

Imagine a pretty standard like two axis chart where we have the level of concern from zero to 10 as the vertical axis and the horizontal axis is, is there an AI bubble from zero to 10? And then they've flooded all of these people with varying levels of fame and or some of them, I don't even know who they are on here with what their opinions are. And the first thing that

I thought was pretty interesting is like, if you were going to do a linear regression on this, it'd be pretty easy to run one because like we have almost a straight line from zero, zero, zero to 10, 10, you know, going, going along here. And there's only a couple of outliers. And the most notable one is, uh, Bill Gates who falls under, um, he's not very concerned, but he's pretty damn sure we're in a bubble. Um,

Shimin (59:38)
Mm-hmm.

Dan (59:52)
which I found fascinating. And then we had two government dots on there. So one is Jerome Powell, who doesn't think we're in much of a bubble coming in at two on the, there a bubble? And three for his level of concern. So he's definitely in the sort of lower left quadrant. And then we had Jared Bernstein coming in on the opposite side. Very concerned and very convinced.

Those are our two government data points. yeah, I don't know. It's just nothing earth shattering here. Again, I think that's kind of like the theme of this week. It's not super earth shattering. But like, interesting to see where some of the leaders' heads are at around this stuff.

Shimin (1:00:30)
Yeah, there are some interesting ones like Cathy Wood of course of ARK fame. She thinks there's no bubble, zero out of ten, but she is a three out of ten concerned. I don't know how you can tie those two together. ⁓ So Cathy is always an odd one. ⁓

Dan (1:00:45)
Yeah.

The charts are interesting to part.

Half the fun is like, want to know how they came up with these values to place the chart based on like probably public statements, right? That have been made.

Shimin (1:00:58)
Yeah,

it's very strange. Overall, again, no financial expert here. Some of my faves, Jamie Dimon, Ray Dalio, in the, there's some of a bubble camp. I think I'm in good company there. Where would you put yourself, Dan, on this chart?

Dan (1:01:17)
You know, it changes every week. think that's partially the fun of doing this segment. I would say right now my level of concern is pretty low. Like I'm probably at a three or four, which for me is low, I should say. And the is there at a are we in a bubble? I'm fairly convinced of that. So I'm probably around like a seven or an eight.

there. Should it be a 10? Does 10 mean we're definitely in one? That's the other problem about this chart is like, is there one that seems pretty binary to me, right? But I guess not.

Shimin (1:01:45)
Mm-hmm.

That's true.

I guess it's the magnitude of the bubble. ⁓ 708 feels pretty, pretty conservative. You're in good company with a...

Dan (1:01:57)
if it's the magnitude, then I

would go probably more like a five right now. If it's purely magnitude. No, you said it's the magnitude.

Shimin (1:02:04)
if there is a bubble.

on the, on the concern.

Yeah. The concern is five, but the bubbleness, how, how, how large is the bubble going to be?

Dan (1:02:15)
Well, that's the part where I'm like a little bit less concerned than I have been in previous weeks, because like I also read an article which didn't make the cut for this about like the level of debt financing involved in some of this stuff. And we haven't hit dot com levels of debt financing yet. So that feels a little bit better, but circular deals are still concerning. So I don't know. Where are you at?

Shimin (1:02:36)
That's

good to know. I'm not on the same ballpark. think I'm a little more concerned than you are. think I'm like a six, just for concern level. But yeah, I'm at like an eight. I'm... ⁓ Yeah, if we were Kathy Woods of the world, we would not have this segment. ⁓ But taking all together, how do we feel about our clock?

Dan (1:02:45)
Yeah, I mean, I guess we wouldn't be doing this segment if we both didn't believe there was a bottle. That's fair. Yeah, yeah, it's true. Oh, zero.

I mean, like, I don't know how much of this is just like I said, holiday news cycle, but things feel pretty calm to me right now.

Shimin (1:03:07)
Me too. I think it's a new cycle, lulling us into a sense of security. But I feel pretty good. The vacation has done a ton for ⁓ our anxiety level.

Dan (1:03:11)
Right.

Yeah.

I know, I'm so happy all the time.

My rant was pretty chill, you know. Yeah, that's true. Yeah, well, I guess does that mean we want to move it or leave it? I mean, we're pretty far away right now.

Shimin (1:03:20)
Yeah.

E E

I I propose we do exactly two minutes to midnight. I'm gonna throw it out there. I feel pretty good this week. Yes.

Dan (1:03:36)
that matching the title, okay? Okay.

Well, let's do it then. Two minutes to midnight. Is it you heard it here first? Two minutes to midnight is now at two minutes to midnight.

Shimin (1:03:40)
All right, let's do it. Let's see what happens. That two minutes in there. That's right.

Dan (1:03:47)
That's fair.

Shimin (1:03:47)
All right.

Well, yeah, that's the show folks. Thank you for joining us for the study session this week. If you like the show, if you learned something new, please share the show with a friend. You can also leave us a review on Apple podcasts or Spotify. It helps people to discover the show and we will really appreciate it. If you have a segment idea, question for us or a topic you want us to cover, shoot us an email at humans at adipod.ai. We would love to hear from you.

You can find the full show notes, transcripts and everything we mentioned today at www.adipod.ai. Thank you again for listening and we will catch you in next week's episode. Dan, do you have any parting words?

Dan (1:04:25)
Also,

I do, if you would rather have Rahul as the co-host instead of me, feel free to email us at humans at adipod.ai. Or both of us, we could do a head-to-head co-host off. We'll see how that goes.

Shimin (1:04:34)
you

yes, I love it. No, Rahul would. Yeah, there's an open invite for him.

Okay. Bye.

Dan (1:04:43)
Bye.

</details>
