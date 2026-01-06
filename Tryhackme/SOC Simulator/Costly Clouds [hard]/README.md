# Costly Clouds [HARD]

## 📊 Información de la Sala
- **ID Interno:** `a31535e4-54a2-4a89-814a-f8552dd1ef28`
- **Nivel:** `HARD`
- **Recompensa:** `715 XP`

## 🎯 Objetivos
- Hunt GUI-Vil actions across AWS activity and piece together the whole attack chain, from credential abuse to resource hijacking.
- Learn to discern attacker behaviour from pressure-driven developer actions.
- Uncover stealthy EC2 crypto-mining hidden within autoscaling bursts.

## 🛠️ Alert Triage
## Read Before You Begin

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

## 🛠️ Alert Classification
## Alert Classification

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

## Alert Escalation

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

## 🛠️ Alert Reporting
## Alert Reporting

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

### Best Practice Reports

- **True Positive - "Windows Account Brute Force"**

  > This activity is classified as a True Positive due to detected brute force attempts from the IP address 211.219.22.213 to the CORP-11 Windows host on the TryHatMe environment. This IP is flagged as malicious on the TryDetectThis app. The attack targeted the username Bob Taylor. This activity started at 10:22 on 05.02.2025. After more than 100 unsuccessful attempts, a successful login was detected at 10:27 on 05.02.2025 from a malicious IP to Bob's account. Immediate escalation is required, as unauthorised access was detected, necessitating remediation actions like account lockout and password change.

- **False Positive - "Windows Account Brute Force"**

  > This activity is classified as a False Positive. I detected that Bob Taylor attempted to log into the CORP-11 Windows host on the TryHatMe environment from the IP address 12.23.4.115. It is worth noting that this user regularly engages in activity from this IP address. During the investigation, 6 failed login attempts were found starting at 12:23 on 01.02.2025, with the reason for the failures being the user's expired password. This resulted in failed events triggering the correlation rule. No anomalies were found.

## 🛠️ SOC Handover
## SOC Shift Handover

Nothing too wild this shift, but as expected, things are heating up with the game launch happening later today. Infra’s more active than usual—definitely feels like the calm before the storm.
Saw a handful of EC2s spun up with tags like '**gamelaunch**' and '**gameload**', which lines up with what the devs said. Sophia and Liam have been busy pushing data to S3 all day—looks like final game assets going out.

For those _less_ familiar with AWS logs (yes, Riley, this means you), please—for the sake of my sanity—**expand the whole tree**. Just because '**requestParameters**' has a family tree that could fill a genealogy site doesn't mean you get to ignore its grandkids. The important stuff is usually buried down in the nested fields.

**Heads up**: devs are deep in the launch trenches right now, so expect noise, weird log patterns, and the occasional "why in the world did they do that?" moment. Try not to overfilter—just because it's noisy doesn't mean it's safe. Launch days are the perfect opportunities for anyone looking to slip under the radar.

Stay paranoid. — Alex

> Expanded the tree.
> Regret expanding the tree.
> Have now met three generations of nested fields and still don’t know what’s going on.
>
> This is fine. — Riley

## 🛠️ Company Information
## Company Introduction

TryHatMe Studios are an up and coming software development house, ranging from Games to utility applications, known famously for previous releases such as “CyberHeist” and the highly anticipated platformer “NeuralNexus”.

### Log Sources

- **AWS CloudTrail logs**: API-level activity across the AWS environment, capturing actions taken by users, roles, and services. Including logins, instance launches, S3 access, and permission changes.
- **Route 53 DNS Resolution logs**: outbound DNS queries made by resources inside the VPC and captured via Amazon Route 53 Resolver. These logs are used to monitor domain lookups from EC2 instances and other AWS services.

### Employees

| Name              | Email                              | Role                      | Org Unit         |
|------------------|------------------------------------|---------------------------|------------------|
| Michael Ascot    | m.ascot@tryhatmestudios.thm         | Lead Developer            | Game Development |
| Michelle Smith   | m.smith@tryhatmestudios.thm         | Head of Marketing         | Marketing        |
| Luke Sullivan    | l.sullivan@tryhatmestudios.thm      | IT Service Delivery       | IT Operations    |
| Riley Tran       | r.tran@tryhatmestudios.thm          | SOC Analyst (Level 1)     | Security         |
| Sophia Reyes     | s.reyes@tryhatmestudios.thm        | Game Developer            | Game Development |
| Jada Collins     | j.collins@tryhatmestudios.thm       | DevOps Engineer           | Infrastructure   |
| Theo Granger     | t.granger@tryhatmestudios.thm       | Infrastructure Architect  | Infrastructure   |
| Ava Noor         | a.noor@tryhatmestudios.thm          | QA Analyst                | QA               |
| Liam Patel       | l.patel@tryhatmestudios.thm         | Backend Developer         | Game Development |
| Dana Brooks      | d.brooks@tryhatmestudios.thm        | Security Operations Lead  | Security         |
| Alex Morgan      | a.morgan@tryhatmestudios.thm        | SOC Analyst (Level 2)     | Security         |
