# Web Attack Forensics - Drone Alone [EASY]

### Información de la Sala / Room Information

| Propiedad / Property | Valor / Value |
| --- | --- |
| **Nombre / Name** | Web Attack Forensics - Drone Alone |
| **Evento / Event** | Advent of Cyber 2025 — Día 15 |
| **Sala / Room URL** | https://tryhackme.com/room/adventofcyber25 |
| **Dificultad / Difficulty** | Easy |
| **Descripción / Description** | Día 15 del calendario AoC 2025 (Web Attack Forensics - Drone Alone). Solución/respuestas del reto diario. |

---


- **Splunk**: inverstigate web-based command injection attack
- Detect suspicious web requests
     1. Search Apache access logs for indicators like cmd.exe, PowerShell, and Invoke-Expression
     2. Identify command injection attempts througha vulnerable CGI script (hello.bat)

- Check Apache Error logs
- Sysmon logs -> to see what processes Apache spawned
- looking for cmd.exe running whoami -> confirms attacker gained interactive command execution
- Search for PowerShell using -EncodedCommand, enc, Base64 strings; If no results -> encoded payloads did not successfully execute

## Respuestas / Answers
- What is the reconnaissance executable file name? : `whoami.exe`
- What executable did the attacker attempt to run through the command injection? : `PowerShell.exe`

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
