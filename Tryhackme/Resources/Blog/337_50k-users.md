# TryHackMe Reaches 50,000 Members

**ID Original:** no disponible
**Slug:** 50k-users
--------------------

If you didn't know, TryHackMe is a platform for learning Cybersecurity through guides, interactive questions and deployable vulnerable machines. TryHackMe has content for all experience levels.
The timeline below shows our progress since the start. From December 2019 to April, we've had 40,000 active registrations. However, the recent growth has been more recent, ever since John Hammond created a video showcasing our platform; followed by other streamers when we released a competitive hacking game, King of the Hill .
Platform Performance
The sudden growth caused several performance issues. Here is what we did to solve them (please note, this isn't a technical blog post):
Splitting up the application & Adding a Load Balancer
With the platform getting between 600-1000 sign ups a day and our daily active users constantly increasing, TryHackMe slowed down to a crawl. Our first step was to split up our application and have everything behind a load balancer.
We managed to split up TryHackMe within a few days. This helped with performance.. But not for long.. We had solved the lack of available resources problem, but our once fast database queries were starting to take a hit.
The good, the bad and the queries..
When TryHackMe was first released at the end of 2018, we focused on releasing a MVP, not engineering the most optimal solution. Upon release, it worked.. people could deploy their own hackable machine, follow guides and immediately start hacking; the idea of TryHackMe has been validated. Pages loaded in <1s.
In October 2019 when we ran an event called HackBack2 , where 27 Universities compete to hack as many challenges as possible. It was here we saw some major issues, which would only get worse as our daily active users increased.
Having a sluggish platform is the easiest way to anger users, and turn people away. So its a problem we needed to tackle immediately. After some investigation, we realised the main culprit to the majority of the performance problems. Without going into too much depth, it was the way TryHackMe stored and managed user progress - this couldn't be fixed by simply adding an index or improving our queries. It was a how the data was stored.
Thankfully, we tore down how we stored users progress data and re-built it up in ( what we think is) the most efficient way. Reducing 10 second queries to 0.3 - a significant change.
Adding more VPN Servers
TryHackMe users can either deploy and control their own Kali Linux machine in their browser (which requires no VPN access) or use a VPN to connect to our network (in order to access machines they deploy).
Another addition to improving performance to our users, was adding multiple VPN servers. We also gave the user the option to choose which server they can connected to, reducing the load on a single server.
Closing Statement
Thank you to everyone who has supported TryHackMe, from our Moderators who manage the ( 7,000 user strong ) Discord community, to people who have signed up and given feedback.
So whats next? We have a lot coming out this year, from interactive network labs to more learning pathways and everything else in between. Its mind blowing that we've reached 50,000 users. Here is until the next 50.
Thanks for reading, Ben (TryHackMe Co-Founder)