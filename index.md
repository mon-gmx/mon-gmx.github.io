All opinions I share here are my opinions, I don't mean any harm and my main interest is to vent out and well, share whatever is going on with my day to day, so yes, eventually I contradict myself.

<!--
<div align="right">
  <small>
    <i>If you're still reading, my title is not misrendering and your visit is a datapoint in GA4, I promise that's all I collect.</i>
  </small>
</div>
-->

---

### Accountability is not coming soon enough to technology (06/25)

>"You know what's wrong with scientific power?... It's a form of inherited wealth... Most kinds of power require a substantial sacrifice by whoever wants the power. There is an apprenticeship, a discipline lasting many years. Whatever kind of power you want. President of the company. Black belt in karate. Spiritual Guru. Whatever it is you seek, you have to put in the time, the practice, the effort. You must give up a lot to get it. It has to be very important to you. And once you have attained it, it is your power. It can't be given away: it resides in you. It is literally the result of your discipline. Now, what is interesting about this process is that, by the time someone has acquired the ability to his with his bare hands, he has also matured to the point where he won't use it unwisely. So that kind of power has a built-in control. The discipline of the getting the power changes you so that you won't abuse it. But scientific power is like inherited wealth: attained without discipline. You read what others have done, and you take the next step... There is no discipline... no mastery: old scientists are ignored. There is no humility before nature... A karate master does not kill people with his bare hands. He does not lose his temper and kill his wife. The person who kills is the person who has no discipline, no restraint, and who has purchased his power in the form of a Saturday night special. And that is the kind of power that science fosters, and permits.”

<sub>Michael Crichton</sub>

From all the things I had in mind for this post, one that got me scratching my head is, if there are any advances in controlling what is being released into the wild now that LLMs have gained traction and who's responsible for that.

It is no wonder that unlike other sectors like the financial, healthcare, construction, energy or aviation, IT has gotten away with a lot for quite a long time. We could argue that the impact IT has on the lives of most people is less immediate yet we have given it power to influence (and even decide) what we read, what we purchase, where we eat, where we vacation, how we send our money and even who we elect within our government. IT has shaped our lives greatly at the will of few, even if we attribute it a greater good like access to information at a speed and scale like we have never seen.

Early in my career I was fortunate enough to work for my central bank within the payment systems area. I think it never clicked to many of us, but we had within our hands an enormous responsibility. Our systems were in charge of moving payments for our population, it would be no big deal until you figure out that those payments can be many relevant things for people, paying a bail, paying rent, paying the hospital bill, paying for your meds, you get the idea, if money was not there in time, we would affect your life in a negative way, this was no small responsibility, but I come to believe not many of us were actually keeping that upfront whenever we changed a line of code, all we wanted to do was ship and meet deadlines; we took no oath, we signed no code, we just followed the path our director traced and moved on.

I think this "move fast" mindset is not really happening in places like a central bank, yet many other important businesses are all in. Engineers, project managers, managers (I've seen some of these fuckers try to sweep their mess under the rug so often), everyone wants things done fast, they want that reward of being the one delivering something, making an impact; no pushback on that, I love crafting and getting things done, I write code every weekend for fun. I think however, in this line of work, oopsies are not seen as such a bad thing. Oopsies have created catastrophic failures of different dimensions: planes failing, payments failing, personal data breached and misused by _the Zuck_, life savings getting smoked, identities getting stolen, self-driving cars smashing pedestrians... Yet unlike a physician doing malpractice, going to court and losing their license, in IT all you get is a slap in the back of your hand and someone pulling hairs about how to get people even with "make goods".

In order to write a program and ship it to the world you need no license, nowadays you don't even need resources, all you need is acceptance and a good license agreement stating you are not responsible for anything. That's it, you created a ticking bomb that people are invited to bring home and use it like a toy. It was decades ago that this toy part was true. When personal computers started getting adoption, people coded for fun, they shared, they just wanted to experiment and show off their toys. Long gone are those days, people nowadays get into tech for the money, they don't care about the toys, they just care about that bonus, that equity, about their A/B testing getting them insight on how and when to serve those ads.

As AI enters the chat, this becomes an even harder problem to address. You coin a term, you create a model, you release it into the wild. Who is responsible for what your model built? OpenAI? Cursor? Microsoft? If what you build impacts people, will this be the guilt of the person who was "vibe coding" a product now that they need no "real" _engineers_? Is this something that Amazon will suck up if your model triggers a million dollars account? Is this something that falls into the gray area of the desperate efforts the European Union or the American congress is doing to address a problem their mummies sitting there can't even fathom? We are entering a very thorny path at a very scary speed, yet nobody seems to want to recognize that IT is broken and that yes, its entry barriers are low and they should stay that way to foster creativity, but it should also be clear that this get rich fast mindset continues costing us as at many levels that of course, nobody wants to admit, because admitting we are doing things wrong and that these new tools are the equivalent of toys coated in radium is letting China or whatever new enemy western society invents will win the race... Now I wonder, what race?

### Using LLMs to code (06/25)

Gotta start this post by saying that "vibe coding" is the ultimate level of stupidity. Yes, your prompt will generate code, yes, the code _might_ work, and yes, you might spare yourself a lot of time writing something that you can explain better. The caveat here is that the LLMs level of correctness is **superficial** and code, good code, solves a problem at different levels depending on the grade of expertise you have managing it.

You can claim that the flaws are in the prompt itself and that prompt engineering would fix that, but the "engineering" just means adjusting the perspective of a prompt (I'd prefer calling it a command) to change the way the model responds, however, addressing a complex task will not just follow because you cannot just drop a request expecting the design to address what different functional and non functional concerns will come across through experience; I come to believe that changing the way you get a response is not really changing the answer itself. I could think that code would evolve as those needs or concerns are dug up, but the code evolution is quite flawed if the approach turns out to be incorrect. What I've seen and experienced is that LLMs don't let go of a bad idea as easily as experts do.

So coding using LLMs is a bad idea? I think coding using LLMs can be **a great way to prototype and learn**, but it is not a good way to generate good quality software. I don't blame this on the LLM, I just ran an exercise where I used GPT to prototype a distributed caching system, which might be considered a complex task. The LLM went right away into suggesting features and writing code. I ended up with code that was working, however as I started going through the code, there were several parts that could be improved and corrected. That doesn't mean that the code itself was flawed, but it was not thought at all. Tasks like removing bottlenecks, distributing responsibilities, avoiding compute overheads, all those weren't thought of and you could see that even when the code ran, it would fail to scale or address corner cases. I can say the same about unit testing; the LLM focus is contextual, thus, the tests will lock into testing functionality rather than functions. This made it hard to follow the "unit tests" because they were not unitary.

I don't want to write this entry just to throw shit at LLMs. I think I wrote an entry last year stating that LLMs shine when we use them to reflect on our own ideas and the improvement from the last time I tried this is tangible, however this didn't save time for me or made me less prone to make mistakes, overall my efficiency was positively affected but the improvements are not in the ability to deliver code fast, but in the ability to deliver well thought code. I think the gains are where we spend less time doing research on how to implement a concept we already know or copy-paste-adjust snippets of code that might be flawed, the exhaustion from doing this is moved to a different stage of the development process, you notice the transfer of time when you do review the generated code and adjust it or simply provide feedback on it, which by itself is a gain for a person as a developer; providing useful and insightful feedback after all, is an expected quality of a seasoned developer. So probably that's where LLMs will accelerate our work, strengthening some of our skills providing us with exposure to tasks that otherwise would take years to gain access not to say credibility.

Am I heading anywhere with this post? Am I saying that vibe coding is a fad or a good practice? I think the answer to both statements is: Yes. The idea of using an LLM to deliver code that works and that it is going to work over time is an understatement of what good software engineering is and if you buy into this idea, you will pay the price and it is not a cheap one. Using generated code and later using the LLM to fix the code that potentially contains pitfalls is a gamble where your chances of losing are high, recent advances on LLMs allow it to access memory so the loss of context is not a great concern as it was a year ago, however, if you modify the code or ask the model to mutate it to improve the flaws you probably failed to detect, the result will be having two new bugs instead of one, just like with real life scenarios.

As any tool, using it responsibly and with measurement is a recipe for achieving a balanced result leaning towards the good quality end. I think these models are no replacement and will not be one just because the ability to mentally exercise and evaluate a result is something a model has not at its own disposal, the model will use contextual "reasoning" but will not break free from the context itself so it cannot do the switch between the task and the function alone, or simply figure out from experience, what might be a bad decision. The model however, will provide feedback on every design decision we make and recent versions propose good ideas taken from other projects, it will not generate new ideas, but it will have more information on similar work that we would not have immediate access otherwise, and that is where it can be **a powerful assist to our work**.

Overall I am not averse to using LLMs to assist us, I think prompt and extensive access to feedback and information is something we don't even get from our peers just because everyone is using their time to solve a problem they own. I despise the idea of saying that the crafting process is replaceable by a model, that is an idiotic and poorly thought out idea on how to use a tool that has proven to be the most powerful when used in a symbiotic manner, should we pursue making the model independent on the long term? I don't know, because I don't control the purpose of Generative AI, I see it as a tool to improve our intellect not as a replacement.

### Containers (06/25)

I have to start here by saying I am no expert in containers. I have been around to watch and participate in the transition from VMs to containers. I have used many and yet not enough of them. This entry is another one of my tiny ass cheat sheet entries by the way.

Anyway, my interest in virtualization and hypervisors dates a couple decades back. I started when vmware was the shit and back then I had no clue what to use it for. I recall having a client running in my budget machine and never delving into what I could do with it because my understanding of Linux was more than limited. Then I graduated college, started delving into Solaris and started hating to do all my work via putty so I ended up finding a way to use virtualbox and a USB to get a terminal and an IDE that actually felt comfortable rather than using notepad++ and putty to get things done. So back then all I understood about isolation were permissions and root privileges, never thought (or learned) about chroot and what a good tool it was to break apart an application path, so for sure cgroups were out of the map.

Then docker came along and it was pure magic, the idea of having an image where you could install, test and ship your code was very exciting, specially when most of my work was done by a playbook, so having a way to automate the build and a way to ship in a tested manner where no installation was required felt like a big time saver. But then one wonders, what is this container actually doing and why do I still use virtualbox anyway? That was a question it took me some time to answer. Articles and demos all mentioned something about borrowing what is part of the kernel, but never mentioned which parts. Well, that's where that explanation sucks because to be fair nothing is borrowed, in the simplest term, a container is just creating a partition within the OS resources to create isolation. Had this been told just like that the concept would be super simple to digest, but you know, people like to sound smart.

I think I never pulled apart from the abstraction docker created and what actually was going on underneath until I stumbled upon a place where containers were self managed! What? You don't use docker for that? It took no time to see docker falling out of fashion and kubernetes ramping up, still, the notion of what is being **used** from the OS itself was intriguing without understanding what is libvirt, what's LXC, what are namespaces and cgroups. So let's try to dig into those things, shall we?

I start with libvirt because it is a quite useful API to communicate the OS with different hypervisors, not to mention giving us tools for management of resources. This comes handy when we try to understand the concept of an orchestrator, although this might feel low level, the tooling and the API we have to work with hypervisors, including LXC is key for managing what the container platform creates. I don't think libvirt has much to do (if any) with containers, still it is worth mentioning, because part of the need for containers comes from the need to communicate to parts of the kernel through an API like this one.

Moving on to LXC and why using it paired with libvirt can be useful to get a similar functionality to Docker, we need to understand what the linux containers project actually is. LXC is not really what introduced the isolation it is going to work with, but it has a nice way to abstract it so we can focus on defining resources and types without delving into what components of the kernel itself is leveraging to provide isolation for an application. No wonder docker started building around it when it started. But trying to dig deeper, can we do our own container by hand?

Well, circling back to the "self managed" mention, yes: Isolation rather than virtualization (we should always make that distinction when we talk about containers) means we provide the means from the kernel itself for an application to run without any awareness of what runs outside its restricted space. How is that achieved? through a set of features from the kernel: capabilities, cgroups, namespaces, policies and filesystem isolation (chroot comes into play again).

But why or how does this work?

Let's think about an application that requires a certain set of libraries, directories, processes and calls to run. If we already have a kernel that provides its scheduler and syscalls, we don't really need to worry about that layer. If we however try to use PID 1 for this application and limit what runs on the OS to a given process, we need a way to let that application "_believe_" be the only one running. Using concepts like namespaces and cgroups that can be achieved, namespaces will _tag_ a set of resources to be used for a specific process and limit its view, what the process can see, to what namespaces has _tagged_ (in a OS structure point of view, this includes the PID tree, networking, ipc, hostname, user mapping and mounting points just to name some, depending on what you define using `unshare`) while cgroups will reserve and limit the resources that are provisioned to the process (you need `cgroup-tools` to get this working since you need a cgroup created using `cgcreate` and add resources using `cgset`). Is this enough to contain a process? To some extent it is, however the restriction is not limiting access to syscalls and other critical parts of the OS, thus, the use of capabilities and apparmor policies are needed not only to isolate a process, but to restrict it from operating beyond its own scope (we can see how this one works using `showpcaps` on a PID and set it using `capsh`).

So is Docker needed at all? What about kubernetes?

Well, docker, just like LXC abstracts and simplifies the operation with containers, just like libvirt and the docker daemon simplify the orchestration at host level. Why is this the first time I mention kubernetes? Because kubernetes is not really part of this orchestration, it lives and operates on a different layer, where groups of containers (or machines) are the abstracted resources so basically executing this same concept at a different scale of resources.

In my experience, all that is needed, all the "magic" is provided by the Linux kernel. We are sold this as a breakthrough but this magic has been around since 2002 and widely adopted in 2008. I have used "in-house crafted" versions of these orchestrators and containerization platforms, they worked and worked quite well. Am I suggesting not using docker or kubernetes? Not at all, these platforms are good, especially paired with cloud providers, however, they mean complexity just as using AWS means complexity managing resources through a non-standard API, yet they are great time savers, when done right, and a strong implementation of what these concepts propose on resource isolation.

Other parts I should mention?

Sure: UFS! Although not necessary, the union filesystem is a layered approach where space is managed with the intent to prevent copying and duplicating files across containers. This provides not only access to different filesystems through a unified view but it allows access to parts of the container like the image where files (read only) can be accessed by different containers, that's why it is a key part of docker, however, it is not an exclusive approach of a layered access FS for user spaces, LXC has its own implementation, however the key purpose of each is different.

And that's it, containers are all about local isolation. Hypervisors are a different animal, they implement their own microcode, drivers and access to resources so while they can run on top of another OS, their purpose is to provide an isolated platform for an OS itself. And this just took me years to understand and explain.

What do I use? Well I use what suits my needs, WSL2 for the time being.

### Emerging challenges (05/25)

I struggled on what to write about, mostly because I feel like revisiting a couple of recent events, but I think I can focus on what I'm closer to, thus, I chose my country's situation. Still I will try to touch the second option. I would like to say I am _outraged_ or _disappointed_, but I think the only feeling I have is helplessness from big tech and their “AI everywhere” narrative. Not that their products aren't shinier than ever, especially anything related to entertainment, they mean progress, it is just the direction this progress has taken and what it is costing to all of us what baffles me, not to mention the lack of novelty or the fact that they wrap a dangerous tool with a toy disguise; from my perspective, they are just focused on establishing a platform where they can keep pumping the idea, hoping for a breakthrough to actually come in some kind of serendipitous way. I'm skeptical at best that this is actually going to happen and I scratch my head wondering if artificial general intelligence is really the end goal, why isn't anybody pooling resources to make it happen? I mean, is their greed such that they prefer to try eating the whole pie even if it never comes over just sharing a slice? I think I already know the answer, yet I like to play some naivety for the sake of trying to think that somewhere in the Bay Area, there is a person or two with real ethics doing things with care and trying not to blow up our society as imperfect as it is. I stopped feeling surprised on the fact that AI's impact on people's lives has not been a net positive and I strive for real novelty, but I'm afraid as well of what the consequences mean to most of people lives, so what a conundrum this is, trying to feel enthusiasm for the new technologies while not trying to hide the unsavory truth that we are just being sold smoke and mirrors by people whose only passion is money.

Anyway, in the wake of making knowledge even more accessible and even more digestible, I think countries like mine are in a pickle. Our working culture, at least in IT, is quite focused on possessing badges. Value is given directly in proportion to how much you happen to know about a given technology, tool, methodology, etc. I come to believe that's driven by the business focus where outsourcing is the breadwinner and certifications are their golden ticket. This to me is quite conflicting since I value potential over domain. I don't dismiss knowledge, I think the more you possess the better are the odds for you to deal with a need, yet I think key skills like the ability to remember, in here, overpowers the ability to learn fast. Now that LLMs have stormed the market, the knowledge volume has been superseded by the ability to challenge concepts and the ability to ask the right kind of questions. So where exactly is my concern here? I think culturally we are not ready to shift our focus and the adoption of these tools will lower further the value of our skills not to say will push the price down or completely annihilate the business models we have in here. Big tech moving their operative costs in droves to a country like this while pushing the pedal to speed up their AI development can spiral out of control, especially for those who are first in line to be replaced: the operative costs themselves.

I don't feel bad for such a dire scenario. I think we need to learn to value craftsmanship, innovation and flexibility over any trophy wall. I think shifting our skills towards creating potential is not a small task but the benefits outweigh the challenges. However, I am pessimistic about our adoption speed, I just don't see people focusing on understanding the concepts behind the tools instead, so inventiveness is still "limp" over here and that's troubling because if we aim to survive being furtherly wiped out (economically), our only option is to stop being sweatshops and try to grow talent pools and do it fast. That means a lot, starting with leaving behind the mediocrity of our way of living.

I wish I could write this in a less critical way and be optimistic about the potential created by the tools that are popping, but paraphrasing a famous Eastern European philosopher: "there's a light at the end of the tunnel and it is another train coming towards us".

### Simplicity and focus are kings in my world (05/25)

I think this title was used in the first entry I added to this page, and well, I am reusing it.

I had an array of raspberries doing weird shit, mostly because I use them to learn. One of the weird things it did, which was not weird, nor learning related was serving CUPS. Yes, in 2025 I am still using CUPS. I have an old printer that went to the USA and came back with us. That shit is reliable so I am not throwing it away. I had reset its counter, changed its heads, refilled its tank and the thing still serves us after 10 years.

Among all the services I put into those raspberries I included prometheus, grafana, haproxy, airflow, redis, postgres, mariadb, influxdb, kafka, nginx, pihole, just to mention some. They all had a function and they all were calling each other and I tried to rebalance their load from time to time (every time I introduced a new service basically). The thing is, raspberries are powerful for their size, but not flawless, and one of their flaws is writing data. I'm not complaining about its IO capabilities, it's more about the limitant you had before the version 5 came around: either you write to SD or to USB. Well, I chose USB and while I tried not to put irrelevant data where it could be persisted, that sole configuration is challenging enough that you end up leaving loose ends, and one of those loose ends ended up busting a USB drive I had. Well, it turns out that one drive had data from grafana, jenkins, airflow and a CUPS exporter in it.

I did not care much about the drive being toast, after all, they are just so much useful, but reinstalling (even with playbooks) was a true pain in the ass, especially, because I wanted to make it better this time. Had I known how much airflow had changed since I installed it the last time, I would have changed my mind right away, but I wanted my airflow, my DAGs for querying the weather, the stock and keep track of my repositories were there. So I had decided to put everything back together, add monitoring using the statsd exported and ended up with a machine running at 80% CPU most of the time. Those were satisfactory results, except that the machine is tiny and opening a dashboard and printing homework at the same time would brick the whole thing. Could I just move some airflow parts to another machine and call it done? Sure, I would just move out the damn celery workers for the sake of having a CUPS exporter up, so in the end, my dashboard would let me know when the `cupsd` service would fail to start... Then it hit me.

The nerd in me was elated with all these changes, and upgrades and observability, and shit. I ended up wasting hours of my evening rather than sitting with my wife drinking coffee, all to see some graphs of things I could just look up in my phone and leave all the mess to just do one thing: print remotely, because that's all I really needed and when the printer service would not be available, I could just restart it. Well, I don't need a super complex orchestrator and scheduler for that, all I need is a script and a tool that was written in the 1970's.

In the pursuit of what I could do, I lost sight of what I needed to do and what was enough for my needs. I think that's a bad trait from us doing engineering, we let ourselves go from the simplest option ever and pursue what is not even needed because then our goal is no longer getting that piece of work done, but to learn more, try more, use more. Well, that loss of focus costed me 10 hours of my time; yes, I had fun troubleshooting, installing, fixing, configuring, testing; did I learn a couple new tricks? you bet! but in the end it was not really worth it.

So this is it, I ended up re-imaging the damn thing, installing cups, installing the driver it needs, adding a script to a cron job and removing the rest of the array of machines. Was it the simplest option I had? Hell no, I could buy myself a printer with wifi, or just plug the cord into the laptop where I wanted to print, but this one does the trick and costed me 10 minutes of my time, the rest, I give it back to where it matters, spending time with the people I care about.

### Yes, you are the 'I' in AI (05/25)

This week is closing with yet more breaking news about a Tech Giant laying off people at mass. The reason, as usual in this decade, is to free up resources for AI (they say to heavily invest yadah yadah, but they can't pull money out of their ass). What is intriguing to me is, to what benefit? I will speak from my own ignorance as usual, but I want to make a couple statements before I let it loose: 1. Us IT workers are overpaid, yes, we make wonders that nobody can quantify and that are only useful to those connected to a computer, and 2. AI is garbage.

I am not dismissing what AI can achieve. Back in 2017 I was fascinated with what machine learning could achieve, it is accurate when doing sorting when trained correctly and it can save tons of hours doing some predictive tasks when working with data. I wouldn't feel short of awe on what generative AI can achieve when working with natural languages and when it assists on tasks requiring finding patterns, briefing content and analyzing documents. AI works, that is true. But it is also true that AI has no intelligence, at all, nada. It can predict, it can analyze, it can summarize, it can do wonders with what is present, but it has zero intuition, it cannot foresee edge cases, it cannot simulate or come up with made up scenarios; the closest it has achieved is hallucinating and to the big AI minds, that's a faulty behavior.

I was thinking this would be a rant or some venting on how executives are assholes replacing people with made up ideas that fail when faced with reality. I still think they are assholes and that they would easily be replaced by AI because just like it, they lack imagination. Do you need examples? Well, we have an AI that can tell you if your security camera spotted a human or a racoon. We have another AI that can generate emojis. We have another AI that can delete your mom from your pics. We have another AI that can add a cringy smile to your face in a selfie. We have another AI that can generate tits and hands with 6 fingers. We have a bunch of bloated ideas that produce no value and of course we want to invest more into it, because it only needs time. We also have people who think they can come up with good products created using the ultimate shit buzzword: "vibe code". But again, it skips the edge cases, because as good as it can be, it can only use what is already there. It cannot invent, it has no sense of risk, it has no senses and well, hopefully no plane falls from the sky because it was "vibe coded".

I think that the technology is useful as any other technology is, but I also think that dismissing experience and training can be a dangerous endeavor, especially at the speed this is going on. Some people compare this to the transition from horses to cars, except most people took time to adopt a car, they didn't just start breeding colts with wheels. I think AI has potential, but to this moment their applications are just confirming that as a valuable technology it just can't deliver at the same scale as the Internet did, because, again, people trying to sell it have no imagination, they just want to put it _every-fucking-where_ and hope for people to buy how better their products are now that they have AI, but they don't.

Going back to point one, I could never get how a person writing code for a living could make close to a million a year while the people feeding the same useless monkey can barely make ends meet when producing their organic overpriced kale. I get it that this is more of a market driven behavior, but it has been destructive, even to the companies that started this and that now try to "free up" resources and sure, destroying livelihoods is the responsible thing to do, aight?

I am getting nowhere here, right? In the ideal world people would be worth what they contribute rather than what they pretend they are. But this world is less than ideal. I think as long as this goes on, AI will keep harvesting the ideas, criteria, instinct and senses from us humans until it can improve, but I am very skeptic that it will, it still lacks abilities and intuition and overall it lacks the ability to reason, even though those glorified data curators (data scientists my ass) claim they are able to reproduce what not even neuro-scientists and mathematicians (real scientists) understand with clarity. So expect more of the same, more glorified chatbots, more layoffs, more super expensive houses in the valley because Meta pays big bucks and more rot in our society, AI in our reality is not being pursuit to improve anyone's life (I can tell from first hand experience its application in medical devices is as good as using leeches), it exists to inflate the perception of value of companies that would collapse the moment someone pulls the plug.

Why the title anyway? Ah yes, well, I said it before, the "intelligent" entities we have created are just a validating, repurposing machines with a great ability to predict outcome, but the ideas they need to work, the **intelligence** they need to do the processing, that's all on you. Enjoy it while it lasts.

### Postmortems aren't easy (05/25)

One of the best parts of being in an SRE team **definitely** is: running a postmortem. It is also one of the hardest though. I was terribly sloppy when I started taking care of the task, and it was not until I was mentored by great engineers while running postmortems that I understood both the value and how to actually do them right (kind of learned by doing and got scraped in the process, to anyone who I disappointed during my learning process, I am still sorry about the bad experience). There is a great shortcut to get there though, and it is actually documented: Read engineering blogs, play the wheel of misfortune.

A postmortem goes beyond trying to find the ugly truth and following a template, although having a good template and a good postmortem document is a non-trivial task. A memorable postmortem is that one where you leave the room with conviction of: a) now you know way more than what you did when you wrote the document draft, b) your respect for your collaborators and their work has a new high and c) you're convinced you are going to make things better from that point. Truth is, this is not always achieved and especially point _c_ is a pain in the ass, because pressure on releasing new things is always pushing flaws downward in everyone's queue.

So why are postmortems hard anyway? Where is the process turning into something difficult?

Postmortems are a blameless process (or they should be). Keeping it that way is a titanic effort. Nobody likes to hear their work is dogshit and their sloppiness causes an outage, disregard, those things happen and the process of figuring out what happened in detail, when done right, takes out all the dirt under the rugs and sometimes it gets ugly.

Postmortems require a fair amount of effort, both because they require focus, and they require to do an investigation fast. It serves no good to schedule a postmortem meeting a month after an incident happened, by then the world has moved on. So, whoever oversees gathering people needs to do both: a thorough investigation and organize a meeting with a similar sense of urgency to what it took to solve an incident that triggered a postmortem.

Postmortems derail a ton of work. Incidents happen but making sure they don't come back require revisiting a lot of work and disrupting the release process of features, it demands commitment from engineering and product parties to prioritize site up above everything else. As with any important decision, it is not coming for free.

I will steer a little bit here and talk about what is a postmortem anyway, how it is expected to go and what made a postmortem memorable in my experience. My experience is limited though, so this should be brief.

When systems and infrastructure fail, failure brings a learning opportunity. Organizations that follow an incident management practice will identify the steps to follow from the moment an incident is detected until it is resolved, however, the root cause of an incident is not always crystal clear and while in the old ITIL world closure would come after investigation, yet a thorough root cause analysis and long term remediation may remain unclear; probably that's why ITIL themselves formally introduced the process.

The blameless postmortem process as a practice was popularized by Google when they introduced SRE, and it is a powerful tool to understand what has gone wrong rather than figuring out who dropped the ball. As I mentioned before it is easier said than done, egos and power dynamics (a.k.a. red tape office politics) often play against. I think that one of the best practices I witnessed when trying to make this blameless and a learning endeavor is keeping your organization values present, I think the reason why is because you already have a common goal which is honor those values and of course you have that fucking problem that stole away your sleep and hell, you want it gone!

But how do things flow exactly?

```

your system shits the bed
  |
  |____ you get alerted and you start an incident resolution process
          |
          |____ you find the source of the problem, you fix the problem
                  |
                  |____ you want to make sure this is not reoccurring, you start investigating what happened indeed
                          |
                          |____ you document your findings and establish a timeline
                                  |
                                  |____ you bring together all stakeholders of the system | business
                                          |
                                          |____ you unearth the details of the incident and make sure you answer:
                                                   - what gone wrong
                                                   - what gone right
                                                   - where luck was on your side
                                                   - where it wasn't
                                                   - what could have been done to prevent it
                                                  |
                                                  |____ you identify all the broken parts of your system and process, agree to a fix, set a timeline and a priority
                                                          |
                                                          |____ you follow up the fixing process
                                                                  |
                                                                  |____ you recover your sleep... or maybe not
```

Postmortem as a process peak when a meeting occurs. Memorable meetings are not those where people point fingers, but where people recognize things are broken and agree to fix things properly. Basically, a memorable postmortem is one where you agree to make things right. Sadly, not all leaders and top engineers want to go this way, tech debt is often what comes in exchange for moving fast, other people with dubious morals will do what they can to go unscathed or simply suggest sweeping things under the carpet. But even in the ugliness of these situations, great engineers rise, people calling out this as a deviation from your core values or simply owning the problem. When this happens, you realize not everything is rotten. Is this it? Just the old good vs evil? No advice here? Well, I can't spill the secret sauce, but basically try to run a meeting like this:

- Come prepared. Your document is clear, the details are there
- Have people read your doc
- Walk through your timeline, root cause analysis and start asking for gaps
- Have people question what they read, fill in the blanks, improve the picture
- Have the experts chime in, this is where their wisdom helps
- Ask the questions from the diagram
- Set action items
- Find owners, if nobody wants to **own the problem**, ask more questions
- Set a timeline, document again
- Follow up your document, empty promises bring problems back and you as the person in charge of preventing this from happening again, should oblige
- If the problem rises again, your investigation went wrong, it will happen, sometimes it is just symptomatic, sometimes it really is a bad fix, learn from it!

Make sure that no matter what, there is nobody pointing fingers or just ranting, you want a problem fixed, this is your duty.

But wait, who runs the meeting after all?

In my brief experience, incident management leads (the person who coordinated the firefighting) is the right person, however, there's nothing wrong with passing on the lead to a more experience engineer or a manager during the meeting, after all this is not an exercise to take credit, you want things fixed above everything else, your site stability, your system, your alerting and your sanity are at stake here.

What happens after this?

Well, if you write a good postmortem not only you helped solve a problem, you have good material for your engineering blog, a good tale for your nerd friends or a justification for your eye twitching.


### When you open google in your browser (04/25)

This is the first entry of what I will call: Tiny ass cheat sheet, where posts aren't going to be tiny, not reflective of anything going on with my life, yet I am trying to give some closure to some questions where either I bombed or had a _spirit de l'escalier_ moments.


So what happens when you call google.com from either your browser, curl, ping? This is a common systems engineering interview question, where the interviewer will try to delve into your understanding of networking, protocols, name resolution and ultimately try to get off by pointing out how ignorant you are if you miss a thing or two. Yes, those jerks.


So let's go step by step, alright? Your program will call google.com. It will create a socket (`socket()`) to connect to a remote address. There are going to be several steps involved, the first one will focus on name resolution, well, because you are using a name. So `connect()` will first of all require an address. Your OS will likely go to nsswitch to seek where the naming info is taken from, either a Berkeley database or a file. Normally, this is a file (`hosts`) so next stop will be reading that file and -in this scenario- finding nothing, it would not stop there, but moving on to where our name resolution resources are configured (`resolv`). Yes, there were already a bunch of system calls already involved in the process of read and lookup, no I will not mention those, I don't even know all of them (`bind()`, `listen()`, `read()`, `fstat()`, etc), so, the next stop is asking the gateway. This will require figuring out what address is the gateway (if not present in a routing table) so you're going to send (broadcast) an ARP call to your router if that one is missing or if the DHCP has not provided you with it (which likely had). So once you call your gateway (I will emcompass the "gateway" part as your router and ISP here for simplicity, IRL the modem/router at home would forward the call to the ISP routers, POPs and so on, and so on... `computer -> router -> isp`) your next call in the path of what `sendto()` would try (at this point the socket creation is still in need of an address, you will try resolution first), here is another call pending to be mentioned `getaddrinfo()` which we need to define where is the request actually going. So let's talk about domain name (DNS) now.

Your lookup made it all the way to the gateway and no name to address relation is found yet, you will care about routes later, first you need an IP and that's where DNS will come into play. Chances are, your first DNS will be that one your ISP provided, so if the entry for the address is cached in it, you will have an address. Let's pretend it isn't what it is now? Your call will make the DNS go and ask the root level. There are few servers in this level, all they are going to do is direct the call to the next level in the lookup hierarchy: top level, that `.com` extension thingy. DNS relies in forwarding calls in a recursive manner so the request lands where it is likely to be present in a resolution table, yet most of this work is cached already, that explains why sometimes it takes time (lots of it sometimes), for a change to be consistent with reality... now feels like eventual consistency is not so new anymore right?

So the top level (TLD) will search its authoritative server for the domain name (`google`) and send the request there. Can I see this in my interface using `dig`?

Kind of, try: `dig +trace -4 google.com` and you see it. If you happen to have your own Bind9 DNS you are going to get a more thorough view. Cherry on top? Add `strace` and see the syscalls by yourself.

So assuming you have an address (in this case, likely an API gateway or a point of presence that will get you content via CDN), now what? And wait we were sending ARP broadcasts, was this part of it? Nope, these calls were UDP calls to a known path (yes, that routing happened behind scenes and you were basically talking to only one DNS machine), and unless the response was so large or DNSSEC was involved or simply you used `-tcp`, the call will always use UDP.

Once you have your IP, your `connect()` call has a place to go. Now the routing tables in the network including your ISP will direct your packet to the machine with that address. BGP will give devices the optimal route for your request to go, wanna see where that is going? `traceroute` can help.

So what goes on after? It depends, are you using ping? (if ICMP is enabled) you have an echo request. If on the other hand your call uses HTTP, and TLS, then the call is slightly more complicated, your call will be processed by an HTTP server. If TLS is enabled you will have a TLS handshake. If the server handles more than one nameserver, it will need to find the appropriate certificate too (SNI), but the dance is quite the same: ClientHello, ServerHello, you had a negotiation for mechanism, supported extensions, keys exchange and start data transmission. In a nutshell:

`ARP->TCP->UDP->TCP->TLS->HTTP`

This is an imperfect way to paint it as a whole, yet it can be more complete than those infographic diagrams you find at LinkedIn if you care to read through. Jerks will still find a way to tell you you're not good enough, but now you can say, at least I tried to get it deeper.


### Understanding quantum computers (04/25)

I have to start by saying that I know nothing about quantum computers or even understand Grover's algorithm, or for that matter any other; I am super dumb at math, simple as that. I know shit about qubits and the medium that is actually useful for packing them. So yeah, I know nothing. I often watch people talking about quantum computers and how these machines are powerful because they can compute larger numbers faster and that qubits are both _digital_ states at the same time. Yet, I don't think people creating content talking about quantum computers actually understand how they work, so in a nutshell, just like me, they know shit. They just pretend they do and that sucks for the rest of us, because we don't get to _see_ the beauty of how these machines really work.

So trying to shed some light into my own ignorance I was curious if I could actually figure out how quantum computers work and while I got a grasp on it, my explanation still has gaps and it is imperfect, so if you're reading this, you know by now I am no expert nor pretend to be one and this explanation I share just to keep this _imperfect_ understanding alive.

So trying to be the simplest, these computers use qubits to represent data. Their qubits (complex circuits containing particles that can represent quantum states _wuuuut?_) are able to represent all possible answers (all possible combinations in a word) at the same time. Qubits may contain both states of information (_superposition_) so in 2 qubits we can have a word that is both 00, 01, 10 and 11. To make it even more intriguing, qubits often are entangled, thus, these 2 "bits" will contain all combinations when you only need to measure one to infer the values on the other. To make this even more interesting, you can have way larger and more complex words with less qubits compared to digital representation of bits, since the words are 2^N (two to the Nth where N is the number of qubits) unlike with conventional binary words where you "only" have N bits word size... it sounds the same, but it isn't, let's say for 4 bits you'd have a word size of 4 (yes you can combine and reach 16 possible values, but not at the same time) while in a quantum approach you'd have all combos of the states in that number of bits, thus you end up with 16 representations at once.

This is not the only advantage, and it is not advantage at all, having all possible values means nothing if you don't know what value is the one you're trying to represent, or in the practice to calculate. This is the part that often people omit to add into their explanation and in my opinion, the one that puts all the sense into the _how this shit works_. If you measure a computation (operation), in a digital (silicon based) computer you run some gateways and measure the result looking at what is on and off (what bits are 1's and 0's). Quantum machines are less simplistic, they have all results at the same time, so in order to figure out what result is the one that is true, the results are measured more than once. This is where this gets fascinating, a qubit is anything until it is measured, then it collapses (enters one state and only one) to what is *probably* truth. Upon a constant number of measurements, qubits will collapse into what is most likely the right answer, so the word with the highest count of occurrences is the one with the highest probability of being true... Jeez, so this is probabilistic? As I get it: Yes.

But who measures, where is this all being computed? How are all the pieces connected?

That is the part that I had the hardest time understanding, because quantum computers need digital computers to measure results, they are not replacements of each other. One holds the information, the other measures and computes the results to determine what is more likely to be truth. So qubits get signals? My understanding is that they get influenced by gateways just like a transistor would get a signal to produce a result, but their state is affected by external factors (particles, temperature, affecting their entanglement, magnetic changes) and those produce changes in the values they represent once measured. Is this accurate? I don't know, as I said, I am no expert, my understanding is that it kind of is correct, yet the measurement is the other part of the equation/chain, where other external factors like lasers doing the observation and feeding it into digital computers close the loop on a measurement.

Fascinating? Maybe, I wish my understanding was deeper so I could put this yet in a simpler explanation, but if I could summarize, it would go this way:

You have entangled particles in a medium (often supercooled) that is fed signals. These particles are part of a logical gateway that will produce a result once measured. This operation is going to be repeated several times and the measurement will be aggregated into a probabilistic array where the highest probability fed into an algorithm will confirm a response. This is not superfast, it is as fast as the measuring computers get, however it is extremely parallel and that is where the advantage in front of a traditional computer lies, you can measure all paths taking you to a result, and those results in a few iterations will get a trustworthy value that otherwise would require a constant iteration, aggregation and incremental evaluation in a sequential fashion that would take longer time to produce a similar answer.

### Two minute chores (04/25)

I have been quite obsessed over a couple years on this one topic. In our day to day we often struggle to get done more than what we have pending, often, because we choose to do so. Turns out a lot of that burden is composed of tiny tasks that we procrastinate, even worse, those tiny tasks are sneaky and steal the time of other tasks of the same size. I like to call them two minute chores and those little bastards are _every-fucking-where_.

I bring the topic not because I have a clean strategy or because they are important for improving our mood (although the feeling of achievement often is a booster for our mood), I just think that being aware of these kind of little items is important to recognize them and flush them out quick, then we are better suited to take care of larger and more demanding tasks.

If I could propose a rule on how to identify and tackle these tasks, it would be quite simple: if the task needs a small amount of effort, time and we know what to do from start to end, we should execute right away. There is conflict in doing this though (as always), sometimes a fair amount of chores is composed of these tiny blocks so we end up focusing on them and they steal away our attention from what matters. Is there an easy way to find balance? I'd say, just try to find these tasks in between larger activities, usually that's when they pop and that's when you can take care of them, right there!

Is that it? Well, you could say so, except, that often someone else will put more of those in your queue and well, now you have something else to do, that's yet another perk of a busy life.

### Focus is a privilege (03/25)

I have to start by saying **focus is a beautiful state of mind**. Focus gets a marvelous amount of high quality things done. I would not think we would have classic music or high end computers without it. Focus is also a very expensive state of mind. It not only consumes a fair amount of resources from us, but it demands a very special set of conditions for it to thrive. No wonder focus is a rare and precious resource.

Some societies are quite appreciative of it, they want it to flourish, and it really pays fostering it. However, focus is not cheap either. It requires both a substantial amount of time, a proper environment (including lighting and temperature) and isolation from distractions. The struggle will not end there when it is hard to differentiate between distractions and inspiration, where ends one and starts the other?

Other societies, like mine, are quite dismissive in what it takes to achieve focus. The outcome is not great for them. We live plunged in a sea of distractions and noise that mistakenly is tagged as vivid or cheerful. There is a price to the lack of focus in life, a constant sense of underachievement, low quality of outcome and low productivity are few examples. Overall, living surrounded by what our ancestors called "mitote" is harmful. I wonder if sometimes this was purposely started by higher spheres in our society to keep lower classes from thriving; always distracted, always struggling. In places like my hometown, you are constantly bombarded by noise from all sources, the streets, the neighbors, the media (if you allow it into your house), job (trivial) struggles and gossip and cherry on top: heatwaves. Overall, it is no wonder, countries like mine aren't capable of raising the quality of life of their inhabitants where fostering a healthy state of mind is not paramount, we're so distracted that all we care about is making it out just another day. Life is a constant struggle here, even worse, we chase conflict, as if poverty wasn't enough.

Why am I writing this? Why do I care?

I think in our times, distractions are produced en masse. Not only that, they are delivered to us efficiently by a myriad of machines and media that can achieve it like never before, to the extent that we carry a town crier in our pockets. This is detrimental not only to our productivity, but to our mental health, after all, chaos and hectic drive us into a state of psychosis. There are studies sustaining that exposure to noise has adverse effects to cognitive domains, yet we disregard these warnings as irrelevant or too serious. If that's not enough, most thriving businesses are created around distractors, what's most ironic: we pay for it!

In the software engineering world, there is a thing we call a flow, which basically is achieving a peak in our ability to focus on solving a problem. A flow is a fragile state of mind that can easily be disrupted and that we cannot bring back just as easily as we take out our phones and address an alert. There's nothing special about software engineering to be fair, I guess a music composer or a martial artist can achieve more with this state of mind, but I can only talk about what concerns me and probably come here and regret of a bunch of decisions I have made in my life that have deprived me of that privilege of having calm in my life.

Is this reversible?

I think reverting the damage noise and distractions make to our lives is becoming increasingly difficult, we make it that way. Quiet places are rare, distant, exclusive, and a healthy distance from technology is dubiously productive. As time progresses, the lack of achievements takes a toll on our cognitive capacity, thus affecting our skills, our health, our finances and overall hindering the ability to get into a place where we can focus more and deliver more. Quite like a destructive cycle.

I will not draw a conclusion to these lines, simply, because I lost my flow.

### A brief parenthesis on what makes SRE and DevOps different (02/25)


I would come here and rant endlessly about these two terms being used interchangeably, but truth is, SRE is given whatever interpretation a hiring manager pulls out of their ass. Knowing the difference though, is useful because setting expectations is important.

We could argue that both roles intersect. That's not wrong. From time to time one guy is doing the other's job and vice versa, but that's just how things are. A software engineer could cross those thresholds as well, no biggie.

So what's the fuzz then? I think you should think about site reliability when you care about three major aspects of your infrastructure (and your products for that matter):

- Performance
- Resiliency
- Observability

Yes, those are corny terms, just like shift left, democratization and slice and dice, when used as buzz-words, all is shit. These three, if you please, can give you an insight on things you will care more when doing site reliability as a discipline though:

- Performance (as in really how often your software does what is intended vs. how often it fails) and resource utilization. Making the best use of the green papers and making sure the ball drops as least as possible, ideally, below what agreements allow (SLA, SLO, SLI and all the jazz)
- Setting up capacity and redundancy to make a site tolerant to the unavoidable failure. Site up over everything else
- Have the means to understand a problem in a system effectively. Not just guessing or waiting for reports but seeing the failure cause and its effects

Other not less important criteria are covered in what this discipline does, e.g. testing for load and failure, but that can be correctly classified as a resiliency effort.

So now you know. Tooling is good, but it is trivial, because if you talk site reliability, you don't talk about Kubernetes, Terraform or Jenkins, you talk about keeping your site up, because you care about service levels, resource utilization and metrics... you focus on that stupid acronym of KTLON (Fugly as it is).

*- Oh this guy forgot to mention toil!*

Nah, automation is fabulous, it eliminates a lot of waste and errors, but arguably, every single link in the delivery chain should have an appetite for not doing the same task twice. So toil reduction should not be something for SRE's only. Feel free to disagree.

### Operations at large scale are complicated, culture is almost impossible (02/25)

Throughout this journey I have noticed a big gap between big tech companies and the rest.

Now, I must add a disclaimer here: I have only made it into one of those big tech places in my life; I could not complete my onsite with Google, I never made it past screening at Meta, and I hated the only time I dared to start a process with Netflix.
Still I think, since these companies share some of their DNA considering people working for them move back and forth in between them, there is something that sets them apart from the rest other than the massive talent pool and revenue they generate: the culture they build around their infra is far beyond their competitors.

I know that talking (only) from the LinkedIn perspective is terribly limited, yet I dare to say that even when the tooling was dated (and after 2022, quite faulty), their processes were far ahead of any other small and large businesses I have worked with. And probably that's one of the many things that sets them apart. They focus on what matters and make sure to keep it well greased.

Most places, small, large, startups and so on rely on what's the norm: chats, review cycles, stand ups, a ton of tooling and a devops-culture; this is nothing outstanding. Big tech folks have other aces up their sleeves, even when they are large, fat and slow compared to startups: They have continuous reviews, a mature/sophisticated incident response process and culture and tooling that makes sure things are not being overlooked. They will be overlooked for sure, we are humans with the attention span of a mayfly life, but you really can't blame the tools there.

Now that I started the journey in a second place I notice kind of the same missing pieces as I did in the first one (at least after my adventure in Silicon Valley), they are lagging and don't see the relevance these processes have into getting them started with more sophisticated ways to work. Again, I think it is not the tooling. My former (short lived tenure) place had an amazing set of tools to get things done. They drank the Kubernetes and CNCF kool-aid hard. And they did it terribly well. Yet they sucked at the most basic operational tasks: catching issues, remediation, having a blameless culture and having the means to fix shit fast. Automation seems to be the Achilles heel of many.

 They were by no means mediocre engineers, they moved amazingly fast when rolling out projects. I think where they ran dry, was drinking the site up and site reliability (again) kool-aid. Now this is not preaching how good SRE is and how good it can be for most organizations. I think the term is overhyped and misapplied in most places. I think this is more of a site engineering culture that actually cares about two things: making things easy to use and making issues easy to fix. Well, turns out making things easy is terribly hard and it demands resources, tons of them and once you get there, moving your ops to India, Mexico or any developing place, well, it is like kicking the Jenga tower (not to say your own people in the teeth), because operations can be ported, culture can't, like a good brew, it needs the right ingredients, the right temperature, the right timing.

So yeah, besides all the fad, bloat, hate, overpay and frustration these places had before magic faded, they changed things to such an extent that even today where they are the eroded shells, it is still damn hard to catch up with what they built.

Oh and those shells are going to be back in the game, I'm more than sure that the industry is reinventing itself and I am eager to see where this is all headed once the turmoil subsides.

### Zeitgeist (01/25)

In the Zeitgeist of what seems to be a recurrent scenario where nobody wins, I browse eagerly through the news to figure out what's the next big deal. This week's big deal is China doing things the way it should be. A breakthrough with restricted resources, odds against, but we ignore the big picture here: no meaningful paper being published the past decade has no Chinese authors in it. It's like Silicon Valley is oblivious to what the reality is and they race towards a doomsday of unplanned consequences. How good would AGI be when you have no means to give people a livelihood? I think from all scenarios China seems to be the best prepared nation to come up and trump over the rest in this race. I am not praising it though. I don't think this AI race should continue without a common end that is not profit, I think that's where America got all wrong and where at least their counterpart has a best chance of not starving their population by capturing that holy grail.

In the wake of the non-stopping round of layoffs, I cannot stop here just cheering for DeepSeek achievements. I think we need to come to a realization: Things won't go back to where they were before 2020 started. The race of AI is just a tipping point on something that is kind of non sustainable fueled by greed.

It is hard to argue that products of many large companies are not getting worse. Development is getting worse. Operations are getting worse. I think this is no surprise to anyone thinking this through. Executives want to please shareholders, and shareholders sustained their expectations past a blip of what world economies became when a pandemic hit. To make things slightly more interesting, GAI came into the scene with hunger for resources, so capex surged not only through the added load that Covid brought, but because AI demands power. Why the worsening then? These are multi-billion dollar businesses after all, right? Well, these places are massive in all extents of the word, **including their brand**, so they can afford to lose quality without being hit, after all, they started shipping their shiny models fueling their AI (a shitty one). Cutting corners in engineering costs is a no brainer for these guys (In the words of a recruiter when I asked why Mexico: "It is cheaper to get an engineer in Mexico than in California, you don't have to pay hundreds of thousands"), they don't care about social impact, they just want to cut costs, so moving things to other regions seemed fair to them. There is little concern on the "you get what you pay for" motto, there is little concern for anything that is not pushing the operational costs down; keeping the lights on (KTLON) while the new guys catch up seems sufficient, inventive? We have our AI hoax for that!

I should stay shut and be happy for that then? I am on the winning side, right? Not at all, the winning side has a horrible working culture and a lack of critical thinking that blocks us from fostering our own success. It seems that as long as the model is running, that's not a top priority. So while this keeps going (and it will keep going) some folks struggle to hold on their bet of a multimillion valued dump and their H1B shackles, some folks rush into collecting badges so they can add FAANG, MAANG or whatever shit it's now to their resume, while others just cash those big fat bonuses to keep those Big Sur bunkers well supplied.

Anyway, the market is and will remain a tide of non-sense as it has been for the past lustrum. I expect nothing, but more of the same: Layoffs, a desperate fight to reduce capex and improve revenue, all at the cost of quality, dignity and sadly, livelihood.

### (public) Cloud computing fucking sucks (01/25)

I could as well say people fucking suck, most of the issues from cloud computing come from the people running and using them after all. I'm ranting here because it is so damn common to see leaks coming from people who otherwise would have a room with a couple of racks gathering dust with old ass systems that just work when nobody comes with a great idea, except that, according to some C level jerk, the neckbeard maintaining those solid boxes is too expensive and all the people at the golf course talk about how amazing is to use Amazon cloud for their operations... Then, the nightmare starts.

I came to ask myself how could we trust our infra to the most toxic company culture in the globe, that by itself is mind blowing, but on and on, the cloud is just a cake of layers trying to emulate computers. Don't get me wrong, it is fantastic that you can borrow resources at will, only what you need, leave the rest, but there are hidden costs of thinking this actually gets us somewhere safe. Credentials leak all the time. Workflows fail all the time. Groups scale out of control. Costs scale out of control. Yes, there's a human behind all that stupidity, but when putting all together, was leaving the old Dell blade running that bad?

We are sold that we need to be ready to scale, hell, I have been an SRE for half a decade and I totally buy it, but not every business is the next Google, so why design thinking you will ever meet that workload is beyond my comprehension.
Am I just yelling at a cloud? You bet! Distributed computing is fucking awesome. Compute on demand is fucking awesome. Global scale availability is fucking awesome. Orchestration and provisioning automation is fucking awesome. Those concepts are huge, we would have no large data analysis without them, we would have no GAI (and LLMs) without them and many of us would not even have a job without them. As concepts they are magnificent, but the Devil is in the details, right? You get a bunch of people building layers on top of layers and you end up with an obnoxious cake of complexity solving a smaller problem than the one it created by just existing. Not to mention how hard it is to even get your hands on some decent hardware nowadays (good luck getting some Blackwell orders fulfilled). This is not great, especially for companies with zero innovation who will just use and pay the bills. Those poor bastards are the same who will leak a token into a Gitlab public account and get all their customers PII data leaked into the dark web or a stupid 4chan room (wink, wink). Guess what, settlements are fucking expensive. Ransom is fucking expensive. Changing your SSN is fucking expensive (in time). But well, this is our reality today and we learn to cope with it as we lay our hopes into ChatGPT giving us the fix to our last typo that caused a bill of ten quadrillions on unused API Gateway calls.

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

I won't delve here into tmpfs because I don't know where it started beyond what [wikipedia](https://en.wikipedia.org/wiki/Tmpfs) has. However, if you ever worked with a raspberry, you know SD card lifetime is limited and I come to find that tmpfs has been a time and money saver since I minimized the writing to my storage by using it. Yet as you may expect, this is ephemeral (since it is saving data into a block in the RAM) so yes, this has two drawbacks actually, you lose memory for the sake of having a temporary place to write. Is it worth it? IMO yes. Any permanent (and important) storage I have deferred to external drives, but external drives are slow. Things like logs (which in these boards I don't care about), go to the tmpfs for sure.

So how easy is it to get this going?

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

<hr>

### Other entries

[[About me]](./archive/about.md)
[[2024]](./archive/2024.md)

<div align="right">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-PW9NV6T54Q"></script>
    <!-- added for measuring visits only -->
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-PW9NV6T54Q');
    </script>
</div>

