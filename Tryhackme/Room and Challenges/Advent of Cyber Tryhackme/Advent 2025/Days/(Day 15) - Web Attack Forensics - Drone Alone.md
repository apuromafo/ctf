# Web Attack Forensics - Drone Alone

| **Dificultad** | Easy | **Tipo** | walkthrough | **Slug** | `day15webattackforensicsdronealone` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) |
| **Sección** | Advent of Cyber Tryhackme |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Splunk / web attack forensics / command injection / Apache access logs / Apache error logs / Sysmon / hello.bat / PowerShell / EncodedCommand |
| **Impacto** | Investigar y reconstruir un ataque de inyección de comandos web con Splunk y Sysmon |

---

**Contexto:** Día 15 del Advent of Cyber 2025. Se usa **Splunk** para investigar un ataque de inyección de comandos a nivel web: se buscan en los logs de acceso de Apache indicadores como cmd.exe, PowerShell e Invoke-Expression, y se identifica el intento de inyección a través de un script CGI vulnerable (hello.bat). Después se revisan los logs de error de Apache, los logs de Sysmon (para ver los procesos que Apache lanzó), y la ejecución de cmd.exe con whoami que confirma la ejecución de comandos interactiva. Finalmente se busca PowerShell con -EncodedCommand, enc y strings Base64 para confirmar si los payloads codificados llegaron a ejecutarse.

## Solucionario

### Día 15: Web Attack Forensics - Drone Alone

**Explicación:**

- **Splunk**: inverstigate web-based command injection attack
- Detect suspicious web requests
     1. Search Apache access logs for indicators like cmd.exe, PowerShell, and Invoke-Expression
     2. Identify command injection attempts througha vulnerable CGI script (hello.bat)

- Check Apache Error logs
- Sysmon logs -> to see what processes Apache spawned
- looking for cmd.exe running whoami -> confirms attacker gained interactive command execution
- Search for PowerShell using -EncodedCommand, enc, Base64 strings; If no results -> encoded payloads did not successfully execute

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the reconnaissance executable file name? | `whoami.exe` |
| 2 | What executable did the attacker attempt to run through the command injection? | `PowerShell.exe` |

---

**Metodología:** Se arrancó por los Apache access logs buscando patrones de inyección (cmd.exe, PowerShell, Invoke-Expression) y el script CGI vulnerable (hello.bat). Se cruzaron esos hallazgos con los error logs de Apache y los eventos de Sysmon para ver qué procesos lanzó Apache: primero `whoami.exe` (reconocimiento) y después `PowerShell.exe` a través de la inyección. La búsqueda de -EncodedCommand/enc/Base64 determinó si los payloads codificados llegaron a ejecutarse.
**Learning chain:** Splunk (búsqueda en Apache access logs) -> indicadores (cmd.exe, PowerShell, Invoke-Expression) -> script CGI hello.bat -> Apache error logs -> Sysmon (procesos hijos) -> whoami.exe (recon) -> PowerShell.exe (inyección) -> -EncodedCommand/Base64

Cadena de ataque / Attack Chain:
```
request malicioso a hello.bat -> command injection (cmd.exe / PowerShell / Invoke-Expression) en access logs -> Apache spawn de procesos (Sysmon) -> whoami.exe (reconocimiento) -> PowerShell.exe (intento de payload) -> -EncodedCommand/enc/Base64 (éxito o no de la ejecución)
```

**Lección:** *La forense de ataques web se apoya en correlacionar tres fuentes: los access logs (quién pidió qué), los error logs (qué falló) y Sysmon (qué procesos se lanzaron); la cadena whoami -> PowerShell encodificado es la firma clásica de una inyección de comandos.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application, T1059.001 - PowerShell, T1059.003 - Windows Command Shell

**Fuente:** [TryHackMe - Web Attack Forensics - Drone Alone](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.