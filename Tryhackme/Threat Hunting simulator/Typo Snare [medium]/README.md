# 🏹 Typo Snare [MEDIUM]

## 📊 Perfil de la Amenaza / Threat Profile
- **Dificultad / Difficulty:** `MEDIUM`
- **Puntos de Misión / Mission Points:** `2500 XP`

## 🎯 Objetivos de Hunting / Hunting Objectives
- Investigate command-line artifacts and reconstruct process trees to reveal the attacker's steps. 
- Correlate tool usage with MITRE ATT&CK techniques. 
- Map compromised accounts over time. 

## 💡 Hipótesis de Investigación / Investigation Hypothesis
> We suspect that the attacker gained access to Perry’s system via a trojanized file he downloaded from an untrusted website. Following initial execution, the attacker may have established persistence on the host to maintain access.

We further hypothesize that the attacker extracted credentials from Perry’s system using known tools such as Mimikatz, which allowed lateral movement and unauthorized access to other systems in the network. If this is confirmed, it is likely that multiple and privileged user accounts have been compromised.

As a final stage in the attack chain, the attacker encrypted user files on the compromised systems, causing disruption.


## 🛠️ Detalles del Escenario / Scenario Details
## Background

The alert hit the SOC around 4:00 PM. Two machines, fully encrypted. Ransom notes where files used to be. The central SIEM went dark just minutes before.

Fortunately, someone had managed to pull logs from the two affected hosts—Perry’s and another developer’s—before everything spiraled out of control.

Now the team has to figure out what happened. And all signs point to something Perry did earlier that day...

**September 26, 2023**—just another Tuesday at SwiftSpend Financial, a small but resourceful company where everyone’s always juggling five deadlines and too much coffee.

Perry, one of the devs, had a tight sprint deadline. His manager had sent him an encrypted .7z archive with a snippet of code that needed finishing _yesterday_. Perry quickly realized his workstation didn’t have anything that could unzip the file. So, in true caffeine-fueled developer fashion, he Googled the first thing that came to mind, clicked the top result (because who scrolls down?), and downloaded a tool to open it.

Everything seemed fine. Until it wasn’t.

A little more than one hour later, Perry’s workstation started acting weird. At first, it was slow. Then apps crashed. Then everything—literally every file—became unreadable.

Your mission as a threat hunter is to dig through the logs and reconstruct the attack chain. What happened? How did it start? How did it spread? And what damage did it do? 

## Objetivos / Objectives

- Investigate command-line artifacts and reconstruct process trees to reveal the attacker's steps. 
- Correlate tool usage with MITRE ATT&CK techniques. 
- Map compromised accounts over time.

## 🛠️ IoCs
## Lista de Indicadores de Compromiso / Indicator of Compromise List

From the initial investigation of the alert, the SOC team was able to collect the following: 

#### Network Based:

Domain: 

- 7zipp.org

IP address:

- 206.189.34.218

#### Host Based:

FileExtension:

- *.777zzz
- *.msi
- *.ps1

FileNames:

- 7zipp.exe
- 7zipp.dll
- mimikatz.exe

Hashes:

- 4b9213d22989474b467aa53080d9e295
- 29efd64dd3c7fe1e2b022b7ad73a1ba5
- 61c0810a23580cf492a6ba4f7654566108331e7a4134c968c2d6a05261b2d8a1
- fd713992f39338986e8573aff1232675323fde827328159b29a31cc3cd515874

## 🛠️ Información de la Empresa / Company Information
SwiftSpend Finance is a dynamic financial services firm specializing in boutique investment strategies and digital asset management. By combining traditional financial expertise with modern fintech innovation, SwiftSpend delivers tailored solutions to a wide range of clients, from individual investors to small institutions.

Though modest in size, the company operates at high velocity. Cross-functional teams thrive on agility, resourcefulness, and a strong problem-solving culture that keeps SwiftSpend at the forefront of fintech evolution.

#### Empleados / Employees

| Name | Username | Role | Host (last logged in) |  |
| --- | --- | --- | --- | --- |
| Anna Jones | anna.jones | Senior Financial Analyst | WKSTN-02 | 172.16.1.151 |
| Damian Hall | damian.hall | IT Systems Administrator | WKSTN-01 | 172.16.1.150 |
| James Cromwell | james.cromwell | Security Engineer | WKSTN-08 | 172.16.1.157 |
| Perry Parsons | perry.parsons | Software Developer | WKSTN-03 | 172.16.1.152 |
| Olivia Bennett | olivia.bennett | Operations Manager | WKSTN-04 | 172.16.1.153 |
| Ethan Clarke | ethan.clarke | Backend Developer | WKSTN-10 | 172.16.1.159 |
| Maya Singh | maya.singh | Junior Financial Analyst | WKSTN-05 | 172.16.1.154 |
| Leo Martinez | leo.martinez | DevOps Engineer | WKSTN-15 | 172.16.1.164 |
| Grace Turner | grace.turner | Executive Assistant | WKSTN-06 | 172.16.1.155 |
| Noah Edwards | noah.edwards | Product Manager | WKSTN-14 | 172.16.1.163 |
| Sophia Walker | sophia.walker | Software Developer | WKSTN-13 | 172.16.1.162 |
| Marcus Young | marcus.young | Data Analyst | WKSTN-09 | 172.16.1.158 |
| Rachel Kim | rachel.kim | Compliance Officer | WKSTN-12 | 172.16.1.161 |
| Daniel Foster | daniel.foster | Portfolio Manager | WKSTN-07 | 172.16.1.156 |
| Claire Chen | claire.chen | Risk Analyst | WKSTN-11 | 172.16.1.160 |

## 🛠️ Documentación de Herramientas / Tool Documentation
## Documentación de Herramientas / Tool Documentation
Here you will find an overview of the primary tools currently at your disposal for monitoring, investigating, and responding to security incidents.

#### SIEM:
The SIEM is an ELK (Elastic Search) instance with pre-ingested logs from the two affected Windows hosts. 
To access the Kibana console, use the default credentials: `elastic:elastic`

#### Ingested Sources:
- **Windows Sysmon Logs**: System monitoring logs to detect process creations, modifications, and other system-level events.
- **Windows Security Logs**: Logs which record security-related events such as user logins, access attempts, privilege changes, and other security-critical activities.
- **Windows PowerShell Logs**: Logs that capture the execution of PowerShell commands and scripts. These logs are useful for detecting administrative tasks, automation, and potentially malicious activity.

#### Analyst Workstation (My Computer)
The Analyst Workstation is a dedicated VM specifically configured for your investigation needs. This isolated environment ensures a secure and controlled setting for analyzing and responding to potential threats.

---

**Fuente / Source:** [TryHackMe Threat Hunting Simulator](https://tryhackme.com/threat-hunting-sim)
**Autor del documento / Document author:** Apuromafo
**Fecha de acceso / Access date:** 2026-09-01
