# Alert Triage With Elastic [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `alerttriagewithelastic`
* **Link:** https://tryhackme.com/room/alerttriagewithelastic
* **Objeto:** Triage de alertas SOC con Kibana/Elastic, analizando logs de IIS (web), Windows Security, Sysmon y PowerShell para reconstruir un ataque ProxyLogon a SomeCorp. Cobertura: alcance de logs, eventos web, actividad de cuentas y ejecución de comandos.

---

## Solucionario de Tareas / Task Solutions

> Investigación guiada de triage de alertas como analista SOC. Data view: **Alert Triage With Elastic**; tiempo seleccionado: **Entire data range**.
> Guided alert-triage investigation as a SOC analyst. Data view: **Alert Triage With Elastic**; time range: **Entire data range**.

### Tarea 2 / Task 2 — Scenario Briefing

**¿Cuántos logs hay disponibles para análisis en todo el rango de tiempo? / How many logs are available for analysis within the entire time range?**
`1467`

Fuente / Source: github.com/OsmanDhaqane/alert-triage-with-elastic-tryhackme-writeup (alert-triage-with-elastic-writeup.pdf)

**¿Cuál es el valor del campo `client.ip` en el índice weblogs? / What is the field value for the client.ip in the weblogs index?**
`203.0.113.55`

Fuente / Source: OsmanDhaqane writeup PDF (github.com/OsmanDhaqane/alert-triage-with-elastic-tryhackme-writeup)

### Tarea 3 / Task 3 — Investigating Web Attacks

**¿Cuántas peticiones POST hizo la IP 203.0.113.55 a proxyLogon.ecp? / How many POST requests did the IP address 203.0.113.55 make to proxyLogon.ecp?**
`3`

**¿Qué user.agent emparejado con la IP 203.0.113.55 hizo las peticiones POST? / Which user.agent paired with the IP address 203.0.113.55 made the POST requests?**
`python-requests/2.25.1`

**¿Cuántos logs contienen el parámetro de query `cmd=` en el campo `url.path`? / How many logs contain the cmd= query parameter in the url.path field?**
`20`

**¿Qué comando se ejecutó usando errorEE.aspx el día Jul 20, 2025 a las 04:45:50.000? / Which command was run utilizing errorEE.aspx on Jul 20, 2025 @ 04:45:50.000?**
`hostname`

Fuente / Source (tarea 3): OsmanDhaqane writeup PDF (github.com/OsmanDhaqane/alert-triage-with-elastic-tryhackme-writeup)

### Tarea 4 / Task 4 — Uncovering Account Activity

**¿Cuál es el `winlog.record_id` del evento de logon 4624 de Administrador? / What is the winlog.record_id of the Administrator 4624 logon event?**
`17166`

**¿Cuál es el `process.pid` del evento Sysmon 1 que ocurrió el Jul 20, 2025 @ 05:11:27.996? / What is the process.pid of the Sysmon 1 event that occurred on Jul 20, 2025 @ 05:11:27.996?**
`964`

**¿Cuál es el `winlog.event_id` para la creación de la nueva cuenta de usuario? / What is the winlog.event_id for the new user account being created?**
`4720`

**¿Cuál es el nombre de la nueva cuenta de usuario? / What is the name of the new user account?**
`svc_backup`

Fuente / Source (tarea 4): OsmanDhaqane writeup PDF (github.com/OsmanDhaqane/alert-triage-with-elastic-tryhackme-writeup)

### Tarea 5 / Task 5 — Exposing Command Execution

**¿Qué comando usa el atacante para añadir la nueva cuenta al grupo "Remote Desktop Users"? / What command does the attacker use to add the new account to the "Remote Desktop Users" group?**
`net localgroup "Remote Desktop Users" svc_backup /add`

**¿Cuál es el `winlog.record_id` del evento de seguridad 4732 cuando el atacante añade el usuario al grupo Administrators? / What is the winlog.record_id of the 4732 Security event when the attacker adds the user to the Administrator group?**
`17254`

**¿Qué comando PowerShell ejecutó el atacante el Jul 20, 2025 @ 05:16:14.628? / What PowerShell command did the attacker run on Jul 20, 2025 @ 05:16:14.628?**
`net group "Domain Admins" /domain`

**¿Cuál es el nombre del archivo que el atacante crea usando el ejecutable Rar.exe? / What is the name of the archive that the attacker creates using the Rar.exe executable?**
`finance_it_archive.rar`

Fuente / Source (tarea 5): OsmanDhaqane writeup PDF (github.com/OsmanDhaqane/alert-triage-with-elastic-tryhackme-writeup)

---

*Documentación para propósitos educativos y registro de CTF.*
*Fuente de respuestas / Answer source: https://github.com/OsmanDhaqane/alert-triage-with-elastic-tryhackme-writeup (alert-triage-with-elastic-writeup.pdf)*
