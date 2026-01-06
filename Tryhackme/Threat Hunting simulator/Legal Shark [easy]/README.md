# 🏹 Threat Hunting: Legal Shark [EASY]

## 📊 Perfil de la Amenaza
- **Dificultad:** `EASY`
- **Puntos de Misión:** `1102 XP`

## 🎯 Objetivos de Hunting
- Investigate how the attacker initially gained a foothold in the TrySueMe network. Identify the method of delivery and execution of the malicious file.
- Determine how the attacker established remote access. Identify the tool used for command and control and the means of persistence.
- Trace the attacker’s activity within the environment. Document any evidence of lateral movement to file shares or access to sensitive legal documents.
- Analyse system and network logs for indications of data staging or attempted exfiltration. Assess whether client data was successfully transferred out of the network.

## 💡 Hipótesis de Investigación
> Threat actor FIN7 has compromised the environment. Following initial infection via a malicious loader, the actor deployed NetSupport RAT to establish remote access. Using this access, the attacker is believed to have moved laterally to internal file shares, browsed sensitive legal documents, and ultimately exfiltrated client data to external infrastructure over the RAT’s encrypted channel.

## 🛠️ Executive Summary
**Subject:** FIN7 (a.k.a. Carbanak, Navigator Group, Sangria Tempest) Expands Targeting Beyond Financial Sector

**From:** National Cybersecurity Coordination Centre (NCCC)

**To:** Legal Services, Professional Services, and Critical Industry Sectors

The threat group FIN7 (also known as Carbanak, Navigator Group, Sangria Tempest) has been observed adjusting its operations and expanding beyond its usual focus on banks, retail, and hospitality. Recent reporting highlights an increased interest in professional services, including legal practices, with the aim of long-term access to business-sensitive data.

FIN7 is known for its flexibility: it can combine custom tools with legitimate software already present in corporate environments, often making it difficult for defenders to quickly separate malicious from routine activity.

## 🛠️ Emerging TTPs
* Initial Access: User-targeted approaches remain a likely vector, often leveraging email or other everyday communication methods.
* Establishing Presence: Intruders may employ lightweight scripts or automation frameworks that blend into normal IT workflows.
* Persistence: Some observations suggest reliance on scheduled tasks, registry changes, or startup scripts — methods that can be overlooked in routine monitoring.
* Tooling Choices: Reports indicate a preference for repurposing legitimate software (remote access, management, or monitoring utilities) in ways that obscure malicious intent.
* Lateral Exploration: Once inside, FIN7 has demonstrated interest in enumerating networks and identifying high-value systems (such as file servers or domain controllers).
* Data Targeting: Internal document repositories, client data, and legal records remain attractive objectives.
* Evasion Techniques: Use of encryption, obfuscation, or tunneling over common protocols to blend exfiltration with legitimate traffic.
* Adversary Agility: FIN7 adapts rapidly, shifting tools and tradecraft once defenders harden against known patterns.
* Infrastructure Use: Campaigns may involve rotating domains, bulletproof hosting, or cloud-based infrastructure to sustain operations.

## 🛠️ Recommendations
Organizations across the **legal, financial, and professional services sectors** are encouraged to:

1. Monitoring for unusual script or command-line behavior.
2. Reviewing baseline usage of remote management or administration tools.
3. Reinforcing user awareness to reduce the effectiveness of social engineering.
4. Validating permissions and access to sensitive document repositories.
5. Ensuring logging and visibility for persistence attempts and scheduled jobs.

## 🛠️ Company Information
TrySueMe is a fast-moving legal and consulting practice where ambition meets advocacy. Whether you're navigating the grey zones of corporate compliance, restructuring your business strategy, or pursuing justice with conviction, we believe that confidence comes from clarity, not ceremony.

Led by the indomitable Sue Hastings, senior attorney and founder, TrySueMe is about liberation from uncertainty. We combine deep legal insight with modern consultancy flair to empower individuals and small businesses to take bold action. No jargon. No fluff. Just real solutions with a personal touch.

Try standing up for your rights. Try thinking two steps ahead. Try calling Sue.

## 🛠️ Asset Inventory
### Servers

| purpose | hostname | IP |
| --- | --- | --- |
| DC | TSM-DC01 | 10.100.2.1 |
| VPN | - | 10.100.2.254 |
| FileShare | TSM-FS01 | 10.100.2.9 |
| Splunk | TSM-SPLUNK | 10.100.2.5 |
| Web Proxy | TSM-PROXY | 10.100.2.250 |

### Workstations

| User | Hostname | IP |
| --- | --- | --- |
| Sue | WRK-SUE | 10.100.2.21 |
| Mark | WRK-MARK | 10.100.2.22 |
| Tara | WRK-TARA | 10.100.2.23 |
| Paralegal | WRK-PARA | 10.100.2.24 |
| Greg | WRK-GREG | 10.100.2.100 |
| Reception | WRK-RECEPTION | 10.100.2.29 |
| Intern | WRK-INTERN | 10.100.2.30 |
