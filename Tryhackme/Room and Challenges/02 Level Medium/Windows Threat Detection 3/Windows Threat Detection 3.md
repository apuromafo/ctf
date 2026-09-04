# Windows Threat Detection 3 [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `windowsthreatdetection3`
* **Link:** https://tryhackme.com/room/windowsthreatdetection3
* **Objeto:** Detectar Command and Control (C2) y cómo los hackers mantienen acceso a una máquina Windows: malware C2, backdoors, servicios, tareas programadas y técnicas de persistencia.

---

## Solucionario de Tareas / Task Solutions

> Tercera sala de la serie de detección de amenazas en Windows. Enfoque en C2, backdoor users, servicios, scheduled tasks y persistencia.
> Third room of the Windows threat-detection series. Focus on C2, backdoor users, services, scheduled tasks and persistence.

### Tarea 1 / Task 1 — C2 Malware

**¿Qué archivo sospechoso descargó el usuario? / Which suspicious archive did the user download?**
`URGENT!.zip`

**¿Dónde escondieron los atacantes el archivo del malware C2? / Where did the attackers hide the C2 malware file?**
`C:\Users\Administrator\AppData\Roaming\update.exe`

**¿Cuál es el dominio del servidor de Command and Control? / What is the domain of the Command and Control server?**
`route.m365officesync.workers.dev`

Fuente / Source: https://simontaplin.net/2025/07/23/answers-for-the-tryhackme-windows-threat-detection-3-room/

### Tarea 2 / Task 2 — Backdoor User

**2.1 — Número de intentos de inicio de sesión previos antes del acceso del atacante (según la secuencia de la sala). / 2.1 — Number of prior login attempts before the attacker's access (per room sequence).**
`6`

**Después del inicio de sesión exitoso, ¿qué usuario backdoor creó el atacante? / After the successful login, which backdoor user did the attacker create?**
`support`

**¿A qué grupo privilegiado se añadió el usuario backdoor? / Which privileged group was the backdoor user added to?**
`Administrators`

Fuente / Source: https://simontaplin.net/2025/07/23/answers-for-the-tryhackme-windows-threat-detection-3-room/

### Tarea 3 / Task 3 — Service & Scheduled Task Persistence

**¿Qué servicio de Windows se creó para persistir el malware Nessie? / Which Windows service was created to persist the Nessie malware?**
`Data Protection Service`

**¿Qué tarea programada se creó para persistir el malware Troy? / Which scheduled task was created to persist the Troy malware?**
`AmazonSync`

**¿Qué flag obtienes tras encontrar y ejecutar el malware Troy? / What flag do you get after finding and running the Troy malware?**
`THM{c2_is_on_schedule!}`

Fuente / Source: https://simontaplin.net/2025/07/23/answers-for-the-tryhackme-windows-threat-detection-3-room/

### Tarea 4 / Task 4 — Additional Malware (Odin & Kitten)

**¿Cuál es la imagen del proceso padre del malware "Odin"? / What is the parent process image of the "Odin" malware?**
`c:\windows\explorer.exe`

**¿Cuál es la última línea que genera el malware "Odin"? / What is the last line that the "Odin" malware outputs?**
`Done doing bad stuff!`

**¿Qué flag obtienes tras encontrar y ejecutar el malware "Kitten"? / What flag do you get after finding and running the "Kitten" malware?**
`THM{persisting_in_basket!}`

Fuente / Source: https://simontaplin.net/2025/07/23/answers-for-the-tryhackme-windows-threat-detection-3-room/

### Tarea 5 / Task 5 — Theory

**¿Cuál es la mayor amenaza para la mayoría de redes corporativas Windows? / What is the biggest threat to most corporate Windows networks?**
`Ransomware`

**¿En qué etapa es mejor detectar y detener el ataque (p. ej. Exfiltration)? / At which stage is it best to detect and stop the attack (e.g. Exfiltration)?**
`Initial Access`

Fuente / Source: https://simontaplin.net/2025/07/23/answers-for-the-tryhackme-windows-threat-detection-3-room/

*Fuente de respuestas / Answer source: https://simontaplin.net/2025/07/23/answers-for-the-tryhackme-windows-threat-detection-3-room/*

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
