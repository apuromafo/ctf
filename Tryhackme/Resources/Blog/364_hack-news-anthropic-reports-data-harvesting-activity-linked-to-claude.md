# Hack News: Anthropic Reports Data Harvesting Activity Linked to Claude

**ID Original:** no disponible
**Slug:** hack-news-anthropic-reports-data-harvesting-activity-linked-to-claude
--------------------

Anthropic has disclosed that three Chinese AI companies, DeepSeek, Moonshot AI, and MiniMax, conducted coordinated campaigns to systematically extract capabilities from Claude using more than 16 million fraudulent API exchanges. The company described the activity as "industrial-scale campaigns" and published full attribution details alongside a breakdown of the technical methods used.
Source: Anthropic published this disclosure on 24 February 2026 at anthropic.com/news/detecting-and-preventing-distillation-attacks
What happened
Anthropic's security team identified a pattern of API traffic inconsistent with normal usage, characterised by high query volumes concentrated on a narrow set of capabilities, highly repetitive prompt structures, and coordinated account behaviour. After investigation, the company attributed the activity to three separate campaigns, each linked to a named AI laboratory.
All three companies are based in China, where Anthropic does not offer commercial access to Claude due to legal, regulatory, and security risks. To work around regional restrictions, the campaigns used commercial proxy services that resell Claude API access, operating what Anthropic described as a 'hydra cluster' architecture: large networks of fraudulent accounts distributed across the API and third-party cloud platforms. When one account was banned, new accounts took its place. In one case, a single proxy network ran more than 20,000 fraudulent accounts simultaneously, mixing extraction traffic with unrelated requests to complicate detection.
16M+
total exchanges
~24,000
fraudulent accounts
3
campaigns attributed
The three campaigns
Attribution was made using IP address correlation, request metadata, infrastructure indicators, and in some cases corroboration from industry partners who observed the same actors. Each campaign followed a similar approach but targeted different capability areas.
Actor
Scale
Capabilities targeted
DeepSeek
150,000+ exchanges
Reasoning, rubric-based grading, censorship-safe query alternatives
Moonshot AI
3.4M+ exchanges
Agentic reasoning, tool use, coding, computer vision, computer-use agent development
MiniMax
13M+ exchanges
Agentic coding, tool use, and orchestration
Each campaign targeted what Anthropic described as Claude's most differentiated capabilities: agentic reasoning, tool use, and coding. One notable technique observed in the DeepSeek campaign involved prompts that asked Claude to articulate its internal reasoning step by step, effectively generating chain-of-thought training data at scale. DeepSeek also prompted Claude to produce censorship-safe responses to politically sensitive questions, likely to train its own models to redirect similar queries.
The MiniMax campaign was detected while still active. When Anthropic released a new model during the campaign's operation, MiniMax redirected nearly half its traffic to the new system within 24 hours, providing what Anthropic called visibility into a distillation attack across its full life cycle.
What is model distillation, and why does it matter here?
Model distillation is a standard AI training technique. A larger, more capable model (the 'teacher') generates outputs that are used to train a smaller model (the 'student'), allowing the smaller model to approximate the teacher's performance at lower cost. AI companies routinely distil their own models to produce smaller, cheaper variants for deployment.
The problem described here is not distillation itself, but illicit distillation: using a competitor's model as the teacher without authorisation. Anthropic's concern is twofold. First, it is a terms of service violation and a circumvention of export controls designed to prevent advanced AI capabilities from reaching certain jurisdictions. Second, Anthropic argues that models built this way are unlikely to retain the safety controls and refusals built into the original, meaning dangerous capabilities may proliferate with protections removed.
In Anthropic's words: "Illicitly distilled models lack necessary safeguards, creating significant national security risks... dangerous capabilities can proliferate with many protections stripped out entirely."
Anthropic also noted that the scale of distillation attacks requires access to significant compute resources, reinforcing its view that export controls on advanced chips remain relevant — not because they prevent innovation entirely, but because they constrain the scale at which illicit extraction can be carried out.
How the activity was detected
Anthropic described several detection mechanisms that allowed it to identify and attribute the campaigns. The key signals were pattern-based rather than content-based: not what individual prompts asked, but the aggregate structure of traffic across thousands of accounts.
A single prompt requesting structured analytical output may appear legitimate in isolation. The same prompt arriving tens of thousands of times across hundreds of coordinated accounts, all targeting the same capability, constitutes a statistically distinct fingerprint. Anthropic built classifiers and behavioural fingerprinting systems specifically to identify these patterns in API traffic, including detection of chain-of-thought elicitation used to generate reasoning training data.
Supporting signals included synchronised traffic timing and load-balancing patterns between accounts (observed in the DeepSeek campaign), shared payment methods, and infrastructure correlation. In some cases, request metadata was traced to specific researchers at the named laboratories.
The company is now sharing technical indicators with other AI labs, cloud providers, and relevant authorities as part of a broader industry response.
What this means for the security community
This disclosure is notable for several reasons beyond the specific companies named. It represents a detailed public account of API abuse at scale, and the detection methodology described — behavioural fingerprinting, coordinated account clustering, traffic pattern analysis — reflects techniques directly relevant to threat detection and API security more broadly.
A few things worth noting for anyone following threat intelligence or working in security operations:
Proxy services are increasingly weaponised as an abstraction layer for large-scale API abuse, distributing fraudulent traffic across a wide network to eliminate single points of failure and complicate attribution.
Behavioural detection at the API level — looking at request patterns, timing, structure, and metadata rather than just content — is what allowed Anthropic to attribute activity to specific organisations.
The 'hydra cluster' model described here has structural similarities to botnet architectures: distributed, resilient to takedowns, mixing malicious traffic with legitimate requests to reduce signal clarity.
Model outputs as a theft vector is a relatively new category of concern. As AI systems become more capable, the value of their outputs as training data increases, creating incentives for this kind of harvesting at scale.
Google reported a similar pattern in early February 2026, disclosing that it had identified and disrupted distillation and model extraction attempts targeting its Gemini system through more than 100,000 prompts. The pattern appears to be industry-wide.