# Incident Response in Action: A Step-by-Step Walkthrough of a Phishing Attack

**ID Original:** 68c3dd7e91ff6400019bf0b8
**Slug:** incident-response-in-action-a-step-by-step-walkthrough-of-a-phishing-attack
--------------------

Phishing remains the most common way attackers break into organisations. In fact, according to the [2024 Verizon Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/dbir/?ref=blog.tryhackme.com), phishing accounted for nearly half of all breaches last year.So how do security teams actually respond when a phishing email slips through? Let’s walk through a realistic **incident response process**, step by step—using a phishing attack as our example.
## **Step 1: Detection**
The process starts when something suspicious is spotted. That might be:
* An employee reporting a strange email
* Security monitoring tools flagging a known malicious domain
* Endpoint detection software catching suspicious file execution👉 On TryHackMe, the[ SOC Level 1 Path](https://tryhackme.com/path/outline/soclevel1?ref=blog.tryhackme.com) trains you to detect suspicious events through log analysis and alert triage.
## **Step 2: Analysis**
Next, the incident responder digs into the evidence:
* Reviewing the phishing email headers
* Analyzing attachments or links in a safe sandbox
* Checking whether the sender domain or IP matches known malicious sourcesThis step confirms whether it’s a **false positive** or a genuine threat.👉 TryHackMe’s[ Incident Response module](https://tryhackme.com/module/incident-response?ref=blog.tryhackme.com) walks you through analysing indicators of compromise (IOCs) in real-world scenarios.
## **Step 3: Containment**
If the email is confirmed malicious, the goal is to stop the damage from spreading. Containment might include:
* Blocking the malicious domain in the email gateway
* Isolating affected endpoints from the network
* Resetting compromised user accountsContainment buys responders time while preventing further exploitation.
## **Step 4: Eradication &amp; Recovery**
Once contained, responders remove the threat:
* Deleting malicious files from systems
* Patching exploited vulnerabilities
* Restoring affected machines from clean backupsRecovery means ensuring normal operations resume securely—without leaving any hidden backdoors behind.
## **Step 5: Lessons Learned**
Finally, the team reviews the incident to strengthen defences for the future. That can involve:
* Updating detection rules
* Running phishing awareness training for employees
* Feeding new IOCs into SIEMs and threat intel platforms👉 The[ Digital Forensics &amp; Incident Response module](https://tryhackme.com/module/digital-forensics-and-incident-response?ref=blog.tryhackme.com) dives deeper into post-incident investigations and strengthening processes.
## **Why This Matters**
Phishing may seem simple, but it’s one of the most **effective and dangerous attack vectors**. Understanding the incident response lifecycle not only helps organisations defend against it—it gives aspiring cybersecurity professionals a clear roadmap for what responders actually do on the job.Want to practice this process for yourself? Start below and step into the role of an analyst responding to phishing, malware, and more.            Launch the SOC Level 1 Learning Path      
