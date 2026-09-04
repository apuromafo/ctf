

# SOC-Role-in-Blueteam [EASY]
**Room Link:**  https://tryhackme.com/room/socroleinblueteam

 <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/678ecc92c80aa206339f0f23-1756302396554" width="250" alt="SOC Role in Blue Team">

#### Learning Objectives

- Understand the concept and purpose of the Blue Team
- Explore a place of the SOC within the company structure
- Find out about your career path as a SOC L1 analyst

#### Prerequisites

- Complete the [[Junior Security Analyst]] room

## Security Hierarchy

#### Security Departments

In tiny companies, the IT department takes the role of securing the company. Small to medium-sized companies may have a generic "Information Security" team that does all sorts of tasks. For this room, we will focus on bigger companies with a CISO overseeing multiple security teams, each handling a specific task. For example:

- **Red Team**: Offensive security experts, pentesters, or ethical hackers who look for security issues
- **GRC Team**: Specialists managing policies and ensuring compliance with regulations like PCI DSS
- **Blue Team**: Defensive security experts like SOC analysts, engineers, or incident responders

#### Questions

1. Which senior role typically makes key cyber security decisions?
   **Answer:** CISO
2. What is the common name for roles like SOC analysts and engineers?
   **Answer:** Blue Team

## Meet the Blue Team

#### SOC

- **L1 Analysts**: Junior members who triage alerts and pass complex cases to L2
- **L2 Analysts:** Experienced members who investigate more advanced attacks
- **Engineers**: Experts in configuring security tools like EDR or SIEM
- **Manager**: A person who manages the whole SOC team

#### CIRT (Cyber Incident Reponse Team)

If SOC expertise is not enough or the incident goes out of control, you urgently call the "firefighters" - CIRT, also called CSIRT or CERT. The members should have a broad knowledge of cyber threats and handle breaches without depending on tools like EDR or SIEM. A CIRT job is stressful and responsible, but also rewarding. Here are a few CIRT examples:

- [JPCERT](https://www.jpcert.or.jp/english): Japan's CERT handling nation-wide breaches
- [Mandiant](https://www.mandiant.com/): A private team responding to global cyber incidents
- [AWS CIRT](https://aws.amazon.com/security-incident-response): Investigates security incidents of AWS customers

#### Specialized Defensive Roles

Large companies, technology-focused startups, and government agencies often require narrow and specialized Blue Team roles - exciting and highly valuable, but requiring deep topic knowledge and broad experience in broader fields like SOC or IT. These narrow roles can include:

- **Digital Forensics Analyst**: Uncover hidden threats in disk and memory
- **Threat Intelligence Analyst**: Gather data about emerging threat groups
- **AppSec Engineer**: Maintain a secure software development lifecycle
- **AI Researcher**: Study AI threats and how to defend against them

#### Questions

1. Does Blue Team focus on defensive or offensive security?
   **Answer:** Defensive
2. Which department handles active or urgent cyber incidents
   **Answer:** CIRT

## Advancing SOC Career

#### Internal SOC vs MSSP

Not every organization has the expertise to operate a SOC on its own and relies on a Managed Security Services Provider (MSSP), a company that delivers outsourced security services, most commonly SOC, to its clients. Working at MSSP is typically high-pressure, but it is also a good option to quickstart your career. While we recommend applying for any open SOC position as your first job, it's also important to understand the differences:

#### Questions

1. How would you call a cyber security company providing SOC services?
   **Answer:** MSSP
2. Which role naturally continues your SOC L1 analyst journey?
   **Answer:** SOC L2 Analyst

## Final Challenge

1. What flag did you claim after completing the final challenge?
   **Answer:** THM{trysecureme_is_secured!}
   
   
#Module: SOC Role in Blue Team Answers
| Task | Title | Response |
| :--- | :--- | :--- |
| **1** | Introduction | No answer needed |
| **2** | Security Hierarchy | 1. CISO<br>2. Blue Team |
| **3** | Meet the Blue Team | 1. Defensive<br>2. CIRT |
| **4** | Advancing SOC Career | 1. MSSP<br>2. SOC L2 Analyst |
| **5** | Final Challenge | `THM{trysecureme_is_secured!}` |
| **6** | Conclusion | No answer needed |