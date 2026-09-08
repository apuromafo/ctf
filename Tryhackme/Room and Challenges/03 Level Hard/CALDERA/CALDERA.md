# CALDERA

| **Dificultad** | Hard |
| **Tipo** | Walkthrough |
| **Slug** | `caldera` |
| **Link** | [TryHackMe](https://tryhackme.com/room/caldera) |
| **Sección** | 03 Level Hard |
| **Fuente** | TryHackMe |
| **Componentes** | CALDERA / Sandcat / APOLLO / planner / Sysmon / ELK / Sigma / Atomic Red Team / PowerShell |
| **Impacto** | Presenta CALDERA (v4) para la emulación autónoma de adversarios: despliegue de agentes, planificadores y operaciones, generación de telemetría Sysmon, detección con reglas Sigma y respuesta autónoma de incidentes. |

---

**Contexto:** El room invita a operar CALDERA 4.x, el marco open-source del MITRE para emular adversarios de forma autónoma. Se configura el agente Sandcat (canal HTTP), se elige un planner que decide el orden de las abilities y se ejecutan operaciones con perfiles como Enumeration e In-Through-Out que simulan un ataque completo (descarga de un adjunto macro, ejecución de notepad, enumeración de cuentas, archivado y exfiltración). A continuación se pasa al lado defensivo: correlacionar la telemetría de Sysmon/ELK con reglas Sigma (incluidas las Match Strings) para detectar cada técnica, y finalmente montar una respuesta autónoma que termina procesos sospechosos y aplica reglas de firewall, cerrando con un caso de estudio de emulación de APT41.

## Solucionario

### Task 1: Introduction

**Explicación:** Introducción al marco CALDERA del MITRE: una plataforma que ejecuta operaciones ofensivas autónomas (basadas en MITRE ATT&CK) y telemetría defensiva. No hay respuesta que introducir.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 2: CALDERA Overview

**Explicación:** CALDERA despliega **agentes** (implant que conecta con el servidor), organiza tactic-abilities y usa un **planner** (que determina el orden de ejecución de las abilities) y perfiles de operación. El agente que soporta comunicación por HTTP, GitHub GIST o DNS tunnelling es **Sandcat**; la simulación de actividad humana corre a cargo del plugin **Human**. La respuesta correcta para el orden de abilities es `planner`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the agent that has the capability to communicate via HTTP, GitHub GIST, or DNS tunnelling? | `Sandcat` |
| 2 | What functionality determines the order in which abilities are run? | `planner` |
| 3 | What is the name of the plugin that allows the simulation of human activity? | `Human` |

### Task 3: Running Operations with CALDERA

**Explicación:** Al configurar un agente Sandcat, la IP del servidor se rellena con `0.0.0.0` por defecto (hay que cambiarla por la del host para que el agente conecte). El perfil **Enumeration** incluye 5 abilities; la de enumeración de procesos ejecuta `tasklist /m >> $env:APPDATA\vmtool.log;cat $env:APPDATA\vmtool.log`. Durante la operación, la ability "SysInternals PSTool Process Discovery" no produjo salida (no devolvió output), lo que se observa en el panel de la operación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What IP address is set by default during the configuration of an agent? | `0.0.0.0` |
| 2 | How many abilities are included in the Enumeration profile? | `5` |
| 3 | What is the command executed by the tasklist Process Enumeration ability? | `tasklist /m  >> $env:APPDATA\vmtool.log;cat $env:APPDATA\vmtool.log` |
| 4 | What is the name of the ability that did not produce an output during the operation? | `SysInternals PSTool Process Discovery` |

### Task 4: In-Through-Out

**Explicación:** El perfil **In-Through-Out** encadena una simulación completa de ataque: la primera ability descarga un adjunto de phishing (`PhishingAttachment.xlsm`); la segunda abre ese documento y lanza `notepad.exe` (proceso hijo); la tercera/cuarta enumeran y reconocen cuentas (4 cuentas encontradas); la quinta archiva el directorio `Downloads`; la sexta exfiltra generando 23 peticiones HTTP hacia el servidor C2. Las respuestas salen directamente del detalle de la operación en CALDERA.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the file downloaded by the first ability? | `PhishingAttachment.xlsm` |
| 2 | What is the name of the new process spawned by the second ability? | `notepad.exe` |
| 3 | How many accounts were identified by the fourth ability? | `4` |
| 4 | What is the name of the directory that was archived by the fifth ability? | `Downloads` |
| 5 | How many HTTP requests were made by the sixth ability? | `23` |

### Task 5: Emulation to Detection

**Explicación:** La operación deja telemetría que se correlaciona con reglas **Sigma** (en ELK). El primer log generado tiene como ParentImage `C:\Users\Public\chrome.exe` (proceso padre del atacante simulado). La creación de un valor HKLM Shell de Winlogon se atribuye a la ability "Winlogon HKLM Shell Key Persistence - PowerShell". El uso de `Invoke-WebRequest` lo detecta la regla "PowerShell Web Download". Para detectar el archivado ZIP con `Compress-Archive` hacen falta las Match Strings `'Compress-Archive ' in CommandLine`, `' -Path ' in CommandLine`, `' -DestinationPath ' in CommandLine` y `$env:TEMP\ in CommandLine`. La ejecución PowerShell ofuscada se marca con la regla "Hacktool - CrackMapExec PowerShell Obfuscation".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the ParentImage of the process that triggered the first generated log? | `C:\Users\Public\chrome.exe` |
| 2 | Which ability is responsible for the log that shows the creation of a Winlogon HKLM Shell value? | `Winlogon HKLM Shell Key Persistence - PowerShell` |
| 3 | Which Sigma rule was used to flag the use of Invoke-WebRequest? | `PowerShell Web Download` |
| 4 | Which Match Strings must be set for the detection of the ZIP archiving ability? | `'Compress-Archive ' in CommandLine, ' -Path ' in CommandLine, ' -DestinationPath ' in CommandLine, $env:TEMP\ in CommandLine` |
| 5 | Which Sigma rule flagged the execution of the obfuscated PowerShell command? | `Hacktool - CrackMapExec PowerShell Obfuscation` |

### Task 6: Autonomous Incident Response

**Explicación:** En el plugin de respuesta autónoma, la ability "Find unauthorized processes" falló 3 veces durante el primer lote (cuando no había procesos sospechosos). Junto al fact `remote.port.unauthorized` se genera el fact `host.pid.unauthorized` (PID del proceso no autorizado). La regla de firewall creada por "Enable Outbound TCP/UDP firewall rule" usa el grupo `Caldira`. Cuando se detecta un proceso rogue, la ability de respuesta que se dispara es "Kill rogue process", que usa el cmdlet `Stop-Process`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many times did the Find unauthorized processes ability fail during the first batch? | `3` |
| 2 | What is the name of the fact that is generated alongside `remote.port.unauthorized`? | `host.pid.unauthorized` |
| 3 | What is the group value of the firewall rule created by the Enable Outbound TCP/UDP firewall rule ability? | `Caldira` |
| 4 | Which response ability executed when a rogue process was detected? | `Kill rogue process` |
| 5 | What PowerShell cmdlet is used by that ability to stop the process? | `Stop-Process` |

### Task 7: Case Study: Emulating APT41

**Explicación:** En el caso APT41 se correlacionan abilities con su telemetría: "Download Macro-Enabled Phishing Attachment" crea `C:\Users\Administrator\AppData\Local\Temp\2\PhishingAttachment.xlsm`; la ejecución WMI ofuscada se marca con el Match String `\WmiPrvSE.exe in ParentImage`; "Execute a Command as a Service" crea el servicio `ARTService`; la tarea programada de PowerShell deja `C:\Windows\System32\Tasks\AtomicTask`. La creación de usuario se detecta con la regla "New User Created Via Net.EXE", el borrado de logs con "Suspicious Eventlog Clear or Configuration Change", y la ability de descubrimiento de archivos/directorios ejecuta `ls -recurse; get-childitem -recurse; gci -recurse` (la ability "Find files" se ejecutó 3 veces en la emulación).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the TargetFilename of the file created by Download Macro-Enabled Phishing Attachment? | `C:\Users\Administrator\AppData\Local\Temp\2\PhishingAttachment.xlsm` |
| 2 | Which Match String flagged the execution of the obfuscated WMI process? | `\WmiPrvSE.exe in ParentImage` |
| 3 | What is the name of the service created by Execute a Command as a Service? | `ARTService` |
| 4 | What is the TargetFilename of the file created by Powershell Cmdlet Scheduled Task? | `C:\Windows\System32\Tasks\AtomicTask` |
| 5 | Which Sigma rule detected the creation of a new user? | `New User Created Via Net.EXE` |
| 6 | Which Sigma rule detected the clearing of the event logs? | `Suspicious Eventlog Clear or Configuration Change` |
| 7 | What is the command used by the File and Directory Discovery ability? | `ls -recurse; get-childitem -recurse; gci -recurse` |
| 8 | How many times did the Find files ability execute during the emulation? | `3` |

### Task 8: Conclusion

**Explicación:** Cierre del room: recapitulación de todo el ciclo emulación → detección → respuesta. Sin respuesta que introducir.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

---

**Metodología:**
1. Desplegar CALDERA 4.x en Docker, crear el usuario admin y acceder al panel web (`:8888`) que permite gestionar agentes, abilities y operations.
2. Configurar el agente Sandcat apuntando a la IP del host (por defecto `0.0.0.0`) e iniciar una operación con el planner predefinido y el perfil de Enumeration (5 abilities) para observar qué habilidades ejecutan y cuáles no devuelven salida.
3. Ejecutar el perfil In-Through-Out y correlacionar la telemetría recogida (archivos descargados, procesos, cuentas, directorio archivado y salidas HTTP) con cada pregunta.
4. Analizar los logs de Sysmon/ELK generados por la operación para traducir la emulación en detección: reglas Sigma y sus Match Strings para cada técnica.
5. Configurar la respuesta autónoma de incidentes para identificar procesos no autorizados, terminarlos con `Stop-Process` y crear reglas de firewall del grupo Caldira.
6. Revisar el caso práctico de emulación de APT41 comparando abilities, archivos creados, Match Strings y las reglas Sigma resultantes.

**Learning chain:** `CALDERA → Sandcat/planner → operación Enumeration → perfil In-Through-Out → telemetría Sysmon → reglas Sigma → respuesta autónoma → caso APT41`

**MITRE ATT&CK:** T1105 (Ingress Tool Transfer), T1059 (Command and Scripting Interpreter), T1547.004 (Winlogon Helper DLL), T1053.005 (Scheduled Task), T1027 (Obfuscated Files or Information), T1083 (File and Directory Discovery)

**Fuente:** [TryHackMe - CALDERA](https://tryhackme.com/room/caldera)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
