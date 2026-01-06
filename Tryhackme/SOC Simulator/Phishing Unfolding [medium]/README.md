# Phishing Unfolding [MEDIUM]

## 📊 Información de la Sala
- **ID Interno:** `1542debf-4bcd-4cd3-b52c-2203de746689`
- **Nivel:** `MEDIUM`
- **Recompensa:** `1880 XP`

## 🎯 Objetivos
- Monitor and analyse real-time alerts as the attack unfolds.
- Identify and document critical events such as PowerShell executions, reverse shell connections, and suspicious DNS requests.
- Create detailed case reports based on your observations to help the team understand the full scope of the breach.

## 🛠️ Alert triage
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
  - **True Positive:** Contractor ran a brute force attack via Hydra without getting any approval
  - **False Positive:** IT misconfigured their script and it now fails to log in every minute
  - **False Positive:** The password had expired but the user tried to log in with old credentials 6 times
- Rule "Login from Unfamiliar Location":
  - **True Positive**: Threat actor used an EC2 instance in the US to breach a Europe-based employee
  - **True Positive:** Threat actor used a popular VPN service to access the breached account
  - **False Positive:** A US-based employee accessed their email from a phone during a vacation in Asia
  - **False Positive:** Salesperson used an approved VPN to log in and triggered the alert

## Alert Escalation

**Escalation Required**

True Positive alert must be escalated if additional actions or remediation are required, or if the alert belongs to a single incident (single attack chain) and is connected to other alerts that require escalation.

**When Escalation IS NOT Required**

- An employee downloaded an unwanted or cracked software from the web, but the downloaded installer was quarantined by AV or removed by the user before execution, before any impact
- A corporate mail server received an email, classified it as phishing, and quarantined it before any users had a chance to access the malicious email
- Botnet scanned the corporate website for common vulnerabilities like XSS and path traversal, and the activity did not cause any performance or security issues

**When Escalation IS Required**

- Threat actor gained access to the corporate server or workstation and ran a port or network scan from there, even if the scan was not successful or no further actions were taken
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

  > This activity is classified as a True Positive due to detected brute force attempts from the IP address 211.219.22.213 to the CORP-11 Windows host on the TryHatMe environment. This IP is flagged as malicious on the TryDetectThis app. The attack targeted the username Bob Taylor. This activity started at 10:22 on 05.02.2025. After more than 100 unsuccessful attempts, a successful login was detected at 10:27 on 05.02.2025 from a malicious IP to Bob's account. Immediate escalation is required, as unauthorized access was detected, necessitating remediation actions like account lockout and password change.

- **False Positive - "Windows Account Brute Force"**

  > This activity is classified as a False Positive. I detected that Bob Taylor attempted to log into the CORP-11 Windows host on the TryHatMe environment from the IP address 12.23.4.115. It is worth noting that this user regularly engages in activity from this IP address. During the investigation, 6 failed login attempts were found starting at 12:23 on 01.02.2025, with the reason for the failures being the user's expired password. This resulted in failed events triggering the correlation rule. No anomalies were found.

## 🛠️ Company information
# Company Information
TryHatMe is one of the fastest-growing companies within the e-commerce industry, specializing in the online sale of hats. Our unique value proposition, which allows customers to virtually "try on" hats before purchasing, has distinguished us in the market and driven rapid growth.

### Directory
| Name                | Role       | Email                         | Logged-in Host |
|---------------------|------------|-------------------------------|----------------|
| Michael Ascot       | CEO        | michael.ascot@tryhatme.com    | win-3450       |
| Sophie J            | HR         | sophie.j@tryhatme.com         | win-3461       |
| Michelle Smith      | Legal      | michelle.smith@tryhatme.com   | win-3459       |
| Roger Fedora        | Marketing  | roger.fedora@tryhatme.com     | win-3460       |
| Yani Zubair         | IT         | yani.zubair@tryhatme.com      | win-3449       |
| Miguel O'Donnell    | Sales      | miguel.odonnell@tryhatme.com  | win-3451       |
| Cain Omoore         | Sales      | cain.omoore@tryhatme.com      | win-3452       |
| Kyra Flores         | Sales      | kyra.flores@tryhatme.com      | win-3453       |
| Amna Espinoza       | Sales      | amna.espinoza@tryhatme.com    | win-3454       |
| Ashwin Johnston     | Sales      | ashwin.johnston@tryhatme.com  | win-3455       |
| Safa Prince         | Sales      | safa.prince@tryhatme.com      | win-3456       |
| Diego Summers       | Sales      | diego.summers@tryhatme.com    | win-3457       |
| Armaan Terry        | Sales      | armaan.terry@tryhatme.com     | win-3458       |
