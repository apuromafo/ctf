# Linux Threat Detection 3

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Premium (requiere suscripción) | linuxthreatdetection3 | https://tryhackme.com/room/linuxthreatdetection3 | Linux / Threat Detection | Writeup de thmrevenant (GitHub) / simontaplin.net | auditd, TryPingMe, reverse shell, grep -iR, su root, .env, cron, systemd, SSH authorized_keys | Detección de etapas finales de un ataque Linux |

> **Objeto:** Detectar las etapas finales de un ataque en Linux mediante logs y auditd: reverse shells, escalada de privilegios, persistencia por cron/systemd y persistencia de cuentas/SSH.

---

**Contexto:** La sala **Linux Threat Detection 3** es la última de la serie de detección de amenazas en Linux (Premium). Cubre las etapas finales de un ataque: inyección de comandos en la web app **TryPingMe** y reverse shell, escalada de privilegios (`grep -iR pass .`, `su root`, contraseña en `.env`), persistencia por servicio systemd y cron job, persistencia de cuentas/SSH (`authorized_keys`) y una parte teórica sobre ransomware en Linux. La reconstrucción se apoya en los logs de auditd exportados en `/home/ubuntu/scenario`.

## Solucionario

> Última sala de la serie de detección de amenazas en Linux. Cubre reverse shells, inyección de comandos, escalada de privilegios y persistencia.
> Last room of the Linux threat-detection series. Covers reverse shells, command injection, privilege escalation and persistence.

### Task 1: Command Injection & Reverse Shell
**Explicación:**

Se inyecta el comando en la web app TryPingMe y se comprueba la salida tras los resultados del ping y la flag devuelta; después se busca en los logs de auditd la IP que lanzó un reverse shell similar.

**Ejecuta `127.0.0.1 && whoami` en la web app TryPingMe. ¿Qué salida ves después de los resultados del ping? / Run `127.0.0.1 && whoami` in the TryPingMe web app. What output do you see after the ping results?**
`svctrypingme`

**¿Cuál es la flag devuelta en la respuesta de TryPingMe? / What is the flag returned in the TryPingMe response?**
`THM{revshells_practitioner!}`

**Ahora mira los logs de auditd exportados en `/home/ubuntu/scenario`. ¿Qué IP lanzó un reverse shell similar vía TryPingMe? / Now look at the exported auditd logs at `/home/ubuntu/scenario`. Which IP spawned a similar reverse shell via the TryPingMe app?**
`10.14.105.255`

Fuente / Source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/

### Task 2: Privilege Escalation
**Explicación:**

Se localiza el comando usado para buscar la palabra clave "pass" en los archivos, la línea de escalada a root y la contraseña de root encontrada en el archivo `.env`.

**¿Qué línea de comando se usó para buscar la palabra clave "pass" en archivos? / Which command line was used to look for the "pass" keyword in files?**
`grep -iR pass .`

**¿Qué línea de comando se usó para escalar privilegios a root? / Which command line was used to escalate privileges to root?**
`su root`

**Mirando el archivo .env detectado, ¿cuál era la contraseña de root? / Looking at the detected .env file, what was the root password?**
`nGql1pQkGa`

Fuente / Source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/

### Task 3: Persistence (Service & Cron)
**Explicación:**

Se ejecutan los malwares que persisten como servicio systemd y como cron job, obteniendo sus respectivas flags.

**¿Qué flag obtienes tras ejecutar el malware que persiste como servicio? / What flag did you get after running the malware persisting as a service?**
`THM{hidden_penguin!}`

**¿Qué flag obtienes tras ejecutar el malware que persiste como cron job? / What flag did you get after running the malware persisting as a cron job?**
`THM{ressurect_on_reboot!}`

Fuente / Source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/

### Task 4: Account & SSH Persistence
**Explicación:**

Se identifica el usuario creado y añadido al grupo sudo, y el archivo modificado para habilitar la persistencia con clave SSH.

**¿Qué usuario fue creado y añadido al grupo sudo? / Which user was created and added to the sudo group?**
`koichi`

**¿Qué archivo fue modificado para permitir persistencia con clave SSH? / Which file was changed to allow SSH key persistence?**
`/root/.ssh/authorized_keys`

Fuente / Source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/

### Task 5: Theory
**Explicación:**

Parte teórica: se responde si existe ransomware de Linux con impacto organizacional global y si conviene aprender amenazas Linux incluso trabajando con Windows.

**¿Existe ransomware de Linux y afecta a organizaciones en todo el mundo? (Yea/Nay) / Does Linux ransomware exist and impact organizations worldwide? (Yea/Nay)**
`Yea`

**¿Deberías aprender amenazas Linux aunque trabajes con Windows? (Yea/Nay) / Should you learn Linux threats even if working with Windows? (Yea/Nay)**
`Yea`

Fuente / Source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/

*Fuente de respuestas / Answer source: https://simontaplin.net/2025/10/15/answers-for-the-tryhackme-threat-detection-3-room/*

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | ¿Qué salida ves después de los resultados del ping al ejecutar `127.0.0.1 && whoami`? | `svctrypingme` |
| 1.2 | ¿Cuál es la flag devuelta en la respuesta de TryPingMe? | `THM{revshells_practitioner!}` |
| 1.3 | ¿Qué IP lanzó un reverse shell similar vía TryPingMe? | `10.14.105.255` |
| 2.1 | ¿Qué línea de comando se usó para buscar la palabra clave "pass" en archivos? | `grep -iR pass .` |
| 2.2 | ¿Qué línea de comando se usó para escalar privilegios a root? | `su root` |
| 2.3 | Mirando el archivo .env detectado, ¿cuál era la contraseña de root? | `nGql1pQkGa` |
| 3.1 | ¿Qué flag obtienes tras ejecutar el malware que persiste como servicio? | `THM{hidden_penguin!}` |
| 3.2 | ¿Qué flag obtienes tras ejecutar el malware que persiste como cron job? | `THM{ressurect_on_reboot!}` |
| 4.1 | ¿Qué usuario fue creado y añadido al grupo sudo? | `koichi` |
| 4.2 | ¿Qué archivo fue modificado para permitir persistencia con clave SSH? | `/root/.ssh/authorized_keys` |
| 5.1 | ¿Existe ransomware de Linux y afecta a organizaciones en todo el mundo? (Yea/Nay) | `Yea` |
| 5.2 | ¿Deberías aprender amenazas Linux aunque trabajes con Windows? (Yea/Nay) | `Yea` |

---

**Metodología:** 1. Command injection & reverse shell: pivotar `127.0.0.1 && whoami` en TryPingMe y contrastar con los logs auditd (`/home/ubuntu/scenario`) para hallar la IP del reverse shell. 2. Privilege escalation: búsqueda de "pass" (`grep -iR pass .`), escalada `su root` y contraseña en `.env`. 3. Persistence: ejecución de los malwares de servicio systemd y cron. 4. Account & SSH persistence: cuenta en sudo y `authorized_keys`. 5. Teoría sobre ransomware Linux.

**Learning chain:** Command injection en TryPingMe → reverse shell (10.14.105.255) → credenciales ocultas (grep pass, .env) → `su root` → persistencia systemd/cron → persistencia cuentas/SSH → teoría ransomware.

**Lección:** *La última milla del ataque Linux se detecta en auditd, la web app vulnerable y la persistencia: una inyección de comandos en una app web termina en root con servicio systemd, cron y claves SSH autorizadas si no se monitorizan esos tres planos.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059.004 Command and Scripting Interpreter: Unix Shell · T1548.002 Abuse Elevation Control Mechanism: Sudo and Sudo Caching · T1552.001 Unsecured Credentials: Credentials in Files · T1543.002 Create or Modify System Process: Systemd Service · T1053.003 Scheduled Task/Job: Cron · T1098.004 Account Manipulation: SSH Authorized Keys · T1136.001 Create Account: Local Account.

**Fuente:** [TryHackMe - Linux Threat Detection 3](https://tryhackme.com/room/linuxthreatdetection3)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.