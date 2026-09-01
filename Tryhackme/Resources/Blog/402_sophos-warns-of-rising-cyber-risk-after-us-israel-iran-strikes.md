# Sophos Warns of Rising Cyber Risk After US-Israel-Iran Strikes

**ID Original:** no disponible
**Slug:** sophos-warns-of-rising-cyber-risk-after-us-israel-iran-strikes
--------------------

DEVELOPING SITUATION This is a developing situation. Intelligence reflects reporting as of 4 March 2026.
Cybersecurity firm Sophos has published a formal cyber advisory warning organisations in the United States, Israel, and allied regions of elevated cyber risk following the joint US-Israeli military strikes on Iran on 28 February 2026. The operations, designated Operation Epic Fury by the US and Operation Roaring Lion by Israel, targeted Iranian military infrastructure, nuclear sites, and senior leadership. Iran's Supreme Leader, Ayatollah Ali Khamenei, was confirmed killed in the strikes. Iran has launched retaliatory missile and drone barrages across the region in the days since.
Within hours of the initial strikes, Sophos X-Ops and Unit 42 researchers at Palo Alto Networks observed a rapid surge in activity from Iran-aligned hacktivist groups across Telegram, X, and underground forums. Sophos's companion hacktivist activity report , published 2 March 2026, documents over 60 individual threat groups mobilising, with activity skewing toward website defacement, distributed denial-of-service attacks, and credential-based intrusions.
60+
hacktivist groups active as of 2 March 2026
150+
hacktivist incidents recorded in 72 hours
~1%
Iranian internet connectivity after strikes
Sources: Sophos X-Ops, Unit 42, CloudSEK. Figures as of 2 March 2026.
What happened on 28 February
The strikes targeted military installations, IRGC facilities, and nuclear infrastructure across multiple Iranian cities including Tehran, Isfahan, Qom, Karaj, and Kermanshah. Reports from Israeli and US media indicate simultaneous cyber operations caused widespread disruption to Iranian state media, communications infrastructure, and financial systems. Internet monitoring organisations Netblocks and Cloudflare recorded Iranian national connectivity collapsing to between 1% and 4% of normal levels in the immediate aftermath.
That near-total connectivity loss has a dual effect on the threat landscape. Unit 42 assesses that the degradation of Iranian command structures and internet access will likely limit the near-term capability of state-sponsored groups to coordinate sophisticated attacks from within Iran. However, proxy actors, diaspora groups, and ideologically motivated hacktivists operating outside Iranian borders face no such constraint, and their activity has risen sharply.
Key threat actors identified
Sophos X-Ops and Unit 42 have identified the following groups as active or escalating since the strikes:
Threat actor
Affiliation
Observed or claimed activity
Handala Hack
MOIS-linked persona (COBALT MYSTIQUE)
Claimed attacks in Jordan, launched 'RedWanted' site listing Israeli supporters, threatened broader regional targets. Capable of data theft and wiper deployment despite history of overstating impact.
APT Iran
Pro-Iranian hacktivist collective
Hack-and-leak operations. Claimed responsibility for sabotage of Jordanian critical infrastructure. Active on Telegram encouraging coordinated retaliation.
Cyber Islamic Resistance
Pro-Iranian umbrella group
Coordinates multiple teams including RipperSec and Cyb3rDrag0nzz for synchronised DDoS, data-wiping, and website defacement against Israeli and Western infrastructure.
NoName057(16)
Pro-Russian hacktivist group
Claimed multiple Israeli targets including municipal, political, telecoms, and defence-related entities. Assessed as state-aligned but independently operating.
HomeLandJustice
Iran-linked persona
Previously linked to wiper and data-leak operations against Albanian government entities since 2022. Flagged by Sophos as a historically capable actor.
Sophos note: While some Iranian military and intelligence-linked groups have historically overstated operational success, they remain capable actors. Documented activity has included data theft, ransomware deployment, wiper malware, and public release of stolen information.
Attack types assessed as most likely
Based on historical Iran-linked campaigns and current observed activity, Sophos and Unit 42 assess the following tactics as most probable against US and Israeli-affiliated targets:
Tactic
Detail
Website defacement
Low-sophistication, high-visibility. Already observed against dozens of Israeli and regional targets within hours of the strikes.
DDoS
CrowdStrike confirmed reconnaissance and DDoS initiation consistent with Iranian-aligned actors by 1 March 2026. Often precedes more damaging operations.
Phishing and password spraying
Credential-based access remains a core Iranian TTP. CISA has previously warned of Iranian actors targeting exposed services and default credentials.
Hack-and-leak
Stolen data published publicly for psychological and reputational impact. Handala and APT Iran both use this model.
Wiper malware
Deployed selectively for destructive effect. Handala has demonstrated this capability, though not yet confirmed in the current escalation window.
Mobile spyware
Unit 42 identified an active phishing campaign distributing a malicious replica of the Israeli Home Front Command RedAlert app targeting Android devices.
Who is at elevated risk
Sophos identifies the primary at-risk population as organisations with US or Israeli affiliation, including commercial suppliers, defence-adjacent contractors, and civilian infrastructure operators. Gulf Cooperation Council states are also assessed as likely targets given Iranian retaliatory missile activity in the region. The CISA advisory library on Iranian threats provides additional sector-specific guidance.
Sectors most commonly targeted in historical Iran-linked campaigns include energy, critical infrastructure, finance, telecoms, and healthcare. Organisations in these sectors with internet-facing systems, default credentials, or unpatched VPN appliances are particularly exposed to opportunistic intrusion attempts.
US angle: While Iranian hacktivist focus has concentrated on Israeli targets, the US role in the strikes substantially raises the risk to US-affiliated organisations. CrowdStrike head of counter adversary operations Adam Meyers noted that behaviours observed are consistent with preparations that, in past conflicts, have preceded more aggressive operations.
Recommended defensive posture
Sophos recommends organisations take the following actions immediately:
Tactic
Detail
Patch internet-facing systems
Prioritise VPN appliances, remote access gateways, and web-facing services. Iranian actors routinely exploit known CVEs in these categories.
Enforce MFA universally
Credential-based access is the dominant Iranian entry point. MFA stops credential theft from translating into account compromise.
Review and test incident response plans
Specifically rehearse scenarios involving wiper malware and destructive payloads. Backup integrity is critical.
Monitor for DDoS pre-indicators
Elevated reconnaissance, port scanning, and connection probing may precede DDoS or intrusion attempts. Baseline your traffic now.
Watch for phishing uplift
Spearphishing tied to geopolitical events is a reliable Iranian TTP. Warn staff and increase scrutiny of credential-harvesting lures.
Verify backup and recovery
Wiper malware is designed to be unrecoverable. Offline backups tested recently are your primary defence if destructive payloads deploy.
Build your threat intelligence skills on TryHackMe
Understanding how to read and respond to advisories like this is a core skill for SOC analysts and threat intelligence roles. The following TryHackMe rooms cover the relevant techniques.

---
**Fuente / Source:** [sophos-warns-of-rising-cyber-risk-after-us-israel-iran-strikes](https://tryhackme.com/resources/blog/sophos-warns-of-rising-cyber-risk-after-us-israel-iran-strikes)
