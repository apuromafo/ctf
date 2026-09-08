# Analysing Volatile Memory
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `analysingvolatilememory` |
| **Link** | [TryHackMe](https://tryhackme.com/room/analysingvolatilememory) |
| **Sección** | Forensics / Memory Analysis |
| **Fuente** | Writeup de thmrevenant (GitHub), Esther7171 (GitHub) y kim-kimani (GitHub) |
| **Componentes** | Windows memory forensics, hiberfil.sys, pagefile.sys, MEMORY.DMP, EZ Tools, Registry Viewer, Reliability Monitor, Wireshark, WinDbg (!time), PEB, crash dumps |
| **Impacto** | Sala de forense de memoria de dificultad media: cómo Windows gestiona los datos volátiles en disco (hiberfil.sys, pagefile.sys, volcados de memoria) y cómo extraer/analizar esos artefactos con herramientas forenses (EZ Tools, Registry Viewer, Reliability Monitor, WinDbg). |
---
**Contexto:** Sala de forense de memoria de dificultad media. Aprende cómo el sistema operativo Windows gestiona los datos volátiles en diferentes archivos del disco (hiberfil.sys, pagefile.sys, volcados de memoria) y cómo extraer y analizar esos artefactos con herramientas forenses (EZ Tools, Registry Viewer, Reliability Monitor, WinDbg).
*EN: Medium difficulty memory forensics room. Learn how the Windows OS manages volatile data in different files on disk (hiberfil.sys, pagefile.sys, memory dumps) and how to extract and analyse those artefacts with forensic tools (EZ Tools, Registry Viewer, Reliability Monitor, WinDbg).*
## Solucionario
### Task 1 — Lab Setup & Volatile Data
**Explicación:** En el escritorio del lab hay **12 herramientas** en la carpeta **EZ tools** (Registry Viewer, Process Explorer, Wireshark, WinDbg, etc.). Datos volátiles en disco: el tamaño de página por defecto es de **4 KB**; el archivo de hibernación es **hiberfil.sys** (imagen comprimida de la memoria); **pagefile.sys** se considera la "extensión de la RAM"; la información sobre el pagefile se almacena en la hive de registro **SYSTEM**.
*EN: The lab Desktop holds **12 tools** inside the **EZ tools** folder (Registry Viewer, Process Explorer, Wireshark, WinDbg, etc.). Volatile data on disk: the default page size is **4 KB**; the hibernation file is **hiberfil.sys** (a compressed memory image); **pagefile.sys** is considered the RAM extension; pagefile information lives in the **SYSTEM** registry hive.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Connect to the Lab. How many tools are present in the EZ tools folder on the Desktop? | `12` |
| 2 | What is the default page size (in KB) in most Operating systems? | `4` |
| 3 | What is the name of the hibernation file? | `hiberfil.sys` |
| 4 | Which file is considered as the extension of the RAM? | `pagefile.sys` |
| 5 | Which Registry Hive contains the information about the pagefile? | `SYSTEM` |
### Task 2 — Network & Process Analysis
**Explicación:** Analizando el **domain-histogram** destaca el dominio **3z[.]nu** asociado a distribución de malware, ocurrido 192 veces (veredicto en VirusTotal: `malware`). En el momento de la hibernación la herramienta de escaneo de red en ejecución era **wireshark** con PID **5604**. Revisando las líneas de comandos del host se encuentra la herramienta de borrado de datos **DiskWipe.exe**, ejecutada desde `C:\Users\Administrator\Downloads\Tools\DiskWipe.exe`.
*EN: Inspecting the **domain-histogram**, the malware-distributing domain **3z[.]nu** appears 192 times (VirusTotal verdict: `malware`). At hibernation time the running network scanning tool was **wireshark** with PID **5604**. Checking the host's executed command lines reveals the data wiping tool **DiskWipe.exe**, run from `C:\Users\Administrator\Downloads\Tools\DiskWipe.exe`.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Examine the domain-histrogram. Which domain associated with distributing Malware has occurred 192 times? Defang the domain. | `3z[.]nu` |
| 2 | Check the domain on VirusTotal; What is the verdict about this suspicious-looking domain? | `malware` |
| 3 | At the time of hibernation, which network scanning tool was running? | `wireshark` |
| 4 | What is the process ID associated with the network scanning tool? | `5604` |
| 5 | Examine the command lines executed on this host; which data wiping tool was executed on the host? | `diskwipe.exe` |
| 6 | What is the full path, from which the data wiping tool was executed? | `C:\Users\Administrator\Downloads\Tools\DiskWipe.exe` |
### Task 3 — Crash Dump Analysis
**Explicación:** Análisis de volcados de memoria: en el registro, `CrashDumpEnabled` = **1**. En el **Reliability Monitor**, el report ID del último crash dump es `cf3767cb-2cdf-4b9a-b6e1-c222d4fd192d` y ha habido **7** eventos críticos. La ruta por defecto del volcado es `%SystemRoot%\MEMORY.DMP`; la primera aplicación responsable del crash fue **myfault**. El proceso sospechoso **evil.exe** tiene PID **1970**. Con **WinDbg** sobre el volcado, `!time` encuentra la hora exacta del crash y una variable del **PEB** (Process Environment Block) contiene la flag.
*EN: Crash dump analysis: in the registry, `CrashDumpEnabled` = **1**. In the **Reliability Monitor**, the report ID of the last crash dump is `cf3767cb-2cdf-4b9a-b6e1-c222d4fd192d` with **7** critical events. The default dump path is `%SystemRoot%\MEMORY.DMP` and the first crashing application was **myfault**. The suspicious process **evil.exe** has PID **1970**. Using **WinDbg** on the dump, `!time` reveals the exact crash time and a **PEB** (Process Environment Block) variable holds the flag.*

```
Lab (EZ tools) → hiberfil.sys / pagefile.sys / MEMORY.DMP → domain-histogram → 3z[.]nu (malware) → Wireshark PID 5604 → DiskWipe.exe → CrashDumpEnabled=1 → Reliability Monitor → report ID → myfault → evil.exe PID 1970 → WinDbg !time → PEB flag
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of CrashDumpEnabled field in the Registry? | `1` |
| 2 | Examine the Reliability Monitor chart. What is the report ID of the last crash dump? | `cf3767cb-2cdf-4b9a-b6e1-c222d4fd192d` |
| 3 | How many times the system has reported critical events in the past? | `7` |
| 4 | What is the default path set for placing the crash dump in the settings? | `%SystemRoot%\MEMORY.DMP` |
| 5 | Which application was responsible for the first crash? | `myfault` |
| 6 | What is the process ID associated with a suspicious-looking process called evil.exe? | `1970` |
| 7 | Which command can be used to find the exact time of the crash? | `!time` |
| 8 | One of the variables in PEB contains a secret flag; what is the value of the flag? | `THM{__ITS_FUN_T0_Learn_at_THM__}` |
---
**Metodología:** Configuración del lab (EZ tools) → datos volátiles en disco (hiberfil/pagefile/MEMORY.DMP) → análisis de red (domain-histogram + VirusTotal) → análisis de procesos (command lines, DiskWipe.exe) → análisis de crash dumps (registry + Reliability Monitor) → análisis con WinDbg (`!time`, PEB).
**Learning chain:** artefactos volátiles en disco → descubrimiento de C2/malware → correlación de procesos → análisis de crash dumps → extracción de la flag (WinDbg/PEB).
**MITRE ATT&CK:** T1070.004 (File Deletion) / diskwipe (T1485 Data Destruction), T1046 (Network Service Scanning) / Wireshark, T1059.003 (Windows Command Shell), T1071.001 (Web Protocols / 3z.nu C2).
**Fuente:** [TryHackMe - Analysing Volatile Memory](https://tryhackme.com/room/analysingvolatilememory)