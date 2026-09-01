# 🏹 Chasing APT28 Shadows [HARD]

## 📊 Perfil de la Amenaza / Threat Profile
- **Dificultad / Difficulty:** `HARD`
- **Puntos de Misión / Mission Points:** `1000 XP`

## 🎯 Objetivos de Hunting / Hunting Objectives
- Detect initial access and execution techniques associated with APT28 activity.
- Investigate persistence mechanisms and privilege escalation methonds leveraged by APT28.
- Analyse a variety of log sources to detect anomalies in Windows environment.

## 💡 Hipótesis de Investigación / Investigation Hypothesis
> Threat actors gained initial access to the Dev-QA Windows Server via a targeted phishing campaign on or before December 7, 2024. 
Once inside the environment, they may have performed reconnaissance and established persistence, which requires verification from the threat hunter side. 
In addition, they discovered insecure credential storage, located Bob Martin’s plaintext AWS credentials, stole those credentials, and subsequently used them to access our AWS infrastructure.

## 🛠️ Detalles del Escenario / Scenario Details
## Background


Here at TryGovMe, we and our partners are constantly under attacks by various threat groups, especially by APT28, who is trying to reach our national database in AWS. This case, however, is particularly concerning to us.

Two days ago, another government agency was breached and shared a list of attack indicators with us, some matching APT28. Our cloud team checked the IoCs across our AWS log sources, got a match, and eventually discovered an unauthorized login for the user bmartin@trygovme.thm dated December 7th, 2024.

Although our cloud team immediately contained and secured the affected AWS resources, a critical question remains open: How did the bmartin@trygovme.thm credentials get leaked in the first place?
From what we know now, Bob Martin is a QA engineer hired to test our new web app. He confirms using Dev-QA Windows Server for his day-to-day work and even admitted to storing his AWS credentials in plain text, so likely the attack originated from there. 

Your mission as a Threat Hunting analyst is to conduct an investigation across the on-premises environment and attempt to identify potential anomalies.


## Objetivos / Objectives
- Detect initial access and execution techniques associated with APT28 activity;
- Investigate persistence mechanisms and privilege escalation methods leveraged by APT28;
- Analyse a variety of log sources to detect anomalies in Windows environments.

## Referencias / References
- [APT28 Inception Theory TryHackMe room](https://tryhackme.com/room/apt28inceptiontheory)
- [APT28 Overview FireEye Report](https://services.google.com/fh/files/misc/apt28-window-russia-cyber-espionage-operations.pdf)
- [APT28 Unit42 Reports](https://unit42.paloaltonetworks.com/russian-apt-fighting-ursa-exploits-cve-2023-233397/)
- [APT28 MITRE](https://attack.mitre.org/groups/G0007/)

## 🛠️ IOCs
## Lista de Indicadores de Compromiso / Indicator of Compromise List


We received a list of IOCs from other affected government agencies. This information may support you during your investigation.


####  Host Based:

**File Names:**

- lncstnt.exe
- Office.exe
- msoutlook.dll

**Hashes:**

- 5086989639aed17227b8d6b041ef3163
- ef8b5fbd87b30d97225860f1a918b057
- 46e2957e699fae6de1a212dd98ba4e2bb969497d

#### Network Based:

**IP Addresses:**

- 185.183.107.40
- 94.177.12.150
- 169.239.129.121

## 🛠️ Información de la Empresa / Company Information
## Información de la Empresa / Company Information
TryGovMe is a government-affiliated research division specialising in the development of intelligent IoT and robotics solutions 
for national energy resilience. As part of a broader state initiative to modernise and secure critical infrastructure, 
TryGovMe designs and deploys autonomous systems, known as smart grid bots, that can monitor, maintain, and self-heal components of the national power grid. We stand out by combining robotics, secure data systems, and edge computing to help build a safer and more sustainable energy network.

## Estructura de la Empresa / Company Structure

### Employees
| Name             | Department                        | Email                         | Logged-in Host | Workstation IP   |
|------------------|-----------------------------------|-------------------------------|----------------|------------------|
| James Foster     | Director of Energy Robotics Research | jfoster@trygovme.thm         | HOST01         | 10.10.219.10     |
| Ella Thompson    | Lead IoT Infrastructure Engineer  | ethompson@trygovme.thm        | HOST02         | 10.10.219.11     |
| Tom Barry        | DevOps                            | tbarry@trygovme.thm           | HOST03         | 10.10.219.12     |
| Bob Martin       | QA Engineer                       | bmartin@trygovme.thm          | HOST04         | 10.10.219.13     |
| Sophie Reynolds  | OT Systems Administrator          | sreynolds@trygovme.thm        | HOST05         | 10.10.219.14     |
| Daniel Morgan    | Sensor Integration Specialist     | dmorgan@trygovme.thm          | HOST06         | 10.10.219.15     |
| Olivia Bennett   | Energy Systems Data Analyst       | obennett@trygovme.thm         | HOST07         | 10.10.219.16     |

## Servidores / Servers
| Purpose         | Hostname        | IP Address     |
|------------------|-----------------|----------------|
| Product Server   | Dev-Server      | 10.10.219.50   |
| QA Server        | Dev-QA-Server   | 10.10.219.40   |
| Web Server       | Web-Server   | 10.10.219.129    |

## 🛠️ Diagrama de Red / Network Diagram
#### Below is a diagram illustrating the network architecture of the TryGovMe.


![](https://tryhackme-images.s3.amazonaws.com/user-uploads/674d9727a22822c1eb46cb31/room-content/674d9727a22822c1eb46cb31-1747645473439.png)

## 🛠️ Documentación de Herramientas / Tool Documentation
## Documentación de Herramientas / Tool Documentation
Here you will find an overview of the primary tools currently at your disposal for monitoring, investigating, and responding to security incidents.


#### Ingested Sources:
- **Sysmon Logs**: System monitoring logs from machines in the network to detect process creations, modifications, and other system-level events.

- **List of Sysmon Events ID**:
	- Event ID 1: Process creation;
	- Event ID 2: A process changed a file creation time;
	- Event ID 3: Network connection;
	- Event ID 7: Image loaded;
	- Event ID 11: FileCreate;
	- Event ID 12: RegistryEvent (Object create and delete);
	- Event ID 13: RegistryEvent (Value Set);
	- Event ID 15: FileCreateStreamHash;
	- Event ID 22: DNSEvent (DNS query);
	- Event ID 25: ProcessTampering (Process image change);
  
- **Security Logs**: Logs from machines which record security-related events such as user logins, access attempts, privilege changes, and other security-critical activities.

#### Analyst Workstation (My Computer)
The Analyst Workstation is a dedicated VM specifically configured for your investigation needs. This isolated environment ensures a secure and controlled setting for analyzing and responding to potential threats.

---

**Fuente / Source:** [TryHackMe Threat Hunting Simulator](https://tryhackme.com/threat-hunting-sim)
**Autor del documento / Document author:** Apuromafo
**Fecha de acceso / Access date:** 2026-09-01
