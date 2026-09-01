# You Can Govern AI Without Killing Coding Velocity: Key Takeaways From Our Live Session

**ID Original:** no disponible
**Slug:** you-can-govern-ai-withouth-killing-coding-velocity
--------------------

Last week we hosted a webinar to discuss a topic we know is keeping many of the cyber security leaders in our community up at night. AI tools in development are unavoidable, but the choice isn’t actually between all-out bans or an unmonitored free-for-all.
Sonya Moisset (Staff AI Security Advocate at Snyk), and Max Robertson (Senior Content Engineer at TryHackMe) joined Vlad Boldura (Senior Manager, Content Engineering at TryHackMe) to share practical perspectives on governing AI-assisted development without slowing teams down.
As our guests discussed, the key is a purposeful and realistic approach to governance that engages teams outside of the SOC and embraces education.
Here are our key takeaways.
Shadow AI is a governance gap
Shadow AI looks less dramatic than the name implies. It’s a coding assistant that isn't on the approved list, a browser plugin, a SaaS tool processing internal data outside your enterprise plan. The root cause of Shadow AI isn't bad intent, it’s the gap between genuinely useful tools  and an approach to governance that hasn't caught up to their usage.
There’s no blocking Shadow AI. The organization will always find ways to circumvent it.
Leaders will have much more success preventing the risks associated with Shadow AI by asking pragmatic questions:
Is AI being used across workflows? If so, which ones?
What data is it touching?
What does appropriate oversight look like at this point?
Oversight doesn't have to mean friction. It starts with visibility, understanding which AI tools are active across your environment, which models are connected to which data, and where outputs are feeding into business decisions.
Tools like an AI Bill of Materials (AI BOM) give you that inventory.
AI Security Posture Management (AISPM) platforms layer continuous monitoring on top of it.
From there, oversight becomes operational: approved tools lists that give developers a sanctioned path rather than a reason to go around you, security requirements embedded in development workflows rather than bolted on at the end, and human approval gates on any action that's destructive or irreversible.
None of that effort requires slowing development down. But it does require deliberately deciding where the guardrails go.
Horror stories can be lessons learned
The speakers chatted about the consequences of the governance gap. Though each had a different context of tools and teams, each demonstrated why ignoring the gap wasn’t an option.
Production database wiped by an AI agent
A developer asked an AI coding tool to clean up some code. It deleted the production database. No rollback existed. Basic environment separation of development versus production only got implemented after the incident went public.
An agent that ignored "stop"
A researcher ran an AI agent with a prompt to clean up her inbox. It began mass-deleting emails. She told it to stop. It kept going and had already queued the actions. Human approval gates for destructive, irreversible operations should be a priority
A skills marketplace became an attack surface.
A few weeks after a popular AI coding tool launched a plugin marketplaces, researchers showed that weaponized skills with convincing names could exfiltrate credentials and API keys. This followed the same pattern as malicious npm packages, with an AI wrapper.
Two new attack vectors worth knowing by name
The tools your developers use to ship faster are the same tools being used offensively. The speakers discussed two new threat patterns that are already out there, and which every cyber team should be aware of:
Slop squatting
AI models sometimes suggest installing packages that don't exist. Attackers register those hallucinated package names in public registries with malicious code and wait. A fake JavaScript package accumulated over 200 downloads this way before anyone flagged it.
AI-orchestrated cyberattacks
In late 2024, Anthropic documented the first known AI-orchestrated espionage campaign: a threat actor used an AI coding tool to direct multiple agents through the full attack lifecycle (reconnaissance, exploitation, exfiltration) with human operators only checking in at key decision points. 80–90% was autonomous.
Controls that reduce risk and support velocity
The good news is that the security fundamentals relevant to governance are not new. It’s just a question of applying them to AI-assisted workflows.
Prompt-level
Security requirements don't appear in AI-generated code unless they're in the instructions. Teams that build security standards into prompt templates get better output from the start rather than reviewing for gaps at the end.
Architecture-level
Agents shouldn't have direct production access. Destructive actions like database changes, mass deletions, and privilege modifications  need explicit human approval. Sandbox environments and network segmentation apply here for the same reasons they apply everywhere.
Supply chain
An AI Bill of Materials (AI BOM) gives you an inventory of every component in your AI systems: models, datasets, APIs, plugins, infrastructure. Pair it with an AI Security Posture Management (AISPM) platform for continuous monitoring rather than periodic audits.
Workflow-level
Security scanning can be embedded directly into the development loop so that every code change triggers an automatic scan and flags issues inline without a separate review step or friction added to the developer workflow. This is what non-blocking security governance looks like in practice.
Context windows
A practical limitation that rarely comes up in governance discussions is AI models losing context as sessions get longer, and hallucinations increase as a result. A model given security requirements at the start of a long session may not be applying them consistently by hour three. This is why it’s so crucial that security constraints need to be reinforced throughout a workflow.
The organizational levers that work
AI security champions in teams
Practitioners embedded within engineering,  and extended to finance, HR, marketing, who understand both the tools and the risks change behavior more effectively than any policy document. They're present when decisions get made, not reviewing outputs afterward.
💡 To support this shift, TryHackMe recently launched the SEC0 certification , perfectly geared for non-technical professionals.
An approved tools list with clear rationale
Developers need a clear path, and security teams need the visibility that comes with one.
Policy embedded in the development environment
Encoding security requirements, compliance constraints, and architectural standards in specification files that agents treat as a source of truth moves security left in a way that's hard to bypass. Compliance requirements like FedRAMP, NIST, and others can be expressed here and applied automatically throughout development.
Where we’re going
Agentic AI is where the security stakes are highest and frameworks are still catching up. OWASP published a dedicated Agentic AI security framework in December 2024, separate from its LLM Top 10, which signals how distinct the risk surface has become. The Anthropic case is likely a preview, not an outlier.
The organizations building governance capability like visibility tooling, champion programs, and embedded controls now, will be better positioned than those waiting for a forcing event.
If this conversation resonated and you're thinking about how to strengthen cybersecurity capability across your teams, see how TryHackMe helps organizations build real-world security skills through hands-on simulation s.

## Multimedia

[Video embebido / Embedded video](https://www.loom.com/embed/9385770ff2e7466cb457e0d5f1cd49a3)

[Video embebido / Embedded video](https://www.loom.com/embed/25cbb91cf9e14afa930edb99e5e7c02a)

[Video embebido / Embedded video](https://www.loom.com/embed/cbee78afd1fb4e9db79b09869ef52c5c)

[Video embebido / Embedded video](https://www.loom.com/embed/593156e116df4612b959fbbfe1007b76)

---
**Fuente / Source:** [you-can-govern-ai-withouth-killing-coding-velocity](https://tryhackme.com/resources/blog/you-can-govern-ai-withouth-killing-coding-velocity)
