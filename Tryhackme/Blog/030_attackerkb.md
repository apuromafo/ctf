# AttackerKB - Not All Vulns Are Created Equal

**ID Original:** 60e84cd565e4000001040869
**Slug:** attackerkb
--------------------

[AttackerKB is a community-based tool](https://attackerkb.com/?referrer=thm&ref=blog.tryhackme.com) users can leverage to search vulnerabilities - which are rated through the use of assessments performed by the community. We will discuss this tool and a [newly launched TryHackMe room](https://tryhackme.com/room/attackerkb?ref=blog.tryhackme.com), made in collaboration with AttackerKB, DarkStar7471 and Rapid7. Having been involved with the room creation and participating in the private beta of the website, I invite you on a journey to discover how to implement AttackerKB in the best way possible; to introduce it to your workflow and to see how to gain the best results from its use.
## What is AttackerKB?
Let’s explore why you would want AKB to be part of your daily life. In order to do so, we will cover what this tool does. AttackerKB - not all vulns are created equal.This slogan says it all, [AttackerKB ](https://attackerkb.com/?referrer=thm&ref=blog.tryhackme.com)is a tool on which you can search vulnerabilities - which are all rated thanks to assessments performed by the community.Here are key points:
* It is community-based
* It is in constant development and improvement
* It features up-to-date CVE database
* CVEs assessments and ratings are provided by other users such as pentesters, researchersAttackerKB homepageAfter going to the [AttackerKB website](https://attackerkb.com/?referrer=thm&ref=blog.tryhackme.com), you have access to the most active and popular CVEs. You can also search for one using the search bar, entering its code (CVE-XXXX-XXXX) - or by searching for keywords, or the product/system related to the vulnerability.What makes AKB a really powerful tool is the diversity and relevance of the information provided on each CVE on their respective pages.From assessments made about it, to a rating system with information such as the Attacker Value and Exploitability.Some of the ratings of the Bluekeep CVE.You can also find - where applicable - the Metasploit modules, MITRE ratings, and lots of resources/references where the CVE has been mentioned on other websites.Vulnerability details from CVE-2020-25592You will also find on some CVE an official Rapid7 Analysis such as the following one.Rapid7 Analysis from CVE-2020-25592
## But wait, there's more!
You have a scoreboard system with user scores. To get points, you need to make assessments or reply to one, and the more people who upvote your assessment (or comment), the more points you score!This goes along with cool badges:
## Okay okay, now, how do I make the best out of AKB?
After enumeration, it is recommended to search terms on AKB such as services names and versions. After some more searching (hello Google,) if you find a CVE online that seems to fit your case, search for it on AKB. A lot of useful CVEs are not well documented, or documentations/blog articles are hard to find.This is what AKB is for!I have also made a tool called AttackerKB-Explorer which provides a basic CLI (Command-Line Interface) to AttackerKB using their API.(Note: It's not always up-to-date and well maintained)
* My CLI tool: [https://github.com/horshark/akb-explorer](https://github.com/horshark/akb-explorer?ref=blog.tryhackme.com)
* KevTheHermit's incredible python wrapper [https://github.com/kevthehermit/attackerkb-api](https://github.com/kevthehermit/attackerkb-api?ref=blog.tryhackme.com)