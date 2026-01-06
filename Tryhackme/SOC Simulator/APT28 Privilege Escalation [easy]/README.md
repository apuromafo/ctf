# APT28: Privilege Escalation [EASY]

## 📊 Información de la Sala
- **ID Interno:** `f1c34265-f1aa-4bd7-9b4f-8b3dfcff4edc`
- **Nivel:** `EASY`
- **Recompensa:** `150 XP`

## 🎯 Objetivos
- Identify and triage security alerts indicating malicious behaviour consistent with APT28 activity.
- Explore the method for privilege escalation in enterprise environments attributed to APT28.
- Analyse and correlate various log types to identify anomalies and gain insight into adversary activity.

## 🛠️ Alert Triage
## Read Before You Begin

- Check out the Alert Triage Playbook described below (**Alert Triage** tab)
- Understand how to classify and escalate alerts (**Alert Classification** tab)
- Review case report guide and best practice examples (**Case Reporting** tab)
- Familiarise yourself with the company's assets and employees
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
   - **Use Analyst VM**: From "Analyst VM", open TryDetectMe app to check threat score of found indicators
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

Classification for activities which were determined to be legitimate, meaning those that did not have malicious intent, can’t harm the organization, and don’t violate the security policies. False Positives are often candidates for review to improve the detection rule or fix a misconfiguration in the network.

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

- An employee downloaded an unwanted or cracked software from web, but the downloaded installer was quarantined by AV or removed by the user before execution, before any impact
- A corporate mail server received an email, classified it as phishing, and quarantined it before any users had a chance to access the malicious email
- Botnet scanned the corporate website for common vulnerabilities like XSS and path traversal, and the activity did not cause any performance or security issues

**When Escalation IS Required**

- Threat actor gained access to the corporate server or workstation and ran port or network scan from there, even if the scan was not successful or no further actions were followed
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

  > This activity is classified as a False Positive. I detectd that Bob Taylor attempted to log into the CORP-11 Windows host on the TryHatMe environment from the IP address 12.23.4.115. It is worth noting that this user regularly engages in activity from this IP address. During the investigation, 6 failed login attempts were found starting at 12:23 on 01.02.2025, with the reason for the failures being the user's expired password. This resulted in failed events triggering the correlation rule. No anomalies were found.

## 🛠️ Company Information
# Company Information
TryGovMe is a government-affiliated research division specialising in the development of intelligent IoT and robotics solutions 
for national energy resilience. As part of a broader state initiative to modernise and secure critical infrastructure, 
TryGovMe designs and deploys autonomous systems, known as smart grid bots, that can monitor, maintain, and self-heal components of the national power grid. We stand out by combining robotics, secure data systems, and edge computing to help build a safer and more sustainable energy network.

## Company Structure

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

## Servers
| Purpose         | Hostname        | IP Address     |
|------------------|-----------------|----------------|
| Product Server   | Dev-Server      | 10.10.219.50   |
| QA Server        | Dev-QA-Server   | 10.10.219.40   |
| Web Server       | Web-Server   | 10.10.219.129    |

## 🛠️ Network Diagram
#### Below is a diagram illustrating the network architecture of the TryGovMe.


![Network Map](https://tryhackme-images.s3.amazonaws.com/user-uploads/674d9727a22822c1eb46cb31/room-content/674d9727a22822c1eb46cb31-1747645473439.png)

## 🛠️ Tool Documentation
# Tool Documentation
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
The Analyst Workstation is a dedicated VM specifically configured for your investigation needs. This isolated environment ensures a secure and controlled setting for analysing and responding to potential threats.
