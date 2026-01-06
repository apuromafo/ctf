# 🏹 Threat Hunting: Health Hazard [EASY]

## 📊 Perfil de la Amenaza
- **Dificultad:** `EASY`
- **Puntos de Misión:** `360 XP`

## 🎯 Objetivos de Hunting
- Determine how a threat actor first gained a foothold on the system. Identify suspicious activity that may point to the initial compromise method.
- Investigate signs of malicious execution following the initial access. Analyse the logs and system behaviour to uncover the attacker's actions.
- Identify any mechanisms the attacker used to maintain access across system restarts or user sessions. Look for indicators of persistence that could allow long-term control.

## 💡 Hipótesis de Investigación
> An attacker may have leveraged a compromised third-party software package to gain initial access to the system and silently stage a payload for later execution. They likely established persistence to maintain access without immediate detection.

## 🛠️ Executive Summary
**Issued by:** TryDetectThis Intelligence

**Classification:** Internal – TLP:AMBER

TryDetectThis Intelligence has identified a coordinated supply chain attack campaign targeting open-source ecosystems, specifically, npm and Python package repositories. The campaign appears to be orchestrated by a threat actor leveraging long-term infiltration of neglected or low-profile projects to weaponize legitimate packages.

The attacker’s strategy involves contributing to moderately used but under-maintained libraries, gaining contributor or maintainer status through helpful commits. Once trusted, they publish malicious updates, embedding post-installation payloads or obfuscated backdoors within version releases that appear minor or maintenance-related.

These weaponized libraries often act as stagers for follow-on actions—such as downloading secondary payloads, establishing persistence, or exfiltrating tokens and credentials from developer machines. Due to their presence in tutorials, starter templates, or widely shared codebases, they have a high chance of spreading through organic adoption.

## 🛠️ IOCs
## Host-Based IOCs

| **Type**             | **Value**                                                |
| -------------------- | -------------------------------------------------------- |
| NPM Package          | `healthchk-lib@1.0.1`                                    |
| Registry Path        | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`     |
| Registry Value Name  | `Windows Update Monitor`                                 |
| Registry Value Data  | `powershell.exe -NoP -W Hidden -EncodedCommand <base64>` |
| Downloaded File Path | `%APPDATA%\SystemHealthUpdater.exe`                      |
| PowerShell Command   | `Invoke-WebRequest -Uri ... -OutFile ...`                |
| Process Execution    | `powershell.exe -NoP -W Hidden -EncodedCommand ...`      |
| Script Artifact      | Found in `package.json` under `"postinstall"`            |

## Network-Based IOCs
| **Type**           | **Value**                                                  |
| ------------------ | ---------------------------------------------------------- |
| Download URL       | `http://global-update.wlndows.thm/SystemHealthUpdater.exe` |
| Hostname Contacted | `global-update.wlndows.thm`                                |
| Protocol           | HTTP (unencrypted)                                         |
| Port               | 80                                                         |
| Traffic Behavior   | Outbound file download to `%APPDATA%` via PowerShell       |

## 🛠️ Company Information
## Company Information

PawPressMe is a lean online media company that helps small brands and startups tell their stories through digital content, ebooks, and social media strategy.

From cyber security whitepapers to playful lifestyle campaigns, PawPressMe produces fast-turnaround content that helps clients grow their digital presence.

The company operates with a small creative team, collaborative tools, and a high-volume content pipeline, making speed and flexibility core to its value.

### Employees

| Name               | Position                                       | Email                     | Logged-in Host |
|--------------------|------------------------------------------------|---------------------------|----------------|
| Tom Whiskers       | Co-Founder & Content Strategist (Interim IT)   | tom@pawpress.me           | paw-tom        |
| Marie Purrman      | Finance Manager                                | marie@pawpress.me         | paw-marie      |
| Tabitha Clawson    | Copywriter                                     | tabitha@pawpress.me       | paw-tabitha    |
| Leo Meowrell       | Multimedia Editor                              | leo@pawpress.me           | paw-leo        |
| Penny Pawsworth    | Social Media Specialist                        | penny@pawpress.me         | paw-penny      |
| Sally Felina       | Founder & Creative Director                    | sally@pawpress.me         | paw-sally      |

## 🛠️ Asset Inventory
### Network and Subnets

| Purpose                   | Range          |
|---------------------------|----------------|
| PawPressMe Corporate LAN  | 10.10.50.0/24  |

### Endpoints and Network Devices

| Purpose                | Hostname      | Public IP | Internal IP    |
|------------------------|---------------|-----------|----------------|
| Backup Server      | pawbackup  | –         | 10.10.50.5     |
