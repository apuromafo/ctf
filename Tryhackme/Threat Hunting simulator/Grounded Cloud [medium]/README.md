# 🏹 Threat Hunting: Grounded Cloud [MEDIUM]

## 📊 Perfil de la Amenaza
- **Dificultad:** `MEDIUM`
- **Puntos de Misión:** `905 XP`

## 🎯 Objetivos de Hunting
- Identify exploitation of insecure configurations for initial access.
- Explore advanced methods of persistence and privilege escalation.
- Discover execution paths and attempts to impact cloud environment.

## 💡 Hipótesis de Investigación
> This threat hunting session focuses on investigating a set of TTPs commonly used by adversaries in cloud environments. The customer provided us with a list of techniques and tactics to validate during the hunt. Since TryEarthMe is a fast-growing startup with valuable and sensitive data, there is a risk that some malicious activity could already exist in their environment. The goal is to determine whether traces of such activity can be found in the customer’s cloud environment.

## 🛠️ Scenario Details
## Background


This threat hunting session investigates a range of TTPs that adversaries commonly use in cloud environments. The customer, TryEarthMe, provided us with a list of techniques and tactics they want us to validate during the hunt.

We suspect certain malicious activity types may already be present in their environment. As a fast-growing startup working with sensitive agricultural and industrial data, TryEarthMe represents an attractive target for adversaries seeking to compromise cloud workloads and gain access to valuable intellectual property.

Your objective is to proactively analyse the cloud infrastructure, test against the provided TTPs, and uncover potential anomalies that could indicate early signs of compromise.

## Objectives
- Identify exploitation of insecure configurations for initial access;
- Explore advanced methods of persistence and privilege escalation;
- Discover execution paths and attempts to impact cloud environment.

## References
- [Attackers Exploit Public Files to Breach Cloud Accounts](https://thehackernews.com/2024/08/attackers-exploit-public-env-files-to.html)
- [Leaked Environment Variables Enable Cloud Extortion Campaigns](https://unit42.paloaltonetworks.com/large-scale-cloud-extortion-operation/)

## 🛠️ List of TTPs
## TTPs

Below you can find the list of TTPs provided by the client for the threat hunting session.


1. Initial Access
* Phishing - MITRE ID T1566
* Valid Accounts - MITRE ID T1078

2. Persistence
* Create Account - MITRE ID T1136
* Account Manipulation - MITRE ID T1098

3. Privilege Escalation
* Abuse Elevation Control Mechanism - MITRE ID T1548
* Account Manipulation - MITRE ID T1098

4. Impact	
* Data Destruction - MITRE ID T1485
* Network Denial of Service - MITRE ID T1498

## 🛠️ Company Information
# Company Information
TryEarthMe is an agri-tech startup revolutionising soil enrichment and crop production with autonomous drone technology.
Our mission is to transform traditional agriculture into a smarter, more sustainable practice by combining advanced robotics, soil science, and real-time data.

TryEarthMe’s drones analyse soil conditions, apply eco-friendly fertilisers with precision, and monitor crop health, helping farmers increase yields while reducing waste.
As a fast-growing startup, we stand out by merging cutting-edge automation with sustainability to shape the future of global food production.

## Company Structure

### Employees
| Name              | Position                          | Email                          | AWS Account Name         |
|-------------------|-----------------------------------|--------------------------------|--------------------------|
| Michael Carter    | Chief Executive Officer           | michael.carter@tryearthme.thm  | michael.carter-tem       |
| Emily Davis       | Soil Fertility Research Scientist | emily.davis@tryearthme.thm     | emily.davis-tem          |
| Robert Hughes     | Infrastructure Administrator      | robert.hughes@tryearthme.thm   | robert.hughes-tem        |
| Anna Walker       | Agricultural Data Analyst         | anna.walker@tryearthme.thm     | anna.walker-tem          |
| Benjamin Scott    | AI Vision Specialist              | benjamin.scott@tryearthme.thm  | benjamin.scott-tem       |
| Laura Mitchell    | Sustainability Officer            | laura.mitchell@tryearthme.thm  | laura.mitchell-tem       |
| Christopher Allen | Field Operations Supervisor       | christopher.allen@tryearthme.thm | christopher.allen-tem  |
| Victoria Brooks   | IoT Systems Engineer              | victoria.brooks@tryearthme.thm | victoria.brooks-tem      |
| Daniel Turner     | Lead Robotics Engineer            | daniel.turner@tryearthme.thm   | daniel.turner-tem        |
| Sophia Collins    | Sale Specialist                   | sophia.collins@tryearthme.thm  | sophia.collins-tem       |

## 🛠️ Tool Documentation
# Tool Documentation
Here, you will find an overview of the primary tools you currently have for monitoring, investigating, and responding to security incidents.

#### Ingested Sources:
AWS CloudTrail logs from the customer’s environment have been ingested into Splunk. These logs are available for investigation and analysis, and can be queried directly in Splunk using the following search: 
**`index=tem-th`**

#### Analyst Workstation (My Computer)
The Analyst Workstation is a dedicated VM specifically configured for your investigation needs. This isolated environment ensures a secure and controlled setting for analysing and responding to potential threats.
