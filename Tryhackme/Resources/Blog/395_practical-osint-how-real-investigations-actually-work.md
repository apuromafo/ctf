# Practical OSINT: How Real Investigations Actually Work

**ID Original:** no disponible
**Slug:** practical-osint-how-real-investigations-actually-work
--------------------

OSINT (open-source intelligence) is one of the most misunderstood disciplines in cyber security. Most introductions focus on the tools: Shodan, Maltego, reverse image search, WHOIS lookups. The tools matter, but they are not the investigation. What separates a productive OSINT analyst from someone just running searches is methodology: knowing what question you are trying to answer , choosing the right source, and understanding how to connect fragments of public information into something actionable.
The four case studies below are representative of how real OSINT investigations actually unfold - the kind of work done by threat intelligence analysts, security researchers, investigative journalists, and law enforcement. Each illustrates a different investigation type, the techniques that work, and where learners can build the same skills on TryHackMe.
Case study 01 Geolocating a threat actor's operational photo
In 2022, Bellingcat researchers geolocated the precise position of a military unit from a single photograph posted to a Telegram channel. The image showed soldiers with no visible landmarks — but a distinctive shadow angle, partial road markings, and a tree line on the horizon. By cross-referencing Google Earth time-lapse imagery and sun position calculators, analysts placed the photo within a 200-metre area.
This type of geolocation analysis is now a standard technique in conflict intelligence. The core skill is learning to read images not for what is obvious, but for what is incidentally present — utility pole spacing, road surface type, vegetation patterns, building construction styles, and shadow geometry are all sources of locational data.
Tools used: Google Earth • SunCalc • Bellingcat's geolocation guides
Key takeaway Even an image stripped of EXIF metadata tells a geolocation story. Training your eye to read environmental context is a skill built through practice, not theory.
Practise this on TryHackMe: Geolocating Images
Case study 02 Attributing a phishing infrastructure to a threat actor
When a security team identifies a phishing domain, the investigation rarely stops at the URL. The goal is attribution: who registered this? What else do they operate? A typical pivot chain starts with a WHOIS lookup on the domain — even where registration details are redacted, the registrar, nameservers, and creation timestamp are often visible.
From there, analysts query Shodan for the IP address hosting the domain, examining open ports, TLS certificate details, and whether the same certificate is used across other infrastructure. Certificate transparency logs frequently reveal previously unknown domains operated by the same actor. A single phishing campaign can unravel into a network of dozens of related domains — all from one initial pivot.
In the 2016 DNC breach investigation, OSINT researchers traced a malicious domain registration to infrastructure previously linked to APT28 through exactly this kind of certificate and registrar chaining — well before the formal attribution statement from the US government.
Tools used: Shodan • VirusTotal • crt.sh • WHOIS lookup
Key takeaway Infrastructure leaves traces across certificate logs, passive DNS records, and hosting patterns. Attribution is rarely certain from a single source — it is built from convergent evidence across multiple independent pivots.
Practise this on TryHackMe: Shodan • OhSINT • Threat Intelligence Tools
Case study 03 Investigating an online persona across platforms
Threat actors rarely maintain perfect operational security. A username chosen for a hacking forum in 2015 often reappears on a gaming platform, a GitHub account, or a Stack Overflow profile. A small slip — using the same avatar, referencing the same hometown, or posting at a consistent time that implies a specific timezone — can connect accounts that were meant to be unrelated.
This cross-platform persona investigation is a core OSINT technique in fraud analysis, insider threat cases, and threat actor profiling. The methodology involves selecting a seed identifier (a username, email address, or profile image), querying it systematically across platforms using tools like Sherlock or Holehe for username enumeration, and building a relationship map of connected accounts.
Analysts document the pivot chain carefully: each connection needs a source. 'Same username' is a weak signal. 'Same username, same profile photo, same writing style, posts referencing the same local sports team' is a significantly stronger one. OSINT investigations in this category are about building convergent evidence, not relying on any single data point.
Tools used: Sherlock • Holehe • Maltego
Key takeaway Operational security failures are cumulative. Investigators look for the intersection of multiple weak signals, not a single smoking gun. The more independently a connection can be verified, the stronger the attribution.
Practise this on TryHackMe: OhSINT • Sock Puppets • Maltego
Case study 04 Mapping a shell company network
When the OCCRP and ICIJ published the Panama Papers investigation, the underlying methodology was OSINT applied to corporate registry data at scale. Public company registrations, beneficial ownership filings, and director records — all publicly available — were cross-referenced to expose networks of shell companies obscuring the movement of illicit funds.
Financial OSINT follows a similar pattern to infrastructure attribution: you start with one entity and pivot outward. A company name leads to a registered address, which appears in three other company filings. A director appears in the registries of seven jurisdictions. A phone number submitted in one filing reappears in a sanctions database.
Sanctions evasion investigations frequently use maritime tracking data alongside corporate registries — vessels routed through intermediary ports, or registered under flag-of-convenience states, tell a story when overlaid with publicly available sanctions lists and AIS tracking records.
Tools used: OpenCorporates • OCCRP Aleph • MarineTraffic • Maltego
Key takeaway Public registries are a goldmine. In many jurisdictions, company formation, director appointments, and filing history are all publicly searchable. The skill is in the pivoting — finding the thread that connects one entity to the next.
Practise this on TryHackMe: Web OSINT • Maltego
What these cases have in common
Across all four investigation types, the same underlying pattern holds. OSINT is not a single-tool operation. It is an iterative process of asking a question, identifying the most reliable public source that could answer it, following the pivot that source opens, and documenting every step.
The methodology in practice:
Start with a seed: a domain, username, image, company name, or IP address
Identify what public data sources could contain that seed
Query those sources, note what you find, and identify the next pivot point
Build a documented chain of connections, noting the strength of each link
Stop when you have answered the question - or when further pivots would require non-public data
The discipline of documenting as you go is what separates professional OSINT from casual Googling. An investigation that cannot show its reasoning is not actionable. Bellingcat's guides are the closest thing to a public-facing methodology reference the OSINT community has.
Build these skills on TryHackMe
The OSINT module on TryHackMe covers the tools and techniques from all four case study types - image geolocation, infrastructure pivoting, persona investigation, and web footprinting - in browser-based labs with no local setup needed.