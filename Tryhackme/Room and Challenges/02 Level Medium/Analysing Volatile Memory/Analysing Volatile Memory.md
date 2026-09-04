# Analysing Volatile Memory [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `analysingvolatilememory`
* **Link:** https://tryhackme.com/room/analysingvolatilememory
* **Sección / Section:** Forensics / Memory Analysis
* **Fuente / Source:** Writeup de thmrevenant (GitHub), Esther7171 (GitHub) y kim-kimani (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de forense de memoria de dificultad media. Aprende cómo el sistema operativo Windows gestiona los datos volátiles en diferentes archivos del disco (hiberfil.sys, pagefile.sys, volcados de memoria) y cómo extraer y analizar esos artefactos con herramientas forenses (EZ Tools, Registry Viewer, Reliability Monitor, WinDbg).
> **EN:** Medium difficulty memory forensics room. Learn how the Windows OS manages volatile data in different files on disk (hiberfil.sys, pagefile.sys, memory dumps) and how to extract and analyse those artefacts with forensic tools (EZ Tools, Registry Viewer, Reliability Monitor, WinDbg).

---

### Task 1 — Lab Setup & Volatile Data

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Connect to the Lab. How many tools are present in the EZ tools folder on the Desktop? | `12` |
| What is the default page size (in KB) in most Operating systems? | `4` |
| What is the name of the hibernation file? | `hiberfil.sys` |
| Which file is considered as the extension of the RAM? | `pagefile.sys` |
| Which Registry Hive contains the information about the pagefile? | `SYSTEM` |

---

### Task 2 — Network & Process Analysis

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Examine the domain-histrogram. Which domain associated with distributing Malware has occurred 192 times? Defang the domain. | `3z[.]nu` |
| Check the domain on VirusTotal; What is the verdict about this suspicious-looking domain? | `malware` |
| At the time of hibernation, which network scanning tool was running? | `wireshark` |
| What is the process ID associated with the network scanning tool? | `5604` |
| Examine the command lines executed on this host; which data wiping tool was executed on the host? | `diskwipe.exe` |
| What is the full path, from which the data wiping tool was executed? | `C:\Users\Administrator\Downloads\Tools\DiskWipe.exe` |

---

### Task 3 — Crash Dump Analysis

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the value of CrashDumpEnabled field in the Registry? | `1` |
| Examine the Reliability Monitor chart. What is the report ID of the last crash dump? | `cf3767cb-2cdf-4b9a-b6e1-c222d4fd192d` |
| How many times the system has reported critical events in the past? | `7` |
| What is the default path set for placing the crash dump in the settings? | `%SystemRoot%\MEMORY.DMP` |
| Which application was responsible for the first crash? | `myfault` |
| What is the process ID associated with a suspicious-looking process called evil.exe? | `1970` |
| Which command can be used to find the exact time of the crash? | `!time` |
| One of the variables in PEB contains a secret flag; what is the value of the flag? | `THM{__ITS_FUN_T0_Learn_at_THM__}` |

---

## Metodología / Methodology

1. **Configuración del laboratorio / Lab setup:** conectarse a la máquina y revisar la carpeta **EZ tools** del escritorio, que contiene 12 herramientas forenses (Registry Viewer, Process Explorer, Wireshark, WinDbg, etc.).
2. **Datos volátiles en disco / Volatile data on disk:** entender los archivos que contienen memoria volátil: `hiberfil.sys` (archivo de hibernación con una imagen comprimida de la memoria), `pagefile.sys` (extensión de la RAM) y el volcado de memoria `MEMORY.DMP`. El tamaño de página por defecto en la mayoría de sistemas operativos es de 4 KB. La información sobre el pagefile se almacena en la hive de registro `SYSTEM`.
3. **Análisis de red / Network analysis:** examinar el **domain-histogram** (histograma de dominios) que muestra el dominio `3z[.]nu` asociado a distribución de malware, ocurrido 192 veces. Verificar el veredicto en VirusTotal → `malware`. Identificar que en el momento de la hibernación estaba corriendo `wireshark` (PID `5604`).
4. **Análisis de procesos / Process analysis:** revisar las líneas de comandos ejecutadas en el host y encontrar la herramienta de borrado de datos `DiskWipe.exe`, ejecutada desde `C:\Users\Administrator\Downloads\Tools\DiskWipe.exe`.
5. **Análisis de volcados de memoria / Crash dump analysis:**
   - Verificar en el registro el campo `CrashDumpEnabled` → `1` (volcado de memoria habilitado).
   - Examinar el **Reliability Monitor** para obtener el report ID del último crash dump → `cf3767cb-2cdf-4b9a-b6e1-c222d4fd192d` y el número de eventos críticos → `7`.
   - La ruta por defecto del volcado es `%SystemRoot%\MEMORY.DMP`. La primera aplicación responsable del crash fue `myfault`.
   - Encontrar el proceso sospechoso `evil.exe` con PID `1970`.
6. **Análisis con WinDbg / WinDbg analysis:** abrir el volcado de memoria con WinDbg y usar el comando `!time` para encontrar la hora exacta del crash. Examinar las variables del **PEB** (Process Environment Block) donde una de ellas contiene la flag → `THM{__ITS_FUN_T0_Learn_at_THM__}`.

### Cadena de análisis / Analysis Chain

```
Lab (EZ tools) → hiberfil.sys / pagefile.sys / MEMORY.DMP → domain-histogram → 3z[.]nu (malware) → Wireshark PID 5604 → DiskWipe.exe → CrashDumpEnabled=1 → Reliability Monitor → report ID → myfault → evil.exe PID 1970 → WinDbg !time → PEB flag
```

**Lección:** los datos volátiles de un sistema Windows se conservan en varios artefactos en disco (hiberfil.sys, pagefile.sys y volcados de memoria). El análisis forense de memoria combina herramientas como Registry Viewer, Reliability Monitor y WinDbg para reconstruir la actividad del sistema, identificar malware y extraer indicadores de compromiso.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.