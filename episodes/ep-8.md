---
episode: "8"
title: "AI Acquisitions, Everyone's a Staff Engineer Now, and Building a Technical Writing Agent"
date: "2026-01-09"
slug: "8-ai-acquisitions-everyone-s-a-staff-engineer-now-and-building-a-technical-writing-agent"
description: "The podcast Artificial Developer Intelligence features hosts Shimin Zhang and guest co-host Rahul Yadav discussing the evolving landscape of AI in software engineering. They cover recent AI-related acquisitions, such as Nvidia's purchase of Groq and Meta's acquisition of Manus, and explore the implications of these moves. The conversation also delves into the challenges and opportunities presented by AI in the tech industry, including the role of AI in automation and the potential for AI to reshape job roles. The episode concludes with a discussion on the AI bubble and its impact on the economy, highlighting the balance between technological advancement and financial stability."
keywords: "Nvidia Groq acquisition, LPU, Meta Manus, Andrej Karpathy, staff engineer, AI abstractions, MCP, agents, Functionize, Llama, Qwen, DeepSeek, AI agents, career ladders"
appleUrl: "https://podcasts.apple.com/podcast/artificial-developer-intelligence/id1857109105"
spotifyUrl: "https://open.spotify.com/show/4eDLlGoktxMngPNq9aGqLX"
overcastUrl: "https://overcast.fm/itunes1857109105"
pocketCastsUrl: "https://pca.st/itunes/1857109105"
amazonUrl: "https://music.amazon.com/podcasts/da06d4c3-ecf6-498f-abe3-4d3b00026bf2"
transistorId: "a48706bf"
youtubeId: "CBmHcXv7_NY"
---

The podcast "Artificial Developer Intelligence" features hosts Shimin Zhang and guest co-host Rahul Yadav discussing the evolving landscape of AI in software engineering. They cover recent AI-related acquisitions, such as Nvidia's purchase of Groq and Meta's acquisition of Manus, and explore the implications of these moves. The conversation also delves into the challenges and opportunities presented by AI in the tech industry, including the role of AI in automation and the potential for AI to reshape job roles. The episode concludes with a discussion on the AI bubble and its impact on the economy, highlighting the balance between technological advancement and financial stability.

## Takeaways

- Nvidia's acquisition of Groq highlights strategic tech investments.
- Meta's purchase of Manus aims to bolster AI capabilities.
- Even world class AI scientists can feel beyond on the rapidly developing AI field.
- Not all bubbles are negative, technological bubble can bring real efficiencies at the cost of investor capital.

## Resources Mentioned

- [Ho Ho Ho, Groq+NVIDIA Is A Gift](https://morethanmoore.substack.com/p/ho-ho-ho-groq-nvidia-is-a-gift)
- [Meta Platforms buys Manus to bolster its agentic AI skillset](https://siliconangle.com/2025/12/29/meta-platforms-buys-manus-bolster-agentic-ai-skillset/)
- [Karpathy's Tweet](https://x.com/karpathy/status/2004607146781278521)
- [Everyone is a Staff Engineer Now](https://read.engineerscodex.com/p/everyone-is-a-staff-engineer-now)
- [ZhangDong's 2025 Letter](https://zhengdongwang.com/2025/12/30/2025-letter.html)
- [AI faces closing time at the cash buffet](https://www.theregister.com/2025/12/24/ai_spending_cooling_off/)
- [As A.I. Companies Borrow Billions, Debt Investors Grow Wary](https://www.nytimes.com/2025/12/26/business/ai-debt-investors.html)

## Chapters

- (00:00) - Introduction to AI in Software Engineering
- (02:51) - Acquisitions in AI: Nvidia and Grok
- (05:11) - Meta's Acquisition of Manus
- (09:54) - Andrej Karpathy's Reflections on Programming
- (19:51) - Tool Shed: Gemini in Chrome
- (24:55) - Posts of the Week: Staff Engineers and Future Predictions
- (35:48) - Reflections on AI Progress and Future Predictions
- (42:25) - Innovations in Technical Writing with AI
- (51:13) - The Role of AI in Internal Documentation
- (59:44) - Navigating the AI Bubble: Current Trends and Insights
- (01:12:51) - ADI Intro.mp4


## Transcript

<details>
<summary>Show full transcript</summary>

Shimin (00:15)
Hello and welcome to Artificial Developer Intelligence, a conversational podcast where two software engineers navigate the ever changing AI enabled software engineering landscape. We're your study buddies who use AI every day at work and sometimes read a few AI papers at night. I am Shimin Zhang and with me today is my guest co-host Rahul. Wait, that isn't Dan talking. Yadav. Rahul.

Rahul Yadav (00:39)
Hi everybody.

Shimin (00:42)
What is your favorite and best Dan impression?

Rahul Yadav (00:45)
the, think not with that attitude is the Dan Crip that, you know, when you talk about your, two minutes to midnight, you can like, ⁓ just do, you know, XYZ is happening and for 30 seconds to midnight, but not with that.

That's it.

Shimin (01:03)
Perfect. I have a strange urge to eat some Skittles right now for some reason. On today's show, we've got our usual news threadmill where we're going to be talking about a couple of articles related to some acquisitions in the AI space, followed by post of the week where we have two articles, one titled, Everyone is a Staff Engineer Now, and another, a News End 2025 Letter.

After that, we're going to go to VibeIntel, where Rahul is going to give us some hard-won experience with working on AI-enabled automation at his company. I should introduce him. Rahul is the director of engineering at Functionize. Welcome.

Tell us a little bit about what functionalizes and what you do there.

Rahul Yadav (01:51)
Yeah, yeah, all these thoughts my own don't represent functionizes. So anything I said before this and anything else I'm about to say for the rest of podcast, my own thoughts.

Shimin (02:03)
After that,

we're going to do a brief talk about the tool shed, about using Gemini in Chrome and our experience with that.

Next, we will be talking about two minutes to midnight, where as per custom, we will discuss where we are on the AI DOOM atomic nuclear clock. So let us get started.

All right, first up, we have the news that Groq has been purchased by Nvidia. This is coming from the Substack more than Moore but it has also been making its rounds around the news lately. So the news that has happened last week during the Christmas holiday weekend was that Nvidia has paid $20 billion for the

the chip manufacturer Groq and it is taking on all of its IP license as well as the entire team. So this is kind of a Acq Hire situation. Now, if you've not heard of Groq have you heard of Groq before this news?

Rahul Yadav (03:01)
Yeah.

not until this acquisition

for 20 billions worth. I think I'd seen their name here, they're in like some newsletters but didn't really look into it until before this.

Shimin (03:08)
20 billion nuts.

Yeah, I think in our day to day, we don't spend that much time with the low level GPU manufacturers. But Groq is a company founded in 2016 that creates LPUs or language processing units, a specialized type of chips that are

created to efficiently process large language models. The company was founded by Jonathan Ross, who was a part of Google's original Tensor Processing Unit team. So with this 20 billion purchase, NVIDIA has purchased both their ⁓ new LPU design, the second generation that just came out this year, along with the entire team.

What I found interesting about the acquisition is that Nvidia decided to not incorporate the company into Nvidia, but keeping them as a separate ⁓ entity entirely. So Groq will remain an independent company that holds its own IP, along with continuing ⁓ its existing deals using its Groq Cloud product.

Rahul Yadav (04:26)
think it is interesting in the sense that in the future, like if you're not embedding something, when you like aqua-hire the talent, in the future, either NVIDIA assesses their technology from the bottom up and decides like,

Yes, this was, you know, there was something here, but we're on a better path or we can like, take up this market with what we've been working on. Or it could be that they end up selling this to someone else and keeping this separate and clean might be the way to do it.

I don't know if NVIDIA wants to sell anything to anyone. was like, I was listening to, have you heard of the founders of podcast? did a whole one on Jensen Hong and Jensen like.

Shimin (05:24)
No, I haven't.

Rahul Yadav (05:25)
Oh yeah, it's really good. The Jensen one and Elon Musk one, he's done two of like how Jensen works, how Elon works. Those two are very good. And Jensen many years, maybe even like decade or two ago was talking about Intel is going to kill us. So instead I'm just going to go and kill Intel. And I see like when I see stuff like that, that's what I think of. like, and maybe it was nothing back then when he was saying, yeah, we're just going to, we're going to kill Intel.

long term and like, obviously, you know, it's much more likely today they're investing in Intel and everything. So it's interesting from that perspective that

even with the acquisition, they're deciding to keep it separate. think part of it could be also like the third take on this could be you want the big companies always like aspirationally spin up these like smaller departments that can move faster and win faster. And so that could be the third thing that they've acquired it. But they don't want it to operate in how fast and within your moves. It's still like, you know, tens of thousands of people there. Maybe they want them to keep.

them lean and let them give them the feel they want.

Shimin (06:35)
Yeah, that's kind of how my take on this is. I don't think this is an acquired to kill situation. And I don't necessarily think this is an acquired to sell situation since, like, what is money to Nvidia right now? It's meaningless. And so the Groq chips has no DDR or HPE-M. So they are fast, but with limited

Rahul Yadav (06:41)
Yep.

Shimin (06:56)
memory capacity. ⁓ So they are fast. They're good at inference, but they seem to be very, very different architecturally from what Nvidia is currently producing. maybe the integration would be both difficult and also kind of kill the specialness of Groq So in that sense, I think, yeah, it makes sense. We'll see how it plays out.

Rahul Yadav (06:58)
Mm-hmm.

Yeah, pretty crazy. 20 billion.

Shimin (07:18)
20 billion. That's pocket change these days. Speaking of pocket change, Facebook, or I should say Meta, buys Manus to bolster its agentic AI skill set. Let me see if I can. Do we know how much they pay for Manus? This also came out last week.

Rahul Yadav (07:21)
Hahaha

Shimin (07:39)
So for a little background, Manus was one of the first AI agent companies, even before Cloud Code and when we were still trying to find out what agents mean in 2025. I remember reading about

their development blogs about the lessons they learned in building agents. And they build general agents that is meant to do everything for the user, as opposed to specialized agents like Claude Code. They have some interesting demos for using their menace agent to find apartments for a particular city based on the goodness of schools.

They can also use it for HR purposes. A very general AI agents company with, according to Menace, 100 million ARR and they were only maybe 10, 11 month old. And they've already and processed more than 147 trillion tokens this year.

on 80 million virtual computers. So very impressive numbers. Seems to be a very popular general agentic tool for consumers. And Meta got to them.

Rahul Yadav (08:44)
Interesting

I looked up in Gemini to your question like how much did they pay for it? It says the value was two and a half to three billion.

Shimin (09:03)
Okay, so.

Rahul Yadav (09:03)
which

20 times multiple is worth 2 billion would be. Given how hard AI is, this almost seems undervalued. I don't know. Right? Yeah, exactly. But like with the, if you look at some of the other companies,

Shimin (09:16)
What is money?

Rahul Yadav (09:23)
with 100 million in ARR.

They are valued way beyond two billion. And so it is interesting that Meadow was able to get them for like two to three billion. I think there are also some piece of, you one of the things that.

Gemini calls out is like Manus is shuttering all the mainland China operations and moved entirely to Singapore and everything. So I wonder if there's something there that led to less value or something.

Shimin (09:54)
Right, yeah, didn't mention that Meta is based in Singapore, which it's kind of in... I'm sure if this is a proof that Meta is relatively desperate to get those users or get their agents in front of users eyeballs that they have to go all the way to Singapore to purchase a agent startup. But I definitely feel like...

Rahul Yadav (09:58)
Yep.

Yeah.

Shimin (10:18)
out of all the big FAANG companies, Meta feels behind to me in terms of their reach. They were the pioneers of the Lama open weight models. But basically, Chinese models have ate their lunch. No one's using Lama 4 They came out this year, and I feel like I haven't heard about them at all. Everyone's using Quinn.

Rahul Yadav (10:37)
Yup, Yup.

Shimin (10:41)
or deep seek or even Kimi. ⁓ Meta feels very behind. So, in addition to that, I personally have never used any of Meta's AI features. I mean, I still have Facebook. I still have WhatsApp. I even still have Instagram. I have personally not used any Meta AI features and I don't know how they're going to reach

Rahul Yadav (10:43)
Yep, yep.

Shimin (11:03)
consumers if I, know, N of one is of any indication.

Rahul Yadav (11:07)
Yeah, there is a this kind of like, very, you know, loosely tied to this. I was looking at a small business where

the pastor gives their sermon and everything. And the business is to take all of that and create social media posts so that they can have an outreach across all these different things. And so it's not, it's still.

I don't know if you look at the, you know, them as a small like entity, the church is an entity. It at least makes sense to me that they're, you know, you would pay some money to be able to like, I want to be on all the different platforms and everything and build my congregation that way. individuals using it. At what point does everything just become ⁓

slop if everybody's using the same products to write the same or similar things because they tend to favor some things over the others like dash until recently and then like the word delve i was reading was one of the favorite ones of the model so it's like how much does

META a pushing this actually take away from the diversity of posts that would actually make it a better social media platform.

Shimin (12:21)
Mm-hmm.

Yeah, it makes sense for them to just stick Manus into their existing UI. And now we have AI slop everywhere. More so than they already have. My Facebook feed is basically slop central at this point. And it's just going to get even sloppier in the new year. As someone who used dash, I'm an OG dash user. I'm looking at my notes right now. I see like.

Rahul Yadav (12:39)
Yeah.

Shimin (12:50)
8m dashes. I'm kind of offended that LMS have taken my lunch.

Rahul Yadav (12:55)
You used to use it on your own like you would use the dash not just like I don't know there's the regular dash hyphen but then I rarely seen people use the dash I don't even know how I would I don't know how one puts it on there you know like what the key is for that

Shimin (13:04)
Mm-hmm. Yep.

dash, well, you do dash dash and it converts automatically to dash. Lots of editors. The dash is for people who love run on sentences like I do. ⁓ It's a replacement for parentheses. I also love to do parentheses ⁓ between my sentences. So it just serves the same purpose, but looks a little better. ⁓ Still the same ADHD brain at work. All right.

Rahul Yadav (13:18)
okay.

Yeah.

Yep, yep.

Yeah.

Shimin (13:40)
Moving on, our next topic is Andrej Karpathy's tweet that came out on December 26th. And I'm going to read the entire tweet. I guess it's X now from beginning to end, because I thought that encapsulates a lot of how software developers are feeling right now.

Quote, I've never felt this much behind as a programmer. The profession is being dramatically refactored as bits contributed by the programmers are increasingly sparse and between. I have a sense that I could be a 10 times more powerful if I just properly string together what has become available over the last year and a failure to claim the boost feels decidedly like a scale issue. There are

New programmable layers of abstractions to master in addition to the usual layers now involving agents, subagents, their prompts, contacts, memory, modes, permissions, tools, plugin skills, hooks, MCP, LSP, slash commands, workflows, ID integration, and the need to build an all-encompassing mental model for strength and pitfalls of a fundamentally stochastic, fallible, unintelligible, and changing entities suddenly intermingled with what used to be good old fashioned engineering.

Clearly some powerful alien tool was handed around except it comes with no manual and everyone has to figure out how to hold it and operate it while the resulting magnitude 9 earthquake is rocking the profession. Roll up your sleeves to not fall behind. Can I just say Andre, I love him, ⁓ but he could have used a couple of dashes in that very long tweet. It would really help breaking up the

Rahul Yadav (15:13)
You

Shimin (15:23)
that long string of wall of text there.

Rahul Yadav (15:25)
Yeah.

Shimin (15:26)
Yeah, I think this crystallizes. And of course, Andre, you know, he invented vibe coding. We talk about him on this podcast. He is not only a researcher, but also a great teacher. He was at OpenAI for a while. If anyone has reasons to, you know, rest on their laurels and feel like, hey, I'm up to date, it would be him.

And even he feels like he could be a 10 times more productive engineer if he just knows how. that crisis moment, that feeling I think, I think is real and is, ⁓ permeating within the entire industry. Do you see that at your day to day job? Maybe not you directly.

Rahul Yadav (16:04)
Yeah, definitely. You know, he's one of the most prominent AI people in the world. He's worked at, you know, all these companies that we admire and some really cool stuff. And yet

some of the things he feels are the same things we feel. he, you know, we're not so different in how we're feeling about what's happening in the industry right now. So it was at least it was like,

maybe a bit comforting to be like, hey, this guy is supposed to know, you know, everything before it even comes out and becomes public, but he's struggling to keep up and catch up. And so I think that's definitely true. To me, you know, I see that ⁓ a little bit in the day to day where there's

you would see a, you know, there were agents, then you have skills, then you have specs and everything. And the problem is at the end of the day, you still have to.

And there's kind of this like balance that you have to walk where you don't want to fall so far behind that you're still using outdated technology or something where you're like, this is just a fundamentally, you know, you're not using containerization or something ⁓ where it's like, won't you do this? But then the other side is

Shimin (17:15)
Alright.

Rahul Yadav (17:19)
you the field is changing so fast that if you adopt every single thing there's not even a guarantee that all of that would be supported across these different agents and models and everything because they're trying to figure these things out themselves and so to me part of that also comes down to regardless of like

how shiny the new way to do things is or how shiny this thing is. What are the core problems that you need to solve, your company needs to solve and how best are these being solved today and like how much of a you know what order of magnitude improvement would you get from these if you're just like it's for like it's fun it's slightly better but mostly you're

you know, things are still the same. It doesn't really matter as much and it might be better to just not adopt every single thing that comes out. On the other hand, if you can fundamentally unlock something using say, cloud skills or something that you could not before, you can spin up multiple agents at the same time and now you've, you know.

exterior productivity by a few factors then that's definitely worth spending some time on. So and part of it is like you have to go at these things at your own pace and the job you're in the

You know, we were talking about GPUs and stuff you mentioned earlier how we don't really dig deeper into the low level details of GPUs and everything. And part of it is just because we're not in the like...

manufacturing the research side of the industry. If I were a researcher, I very much want to stay up to date on what's happening in the field because some of it might just leave my research redundant to a certain extent or I might have to take that into factor as I'm researching certain ways of doing something. On the other hand, like if there are some new things that are happening that

don't fundamentally change how I build software day in and day out. How much do I need to make sure that I know about it and I'm 100 % into it every single day. So part of it is like, you know, it's about the long game and you have to go at these things at your own pace.

Shimin (19:31)
You, you're the hot takes guy. And that is a very reasonable calm, like, ⁓ hold on, like, it's okay to, to wait and see and, know, put your eyes, eyes on the ball of, know, making your job more productive ⁓ and take, take the bits as they come kind of a solution there.

Rahul Yadav (19:51)
Yeah,

there's like, if I can add a couple other things, after I read this, and you know, everybody's been drawing comparisons to the industrial revolution and everything. And so I was looking up and I don't know what

cars much or anything. before I say that, we'll start there. My car drives itself. So what would I know about what's going on inside?

Shimin (20:12)
Mm-hmm.

Rahul Yadav (20:14)
I was looking up like when did when was the steam engine or the modern car engine created and then Gemini was like, you know, the car engine came from the steam engines. We're talking about the first engine which came which was created in 1769. It led to the first car engine in 1860. So you're talking almost 90 years later from like that engine to the one you could make smaller, you can make more efficient that you could put it into.

cars and then I was like okay took about 90 years to get there. When was the latest significant improvement made to a car engine and I didn't know what significant improvement looks like so I was like it can define it itself and then it was like last significant improvement was pushing the thermal efficiency of these engines past 40 percent which is apparently really hard and so they did this like in the 2020 so within the last five years or so as we were talking about like

250

years from the engine being created to, you know, still making it thermally efficient and leaking out all these efficiencies. That's as long as US has been around. And, you know, this will be our 250 years of existence of the country. And so there's you can't really ever catch up to these things that will just lead to, I don't know.

sadness to a certain extent. And so you kind of have to figure out what are the parts that you're really focused on and then really like, what really ties into your craft and really focus on that. Versus trying to absorb the whole industry is just as Andre is, you know, showing us, he's supposed to know everything and if he can't keep up then what chance do the rest of us have?

Shimin (22:00)
That's true. That's why I've been crying so much at my desk lately. I will say that I do have to say for my personal projects, to the extent that I have personal projects on the side, I've almost completely moved over to Vibe coding for some definition of Vibe coding or agent-assisted programming. Even if at work, I'm not 100 % switched over yet.

Rahul Yadav (22:18)
Yep.

Yep.

Shimin (22:25)
Yeah, it's OK to do some combination of the two. You don't have to go one way or another ⁓ and buy plenty of tissues for the days when you feel like you're super behind. All right, on this week's Tool Shed, we are going to be talking about Gemini in Chrome. Rahul, this is your topic. You want to talk a little bit about your Gemini in Chrome experience?

Rahul Yadav (22:30)
Yeah.

Hahaha.

Yeah.

Yeah, I had read about Gemini in Chrome, think, a couple months ago at this point, we in the US didn't have access to it. I think US was still the first country where this got rolled out, but in phases. And so I got access to it maybe six-ish weeks ago or something like that. But it is probably

⁓

one of the tools that I use most at work these days. What Gemini in Chrome is, is if you haven't used it or hasn't rolled out to you yet for anyone listening, it's on the right side of your Chrome browser, you would see this little Gemini icon. If you're a Chrome user that you can use and you can, the critical thing that it does is it takes Gemini, the whole like chat experience and everything, but it is able to share your screen with that. And so one of the missing

pieces of all these things when you've chatted with you know chat gbt, claud, gemini, whatever is I'm trying to do xyz it's like okay based on what you're saying and we're only like you know it's not like we can describe everything in our situation with perfect fidelity so it's always like help me do this and then it's like okay here's my rough guess on what you're trying to ask me here's my answer to it.

But this adds context, which has made everything so much better. Like I feel much more productive these days when I need to like change different settings, set up APIs, set up all sorts of like access permissions and everything. I don't have to go and figure out what's in the docs or ask the agents to like go look the docs for me or anything. I can share my tab with Gemini and Chrome. It knows exactly the screen I'm looking at.

And then it's like, oh yeah, these are the settings that you should be concerned about. This is how you set up XYZ workflow or anything. And so it's been a game changer. I use it every single day at work, multiple times a day. I've started using it for just some like random things at home as well, where it's like, you know, this website is not to my liking. This is a silly example. You and I were talking about it, you know.

a few days ago where we make a lot of food at home and recipes have their ingredient, the amount listed at the top and then they just go like put this much pepper or put the pepper in and it's like well I don't remember how much pepper you have to scroll up and down. I just shared the whole tab with Gemini and Chrome and be like can you rewrite the recipe so that it actually takes the actual amounts of the ingredients and puts it in there. So

I can't go and rewrite the website, but I can at least shape it to my own liking. And those are the things that were possible before, but it would be more work for me to copy paste the URL and do these other things versus now I can just talk to Gemini and get it to give me, know, help me in the right direction that I'm trying to go in.

You can, it keeps the chat history so you can like do something and say your Google Sheets or something and then go do it. Go do something else in your Slack or whatever. And if you're working across different applications, since the history is preserved, it can actually help guide you through some very.

workflows as well. So big fan. I've been telling anyone at work who has access to go use it. You guys talk about cloud a lot. So part of this, guess, is me trying to balance with some like Google has some cool stuff too. Maybe you'll need to have someone from open, like someone who is a big open AI fan next and they can balance it out with chat GPT.

Shimin (26:23)
Yeah, I use Firefox for the part. And I do use its AI integration feature. I'll have to check out Google Chrome and Gemini. I think what I really like about Anti-Gravity is it has that browser automation built in. ⁓ So I can only see it.

Rahul Yadav (26:40)
it.

Shimin (26:43)
being just as nice in the browser itself. It's never occurred to me to do something like double the recipe amount on a page. But yeah, of course, it could do that. ⁓ yeah, that's great tip. I'll go and check it out.

Rahul Yadav (26:53)
Yeah.

Shimin (26:57)
All right, time for posts of the week. We've got two posts this week. The first one is from the engineers codecs. It's a sub stack I've been following for a while now. The title is called, Everyone is a Staff Engineer Now. And the short of it is,

It talks about what, you know, we're always talking about, you know, how AI assisted software engineering will change the workflow and kind of the nature of the software engineering industry. And this gives a rundown of what are the impacts, what are ramifications of that and what kind of engineer in ⁓ the author's mind would succeed in our new paradigm.

So the lists are the following. ⁓ Maintain context across multiple domains and projects because reading code is harder than writing it. And that's one of those things that I think if it's not a truism before, it certainly is with agents spinning out dozens of lines of code in less than four or five minutes.

So we need to be able to understand and preserve a very detailed working model of the code base so we can review code quickly. And this could be across multiple domains and multiple projects. The next one is meeting focus in a asynchronous workflow. This one is pretty big for me. Instead of going to a flow state for most part of the day, you

either have to batch your AI tasks, spend your time writing ⁓ prompts and providing context, and then wait for the agent to run. Or you just kind of have to split your days into many different parts of writing context and then checking the work. And that is a new skill that you have to learn. And to go from flow state to constantly interrupted is something that I think we all are.

already impacted by this. But it's going to be even more of an issue going forward. The next one is being able to plan and steer agents effectively. This is what makes a senior engineer a senior engineer. ⁓ You should be able to have clear instructions. And those same skills when you're writing requirement documents carries right over to writing prompts for agents or

managing context for agents. Next item, reviewing and read code, overriding it. We kind of already talked about it. If you're good at reviewing code, your productivity just went straight up. If you're slow or at reviewing code, then it just seems like more painful work that you have to get through when you see the flow state.

And lastly, engineering is moving up the stack. And this is one that we see all the time. Folks are creating, whether it's plug-in, whether it's low level programs, folks are able to domains that are at first alien to them.

And as long as we can control the workflow and control the context, we can get more done. organize, orchestrate, as opposed to doing the groundwork.

How did you feel about any of these pieces of Avisis comments observations?

Rahul Yadav (30:17)
I think...

Yeah, some of this makes sense. I think they touched on it very slightly. Let me find where this is. Because I had jumped out. Yeah, one of the things they say under like being able to plan and steer AI agents effectively. They say building a new feature versus updating existing production infrastructure will require drastically different approaches and that kind of

brings me to the if we go back to the title of the article it says everyone is a staff engineer now and what

from their framing, they're saying everyone is a staff engineer, but the things that they're describing and at writing code, not as much as like owning it in production because a staff engineer or you know, any product engineer doesn't much more than like you commit your code, you get it to production, but you also maintain it, you fix it when it breaks and one of the one of the weaknesses somewhat

or maybe like this is happening and I haven't just went out to look for as many examples is when things break, how confident are you that you can go and fix them? then, how usually like if there are simple failures.

like maybe the agents would be able to solve that but if there are multiple complicated things that collide and then you end up getting some failure that an agent just doesn't have enough context to solve you need people who have made some of these mistakes by themselves right with some mistakes you just have to make on your own you can't learn from reading

articles and like having the agents teach you. And so that's the part that I think the article was missing a little bit is there is more to a staff engineer than the pieces they described.

And I'm only talking about the like, when stuff breaks, who do you call piece, but there's also like all sorts of or because I organizational buying part of staff engineer job is actually like going and convincing people across their org to use AI and use agents and everything. So, you know, like, to be able to evaluate these different things and be able to standardize so that you can everybody can have their own agents dot MD and everything and agents can have much more context across these different

think so. Some of that I think the article was lacking in but I guess the headline everyone is kind of a staff engineer is not as catchy as everyone's a staff engineer now.

Shimin (32:56)
Yeah, or

everyone has responsibilities that used to belong to a staff engineer is less catchy.

Rahul Yadav (33:01)
which came,

yeah, like, and you know, on the, on the positive side, what they call, what they're calling out is the like, what's true now, which is like,

even if you're a junior engineer, you're expected to do a senior staff engineer's work because that's what the just the state of the world we're in, which means you have to own a lot more, you have to learn a lot more. And so it does improve or it does like the expectations are just much more higher and you have to go learn all these things. So that was a

positive piece from it. One other thing that jumped to me was like they're saying junior engineers are expected to be staff engineers and all the time you read these articles about junior engineers limiting there's no jobs out there and us reading about how like people are not really getting hired and everything.

because entry-level jobs are like not as, people are not hiring for them as much. And so it's just, there's something there about either you don't get hired or even if you get hired, you are supposed to compress decades of experience within, you know, a year or less or whatever.

Shimin (34:14)
Yeah, on the bright side for the juniors out there, AI also makes learning 10 times easier. So they do have a heads up in terms of having more time than some of the more senior engineers to ramp up and learn. ⁓

Rahul Yadav (34:21)
Absolutely. Yep.

Yeah.

Also

not having strong opinions that you just are stuck to because that's just, you know, how you've done things. So there's a lot of like, there's nothing against that. And ⁓ there are benefits to having people who are not scarred by anything and are just like very hardworking and everything and have a lot of agency that they exercise.

Shimin (34:43)
Right.

They haven't learned that spaces are way better than tabs yet. We need to include them. I see you have no opinion. Okay. Well, on that note, our next post of the week is the 2025 letter by Zhendong Wang.

Rahul Yadav (34:59)
Save it for when Dan is back. ⁓

.

Shimin (35:21)
a research engineer at Google DeepMind in London. He works on post-AGI questions and Gemini. So.

Rahul Yadav (35:30)
Yeah,

there's a little background on this. I recently read, I think he has posts going or his letters going, starting, what are we looking at? 2022, I think was when he published his first letter and he talks about.

He's like shamelessly by his own admission. He's like, I really like what Dan Wang, this person who wrote the breakthrough book about, you know, the US-China race and everything about like how that.

Shimin (36:02)
Can we just talk

about how great that book is? I assume you read it. Yeah, great book. Love that.

Rahul Yadav (36:05)
Yeah. Yeah. Yeah. Yeah. Yeah.

And, and then also, ⁓ he does his. didn't do any letter last year, but he did one this year, which came out, I think, four days ago, or so I think he does it on the first of every year. So anyways, so and I'm I think I'm a butcher this name little bit. John, though, is that how you say it?

Shimin (36:30)
Yeah,

I couldn't pronounce it without knowing the characters anyways. it could, yeah.

Rahul Yadav (36:33)
Okay, yeah.

And so, you know, he really likes how Dan does his annual letters and wants to model that behavior. So he's written a few of these in the past. And then I was reading through his latest one. I'll read through, this is gonna take a couple minutes. What I want to read through are, there's like three paragraphs at the beginning that I thought were,

really interesting and then he goes through like how he got to deep mind and everything and like his thoughts and compute but one of the most thought-provoking parts was in the beginning

We want to think about our future with AI, but to think about the future, let's think about what's happened in the last 10 years. So here we go. Steep yourself in the last months of 2015. The program AlphaGo has just defeated the European champion in Go. The first time a computer has ever beaten a human professional. The 18-time world champion, Lee Sedol.

would be quite unmoved, remarking that the level of the player that AlphaGo went against in October is not the same level as me. And then parentheses, AlphaGo would defeat Lee the following March, so five months later. Elsewhere in the world, there is war in Ukraine. SpaceX landed its Falcon 9 for the first time. Star Wars The Force Awakens premiered. A new startup called OpenAI was founded. ⁓

If you think it through, you won't be surprised to learn that in 2025, programs using natural language under human time controls will win gold medals at the International Math Olympiad and the International Collegiate Programming Contest. Computers will be competing there because they'll have already surpassed, already passed the bar and the MCAT years ago. Lawyers and doctors will still have their jobs though, and global real growth will be gently slowing. Coding agents will

and there's like a emphasis on coding as the job. ⁓ Coding agents will have changed that job forever. A Chinese firm will draw comparisons to Sputnik. A new pope will name himself after Leo XIII explicitly to respond to quote, another industrial revolution and to developments in the field of artificial intelligence end quote.

In your whole and consistent view, you'll point out that AI data center investment will account for over 90 % of US GDP growth in the first half of 2025. A few companies everybody knows will together spend more than the cost of the entire Apollo program, inflation adjusted in 10 months. Yet in the general public opposition to data centers will shape up to be a new bipartisan rallying cry. That will partly be because of a frozen labor market with neither hiring nor

though no one will know if that's due to AI. One lab will offer at least one AI researcher a billion dollars. He will turn it down at first. then attendees enjoying organic British ballettine at President Donald Trump's unprecedented second UK state banquet in parentheses, yes dear time traveler, you heard that right, will include Demis Hassabis, Sam Altman, and Jensen Huang.

Alan there, you can link to the whole letter. he talks about the bitter lesson and how there's still like, people still haven't completely learned it as much and like the power of compute. It was bananas to think about.

In the past 10 years, some things have changed and some things have not to a certain extent. Like, you know, the Ukraine war was the first thing that jumped out that there was a war in Ukraine back in 2015 and there's a different one that we're going, that's happening right now. And then Trump's been president twice in the past 10 years. And so how much does

the world has changed in that time. And then also like you look at, you know, the 18 time world chess champion going like, yeah, you know, that guy was whatever. And then within five months, the AlphaGo ends up beating him as well. And so it's crazy the amount of progress and it's crazy to think that OpenAI, which is now like synonymous with

lot of the improvements we've seen in the AI industry was only founded within the last 10 years. yeah, this really jumped out to me on how fast the field has moved and how much has changed and yet how some things have not changed. Yeah.

Shimin (41:01)
Yeah. And I, I really love using this as a way to maybe not predict the future, but to come up with the right, the right model to think about the future. It's like how, you know, Charlie Munger was always a one that always says, you know, to reverse, always to reverse. And, and I like this approach of reversing and then applying that to the future. ⁓ It sounds like you're predicting that there will still be a

Rahul Yadav (41:11)
Yep.

Yep.

Yep.

Shimin (41:28)
were in Ukraine 10 years from now. Maybe that's the case.

Rahul Yadav (41:30)
Just that

some things are, you know, some things don't change as much. I hope there's no war in Ukraine or anywhere else, but, you know, as the saying goes, geography is destiny. And so some of these things you end up seeing over and over again through no fault of Ukraine.

Shimin (41:50)
Yep.

And of course, Trump will still be on his third term. We're not going there. Okay.

Robotrump. That's it. Yeah.

Rahul Yadav (41:58)
Yeah, it will include Demis, Hasabe, Seymour, Altman, Jensen, maybe others.

Shimin (42:05)
Yes, in their robot forms.

Well, let's do a little vibe and tell, speaking of where AI is currently. You've recently worked on a technical writing agent project at work. And we should mention you are, we already did, but you're the director of engineering, ⁓ Functionized.

Rahul Yadav (42:16)
Yep.

Functionize is a test automation company. So what we do is we focus on

things that are manually tested today. And so you can think about, know, manual QA testers testing all sorts of different parts of an application that are complicated and cannot be automated easily. And we build our own models in-house. And so one of the things I like to talk about with candidates is...

My test for, if they want to work in AI, my test for a true native AI company is if you take AI out, the company ceases to exist. And so you always see like LLM wrappers and stuff, and then you look at like companies that are fundamentally built on AI. So yeah, we're a company fundamentally built on AI, you take AI away, the company doesn't exist. And we do this for a number of Fortune 500 companies.

Yeah, it's a great fun to be able to use AI to be able to automate different things that were just not possible to be automated before. yeah, going into the technical writer agent.

you know, since we're an AI company, I'm continuously thinking about not just building customer facing products that are, you know, leveraging AI to make their life easier, but also internally, how can we leverage AI to really be able to, you know, have the best team possible, be as great as a company as possible. And so what happened was a few months ago, the technical writer on our team

team, they departed. when I was looking at our docs and everything, I started thinking about, can we actually use AI to be able to create a whole flow here where we can create technical docs that you can generate using all different inputs, not just your code base or what your product looks like? So I spent some time. This was a

Shimin (44:23)
Mm-hmm.

Rahul Yadav (44:26)
completely vibe coded. I do not recommend, you know, vibe coding things in production that you have to maintain because going back to everyone's a staff engineer, even if you do it, you have to then like when things break, you have to go fix them. So, or take ownership of anything that you're vibe coding for internal apps, the way I look at them is they're great candidates to be able to do these things.

because the stakes are much lower. You have a lot more margin for even if the thing breaks, it is okay, because there is no customers relying on it, or it's not in any critical path or anything. So I started looking at...

how do you actually even get the source material to write documentation and then all the way to how do you publish your documentation that can then be used and everything. And one of the things that I've realized is, and this kind of goes maybe to the, everyone says is a staff engineer now ⁓ article as well.

Shimin (45:10)
Right.

Rahul Yadav (45:26)
Part of the trick is not just doing, just like working on smaller tickets or like smaller scope things, but be able to map out whole processes and whole like jobs and to be able to then see.

The obvious thing you can do is you can just use AI to be like, which parts can I automate and where do I need the human in the loop because those are bottlenecks that I need to resolve using humans. Another way you can look at it is like maybe having AI means you can reconfigure the whole thing a little bit so that you can redefine the whole process so that it's optimized for an AI to be able to work on it. And then you still have

Maybe you still have humans at some point, but it's not the same process as what you would have done if it was a process run by a human. So I started looking at where does our source material come from? ⁓ comes down to, Slack is always a great for anyone who use Slack or Microsoft Teams or anything. There's a lot of information.

in chat that you can, that could be public, should you choose, if you chose to make it public or you need to have someone who's very vigilant in all these channels whose job it is to make the documentation up to date or someone who's like, who has that mindset of like, hey, this can be public and everything. There are other things like one of the biggest sources of

hey, this should be public information, our support tickets. And that was one of our big sources here is customers ask a lot of questions that once you answer the question or even before answering the question, like the thing that I always ask myself is,

Did they, how could we have proactively addressed this either in our product or if you can't like throw a whole essay on something in the product through your documentation, how could we have proactively addressed this? Because if you're getting a support ticket, then like that's generally not the end state that you're striving for the customer already. Like people don't want to reach out to support unless they're stuck on something.

And so what I did was, you know, I use cursor as my ⁓ ID at work. I planned out this process of, I would like to create a documentation agent. These are the main sources that I'm looking at. And I would like multiple ways to be able to do this. You know, I set up my Zendesk credentials and everything so that we could pull in support ticket data. We also use the Zendesk knowledge base to be able to publish our blog posts and everything.

So I hooked it up so that I could pull in the ticket information, raw information that had like all the different comments and everything, scrub out the anything sensitive information from there, generate documentation from it, and then post it as a draft to Zendesk. Now...

if you try and do that as a person, like I wouldn't be able to get through, you know, more than a handful of tickets a day because it's a lot to like take a whole ticket and you know sometimes the conversations run over the course of days, weeks, months even and you have to like parse all of that to figure out what is the core piece here. And so that was one of the things that really got sped up. The other thing I

Shimin (48:35)
Alright.

Rahul Yadav (48:39)
it was I downloaded our external knowledge base and then I asked Gemini to suggest how do I find similarity so that we don't look like it doesn't end up creating articles that are already existing in the knowledge base and you don't need to like publish duplicates. And so it created this semantic similarity. ⁓

Shimin (48:56)
Interesting.

Right?

Rahul Yadav (49:03)
algorithm where you take the first 500 words, the heading plus the like, you know, n number of words. And then if they're semantically similar, I forget if it's like a by 0.9 or more than it's similar. And then if it's less than that, you create and I think you can define that and then you create a new article. So at this point, I knew what

you know, what we already had published and what we had candidates that or like data we could look into to publish these things. And then the final piece was like, how do we go about automating it? So I got it working locally. I worked with one of my engineers to deploy it internally. And now we have one of our people in support who actually

is able to, and this could further be optimized. Today what we're doing is you could give our docs agent a support ticket or even like a manual chunk of text. Let's say you and I are talking about something related to product. There's some useful information. You can just literally copy paste the whole thing into the text box and say, you generate?

customer-facing docs from it, and it's able to do that, and it's able to post a draft Zendesk article, and then all you have to do is go and review it if it looks great for your head publish. One thing that I think this can all be automated, I haven't figured out is, I just haven't looked into it enough is there's this concept of like sections and categories in Zendesk Knowledge Base, so.

they don't end up in the right category that we would want them to. But I'm sure like it's not a big deal to figure that out. And some optimizations that we haven't done yet are do we even, Slack I think has enough conversation that you need to.

Shimin (50:34)
Mm.

Rahul Yadav (50:47)
paste specific you need to like, you know, pulling specific text into the agent. But for Zendesk tickets and everything, you could take it level further in optimization. And you could use an agent to look through every ticket, categorize them in does can this be turned into external documentation or not automatically generate documentation from it. And then it simplifies

you know, our teammates workflow even further where he doesn't even have to like look through tickets or anything to give them to the agent of like generate docs for this one. All he has to do is review the drafts that are getting posted and then anything that's worth it gets published, anything that's not gets discarded. And so.

⁓ How do you close that loop? haven't figured out yet. We ended up discarding this one. Here's the reasons why, because I think that's good hope, but I think that would be premature optimization. Right now, we're just able to do a lot with our teammate who also works on support.

Shimin (51:45)
Yeah, that's it.

Right. So how do

you, I guess, have you run into any kind of context issues? These tickets can have, you know, images, videos. I can imagine all kinds of additional multimedia stuff coming from Zendesk. ⁓ Did you find you have to do any kind of chunking of the text or of the ticket or anything like that?

Rahul Yadav (52:04)
Yep.

I did the, there's audio not as much video once in a while, but what happens is.

it hasn't been so we don't really like uh parse videos in the agent or anything um the reason why is even if i send you a video over um a zendas ticket in future references um either me the you know the user creating the ticket or one of our support agents ends up actually like describing what happened in the video of like hey you mentioned that you know step xyz had this problem um because at the

Shimin (52:44)
Hmm.

Rahul Yadav (52:48)
of the day we have to like, hey this is the part I'm talking about. And so that surprisingly and that and you know again like we're not starting from no knowledge base at all so we have enough that I think the agent can build on top of that. And so if we haven't needed, we haven't felt the need to actually be able to like parse what's going on in videos or anything like that maybe in the future that might become a problem but for now there's a

we're finding where we can create documentation for things where all you need is a plain text from tickets or from Slack conversations or anything like that. Or from some internal docs that come from your product specs or something where you take away all the technical details and internal details and you can easily turn those into external docs.

Shimin (53:36)
Right. So

almost like the tickets have already managed your contacts for you before you even kind of have to worry about, you know, doing that additional management for, for videos. ⁓ another question I have is what about the, the code base itself? Cause it needs to know about a code or is the existing knowledge base sufficient to kind of create these posts?

Rahul Yadav (53:45)
Yep.

existing knowledge base is sufficient. We do pull in images once in a while when needed to be able to give the model or give the agent more context. It has a needed access to the internal code base. The thing that, and I think we could.

I thought about it as a future optimization. The problem ends up being is you have to point it to the latest like your main branch or whatever, right?

but we don't do continuous deploys or anything, so it's not like as soon as you commit something, it will get deployed to production, so your documentation would be referring to the latest version of the product. so you have to then, part of the thing you have to solve with get tags or branches or whatever is the version of the product I'm generating documentation for, this is the code for that. And also our code is across multiple repos, so you have to

account for all those different things as well. I think we might end up doing that one day if needed. For now, it's given us a lot of things to work with that we haven't needed to, even some of the other optimizations I mentioned, we haven't needed to go down that path.

Shimin (55:10)
Right. And then we're talking about a single agent. Do you have like multiple agents being orchestrated pulling in various data? like if, you use an orchestrator, like what are you using?

Rahul Yadav (55:17)
⁓

No, single agent. ⁓ Yeah, and I ended up using vertex so that GCP has vertex so that you can swap between different models and everything. Some of the other things were like, you know, small things that you run into of like, you've exceeded the context window and everything. And so I had to be like, you know, optimize that piece. But

Shimin (55:21)
Single agent.

Rahul Yadav (55:42)
Yeah, other than that, it wasn't, one other thing that we, it has been useful for is there are things that

you want to create external documentation for, but there's also like, you know, people have internal knowledge base and everything. And for like things that we don't want to maybe necessarily have external documentation for, it has also been very helpful with that, where instead of like, I don't know how many chats you can pin in Slack or how many like, you know, the search is good, but it's not like magical that it will tell you exactly what you're looking for. And so you

You

can also take different sources and you can use that as internal knowledge base generator as well. And then we've been able to use it for some internal things as well, before someone would, again, would have had to take the paints to summarize the whole thing and then put it in a form that other people could use. Yep.

Shimin (56:39)
Right. ⁓

And you like how much data they programming do you do these days?

Rahul Yadav (56:46)
Not much. ends up being these internal tools that I could build to like, we did this for documentation. There are some other tools that I built for our support team, other like internal tools to be able to like pull data and everything. And so,

That's what I end up spending my time on. like, you know, it's either that or doing some crazy production to be able to look up some stuff that we don't have like any UI layer or anything built out for. So that's what I end up spending my time on ⁓ usually these days. Yeah, so good.

Shimin (57:32)
Yeah, think this

is a great showcase for how Vibe coding allows a lot of roles in the organization, the PMs, the designers, to get back into programming or getting into programming for the first time. It really opens up the... It reduces the friction so much that you get to...

Rahul Yadav (57:48)
Yep.

Shimin (57:54)
create tools and new workflows for things that that's like always been so far out of reach that it doesn't even make it onto the maybe someday list because that is just like all the question. Yeah.

Rahul Yadav (58:05)
Yeah, I agree.

Yeah, and I was, I think this was like an AI engineer video where they were talking about

You know, the traditional model of building product where you like have your PRD, you plan everything out, you create like prototypes and everything. You do, you iteratively build things and everything. And how that's changing with these agents is.

Now, before it was like, I forget the term they use, but like you plan everything and you like, you know, tell me the story or anything. And now it's very much like, show me how it show me the prototype, you can do these things so much faster that instead of like spending a lot of time, you know, writing out every single thing that it needs to do and all these different things. And then like,

spending weeks on all sorts of different versions and everything iterate quickly and like you know picture paints a thousand words so like a working application is giving you worth a million words of something that you would have done otherwise and so like you said the people talk about like agency a lot

And to a certain extent, it now very much is the overcoming of our own barriers that we set for ourselves. like these things are not as hard anymore. And yes, they used to be hard, you know, but now a lot of the barriers that we're putting up are of our own creation, especially when

if you're creating internal tools, if you're creating like throwaway prototypes or anything, it's perfectly fine to be able to use these things. And if people are not doing that, that's not a technological bottleneck. It's you have to work on like mental bottlenecks on why that might not be happening.

Shimin (1:00:01)
Yeah, it almost sounds like, you know, what agile in quotes, but the agile manifesto version of agile is meant to be quick iterative with stakeholders and daily feedback. So, ⁓ yeah, I think a blessing for the industry, really. ⁓ Well, thank you for sharing that experience. ⁓ Let's get to our favorite segment.

Rahul Yadav (1:00:04)
Hmm?

Yep.

Yep.

Yeah.

Yeah, absolutely.

Shimin (1:00:27)
It used to be dance favorite segment, but I also like it. Two minutes to midnight, where we have a conversation about where we are in the AI bubble cycle to borrow an analogy from the nuclear clock during the Cold War. so we were two weeks ago, we were at a minute and 30.

Rahul Yadav (1:00:31)
Hahaha

Shimin (1:00:50)
And midnight is when the bubble bursts, of course. And we were at a minute and 30. That was actually an optimistic note for the end of the year. And we have two articles this week, one from the register called AI Faces Closing Time at the Cash Buffet,

where it talks about how the tech industry is burning through essentially one and a half trillion dollars on AI. And that is more than the cost of the ⁓ war in Iraq and Afghanistan, or it's around the same spending.

And they are starting to get pullbacks from corporations.

so here's an I quote, notoriously, do our economists with Apollo global management, trust and slogs setting up tober that there is essentially no growth in corporate capital spending quote outside of AI. While other economists have said AI investments are the only thing that is keeping the US out of a recession.

Rahul Yadav (1:01:54)
This goes to, by the way, Dan Wing, he was doing, I think it was, that's what I was listening to. His 2025 letter, think, either there or one of his podcasts that he's done about the book, this paragraph right there of, you know, the AI spending is what keeping,

us the US out of a recession. That was something that he was talking about as well is, do you really want to be a country that is monomaniacally focused on one thing? Or do you want to actually do like push the boundaries on a lot of things and you want to have like, this is one of the things that we should be doing, but there's a lot of other things that we should be doing.

There's this smaller scale version of this as well where Chicago, think, is the most diversified.

economy, the city economy, because only like 13 % or something, it was one of the larger industries, but it has like, you know, between universities and between all the different industries and everything, there's it doesn't have all its eggs in one basket. Versus we all, you know, talk about Detroit, and you see this with like other cities as well. Or if you have the one thing and the one thing is

not hot for a while then you suffer a lot as the know the people whose identity was tied to that one thing and so there is that's this reminds me of like the is it we shouldn't diversify too much maybe I guess you know as Charlie Munger used to say but maybe a little bit is not bad

Shimin (1:03:37)
Well, if AGI is around the corner, it's not bad. But this article also says that 25 % of survey enterprises are delaying AI spending into 2027. So is this potentially the turning point where companies are going to pull back because there hasn't been any fundamental shifts that is AI other than AI spending, I suppose? Of course, companies that

Rahul Yadav (1:03:39)
Hahaha!

Shimin (1:04:04)
completely rail on AI like yours is what be the exception here. But if we do start seeing enterprise, existing enterprise customers are pulling back on AI spending, then we might be in for a rough time, so to speak. ⁓ Yeah. And the second article we have here is from a New York Times titled as AI companies borrow billions, debt investors grow weary. And this one is about how some

Rahul Yadav (1:04:16)
Yep.

Shimin (1:04:29)
data center builders, especially the case they talked about here is applied digital. The company had to pay as much as 3.75 % above similarly rated companies because they are a data center company that services, I believe, CoreWeave, which then sells the compute capacity to the rest of the fan companies.

Rahul Yadav (1:04:51)
Mm-hmm.

Shimin (1:04:53)
⁓ It seems like the stock market is still melting up, but the bond investors are not happy with the amount of construction risk that these data center construction companies are ⁓ asking for. In this case, Applied Digital received a double B rating when it sold 2 billion worth of debt and

Double B is not terrible, but it's not great. It's definitely not triple A. And I think a lot of investors, especially debt investors are only looking at the downside of the debts not being paid back rather than the upside because they don't get anything if the data center does extremely well. So I personally don't think this is super controversial. Maybe it's a little...

Rahul Yadav (1:05:32)
Yeah.

Yep.

Shimin (1:05:43)
lower than I expected, with all the bubble talk in the air and considering that the debt investors don't get to partake in the upside, ⁓ I think this makes sense. And not necessarily a sign that everything is about to collapse.

Rahul Yadav (1:05:56)
Yeah, there's I read this book, I think it came out last year about tech bubbles versus financial bubbles. I think, you know, I don't see whenever I read these talks about bubble versus not bubble, I don't see it being referenced directly. But I get the sense that

these like anyone who's talking about that has read the book or, you know, read a review of the book or whatever. The book is Boom by Bern Hobart and Tobias Huber. And what they talk about is like, you get the technological bubbles they go through. Like the Manhattan Project was a bubble, you know, we talked about all the broadband that got laid.

train lines that relate and everything. All of these are bubbles. And they do in the short term cause chaos and people lose their jobs. In the long term, they cause prosperity versus financial bubbles where there's no like, the underlying world hasn't changed, right? So like the housing bubble is one of the examples they give where like the house is not going to produce

magically a baby house or something if you invest more in it. And so the concept makes sense to me. And so whenever I look at the, you know, who's worried about the bubble and who's not worried about the bubble, one of the things that I feel like

The big tech companies are not worried about the bubble because they are big tech companies and they are critical enough. Even in a bust.

we will still be using Amazon and its products. We will still be using Google and its products. People who are on social media would still be using one or more of Facebook's products and everything. And people still be playing video games and stuff, even if you're not trading models. so like self-driving cars and video GPUs would still be doing well and all that. And so the reason why I bring that up is

The person concerned about the bubble, are they, the big tech companies I don't think are concerned about the bubble because yes, things would be bad in the short term, but would be fine in the long term. And they'll be able to like create much more value, capture much more of the market if they actually are able to build all these things out now. know, bubble or not, I think they're gonna.

keep pushing for it ⁓ as much as they can because down the road is what they're looking at versus obviously like people who invest in the market you don't want to pay 100 bucks for something and it goes down to 20 bucks tomorrow if that's where you know how you're looking to grow your route or something those are the things that where the concern is coming from and it's valid and so

It has been a good framework to look at these things and why I at least yet don't get any sense of from the big tech companies of like we're a bubble. And even if we are, don't think they're gonna be saying that because I think they see this as a technological bubble and they see this as a fundamentally good thing versus financial bubble where, you know, nothing.

good happens for most of the people unless your job is to be on Wall Street and then you still make a killing.

Shimin (1:09:27)
I agree with you that boom is a good book, although I'm only 25 % of the way in and that the future of AI is bright. Otherwise, why are we doing this show? I do think that in the short run, if you have, and again, none of this is financial advice. We're just talking crap about the AI bubble.

And it is purely a financial bubble. I looked at Tesla's PE today and it is 300. So, you know, I mean, I haven't checked the videos in a second, but I think Tesla is purely running on AI and robotics on that high to reach that 300 PE. So in that sense, I do think as far as my 401k and my stock portfolio is concerned,

I do care that potentially there is a, well not potentially, I do believe there is a bubble. Like there is the cable network bubble in the 2000s. the 10 years on bolish, two years? Maybe not so much.

Rahul Yadav (1:10:15)
Yeah.

Yeah.

Yep. Yep.

Yeah, and part of it is also this is more just like people financially smarter than we would know better with like if tech keeps growing and more and more of the S &P 500 is concentrated in tech and

lot of people put their retirement funds or whatever in S &P 500 and tech is reliant on AI, then the cost for concern and so being much more because then the direction of AI and your personal finances are tied much more closely versus if you, you know, invest in different types of portfolios or something. Part of the like tricky part is AI is not like a

vertical slice is going to cut across everything and so you know you'll have to figure out what non-tech means to protect yourself from AI and whatever. Yeah, yeah.

Shimin (1:11:39)
Yeah.

Yeah. Again, not financial advice, Do you think we've moved closer to the bubble bursting purely in terms of the financial stock market sense?

Rahul Yadav (1:11:50)
Don't watch it enough. I'll stick with your minute 30 seconds.

Shimin (1:11:53)
Alright,

a minute 30. We can't deal with a minute 30. We might just stick to...

Rahul Yadav (1:11:55)
Happy New Year! We'll start

it positively.

Shimin (1:12:00)
We might stay at minute 30 until Dan comes back and come up with some Doomer takes. see. Well, minute 30 it is. And that is the show, folks. Well, thank you for joining us again for our study session this week. If you like the show, if you learned something new, please share the show with a friend. You can also leave us a review on Apple Podcasts or Spotify. It helps people discover the show and we really appreciate it.

Rahul Yadav (1:12:03)
Yeah.

Shimin (1:12:25)
If you have a segment idea, a question for us or a topic you want us to dive deep into, shoot us an email at humans at adipod.ai. We love to hear from you. You can find the full show notes, transcripts and everything else mentioned today at www.adipod.ai. Thanks again for listening and we will catch you on next week's episode. Maybe.

Orho, do you have any final words?

Rahul Yadav (1:12:48)
Glad to be here. Thanks for having me on. Appreciate it.

</details>
