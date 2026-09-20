# SOC Fundamentals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `socfundamentals` | [TryHackMe](https://tryhackme.com/room/socfundamentals) | 01 Level Easy | TryHackMe | SOC, SIEM, Alert Triage, Incident Response | Operational — SOC analyst workflow and alert handling |

---

**Contexto:** Este room introduce los fundamentos de un Security Operations Center (SOC), incluyendo sus componentes, roles, procesos y tecnologías. Se aborda la detección de incidentes, el análisis de alertas y las herramientas utilizadas en un entorno SOC real.

## Solucionario

### Task 1: Security Operations Center

**Explicación:** Se identifica el concepto fundamental de un SOC como centro de operaciones de seguridad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the full form of SOC? | `Security Operations Center` |

### Task 2: Detection / People, Process, Technology

**Explicación:** Se Exploran los pilares de un SOC: las personas, los procesos y la tecnología que conforman la detección de incidentes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the primary goal of a SOC? | `Detection` |
| 2 | What are the three main components of a SOC? | `People, Process, Technology` |

### Task 3: SOC Roles

**Explicación:** Se Identifican los roles dentro de un SOC, desde el analista nivel 1 hasta el ingeniero de detección.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the entry-level role in a SOC? | `SOC Analyst (Level 1)` |
| 2 | What role focuses on creating and tuning detection rules? | `Detection Engineer` |

### Task 4: SOC Responsibilities

**Explicación:** Se Analiza las responsabilidades fundamentales de un SOC: quién es el responsable y qué se Monitorea.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Who is responsible for monitoring and detecting security incidents? | `Who` |
| 2 | What does a SOC monitor? | `What` |

### Task 5: Security Devices

**Explicación:** Se Identifica el dispositivo de seguridad utilizado en un SOC para filtrar tráfico de red.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What device is used to filter network traffic? | `Firewall` |
| 2 | Is the firewall an essential component of a SOC? | `yea` |

### Task 6: Alert Analysis

**Explicación:** Se Analiza una alerta de seguridad específica, incluyendo la fecha, IP de origen, herramienta utilizada y la determinación de si es un intento legítimo o no.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of alert was triggered? | `Port Scan` |
| 2 | When was the alert triggered? | `June 12, 2024 17:24` |
| 3 | What is the source IP address? | `10.0.0.3` |
| 4 | What tool was used to perform the scan? | `Nessus` |
| 5 | Is this a legitimate scan or an attack? | `Intended` |
| 6 | Is this alert a true positive? | `yea` |
| 7 | What is the flag? | `THM{000_INTRO_TO_SOC}` |

### Task 7: Practical Exercise

**Explicación:** Se Aplica los conocimientos adquiridos en un ejercicio práctico de SOC.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the practical exercise | `No answer needed` |

---

**Metodología:** Se Utilizan conceptos fundamentales de SOC para identificar y analizar alertas de seguridad, desde la detección inicial hasta la determinación de la naturaleza del incidente.

### Cadena de ataque / Attack Chain

**Learning chain:** SOC Fundamentals → Alert Detection → Alert Analysis → Incident Determination → SOC Workflow

**Lección:** *Un SOC efectivo integra personas, procesos y tecnologías para detectar, analizar y responder a incidentes de seguridad de manera coordinada y eficiente.*

**MITRE ATT&CK:** T1040 — Network Sniffing; T1595 — Active Scanning

**Fuente:** [TryHackMe - SOC Fundamentals](https://tryhackme.com/room/socfundamentals)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.