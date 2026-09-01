# 🏹 Darker Cat [MEDIUM]

## 📊 Perfil de la Amenaza / Threat Profile
- **Dificultad / Difficulty:** `MEDIUM`
- **Puntos de Misión / Mission Points:** `1078 XP`

## 🎯 Objetivos de Hunting / Hunting Objectives
- Investigate whether any leaked credentials were successfully used to gain access to a PawPressMe system. Identify the entry point and source of the login.
- Reconstruct how the attacker moved from the initial foothold to other machines within the network, particularly Windows workstations. Determine the technique used and which accounts were leveraged.
- Analyse system and network logs for indications that files were staged, compressed, and transferred out of the environment. Correlate any observed exfiltration with claims on the BlackCat leak site.
- Determine how the ransomware payload was deployed across systems. Identify the payload used, delivery method, and file encryption scope.

## 💡 Hipótesis de Investigación / Investigation Hypothesis
> An employee reused a personal password to WatchingCatsLounge.com, which was exposed in a recent credential leak. The attacker used these credentials to access our Linux backup server via SSH. The Splunk Forwarder on that server stopped reporting shortly afterwards. A public leak-site post later confirmed data exfiltration, followed by widespread ransomware deployment across multiple systems. These events suggest the initial access originated from the leaked credentials and led to a broader compromise.

## 🛠️ Detalles del Escenario / Scenario Details
### Crabs On Security

## Pawnd: WatchingCatsLounge Credential Dump Hits Dark Web
_By Ryan Crabs | July 9, 2025_

A new thread on the underground forum `WhiskerLeaks` is drawing attention after a seller known as `Katnip` posted a database of stolen credentials allegedly taken from `WatchingCatsLounge.com`, the internet’s most beloved destination for cat memes and feline forums.

Titled “Meowmix of Access – Real Corporate Emails from WCL Breach”, the post offers over 23,000 email-password pairs, with a sample of 100 lines attached. The data includes a mix of free email providers and corporate domains—primarily from users in creative, media, and tech-adjacent industries.

The asking price? 300 XMR, with limited resale rights and an option for “live chat preview” with the seller.

Crabs On Security examined the sample and found:

* Several entries using corporate email domains.
* Passwords that match common weak credentials or have been seen in previous leaks.
* Metadata suggesting the data was collected in mid to late June 2025, potentially through a credential stuffing campaign or insecure third-party API.

A notable quote from Katnip’s post:

> “Already sold to a buyer. Expect shells soon. Corporate cats don’t rotate passwords.”

Forum responses imply that one buyer may have successfully used the dump for initial access. One reply reads:

> “Tested 10 creds. 1 hit. SSH into something ugly. Pivoting.”

While WatchingCatsLounge itself is not considered critical infrastructure, this dump presents a high risk of credential reuse, particularly for organizations with weak access controls or shared credentials across personal and work systems.

### Por Qué Importa / Why It Matters
Credential reuse remains one of the most consistent ways attackers gain a foothold—especially in flat networks or environments without 2FA. When employee logins from niche websites are recycled on business infrastructure, a minor leak can snowball into a full-blown incident.

Organizations with users known to frequent WatchingCatsLounge (or any hobby community, for that matter) should immediately:

* Review credential hygiene policies.
* Conduct internal checks for account overlaps with the leaked domains.
* Monitor authentication logs for unusual login behavior or brute-force patterns.

This isn’t the first time cats have brought down a network.
But this one might have claws.

## 🛠️ Información de la Empresa / Company Information
## Información de la Empresa / Company Information

PawPressMe is a lean online media company that helps small brands and startups tell their stories through digital content, ebooks, and social media strategy.

From cyber security whitepapers to playful lifestyle campaigns, PawPressMe produces fast-turnaround content that helps clients grow their digital presence.

The company operates with a small creative team, collaborative tools, and a high-volume content pipeline, making speed and flexibility core to its value.

### Empleados / Employees

| Name               | Position                                       | Email                     | Logged-in Host |
|--------------------|------------------------------------------------|---------------------------|----------------|
| Tom Whiskers       | Co-Founder & Content Strategist (Interim IT)   | tom@pawpress.me           | paw-tom        |
| Marie Purrman      | Finance Manager                                | marie@pawpress.me         | paw-marie      |
| Tabitha Clawson    | Copywriter                                     | tabitha@pawpress.me       | paw-tabitha    |
| Leo Meowrell       | Multimedia Editor                              | leo@pawpress.me           | paw-leo        |
| Penny Pawsworth    | Social Media Specialist                        | penny@pawpress.me         | paw-penny      |
| Sally Felina       | Founder & Creative Director                    | sally@pawpress.me         | paw-sally      |

## 🛠️ Inventario de Activos / Asset Inventory
### Red y Subredes / Network and Subnets

| Purpose                   | Range          |
|---------------------------|----------------|
| PawPressMe Corporate LAN  | 10.10.50.0/24  |

### Endpoints y Dispositivos de Red / Endpoints and Network Devices

| Purpose                | Hostname      | Public IP | Internal IP    |
|------------------------|---------------|-----------|----------------|
| Backup Server      | pawbackup  | –         | 10.10.50.5     |

---

**Fuente / Source:** [TryHackMe Threat Hunting Simulator](https://tryhackme.com/threat-hunting-sim)
**Autor del documento / Document author:** Apuromafo
**Fecha de acceso / Access date:** 2026-09-01
