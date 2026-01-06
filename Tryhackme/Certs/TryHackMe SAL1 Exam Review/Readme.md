oficial información**
https://tryhackme.com/certification/security-analyst-level-1

https://tryhackme.com/resources/blog/creating-sal1





review:
https://raw.githubusercontent.com/GoldenEye10/goldeneye10.github.io/refs/heads/main/_posts/2025-03-30-SAL1_review.md

https://github.com/Remy-Haidaraly/Remy-Haidaraly.github.io/blob/4d3312a6e54ad18d678474512124082e04a6d98e/_posts/2025-04-19-SAL1.md




---
> TryHackMe SAL1 Exam Review
>
>description: TryHackMe Security Analyst Level 1 (SAL1)
>
> date: 2025-03-30 11:33:00 +0800
  
---

## Overview
The **TryHackMe Security Analyst Level 1 (SAL1)** exam is a brand-new hands-on certification designed to test practical cybersecurity skills. In February 2025, TryHackMe announced its launch and offered free exam vouchers to those holding **CompTIA CySA+** or **Blue Team Level 1 (BTL1)**. Naturally, I took advantage of this opportunity, Since I already held the BTL1 Certification.

---

## Should You Take SAL1?
### You should take SAL1 if:
- You want a **hands-on experience** like **CompTIA CySA+** or **BTL1**.
- You enjoy **learning through practical experience** rather than theoritical.
- You appreciate **affordable certifications**.

### You should NOT take SAL1 if:
- You’re **only looking to boost your resume**.
- You want a certification **just to pass HR filters**.

TryHackMe is a well-respected platform, but this certification is **brand new** and may take time to gain industry recognition.

---

## Preparation Strategy
TryHackMe recommends its **Cyber Security 101** and **SOC Level 1** pathways for exam preparation. Due to the limited time available before my free voucher expired (March 30, 2025), I just went with my knowledge from **BTL1**.

### Key Takeaways:
- **Master Splunk:** It plays a crucial role in the exam.
- **Prioritize hands-on exercises:** Especially SOC Simulators.
- **Time management is critical.**
- **Proper ducomentation is critical.**

---

## Exam Breakdown
The **SAL1 exam** consists of three sections, with a maximum score of **1000 points**:

- **200 points** – 80 **multiple-choice questions** (**1 hour**).
- **400 points** – **Scenario I** (hands-on investigation, **2 hours**).
- **400 points** – **Scenario II** (hands-on investigation, **2 hours**).

### Tools Provided:
- **Alerts Dashboard**
- **Splunk** (primary tool for analysis)
- **Analyst VM** (not heavily utilized, mostly for copying IPs into ‘TryDetectThis’, a TryHackMe fake VirusTotal)

### Exam Tips:
- **Close all True Positive alerts before the timer expires** – incomplete scenarios earn **zero** points.
- **Exam instructions are vague** about whether True Positives should be escalated. Over-escalation may cost points.
- **Multiple-choice questions are straightforward** – if you’ve taken **CompTIA Security+, ISC2 SSCP, or EC-Council CND**, you’ll do fine.

---

## Reporting Format
During preparation, I copied a **Documentation demo of exam on how to write report** to streamline my reports:

```
Alert description: <Type of attack>

### 5Ws
- **Who:** <Usernames, IPs, hostnames, etc.>
- **What:** <Type of attack>
- **Impact:** <What happened? Data exfiltration? Malware infection?>
- **When:** <Timestamps from Splunk>
- **Where:** <Device logs in Splunk>
- **Why:** <Attacker’s goal>

### Attacker Intent
- **Objective:** (e.g., ransomware, lateral movement, data theft)
- **Impact:** Was the attack successful?
- **MITRE ATT&CK Mapping:** (Identify relevant TTPs)

### Indicators of Compromise (IOCs)
- **List all related IPs, hostnames, usernames, and artifacts.**

### Recommended Actions
- **Block IPs, disable compromised accounts, or take other necessary security measures.**

### Escalation Decision
- **State whether you are escalating the alert, if yes, then justify the reason.**
```

### AI Grading Criteria:
1. **Correctly identifying alerts** (True Positive vs. False Positive).
2. **Providing detailed 5W analysis.**
3. **Assessing attacker intent accurately.**
4. **Listing comprehensive IOCs.**
5. **Making correct escalation decisions.**

AI **strictly penalizes incorrect escalation choices** but seems to be lenient on typos and grammer.

---

## Exam Experience & Verdict
One frustration was the **inability to take defensive actions** when detecting attacks in Splunk. While I could **observe** the attack unfolding, I couldn’t **isolate systems or disable compromised accounts**, which felt limiting but makes sense you are just the level 1 SOC. The lab is kind of slow and you do not have to use lot of tool except for splunk.

### Exam Format Flaws:
- **No scenario details until after the timer starts.**
- **VM boot-up time counts against your timer.**
- **Does not allow you to confirm, so you can review all the alerts one final time before the end of each section**
- **Tip:** Immediately start VMs before reading the scenario.

### Final Thoughts:
- **Well-structured exam but seems very basic compared to BTL1.**
- **Great for SOC aspirants looking for hands-on experience. While BTL1 is focused more on incident response, this is pure SOC Scenario**


---

## Conclusion
Despite its pros and cons, **SAL1 is a solid fun hands-on blue team certification**. Beginners who complete **the relevant TryHackMe pathways** have a strong chance of passing. Upon success, you receive a **certification, Credly badge, and some well-earned bragging rights.**



 2nd review:
 

---

## Comparativa: SAL1 vs. BTL1

Si estás dudando entre **SAL1 (Security Analyst Level 1)** y **BTL1 (Blue Team Level 1)**, aquí te comparto mi análisis tras haber cursado ambos:

* **BTL1 (Enfoque Generalista):** Esta certificación es un "Blue Team" en sentido amplio. Se centra profundamente en el uso de herramientas forenses y de investigación (como **Autopsy, Volatility, KAPE y DeepBlueCLI**). Es ideal si buscas entender la respuesta ante incidentes desde la raíz técnica.
* **SAL1 (Enfoque Operativo SOC):** Está diseñada específicamente para el rol de **Analista SOC**. El contenido se vuelca en la operativa diaria: gestión de servicios críticos como **SIEM y SOAR**, triaje de alertas, redacción de informes y priorización de incidentes.

**En resumen:** Ambos son muy completos, pero mientras que BTL1 te da una visión técnica general del equipo azul, **SAL1 te prepara para el día a día real dentro de un SOC.**

> [!TIP]
> Si completas los recorridos **SOC L1 + SOC L2 de TryHackMe**, tendrás los conocimientos necesarios para afrontar ambas certificaciones con éxito.

---
Imagen del certificado (fr)
![Demo](./demo/sal1_remy%20haidaraly.png)

## Conclusión

La certificación **SAL1** es una excelente puerta de entrada al mundo de la defensa activa. Te capacita específicamente para:

* **Priorizar y analizar** alertas de seguridad de forma eficiente.
* **Leer e interpretar logs** de diversas fuentes.
* **Correlacionar información** (IOCs y comportamientos sospechosos).
* **Redactar informes** claros, técnicos y argumentados.

Todo esto se desarrolla en un entorno realista e inmersivo, con una relación calidad-precio muy competitiva para un nivel *entry-level*.

--- 
 