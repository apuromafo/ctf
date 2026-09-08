# Investigating Windows 2.0

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | investigatingwindows2 |
| **Link** | [TryHackMe](https://tryhackme.com/room/investigatingwindows2) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=investigatingwindows2` + walkthrough austin-lai) |
| **Componentes** | Registry (Plugin), Scheduled Tasks, WMI, SysInternals (Procexp, ProcMon, Loki), PowerShell, YARA, Windows Event Logs |
| **Impacto** | Alto — investigación forense de un endpoint comprometido con múltiples backdoors en persistencia y dual-use tools |

---

**Contexto:** Room de investigaciones (reto, no hay walkthrough oficial paso a paso; las preguntas "saltan de un lado a otro"). Partes de ~30 preguntas sobre un Windows comprometido. Requiere conocimientos básicos de registry, PowerShell, scripting y Windows Events, prestando atención a los **tiempos de los eventos**. En el Desktop hay una carpeta **Tools** con las SysInternals: Process Explorer (procexp64.exe), ProcMon, Loki (yo anti-malware), Process Hacker, etc.

Las respuestas se obtienen principalmente de: (1) un script malicioso con WMI persistent en el sistema que cae en `C:\TMP`, (2) el escaneo de **Loki** y (3) el seguimiento de procesos con **ProcMon/ProcExp**.

## Solucionario

### Task 1: Investigación inicial — Registry y Scheduled Task

**Explicación:** La pregunta 1 busca la clave de registro que contiene el mismo comando que se ejecuta en una tarea programada. En el Task Scheduler hay una tarea que ejecuta un comando; ese mismo comando vive como valor de registro. Se localiza en:

```
HKCU\Environment\UserIntMprLogonScript
```

Esta clave (relacionada con el logon y los scripts de usuario) se usa como **persistencia** para lanzar el comando al inicio de sesión.

| # | Pregunta | Respuesta |
| 1 | What registry key contains the same command that is executed within a scheduled task? | `HKCU\Environment\UserIntMprLogonScript` |

---

### Task 2: Tools de análisis

**Explicación:** En la carpeta "Tools" del Desktop están las herramientas de análisis. La herramienta SysInternals por excelencia para ver procesos es **Process Explorer** (`procexp64.exe`). Es precisamente la herramienta que se cierra inmediatamente si se intenta abrir (porque el malware la vigila y la mata o porque el WMI la bloquea).

| # | Pregunta | Respuesta |
| 2 | What analysis tool will immediately close if/when you attempt to launch it? | `procexp64.exe` |

---

### Task 3: El backdoor WMI

**Explicación:** El script malicioso (`LaunchBeaconingBackdoor`) está escrito en **VBScript** y usa WMI. La consulta WQL completa asociada al script es:

```
SELECT * FROM Win32_ProcessStartTrace WHERE ProcessName = 'procexp64.exe'
```

Es decir: el backdoor "ve" en tiempo real cuándo se lanza Process Explorer y actúa en consecuencia (por eso la herramienta se cierra). El otro script presente se llama `LaunchBeaconingBackdoor`. El script referencia a la compañía de software **Motobit Software**, con dos webs asociadas (`http://www.motobit.com` y `http://motobit.cz`). Buscando en internet el nombre del script de la Q5 junto con una de esas webs, aparece el script de ataque **WMIBackdoor.ps1** (un PoC público de persistencia vía WMI).

| # | Pregunta | Respuesta |
| 3 | What is the full WQL Query associated with this script? | `SELECT * FROM Win32_ProcessStartTrace WHERE ProcessName = 'procexp64.exe'` |
| 4 | What is the script language? | `VBScript` |
| 5 | What is the name of the other script? | `LaunchBeaconingBackdoor` |
| 6 | What is the name of the software company visible within the script? | `Motobit Software` |
| 7 | What 2 websites are associated with this software company? (answer, answer) | `http://www.motobit.com, http://motobit.cz` |
| 8 | Search online for the name of the script from Q5 and one of the websites from the previous answer. What attack script comes up in your search? | `WMIBackdoor.ps1` |
| 9 | What is the location of this file within the local machine? | `C:\TMP` |

---

### Task 4: Temporización de procesos con ProcMon

**Explicación:** Con Process Monitor (ProcMon) se observa que dos procesos se abren y cierran muy rápido cada pocos minutos: **mim.exe** y **powershell.exe**. Su proceso padre es **svchost.exe** (aunque en el WMI era `svchost.exe`). La primera operación que registra ProcMon para el primero de esos procesos es **Process Start**. En la pestaña "Event" de la primera ocurrencia se muestran 4 campos: **Parent PID, Command line, Current directory, Environment**.

En las operaciones de disco no aparece ningún proceso inusual (No process): todo el movimiento de archivos proviene de `C:\TMP`.

| # | Pregunta | Respuesta |
| 10 | Which 2 processes open and close very quickly every few minutes? (answer, answer) | `mim.exe, powershell.exe` |
| 11 | What is the parent process for these 2 processes? | `svchost.exe` |
| 12 | What is the first operation for the first of the 2 processes? | `Process Start` |
| 13 | Inspect the properties for the 1st occurrence of this process. In the Event tab what are the 4 pieces of information displayed? (answer, answer, answer, answer) | `Parent PID, Command line, Current directory, Environment` |
| 14 | Inspect the disk operations, what is the name of the unusual process? | `No process` |

---

### Task 5: Análisis con Loki

**Explicación:** Ejecutando **Loki** (del kit "Tools") se obtiene el volcado de detecciones que responde a las preguntas 15-28. También se puede abrir y examinar directamente el contenido de los scripts. Hallazgos de Loki:

- El módulo después de `Init` es **WMIScan**.
- El `eventFilter` del 2º warning es **ProcessStartTrigger**.
- La clase del 4º warning es **__FilterToConsumerBinding** (clase WMI que une filtro y consumidor).
- Alerta binaria con `FIRST_BYTES` `4d5a90000300000004000000ffff0000b8000000`: **nbtscan.exe**.
- La descripción del "reason 1" es **Known Bad / Dual use classics**.
- Binario marcado como **APT Cloaked**: **p.exe**.
- Los matches `(str1, str2)`: **psexesvc.exe, Sysinternals PsExec**.
- Binario asociado a `somethingwindows.dmp` en `C:\TMP`: **schtasks-backdoor.ps1**.
- Binario cifrado similar a un trojan: **xCmd.exe**.
- Binario que se hace pasar por un proceso legítimo de Windows (svchost): ruta completa **C:\Users\Public\svchost.exe**.
- La ruta de la versión legítima (googleando el nombre de la Q24): **C:\Windows\System32**.
- Otra descripción para "reason 1": **Stuff running where it normally shouldn't**.
- Archivo etiquetado como hacktool en la misma carpeta: **en-US.js**.
- El Yara Rule MATCH se llama **CACTUSTORCH** (patrón del framework CACTUSTORCH).
- El binario que NO apareció en los resultados de Loki: **mim.exe**.

| # | Pregunta | Respuesta |
| 15 | Run Loki. Inspect the output. What is the name of the module after `Init`? | `WMIScan` |
| 16 | Regarding the 2nd warning, what is the name of the eventFilter? | `ProcessStartTrigger` |
| 17 | For the 4th warning, what is the class name? | `__FilterToConsumerBinding` |
| 18 | What binary alert has the following 4d5a90000300000004000000ffff0000b8000000 as FIRST_BYTES? | `nbtscan.exe` |
| 19 | According to the results, what is the description listed for reason 1? | `Known Bad / Dual use classics` |
| 20 | Which binary alert is marked as APT Cloaked? | `p.exe` |
| 21 | What are the matches? (str1, str2) | `psexesvc.exe, Sysinternals PsExec` |
| 22 | Which binary alert is associated with somethingwindows.dmp found in C:\TMP? | `schtasks-backdoor.ps1` |
| 23 | Which binary is encrypted that is similar to a trojan? | `xCmd.exe` |
| 24 | There is a binary that can masquerade itself as a legitimate core Windows process/image. What is the full path of this binary? | `C:\Users\Public\svchost.exe` |
| 25 | What is the full path location for the legitimate version? | `C:\Windows\System32` |
| 26 | What is the description listed for reason 1? | `Stuff running where it normally shouldn't` |
| 27 | There is a file in the same folder location that is labeled as a hacktool. What is the name of the file? | `en-US.js` |
| 28 | What is the name of the Yara Rule MATCH? | `CACTUSTORCH` |
| 29 | Which binary didn't show in the Loki results? | `mim.exe` |

---

### Task 6: Completar la regla YARA

**Explicación:** Para detectar el binario que Loki no detectó (mim.exe) hay que completar el fichero de regla YARA de la carpeta Tools con 3 strings. Consultando el binario con `strings64.exe` (SysInternals) se obtienen las cadenas:

| # | Pregunta | Respuesta |
| 30 | Complete the yar rule file located within the Tools folder on the Desktop. What are 3 strings to complete the rule in order to detect the binary Loki didn't hit on? (answer, answer, answer) | `mk.ps1, mk.exe, v2.0.50727` |

---

**Metodología:** DFIR / Incident Response sobre host Windows (triaje forense): correlación de registry + scheduled tasks, análisis de scripts con WMI, escaneo con herramientas anti-malware (Loki) y trazabilidad de procesos con SysInternals, respetando la línea temporal de eventos.

**Learning chain:** Persistencia vía `UserInitMprLogonScript` → backdoor WMI con `Win32_ProcessStartTrace` (mata procexp64) → `C:\TMP` → procesos `mim.exe`/`powershell.exe` bajo `svchost.exe` → detección con Loki (nbtscan, xCmd, CACTUSTORCH, psexec, svchost falso) → YARA manual para el binario no detectado (mim.exe).

**MITRE ATT&CK:** T1547.001 – Boot/Logon Autostart Execution: Registry Run Keys / Startup Folder; T1053.005 – Scheduled Task; T1546.003 – Event Triggered Execution: WMI Event Subscription; T1047 – Windows Management Instrumentation; T1036 – Masquerading; T1559 – Inter-Process Communication (WMI); T1219 – Remote Access Software (PsExec/xCmd).

**Fuente:** [TryHackMe - Investigating Windows 2.0](https://tryhackme.com/room/investigatingwindows2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
