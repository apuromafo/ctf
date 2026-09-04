# Linux Threat Detection 3 [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `linuxthreatdetection3`
* **Link:** https://tryhackme.com/room/linuxthreatdetection3
* **Objeto:** Detectar las etapas finales de un ataque en Linux mediante logs y auditd: reverse shells, escalada de privilegios, persistencia por cron/systemd y persistencia de cuentas/SSH.

---

## Solucionario de Tareas / Task Solutions

> Última sala de la serie de detección de amenazas en Linux. Cubre reverse shells, inyección de comandos, escalada de privilegios y persistencia.
> Last room of the Linux threat-detection series. Covers reverse shells, command injection, privilege escalation and persistence.

### Tarea 1 / Task 1 — Command Injection & Reverse Shell

**Ejecuta `127.0.0.1 && whoami` en la web app TryPingMe. ¿Qué salida ves después de los resultados del ping? / Run `127.0.0.1 && whoami` in the TryPingMe web app. What output do you see after the ping results?**
`svctrypingme`

**¿Cuál es la flag devuelta en la respuesta de TryPingMe? / What is the flag returned in the TryPingMe response?**
`THM{revshells_practitioner!}`

**Ahora mira los logs de auditd exportados en `/home/ubuntu/scenario`. ¿Qué IP lanzó un reverse shell similar vía TryPingMe? / Now look at the exported auditd logs at `/home/ubuntu/scenario`. Which IP spawned a similar reverse shell via the TryPingMe app?**
`10.14.105.255`

Fuente / Source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/

### Tarea 2 / Task 2 — Privilege Escalation

**¿Qué línea de comando se usó para buscar la palabra clave "pass" en archivos? / Which command line was used to look for the "pass" keyword in files?**
`grep -iR pass .`

**¿Qué línea de comando se usó para escalar privilegios a root? / Which command line was used to escalate privileges to root?**
`su root`

**Mirando el archivo .env detectado, ¿cuál era la contraseña de root? / Looking at the detected .env file, what was the root password?**
`nGql1pQkGa`

Fuente / Source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/

### Tarea 3 / Task 3 — Persistence (Service & Cron)

**¿Qué flag obtienes tras ejecutar el malware que persiste como servicio? / What flag did you get after running the malware persisting as a service?**
`THM{hidden_penguin!}`

**¿Qué flag obtienes tras ejecutar el malware que persiste como cron job? / What flag did you get after running the malware persisting as a cron job?**
`THM{ressurect_on_reboot!}`

Fuente / Source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/

### Tarea 4 / Task 4 — Account & SSH Persistence

**¿Qué usuario fue creado y añadido al grupo sudo? / Which user was created and added to the sudo group?**
`koichi`

**¿Qué archivo fue modificado para permitir persistencia con clave SSH? / Which file was changed to allow SSH key persistence?**
`/root/.ssh/authorized_keys`

Fuente / Source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/

### Tarea 5 / Task 5 — Theory

**¿Existe ransomware de Linux y afecta a organizaciones en todo el mundo? (Yea/Nay) / Does Linux ransomware exist and impact organizations worldwide? (Yea/Nay)**
`Yea`

**¿Deberías aprender amenazas Linux aunque trabajes con Windows? (Yea/Nay) / Should you learn Linux threats even if working with Windows? (Yea/Nay)**
`Yea`

Fuente / Source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/

*Fuente de respuestas / Answer source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/*

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
