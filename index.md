All opinions I share here are my opinions, I don't mean any harm and my main interest is to vent out and well, share whatever is going on with my day to day, so yes, eventually I contradict myself. This is far cheaper than therapy so bear with me.

### About me

I have been a computer systems engineer for the past two decades. I have some knowledge in things like Operating Systems Administration, Software Development, Infrastructure Engineering and Site Reliability. All those catchy terms just mean I can deal with computers at a large number (I can also play with raspberries), write code to run them and understand what it takes to keep them running for more than a day.
I have worked in the financial world, consulting, gaming and recently in the internet industry. I like to meet people although I am not the most extrovert and I like to spend time learning about things related to technology and the industries I work with. I enjoy mentoring, but I am more of a jack of all trades so I end up learning more from others.

I have been lucky enough to have an education at many levels in many countries and continued that streak with my professional life.

I may come back here from time to time and speak of things I have in my mind. I rarely contribute to any other social media platforms, I like to be the only loon in my feed, so yeah that's it.

---

### Operations at large scale are complicated, culture is almost impossible (02/25)

I wish I could open this entry with a better piece, than telling how I have changed jobs twice in the past few months, but that quite helped me get into the mood for writing this after all. Throughout this journey I have noticed a big gap between big tech companies and the rest. Have I chosen wrong? Not sure, I learned a few things: changing jobs is a 2 way door, relocating, not so much.

Now, I must add a disclaimer here: I have only made it into one of those big tech places in my life; I could not complete my onsite with Google, I never made it past screening at Meta, and I hated the only time I dared to start a process with Netflix.
Still I think, since these companies share some of their DNA considering people working for them move back and forth in between them, there is something that sets them apart from the rest other than the massive talent pool and revenue they generate: the culture they build around their infra is far beyond their competitors.

I know that talking (only) from the LinkedIn perspective only is terribly limited, yet I dare to say that even when the tooling was dated (and after 2022, terribly faulty), their processes were far ahead of other small businesses I have worked with. And probably that's one of the many things that sets them apart. They focus on what matters and make sure to keep it well greased.

Most places, small, large, startups and so on rely on what's the norm: chats, review cycles, stand ups, a ton of tooling and a devops-culture; this is nothing outstanding. Big tech folks have other aces up their sleeves, even when they are large, fat and slow compared to startups: They have continuous reviews, a mature/sophisticated incident response process and culture and tooling that makes sure things are not being overlooked. They will be overlooked for sure, we are humans with the attention span of a mayfly life span, but you really can't blame the tools there.

Now that I started the journey in a second place I notice kind of the same missing pieces as I did in the first one (at least after my adventure in Silicon Valley), they are lagging and don't see the relevance these processes have into getting them started with more sophisticated ways to work. Again, I think it is not the tooling. My former (short lived tenure) place had an amazing set of tools to get things done. They drank the Kubernetes and CNCF kool-aid hard. And they did it terribly well. Yet they sucked at the most basic operational tasks: catching issues, remediation, having a blameless culture and having the means to fix shit fast. Automation seems to be the Achilles heel of many.

 They were by no means mediocre engineers, they moved amazingly fast when rolling out projects. I think where they ran dry, was drinking the site up and site reliability (again) kool-aids. Now this is not preaching how good SRE is and how good it can be for most organizations. I think the term is overhyped and misapplied in most places. I think this is more of a site engineering culture that actually cares about two things: making things easy to use and making issues easy to fix. Well, turns out making things easy is terribly hard and it demands resources, tons of them and once you get there, moving your ops to India, Mexico or any developing place, well, it is like kicking the Jenga tower, because operations can be ported, culture can't, like a good brew, it needs the right ingredients, the right temperature, the right timing.

So yeah, besides all the fad, bloat, hate, overpay and frustration these places had before magic faded, they changed things to such an extent that even today where they are the eroded shells, it is still damn hard to catch up with what they built.

Oh and those shells are going to be back in the game, I'm more than sure that the industry is reinventing itself and I am eager to see where this is all headed once the turmoil subsides.

### Zeitgeist (01/25)

In the Zeitgeist of what seems to be a recurrent scenario where nobody wins, I browse eagerly through the news to figure out what's the next big deal. This week's big deal is China doing things the way it should be. A breakthrough with restricted resources, odds against, we ignore the big picture here: no meaningful paper being published the past decade has no Chinese authors in it. It's like Silicon Valley is oblivious to what the reality is and they race towards a doomsday of unplanned consequences. How good would AGI be when you have no means to give people a livelihood? I think from all scenarios China seems to be the best prepared nation to come up and trump over the rest in this race. I am not praising it though. I don't think this AI race should continue without a common end that is not profit, I think that's where America got all wrong and where at least their counterpart has a best chance of not starving their population by capturing that holy grail.

In the wake of the non-stopping round of layoffs, I cannot stop here just cheering for DeepSeek achievements. I think we need to come to a realization: Things won't go back to where they were before 2020 started. The race of AI is just a tipping point on something that is kind of non sustainable fueled by greed.

It is hard to argue that products of many large companies are not getting worse. Development is getting worse. Operations are getting worse. I think this is no surprise to anyone thinking this through. Executives want to please shareholders, and shareholders sustained their expectations past a blip of what world economies became when a pandemic hit. To make things slightly more interesting, GAI came into the scene with hunger for resources, so capex surged not only through the added load that Covid brought, but because AI demands power. Why the worsening then? These are multi-billion dollar businesses after all, right? Well, these places are massive in all extents of the word, **including their brand**, so they can afford to lose quality without being hit, after all, they started shipping their shiny models fueling their AI (a shitty one). Cutting corners in engineering costs is a no brainer for these guys (In the words of a recruiter when I asked why Mexico: "It is cheaper to get an engineer in Mexico than in California, you don't have to pay..."), they don't care about social impact, they just want to cut costs, so moving things to other regions seemed fair to them. There is little concern on the "you get what you pay for" motto, there is little concern for anything that is not pushing the operational costs down; keeping the lights on while the new guys catch up seems sufficient, inventive? We have AI for that!

I should stay shut and be happy for that then? I am on the winning side, right? Not at all, the winning side has a terrible working culture, terrible work conditions (like they cared), a very inefficient government (grease money for e v e r y f u c k i n g t h i n g), weak, almost laughable law enforcement, shitty infrastructure (really, forget about HD zoom calls), a different focus on what quality means, zero regard for accountability, and the list of problems can go on; we have more jobs, but the quality of life isn't really improved for anyone here and the problems we learned to solve (not to say how to solve them) are of a different scale, so when these behemoths land on our hands, we cannot but spill the beans (pun intended). It seems that as long as the model is running, that's not a top priority. So while this keeps going (and it will keep going) some folks struggle to hold on their bet of a multimillion valued dump and their H1B shackles, some folks rush into collecting badges so they can add FAANG, MAANG or whatever shit it's now to their resume, while others just cash those big fat bonuses to keep those Big Sur bunkers well supplied.

Anyway, the market is and will remain a tide of non-sense as it has been for the past lustrum. I expect nothing, but more of the same: Layoffs, a desperate fight to reduce capex and improve revenue; so go on big tech, keep sending us your jobs down here.


### (public) Cloud computing fucking sucks (01/25)

I could as well say people fucking suck, most of the issues from cloud computing come from the people running and using them after all. I'm ranting here because it is so damn common to see leaks coming from people who otherwise would have a room with a couple of racks gathering dust with old ass systems that just work when nobody comes with a great idea, except that, according to some C level jerk, the neckbeard maintaining those solid boxes is too expensive and all the people at the golf course talk about how amazing is to use Amazon cloud for their operations... then, the nightmare starts.

I come to ask myself how could we trust our infra to the most toxic company culture in the globe, that by itself is mind blowing, but on and on, the cloud is just a cake of layers trying to emulate computers. Don't get me wrong, it is fantastic that you can borrow resources at will, only what you need, leave the rest, but there are hidden costs of thinking this actually gets us somewhere safe. Credentials leak all the time. Workflows fail all the time. Groups scale out of control. Costs scale out of control. Yes, there's a human behind all that stupidity, but when putting all together, was leaving the old Dell blade running that bad? 

We are sold that we need to be ready to scale, hell, I have been an SRE for half a decade and I totally buy it, but not every business is the next Google, so why design thinking you will ever meet that workload is beyond my comprehension.
Am I just yelling at a cloud? You bet! Distributed computing is fucking awesome. Compute on demand is fucking awesome. Orchestration and provisioning automation is fucking awesome. Those concepts are huge, we would have no large data analysis without them, we would have no GAI (and LLMs) without them and many of us would not even have a job without them. As concepts they are magnificent, but the Devil is in the details, right? You get a bunch of people building layers on top of layers and you end up with an obnoxious cake of complexity solving a smaller problem than the one it created by just existing. Not to mention how hard is to even get your hands on some decent hardware nowadays (good luck getting some Blackwell orders fulfilled). This is not great, especially for companies with zero innovation who will just use and pay the bills. Those poor bastards are the same who will leak a token into a Gitlab public account and get all their customers PII data leaked into the dark web or a stupid 4chan room (wink, wink). Guess what, settlements are fucking expensive. Ransom is fucking expensive. Changing your SSN is fucking expensive (in time). But well, this is our reality today and we learn to cope with it as we lay our hopes into ChatGPT giving us the fix to our last typo that caused a bill of ten quadrillions on unused API Gateway calls to 127.0.0.1


### Moving to RSS (01/25)

This sounds like something one would do in the early 2000's, but I think that after the first quarter of the century has passed, it is only sane to stop using any kind of social media and well, this change kinda fulfills my needs. I tried to become active starting this year in the only network I used (LinkedIn), but even if I loved being part of the company, I don't love the product, so I am ditching it. This would be just another post of people fleeing away from different platforms into "safe spaces", but I think I don't care about those ideas, social media was meant to bring you close to the people that once were part of your life, however it is not strange that I find myself in a room full of relatives staring at different screens at the same time, talking to no one, and I just think that these sites just keep making worse and worse the internet for everyone, so it is time to get away.

It is a no brainer that these algorithms used for "relevance" are just means to "amplify" what's controversial for the sake of "engagement", these are just fancy terms for giving more room to content that will block time and attention from the users, but rarely this is a healthy kind of content; controversial more often than not are comments and scenarios that are not realistic and tend to harm your mental well being, just like pornography. I don't want to be part of it, not even as a user, thus, I am going back to when the internet was exciting.

### Onboarding is underestimated (01/25)

After watching the NVIDIA CES keynote a couple of days ago, many ideas resonated with me. However, one in particular stood out as challenging: onboarding agents as a key process. The reason I am writing this post is that I believe we often overlook how important good onboarding is. I have a few stories, some of success and many of horror, and they all begin, well, at the start. Whether it’s joining a new team, entering a new organization, or taking on a new responsibility, the process of transferring knowledge is an art that, especially in engineering, few have mastered. This is often because it’s perceived that there are more pressing things to do.

Onboarding is no simple task; it requires dedication. It’s easy to think that writing a checklist and passing it on to the newcomer will suffice. In reality, this approach dismisses the unique circumstances surrounding the newcomer and makes assumptions that might be wrong. It was only recently that I realized one of the best things that happened in my career was starting in a place where most people were not only good at their jobs but also great mentors. Conversely, every single time I failed to catch up or decided to pursue a different path, it was triggered by the perception that there was no investment in helping me start. By “investment,” I mean time and will.

I also like to think that my best contribution to my former job at LinkedIn was helping engineers, regardless of their position, get up to speed. It demanded a significant toll on my time and ability to deliver other projects, but I regret nothing. The people I onboarded have seen their careers thrive (or at least not obstructed by the lack of awareness) to this day, and that makes me believe every minute invested was worth it.

Onboarding and mentoring overall are not simple. You may know many things or quite a few, but the real challenge lies in understanding where to start with the person you’re bringing in. Too often, I’ve been in situations where the person tasked with onboarding me approached the task with the same level of commitment as any other item on their to-do list. The result was poor not only for me as the one being onboarded but also for the organization. Having a new person join and contribute from the start would be fantastic, but that requires another person to step away from their tasks to prioritize knowledge transfer and training. Unfortunately, not many engineers or managers are willing to make that sacrifice.

As AI takes over many key positions, I believe the approach to onboarding will need to change. After all, a well-trained model is a productive model. Passing on knowledge will become a paramount activity for many organizations, and it’s about time. The investment in time and effort always pays off.

### Saving my SDs using tmpfs (01/25)

I won't delve here into tmpfs because I don't know where it started beyond what [wikipedia](https://en.wikipedia.org/wiki/Tmpfs) has. However, if you ever worked with a raspberry, you know SD card lifetime is limited and I come to find that tmpfs has been a time and money saver since I minimized the writing to my storage by using it. Yet as you may expect, this is ephemeral (since it is saving data into a block in the RAM) so yes, this has two drawbacks actually, you lose memory for the sake of having a temporary place to write. Is it worth it? IMO yes. Any permanent (and important) storage I have deferred to external drives, but external drives are slow. Things like logs, go to the tmpfs for sure.

So how easy is to get this going?

Actually it is pretty simple. To the extent to say it comes out of the box, so pretty much all I needed is:
1. Add the entry to my `/etc/fstab` file`
2. Add the dirs (this is a minor ache) that need services like nginx back to the filesystem in order not to have startup failure upon restart; file: `/etc/tmpfiles.d/var.conf`

The entries of each file are quite simple:
```
# fstab
# in this case, we specify we mount /var/log as tmpfs with 400MB size
tmpfs  /var/log  tmpfs  defaults,noatime,nosuid,nodev,mode=0755,size=400M  0  0

# var.conf <- this would go for any filesystem that actually is mounted
# in this case, we specify we want a dir for nginx with owner www-data in the path
d /var/log/nginx 0755 www-data www-data -
```

And just like that, I have kept my SD cards alive for close to two years. Probably with a v.5 this is not needed if you just use a NVMe, but that's not a cheap option when dealing with more than one board.

### On frameworks and languages... and AI (12/24)

Yes, this is one more of those posts. I was just exploring the whatabouts of FastAPI. I was interested in how hard or how easy it is to get it to work compared to Flask or Django 🤮
I find that it is super easy to get it working and I really liked it, but to be fair, it still brings a bunch of dependencies that a language like Go just natively has (Go's tooling is sleek). And that brought me to the questioning on why are frameworks proliferating at all? Not long ago I spent some time reading about the need to push back on things like React and come to believe that if JavaScript had offered a bunch of much needed functionality like async calls, a lot of these framework nightmares would simply not exist. Yes, JavaScript is a terrible example, but thinking about Java, well, it is not very different, and possibly the list just goes on because, well, if the language is complete, and getting things done does not require an obscene amount of code, do you really need the framework?

I don't have many friends I can bring on the conversation and ended up asking ChatGPT about this and well, it started using a lot the term "overengineering" which brought the conversation from Frameworks and language feature completeness to more weird concepts like cloud native applications and to even harder topics like accountability and why engineering is a very condescending word in a world of do as you go.

Anyway FastAPI is nice, but old me thinks Golang is nicer, even when it has some weird traits.

### Beware on what you learn... and what you skip learning (12/24)

So I just came back from a two week trip. That means, it is time for me to shake up the rust. Well, not only I like to do that on my coding skills, but the design ones. I like putting about an hour daily to go through blogs or lately videos on design mocks and well, I found a full playlist with those and oh boy, some are so flawed that I just feel bad for those taking notes from them. I criticize without having a better recipe, yet I think there are some fundamentals you cannot just toss away and hope for a good result, e.g. if you design an API, you want to follow REST principles so your API is not your weakest link. Same I could say for caching or other buffering solutions, they are mentioned but never brought into consideration on what could be their caveats or simply their strategies.
I used to think NALSD was the coolest thing ever in a design interview, but surely, it is not a single thing, it's the collection of all parts that makes the task not only enjoyable, but worth exercising. So if I had to write a list on things you need to pay attention to provide good solutions I would be keen on using what you understand well and only add up new pieces where you know bottlenecks usually are, this sounds kind of counterintuitive in a world where big tech tells you their shit is a panacea, but a cake of layers rarely makes things better and -true story- they are experts in making cakes.

Moving on; since I am not fully occupied at the moment, I thought it was a good time to actually learn a new skill that I indefinitely postponed like: a mobile application. My idea was simple: a localization app that can give me useful data (for a traveler), location (coordinates and nearby address), weather and time. Nothing fancy, text would work. I downloaded Android studio and started writing something (with the help of tutorials and AI, since I had zero idea on how to set up a project, let alone write Kotlin). Well, my project was ready to be tested except I was missing API keys. And well, in a distant decade ago, I would just need to generate my key using my Google account. Sadly those days are gone. I was welcomed with the GCP mess of a landing page where the first thing I needed to add was my fiscal information and a credit card. **Hell no!**

So I wrapped my project, hit `rm -rf MyWeatherApp` and came in here to rant about how bad things are where all content is social, all infra is rented, all projects are a layered mess of YAMLs and XMLs, all services are (public) cloud hosted and even all useful advice is subscription restricted. Yes, I advocate for a system where you pay for what you use, yet I cannot just put out $20 bucks on every step I take and get nowhere. I start to fear that productivity is for sale under this weird world that big tech crafted for us. It saddens me because it resembles the reality I live beyond this screen where a mob and a caste of parasitic politicians extort you by forcing you to pay protection money so you just can make a living.

I would argue that open-source would be a valid alternative, and it is to some extent, but eventually we hit the spot where we need to use something Google authored and I guess my frustration here is how much worse things are thanks to G and friends. 

My small victory from all this wiggling is that ChatGPT is terrible, as usual, writing a good solution so it forces me to at the very least troubleshoot what it suggests. So at the end of the exercise, I learned something.


### Why ChatGPT is (for now) my best pair programming amigo (11/24)

Using ChatGPT to code is like shooting at your own feet, except that IMO, it has been the best companion ever. I would guess co-pilot would be fairly efficient, but I am budget restricted to try it. Anyway, I find the capacity of bouncing ideas with the GAI a big up that if handled with care can boost productivity.
Unlike using stackoverflow, which I despise, ChatGPT will lay the mines right under your feet. They will blow before you ship, which is a good thing to find out. If you are careful enough with what you ask for, with reading what you got served and with being critical to the response, probably you can get better code. Not saying it is easy though, GPT is terribly bad at getting good and consistent unit tests, however it is brilliant at providing useful mocks so that's a big tradeoff.
So what am I suggesting here? Should you replace all your tools for using ChatGPT? Nah, but there are a few you for sure will want to get rid off: Google being the first one. If you can search through your prompt (hey, hey! just don't trust everything it says!), the only other thing you need is access to github (GPT is not actual and deprecated and bad code may be replied). So having the changelog, API descriptions and a peer that reviews your ideas is like a powerful trifecta, that in my case, has helped me ship at least 5 projects in less than a couple months. Am I grateful for it? You bet! Am I afraid it will replace me? Nah, it will get better when it can handle context and when that happens, I will be grateful for the transition 🤖💙
I truly believe that it is a good mentor, but what's remarkable of all of this, is that if you pay close attention, you are setting the pace and you are reasoning with yourself, it is like looking into a warped mirror to get a fresh perspective of what you can actually do with a little more time and a better education.


### A small parenthesis on capacity (09/24)

I will start this one by posting a term I forgot to mention in a recent conversation: **load testing**

Capacity planning is a very interesting discussion; it requires knowing where you're standing and where you're going. I just had a conversation where we discussed vertical vs. horizontal scaling. But the conversation can only start when you know where you are standing and for that understanding to happen, you need to know what are your current limits (limits are good, this is one of the most important lessons I have ever learned in my career), that's where load testing comes into play. Yes, you will add buffering in different layers to disperse the load and you will break the problem you try to solve to improve your ability to scale, but that is step number two.

### My two cents on "coding" interviews (07/24)

Yes I am one of those guys. I see no benefit to them other than stress the shit out of a person to no good end. I would say I am the same as happy doing these interviews as I am creating a 1 machine cluster using kubernetes. Two of the most enjoyable interview processes I had (and memorable since they really demanded more skills than memorizing algorithms or snooping over the answers tab) were with Klarna and Wizeline; Klarna asked me not only to provide complex functions but to actually write a service to query those functions and emit metrics for them (2 days given for the task) and Wizeline asked me to write a function in a language they invented so they could evaluate my ability to learn and work with what I learned (no guy on the other side of the terminal). I wish I could mention Apple, Amazon, Netflix, Google, Microsoft of Meta here, but nope, they all do the same silly handshake, so I dare to say that I don't see this inventive anywhere in big tech, I know, the process was created to pick the brightest, but just as with immigration, it is gamed and not fun at all. So this is the hill I choose to die on: leetcode is crap, I will always push back on it. Not saying puzzles are crap, they are not, they are fun and educational, but using them as the first step to filter out the competence of a candidate is silly, just like certifications.


### Is my connection the issue? (07/24)

Recently I got this as feedback from an interview: _"Your internet connection seems poor"_. I was concerned about it since I want to work remotely when the chance is there without driving my family crazy by hogging the network. I knew I had 150 symmetric Mbps, so what's wrong then? Well, I had no clue, but I could start by monitoring and a quick search got me this neat python library: [speedtest-cli](https://github.com/sivel/speedtest-cli/wiki), so the nerd in me took the chance to write a prometheus sensor and poll the metric constantly. I wrote a non-prod-ready **[gist](https://gist.githubusercontent.com/mon-gmx/8b70cc44a4bf37c0015db1000fb83abc/raw/24ab84640b7c25dc11d002b9940f59f6a8ce7dae/speed_test_sensors.py)** for that matter that paired to a systemd service got me monitoring my internet speed in no time. Now to what matters: it is not my connection the one that sucks, yes, it is slow by today's standards, but never degraded below the 90Mbps in any direction, and that's why data trumps everything and why observability is a must whenever dealing with problems where the root cause is not so evident. Will I dig further here? Hell yes, I have `iperf` measuring different latencies between different antennas (my network is simple: `modem -> router -> repeaters (mesh) -> computers`).

![image](https://github.com/user-attachments/assets/cf43a151-92e6-4a1b-9288-5a0eeb6b94d1)

### Simplicity is king in my world (02/24)

In the gist of many things going on lately around my own life I come close in contact with a lot of complaints about how things keep degrading in quality and surging in price and I keep reaching over and over again to the same conclusion: simple was, is and will always be better. Focusing on shells full of gimmicks tends to always have the same outcome yet we often just don't get it. I usually am triggered by buzzwords like _slice and dice_ or _democratize_ but I come to really sympathize with this one: _enshitification_.

I like my code with zero boilerplate, my internet with zero quotas, my services with zero subscriptions and the list goes on. I am not against progress, progress is good, that's why cars are safer and phones are faster, yet this decade all we get are flashy pinatas solving no problem, but the problem created to keep the greedy appeased. I never realized how much I miss what is simple and reliable. Screw those flashy trims and non-sense all glued together gadgets, let's go back to simple, there's where beauty of crafting lies, that's where we have control.

<small> This site uses Google Analytics for the sole purpose of measuring visits </small>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-PW9NV6T54Q"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-PW9NV6T54Q');
</script>
