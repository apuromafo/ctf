# Cyber Security in January 2025

**ID Original:** 679b9d2891ff6400019be4c3
**Slug:** month-in-cyber-january-2025
--------------------

As January comes to a close, we’re hitting the ground running in 2025 with the latest insights and news stories from this month.Let’s dive in!
## New attack exploits popular messaging apps
A newly discovered zero-click de-anonymization attack exposes users' locations on messaging platforms like Signal, Discord, and X (formerly Twitter), raising critical privacy concerns.By exploiting CDN caching mechanisms, attackers can deduce the user’s geographical location based on the data centre delivering the content. Messaging apps like Signal and Discord are particularly vulnerable due to their default notification behaviours. For instance, Signal’s handling of message attachments and Discord’s Nitro emojis can trigger downloads that reveal user locations.The researcher behind the discovery, armed with a tool named "GeoGuesser," demonstrated how this technique could locate individuals, including high-profile targets, with alarming accuracy. Despite these findings, responses from platforms and CDN providers like Cloudflare have been criticised as insufficient. While Cloudflare has patched some vulnerabilities, the attack remains viable by exploiting underlying design flaws.
## TorNet backdoor exploits Windows tasks to deliver malware
Since mid-2024, a financially motivated threat actor has been targeting users in Poland and Germany with a sophisticated malware campaign, distributing a variety of payloads, including the newly discovered TorNet backdoor. Delivered via phishing emails posing as financial or logistics organisations, this malware leverages Windows Scheduled Tasks for persistence and advanced evasion techniques.The attack begins with phishing emails containing malicious attachments compressed in .tgz format. Once extracted, a .NET loader installs PureCrypter malware, which decrypts and delivers the final payload, often the TorNet backdoor. PureCrypter employs AES encryption and anti-analysis methods to avoid detection, disconnecting victims from their networks during installation to bypass real-time security tools.The TorNet backdoor uses the TOR network for stealthy command-and-control (C2) communications, routing all traffic through anonymised TOR SocksPorts. It maintains persistence by exploiting Windows Task Scheduler, creating tasks that run frequently and even under low battery conditions. Memory-only execution and encrypted task names further complicate detection.
## Vulnerabilities in telecom networks let hackers gain access to 3,000 companies
Researchers have uncovered critical security flaws in a telecom network that compromised over 3,000 companies, exposing sensitive data and administrative controls. Exploiting backend API vulnerabilities and weak authentication systems, attackers gained unauthorised access to customer invoices, employee documents, and even real fingerprints.The attack began with path traversal techniques that bypassed Web Application Firewall protections, leading to internal APIs and microservices. A vulnerable endpoint revealed sensitive employee data and customer information. Exploiting poor backend security practices, attackers bypassed KYC checks, enabling SIM swaps and unauthorised access to critical services like SMS-based 2FA.The researchers also identified a super admin panel that gained control of all subsidiaries through brute-force attacks and POST request vulnerabilities. This panel granted access to alter passwords, IDs, and sensitive organisational data.
## DeepSeek limits new users due to malicious attacks
DeepSeek, the fast-growing Chinese AI startup, announced on Monday that it would temporarily limit new user registrations due to large-scale malicious attacks targeting its services. Existing users, however, can continue accessing the platform.This announcement comes just after DeepSeek overtook OpenAI’s ChatGPT as the most downloaded free app on Apple’s App Store. The company’s rise has been fast since its founding in 2023, driven by its open-source R1 reasoning model, released last week. This model, praised for its advanced reasoning capabilities, rivals offerings from OpenAI and Google and was developed at a fraction of their costs.Despite challenges posed by U.S. chip export restrictions, DeepSeek has captured significant attention, sparking concerns among tech giants about falling behind in the competitive AI landscape.
## Sophos reveals two ransomware campaigns exploiting Microsoft Teams vulnerabilities
Sophos researchers have uncovered two ransomware campaigns, STAC5143 and STAC5777, exploiting Microsoft Teams to infiltrate organisations. By leveraging Teams’ default settings, which allow external users to initiate chats or calls, attackers gain unauthorised access and deploy malware.
## Key Attack Methods
1. Victims are overwhelmed with spam emails to disrupt their workflow.2. Attackers impersonate IT support and initiate Teams voice calls.3. Using Microsoft Quick Assist or Teams’ remote control feature, attackers guide victims to unknowingly install malicious software.4. Once access is gained, malicious payloads are executed.
## STAC5143 Campaign
This operation uses Java Archive (JAR) files and Python-based backdoors, including an obfuscated RPivot reverse proxy tool, to maintain stealthy access. It connects to command-and-control (C2) servers via port 80, blending in with regular HTTP traffic.
## STAC5777 Campaign
STAC5777 utilises legitimate software to mask its activity, such as side-loading a malicious DLL through Microsoft OneDrive’s updater. The malware disables security measures, modifies the registry, and spreads laterally across networks via SMB scanning. In one case, it attempted to deploy Black Basta ransomware, which was blocked by Sophos endpoint protection.
## Impacted Systems
The malware can:
* Collect system and OS details
* Log keystrokes and capture credentials
* Perform lateral movement and exfiltrate sensitive data
* Attempt to disable Multi-Factor Authentication (MFA) and security tools
## Mitigation Measures
Organisations are advised to:
* Restrict Teams calls from external users
* Limit or disable remote access tools like Quick Assist
* Implement application controls to prevent unauthorised software execution
* Integrate Microsoft Office 365 with security monitoring solutions for enhanced visibilityThat’s all from us this month! Check back again next month for our next monthly roundup of cyber security news.