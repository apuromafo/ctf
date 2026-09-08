# Boogeyman 3
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `boogeyman3` |
| **Link** | [TryHackMe](https://tryhackme.com/room/boogeyman3) |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Elasticsearch/Kibana, Sysmon (Event IDs 1, 3, 11), análisis de procesos (mshta, xcopy, rundll32, fodhelper), mimikatz, DCSync, Pass-the-Hash, tareas programadas, ransomware |
| **Impacto** | Investiga el cierre del caso Boogeyman en un SOC (ELK): desde el HTA inicial de phishing hasta el dominio completo, con UAC bypass, volcado de credenciales, movimiento lateral Pass-the-Hash, DCSync y despliegue de ransomware. |
---
**Contexto:** Quick Logistics contrata un MSSP para su SOC; el CEO (Evan Hutchinson, WKSTN-0051) abre un .hta disfrazado de PDF (`ProjectFinancialSummary_Q3.pdf`) y compromete la máquina. La sala es un capstone de caza de amenazas en Kibana (Sysmon) que sigue toda la cadena: implantación de `review.dat`, persistencia, C2, UAC bypass, volcado de credenciales, lateral movement y ransomware.
## Solucionario
### Task 1: Introduction
**Explicación:** El Boogeyman vuelve por tercera vez. Se proporcionan los logs de la infraestructura (ELK) para investigar la intrusión del CEO y su extensión al dominio.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Comienza la investigación en la plataforma de logs. | `No answer needed` |
### Task 2: SOC Investigation
**Explicación:** Se filtra por el nombre del archivo (`*ProjectFinancialSummary_Q3.pdf`) y se ve que `mshta.exe` (PID 6392) ejecuta el HTA inicial. Siguiendo con `process.parent.pid: 6392` aparecen la copia con `xcopy.exe` (implantación de `D:\review.dat` en el Temp del usuario), la ejecución con `rundll32.exe` (registro del DLL) y la creación de una **tarea programada** llamada `Review` (persistencia diaria a las 6:00). En Event ID 3 se descubre la conexión C2 `165.232.170.151:80`. El atacante, ya administrador local, ejecuta el UAC bypass con **fodhelper.exe**, descarga **mimikatz** y vuelca credenciales en claro y hashes (NTLM). Con Pass-the-Hash se mueve lateralmente (wsmprovhost.exe) al servidor WKSTN-1327 donde está `IT_Automation.ps1` con credenciales de dominio en claro; allí se vuelcan más hashes con DCSync (`administrator:00f80f...` y el usuario `backupda`). Finalmente descarga el ransomware `ransomboogey.exe` desde `http://ff.sillytechninja.io/`.

```text
Search: *ProjectFinancialSummary_Q3.pdf        -> mshta.exe PID 6392
Search: process.parent.pid : 6392             -> xcopy, rundll32, Register-ScheduledTask Review
Search: winlog.event_id:3                      -> 165.232.170.151:80
Search: process.parent.command_line:*review.dat*
Search: winlog.event_id:11                     -> archivos creados (mimikatz, ransomware)
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el PID del proceso que ejecutó el payload stage 1 inicial? | `6392` |
| 2 | El payload stage 1 intentó implantar un archivo en otra ubicación. ¿Cuál es el valor completo de la línea de comandos de esta ejecución? | `"C:\Windows\System32\xcopy.exe" /s /i /e /h D:\review.dat C:\Users\EVAN~1.HUT\AppData\Local\Temp\review.dat` |
| 3 | El archivo implantado acabó siendo usado y ejecutado por el payload stage 1. ¿Cuál es el valor completo de la línea de comandos de esta ejecución? | `"C:\Windows\System32\rundll32.exe" D:\review.dat,DllRegisterServer` |
| 4 | El payload stage 1 estableció un mecanismo de persistencia. ¿Cuál es el nombre de la tarea programada creada por el script malicioso? | `Review` |
| 5 | La ejecución del archivo implantado dentro de la máquina inició una posible conexión C2. ¿Cuál es la IP y el puerto usados por esta conexión? (Formato: IP:puerto) | `165.232.170.151:80` |
| 6 | El atacante descubrió que el acceso actual es de administrador local. ¿Cuál es el nombre del proceso usado por el atacante para ejecutar un bypass de UAC? | `fodhelper.exe` |
| 7 | ¿Qué enlace de GitHub usó el atacante para descargar mimikatz? | `https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip` |
| 8 | El atacante volcó las credenciales de esta máquina. ¿Cuál es el nombre de usuario y el hash NTLM volcados? (Formato: usuario:hash) | `itadmin:F84769D250EB95EB2D7D8B4A1C5613F2` |
| 9 | ¿Qué archivo contenía credenciales en claro que el atacante descubrió en la segunda máquina? | `IT_Automation.ps1` |
| 10 | Con esas credenciales, el atacante se movió lateralmente a la segunda máquina. ¿Qué credenciales de dominio en claro se descubrieron? (Formato: dominio\usuario:contraseña) | `QUICKLOGISTICS\allan.smith:Tr!ckyP@ssw0rd987` |
| 11 | ¿En qué máquina se ejecutó el ransomware? | `WKSTN-1327` |
| 12 | ¿Qué proceso fue ejecutado por el atacante para el movimiento lateral a la segunda máquina? | `wsmprovhost.exe` |
| 13 | El atacante volcó los hashes en esta segunda máquina. ¿Cuál es el nombre de usuario y el hash de las credenciales recién volcadas? (Formato: usuario:hash) | `administrator:00f80f2538dcb54e7adc715c0e7091ec` |
| 14 | Tras acceder al controlador de dominio, el atacante intentó volcar hashes mediante un ataque DCSync. Aparte de la cuenta administrator, ¿qué cuenta volcó el atacante? | `backupda` |
| 15 | Tras volcar los hashes, el atacante intentó descargar otro archivo remoto para ejecutar ransomware. ¿Qué enlace usó el atacante para descargar el binario del ransomware? | `http://ff.sillytechninja.io/ransomboogey.exe` |
---
**Metodología:** Caza de amenazas en SIEM/EDR (Kibana + Sysmon): filtrado por procesos, correlación de Event IDs (1 proceso, 3 red, 11 archivo) y análisis de la cadena de ataque completa.
**Learning chain:** HTA/phishing → implantación de payload → persistencia (scheduled task) → C2 → UAC bypass → dumps de credenciales/mimikatz → lateral movement (Pass-the-Hash/WinRM) → DCSync → ransomware.
**MITRE ATT&CK:** T1566.001 (Spearphishing Attachment), T1204.002 (User Execution: Malicious File), T1053.005 (Scheduled Task), T1071.001 (Web Protocols C2), T1548.002 (Bypass User Account Control), T1003.001 (LSASS Memory) / T1003.006 (DCSync), T1550.002 (Pass-the-Hash), T1021.006 (Windows Remote Management), T1486 (Data Encrypted for Impact).
**Fuente:** [TryHackMe - Boogeyman 3](https://tryhackme.com/room/boogeyman3)