All opinions I share here are my opinions, I don't mean any harm and my main interest is to vent out and well, share whatever is going on with my day to day, so yes, eventually I contradict myself.

<!--
<div align="right">
  <small>
    <i>If you're still reading, my title is not misrendering and your visit is a datapoint in GA4, I promise that's all I collect.</i>
  </small>
</div>
-->

### About me

I have some knowledge in things like Operating Systems Administration, Software Development, Infrastructure Engineering and Site Reliability. All those catchy terms just mean I can deal with computers at a large scale, write code to run them and understand what it takes to keep them running for more than a day.
I have worked in the financial world, consulting, gaming and recently in the internet industry. I like to meet people although I am not the most extrovert and I like to spend time learning about things related to technology and the industries I work with. I enjoy mentoring and often I end up learning more from others.

I have been lucky enough to have an education at many levels in many countries and continued that streak with my professional life.


---

### Yes, you are the 'I' in AI (05/25)

This week is closing with yet more breaking news about a Tech Giant laying off people at mass. The reason, as usual in this decade, to free up resources for AI (they say to heavily invest yadah yadah, but they can't pull money out of their ass). What is intriguing to me is, to what benefit? I will speak from my own ignorance as usual, but I want to make a couple statemets before I let it loose: 1. Us IT workers are overpaid, yes, we make wonders that nobody can quantify and that are only useful to those connected to a computer, and 2. AI is garbage.

I am not dismissing what AI can achieve. Back in 2017 I was fascinated with what machine learning could achieve, it is accurate doing sorting when trained correctly and it can save tons of hours doing some predictive tasks when working with data. I wouldn't feel short of awe on what generative AI can achieve when working with natural languages and when it assists on tasks requiring finding patterns, briefing content and analyzing documents. AI works, that is truth. But it is also truth that AI has no intelligence, at all, nada. It can predict, it can analyze, it can summarize, it can do wonders with what is present, but it has zero intuition, it cannot foresee edge cases, it cannot simulate or come up with made up scenarios; the closest it has achieved is hallucinating and to the big AI minds, that's a faulty behavior.

I was thinking this would be a rant or some venting on how executives are assholes replacing people with made up ideas that fail when faced with reality. I still think they are assholes and that they would easily be replaced by AI because just like it, they lack imagination. Do you need examples? Well, we have an AI that can tell you if your security camera spotted a human or a racoon. We have another AI that can generate emojis. We have another AI that can delete your mom from your pics. We have another AI that can add a cringy smile to your face in a selfie. We have another AI that can generate tits and hands with 6 fingers. We have a bunch of bloated ideas that produce no value and of course we want to invest more into it, because it only needs time. We also have people who think they can come up with good products created using the ultimate shit buzzword: "vibe code". But again, it skips the edge cases, because as good as it can be, it can only use what is already there. It has no inventive, it has no sense of risk, it has no senses and well, hopefully no plane falls from the sky because it was "vibe coded".

I think that the technology is useful as any other technology is, but I also think that dismissing experience and training can be a dangerous endeavor, especially at the speed this is going on. Some people compare this to the transition from horses to cars, except most people took time to adopt a car, they didn't just started breeding colts with wheels. I think AI has potential, but to this moment their applications are just confirming that as a valuable technology it just can't deliver at the same scale as the Internet did, because, again, people trying to sell it have no imagination, they just want to put it _every-fucking-where_ and hope for people to buy how better their products are now that they have AI, but they don't.

Going back to point one, I could never get how a person writing code for a living could make close to a million a year while the people feeding the same useless monkey can barely make ends meet when producing their organic overpriced kale. I get it that this is more of a markets driven behavior, but it has been destructive, even to the companies that started this and that now try to "free up" resources and sure, destroying livelihoods is the responsible thing to do, aight?

I am getting nowhere here, right? In the ideal world people would be worth for what they contribute rather than what they pretend they are. But this world is less than ideal. I think as long as this goes on, AI will keep harvesting the ideas, criteria, instinct and senses from us humans until it can improve, but I am very exceptic that it will, it still lacks abilities and intuition and overall it lacks the abilty to reason, even though those glorified data curators (data scientists my ass) claim they are able to reproduce what not even neuro-scientists and mathematicians (real scientists) understand with clarity. So expect more of the same, more glorified chatbots, more layoffs, more super expensive houses in the valley because Meta pays big bucks and more rot in our society, AI in our reality is not being pursuit to improve anyone's life (I can tell from first hand experience its application in medical devices is as good as using leeches), it exists to inflate the perception of value of companies that would collapse the moment someone pulls the plug.

Why the title anyway? Ah yes, well, I said it before, the "intelligent" entities we have created are just a validating, repurposing machines with a great ability to predict outcome, but the ideas they need to work, the **intelligence** they need to do the processing, that's all on you. Enjoy it while it lasts.

### Postmortems aren't easy (05/25)

One of the best parts of being in an SRE team **definitely** is: running a postmortem. It is also one of the hardest though. I was terribly sloppy when I started taking care of the task, and it was not until I was mentored by great engineers while running postmortems that I understood both the value and how to actually do them right (kind of learned by doing and got scraped in the process, to anyone who I disappointed during my learning process, I am still sorry about the bad experience). There is a great shortcut to get there though, and it is actually documented: Read engineering blogs, play the wheel of misfortune.

A postmortem goes beyond trying to find the ugly truth and following a template, although having a good template and a good postmortem document is a non-trivial task. A memorable postmortem is that one where you leave the room with conviction of: a) now you know way more than what you did when you wrote the document draft, b) your respect for your collaborators and their work has a new high and c) you're convinced you are going to make things better from that point. Truth is, this is not always achieved and especially point _c_ is a pain in the ass, because pressure on releasing new things is always pushing flaws downward in everyone's queue.

So why are postmortems hard anyway? Where is the process turning into something difficult?

Postmortems are a blameless process (or they should be). Keeping it that way is a titanic effort. Nobody likes to hear their work is dogshit and their sloppiness caused an outage, disregard, those things happen and the process of figuring out what happened in detail, when done right, takes out all the dirt under the rugs and sometimes it gets ugly.

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

Well, if you write a good postmortem not only you helped solving a problem, you have good material for your engineering blog, a good tale for your nerd friends or a justification for your eye twitching.


### When you open google in your browser (04/25)

This is the first entry of what I will call: Tiny ass cheat sheet, where posts aren't going to be tiny, not reflective of anything going on with my life, yet I am trying to give some closure to some questions where either I bombed or had a _spirit de l'escalier_ moments.


So what happens when you call google.com from either your browser, curl, ping? This is a common systems engineering interview question, where the interviewer will try to delve into your understanding of networking, protocols, name resolution and ultimately try to get off by pointing out how ignorant you are if you miss a thing or two. Yes, those jerks.


So let's go step by step, alright? Your program will call google.com. It will create a socket (`socket()`) to connect to a remote address. There are going to be several steps involved, the first one will focus on name resolution, well, because you are using a name. So `connect()` will first of all require an address. Your OS will likely go to nsswitch to seek where the naming info is taken from, either a Berkeley database or a file. Normally, this is a file (`hosts`) so next stop will be reading that file and -in this scenario- finding nothing, it would not stop there, but moving on to where our name resolution resources are configured (`resolv`). Yes, there were already a bunch of system calls already involved in the process of read and lookup, no I will not mention those, I don't even know all of them (`bind()`, `listen()`, `read()`, `fstat()`, etc), so, the next stop is asking the gateway. This will require figuring out what address is the gateway (if not present in a routing table) so you're going to send (broadcast) an ARP call to your router if that one is missing or if the DHCP has not provided you with it (which likely had). So once you call your gateway (I will emcompass the "gateway" part as your router and ISP here for simplicity, IRL the modem/router at home would forward the call to the ISP routers, POPs and so on, and so on... `computer -> router -> isp`) your next call in the path of what `sendto()` would try (at this point the socket creation is still in need of an address, you will try resolution first), here is another call pending to be mentioned `getaddrinfo()` which we need to define where is the request actually going. So let's talk about domain name (DNS) now.

Your lookup made it all the way to the gateway and no name to address relation is found yet, you will care about routes later, first you need an IP and that's where DNS will come into play. Chances are, your first DNS will be that one your ISP provided, so if the entry for the address is cached in it, you will have an address. Let's pretend it isn't what now? Your call will make the DNS go and ask the root level. There are few servers in this level, all they are going to do is direct the call to the next level in the lookup hierarchy: top level, that `.com` extension thingy. DNS relies in forwarding calls in a recursive manner so the request lands where it is likely to be present in a resolution table, yet most of this work is cached already, that explains why sometimes it takes time (lots of it sometimes), for a change to be consistent with reality... now feels like eventual consistency is not so new anymore right?

So the top level (TLD) will search its authoritative server for the domain name (`google`) and send the request there. Can I see this in my interface using `dig`?

Kind of, try: `dig +trace -4 google.com` and you see it. If you happen to have your own Bind9 DNS you are going to get a more thorough view. Cherry on top? Add `strace` and see the syscalls by yourself.

So assuming you have an address (in this case, likely an API gateway or a point of presence that will get you content via CDN), now what? And wait we were sending ARP broadcasts, was this part of it? Nope, these calls were UDP calls to a known path (yes, that routing happened behind scenes and you were basically talking to only one DNS machine), and unless the response was so large or DNSSEC was involved or simply you used `-tcp`, the call will always use UDP.

Once you have your IP, your `connect()` call has a place to go. Now the routing tables in the network including your ISP will direct your packet to the machine with that address. BGP will give devices the optimal route for your request to go, wanna see where that is going? `traceroute` can help.

So what goes on after? It depends, are you using ping? (if ICMP is enabled) you have an echo request. If on the other hand your call uses HTTP, and TLS, then the call is slightly more complicated, your call will be processed by an HTTP server. If TLS is enabled you will have a TLS handshake. If the server handles more than one nameserver, it will need to find the appropriate certificate too (SNI), but the dance is quite the same: ClientHello, ServerHello, you had a negotiation for mechanism, supported extensions, keys exchange and start data transmission. In a nutshell:

`ARP->TCP->UDP->TCP->TLS->HTTP`

This is an imperfect way to paint it as a whole, yet it can be more complete than those infographic diagrams you find at LinkedIn if you care to read through. Jerks will still find a way to tell you you're not good enough, but now you can say, at least I tried to get it deeper.


### Understanding quantum computers (04/25)

I have to start by saying that I know nothing about quantum computers or even understand Grover's algorithm, or for that matter any other; I am super dumb at math, simple as that. I know shit about qubits and the medium that is actually useful for packing them. So yeah, I know nothing. I often watch people talking about quantum computers and how these machines are powerful because the can compute larger numbers faster and that qubits are both _digital_ states at the same time. Yet, I don't think people creating content talking about quantum computers actually understands how they work, so in a nutshell, just like me, they know shit. They just pretend they do and that sucks for the rest of us, because, we don't get to _see_ the beauty of how these machines really work.

So trying to shed some light into my own ignorance I was curious if I could actually figure out how quantum computers work and while I got a grasp on it, my explanation still has gaps and it is imperfect, so if you're reading this, you know by now I am no expert nor pretend to be one and this explanation I share just to keep this _imperfect_ understanding alive.

So trying to be the simplest, these computers use qubits to represent data. Their qubits (complex circuits containing particles that can represent quantum states _wuuuut?_) are able to represent all possible answers (all possible combinations in a word) at the same time. Qubits may contain both states of information (_superposition_) so in 2 qubits we can have a word that is both 00, 01, 10 and 11. To make it even more intriguing, qubits often are entangled, thus, these 2 "bits" will contain all combinations when you only need to measure one to infer the values on the other. To make this even more interesting, you can have way larger and more complex words with less qubits compared to digital representation of bits, since the words are 2^N (two to the Nth where N is the number of qubits) unlike with conventional binary words where you "only" have N bits word size... it sounds the same, but it isn't, let's say for 4 bits you'd have a word size of 4 (yes you can combine and reach 16 possible values, but not at the same time) while in a quantum approach you'd have all combos of the states in that number of bits, thus you end up with 16 representations at once. 

This is not the only advantage, and it is not advantage at all, having all possible values means nothing if you don't know what value is the one you're trying to represent, or in the practice to calculate. This is the part that often people omit to add into their explanation and in my opinion, the one that puts all the sense into the _how this shit works_. If you measure a computation (operation), in a digital (silicon based) computer you run some gateways and measure the result looking at what is on and off (what bits are 1's and 0's). Quantum machines are less simplistic, they have all results at the same time, so in order to figure out what result is the one that is truth, the results are measured more than once. This is where this gets fascinating, a qubit is anything until it is measured, then it collapses (enters one state and only one) to what is *probably* truth. Upon a constant number of measurements, qubits will collapse into what is most likely the right answer, so the word with the highest count of occurrences is the one with the highest probability of being truth... Jeez, so this is probabilistic? As I get it: Yes.

But who measures, where is this all being computed? How all the pieces are connected?

That is the part that I had the hardest time understanding, because quantum computers, need digital computers to measure results, they are not replacements of each other. One holds the information, the other measures and computes the results to determine what is more likely to be truth. So qubits get signals? My understanding is that they get influenced by gateways just like a transistor would get a signal to produce a result, but their state is affected by external factors (particles, temperature, affecting their entanglement, magnetic changes) and those produce changes in the values they represent once measured. Is this accurate? I don't know, as I said, I am no expert, my understanding is that it kind of is correct, yet the measurement is the other part of the equation/chain, where other external factors like lasers doing the observation and feeding it into digital computers close the loop on a measurement.

Fascinating? Maybe, I wish my understanding was deeper so I could put this yet in a simpler explanation, but if I could summarize, it would go this way:

You have entangled particles in a medium (often supercooled) that is fed signals. These particles are part of a logical gateway that will produce a result once measured. This operation is going to be repeated for several times and the measurement will be aggregated into a probabilistic array where the highest probability fed into an algorithm will confirm a response. This is not superfast, it is as fast as the measuring computers get, however it is extremely parallel and that is where the advantage in front of a traditional computer lies, you can measure all paths taking you to a result, and those results in a few iterations will get a trustworthy value that otherwise would require a constant iteration, aggregation and incremental evaluation in a sequential fashion that would take longer time to produce a similar answer.

### Two minute chores (04/25)

I have been quite obsessed over a couple years on this one topic. In our day to day we often struggle to get done more than what we have pending, often, because we choose to do so. Turns out a lot of that burden is composed by tiny tasks that we procrastinate, even worse, those tiny tasks are sneaky and get to steal the time of other tasks of the same size. I like to call them two minute chores and those little bastards are _every-fucking-where_.

I bring the topic not because I have a clean strategy or because they are important for improving our mood (although the feeling of achievement often is a booster for our mood), I just think that being aware of these kind of little items is important to recognize them and flush them out quick, then we are better suited to take care of larger and more demanding tasks.

If I could propose a rule on how to identify and tackle these tasks, it would be quite simple: if the task needs a small amount of effort, time and we know what to do from start to end, we should execute right away. There is conflict in doing this though (as always), sometimes a fair amount of chores is composed of these tiny blocks so we end up focusing on them and they steal away our attention from what matters. Is there an easy way to find balance? I'd say, just try to find these tasks in between larger activities, usually that's when they pop and that's when you can take care of them, right there!

Is that it? well, you could say so, except, that often someone else will put more of those in your queue and well, now you have something else to do, that's yet another perk of a busy life.

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

Other not less important criteria are covered into what this discipline does, e.g. testing for load and failure, but that can be correctly classified as a resiliency effort.

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

I could as well say people fucking suck, most of the issues from cloud computing come from the people running and using them after all. I'm ranting here because it is so damn common to see leaks coming from people who otherwise would have a room with a couple of racks gathering dust with old ass systems that just work when nobody comes with a great idea, except that, according to some C level jerk, the neckbeard maintaining those solid boxes is too expensive and all the people at the golf course talk about how amazing is to use Amazon cloud for their operations... then, the nightmare starts.

I come to ask myself how could we trust our infra to the most toxic company culture in the globe, that by itself is mind blowing, but on and on, the cloud is just a cake of layers trying to emulate computers. Don't get me wrong, it is fantastic that you can borrow resources at will, only what you need, leave the rest, but there are hidden costs of thinking this actually gets us somewhere safe. Credentials leak all the time. Workflows fail all the time. Groups scale out of control. Costs scale out of control. Yes, there's a human behind all that stupidity, but when putting all together, was leaving the old Dell blade running that bad? 

We are sold that we need to be ready to scale, hell, I have been an SRE for half a decade and I totally buy it, but not every business is the next Google, so why design thinking you will ever meet that workload is beyond my comprehension.
Am I just yelling at a cloud? You bet! Distributed computing is fucking awesome. Compute on demand is fucking awesome. Global scale avaliabilty is fucking awesome. Orchestration and provisioning automation is fucking awesome. Those concepts are huge, we would have no large data analysis without them, we would have no GAI (and LLMs) without them and many of us would not even have a job without them. As concepts they are magnificent, but the Devil is in the details, right? You get a bunch of people building layers on top of layers and you end up with an obnoxious cake of complexity solving a smaller problem than the one it created by just existing. Not to mention how hard is to even get your hands on some decent hardware nowadays (good luck getting some Blackwell orders fulfilled). This is not great, especially for companies with zero innovation who will just use and pay the bills. Those poor bastards are the same who will leak a token into a Gitlab public account and get all their customers PII data leaked into the dark web or a stupid 4chan room (wink, wink). Guess what, settlements are fucking expensive. Ransom is fucking expensive. Changing your SSN is fucking expensive (in time). But well, this is our reality today and we learn to cope with it as we lay our hopes into ChatGPT giving us the fix to our last typo that caused a bill of ten quadrillions on unused API Gateway calls.

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

<hr>

### Older entries

[2024](./archive/2024.md)

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
