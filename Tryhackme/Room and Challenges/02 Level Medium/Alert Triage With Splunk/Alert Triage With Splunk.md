# Alert Triage With Splunk [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `alerttriagewithsplunk`
* **Link:** https://tryhackme.com/room/alerttriagewithsplunk
* **Objeto:** Uso de Splunk para triage de alertas (brute-force SSH en Linux, tarea maliciosa en Windows, web shell) y determinar si cada alerta es un True Positive o False Positive.

---

## Solucionario de Tareas / Task Solutions

> Tres alertas llegan en distintos entornos (Linux, Windows y web). Cada una se triagea con Splunk y se clasifica.
> Three alerts arrive across different environments (Linux, Windows, web). Each is triaged with Splunk and classified.

### Tarea 1 / Task 1 — Linux SSH Brute-Force

**¿Cuántos intentos de inicio de sesión fallidos se hicieron en el usuario john.smith? / How many failed login attempts were made on the user john.smith?**
`500`

**¿Cuál fue la duración del ataque de fuerza bruta en minutos? / What was the duration of the brute force attack in minutes?**
`5`

**¿A qué nombre de usuario pudo escalar privilegios el atacante? / What username was the attacker able to privilege escalate to?**
`root`

**¿Cuál es el nombre de la cuenta de usuario creada por el atacante para persistencia? / What is the name of the user account created by the attacker for persistence?**
`system-utm`

Fuente / Source: https://simontaplin.net/2025/11/28/answers-for-the-tryhackme-alert-triage-with-splunk-room/

### Tarea 2 / Task 2 — Windows Malicious Task

**¿Cuál es el ProcessId del proceso que creó esta tarea maliciosa? / What is the ProcessId of the process that created this malicious task?**
`5816`

**¿Cuál es el nombre del proceso padre del proceso que creó esta tarea maliciosa? / What is the name of the parent process for the process that created this malicious task?**
`cmd.exe`

**¿Qué grupo local enumeró el atacante durante el descubrimiento? / Which local group did the attacker enumerate during discovery?**
`Administrators`

**¿Cuál es el nombre de la estación de trabajo desde la que el Threat Actor inició sesión en este host? / What is the name of the workstation from which the Threat Actor logged into this host?**
`DEV-QA-SERVER`

Fuente / Source: https://simontaplin.net/2025/11/28/answers-for-the-tryhackme-alert-triage-with-splunk-room/

### Tarea 3 / Task 3 — Web Shell (Network)

**¿A qué hora comenzó la actividad de fuerza bruta usando Hydra? / What time did the brute-force activity using Hydra begin?**
`2025-09-14 21:20:27`

**¿Qué user agent usó el atacante al interactuar con el web shell? / Which user agent did the attacker use when interacting with the web shell?**
`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36`

**¿Cuál fue el número de peticiones hechas por el atacante al servidor vía el web shell? / What was the number of requests made by the attacker to the server via the web shell?**
`4`

Fuente / Source: https://simontaplin.net/2025/11/28/answers-for-the-tryhackme-alert-triage-with-splunk-room/

*Fuente de respuestas / Answer source: https://simontaplin.net/2025/11/28/answers-for-the-tryhackme-alert-triage-with-splunk-room/*

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
