# BlackCat [MEDIUM]

## 📊 Información de la Sala / Room Information
- **ID Interno / Internal ID:** `22a48195-d64d-4413-827b-0396e32f0252`
- **Nivel / Level:** `MEDIUM`
- **Recompensa / Reward:** `1335 XP`

## 🎯 Objetivos / Objectives
- Identify and correlate attacker activity from leaked credentials to ransomware deployment.
- Classify and escalate alerts appropriately using the THM SOC Rulebook.
- Determine how the attacker moved laterally and established persistence.
- Identify which accounts, machines, and data were affected during the attack.

## 🛠️ Triaje de Alertas / Alert Triage
## Lee Antes de Empezar / Read Before You Begin

- Check out the Alert Triage Playbook described below (**Alert Triage** tab)
- Understand how to classify and escalate alerts (**Alert Classification** tab)
- Review case report guide and best practice examples (**Case Reporting** tab)
- Familiarise yourself with SOC notes, company's assets, and employees
- Note that the provided information is beneficial for earning the highest score!

### Alert Triage Playbook

1. **Initial Alert Review**:

   - **Access the SOC Dashboard**: Open the SOC dashboard and review the new alerts
   - **Assign Alert to Yourself**: Add the first (earliest) alert to the list of assigned alerts
   - **Understand Alert Logic**: Review the alert description and understand its logic
   - **Review Alert Details**: Look at the IOCs provided in the alert, like IPs and domains

2. **Investigate in the SIEM**:

   - **Access the SIEM**: Open the "SIEM" tool to access raw security events that triggered the alert
   - **Query Related Logs**: Perform searches to gather more context and build the activity timeline
   - **Use Analyst VM**: From the "Analyst VM", open the TryDetectThis app to check the threat score of found indicators
   - **Correlate and Validate**: Correlate the alert data with other data sources to validate the credibility of the alert

3. **Resolution and Closure**:
   - **Decide on Alert Classification**: Click "Write Case Report" and follow the **Alert Classification** guide
   - **Write Case Report**: Provide a detailed report of the triaged alert according to the **Alert Reporting** guide
   - **Decide if Alert Requires Escalation**: For True Positives, refer to the same guide and follow the Escalation section
   - **Submit and Close the Alert**: Once the alert is triaged, submit and close its case report in the SOC dashboard

## 🛠️ Clasificación de Alertas / Alert Classification
## Clasificación de Alertas / Alert Classification

**True Positive**

Classification for unauthorised access to information, threats like malware, adware, phishing, brute force, account breach, or an action that violates the company’s security policies. True Positives are often candidates for further remediation steps like host isolation, password rotation, or malware cleanup.

**False Positive**

Classification for activities which were determined to be legitimate, meaning those that did not have malicious intent, can’t harm the organisation, and don’t violate the security policies. False Positives are often candidates for review to improve the detection rule or fix a misconfiguration in the network.

**Classification Examples**

- Rule "Windows Account Brute Force":
  - **True Positive**: Threat actor indeed attempted brute force, even if it was unsuccessful
  - **True Positive:** Contractor ran brute force attack via Hydra without getting any approval
  - **False Positive:** IT misconfigured their script and it now fails to log in every minute
  - **False Positive:** The password was expired but user tried to login with old credentials 6 times
- Rule "Login from Unfamiliar Location":
  - **True Positive**: Threat actor used EC2 instance in US to breach Europe-based employee
  - **True Positive:** Threat actor used a popular VPN service to access the breached account
  - **False Positive:** US-based employee accessed their email from phone during a vacation in Asia
  - **False Positive:** Sales person used an approved VPN to login and triggered the alert

## Escalada de Alertas / Alert Escalation

**Escalation Required**

True Positive alert must be escalated if additional actions or remediation are required, or if the alert belongs to a single incident (single attack chain) and is connected to other alerts that require escalation.

**When Escalation IS NOT Required**

- An employee downloaded an unwanted or cracked software from the web, but the downloaded installer was quarantined by AV or removed by the user before execution, before any impact
- A corporate mail server received an email, classified it as phishing, and quarantined it before any users had a chance to access the malicious email
- Botnet scanned the corporate website for common vulnerabilities like XSS and path traversal, and the activity did not cause any performance or security issues

**When Escalation IS Required**

- Threat actor gained access to the corporate server or workstation and ran a port or network scan from there, even if the scan was not successful or no further actions were followed
- Threat actor tried to dump credentials from the breached file server via Mimikatz, but the attempt was blocked by an existing EDR solution
- The alert was identified as part of a larger attack chain but was initially misclassified. Here, an analyst needs to go back and update their case report

## 🛠️ Reporte de Alertas / Alert Reporting
## Reporte de Alertas / Alert Reporting

- Provide a clear and detailed explanation of the reason why the activity is classified as TP or FP
- Clearly explain why the alert requires escalation and which remediation actions may be required
- Specify the entities associated with the activity detected by the alert:
  - Identify **who** or **what** was affected
  - Indicate **where** the activity occurred
  - Clarify **when** the activity took place
- Provide all IOCs associated with the activity:
  - **Network Indicators**: IP addresses, Ports, Domains, URLs, etc
  - **Host Indicators**: File Names, File Paths, Hashes, Signatures, etc.
- Specify which goals the threat actor attempted to achieve
- (Optional) Specify which MITRE techniques or tactics the activity can be related to

### Reportes de Buenas Prácticas / Best Practice Reports

- **True Positive - "Windows Account Brute Force"**

  > This activity is classified as a True Positive due to detected brute force attempts from the IP address 211.219.22.213 to the CORP-11 Windows host on the TryHatMe environment. This IP is flagged as malicious on the TryDetectThis app. The attack targeted the username Bob Taylor. This activity started at 10:22 on 05.02.2025. After more than 100 unsuccessful attempts, a successful login was detected at 10:27 on 05.02.2025 from a malicious IP to Bob's account. Immediate escalation is required, as unauthorised access was detected, necessitating remediation actions like account lockout and password change.

- **False Positive - "Windows Account Brute Force"**

  > This activity is classified as a False Positive. I detected that Bob Taylor attempted to log into the CORP-11 Windows host on the TryHatMe environment from the IP address 12.23.4.115. It is worth noting that this user regularly engages in activity from this IP address. During the investigation, 6 failed login attempts were found starting at 12:23 on 01.02.2025, with the reason for the failures being the user's expired password. This resulted in failed events triggering the correlation rule. No anomalies were found.

## 🛠️ Notas de Entrega del SOC / SOC Handover Notes
## Notas de Entrega del SOC / SOC Handover Notes

### 1 day ago
- Our new Threat Intelligence feed is live in SIEM. Let me know if you spot any false positives. - Jordan
- Also, someone left a fresh box of cat-shaped cookies in the break room. High-value asset: grab ’em before they vanish! - Bud

### 2 days ago

- Worked with Tom (co-founder and their interim IT Guy) to finish deploying the Splunk forwarder to all hosts. Verify your searches to confirm no hosts are missing. - Jen

### 3 days ago

- Welcome aboard, PawPressMe! Let’s show our newest client why our SOC purr-formance is top-tier. - Jordan
- Smooth sailing ahead! - Bud

![A meme of a cat saying yer boat is ready, capnm](https://tryhackme-images.s3.amazonaws.com/user-uploads/63588b5ef586912c7d03c4f0/room-content/63588b5ef586912c7d03c4f0-1747760673441.jpg)

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

**Fuente / Source:** [TryHackMe SOC Simulator](https://tryhackme.com/soc-sim)
**Autor del documento / Document author:** Apuromafo
**Fecha de acceso / Access date:** 2026-09-01
