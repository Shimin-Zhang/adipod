---
episode: "6"
title: "GPT 5.2, Claude Skills, and Hacker Hall of Fame"
date: "2025-12-19"
slug: "6-gpt-5-2-claude-skills-and-hacker-hall-of-fame"
description: "In this episode of Artificial Developer Intelligence, hosts Shimin Zhang and Dan explore the latest advancements in AI, including the release of GPT 5.2 and its implications for the industry. They discuss the integration of Claude Code into Slack, Mistral AI's new coding model, and the innovative MindEval framework for assessing AI's clinical competence. The episode also features a deep dive into AI-generated user interfaces and a lively discussion on the evolving role of hackers in the tech industry."
keywords: "GPT 5.2, Claude Code Slack, Mistral DevStral 2, MindEval, verification debt, HTML tools, Claude Code skills, generative UI, context indicator, Gemini design, CoreWeave, OpenAI enterprise"
appleUrl: "https://podcasts.apple.com/podcast/artificial-developer-intelligence/id1857109105"
spotifyUrl: "https://open.spotify.com/show/4eDLlGoktxMngPNq9aGqLX"
overcastUrl: "https://overcast.fm/itunes1857109105"
pocketCastsUrl: "https://pca.st/itunes/1857109105"
amazonUrl: "https://music.amazon.com/podcasts/da06d4c3-ecf6-498f-abe3-4d3b00026bf2"
transistorId: "30a0719a"
---

In this episode of "Artificial Developer Intelligence," hosts Shimin Zhang and Dan explore the latest advancements in AI, including the release of GPT 5.2 and its implications for the industry. They discuss the integration of Cloud Code into Slack, Mistral AI's new coding model, and the innovative MindEval framework for assessing AI's clinical competence. The episode also features a deep dive into AI-generated user interfaces and a lively discussion on the evolving role of hackers in the tech industry.

## Takeaways

- GPT 5.2 offers incremental improvements and new modes for AI applications
- Cloud Code's integration into Slack aims to streamline coding workflows.
- Mistral AI's new model targets the coding space with open-weight strategies.
- OpenAI's enterprise products show significant adoption, especially in non-coding sectors.

## Resources Mentioned

- [Introducing GPT-5.2](https://openai.com/index/introducing-gpt-5-2/)
- [Claude Code is coming to Slack, and that’s a bigger deal than it sounds](https://techcrunch.com/2025/12/08/claude-code-is-coming-to-slack-and-thats-a-bigger-deal-than-it-sounds/)
- [Mistral AI surfs vibe-coding tailwinds with new coding models](https://techcrunch.com/2025/12/09/mistral-ai-surfs-vibe-coding-tailwinds-with-new-coding-models/)
- [Introducing MindEval: a new framework to measure LLM clinical competence](https://swordhealth.com/newsroom/sword-introduces-mindeval)
- [AI should only run as fast as we can catch up](https://higashi.blog/2025/12/07/ai-verification/)
- [Useful patterns for building HTML tools](https://simonwillison.net/2025/Dec/10/html-tools/)
- [Ask HN: How can I get better at using AI for programming?](https://news.ycombinator.com/item?id=46255285)
- [Claude Agent Skills: A First Principles Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/)
- [Generative UI: A rich, custom, visual interactive user experience for any prompt](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/)
- [CoreWeave CEO defends AI circular deals as ‘working together’](https://techcrunch.com/2025/12/09/coreweave-ceo-defends-ai-circular-deals-as-working-together/)
- [OpenAI boasts enterprise win days after internal ‘code red’ on Google threat](https://techcrunch.com/2025/12/08/openai-boasts-enterprise-win-days-after-internal-code-red-on-google-threat/)

## Chapters

- (00:00) - Introduction to AI in Software Engineering
- (02:40) - Latest Developments in AI Models
- (09:12) - Innovations in AI Coding Assistants
- (12:11) - Benchmarking AI Clinical Competence
- (12:59) - Techniques for Effective AI Utilization
- (17:48) - Exploring AI Tools for Web Development
- (22:01) - Personal Experiences with AI Models
- (26:30) - Deep Dive into Claude's Agent Skills
- (27:40) - Exploring Skill Invocation in AI Tools
- (31:38) - Generative UI: The Future of Interactive Experiences
- (36:36) - Ranting About Context Management in AI
- (44:21) - The Hacker Ethos in Software Development
- (50:37) - Two Minutes to Midnight: AI Bubble Watch
- (51:40) - ADI Outro


## Transcript

<details>
<summary>Show full transcript</summary>

Shimin (00:15)
Hello and welcome to Artificial Developer Intelligence, a conversational podcast where two software engineers navigate the ever-changing AI enabled software engineering landscape. We are your study buddies who uses AI every day at work. And sometimes we even read a few AI papers at night. I'm Shimin Zhang and with me today is my co-host, Dan. He comes in both instant and thinking modes. Lasky, Dan, how was your weekend?

Dan (00:40)
⁓ It was alright. I survived some kind of brutally cold temperatures along with I feel like maybe a third of the country and Yeah, very excited that it's like almost 40 degrees today. It feels like I should be on a beach somewhere or something so

Shimin (00:54)
Yeah, we have a 55 miles per hour winds here in Washington, so I may lose power at some point during this recording.

Dan (01:00)
during the recording.

Lovely. Well, through the magic of the internet.

Shimin (01:04)
So this week, we have a few news items on the news thread mail. We have the latest GPT 5.2 model. We have the news that Cloud Code is coming to Slack. have Mistral AI's latest AI coding model and ⁓ MindEval, a new framework to measure large language models' clinical competence.

Dan (01:04)
So, yeah.

Shimin (01:27)
After that, we have...

Dan (01:28)
I

Technique corner. So we're going to be looking at actually a couple of things this week. We have an article entitled AI should only run as fast as we can catch up. We have useful patterns for building HTML tools. And then we have a kind of interesting hacker news discussion about how can I get better at using AI for programming? And then after that, we're actually going to do a rare

One that we don't do all the time.

Shimin (01:52)
Right, we have Vibe and Tell where Dan uses Gemini seriously and is surprised by how good Gemini is. Followed by...

Dan (01:59)
And then we're

going to follow that up with the deep dive. We have two deep dives this week. So first is despite its title, this is actually not an anthropic article, believe it or not, Claude agent skills of first principles deep dive. And then second, we're going to have generative UI. LLMs are effective UI generators.

Shimin (02:20)
And then comes my favorite segment, Dan's rant, where Dan is gonna rant about something. And maybe I'll have a mini rant afterwards. We'll see.

Dan (02:28)
All right. And then finally we have two minutes to midnight, which is where we decide authoritatively how close are we to the AI bubble bursting, popping, floating up into the sky.

Shimin (02:40)
All right, well, let's get started. Our first article this week is coming from, well, OpenAI, but also from MacRumors. OpenAI released the, I'm not sure if it's long anticipated, but it's certainly a new model. The GPT 5.2 model comes pretty quick in the heels of 5.1 and about a week after the OpenAI code

Dan (02:53)
You

Shimin (03:05)
red news where they've been freaking out. So this new model has pretty strong benchmark results. I think at this point, we're looking at incremental improvement on our state-of-the-art large lab models. And GPT 5.2 is slightly more expensive and comes in both instant and thinking modes. So kind of

similar to the idea of tuning how much thinking the model is supposed to do. And the model also has a knowledge cutoff date of August 31, 2025. And that's pretty significant because 5.1 and 5 both had September 30, 2024 as its knowledge cutoff date. So I don't know if you heard this, but there were rumors that

OpenAI had not had success training a new foundation model since 2024.

Dan (03:59)
Wow, I hadn't heard that.

Shimin (04:01)
Yeah.

Hence the code red. They were like, we haven't trained anything new. But it does look like 5.2 is probably a new foundation model that they released quickly.

Dan (04:04)
Yeah.

Although there is quite a bit that can go wrong in training, especially at that scale too. Like it's crazy how much like hardware failure impacts a run for a training model and like how many GPUs you lose during a training run at that scale. It's just like, it's pretty wild. I don't know if that's still going to be the case with Blackwell stuff because I think they're water cooled now, but at least on the air cooled ones it was.

pretty fascinating. But the other thing I found really interesting, but like reading the official open AI press release for this was how much they, they really stress in the language about the economic value that 5.2 will be creating. They're like, it's much better at doing things like spreadsheets and other economically valuable, like they actually use the words like economically valuable tasks in there.

Shimin (04:55)
Mm-hmm.

Dan (05:01)
And so I actually went back and reread the releases for five one and four five to see if they were including that language in there and they weren't. So I was like, Hmm, that's interesting. Maybe that was part of the code red. I don't know. But, ⁓ yeah, in any case, benchmarks look pretty cool.

Shimin (05:13)
Huh.

Yeah, they're really trying to maybe pivot towards making that making that money either that or they're trying to declare that they've reached AGI as we spoke about

Dan (05:30)
they have a financial incentive to do so we'll see how that goes.

⁓ yeah, so we also had a little snippet news. It's not super interesting, but, that Claude code is coming to Slack. so the gist of this is basically, I mean, you've already probably by this point, you know, heard of, or at least use Claude code right? Which is like the command line CLI application you can use. recently in Thropic has included it in

the desktop application as well. So now there's like a little tab for Claude code and that one's kind of funky, at least in my experience, cause you have to essentially give it access to GitHub and then it'll run an agent in their infrastructure for you. so now this is sort of riffing on that even, and you can actually spin up a task from like at Claude in Slack and it will

look at the conversation and attempt to figure out what code base you're talking about from the conversation and then spin up an agent in that code base and do whatever based on the context of the thread. So kind of interesting maybe for something where like you find an issue and you want to just like spin it up and have it crank on it in the background and you don't want to like retype all that context, you know, and do a nice like job description for code ⁓

Shimin (06:26)
Hmm.

Right.

Dan (06:46)
So I don't know that it's like revolutionary, but it's fascinating to see Anthropic thinking about workflow in this way. And then also really Slack kind of like trying to position itself as like a workflow tool where like you can use this kind of tooling in there. So

Shimin (06:59)
Right.

Dan (07:03)
Again, you know, not as there is shaking as some of the model analysis we've been talking about, but it's interesting just to see how folks are jockeying for positions, so to speak.

Shimin (07:11)
Yeah, this changes Slack's total addressable market, right? It goes from in-team communication to almost a Jira like everything about your project is going to live in Slack from now on. I think it's also really interesting that the IDE is designed for a user to navigate a code base and read the code, obviously. Whereas to go from the IDE to Slack means you no longer care.

Dan (07:22)
Mm-hmm.

Shimin (07:36)
what the code output is because Slack is clearly not the best way to explore code base. This is kind of the continuation of our spec driven development talk. We're moving everything to the spec as opposed to, but there's not even a spec. Nothing is saved. It's in the cloud.

Dan (07:48)
Although...

That's true.

Although the one thing that Slack is when you really think about it is a massive set of existing business contexts. So it is actually pretty valuable from that perspective of like, because you probably already, if you ran into that bug in the first place, it came in from somewhere. And then whoever brings it to the attention of the team is probably saying like,

is this a bug or not? And then there's like a little bit of conversation about it. And then, you know what I mean? So there's like a fair amount of like actual guts in there already that are very useful for, for LLM. So.

Shimin (08:24)
Yeah. And next up, have Mistral with their new model. I don't think we talked about this, on the show, Mistral is a French based FrontierLab. They are known to release open weighted models, despite also trying to, of course, ⁓ you know, create revenue from

Dan (08:36)
Mm-hmm.

Shimin (08:48)
from selling services. Yeah. Yeah. So they released the Mistral 3 family of open-ended models recently, and they released DevStral 2, a new generation of its AI model designed for coding. This is coming from TechCrunch. Mistral is also trying to get into the vibe coding space with the release of LeChat, which I think is a great name for a...

Dan (08:49)
posting it themselves.

Shimin (09:13)
CLI-based coding assistant.

And I'm trying see. Their latest model is around 120 billion parameters. And they are shipping all their models under a, I think, modified MIT. So fairly open for commercial purposes. I like.

Dan (09:23)
Mm-hmm.

Then you can download

the weights and just run it. Assuming you got enough hardware. We talked about that previously.

Shimin (09:38)
Right.

Yeah, I find it fascinating that almost every single national champion models outside the US is going with an open weight strategy. Whereas in the US, frontier labs are using co-sourced models. But I'm excited to see where Mistral goes. I'm rooting for them.

Dan (09:55)
Yep. Yeah, it is pretty interesting.

Yeah, I haven't really used their open weight stuff extensively, but I am pretty curious to try out DevStrile too, because I have a pretty beastly machine to run stuff like that now, where I feel like maybe it would actually be usable at fast enough speeds that I could realistically use it in something like an agent workflow. it'd be interesting to kind of, you know, if we ever do make our...

our benchmarking thing that we were talking about in the last episode to compare it because otherwise it's just me looking at it going like, hmm, is this better? Is this worse? I don't know.

Shimin (10:34)
Right, the benchmark performances are, I think, slightly below the Anthrobic and OpenAI.

Dan (10:37)
They are, Yep.

But you're not sending all your data to the cloud, because it's just other people's computers, man.

Shimin (10:48)
trust other people's ever. But speaking of our own benchmarks...

Dan (10:51)
Yeah. ⁓ so if you recall from last week's episode, and if you don't, please go listen to it. Cause it was a pretty amazing one. we talked about a paper where they'd run a series of, sort of like, gosh brain help me now.

Shimin (11:06)
psychometric

evaluations.

Dan (11:07)
Yes,

thank you. That's a good word. was looking like what is psychometric evaluation, evaluations on LLMs to basically see what their mental problems were, which was kind of fun. so now we have the flip side of that, which is, sword health in PR newsroom has is introducing mind of Al, which is a new framework. So it's just yet another benchmarking framework to measure LLM clinical competency as a

Shimin (11:10)
Not a word you use every day.

Dan (11:31)
therapist essentially. So I thought that was kind of funny because like people are certainly using this stuff for mental health purposes. So it'll be like actually kind of fascinating to see, you know, how does this play out over time and or like if this is taken seriously as a benchmark.

Shimin (11:47)
Yeah, and according to them, their benchmark is using LLM as a judge to see how closely the model output matches that of a human therapist. So there's some ground truth in going on there. I'm looking forward to seeing this and also looking forward to maybe finally follow the crowd and use AI or some cheap therapy. Yes.

Dan (12:09)
As a therapist, yeah, that's

true. All you pay for is the tokens.

Shimin (12:12)
Okay.

Yeah, that's much cheaper. Actually, I don't know. I've never really had a pay for therapy before. ⁓ Okay. Onto the technique corner where first thing we got this week is an article called AI should only run as fast as we can catch up. This is from higesh.blog and

Dan (12:18)
You

Shimin (12:33)
I really found this article, this blog post insightful, because it talks about something that I think is not talked enough about in the industry. Assuming you are still looking at the code as a software developer to ensure that the AI works reliably, then the verification of the code generated becomes a bottleneck. And he here has this interesting equation of

verification being a function of learning over creation. So of course, the faster you learn, the quicker you can verify. But also the more that the model can create, the slower you will be able to verify the code that it generates. So this kind of helps us to think about what future

tools could use as well as kind of how our workflow would change. So for example, if verification is visual and instantaneous, then we are much better at processing visual information. And then we can verify much faster because the learning rate goes up. Whereas with text, it is going to be much slower, especially if the code changes multiple sections in code base. And lastly, verification Debt

is scarier than Tech Debt. I'm not sure I 100 % agree with that, but it's at least as scary as Tech Debt.

Dan (13:55)
Yeah, I feel like the consequences there a little bit shorter term than tech. Like if you just yoloed some code into production, it might be why US East went down, who knows?

Shimin (14:00)
Right.

Wow, that, yeah, I can't wait to find out why USC's went down. was a week ago, yeah.

Dan (14:13)
the other thing that I thought interesting about that too, is that the, you know, talking about not only is like models improve, like taking bigger swaths, but also like they're creating bigger swaths at a time. Right. So like, it'll just spit out an entire file and jump to the next one before you even really had a chance to like read the first one if you wanted to.

Shimin (14:25)
Mm-hmm. Mm.

Dan (14:35)
And as that rate continues to increase too, think that's, I mean, that's kind of what they're talking about, I guess, in this, also just like, I'm astonished how it just kind of like one shots of entire file these days, you know, and it used to be, you'd be more like doing inline edits where you were like watching individual pieces come and go. so yeah, that's, that's pretty, pretty interesting. And you know, it reminds me of a rant from a couple of weeks ago, right? Which is that.

What is the most important thing? Your time and verification takes a lot of time. ⁓

Shimin (15:03)
Mm-hmm.

Yeah, verification is

absolutely my bottleneck in my day-to-day workflow right now. But one thing that is actually really hard to verify and that the model is really good at generating are single page HTML documents with inline JavaScript and CSS.

Dan (15:23)
Yeah. So, uh, I found this article kind of interesting. It's from Simon Willisons, right? So he's around quite a bit as a big proponent of, uh, of LM stuff. And this is actually a single article in what I believe is a multi-part series from him. I'm not like a regular reader of his blog, but, um, he even like publishes like a set of tools that are generated by LLMs So it's kind of cool in like,

I hadn't really considered doing something like this, which is the main reason why I wanted to bring it up. So like a lot of what I've been using LLMs for just in my personal workflow are like typically like some sort of their shell script or Node.js or even little simple Go programs sometimes to like solve a one-off thing. it's never, despite being primarily a UI developer, it never occurred to me to like...

make self-contained web pages as tools that can do like one thing well and do it really quickly using an LLM. So he had a couple of examples of ones that he's created. So he made SVG render, which renders SVG code to JPEG or ping, which is kind of cool. PyPy changelog, which lets you generate and copy to clipboard diffs from PyPy package releases. Kind of cool if you're Python guy. And then like blue sky thread, which provides a nested view of a

a blue sky thread. So, kind of cool. But I just thought, you know, not a super in-depth article, but like we talk a lot about like different ways to like leverage OMS for personal glory on the show. And I thought that was the sort of innovative one that I hadn't really personally thought of. I'm sure maybe other people have, but yeah, so I thought we'd cover it.

Shimin (17:05)
Yeah, I found it really good at creating these one-shot, simple HTML tools. I think I mentioned this last week. I was creating a tool to render a PNG in the browser so I can draw masks over it. And that's just something that is really one-off. But you can get a tool to

read everything in your directory and generate a ⁓ searchable, filterable way to navigate those PNG files and then just use your mouse. Yeah, I think it's great at these very targeted paper cut problems that is easy to encapsulate. And the best part is you don't have to read it. It just works.

Dan (17:30)
Nice.

That's true, because the tool

either works the way you want it to, you didn't. And if it doesn't, a new one. Code is free.

Shimin (17:47)
Right.

Dan (17:48)
Yeah, third thing we wanted to go over on Technique Corner this week is really it was a discussion thread that showed up on Hacker News this week that was kind of interesting in some ways because of the debate that it spawned, but also because of people's opinions that were kind of being publicly espoused in the Hacker News thread. So it was ask HN.

How can I get better at using AI for programming? So the author's saying, I've been working on a personal project, rewriting an old jQuery, Dijango project into SvelteKit, It seems like this would be a great use for AI-assisted programming, but I've failed to use it effectively. At most, I can only get Cloud Code to recreate some slightly less spaghetti code in Svelte.

Simple prompting just isn't able to get AI's code quality within 90 % of what I'd write by hand. Ideally, AI could get its code to something I could review manually in 15 to 20 minutes, which would massively speed up the time spent on this project. Do you guys have tips or suggestions? And the very first post in the Hacker News comments is Boris from the Cloud Code team. So he had three tips.

First was, if there's anything Claude code tends to get repeatedly wrong, not understand or spend lots of tokens on, put it in your Claude MD file, which we've heard that before on previous episodes. Two is use plan mode, press Shift Tab, 2X, go back and forth with code until you like the plan and then let code execute, which is also, I feel like something we've talked about a lot on here, and use beads for extra credit. Three, give the model a way to check its work.

for Svelte considering using the puppeteer MCP server and tell Claw to check its work in the browser. This is another two to three X. And then four, of course, you cause this is all basically an advertisement for Anthropic is use Opus 4.5. It's a step change from Sonnet 4.5 and earlier models. I hope that helps. And so the part that I found fascinating was the number of people posting that like,

ClawedMD just gets ignored after four to five posts. And then this huge debate that got spawned in the comments about whether or not ClawedMD is actually used. So there's a whole bunch of back and forth there. But the one takeaway that, you know, I don't think it's like amazing news or anything, but I think that it will make, it makes a lot of sense to me, especially given the context of articles we've read previously on here.

is that like really context management is super important and your context, I don't know, loss or decay starts to happen before you hit the end of the context window. And that's when you'll start seeing like, it's particularly CloudMD get ignored. And I think that might be causing some of the debate because of like, people aren't super aware about where they are in their context window. You can just be like, it's ignoring me, but.

Yeah, it's ignoring you and you also loaded 750 MCP servers before you prompted it. Yeah.

Shimin (20:37)
Before we put in even your first token, yeah.

I don't remember if we mentioned this on our last week's show, but DAX from HumanLayer has a rule of thumb of 40 % is when the performance degrades dramatically.

keep your work using 40 % or less of the token. And once it hits 40%, start a new chat.

Dan (21:02)
Yeah. it was pretty interesting to see like folks from the cloud go team commenting on it and, know, sharing their own, maybe less polished best practices in there too.

Shimin (21:12)
Yeah, it's good confirmation that we're doing a right or maybe not we're doing a right, but we're using cloud code the same way that someone from a cloud code team uses it. I also want to point out that this week we're maybe for the first time not going to cover any links from the Anthropic blog. However, they managed to...

Dan (21:12)
some depth in here. Yeah.

Yeah.

Amazing. They're falling down on

the job.

Shimin (21:34)
Well no, I was going say they are doing a little bit viral marketing, guerilla marketing here on Hacker News. They managed to sneak their content into the show after all.

Dan (21:40)
Yeah,

anyway. Well done, folks.

Shimin (21:44)
They did their best.

Dan (21:44)
That's true.

So speaking of not anthropic, we have a little section that we don't always do on the show, but it's Vive and Tell. And so we're really, it's meant to kind of talk to our own experience. on this section of Vive and Tell, I would like to make an admission to, I guess, you, Shimin

and or the broader internet, which is that I used Gemini seriously this weekend. So two things that, well, first something I'm a little embarrassed about and I'll just put it on the internet because I have no shame. when we'd previously talked about Gemini when they're pro like three, one pro or whatever came out, I actually wasn't even using it and didn't realize it because I didn't realize how their opt-in process worked.

So now I've used it and what I was using it for was I've been doing that thing that I do, which is work forever on my, I have several personal websites and I slowly, slowly work on redoing them over time, which is usually if I'm honest and I don't think this is a bad thing necessarily, but it's like, I use them kind of as a test bed to just play around with new technologies or like.

things that I might not normally use at work day to day and like just kind of broaden my technical horizons a little bit. so for this one I've been working on, well, I also really think that the web today is pretty boring, which we can save that for another, a future Dan's rant at some point. So I was trying to make like a really like wild sort of unconventional design for it. So I've been doing a bunch of design stuff by hand and gotten

Shimin (22:51)
Uh-huh.

Mm-hmm.

Dan (23:13)
So-so with it, but just on a whim, I have a mood board of like all these images that I pulled together. So I threw them all into Gemini and the mockups that I had done for my personal one was like, make me just a static HTML page that like sort of in this vibe. And I was literally stunned by the output. And I think that's largely because I've been such a code Coat fan boy and like,

Shimin (23:42)
Mm-hmm.

Dan (23:43)
I'm sorry, Anthropic, I'm sorry. But code is just not as good at like multimodal stuff, like, you know, visuals. Like it did a ridiculously good job of like spitting out something that like had the, I mean, I had to tweak it a bit, but like it had the vibe I was looking for, which I thought was really cool. And like, I tried to do that multiple times with code and unfortunately got nowhere with it. So.

Shimin (23:45)
you

Dan (24:06)
Maybe this is sort of the next phase of my ⁓ learning experience, which is like, you know, you really should use the best tool for the job, including models, which I know you've been using multiple a lot longer than I have, but yeah. So that was my first like really serious experience with the Gemini CLI over the weekend.

Shimin (24:23)
I wonder if Gemini CLI creates a image first before it codes out the actual site. cause Nano Bananas, Nano Bananas Pro is seriously impressive. I used it to just on a whim today, generate a medieval manuscript version of a diagram that explains how the V6 engine works.

And after a couple of prodding, it came up with a really good diagram with like

Dan (24:53)
I'm

very curious to know why you were doing that, okay.

Shimin (24:59)
Inspiration just hits me sometimes. And it has little medieval dragons in the pistons, kind of like...

Dan (25:06)
for the fire. That's fantastic. Yeah. For this episode. In this episode, the Arby dragons just in the cylinders. Yeah. Well, props to Gemini. I thought that was really cool.

Shimin (25:07)
Yes, it's so good. I need to show it to you. That could be our cover art for this week.

Yeah, super entertaining. ⁓

Yeah. And then they also got the, ⁓ the instructions correct. was first generating random letters, but then I told it to generate actual descriptions of, you know, the parts of the thing that works. I'm doing this because I have no idea how an engine works then. and then it actually like spit out some valid to me looking combination of Latin and English to, explain like what the piston does. It's super impressive.

Dan (25:48)
Interesting. I don't know enough Latin to even make a pithy comment about that, but Explodoramus. I don't know. Yeah, that's enough fake Latin for me.

Shimin (25:55)
Yeah, so.

So use Gemini for image generation and use Cloud Code for writing code still.

Dan (26:04)
Yeah.

that was the other thing I did that I found interesting was I, I used Gemini and then when I wanted to drop in and do some more conventional edits, I switched over to code in the same file and was sort of, because I'm just used to it and it worked pretty well. So it's pretty cool. But yeah, ⁓ a very unusual week where we aren't just purely singing Anthropics praises all week. And we're continuing that into the deep dive section with an article that sounds

Shimin (26:17)
Right, yeah.

Dan (26:30)
Well, I guess we're kind of seeing anthropics praises with the article, but it sounds like something that should be on their blog. Hint, hint, but it's not. It is our deep dive where we go into code agent skills of first principles deep dive. So this is by, ⁓ Han Lee, not Han. So Han, not solo pretty great blog title. and. is not kidding when they say it's a deep dive.

Shimin (26:50)
Mhm.

Dan (26:56)
because they really tore the entire skills system apart in, in code code is pretty fascinating. So it's really the article kind of goes a high level through like what skills are. So if you haven't used them skills are the new sort of entropic tool that is meant to sort of combat MCPs context leaking problem.

And, it allows it to have many, many, many, many more skills than you could have MCP servers turned on and then hopefully use them a little bit more intelligently. So at a high level, there's actually a tool call. there is, you know, akin to MCP, a tool call that's created that basically says use a skill. So that's like the very first.

part of this,

there's a tool call piece that invokes skills within that tool call. It injects the, essentially the header from the skills that are tell it, tell it what each skill is for, for all of the skills that you have loaded into context. And then.

the, the part that I found truly fascinating is there isn't any kind of deterministic flow that chooses what skill to use. It's actually just like a raw inference call. and then once, once the agent has chosen a skill, it loads the skill tool, which is essentially just a very custom system prompt that tells it what tools it

what sub tools it has access to, so like git bash, whatever. And then what, you know, description of the behavior in the prompt. And then the other part that I found kind of interesting is that they actually modify the execution context. So like the tool permissions and all those things get updated at runtime based on what the school has allowed or not allowed in there. And then,

It also injects two, two user messages every time you pull up to skill. One is for the user user. So it's actually for you to see what it's doing. And then the second one is like this huge blob of like all the stuff that it needs to actually do the job. so that was kind of a high level overview

Shimin (29:01)
I want to comment on the framework for skills. I think skills makes a lot of sense when it comes to using the jobs to be done framework, right? Because ultimately we have a workflow that has specific jobs that needs to be done.

Therefore, injecting specific prompts along with specific tools for those prompts in the new execution context makes a ton of sense compared to MCP, where you just stuff everything in a context, and then the LLM has trouble fixing which ones to use. And also, of course, you have better segregation that way. A design prompt, a design skill should not have access to

Dan (29:27)
Mm-hmm.

Shimin (29:44)
remove directories. It doesn't make sense on the surface.

Dan (29:46)
Yeah,

the part I found fascinating too I guess the one piece I sort of omitted in the run through two is that there's also like a skill itself consists of three chunks, right? So there's like the prompt file I think there's like a Jason blocked. I remember that correctly and then there's also like a assets folder where you can have

Shimin (30:09)
Right. Yep.

Dan (30:10)
Like scripts and stuff for it to actually

run. So a lot of the, like the official anthropic ones are, that's how they're doing all the like manipulating Excel files and stuff like that is they have scripts that actually do the manipulation. And then it's just like a detailed markdown of how it should do it. Um, but the thing that I found wild is like, cause we'd talked about this a little bit, in the context of you can actually overload skills too. And.

I had thought that there was more of like an actual like search tool that it was invoking to figure out what's cool, what skill to invoke. the fact that it just jams it all together and a big thing makes a lot of sense to me and it explains why ⁓ some people have run into problems. So, I thought that was pretty cool too.

Shimin (30:40)
Mm-hmm.

I think there is a little bit of context management where after the skill invocation happens in a new execution context, only the result is returned to the initial context. So we get a little bit of context management from it as well, which is nice.

Dan (31:12)
⁓ but if you're interested in, the full deep dive, which I highly recommend, we'll throw it in the show notes after this. ⁓ they went really deep to the point where it's like reverse engineering some of the actual agent code in, Claude code itself, which I thought was pretty fascinating just to see like how this stuff works, you know, it's like, someone that spends a lot of time in TypeScript and working with, tools like this is pretty neat to see how.

Shimin (31:27)
Mm-hmm.

Dan (31:38)
other engineers built them and like how much sort of deterministic thinking goes into a very non-deterministic system.

Shimin (31:46)
Yeah, I agree. It's a great blog post. Next item on a deep dive is actually this one is from Gemini. This one is actually an existing Gemini feature. This is coming from Google Research

the paper titles, generative UI, LLMs are effective UI generators. What they did here is they compared Gemini generated websites or web apps for visual representation of data.

to human generated websites for the same set of data. And then they compared the ⁓ user reception using a ELO score, actually. So the humans are still winning. Yes. Love to be ⁓ part of that team. So the human.

Dan (32:30)
So it's matchmaking. Interesting.

Team human

or team Gemini?

Shimin (32:39)
Team human as of right now website has a ELO score of 1756 and Gemini has a score of 1710. So 40 point difference. do want it. I did look through the methodology and it looks like so they were using the pagan data set, which is actually a pretty good data set for the kind of random things that folks may want to generate. For example, give me a history of timekeeping.

⁓ and the natural follow-up question to that would be like, how were the humans chosen? And are these, you know, 10 X developers or are these random folks you grab off of the data webs? ⁓

Dan (33:19)
You

Yeah, and

who's doing the design too? it Mr. Tufty or just some random, random person we found on Dribbble?

Shimin (33:27)
Yeah.

And also, how much time did the humans have? So what they did was they used Upwork, the kind freelancing site, and gave the human developers a five-hour time limit for generating the comparison websites. So a decent amount of time, right? But I don't think it's the best that humans can do, for example.

But we're still winning. So that's good. That's a little bit of job security for the rest of us for now. And I also found the prompt insightful. It is actually a pretty detailed prompt that they've included in the paper itself. It's got stuff like your goal is to build a rich interactive application.

Dan (33:56)
now.

Shimin (34:12)
not just display static text or basic information. They use research before building the functionality, which makes me think like if I was a human doing this, I probably spent like 45 minutes to an hour just kind of researching the history of timekeeping in human history. Yeah.

Dan (34:28)
to understand it before you... yeah,

that makes sense.

Shimin (34:31)
Right. And they have a generator that generates the web page and a couple of helper, kind of linter fixer uppers to act as post processors before hitting the browser. It's pretty simple, pretty simple setup. ⁓ I think a lot of it comes down to the prompts. And I've actually

To test this out since Google mentioned that they already have this in Gemini, I asked Gemini earlier today to explain to me how a fish swims. And I used ⁓ the thinking option and it did generate for me a little web widget with like kind of swim speed versus drag coefficient, like a little 3D. ⁓

playing kind of interactive demo to help the user learn the lesson. Which is quite impressive, I have to say. It took maybe 45 seconds, but it got the job done. Yeah. So I think this is a glimpse into the future of chat interfaces, because a wall of text is never going to be the best way for anyone to learn, right? This is why we don't all

read a dictionary in order to become a better writer or reader for that matter. I'm impressed by some of these demos and I'm looking forward to see where they evolve this.

Dan (35:51)
It'll be interesting too, to see if like some of this stuff winds up making its way into more persistent interfaces, right? Cause this neat that they're just kind of throw away like here, learn this thing. mean, I guess you can come back to them in your session or whatever, but like at the end of the day, it's, it's sort of still a throw away, you know, ephemeral like experience, but what if you start persisting them too, right? So it's like, this is your personal dashboard that

you kind of evolve over time and it has a UX experience that's tailored for exactly the way you learn or the way you want to consume news or whatever each day.

Shimin (36:18)
Mm.

Well, that's how I stumbled upon the paper for a side project. And Jim and I pointed me to it. So a little bit of circular marketing going on there.

All right, ⁓ my favorite segment, Dan's rant. What are you ranting about this week, Dan?

Dan (36:37)
Good old Google.

So at the risk of being a little redundant, cause I know I have complained about this in the past. Why? And this is now I can actually include Gemini too, since I've really like given that a example usage over the weekend. Why can't we have a simple context indicator that is part

of the tool, the agent tool. So one of things I really like about Klein, like Kleinbot, which is a, it's a VS Code plugin. I may have standalone stuff too. I'm not sure. I used it as a VS Code plugin is they have this great, sort of running context window thing at the top that sort of shows you where you're at in it. How come nobody else has that?

Like the worst thing in the world is when you get from code that like you've hit 10 % left in your budget because like realistically, and we sort of discussed this earlier, like you've gone way too far if you've hit that, right?

Shimin (37:40)
Mhm.

Yep. Yep.

Dan (37:49)
Um, and to some degree, you kind of know when you've had it, but like, would be great. And I think a very useful thing if we just had like old school, like power line, you know, nine K or whatever status bar at the bottom of the tool. That's just like, you've used 6 % of your context, 7%, 8%, 290, you know, it's like, why, why isn't that a thing? I don't know.

Shimin (38:03)
Mm-hmm.

Dan (38:17)
And the other piece of that that I think would be really useful would be like, what if is part of the planning phase that I like to do upfront when, especially when it's like a bigger chunk of work, which I feel like is when I'm hitting this to begin with, right? You're not hitting this on like, you know, fix this little bug or whatever. Why can't we set the compaction rules upfront if you are going to compact?

Shimin (38:39)
Mm-hmm. That's a point.

Dan (38:39)
I think that would be

kind of neat too, as like part of the plan or like, given this plan, tell me what you think the compaction rule should be and then set it. It's like, just given how important context are, again, I know I've hammered on this before, but like, it's really important. Why don't we have better tools? We need some tools, folks.

Shimin (38:58)
Yeah, there's lots of direction we can take where that you can like use color indicators. You can have a little running summary. then you kind of know when it's running out of it's doing a bad job compacting, you know, portions of the previous discussions. So yeah, lots of places that can go.

Dan (39:11)
And the other part that's odd is

like particularly in Claude code, when you do slash context or like slash stats and Gemini, it's, it's a, I don't know how they process that, but it seems like it won't actively handle it when the agent is doing something. So there's kind of like, like if it's, if it's doing a bunch of tool calls, for example, it won't actually do your slash context thing until after all those complete. ⁓

Shimin (39:35)
Mm.

Dan (39:37)
Maybe if you're using subagents, it's different or something. But like, it drives me a little crazy because then it's also like, you really don't have an indicator of where you're at while you're doing whatever that process is too. And it could be using a ton of context depending on how big the files are that's reading and everything else. So it would be nice to get a little bit more, even if it was approximate, just like an indicator of where you're at.

Shimin (39:59)
Yeah, help the user kind of give that feedback early. ⁓ I do want to mention that, yeah, I use Kero CLI at work, and it actually does have a context indicator at the beginning of every single interaction. So another thing that I find really helpful with it is you get to find out exactly how much of the context is being used up from your MCPs to begin with.

Dan (40:03)
Yeah, help the user help themselves.

⁓

Mm-hmm.

Shimin (40:24)
Right. Like we should have full access to that. So, you know, like, I added four MCPs. Now context usage has gone from four to 18%. And like, yeah, maybe delete a few.

Dan (40:31)
Yeah, which you can

figure that out in cloud, but you do have to do like, you know, slash context after you load it. And it does show you what's, what's system prompt, what's context, what's whatever, but that's pretty cool. Kero is the AWS one. Is that right? Nice. have not, I have not experienced that tool yet. Maybe someday. I'm already running three at once. How many more?

Shimin (40:37)
Yeah.

Yep, yep, yep. Make it easy for me.

I- I have a-

Dan (40:54)
You have a rant. You're not allowed to have rants. This is my section.

Shimin (40:54)
there.

I want to have a little tiny Shimin rant corner. We may even cut this.

Dan (41:00)
fine. Okay, we'll allow it this time.

We'll allow it this time.

Shimin (41:05)
all right. My rent for this week is I have been thinking about, the software development industry as a whole. And, you know, you and I both are chronic hacker news addicts. And I, yeah, I just been thinking about the role of hacker and the hacker ethos that is

Dan (41:18)
It's true.

Shimin (41:25)
probably missing in the software development industry as a whole. Like for a young, just graduated engineer, who do they look up to when they think of like, I'm going to become a great hacker. they look for, do they think Mark Zuckerberg? Do they think I'm going to aspire to be a, you know,

mid-level manager at one of the fan companies and collect my RSUs and then go fire.

Dan (41:52)
You

Shimin (41:53)
⁓ that's not who I think of when I think of being, someone who's good at my craft, good at my job. Like I look back and I, I go, I think about, you know, Peter Norvig the head, scientist at Google for many years, or I think, maybe even Bill Gates, right? Like he, called it definitely was. but. Yeah. Carmack is huge. but our.

Dan (42:11)
Carmack

Shimin (42:15)
Are we losing that ethos of of what being a hacker is really about? Are we going away from the kind of, you know, hacking AT &T or Bell Labs long distance phone freak nature? Yeah. We should have a hacker hall of fame. That is my hot take that people need to know. We need kids to think about Carmack the way that

Dan (42:26)
Captain Crunch.

Shimin (42:40)
Folks still think about Michael Jordan. We should have branded Shoe deals.

Dan (42:43)
branded keyboards

Shimin (42:46)
I feel

instantly like 20 years older from that rant of like kids, what's going on with kids these days, but

Dan (42:54)
Well, Claude is their new hacker role model.

Shimin (42:58)
Right, or yeah, or maybe there's no one to look up to because there will be no more jobs. That's also possible. But I think role models are important for an industry. And I don't particularly think Sam Altman or Zuck are amazing role models. So.

Dan (42:59)
It's our friend Claude

Well, they're also, you know, largely business people, right? Not like the sort of coder heroes of your, where they might've been larger than life figures, but they did word that way because they had done something that, you know, required hands on keyboard too. I mean, I guess it's, I wrote probably the first couple of versions of Facebook, but like, I wonder how much he actively, how much time he actively spends coding. Maybe more than I think, I don't know.

Shimin (43:40)
Yeah, or, you know, Richard Stallman, free as in speech, free as in beer, like that kind of gave us our jobs, right? That too, let's overlook that. Maybe he's now a first ballot Hall of Famer, but I think it will be, or Linus, I think it's time to kind of bring some of that cyberpunk hacker ethos back into the software development industry.

Dan (43:46)
Free is in controversy.

true probably all of all of the machines running all of the LLMs out there all running on Linux. It's all built on his shoulders one way or another.

Shimin (44:14)
We need to folk heroes.

Dan (44:15)
true.

Shimin (44:16)
Okay, rant over.

Dan (44:18)
It was a good rant.

I think we'll keep it. You still owe me $5, though.

Shimin (44:23)
What? Why did I you $5?

Dan (44:22)
Huh?

for infringing on the copyrighted Dan's Rants copyright 2000, what year is this? Five, six, where are we? Yeah.

Shimin (44:33)
Yeah, nickel, a nickel every time I infringe on your copyright.

Dan (44:37)
That's true. So now it's time for my favorite segment because Dan's Rants is not actually my favorite segment, believe it or not. My favorite segment is Two Minutes to Midnight, where we look at in the spirit of the old atomic doomsday clock from the 1950s and 60s, how close are we to the AI bubble bursting? And

Weirdly, it has been kind of a quiet week this week in terms of bubble news, bubble clues. So we really only have two things. So I'm going to kick it off with CoreWeave article from TechCrunch where CoreWeave CEO defends AI circular deals as working together. So if you don't know, CoreWeave is a cloud, AI cloud infrastructure company.

Shimin (45:07)
Mm-hmm.

Dan (45:28)
that runs a lot of the GPUs that are running all of this stuff. And they're heavily involved in the circular deal making that has been going on. And we've sort of covered in depth in this segment. So there was an interview at the Fortune Brainstorm AI Summit in San Francisco on Tuesday. And Cora Weaves, co-founder and CEO, Michael, I'm going to butcher this. I apologize, Michael. Intrator, maybe?

Trotter? I don't know. I'm sorry, Michael. ⁓ He defended his company's performance from critics noting that it was in midst of creating a new business model for how cloud computing can be built and run. Their collection of Nvidia GPUs is so valuable, they borrow against it to help finance their business. So you're implying that if you're charting a new path, you're destined to encounter some bumps along the way. So his,

take on all of the circular dealing is that's just like the way that we're doing business right now.

Shimin (46:23)
Yeah, CoreWeave, the company that I only know because I see their prices jumping around like a meme stock all the time.

Dan (46:33)
Whenever one of these circular deals is announced.

Shimin (46:36)
You know, I check CNBC

sometimes for the stocks that have moved up and down the most ⁓ over this past year and Core Weave routinely dropped like 14 % in a day. This is, yeah, I don't know. They seem like a meme stock to me. So I don't know if I take their CEO's words very seriously.

Dan (46:42)
You

Yeah, that's a fair point.

Shimin (46:57)
They have an incentive to pump

up the stock. Here's what I'm trying to say.

Dan (47:00)
That's fair.

Shimin (47:01)
Yeah, next up we have an article from TechCrunch called OpenAI boasts Enterprise wins days after internal code read on Google Thread. And this is a, I guess it's based on a release memo from OpenAI about their enterprise usage.

The use of custom GPTs, which companies use to qualify institutional knowledge into assistance to automate workflows, jumped 19 % this year and accounts for 20 % of enterprise messages. And that while close to 36 % of US businesses are chat GPT enterprise customers, only 14 % is true for Anthropic.

I do think that OpenAI does have a bit of a moat, because all these companies have decided to create a custom wrapper around GPT, with custom knowledge and partly like rag setups. And according to OpenAI, according to their internal...

Dan (47:49)
Mm-hmm.

Shimin (47:59)
research participants reported saving 40 to 60 minutes per day with OpenAI's enterprise products. And that they also reported 36 % increase in coding related messages outside of engineering, IT and research teams. So I think we talk a lot about LLMs for coding, but there is this potentially large iceberg of non-code related enterprise use of AI.

And it seems like OpenAI is doing a pretty good job of cornering that market.

Dan (48:30)
And really that sort of like internal knowledge base one is almost like the perfect use case for rag. When you think about it, you know, it's like, get your companies and anything like mine, you have a giant internal Wiki that has like the collective knowledge of engineering and, know, probably five or six other orgs as well in there. it's like, search is a decent way to get it, but it doesn't always sort of connect the dots for you. And if you have like a reasonably good LLM.

Shimin (48:37)
Mm-hmm.

Dan (48:58)
could see that being really a huge leg up in terms of saving you time especially if it's like a process oriented thing where you have to jump through steps A through you know G to be able to get something done so

Shimin (49:09)
So adoption is definitely happening, but OpenAI also still has that $1.4 trillion of infrastructure commitment. So is that 19 % increase or 19 times increase going to be sufficient to justify that $1 trillion of investment? That's the question.

Dan (49:25)
you

But you

know, according to CoreWeave, the GPUs are so valuable that you can leverage them for purchasing more GPUs, so maybe.

Shimin (49:42)
That was wild. Kind of a lighter news week this week. And I'm feeling pretty OK ⁓ with the enterprise revenue numbers from OpenAI.

Dan (49:43)
I'm

Yeah, I, to me it's not even the numbers that matter that much. It's the fact that like, it has been so calm. There was sort of like a storm of all these sort of like Doomer articles hitting over the past two weeks. And then here we are and there's like barely a blip. So I'm, I'm tempted to move it back. I could be persuaded how much.

Shimin (50:12)
Yeah, I mean the same boat. I'm thinking 30 seconds to a minute, which is funny because the SMP has been down all week, but yeah.

Dan (50:20)
Right.

That is interesting.

Shimin (50:22)
It was at 50 seconds last time. I'm happy to move it to like a minute 30.

Dan (50:24)
Yeah.

Alright, wow, we're feeling very comfortable this week. Okay, let's do it. And we'll see how we fare in a week. That's the cool thing about doing this every week is we get fast feedback loops, my favorite kind.

Shimin (50:31)
You know, just like the investors.

Yeah, I'm

going to YOLO like the investors of CoreWeave. I'm going to meme stock our clock.

Dan (50:41)
Hahaha

That's true. All right. So yeah, there you have it. Two minutes to midnight. In this case, almost two minutes to midnight. One minute and 30 seconds to midnight.

Shimin (50:46)
All right.

we should celebrate when we finally hit two minutes in midnight. But yeah, that's the show folks. Thank you for joining us for our little study session AI catch up this week. If you like the show, if you learned something new, please share the show with a friend. You can also leave us a review on Apple podcast or Spotify. It helps people discover the show and we really appreciate it. If you have a segment idea, a question for us or a topic you want us to cover, shoot us an email at humant at adipod.ai.

We love to hear from you. You can find the full show notes, transcripts and everything else mentioned today at adipod.ai. Thank you again for listening and we'll catch you in next week's episode. Dan, do you have any final words?

Dan (51:35)
I don't.

Shimin (51:36)
In that case, we'll cut it.

Dan (51:37)
It's lovely.

Yeah.

</details>
