# Trooper

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `trooper` | [TryHackMe](https://tryhackme.com/room/trooper) | 01 Level Easy | THM | Tropic Trooper, MITRE ATT&CK, STIX, spear-phishing, USBferry, BITSAdmin | Análisis del grupo APT Tropic Trooper y sus herramientas bajo el marco MITRE ATT&CK |

---

**Contexto:**

> **ES:** La sala analiza la actividad del grupo APT Tropic Trooper desde la óptica de la inteligencia de amenazas (CTI) y el marco MITRE ATT&CK: vectores de acceso inicial (spear-phishing), malware que se replica por medios extraíbles (USBferry), identificación de objetos STIX, herramientas como BITSAdmin, tácticas de defensa evasión y técnicas de recolección automatizada.

> **EN:** This room analyzes the activity of the APT group Tropic Trooper from a Cyber Threat Intelligence (CTI) and MITRE ATT&CK perspective: initial access vectors (spear-phishing), malware that replicates over removable media (USBferry), STIX object identification, tools such as BITSAdmin, defense evasion tactics, and automated collection techniques.

## Solucionario

### Task 1: Análisis del grupo Tropic Trooper / Tropic Trooper Group Analysis

**Explicación:**

1. 1. spear-phishing emails
   2. USBferry
   3. malware--5d0ea014-1ce9-5d5c-bcc7-f625a07907d0
   4. Replication through removable media
   5. Tropic Trooper
   6. 39
   7. BITSAdmin
   8. Local Accounts
   9. Initial Access, Persistence,  Defense Evasion and Privilege Escalation
   10. Automated Collection

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which attack vector was successfully used by the group? | `spear-phishing emails` |
| 2 | What is the name of the USB-based malware strain? | `USBferry` |
| 3 | What is the STIX ID of the malware object? | `malware--5d0ea014-1ce9-5d5c-bcc7-f625a07907d0` |
| 4 | Which technique describes propagation over removable media? | `Replication through removable media` |
| 5 | What is the name of the threat group? | `Tropic Trooper` |
| 6 | How many items are associated with the group? | `39` |
| 7 | Which tool is used for command execution? | `BITSAdmin` |
| 8 | Which account type is leveraged by the group? | `Local Accounts` |
| 9 | Which tactics describe the applied technique? | `Initial Access, Persistence,  Defense Evasion and Privilege Escalation` |
| 10 | Which technique automates the collection of data? | `Automated Collection` |

---

**Metodología:** Se realiza una investigación de inteligencia de amenazas sobre el grupo Tropic Trooper: se identifican los vectores de acceso inicial (spear-phishing), el malware propio (USBferry) y su ID STIX, así como la técnica de replicación por medios extraíbles. Se enumeran las herramientas asociadas (BITSAdmin), las cuentas usadas (Local Accounts) y, bajo MITRE ATT&CK, se mapean las tácticas de acceso inicial, persistencia, evasión de defensas, escalada de privilegios y la técnica de recolección automatizada.

### Cadena de ataque / Attack Chain

Phishing → delivery of USBferry malware → replication via removable media → execution via BITSAdmin → defense evasion → automated collection.

**Learning chain:** Cyber threat intelligence → APT research → STIX objects → MITRE ATT&CK mapping → detection

**Lección:** *Conocer a tu adversario antes de enfrentarte a él es la mitad de la detección: los recursos de TTPS permiten anticipar el siguiente movimiento del grupo.*

**MITRE ATT&CK:** T1566 (Phishing), T1091 (Replication Through Removable Media), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1119 (Automated Collection)

**Fuente:** [TryHackMe - Trooper](https://tryhackme.com/room/trooper)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.