# 📋 APT29: Cozy Bear [MEDIUM]

![Thumbnail](thumbnail.png)

## 📈 Resumen Ejecutivo / Executive Summary
- **Industria / Industry:** Finance
- **Tipo de Ataque / Attack Type:** data exfiltration
- **Arquitectura / Architecture:** Hybrid (Cloud & On-prem)
- **Sistemas Operativos / OS:** windows, mac

## 📝 Contexto del Incidente / Incident Context
A bank in the financial services industry recently discovered anomalous network activities during a routine audit. The activities suggest an insider might be involved in sensitive data exfiltration targeting customer PII (personally identifiable information) and financial transaction records.,The exercise tests the efficacy and coordination of the incident response team, focusing on the integration of EDR and SIEM tools in investigating the breach. It challenges the team to employ their technical skills while adhering to compliance requirements mandatory in the financial sector.,The intended outcome is to enhance incident response procedures, bolster communication channels during crises, and ensure the team can effectively contain and remediate cybersecurity incidents.,Scenario Environment: The organization operates on a hybrid infrastructure combining on-premises data centers with cloud-based solutions, utilizing both Windows and macOS platforms across its operations. Key security layers include SIEM systems by Splunk, EDR solutions by Crowstrike and Palo Alto, a web application firewall, and industry-standard encryption protocols. Clients interface with bank services via a multi-platform mobile and web app suite.,Attack Surface: Initial compromises were suspected through spear-phishing emails targeting C-Suite executives, with additional anomalous activity recorded in both the corporate VPN logs and administrative access to key financial systems, indicating possible lateral movement.

## 🎯 Objetivos de la Simulación / Simulation Objectives
- Test and Validate Incident Response Plans and Procedures
- Enhance Team Coordination and Communication

## 🛠️ Aplicaciones y Herramientas Involucradas / Applications & Tools Involved
- SIEM
- EDR
- Web Apps
- Email Platform
- Active Directory
- Remote management tools (RDP)

---
*Escenario creado por / Scenario created by: THMDan*