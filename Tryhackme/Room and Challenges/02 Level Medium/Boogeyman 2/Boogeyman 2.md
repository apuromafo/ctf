# Boogeyman 2
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `boogeyman2` |
| **Link** | [TryHackMe](https://tryhackme.com/room/boogeyman2) |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | olevba, oledump, strings, Volatility 3 (psscan, pstree, filescan, dumpfiles), Wireshark, dnSpy, schtasks, análisis de macro de Word, memory forensics |
| **Impacto** | Desvela la cadena completa de la segunda infección del Boogeyman: macro maliciosa, stage 2 JavaScript, persistencia vía tarea programada y C2, mediante análisis estático del documento y forensia de memoria. |
---
**Contexto:** Maxine, RRHH de Quick Logistics LLC, abre un currículum adjunto a un email y su estación (WKSTN-2961) queda comprometida. La sala mezcla análisis de phishing (email + documento con macro) y forensia de memoria con Volatility 3 para seguir cada etapa: payload inicial, descargas de stage 2, binario de C2 y persistencia con una tarea programada (Empire stager/Sharpire).
## Solucionario
### Task 1: Introduction
**Explicación:** Tras la primera intrusión, Quick Logistics mejoró sus defensas, pero el Boogeyman vuelve con nuevas tácticas. Se proporcionan como artefactos el email phishing (`Resume — Application for Junior IT Analyst Role.eml`), el documento infectado y un volcado de memoria de la víctima.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Comienza el análisis de los artefactos. | `No answer needed` |
### Task 2: Email & Endpoint Analysis
**Explicación:** Se analiza primero el email: el campo `From` da el remitente y los destinatarios del email nos llevan a la víctima. Con `olevba` sobre el doc adjunto se detecta la macro `NewMacros`, que descarga un stage 2 (un `.js`) desde una URL maliciosa y lo ejecuta con `wscript.exe`. Para las preguntas de procesos y PIDs se usa **Volatility 3** sobre `WKSTN-2961.raw`. Con `windows.psscan` se encuentra el proceso que ejecutó el payload (PID y PPID), con `windows.pstree` el proceso hijo que establece C2, y con `filescan`/`dumpfiles` las rutas de `update.png`, `update.exe` y `C:\Windows\Tasks\updater.exe`. El binario `updater.exe` es un Empire stager; mediante `strings`/`dnSpy` se halla la IP:puerto del C2 (`128.199.95.189:8080`) y el comando `schtasks` usado para mantener la persistencia. En el hivelist/dumpregistry también se recupera la ruta exacta del adjunto en la caché de Outlook.

```bash
olevba Resume_WesleyTaylor.doc
olevba -c Resume_WesleyTaylor.doc
vol -f WKSTN-2961.raw windows.psscan
vol -f WKSTN-2961.raw windows.pstree
vol -f WKSTN-2961.raw filescan
strings WKSTN-2961.raw | grep "files.boogeymanisback.lol"
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué email se usó para enviar el phishing? | `westaylor23@outlook.com` |
| 2 | ¿Cuál es la dirección de email de la víctima? | `maxine.beck@quicklogisticsorg.onmicrosoft.com` |
| 3 | ¿Cuál es el nombre del adjunto malicioso del email? | `Resume_WesleyTaylor.doc` |
| 4 | ¿Cuál es el hash MD5 del adjunto malicioso? | `52c4384a0b9e248b95804352ebec6c5b` |
| 5 | ¿Qué URL se usa para descargar el payload stage 2? | `https://files.boogeymanisback.lol/aa2a9c53cbb80416d3b47d85538d9971/update.png` |
| 6 | ¿Cuál es el nombre del proceso que ejecutó el payload stage 2 descargado? | `wscript.exe` |
| 7 | ¿Cuál es la ruta completa del payload stage 2 malicioso? | `C:\ProgramData\update.js` |
| 8 | ¿Cuál es el PID del proceso que ejecutó el payload stage 2? | `4260` |
| 9 | ¿Cuál es el PID padre del proceso que ejecutó el payload stage 2? | `1124` |
| 10 | ¿Qué URL se usa para descargar el binario malicioso ejecutado por el stage 2? | `https://files.boogeymanisback.lol/aa2a9c53cbb80416d3b47d85538d9971/update.exe` |
| 11 | ¿Cuál es el PID del proceso malicioso usado para establecer la conexión C2? | `6216` |
| 12 | ¿Cuál es la ruta completa del proceso malicioso usado para establecer la conexión C2? | `C:\Windows\Tasks\updater.exe` |
| 13 | ¿Cuál es la dirección IP y el puerto de la conexión C2 iniciada por el binario malicioso? (Formato: IP:puerto) | `128.199.95.189:8080` |
| 14 | ¿Cuál es la ruta completa del adjunto malicioso del email según el volcado de memoria? | `C:\Users\maxine.beck\AppData\Local\Microsoft\Windows\INetCache\Content.Outlook\WQHGZCFI\Resume_WesleyTaylor (002).doc` |
| 15 | El atacante implantó una tarea programada justo después de establecer el callback de C2. ¿Cuál es el comando completo usado por el atacante para mantener el acceso persistente? | `schtasks /Create /F /SC DAILY /ST 09:00 /TN Updater /TR 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NonI -W hidden -c "IEX ([Text.Encoding]::UNICODE.GetString([Convert]::FromBase64String((gp HKCU:\Software\Microsoft\Windows\CurrentVersion debug).debug)))"'` |
---
**Metodología:** DFIR/blue team: análisis estático del documento (macros) + forensia de memoria (Volatility 3) para reconstruir la matanza: MalDoc → stage 2 → C2 → persistencia.
**Learning chain:** Análisis de headers de email → extracción de macros (olevba/oledump) → correlación de IOCs → forensia de memoria (psscan/pstree/filescan/dumpfiles/registry) → análisis del malware (strings/dnSpy) → persistencia con schtasks.
**MITRE ATT&CK:** T1566.001 (Spearphishing Attachment), T1059.001 (PowerShell), T1059.007 (JavaScript), T1105 (Ingress Tool Transfer), T1053.005 (Scheduled Task), T1071.001 (Web Protocols C2), T1543.003 (Windows Service/reg).
**Fuente:** [TryHackMe - Boogeyman 2](https://tryhackme.com/room/boogeyman2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
