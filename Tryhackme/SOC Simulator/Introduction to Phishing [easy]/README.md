# Introduction to Phishing [EASY]

## 📊 Información de la Sala / Room Information
- **ID Interno / Internal ID:** `8de2e24d-1072-4f5d-8f5e-6af62d427f17`
- **Nivel / Level:** `EASY`
- **Recompensa / Reward:** `360 XP`

## 🎯 Objetivos / Objectives
- Monitor and analyze real-time alerts.
- Identify and document critical events such as suspicious emails and attachments.
- Create detailed case reports based on your observations to help your team understand the full scope of alerts and malicious activity.

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

## 🛠️ Información de la Empresa / Company Information
## Información de la Empresa / Company Information

**The Try Daily** is a bold, energetic publication dedicated to the art of trying—every single day. Whether it’s testing new ideas, embracing challenges, or stepping outside your comfort zone, we believe that growth comes from action. Our stories, challenges, and expert insights inspire readers to take on something new. We celebrate both success and failure, because every attempt brings you closer to something great. 

At **The Try Daily**, we don’t just report on change—we encourage it! Try something today! Try something tomorrow! Just keep trying!!

### Herramientas y Fuentes de Datos / Tools & Data Sources
 
- **Webserver (ModSecurity Audit Log)**: Web application firewall (WAF) logs from the company webserver, capturing HTTP request details, potential attacks, and rule violations.
- **Email**: Email logs containing message metadata and conversation history, providing insights into internal and external communications within the company.
- **Firewall**: Firewall logs from company's main firewall. 

> **Note:** The current set of ingested sources within our SIEM is limited to the logs mentioned above. We are actively working on expanding these sources to provide you with a more comprehensive view of our security landscape. ~SOC Head

### Estación de Trabajo del Analista / Analyst Workstation
- Access to the **TryDetectThis** platform via a Desktop Shortcut. Use this to submit IPs to check for maliciousness.

### Empleados / Employees

| Name              | Department         | Email                         | Logged-in Host | IP Address   |
|-------------------|--------------------|-------------------------------|----------------|--------------|
| Ethan Johnson     | Editorial           | e.johnson@thetrydaily.thm     | win-3451       | 10.20.2.1    |
| Julia Garcia      | Content             | j.garcia@thetrydaily.thm      | win-3452       | 10.20.2.8    |
| Isabella Martinez | Marketing           | i.martinez@thetrydaily.thm    | win-3453       | 10.20.2.9    |
| Benjamin Lopez    | Sales               | b.lopez@thetrydaily.thm       | win-3454       | 10.20.2.10   |
| Henry Thomas      | Operations          | h.thomas@thetrydaily.thm      | win-3455       | 10.20.2.14   |
| Andrew Moore      | IT                  | a.moore@thetrydaily.thm       | win-3456       | 10.20.2.16   |
| Hannah Harris     | Human Resources     | h.harris@thetrydaily.thm      | win-3457       | 10.20.2.17   |
| Tyler Young       | Project Management  | t.young@thetrydaily.thm       | win-3458       | 10.20.2.24   |
| Grace Wright      | Content             | g.wright@thetrydaily.thm      | win-3459       | 10.20.2.27   |
| Jacob Carter      | IT Support          | j.carter@thetrydaily.thm      | win-3460       | 10.20.2.30   |
| Chloe Scott       | Content             | c.scott@thetrydaily.thm       | win-3461       | 10.20.2.21   |
| Caleb Anderson    | Content             | c.anderson@thetrydaily.thm    | win-3462       | 10.20.2.13   |
| Charlotte Allen   | Web Development     | c.allen@thetrydaily.thm       | win-3463       | 10.20.2.25   |

## 🛠️ Inventario de Activos / Asset Inventory
### Red y Subredes / Network and Subnets
| Purpose | Range |
|---------|--------|
| Office Network | 10.20.2.0/24 |

---

**Fuente / Source:** [TryHackMe SOC Simulator](https://tryhackme.com/soc-sim)
**Autor del documento / Document author:** Apuromafo
**Fecha de acceso / Access date:** 2026-09-01
