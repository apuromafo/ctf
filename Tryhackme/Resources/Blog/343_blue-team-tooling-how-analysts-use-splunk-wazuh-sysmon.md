# Blue Team Tooling: How Analysts Use Splunk, Wazuh & Sysmon

**ID Original:** no disponible
**Slug:** blue-team-tooling-how-analysts-use-splunk-wazuh-sysmon
--------------------

It’s 02:13. A workstation triggers an alert for an unusual PowerShell execution. The command line looks obfuscated. The user swears they “just opened an email attachment.”
At this point, the question isn’t what tool do we use?
It’s how do we investigate this properly?
Modern Blue Teams don’t rely on a single platform. They operate across a visibility stack. Endpoint telemetry feeds detection engines. Detection engines feed centralised search platforms. Analysts pivot between them to build context before making a containment decision.
Three tools commonly found in that stack are Sysmon , Wazuh , and Splunk . But understanding how analysts actually use them is far more important than memorising what each one does.
The Visibility Layer: Sysmon and Deep Endpoint Telemetry
Windows systems generate logs by default, but they often lack the granularity needed for serious investigations. That’s where Sysmon, part of the Microsoft Sysinternals suite, becomes valuable.
Sysmon enhances endpoint visibility by logging detailed process creation events, command-line arguments, parent-child process relationships, network connections, and more. The official Microsoft documentation explains how it extends native logging capabilities in practical security deployments.
When an attacker uses PowerShell for lateral movement or downloads tooling from a remote server, Sysmon can reveal:
The exact command executed
The parent process that launched it
Associated network connections
File hash information
In a real investigation, this context is critical. An alert saying “PowerShell executed” is noisy. An alert that shows PowerShell launched by an unusual parent process, contacting an external IP, with encoded parameters, tells a very different story.
Practising how to interpret that telemetry is a core Blue Team skill, and it’s why hands-on log analysis environments matter. Structured SOC labs, such as the SOC Level 1 pathway on TryHackMe , simulate exactly this type of endpoint investigation in a controlled browser-based environment.
The Detection Layer: Wazuh and Behaviour-Based Alerts
Telemetry alone isn’t enough. It needs interpretation.
Wazuh is an open-source security monitoring platform that provides host-based intrusion detection, file integrity monitoring, and rule-based alerting. Its documentation outlines how it analyses endpoint logs and applies detection rules to identify suspicious behaviour.
In practice, a Blue Team might configure Wazuh to:
Trigger alerts on suspicious PowerShell flags
Detect changes to critical system files
Identify brute-force login attempts
Monitor abnormal privilege escalation patterns
Returning to our 02:13 alert: Wazuh may have triggered the initial detection because a rule matched a known malicious pattern. But that’s only the starting point. Analysts must validate whether the alert reflects genuine compromise or benign activity.
This validation process is where many junior analysts struggle. Alerts are easy. Interpretation is not.
Developing that skill requires working through simulated detection scenarios, tuning rules, and understanding false positives. Training environments that include behavioural detection workflows allow analysts to practise this without touching real production infrastructure.
The Correlation Layer: Splunk and Centralised Investigation
Large environments generate enormous volumes of logs. Without centralisation and search capability, meaningful investigation becomes impossible.
Splunk is widely used in Security Operations Centres as a SIEM platform for log aggregation, search, correlation, and dashboarding. Its Security Operations overview explains how organisations use it to investigate and respond to threats.
In a real workflow:
Sysmon logs suspicious activity on the endpoint.
Wazuh generates a detection alert based on a rule.
Splunk aggregates that alert alongside authentication logs, firewall logs, and other telemetry.
The analyst can then pivot:
Has this user authenticated elsewhere recently?
Are other hosts showing similar behaviour?
Is there outbound traffic to the same IP from multiple machines?
This is where detection becomes investigation.
Splunk enables correlation across data sources. But it doesn’t automatically produce insight. Analysts still need to craft queries, interpret results, and apply contextual reasoning.
Practising query logic, log filtering, and investigation workflows in lab environments is essential for building this capability. TryHackMe’s Network Security Monitoring and SOC-focused content provides guided practice in working with log data and investigation pipelines.
How the Stack Works Together in a Real Investigation
Let’s return to our original scenario.
A suspicious PowerShell execution alert fires.
Sysmon provides detailed telemetry: the encoded command, the parent process, and the associated network connection. Wazuh flags the behaviour as matching a known suspicious pattern. Splunk correlates that activity with other logs, revealing that the same user account authenticated from a second machine shortly after.
At this point, the analyst must answer practical questions:
Is this a phishing-induced compromise?
Has lateral movement begun?
Is privilege escalation occurring?
Each tool contributes a piece of the picture. None provide the full answer alone.
This layered investigation model reflects how modern SOC environments actually function. It also explains why Blue Team training that focuses purely on tool interfaces, without workflow context, often falls short.
Tools Don’t Make Analysts. Repetition Does.
It’s tempting to treat Splunk, Wazuh, and Sysmon as products to “learn.” In reality, they are environments within which analysts develop judgement.
Blue Team capability depends on:
Recognising abnormal process behaviour
Understanding detection logic
Interpreting log context
Making containment decisions under uncertainty
Those skills are developed through repeated investigation cycles.
Hands-on SOC simulations, realistic alert scenarios, and structured defensive pathways allow learners to practise the entire investigation lifecycle without risk. TryHackMe’s SOC Level 1 pathway , for example, walks learners through alert triage, log analysis, and incident response workflows in a safe environment designed to mirror real operational tasks.
The Bottom Line
Sysmon provides visibility. Wazuh provides detection. Splunk provides correlation and search.
But the analyst provides interpretation.
Understanding how these tools interact is far more valuable than memorising their feature lists. For aspiring Blue Team professionals, the goal isn’t simply to “learn Splunk” or “install Wazuh.” It’s to build investigation fluency.
That fluency comes from structured, hands-on defensive practice.
If you want to develop the skills behind the tools, start with realistic SOC labs and incident simulations rather than static tutorials.

---
**Fuente / Source:** [blue-team-tooling-how-analysts-use-splunk-wazuh-sysmon](https://tryhackme.com/resources/blog/blue-team-tooling-how-analysts-use-splunk-wazuh-sysmon)
