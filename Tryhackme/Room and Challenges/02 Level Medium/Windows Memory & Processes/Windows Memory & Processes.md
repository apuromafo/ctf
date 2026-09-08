# Windows Memory & Processes

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `windowsmemoryandprocs` |
| **Link** | [TryHackMe](https://tryhackme.com/room/windowsmemoryandprocs) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Volatility / memory forensics / process structures / pstree / psscan / psxview / memmap |
| **Impacto** | Analizar procesos de Windows desde memoria con Volatility (estructuras, pslist, processtree, psscan, psxview, dump) |

---

**Contexto:** Sala de análisis forense de memoria Windows con Volatility. Profundiza en la estructura interna de los procesos de Windows (campos de estructura, PIDs, Offset) y en el uso combinado de los plugins pslist, processtree, psscan y psxview, hasta el volcado de procesos sospechosos y la identificación del usuario comprometido.

## Solucionario

### Task 1: Estructuras de Procesos de Windows / Windows Process Structures

**Explicación:**

Los campos de la estructura EPROCESS: el campo que mantiene la lista de todos los procesos activos es `ActiveProcessLinks`; el campo que almacena el PID de un proceso es `UniqueProcessId`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What field is used to keep track of all the active processes? Only enter the fields' name. | `ActiveProcessLinks` |
| 2 | What field is used to store the PID of a process? Only enter the fields' name. | `UniqueProcessId` |

### Task 2: Análisis con pslist / Analyzing with pslist

**Explicación:**

Con `windows.pslist` (resultados en `pslist.txt`): el PID del proceso `csrss.exe` que tiene 12 threads es `440`; el Offset(V) de memoria del proceso con PID 5672 es `0x990b29293080`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the PID of the csrss.exe process that has 12 threads? You can use the pslist.txt file to find the answer. | `440` |
| 2 | What is the (memory) Offset(V) of the process with PID 5672? You can use the pslist.txt file to find the answer. | `0x990b29293080` |

### Task 3: Análisis con processtree / Analyzing with processtree

**Explicación:**

Con `windows.pstree` (resultados en `processtree.txt`): el parentID (PPID) de `services.exe (PID 664)` es `524`; el ImageFileName del proceso con PID 7788 es `FTK Imager.exe`; y su ruta completa es `C:\Program Files\AccessData\FTK Imager\FTK Imager.exe`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the parentID (PPID) of the services.exe (PID 664) process? Use the processtree.txt file to answer the question. | `524` |
| 2 | What is the ImageFileName of the process that has the PID 7788? Use the processtree.txt file to answer the question. | `FTK Imager.exe` |
| 3 | What is the path of the process with PID 7788? | `C:\Program Files\AccessData\FTK Imager\FTK Imager.exe` |

### Task 4: Conteos de procesos con psscan y psxview / Process Counts with psscan and psxview

**Explicación:**

Con `windows.psscan` (resultados en `psscan.txt`): el número de procesos que tienen 0 Threads es `3`. Con `windows.psxview` (resultados en `psxview.txt`): el número de procesos que tienen el Exit Time rellenado es `3`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the number of processes that have 0 Threads? Use the psscan.txt file to answer the question. | `3` |
| 2 | What is the number of processes that have the Exit Time filled in? Use the psxview.txt file to answer the question. | `3` |

### Task 5: Volcado de Procesos y Compromiso / Process Dump and Compromise

**Explicación:**

Volcando el proceso con PID 7788 (con `windows.memmap --pid 7788 --dump`), el nombre del archivo volcado que representa el ejecutable es `file.0x990b2ae1ed40.0x990b29954a20.ImageSectionObject.FTK Imager.exe.img`. El nombre del usuario probablemente comprometido es `operator` y el ID asignado a la táctica MITRE Command and Control es `TA0011`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Dump the process with PID 7788. What is the name of the dumped file that represents the executable? | `file.0x990b2ae1ed40.0x990b29954a20.ImageSectionObject.FTK Imager.exe.img` |
| 2 | What is the name of the likely compromised user? | `operator` |
| 3 | What is the ID assigned to the MITRE Tactic Command and Control? | `TA0011` |

---

**Metodología:**

1. Revisar las estructuras internas del kernel de Windows: la lista de procesos activos se mantiene en el campo `ActiveProcessLinks` y el PID se almacena en `UniqueProcessId`.
2. Ejecutar `windows.pslist` sobre el volcado y filtrar los resultados: ubicar el proceso `csrss.exe` con 12 threads (PID 440) y el Offset de memoria del PID 5672 (`0x990b29293080`).
3. Usar `windows.pstree` para reconstruir la jerarquía padre/hijo: el PPID de `services.exe (664)` es 524, y el PID 7788 corresponde al ejecutable `FTK Imager.exe`, cuya ruta completa es `C:\Program Files\AccessData\FTK Imager\FTK Imager.exe`.
4. Cruzar los resultados de `windows.psscan` y `windows.psxview` para contar procesos zombis/terminados: 3 procesos con 0 threads y 3 con Exit Time rellenado.
5. Volcar el proceso PID 7788 (`windows.memmap --pid 7788 --dump`) y obtener el archivo que representa el ejecutable (ImageSectionObject). El análisis de los procesos apunta a un usuario comprometido, `operator`, y la correlación con MITRE asigna la táctica Command and Control al ID `TA0011`.

**Learning chain:** EPROCESS (ActiveProcessLinks + UniqueProcessId) -> pslist (csrss 440, PID 5672 offset) -> processtree (services 664 PPID 524; 7788 FTK Imager) -> psscan (3 with 0 threads) -> psxview (3 exit time) -> dump 7788 -> ImageSectionObject -> operator -> TA0011 C2

**Lección:** *La combinación de plugins de Volatility (pslist, processtree, psscan, psxview, memmap) permite correlacionar estructuras, jerarquías y conteos de procesos para reconstruir la actividad del sistema y detectar al usuario comprometido detrás de la táctica de Command and Control.*

**MITRE ATT&CK:** T1057 (Process Discovery) · T1071 (C2) · TA0011 (Command and Control) · CWE-200 (Exposure of Sensitive Information)

**Fuente:** [TryHackMe - Windows Memory & Processes](https://tryhackme.com/room/windowsmemoryandprocs)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
