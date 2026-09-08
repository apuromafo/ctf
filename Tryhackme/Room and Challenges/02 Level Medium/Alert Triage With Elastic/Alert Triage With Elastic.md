# Alert Triage With Elastic
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `alerttriagewithelastic` |
| **Link** | [TryHackMe](https://tryhackme.com/room/alerttriagewithelastic) |
| **Sección** | 02 Level Medium |
| **Fuente** | OsmanDhaqane writeup PDF (github.com/OsmanDhaqane/alert-triage-with-elastic-tryhackme-writeup) |
| **Componentes** | Elastic/Kibana, SOC, log analysis (IIS weblogs, Windows Security, Sysmon, PowerShell), ProxyLogon, wtriage de alertas |
| **Impacto** | Triage de alertas SOC con Kibana/Elastic: análisis de logs de IIS (web), Windows Security, Sysmon y PowerShell para reconstruir un ataque ProxyLogon a SomeCorp. Cobertura: alcance de logs, eventos web, actividad de cuentas y ejecución de comandos. |
---
**Contexto:** Investigación guiada de triage de alertas como analista SOC. Data view: **Alert Triage With Elastic**; tiempo seleccionado: **Entire data range**. Se reconstruye un ataque ProxyLogon sobre SomeCorp cruzando logs IIS, Security, Sysmon y PowerShell.
*EN: Guided alert-triage investigation as a SOC analyst. Data view: **Alert Triage With Elastic**; time range: **Entire data range**. A ProxyLogon attack on SomeCorp is reconstructed correlating IIS, Security, Sysmon and PowerShell logs.*
## Solucionario
### Task 2 — Scenario Briefing
**Explicación:** Briefing del escenario. Con la data view seleccionada y el rango de tiempo completo se cuenta el total de logs disponibles. Dentro del índice **weblogs** se identifica la IP del cliente (`client.ip`) origen de los eventos sospechosos.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many logs are available for analysis within the entire time range? | `1467` |
| 2 | What is the field value for the client.ip in the weblogs index? | `203.0.113.55` |
### Task 3 — Investigating Web Attacks
**Explicación:** En el índice weblogs se filtran las peticiones POST de la IP `203.0.113.55` a `proxyLogon.ecp` (Path del ataque ProxyLogon), obteniendo 3 peticiones con el user agent `python-requests/2.25.1`. Buscando el parámetro `cmd=` en `url.path` hay 20 logs; se identifica el comando ejecutado vía `errorEE.aspx` (un web shell) el Jul 20, 2025 @ 04:45:50.000.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many POST requests did the IP address 203.0.113.55 make to proxyLogon.ecp? | `3` |
| 2 | Which user.agent paired with the IP address 203.0.113.55 made the POST requests? | `python-requests/2.25.1` |
| 3 | How many logs contain the cmd= query parameter in the url.path field? | `20` |
| 4 | Which command was run utilizing errorEE.aspx on Jul 20, 2025 @ 04:45:50.000? | `hostname` |
### Task 4 — Uncovering Account Activity
**Explicación:** En los logs de Windows Security se ubica el evento de logon 4624 del Administrador (`winlog.record_id`: `17166`). En Sysmon, el evento 1 (creación de proceso) del Jul 20, 2025 @ 05:11:27.996 tiene `process.pid` 964. Para la creación de una cuenta nueva se usa el Event ID **4720**; la cuenta creada se llama `svc_backup`.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the winlog.record_id of the Administrator 4624 logon event? | `17166` |
| 2 | What is the process.pid of the Sysmon 1 event that occurred on Jul 20, 2025 @ 05:11:27.996? | `964` |
| 3 | What is the winlog.event_id for the new user account being created? | `4720` |
| 4 | What is the name of the new user account? | `svc_backup` |
### Task 5 — Exposing Command Execution
**Explicación:** Se expone la ejecución de comandos del atacante: añade la cuenta `svc_backup` a "Remote Desktop Users" con `net localgroup`, la mete en Administrators (evento Security 4732, `winlog.record_id` 17254), ejecuta PowerShell con `net group "Domain Admins" /domain` a las 05:16:14.628 y crea un archivo (exfil) denominado `finance_it_archive.rar` usando Rar.exe.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What command does the attacker use to add the new account to the "Remote Desktop Users" group? | `net localgroup "Remote Desktop Users" svc_backup /add` |
| 2 | What is the winlog.record_id of the 4732 Security event when the attacker adds the user to the Administrator group? | `17254` |
| 3 | What PowerShell command did the attacker run on Jul 20, 2025 @ 05:16:14.628? | `net group "Domain Admins" /domain` |
| 4 | What is the name of the archive that the attacker creates using the Rar.exe executable? | `finance_it_archive.rar` |
---
**Metodología:** Triage SOC (Kibana/Elastic): conteo de logs → análisis de weblogs (ProxyLogon, cmd=, web shell) → Windows Security/Sysmon (logons, creación de cuentas, grupos) → PowerShell/Rar.exe (ejecución de comandos y exfiltración).
**Learning chain:** alcance de logs → eventos web (ProxyLogon) → actividad de cuentas (4720/4732) → ejecución de comandos → cadena completa del incidente.
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application - ProxyLogon), T1059.001 (PowerShell), T1136.001 (Local Account), T1098 (Account Manipulation), T1078 (Valid Accounts), T1048 (Exfiltration Over Alternative Protocol - Rar.exe), T1505.003 (Web Shell).
**Fuente:** [TryHackMe - Alert Triage With Elastic](https://tryhackme.com/room/alerttriagewithelastic)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
