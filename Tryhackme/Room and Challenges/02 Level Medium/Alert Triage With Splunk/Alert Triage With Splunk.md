# Alert Triage With Splunk
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `alerttriagewithsplunk` |
| **Link** | [TryHackMe](https://tryhackme.com/room/alerttriagewithsplunk) |
| **Sección** | 02 Level Medium |
| **Fuente** | https://simontaplin.net/2025/11/28/answers-for-the-tryhackme-alert-triage-with-splunk-room/ |
| **Componentes** | Splunk, triage de alertas, brute-force SSH (Linux), tarea maliciosa (Windows/Sysmon), web shell (red), análisis SOC |
| **Impacto** | Uso de Splunk para triage de alertas (brute-force SSH en Linux, tarea maliciosa en Windows, web shell) y determinación de si cada alerta es un True Positive o False Positive. |
---
**Contexto:** Tres alertas llegan en distintos entornos (Linux, Windows y web). Cada una se triagea con Splunk y se clasifica.
*EN: Three alerts arrive across different environments (Linux, Windows, web). Each is triaged with Splunk and classified.*
## Solucionario
### Task 1 — Linux SSH Brute-Force
**Explicación:** Triage de la alerta de fuerza bruta SSH. Contando los intentos fallidos sobre `john.smith` con Splunk se obtienen 500 logins fallidos en 5 minutos de duración. Del historial de comandos se ve la escalada a `root` y la creación de la cuenta `system-utm` para persistencia.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many failed login attempts were made on the user john.smith? | `500` |
| 2 | What was the duration of the brute force attack in minutes? | `5` |
| 3 | What username was the attacker able to privilege escalate to? | `root` |
| 4 | What is the name of the user account created by the attacker for persistence? | `system-utm` |
### Task 2 — Windows Malicious Task
**Explicación:** Triage de la alerta Windows: la tarea maliciosa fue creada por un proceso con ProcessId `5816`, cuyo proceso padre es `cmd.exe`. Durante el discovery el atacante enumeró el grupo local `Administrators`, y la estación de trabajo desde la que inició sesión en el host es `DEV-QA-SERVER`.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the ProcessId of the process that created this malicious task? | `5816` |
| 2 | What is the name of the parent process for the process that created this malicious task? | `cmd.exe` |
| 3 | Which local group did the attacker enumerate during discovery? | `Administrators` |
| 4 | What is the name of the workstation from which the Threat Actor logged into this host? | `DEV-QA-SERVER` |
### Task 3 — Web Shell (Network)
**Explicación:** Triage de la alerta web: la actividad de fuerza bruta con Hydra comenzó a las `2025-09-14 21:20:27`. Para interactuar con el web shell el atacante usó un user agent de Chrome (`Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...`), realizando 4 peticiones al servidor vía el web shell.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What time did the brute-force activity using Hydra begin? | `2025-09-14 21:20:27` |
| 2 | Which user agent did the attacker use when interacting with the web shell? | `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36` |
| 3 | What was the number of requests made by the attacker to the server via the web shell? | `4` |
---
**Metodología:** Triage SOC con Splunk: buscar eventos (login failures, Sysmon task creation, web logs) → correlacionar con comandos/cuenta → determinar veredicto (TP/FP).
**Learning chain:** brute-force SSH (Linux) → escalada y persistencia → tarea maliciosa Windows (Sysmon) → web shell y user agent → clasificación de alertas.
**MITRE ATT&CK:** T1110.001 (Password Guessing) / T1110.002 (Password Cracking), T1136.001 (Local Account), T1053.005 (Scheduled Task), T1078 (Valid Accounts), T1505.003 (Web Shell), T1069 (Permission Groups Discovery).
**Fuente:** [TryHackMe - Alert Triage With Splunk](https://tryhackme.com/room/alerttriagewithsplunk)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
