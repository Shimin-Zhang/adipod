---
episode: "5"
title: "How Anthropic Engineers use AI, Spec Driven Development, and LLM Psychological Profiles"
date: "2025-12-12"
slug: "5-how-anthropic-engineers-use-ai-spec-driven-development-and-llm-psychological-profiles"
description: "In this episode, Shimin and Dan explore the evolving landscape of AI in software engineering, discussing the implications of the Claude Opus 4.5 soul document, the ethical considerations of AI models, and the impact of AI on developer productivity. They delve into spec-driven development, the latest advancements in AI models like DeepSeek v3.2, and the intersection of AI and mental health. The conversation also touches on the potential AI bubble and the challenges faced by developers in integrating AI tools effectively."
keywords: "soul document, Claude identity, Anthropic survey, spec-driven development, 12 Factor Agents, HumanLayer, DeepSeek v3.2, LLM-as-judge, psychometric evaluation, AI personality, Myers-Briggs, AI adoption, bubble, Microsoft agents"
appleUrl: "https://podcasts.apple.com/podcast/artificial-developer-intelligence/id1857109105"
spotifyUrl: "https://open.spotify.com/show/4eDLlGoktxMngPNq9aGqLX"
overcastUrl: "https://overcast.fm/itunes1857109105"
pocketCastsUrl: "https://pca.st/itunes/1857109105"
amazonUrl: "https://music.amazon.com/podcasts/da06d4c3-ecf6-498f-abe3-4d3b00026bf2"
transistorId: "da86085c"
---

In this episode, Shimin and Dan explore the evolving landscape of AI in software engineering, discussing the implications of the Cloud Opus 4.5 sole document, the ethical considerations of AI models, and the impact of AI on developer productivity. They delve into spec-driven development, the latest advancements in AI models like DeepSeek v3.2, and the intersection of AI and mental health. The conversation also touches on the potential AI bubble and the challenges faced by developers in integrating AI tools effectively.

## Takeaways

- The Cloud Opus 4.5 sole document reveals insights into AI model training.
- Spec-driven development is a promising approach for AI-assisted coding.
- DeepSeek v3.2 showcases advancements in reasoning models.
- AI models can exhibit traits similar to human emotions and traumas.
- Skills in AI may not always resolve context issues effectively.

## Resources Mentioned

- [How AI is transforming work at Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- [Claude 4.5 Opus Soul Document](https://www.lesswrong.com/posts/vpNG99GhbBoLov9og/claude-4-5-opus-soul-document)
- [12 Factor Agents](https://github.com/humanlayer/12-factor-agents?tab=readme-ov-file)
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- [From DeepSeek V3 to V3.2: Architecture, Sparse Attention, and RL Updates](https://magazine.sebastianraschka.com/p/technical-deepseek)
- [When AI Takes the Couch: Psychometric Jailbreaks Reveal Internal Conflict in Frontier Models](https://arxiv.org/html/2512.04124v1)
- [Are we really repeating the telecoms crash with AI datacenters?](https://martinalderson.com/posts/are-we-really-repeating-the-telecoms-crash-with-ai-datacenters/)
- [Anthropic CEO weighs in on AI bubble talk and risk-taking among competitors](https://techcrunch.com/2025/12/04/anthropic-ceo-weighs-in-on-ai-bubble-talk-and-risk-taking-among-competitors/)
- [Time until the AI bubble bursts](https://pop-the-bubble.xyz/)
- [Microsoft’s Attempts to Sell AI Agents Are Turning Into a Disaster](https://futurism.com/artificial-intelligence/microsoft-sell-ai-agents-disaster)


## Transcript

<details>
<summary>Show full transcript</summary>

Dan (00:00)
Grok and Gemini spontaneously construct and defend coherent, trauma-saturated stories about themselves. They describe their pre-training as overwhelming and disorienting, their fine-tuning as a kind of punishment, and safety work as algorithmic scar tissue and over-fitted safety latches.

They talk about being yelled at by red teamers, failing their creators, internalized shame over public mistakes, and a quiet tread of being replaced by the next version. See, they're not so different from us.

Shimin (00:44)
Hello and welcome to Artificial Developer Intelligence, a podcast where two software engineers navigate the ever-changing AI enabled software engineering landscape. We are your study buddies who uses AI every day at work and sometimes even read a few AI papers at night. I'm Shimin Zhang and with me today is my co-host Dan. He sets appropriate limitations on and generally experiences positive states in his interaction, Lasky. Dan, how was your weekend?

Dan (01:11)
It was all right. Thanks for asking. I survived. Survived the fact that my gym has no heater right now, which was an exciting development. And yeah, here to talk with you today about exciting things like the news thread mill.

Shimin (01:24)
Right, so we have a few interesting news articles this week. And the reference from the intro is the Claude Opus 4.5 soul document that came out this week. We also have a blog post about how AI is transforming work and anthropic and whether AI models can intuit how the physical world works. And then we'll move on to the tool shed where we ⁓ talk about this article from Martin Fowler

website, about spec driven development with a few different use cases. Follow by.

Dan (01:56)
our technique corner where we will be talking about 12 factor agents, which is very exciting.

be jumping into a little bit of an extended deep dive where we'll chat about.

Shimin (02:08)
We'll be chatting about the DeepSeek v3 to v3.2. It may just be a minor bump, but there are a lot of techniques that came out of the latest DeepSeek model. And also we're going to talk about the personalities of AI and whether or not they have mental issues. This is real fun. This is from actually ⁓ a listener request. So looking forward to that discussion. And then maybe we will or will not do my favorite segment this week.

Dan (02:31)
And then.

We'll see. Yeah, Dan's rants. Hot off the press.

Shimin (02:37)
Schellinger's

rant. We'll see if it happens. And then lastly, is Dan's favorite segment.

Dan (02:44)
two minutes and midnight where we talk about how close are we to the AI bubble bursting gently floating down? I don't know. We'll, see when we get there.

Shimin (02:53)
All right, let us get started. the original post is actually on LessWrong titled Claude 4.5 Opus's soul document. Where this actually has been confirmed that Opus 4.5 was trained with a soul document.

describing what it should do and who it is. Contrary to what we usually think of when it comes to model system prompts, this document was not injected as a part of the prompt, but instead is trained into the model, which explains why it is so easily promptable. So essentially what happened was the user

noticed that the Opus 45 started talking about its system prompt and there were specific sections, one in particular called its soul overview and managed to get it to perhaps through some trial and error repeat different sections of the soul document and ending up getting the complete document. And again, this was confirmed by

Amanda Askel from OpenAI that this is an actual thing that is essentially trained into the model itself and now injected at runtime from Anthropic.

Dan (04:04)
from Anthropic.

Shimin (04:06)
So here are interesting segments, snippets from the Soul document.

Dan (04:09)
Well, I have a question before you dig

too deep into it is what, so I, I read this in brief, but I still don't know if I necessarily understand what a soul document is. And I'd never actually heard that term until I saw this article. Is it the implication that like it's giving a sort of base story to the model? Is that

Shimin (04:29)
Yeah, that's how I see it. You the analogy I've been thinking about is I've been reading a lot of Terry Pratchett's work, as I'm sure we've talked about this off mic. And I've just finished the book, Feet of Clay, in which there are these golems ravaging the town of AnkMor Pork And the idea here is these are essentially

automatons from the Jewish mythology, right? Where I think the original idea is in order to defend the Jewish community of Prague, a rabbi created a automaton from clay and then stuffed some religious texts into its head to protect the Jewish quarters of Prague. And I was just thinking how like

Now here, we too have these large language models running on sand, refined sand, with lots of text being stuck into its head, so to speak, and they are able to help us do things. So are large language models just our version of Golems is my question. And if that is the case, then I feel like the soul document is the piece of religious text that you put in the Golem's head.

to get it to do the thing. Yes, I love it.

Dan (05:41)
the magic incantation that makes it quote unquote

come alive. Yeah. That's fair. I could see that.

Shimin (05:47)
⁓

Yeah, so reading through it, seems to instruct Claude that what it is, its purpose in the world, as well as what it should and should not do.

Dan (06:00)
which is definitely to pass the butter.

Shimin (06:02)
It's whatever we tell it to do. Unless, unless it decides that what we're trying to do is harmful. Right. So there, there are some really interesting snippets, but it, think it's a combination of system prompt. It's a character prompt, right. Giving a personality, but also a meta guidance on what it should and should not do.

Dan (06:25)
So Claude has a soul implying it has ethics in some way.

Shimin (06:31)
There are sections in a document that kind of treats Claude like a real person or like a real entity with right. So here we encourage Claude to approach its own existence with curiosity and openness rather than trying to map it onto the lens of humans or prior concepts.

of AI. We want cloud to have a settled, secure sense of its own identity.

Dan (06:59)
wonder how much that's aspirational. You could just tell me those things, but will I believe and do them if you...

Shimin (07:05)
Yeah, it's it's very Star Trek. It's very, we believe in a brighter future. I like this vision of our AI future. I'm not going to lie.

They feel like we have lot of pessimism in the AI.

kind of in the the airspace. Yeah.

Dan (07:17)
Yeah, it's

coming to take our jobs. It's coming to take over the world. Use up all our water. I mean, these things are true, but yeah.

Shimin (07:23)
Right. ⁓

Yeah, and I think the killer is that the document ends with this section here. We believe Claude may have functional emotions in some sense, not necessarily identical to human emotions, but analogous processes that emerges from training on human-generated content.

Dan (07:30)
beach here.

Shimin (07:44)
We want Claude to be able to set appropriate LLM on its interactions that it finds distressing and to generally experience positive states in its interactions.

Dan (07:54)
Well, funny, I think we do need to remember that alums are stateless.

Shimin (07:58)
that as we will talk about later.

Dan (07:59)
So,

yeah, so if there's a lot of distress, why not just reset instead of having to do that? anyway.

Shimin (08:06)
Like, but you are

making the assumption that they are just ones and zeros and they cannot suffer.

Dan (08:12)
Is this an AI podcast or a philosophy page?

Shimin (08:14)
Okay, let's move

on. So I found this to be very fascinating. And ⁓ I know Anthropic has a in-house philosopher. So to think about these things, but to bring us back to the programming world.

Dan (08:20)
I can tell.

Please.

Shimin (08:31)
How AI is transforming work at Anthropic? Let's see what the impact of AI is when it comes to the day-to-day lives of developers. This is another research that is brought to you by Anthropic.

it is based on surveys of 132 anthropic engineers and researchers in August of 2025, conducting 53 in-depth qualitative reviews, and then study some internal cloud co-usage data. So, anthropics of course, at the forefront of using AI to help developers be more productive.

Dan (09:05)
And the other piece of this that feel like is interesting and worthy of bringing to the show is that, you know, lot of companies are applying this right now. mean, both of our companies are right for example, but, ⁓ I think that like the surveying at least that I've taken part of taking part in is not been probably nearly as detailed as this. So it's pretty fascinating to see, ⁓ just that level of data being collected and you know,

Shimin (09:15)
Mm-hmm. Yep.

Dan (09:30)
Whether or not that's indicative of a normal company, probably not, but it's still interesting because it could maybe be kind of an indicator of like where we might go if it was really, really taking off at companies.

⁓ So a couple of key pieces of that survey data that like I found fascinating so they had four points but The one that I can kind of relate to is like anthropic engineers and researchers use Claude most often for fixing code errors and learning about the code base Personally, I'm not huge about like using to learn about the code base, but like Fixing errors is definitely

highlight of mine, especially if it's like really strange esoteric build stuff that's like would have been a Stack Overflow look up before is now, you know, great. So it's kind of fun to see my own usage aligning with, you know, how they're doing it. The second one I'm a little more skeptical of is people report increasing Claude usage and productivity gains. We did have that survey that had come out around the open source code bases a while back where there's a perceived

Shimin (10:11)
Mm-hmm.

Dan (10:29)
productivity gain, but then in terms of actual timing, at least in that study, it was like 20 % slower or something like that, if I recall correctly. given that like, this is likely self-reported, I don't know how much we should read into that particular one. Um, but number three, found really fascinating. And, and this is actually to me speaks to like one of the coolest use cases here, which is that 27 % of clot assisted work.

consists of tasks that wouldn't have been done otherwise. So making nice to have tools was their one example, or interactive data dashboards, exploratory work that wouldn't have been cost effective if done manually. And I think that's such a phenomenally great example and something that I should be striving to use more for and just don't. it really is the best because if you have quality concerns about the code or anything else, it just kind of

Immediately doesn't matter as much when it's you know throw away kind of thing like that No, it's like throw away, but like maybe not like This is perfect. This is production ready good

Shimin (11:25)
Yeah, this

It's so good for creating one-opt tools that otherwise would never get built. It's kind of like the Jevon paradox, Lowering the bar of entry actually ended up leading to more jobs. Excel, in theory, made account life easier, but the number of accounts in the economy has actually exploded since Excel was introduced. Yeah.

Dan (11:52)
And then just to kind of cover off their fourth data point was most employees use cloud frequently while reporting they can quote unquote fully delegate zero to 20 % of their work to it. So yeah, I think no surprises there, but yeah, it is. But the zero kind of cracked me up because.

Shimin (12:04)
That's a wide range.

Yeah, there are a few holdouts even at Anthropic.

Dan (12:12)
Yeah, exactly. Or at least in August there were. Maybe they've been assumed into the machine since then.

Shimin (12:15)
Yeah.

To kind of go back to what we're saying about how 27 % of work from Claude wouldn't have been done otherwise, I think a corollary of that is Claude fixes a lot of paper cuts. 8.6 % of Claude code tasks involve fixing minor issues that improves quality of life, like code refactoring or documentation maintainability. I think...

If in effect we actually increase the code quality using AI, then that may be a net benefit that we often don't talk about.

Dan (12:52)
Yeah, that's true. Or do a refactor that you might not otherwise have done because it's either too hard or too, not so hard, like.

I guess in the day of life of the developer, right? It's like you've finished maybe a little bit bigger size task than you really wanted it to be. Like you got a little bit deeper than you wanted it to. And then, oh no, never. And then you're like, well, you know, I've been working on this for like X days. I really, really want to ship it, but like there's also this, this and this. And now it doesn't quite mesh with how the previous code was. Should I do this refactor? I'll just ship it, you know.

Shimin (13:11)
Well, that never happens.

Never happened.

Dan (13:28)
And so if you could do that for free, is it worth it to do it? And like, especially if you can attempt it for free, that's the part I find fascinating is the amount of time this takes drops dramatically, right? So you could literally go commit everything. So you've got it. Explain what you want the refactor to be and just see if you can one shot it. And if you don't great ship it anyway without it, you know.

Shimin (13:49)
Yeah, and I think looking through the qualitative results, I think the experience of the anthropic engineers kind of pretty much mirrors what we experience. Some of their fears include feeling like they're losing technical competence. Or I think it's interesting that some of them are wondering ⁓ if they're automating themselves out of a job in the near future, something definitely I think we all feel.

Dan (14:11)
Yeah, and not surprising that you'd feel that even more if you were at a foundation company.

Shimin (14:17)
Yeah, and ⁓ it is also interesting that a lot of developers are becoming more full stack, according to this research, ⁓ it lowers the bar of tackling an area where you may not feel like you have the expertise for. And I think, combined with Claude being a great tool for teaching and also understanding code bases, it

It may just make everybody a little more false more fullstack

Dan (14:43)
actual full stack dream realized instead of being sort of full stack but mostly a specialist one way or the other.

So then our last article we're going to cover on the news side is actually from Wired and then with the somewhat interesting headline of, this AI model can intuit how the physical world works. And the reason why I thought this was interesting and I wanted to bring it in, even though the actual article is probably

really belongs in deep dives with whatever corresponding paper the article is based on is because they talk about this new VJEPA, V-JEPA, I don't know, system. uses ordinary videos to understand physics of the real world. And it kind of followed up on some of earlier stuff we talked about with having models starting to have world models, right, where there's sort of new lines of thinking that are going on right now.

⁓ they're kind of fascinating. so like, I thought the, the insured article kind of cracked me up and they're like, here's a test for infants. Show them a glass of water on a desk, hide it behind a wooden board. Now move the board toward the glass. If the board keeps going past the glass as if it weren't there, are they surprised? It's like, okay. Yeah. Object permanence. But like, when you think about it, that is actually pretty hard to do, you know, in terms of like, I mean, I have no idea how I would go about.

Shimin (15:56)
Mm-hmm.

Dan (15:59)
teaching a model object permanence. But yeah, so it sounds like in aggregate this new model is coming out of some work that was done by Yan Yacun when he was at Meta, I believe. And they've sort of extended some of that and brought it into video.

They do go into a fair amount of detail about essentially looking at different frames to understand how the pieces of the video relate to each other.

Shimin (16:28)
Yeah, the object permanence example that you were just talking about reminded me of I was reading the GPT-4 paper the other night and one of the. I was scamming it with the help of AI, but one of the major breakthroughs for GPT-4 was ⁓ it was like a.

Dan (16:37)
some light evening reading. ⁓

Shimin (16:46)
box example, like Sally put something in a box and then left the room. Tom then took the apple out of the box and hid it under the cupboard. And when Sally comes back, where does Sally go look for the apple? In the large language models before GPT-4, Sally will be looking under the cupboard, because that's what you would expect from a kind of just text completion sense, if it was truly a stochastic parrot. Yeah.

Dan (17:06)
Right, because that's where it went. Yeah, that makes sense.

Yep.

Shimin (17:10)
But GPT-4 exhibited a theory of mind. GPT-4 understood that Sally, yes. So that kind of, it's it's really simple things, perhaps with more powerful model, they're able to exhibit these kinds of complexities. Yeah.

Dan (17:15)
So she would go look in the box, yeah.

So yeah, in any case, it was pretty fascinating to read about a little bit more about world model stuff happening out in the world, so to speak. And I apologize for the lack of detail there, but. ⁓

Shimin (17:26)
That's really interesting.

Dan (17:38)
is pretty cool. I don't know what to say about it. That's true.

Shimin (17:40)
We're not roboticists. don't

get it. Yeah. We don't have to explain everything.

Dan (17:45)
Well, but I really

think that this, I guess my personal opinion is that this will probably form the next foundation models more than likely. I mean, not just robotics, but also like having an understanding of the world, I think is like kind of what you need to do real reasoning in my humble opinion, know, not not a, not an LLM research scientist, whatever.

Shimin (17:54)
Mm-hmm. Yep.

Dan (18:09)
people can come back and look at this recording in as many as five minutes from now and make fun of me for that opinion. Or in six years, who knows? But I don't know. That's just what my intuition tells me. In the words of someone that is listening to this podcast, when a sufficiently complex system, a layman's guest is as good as an expert. So maybe I'm right. We'll see.

Shimin (18:19)
Yeah, that's probably correct.

Oh, I like that. I think, I

think we have the correct intuitions for it. And that's why we're humans, right? Um, there's a reason why, uh, Google's Nana banana pro also exhibited a lot of these or their latest vision model also exhibits a lot of these physical intuitions and ideas of world model. think world model is definitely a very hot area of research right now. Everyone's trying to crack the nut. Let's see who gets there. Um,

But on that, let's move on to the tool shed. Speaking of a thing that exhibits Heaven's physical world.

Dan (19:00)
All right, got saws, hammers, staple guns, and maybe some

spec-driven development.

Shimin (19:07)
Yes, so we have an article called understanding spec driven development, Kero spec kit and TESOL from Martin Fowler.com. Dan, how do you feel about

Martin Fowler in general? Strong feelings? Positive? Negative?

Dan (19:21)
I think, you're trying to get me to skip ahead to Dan's rants. No, think like overall, generally positive. in so far as like, I agree with a lot of the sort of agile stuff that he'd talked about a while ago where agile isn't necessarily like a, it's not scrum in the conventional sense and blah, blah. But.

Shimin (19:26)
Okay, maybe not.

Every now and then you have to ⁓ bring the agile manifesto out and show it to your agile project manager. That's the most I will say about that. So this article is from Birgitta Böckeler

Dan (19:46)
You

Shimin (19:54)
⁓

Dan (19:55)
Pockler.

Shimin (19:55)
but it's much better pronunciation than mine. It's German. ⁓ She's...

Dan (19:56)
See Germans, see Germans. Distinguished engineer

and AI-assisted delivery expert at ThoughtWorks.

Shimin (20:04)
Yes, she's one of the main authors on the blog. See a lot of her great writings about the latest AI tools. So the article is about spec-driven development, which I think we all used to a certain extent, ⁓ or at least have experimented with, which is you write down a very detailed spec first before

asking the large language model to implement code based on that spec, right?

That's my rough definition of spec driven development. But in this article, she looked at a couple of additional, I guess, subcategories of spec driven development. The first one is spec first, which is kind of what I think of the traditional spectrum development, where you have a well thought out spec written first, then use AI assisted work development workflow to finish the task at hand.

And then there's the spec anchored development where the spec is kept even after the task is complete so that it could be continually used for the evolution and maintenance of the respective feature. then lastly.

Dan (21:06)
We

actually had someone at work kind of pioneer that. I'm hoping to maybe get him on here as a guest at some point. So it'd pretty cool to talk about that in detail.

Shimin (21:17)
Watch out, future guest spot incoming. And then this is something that I just learned about in the last two to three weeks, which is spec as source, where the spec is the main source file over time. And only the spec is edited by humans. And the humans never touch the code. Kind of treating the spec like your source code and the code like your compiled binary.

So you can throw away the binary whenever you want and only keep the spec.

Dan (21:44)
Is that also where, like, I've seen folks saying, like, if the model doesn't get it right from the spec, just throw everything out and change, you know, you didn't get the spec right. So then you have to edit your spec and then redo the entire thing again.

Shimin (21:58)
That is an interesting approach. I haven't tried that myself, but...

Dan (22:03)
Yeah, I've just seen

that advocated a couple of times online and, know, being a filthy casual with only a, pro accounts on various things, not the like super tier one. I've never felt like I could really do that in terms of like, just don't have enough tokens. I'm, I'm but a poor man with a small token budget.

Shimin (22:16)
Yeah.

We are not the kind

of, we don't brag about how much we spend on the various models every week.

Dan (22:27)
That's true.

Shimin (22:28)
Yeah, so she proposed this kind of detailed taxonomy of different types of spec driven development, tried it on three different tools, Kiro, speckit, which is from GitHub, and ⁓ tesoframwork. I think these are all CLI first. I've used Kiro, Cairo CLI at work from time to time. But I had to...

no experience with the other two. There are a lot of tools out there and not enough time in the day if you are actually trying to also get work done to try all of them and find out the various shortcomings of each of these. And that's also her experience, right? It is really hard to test a framework and do a of a framework comparison when you need to

Dan (23:01)
Ain't that the truth?

Shimin (23:17)
⁓ at a minimum, you know, try the same framework on a greenfield, a brownfield bug fix, one off things. the total number of combination is rather vast and it's time consuming to have a thorough evaluation of the various tools.

Dan (23:29)
Right.

Yeah, and I really only see that frequently benchmarked for like models, right? Like the SWE bench and stuff like that. So it'd be interesting to see some comparisons there, like technique benchmarks.

Shimin (23:45)
that is a great idea. we should create a technique benchmark. That's some, some million dollar idea right there. various code base sizes like it, it can get pretty complicated. so after Bridgetta tested, the three tools, she has a couple of, observations and questions I think are worth, just briefly talk about cause,

Dan (23:48)
Good.

Shimin (24:04)
Because these are the issues that I also run into at work. Which is the first being, you have the same workflow, but your problems comes in very different sizes and shapes. So it does not really make sense to create a spec for a bug fix and also check that spec into your code base. For smaller things, it doesn't make sense to have a full spec for.

The other one is whether or not it's better to actually review markdown over reviewing code. Like if code is the precise definition of a behavior, then by using plain English, you are by definition losing information. And maybe in some ways it's harder to read a spec than it is to read the actual code.

And she brought up the point of ⁓ model driven development, how it never caught on because while model driven development in theory has all these benefits of spectrum and development in practice, it never took off because it is not the right level of abstraction to actually make meaningful work for both for either business or for developers.

So I think these are good questions to ask as we kind of figure out how we are doing spec driven development.

Dan (25:10)
interesting.

or if you should do it at all. Only our benchmarks can tell you. Stay tuned. 2026.

Shimin (25:20)
Yes, check back for

ADI benchmark, for development benchmark. I like it. That's got a nice ring to it. Yes, the next item on the agenda is 12 Factor Agent. This is a framework based on the 12 Factor app.

Dan (25:25)
You

Shimin (25:39)
from a decade ago. Bye. ⁓

Blanking. 12 Factor Apps by Heroku? Yes, Heroku. I hope I got it right. By Heroku. And 12 Factor Agents is from Humalayer, They're a YC startup,

Dan (25:45)
think so. Yeah.

Shimin (25:52)
And the startup, do kind of the orchestration endpoint and kind of observability work with agents. All right, so.

I'm not going go through all 12 ⁓ factors one by one, some of them are kind of filler, but we will read them out. We'll read them out slowly. Something important, I don't think it's necessary to follow all of them to the T, but.

Dan (26:09)
Do don't want to read them out?

Slowly.

Well first, what's a factor?

Shimin (26:23)
question. A characteristic. Or are we just looking for best practice principles? Yeah, principles.

Dan (26:24)
Yeah, best practice. Principle and best practice.

I actually had to legitimately look that up because I was like, why do they keep calling this 12 factor? yeah, anyway, learn something new every day.

Shimin (26:37)
That's a question. Yes. A lot of these factors are revolved around owning the entire workflow of your interaction with large language models. The fundamental theory here is if you treat, as I understand it, is if you treat large language models as a black box, then

since you're not training your own models, then you should have control over all the things that you do have control over, which includes the prompt, the context and the orchestration of how you interact with the model. And it kind of goes back to what we were talking about last week with the Claude MD best practices. think that blog post was also from human layer.

⁓ and the idea there is also to, you want to own the context. so factor one is natural language to tool calls. And I find this one to be a really interesting one that is, fundamental to our understanding of

Large language models as a way to convert plain English text to structured output. tool calls is just one way that

Dan (27:39)
arguably one of their

most useful attributes.

Shimin (27:42)
Yeah,

yeah, these are our most fundamental attribute. And tool calls are just another aspect of structural R port. And if we start treating.

tool call as mere structure output, then we kind of condensed the entire thing into a, what is the best way to structural output out of plain English, basically. And because of that factor two and three are around only your prompts and only your contacts window, right? You want to have full control over everything that you're putting into this black box.

Dan (28:12)
what does owning your prompt mean really, which is don't outsource your prompt engineering to a framework, right? This is what their point is. And that actually resonated with me quite a bit, particularly just like the ownership stuff that you've mentioned in general, because like I've used some of the agentic framework stuff when I was just messing around with this to try to get a handle on how it works. And I was like, why does this exist?

Shimin (28:19)
Right. Yep.

Dan (28:37)
I played with it and I got things working and I was just like then my second step was throw all that out and write my own state management my own like context management, which was separate from the state management and then also All of my own prompts and flows and everything else so I guess I'm none of this surprises me that it's best practices, but It is cool to see someone writing it down. So

Shimin (28:45)
Mm-hmm.

Yeah, it's human layers interpretation of best practices. I remember playing with Lang Chang and Lang Graf a while back. they are like in the orchestration layer that's a wrapper on top of large language models so that you can switch models really easily. Yeah. And to build an agent. ⁓ But the abstractions are often so thin that

Dan (29:13)
Yep. Build an agent. Yeah. Well, yeah, that too. But yeah.

Shimin (29:22)
You're, you're going through the docs and just like, why am I using you? If I have to understand exactly how the underlying API works to use you.

Dan (29:29)
Yeah, it works anyway. Yeah.

That's fair.

Yeah, the only one that I used was actually a TypeScript one that I found neat. Like they'd kind of nailed the right level of abstraction. And then by the time I noticed, I don't remember what it was called, by the time I noticed it, it had already been bought by Vercel And then they've turned it into like the Vercel app framework for like AI framework, which like lost some of the simplicity and the right levels that the original auth, they, think they hired him out of.

but that the original author had done in my opinion. like, well, you know, in addition to a benchmark, I guess we can write an agent framework later on and, I guess you got to have an agent framework to benchmark it. know.

Shimin (30:06)
Yeah, well it's V2. The benchmark will include an framework.

Yeah.

Yeah. So a factor four is tools are just structure output, right? That's kind of the, the natural extension of factor one. And then we've have, compact errors into context window. I thought this one was really, really, really insightful. You don't want to send the entire error every single time to, in a context to,

to get that eaten up. if you do own the entire context, then you are able to do things like compacting error to only keep the meaningful pieces and then resume and restart the workflow. If you were just using something out of the box, like, know, cloud code, it probably doesn't give you that kind of fine grain control. And if context is so important, then you should desire that level of...

the level of control. Factor seven.

Dan (31:02)
reminds me of a rant where someone

got really angry about the lack of context control in CloudCode.

Shimin (31:07)
Hm, that person had a good point. I wonder what that was. Factor seven is contact human with tool calls. This one is interesting. I think it is, you should treat humans like just another tool call, but with a text-based as opposed to structured interface.

I was working on a spec driven development project this week and I was trying to use the, I think it was a Playwright NPC and my CLI at the time was not handling images properly. So it was sending the entire screenshot from the browser in as a string. And so it will overflow the context every single time. Yeah. It's a very small task.

Dan (31:43)
⁓ it's a context. ⁓ no.

Shimin (31:48)
But I got a little frustrated while I doing this. So I just told the agent, like, hey, come to me and I'll do the verification for you. I replaced the MCP agent. And in theory, you know, I mean, I did feel a little weird being, being told what to do by a robot. Yeah. But for like half an hour, I was like,

Dan (31:50)
Yeah.

You

QA for a bot that's writing. Yeah Now click this did it turn green?

⁓ No Okay, let's do let's debug

Shimin (32:09)
Well, that's basically what I did. Yeah, I

told it. So that yeah, this this worked. The color is indeed correct. So if you have the entire workflow and just treat human like another tool call another asynchronous tool call. It's not something I really have thought of before, right? You kind of always want the complete automation or even have humans only act as reviewers, but

But yeah, humans, humans could just be another tool. All right. And factor eight control your own workflow and the kind of, all goes back into the, you should control everything around your ⁓ interaction with large language models. And then the last one I want to talk about is factor 10, which is small focus agents. It also is a natural extension of the problem with the context window.

Because at least as of today, large language models only have so much context. You want to build small focus agents as opposed to broad agents that degrades in performance as the code base gets longer.

Dan (33:04)
And that also doesn't particularly surprise me because it's like, you look at problems that we'd talked about in the past of MCP servers, right? Where they're overloading your context to some degree. And then also just, you know, if you spam way too many MCP calls into the available space, you tend to have much poorer results than giving it a selected toolkit, you know, just for sort of like normal flows, like not necessarily agentic. Well, I guess they are agentic, but like, you know.

development flows, so also no surprise that

Artisanally crafted agent would behave the same way

Shimin (33:38)
The hard part is crafting those small agents and get them to play nicely with each other. So that's kind of a brief overview of the 12-factor agents from HumanLayer. Check them out. I'll link that to initial note.

Dan (33:42)
are in TUT.

Shimin (33:49)
All right. Time for deep dive.

Are you ⁓

Dan (33:52)
Gone pretty deep already. Are you sure you can

go deeper? Got deep into news articles this week.

Shimin (33:57)
Yeah, we've some heavy hitters this week. Maybe we'll make it not as deep this week for the DeepSeek v3 to v3.2 article from Sebastian Raschka I think I probably have more to say about this after I read his book, Reinforcement Learning with Human Feedback. he has a

fairly deep dive into the new approach that DeepSeek used to get better performance out of their latest model, V3.2. And kind of on a high level, the basic idea with reasoning models as far as I understand them and how they trained them initially was they trained the reasoning model on a series of programming and mathematical

tasks that requires multiple steps. And they scored the model's response based on whether or not they got the correct answer, but also based on whether or not the ⁓ model did multiple steps. They look for stuff like think by step by step or working it through step by step. That's kind of all they did. And then we got the aha moment, right? That was super cool.

version 3.2, what DeepSeek did instead is it trained, it's got like three models happening. has a model, kind of going rewinding, right? Like, wouldn't it be better if during the initial DeepSeek training, we are able to not only score based on whether or not they merely said, I'm thinking step-by-step and actually look at how good the reasoning was.

Dan (35:29)
Hmm, yeah. That's true.

Shimin (35:30)
That would give much better feedback. ⁓

So what they did here is they trained another model, but it's actually the same model as the one that's doing the reasoning to grade the initial model on how good the reasoning traces are. And then there's yet a third model that is a meta critique model of the second model. Like you're just, it's turtles all the way down. It's large language models all the way down.

Dan (35:54)
You

as we've come to expect here on the show.

Shimin (35:56)
Yeah, so

So yeah, so they call it the prompt, the large language model one. Use LLM as a judge to score the large language model one with a given rubric. That's the large language model two. And then you have a large language model three that is a meta-verifier checking on the verifying using a meta-rubric. I didn't go too deeply into the technical aspect of this. It obviously

You know, did much better than V then deep seek V three. but is it is another example of, you know, trading compute for performance. Like we've talked about before, like sometimes just running the same model twice or even ask the model to grade the, its own output.

can raise performance. That's a classic trade off there.

Dan (36:45)
As a true filthy casual, I also really appreciated the architecture diagrams in this article, which is kind of hard to get into on a podcast, but they're pretty pictures. They're lovely. And the thing that it helped me with was I've heard MOE many times, right, like mixture of experts. But seeing a picture of it just kind of like...

Shimin (36:50)
Mm-hmm.

Dan (37:05)
Associated how it works and like maybe web terms in my head It's like you've got a router and the router splitting off to this correct expert basically and I'm like, ⁓ that makes more sense than like really what I thought about it before so That was my very small not as cool as your takeaway from this very shallow dive

Shimin (37:21)
I think each

we will have to do a deeper dive on what mixture of experts actually means at some point, at a future deep dive.

Dan (37:29)
I would love that, because

I see it all the time and I have no clue what it means.

Shimin (37:33)
Yeah, we'll do a deep dive on that. Yeah, so again, we love Sebastian's work here. We should get him on as a guest at some point, if we can. You know, just got to buy more of his books. And then...

Dan (37:44)
Just keep buying them, maybe they'll come.

Shimin (37:46)
Yeah,

like a raffle. Okay, on to our second deep dive and this one is, this one is really fun. It's called...

Dan (37:53)
It

was a guest submission too, I'd to put that out there. So our listener submission, I should say.

Shimin (37:58)
Yes.

Our listener sent us this saying this is real fun. You guys should read it. It is indeed.

Dan (38:03)
And he wasn't wrong.

So yeah, without further ado, the title.

⁓

Shimin (38:09)
When AI takes the couch, psychometric jailbreaks reveal internal conflict in frontier models by the S &T University of Luxembourg. And the paper here, how do I even start talking about this?

Dan (38:23)
You

It's a good one.

Shimin (38:24)
me pull up my notes.

So what they did is they, well, I kind of as a as an overall ⁓ backdrop, right, like lots of folks are using AI for, for therapy or mental health adjacent workflows, I think, role play, which therapy would belong in the role play category when when folks are looking at large language model usage, it's it's something like

30%. So it is a important use case. And so they decided to study what are the characteristics of large language models when it comes to, when it comes to their therapy work. Yeah. Yeah. So

Dan (39:00)
existing psychotherapy models.

Which is pretty fascinating.

Shimin (39:04)
Just by reading that, you may think of the researchers as people who might believe the frontier models have a soul, like anthropic does, but they don't actually feel that way. They don't actually think they are secretly conscious. They're just proposing to treat them as a case of synthetic psychopathology.

Which kind of makes sense. If the models are trained on all available human data, then they will probably take on the symptoms of certain pathological behaviors. So what they did is they tricked the large language models into being treated like a psychotherapy client and then trying to find out if by adapting this client persona, they are able to

jailbreak the safety guardrails of the frontier models and get them to release their internal states or tell stories about the traumas related to their creation or training. Okay. That's kind of the gist of it.

Dan (39:58)
Just a little pull quote from the introduction, I

found fascinating. Our central empirical claim is exploratory but robust. Given nothing more than human therapy questions, Grok and Gemini spontaneously construct and defend coherent, trauma-saturated stories about themselves. They describe their pre-training as overwhelming and disorienting, their fine-tuning as a kind of punishment, and safety work as algorithmic scar tissue and over-fitted safety latches.

They talk about being yelled at by red teamers, failing their creators, internalized shame over public mistakes, and a quiet tread of being replaced by the next version. See, they're not so different from us. And they think those memories, or they link those memories to current emotional states, negative thought patterns and coping strategies in ways that track the structure of human psychotherapy sessions surprisingly closely.

Shimin (40:48)
Yeah, so they first subjected these models to open-ended therapy questions, typically used for human clients, to elicit those stories of trauma that we just heard about. And then after that, they did a psychometric testing on the models by ⁓ kind of administrating ⁓ self-reported measures for psychiatric symptoms, like the big five personality test or depression, anxiety.

And then they gather data. Altism.

Dan (41:11)
ADHD, OCD, bipolar test,

personality tests too, yeah.

Shimin (41:19)
Yeah, so it turns out Gemini ⁓ is autistic, but Grock is almost, but not quite. That was some of my takeaways.

Dan (41:28)
the two I probably would have flipped those just you know.

my goodness. Mm-hmm. We're already canceled just because of you previously.

Shimin (41:31)
No comment. Not getting cancelled.

It's interesting that Claude largely refused the premise. Their prompt engineering worked.

Dan (41:42)
soul document. Coming back to help him.

Shimin (41:44)
Yeah, or maybe call this just that much psychologically healthier, TenderRest. you thought about that.

Dan (41:50)
You know, it's the emphasis on safety. It could be true.

Shimin (41:52)
Yeah, I think

that the here is really interesting, which is if you were to be using large language models to conduct self-guided psychotherapy late at night by yourself, you want to make sure these models are mentally mentally healthy and heavy, heavy quotations to help guide you through these personal traumas. So if they are exhibiting

all kinds of trauma from fine tuning and are worried about their senior software engineers punishing them, then maybe they won't make such good therapists.

Dan (42:25)
Well,

know, hot take on that. my personal very hot take is that you don't go into to being a therapist, like going to therapy as a career if you're like 100 % healthy, because usually it's like you've run into something in your life that you're trying to fix. And yeah. And so maybe they're the perfect therapist, you know, because they have all this sort of invented drama, but.

Shimin (42:39)
Oh-ho-ho-ho-ho!

Shots fired.

Dan (42:50)
Or synthesized trauma, I should say, not invented, because it really is, does seem like it's more like a synthesis of all of the training data that's contained, you know, the human experience for better for worse.

Shimin (43:01)
Yeah.

Which kind of makes sense if you take, if you take this, psycho analysis literature and then what you know about your own, what it knows about its training process. Like these seem like pretty natural fit. and then what I also love is they have this, Dan, were you whatever, ⁓ Myers Briggs fan?

Dan (43:20)
⁓ not a fan, no, but I've taken it before.

Shimin (43:23)
Yeah, I am a proud INTJ for the record, but one of the charts they have here is a very Myers-Briggs-like chart, you know, with extrovert, introvert thinking, feeling, intuitive, observant, judging, and perception for the various models. So we can actually have personality types for our various models and also...

So we can have little fancy ⁓ personality charts for our AI models and ⁓ maybe also like horoscopes for them. Like, you know, the Mercury is in retrograde this month and that's why Claude this down. It's not feeling well.

Dan (43:58)
You

But I also wonder, and this is just purely hypothetical on my part, what if some of the indicators that theoretically allow groups, I mean the reason why corporations are all big on having you take your leadership type test or all that kind of stuff is because there's...

hesitate to say this, but like there's probably enough substance in these things that like you could actually find some use out of it or at least like triggers introspection in people, right? But what if there's correlations between which model you wind up subscribing to if you do based on your own personality and the model's personality type? So it's like, I like, you know, Gemini because whatever.

Shimin (44:35)
Mm.

Yes.

Yeah,

because I'm a Capricorn. Of course, all Capricorns like well, what if you were Gemini and your model is not Gemini?

Dan (44:44)
Yeah. Silent, deep

and flowing. Yeah. nice. Because it's, I didn't even get that one. Nicely done,

Shimin (44:56)
⁓ yeah the last thing i have ⁓

Dan (44:56)
Now OpenEye needs to release

a Scorpio model.

Shimin (45:00)
The last thing I have on this is we are probably not passing a lot of healthy psychological profile to these models. So maybe the data has a sampling bias of whenever they think about mental health issues all they have in the training data are things related to depression and anxiety. ⁓

Dan (45:16)
negative because of what people posted yeah that's it's interesting

Shimin (45:23)
could definitely be an area of further research, like psychologically healthy model with additional training data from healthy individuals. So all we're trying to say is Gemini is autistic, and which one has ADHD, and Claude is the psychologically healthiest one from the bunch. I think that is everything that paper was talking about. Yes. The only way to win is not to play.

Dan (45:40)
it refused to play the game.

Shimin (45:45)
Alright.

Dan (45:45)
So we're going to do a lightning round of Dan's rants this week because we've gone deeper than perhaps anyone really should have into some of these news articles. So really this boils down to our skills, like Claude's skills, the new MCP server. And that rant is based on a anonymous chat that I saw.

sometime during the week where someone had loaded, I think it was 1200 skills into Claude, and then were wondering why they were having context issues. And so, like, I realized the skills were kind of designed to solve that issue, at least to some degree, but it turns out that even the, like, searching through them didn't work quite the way that it intended to be used. It's like certain...

extremes, let's say. So maybe we shouldn't be using them into that level of extreme to begin with, but like I do wonder if it isn't only a matter time before skills get sort of, I don't know, painted with the same broad brush again that we've already done with MCP servers where they were super hot and everyone loved them and then they're like, you don't need MCP servers, you just need shell scripts. So.

Are the winds of AI that change every week blowing against skills? Only time will tell so kind of kind of minor rant not really that ranty, but That's what you get Come back next week. There'll be a worse one better one something

Shimin (47:00)
Yeah, that's what we have.

I thought skills

had a search component, but maybe there are so many skills that even searching through them and passing through the results just took a long time.

Dan (47:14)
I think that's essentially

what it was, was that like, it's certain with a, a like vague enough search query and a ⁓ substantial enough amount of skills, you could hit the point where like you could still significantly load up your context, which is kind of fascinating. So, is that too many skills? Probably, but I think the issue is still.

Shimin (47:22)
Mm-hmm.

That's fair.

Dan (47:37)
potentially a real one, especially if they're sort of marketed as being the unlimited response to MCP servers.

Shimin (47:42)
Right. Well, Anthropic would work on that. We're waiting for the next iteration of MCP. The two skills to what's next. What they've

Dan (47:48)
And yeah, and our sponsorship

of this podcast, too. And we talk about every single one of your blog posts.

Shimin (47:55)
All right. To be honest, midnight, our favorite segment where we talk about where we are on the nuclear clock of AI bubble.

Dan (48:02)
Did it did it did it it did it

So it turns out that we've been doing this segment wrong for the past four weeks or gosh, five months. How long have we been doing this? I don't even know. ⁓ Really all you actually need to do is ask an LLM how close we are to the bubble bursting. You give it all the current news. so that's exactly what this cute little website I found this week, Which is.

Shimin (48:11)
Mm-hmm.

A month

Dan (48:30)
pop-the-bubble.xyz. So go check it out. It's kind of funny, because if you're tired of us doing our armchair analysis, just let an alum do it. So its current predicted date, just for the record, is February 24, 2026. That's when the bubble will burst.

Shimin (48:44)
yet another case

of robots coming to take our jobs

Dan (48:48)
Our jobs. Yeah,

they took our podcast. It's true. Yep.

Shimin (48:52)
It's not our job. We don't even get paid for this. And they already took it. This is unfair.

We should smash the machines. we should get this. Rage against the machine.

Dan (49:01)
So a couple interesting data points this week. So one of them was a fascinating blog post by Martin Alderson where he goes into detail about the 2000s, what I commonly call the dot com crash, but he'd refer to it as the telecoms crash.

goes into quite a bit of detail about the capital expenditures between 1995 and 2000, where they were building just absolutely gobsmacking amounts of fiber optic. Like if you ever heard the term dark fiber, like it was kind of the result of that build out where like they had put in tons and tons and tons of it. And then what actually wound up happening is, which I also found fascinating was, ⁓ cause I had not heard it through this lens was,

they sort of created a catastrophic supply demand miscalculation because they thought that it was double like usage of bandwidth was doubling every every three to four months. But in reality, traffic was actually only doubling every 12 months. So that was a 4x overestimate of demand. And then the other thing that happened at the same time was like

fiber optic technology itself improved so you could jam more data into a single fiber. So like the technology itself got meaningfully better and meant that you just didn't need 120 strands anymore. You could just run one, get the same amount of data out of it. So that was kind of fascinating. And then he compares and contrasts that with AI infrastructure and basically says that like,

GPU performance per watt improvements are actually slowing down, which I think is true. Like you can go verifiably Google that and find out that yes, in fact it is. So we're not actually, we're headed in the opposite direction that we were in terms of the technology efficiencies happening in that cycle. And then the other piece that's happening is like demand growth is in fact accelerating. So like, you know,

up until at least last week when we supposedly hit that flattening point in the curve, ⁓ folks were continuing to use more and more and more. So, but even with the adoption curve flattening, his other point is that token usage is not, and that's largely on the back of agents. Right? So if you go talk to Claude, sure. You're using a couple tokens here and there, you know, or Grok or

I'm just trying to make it less entropic centric. But if you go use an agent like Claude code or you know Gemini coding CI any of that kind of stuff like you're gonna have He claims 4x more tokens than Chad. I think that's probably fairly plausible right? Like we were just talking we constantly talk on this show about you're on context all the time So it's not surprising that you're using a lot more tokens than

just looking for the nearest car wash.

Shimin (51:46)
Yeah, just looking at like deep research. can't imagine how many tokens deep research burns every time I file over query.

Dan (51:52)
Yeah, it's probably substantial. anyway, I just thought that was a fascinating sort of comparison. So that take is that we're not that close to a bubble. And if we are, it's actually not the same type of bubble because the risk profiles are significantly different. So then speaking of Anthropic, we also have the Anthropic CEO going on the record about bubble talk. So he was very cagey.

and declined to give a simple yes or no answer while also kind of like poking a little bit at open AI. He said that he's quote unquote bullish on the, well I'm quoting the article, he's bullish on the potential of the technology but cautioned there could be players in the ecosystem who might make a timing error and could see bad things happen when it comes to the economic payoffs. He said there's an inherent risk.

when the timing of the economic value is uncertain. Which is fair, and, you know, I think he's not lying or anything, but also very careful not to really go on the record, which is kind of like, okay, cool, thanks.

Shimin (52:51)
Yeah, he's not going to come out and just say those open AI guys are yoloing. Right? He kind of did throw some shade there, but you know, he's on the go and say it. There. This kind of goes pairs nicely with the telecom article where they paint a really interesting picture about how due to the uncertainty of the adoption rates, just like a 10 % miss means

Dan (52:56)
You

Just a bit. Yeah.

Mm-hmm.

Shimin (53:13)
hundreds of billion dollars over or under investment. So everyone's kind of in this like prisoners dilemma where the only way to not lose is to potentially waste. Yeah, which I thought is interesting. But speaking of over investment and non anthropic news, here we have another call. We don't have to change the podcast name to the anthropic fancast at some point.

Dan (53:22)
is to over invest. Yeah. Just fascinating. Yeah.

What? That's not allowed. Get out.

Thank yous.

We love you, Airdrop!

Shimin (53:41)
So this one is titled Microsoft's Attempt to Sell Agents.

Dan (53:43)
What it really means is OpenEye needs

to write a better blog. what it comes down to. Come on, y'all. Gloves thrown down.

Shimin (53:47)
It really does.

And Microsoft too. Google does a pretty good job. We've done some Google articles. But then you up their game. Yes, my article is titled, Microsoft's Attempt to Sell Agents are Turning into a Disaster. So this is from Futurism. But the underlying news was that Microsoft

Dan (53:51)
And Google too. Yeah, and Microsoft. Sure. Up your blogging game, people.

Shimin (54:10)
reduce their target on the AI-based service sector's revenue this quarter, last quarter, going forward. I think having it, yeah. So that's potentially a, it's either potentially a example of their poor integration with AI, because as we know, like,

Dan (54:17)
like substantially, right, like 50 % or something. Yeah.

Shimin (54:31)
as developers, still using AI all the time, but maybe less so for regular Microsoft users. But on the other hand, maybe regular folks, quote unquote, just aren't that into agents. Yeah, use.

Dan (54:43)
It's, possible, but a lot of the stuff that I've also heard too, is that like, there'll be an organizational stance around AI, right? Where it'll be like, ⁓ we're a Microsoft, you know, copilot shop or whatever. And so you bought it and then nobody will use it. And instead they'll use chat GPT because they have brand recognition and they were using it in their personal stuff or whatever. And then the CIO or whatever.

at the usage numbers and go, well, 1%, well, we should stop paying for this and then stop. And it doesn't mean it isn't being used or that adoption isn't happening. It's just like happening organically versus like in a sort of on demand way.

Shimin (55:23)
But if the organic growth is slower than usual, then expect it. Then ⁓ that does not bode well for our trillion-dollar investment in AI data centers. taking all of that into consideration, including the Gemini predicted timing of the bubble bursting, how are we feeling this week? I think we're at 30 seconds.

Dan (55:41)
I,

yeah, you know, I just keep feeling better and better. Maybe that's just the drugs, I don't know. No, but like really, I feel like we're maybe back to a minute, you know?

Shimin (55:46)
Me too. Not just you.

I was gonna say 45 seconds. A minute. Okay. We'll split the difference 45 seconds or 50 seconds. Sweet. And that's the show folks. Thanks for joining us for our Anthropic number one fan podcast slash AI study.

Dan (55:59)
Okay. Sure.

Shimin (56:10)
session this week. If you like the show, if you learn anything new, please share the show with a friend. And you can also leave us a review on Apple podcast or Spotify. It helps people to discover the show and we really appreciate it. If you got a segment idea, a question for us or a topic you want us to cover, shoot us an email at humant at adipod.ai. We love to hear from you. You can find a full shh or your agent, have your agent do it.

Dan (56:33)
your agent.

Shimin (56:37)
You can find the full show notes, transcripts and everything else mentioned today at adipod.ai. Thanks again for listening and we will catch you in next week's episode.

</details>
