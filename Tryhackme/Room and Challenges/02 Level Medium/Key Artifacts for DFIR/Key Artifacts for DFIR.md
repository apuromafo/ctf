# Key Artifacts for DFIR

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `keyartifactsfordfir` | [TryHackMe](https://tryhackme.com/room/keyartifactsfordfir) | 02 Level Medium | TryHackMe | DFIR, Windows event logs, EVTX, EvtxECmd, IIS logs, Prefetch/PECmd, SRUM, PowerShell history, registry, NTFS $MFT, Volatility, MemProcFS, FTK Imager | Construcción del "collection pack" de artefactos forenses Windows durante una respuesta a incidentes |

---

**Contexto:** Esta sala continúa el escenario OpenDoor. Con acceso a la red comprometida es necesario recolectar los artefactos forenses clave de Windows antes de que el adversario pueda destruirlos: event logs (EVTX), logs de aplicación (IIS e historial del navegador), artefactos del sistema operativo (Prefetch, SRUM, Recent Files, historial de PowerShell y registro), artefactos NTFS ($MFT, $LogFile, $UsnJournal), memoria (Volatility/MemProcFS) y disco (FTK Imager). La máquina objetivo es JMP-DMZ (jump host) y se emplean las credenciales DefenseBox DFIRUser:Secure! y target Administrator:Secure!, con herramientas como EvtxECmd, Timeline Explorer, PECmd, Registry Explorer, SQLECmd, Volatility 3 y FTK Imager.

## Solucionario

### Task 1: Introduction / Introducción

**Explicación:** La sala arranca con el escenario OpenDoor: tras identificar al adversario, se pide construir un "collection pack" de artefactos forenses de Windows. Debido al riesgo de que el adversario actúe aún dentro de la red, la recolección debe ser rápida y ordenada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's get going! | `No answer needed` |

### Task 2: Event Logs / Registros de eventos

**Explicación:** Se exportan y analizan los registros de eventos (EVTX) de la DefenseBox. La carpeta de logs contiene un total de 325 archivos EVTX. Al procesar los eventos 4624 y 4625 (inicios de sesión correctos y fallidos) del registro Security se identifica al usuario objetivo de la fuerza bruta: G.Miller. Tras el acceso, los eventos del registro Microsoft-Windows-TerminalServices-RDPClient muestran el host al que el usuario se movió lateralmente: DC01. Para comprobar si existen logs de Sysmon hay que verificar si Microsoft-Windows-Sysmon%4Operational.evtx está presente en la carpeta de logs; según el análisis del caso no había detección EDR, por lo que esta respuesta quedó pendiente de verificación en el lab.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many EVTX files are present in the event log folder? | `325` |
| 2 | What user was brute-forced according to the 4624/4625 events? | `G.Miller` |
| 3 | Are Sysmon logs present to show the process events after the logon? (Yea/Nay) | `Nay` |
| 4 | What hostname was that according to the RDPClient EVTX logs? | `DC01` |

### Task 3: Application Logs / Logs de aplicación

**Explicación:** Antes del ataque de fuerza bruta, el atacante escaneó el servidor IIS local: en los logs web se observa el User-Agent usado por la herramienta de descubrimiento, gobuster 3.6. Por otro lado, el historial del navegador de j.stevenson permite recuperar su última búsqueda en Google antes del incidente, relacionada con buenas prácticas de Windows Gem Server.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Before the brute-force, the attacker scanned the local IIS server. What user-agent did the attacker use, according to the web logs? | `gobuster/3.6` |
| 2 | What was the last Google search of j.stevenson before the attack? | `Windows gem server best practices` |

### Task 4: OS Artifacts / Artefactos del sistema operativo

**Explicación:** El análisis de Prefetch con PECmd revela la ejecución de un C2 Sliver enmascarado como actualizador de Microsoft Office; el archivo `OFFICE.EXE-5B65CF94.pf` confirma su ejecución desde el directorio `C:\ProgramData`. Para la persistencia se busca en `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` una entrada que apunte a office.exe dentro de ProgramData: la Run key usada es `OfficeUpd`. El adversario también ejecutó comandos de descubrimiento con PowerShell; el último comando registrado en el historial de la víctima es la consulta ADSI sobre el grupo Domain Admins.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Prefetch revealed Sliver C2 masking as a Microsoft Office updater. What .pf file confirms its execution from the C:\ProgramData directory? | `OFFICE.EXE-5B65CF94.pf` |
| 2 | The C2 persisted in the registry to launch on logon. What is the Run registry key used for persistence? | `OfficeUpd` |
| 3 | The adversary also ran PowerShell discovery commands. What is the last command seen in the victim's history file? | `([ADSI]"LDAP://CN=Domain Admins,CN=Users,DC=opendoor,DC=thm").Member` |

### Task 5: NTFS Artifacts / Artefactos NTFS

**Explicación:** Se exportan los artefactos NTFS: $MFT, $LogFile y $UsnJournal. Del análisis del $MFT se localiza la copia de Mimikatz en el directorio Public, cuyo timestamp de caída es 2026-07-27 14:27:19. Tres minutos después se crea el archivo users.txt con ruta absoluta `C:\Users\Public\Documents\users.txt`. Como el atacante copió Mimikatz sin eliminar la Mark of the Web, se ejecuta el script PowerShell del task, que recorre los flujos alternativos (ADS) Zone.Identifier en C:\Users\*\Downloads, y se lee la URL contenida en el stream: `http://65.1.49.131/stage/mimi.exe`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When was Mimikatz dropped to the Public directory? (Answer Example: 2026-07-25 15:30:45) | `2026-07-27 14:27:19` |
| 2 | Three minutes later, Mimikatz dropped a .txt file. What is the absolute path to the created file? | `C:\Users\Public\Documents\users.txt` |
| 3 | The attacker copied Mimikatz without stripping its Mark of the Web. What URL is shown once you adjust and run the script from the task? | `http://65.1.49.131/stage/mimi.exe` |

### Task 6: Memory Forensics / Forense de memoria

**Explicación:** Para la fase de memoria se emplean herramientas de análisis como Volatility 3 y MemProcFS. MemProcFS destaca porque representa la memoria de la máquina comprometida como un sistema de archivos virtual, lo que permite consultar procesos, credenciales y estructuras del kernel como si fueran ficheros.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What DFIR tool represents the memory as a virtual filesystem? | `MemProcFS` |

### Task 7: Disk Forensics / Forense de disco

**Explicación:** La fase de disco busca preservar la evidencia a nivel de almacenamiento. FTK Imager permite adquirir tanto archivos individuales del sistema NTFS como imágenes completas de disco, manteniendo la integridad de la evidencia para su análisis posterior.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which of the mentioned tools can be used to acquire both NTFS files and disk images? | `FTK Imager` |

### Task 8: Conclusion / Conclusión

**Explicación:** Con todos los artefactos recolectados, documentados y correlacionados se completa el collection pack del escenario OpenDoor. No se requiere una respuesta escrita.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the room! | `No answer needed` |

---

**Metodología:** La recolección sigue una secuencia orientada a la preservación del triage y a evitar la destrucción de la evidencia: (1) event logs con EvtxECmd y análisis en Timeline Explorer; (2) logs de aplicación (servidor IIS e historial del navegador); (3) artefactos del SO: Prefetch con PECmd, SRUM, Recent Files, historial de PowerShell y registro con Registry Explorer, además de SQLECmd para bases de datos locales; (4) artefactos NTFS: $MFT, $LogFile y $UsnJournal; (5) memoria con Volatility 3 y MemProcFS; y (6) adquisición de disco con FTK Imager. Se documentan los hashes y la cadena de custodia de cada artefacto para sostener la cadena de evidencia en un informe DFIR.

### Cadena de ataque / Attack Chain

```text
[ T1566 ] Phishing / acceso inicial -> Jump host JMP-DMZ (escenario OpenDoor)
        |
        v
[ T1110 ] Fuerza bruta RDP -> usuario G.Miller comprometido (eventos 4624/4625)
        |
        v
[ T1021.001 ] Movimiento lateral por RDP -> DC01 (logs RDPClient)
        |
        v
[ T1105 ] C2 Sliver enmascarado como OfficeUpd (office.exe en C:\ProgramData + Run key)
        |
        v
[ T1003.001 ] Dump de credenciales con Mimikatz -> C:\Users\Public\Documents\users.txt
        |
        v
[ Respuesta ] Collection pack DFIR: EVTX -> IIS -> Prefetch/SRUM/Registro -> $MFT -> Memoria -> Disco
```

**Learning chain:** DFIR -> orden de volatilidad -> EVTX (EvtxECmd/Timeline Explorer) -> logs web IIS (user-agent gobuster/3.6) -> Prefetch/SRUM (PECmd/Registry Explorer) -> registro Run (OfficeUpd) y PowerShell history (ADSI) -> NTFS ($MFT) -> MemProcFS/Volatility -> FTK Imager -> correlación y timeline.

**Lección:** *La elaboración de un collection pack definido y ordenado es lo que convierte una respuesta a incidentes caótica en un proceso forense reproducible: priorizar los artefactos más volátiles, verificar cada hallazgo y correlacionar logs, NTFS y memoria para reconstruir la cadena completa del ataque.*

**MITRE ATT&CK:** T1003.001 (credential dumping: Mimikatz/LSASS), T1562.002 (Disable Windows Event Logging), T1059.001 (PowerShell), T1574 (Hijack Execution Flow), T1595.001 (Active Scanning: gobuster) y T1566 (Phishing).

**Fuente:** [TryHackMe - Key Artifacts for DFIR](https://tryhackme.com/room/keyartifactsfordfir)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
