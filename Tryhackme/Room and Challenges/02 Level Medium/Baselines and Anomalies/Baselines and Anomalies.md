# Baselines and Anomalies
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `baselineanomalies` |
| **Link** | [TryHackMe](https://tryhackme.com/room/baselineanomalies) |
| **Sección** | SOC / Detection |
| **Fuente** | Writeup de thmrevenant (GitHub) |
| **Componentes** | SOC, detección de anomalías, líneas base de activos (IP/modelo/software), firewalls (ACL, change management), DNS, alertas (impossible travel), análisis de logins sospechosos |
| **Impacto** | Sala centrada en la detección de anomalías frente a líneas base: identificación de dispositivos no estándar, anomalías de red y análisis de inicios de sesión sospechosos. |
---
**Contexto:** Sala centrada en la detección de anomalías frente a líneas base: identificación de dispositivos no estándar, anomalías de red y análisis de inicios de sesión sospechosos.
*EN: Room focused on anomaly detection against baselines: identifying non-standard devices, network anomalies, and analyzing suspicious logins.*
## Solucionario
### Task 1 — Anomalías de Activos / Asset Anomalies
**Explicación:** Comparar los activos de la red frente a la línea base establecida para detectar direcciones IP y modelos de dispositivos anómalos: `WS-LON-004` tiene IP anómala, `SVR-NYC-BKUP01` es el servidor con IP anómala y `WS-NYC-004` tiene un modelo de dispositivo distinto. Revisando el inventario de software de Anna, los programas `9` y `15` (seriales) no deberían estar en la lista.
*EN: Compare network assets against the established baseline to spot anomalous IPs and device models: `WS-LON-004` has the anomalous IP, `SVR-NYC-BKUP01` is the server with the anomalous IP and `WS-NYC-004` has a different device model. Reviewing Anna's software inventory, programs `9` and `15` (serials) shouldn't be there.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the workstation that has the anomalous IP address? | `WS-LON-004` |
| 2 | What is the name of the server with the anomalous IP address? | `SVR-NYC-BKUP01` |
| 3 | Which workstation has a device model different from the rest? | `WS-NYC-004` |
| 4 | There are two installed software programs that should not be included in Anna's list. Which ones are they? Share their serial numbers. Answer format: X, Y | `9, 15` |
### Task 2 — Conceptos de Detección / Detection Concepts
**Explicación:** Conceptos de detección: la **comunicación** es la mayor herramienta del defensor para saber si una actividad la realizó el administrador; el **Change Management and Approvals** rastrea y aprueba cambios en la firewall ACL; excluyendo el **Internal DNS server** de los queries al puerto DNS se detecta tráfico DNS que lo está saltando; un login desde dos lugares geográficamente muy distintos en poco tiempo genera una alerta de **Impossible travel**.
*EN: Detection concepts: **communication** is the defender's biggest tool to know whether the administrator performed an activity; **Change Management and Approvals** tracks firewall ACL changes; excluding the **Internal DNS server** from DNS-port queries surfaces DNS bypassing it; logins from two very distant locations in a short time trigger an **Impossible travel** alert.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When trying to identify if an activity was performed by the administrator or not, what is the biggest tool that a defender can use? | `communication` |
| 2 | Which process can be used to track and approve changes to the firewall Access Control List? | `Change Management and Approvals` |
| 3 | If we are looking for DNS traffic bypassing the local DNS server, what should we exclude from the search of all queries to the DNS port? | `Internal DNS server` |
| 4 | What kind of alert should be generated if a user logs in from two vastly geographically different places in a short amount of time? | `Impossible travel` |
### Task 3 — Investigación de Login Sospechoso / Suspicious Login Investigation
**Explicación:** Investigación del login fuera del horario laboral del 27 de julio de 2024: ocurrió a las `06:37:07.659259000` y corresponde a **Mia Perez**. La usuaria realizó actividades anómalas desde dos máquinas; la otra máquina tiene la IP `192.168.1.36`. Se correlaciona el dominio sospechoso `c2server.com`.
*EN: Investigating the login outside office hours on 27 July 2024: it happened at `06:37:07.659259000` and belongs to **Mia Perez**. She performed anomalous activities from two machines; the other machine has IP `192.168.1.36`. The suspicious domain is `c2server.com`.*

```
Establecer línea base → Comparar activos (IP/modelo/software) → Identificar anomalías → Detectar login anómalo → Correlacionar usuario, IPs y dominio → Dominio C2
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | You have been alerted of a login outside of normal office hours on the 27th of July, 2024. Can you identify the time this login happened? | `06:37:07.659259000` |
| 2 | Which user logged in at this time? | `Mia Perez` |
| 3 | This user performed anomalous activities from two different machines; what is the IP address of the other machine? | `192.168.1.36` |
| 4 | What suspicious domain does this user connect to? | `c2server.com` |
---
**Metodología:** Establecer línea base → comparar activos (IP/modelo/software) → identificar anomalías → aplicar conceptos de detección (comunicación, change management, impossible travel) → investigar login anómalo → correlacionar usuario, IPs y dominio C2.
**Learning chain:** líneas base → anomalías de activos → telemetría/conceptos de detección → investigación de logins → correlación con C2.
**MITRE ATT&CK:** T1078 (Valid Accounts), T1071.001 (Web Protocols C2), T1046 (Network Service Scanning)/T1049, T1580 (Network Access Validation)/baselines, M1030 (Network Segmentation).
**Fuente:** [TryHackMe - Baselines and Anomalies](https://tryhackme.com/room/baselineanomalies)