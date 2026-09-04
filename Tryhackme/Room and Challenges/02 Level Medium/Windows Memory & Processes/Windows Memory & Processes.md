# Windows Memory & Processes [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `windowsmemoryandprocs`
* **Link:** https://tryhackme.com/room/windowsmemoryandprocs
* **Sección / Section:** Forensics / Memory
* **Fuente / Source:** (thmrevenant)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de análisis forense de memoria Windows con Volatility. Profundiza en la estructura interna de los procesos de Windows (campos de estructura, PIDs, Offset) y en el uso combinado de los plugins pslist, processtree, psscan y psxview, hasta el volcado de procesos sospechosos y la identificación del usuario comprometido.
> **EN:** Windows memory forensics room with Volatility. It digs into the internal structure of Windows processes (structure fields, PIDs, offsets) and the combined use of the pslist, processtree, psscan and psxview plugins, up to dumping suspicious processes and identifying the compromised user.

---

### Task 1 — Estructuras de Procesos de Windows / Windows Process Structures

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What field is used to keep track of all the active processes? Only enter the fields' name. | `ActiveProcessLinks` |
| What field is used to store the PID of a process? Only enter the fields' name. | `UniqueProcessId` |

---

### Task 2 — Análisis con pslist / Analyzing with pslist

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the PID of the csrss.exe process that has 12 threads? You can use the pslist.txt file to find the answer. | `440` |
| What is the (memory) Offset(V) of the process with PID 5672? You can use the pslist.txt file to find the answer. | `0x990b29293080` |

---

### Task 3 — Análisis con processtree / Analyzing with processtree

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the parentID (PPID) of the services.exe (PID 664) process? Use the processtree.txt file to answer the question. | `524` |
| What is the ImageFileName of the process that has the PID 7788? Use the processtree.txt file to answer the question. | `FTK Imager.exe` |
| What is the path of the process with PID 7788? | `C:\Program Files\AccessData\FTK Imager\FTK Imager.exe` |

---

### Task 4 — Conteos de procesos con psscan y psxview / Process Counts with psscan and psxview

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the number of processes that have 0 Threads? Use the psscan.txt file to answer the question. | `3` |
| What is the number of processes that have the Exit Time filled in? Use the psxview.txt file to answer the question. | `3` |

---

### Task 5 — Volcado de Procesos y Compromiso / Process Dump and Compromise

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Dump the process with PID 7788. What is the name of the dumped file that represents the executable? | `file.0x990b2ae1ed40.0x990b29954a20.ImageSectionObject.FTK Imager.exe.img` |
| What is the name of the likely compromised user? | `operator` |
| What is the ID assigned to the MITRE Tactic Command and Control? | `TA0011` |

---

## Metodología / Methodology

1. **Paso / Step:** Revisar las estructuras internas del kernel de Windows: la lista de procesos activos se mantiene en el campo `ActiveProcessLinks` y el PID se almacena en `UniqueProcessId`. / Review the Windows kernel internal structures: the list of active processes is kept in the `ActiveProcessLinks` field and the PID is stored in `UniqueProcessId`.
2. **Paso / Step:** Ejecutar `windows.pslist` sobre el volcado y filtrar los resultados: ubicar el proceso `csrss.exe` con 12 threads (PID 440) y el Offset de memoria del PID 5672 (`0x990b29293080`). / Run `windows.pslist` on the dump and filter the results: locate the `csrss.exe` process with 12 threads (PID 440) and the memory offset of PID 5672 (`0x990b29293080`).
3. **Paso / Step:** Usar `windows.pstree` para reconstruir la jerarquía padre/hijo: el PPID de `services.exe (664)` es 524, y el PID 7788 corresponde al ejecutable `FTK Imager.exe`, cuya ruta completa es `C:\Program Files\AccessData\FTK Imager\FTK Imager.exe`. / Use `windows.pstree` to rebuild the parent/child hierarchy: the PPID of `services.exe (664)` is 524, and PID 7788 corresponds to the `FTK Imager.exe` executable, whose full path is `C:\Program Files\AccessData\FTK Imager\FTK Imager.exe`.
4. **Paso / Step:** Cruzar los resultados de `windows.psscan` y `windows.psxview` para contar procesos zombis/terminados: 3 procesos con 0 threads y 3 con Exit Time rellenado. / Cross-check the `windows.psscan` and `windows.psxview` results to count zombie/terminated processes: 3 processes with 0 threads and 3 with Exit Time filled in.
5. **Paso / Step:** Volcar el proceso PID 7788 (`windows.memmap --pid 7788 --dump`) y obtener el archivo que representa el ejecutable (ImageSectionObject). El análisis de los procesos apunta a un usuario comprometido, `operator`, y la correlación con MITRE asigna la táctica Command and Control al ID `TA0011`. / Dump the PID 7788 process (`windows.memmap --pid 7788 --dump`) and obtain the file representing the executable (ImageSectionObject). The process analysis points to a compromised user, `operator`, and the MITRE correlation assigns the Command and Control tactic to ID `TA0011`.

### Cadena de ataque / Attack Chain

```
EPROCESS: ActiveProcessLinks (lista activa) + UniqueProcessId (PID)
  -> pslist: csrss.exe PID 440 (12 threads); PID 5672 Offset 0x990b29293080
  -> processtree: services.exe(664) PPID 524; PID 7788 = FTK Imager.exe
  -> psscan: 3 procesos con 0 Threads
  -> psxview: 3 procesos con Exit Time relleno
  -> dump PID 7788 -> ImageSectionObject.FTK Imager.exe.img
  -> usuario comprometido: operator
  -> MITRE Command and Control: TA0011
```

**Lección:** La combinación de plugins de Volatility (pslist, processtree, psscan, psxview, memmap) permite correlacionar estructuras, jerarquías y conteos de procesos para reconstruir la actividad del sistema y detectar al usuario comprometido detrás de la táctica de Command and Control.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.