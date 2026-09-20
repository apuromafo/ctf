# FlareVM_ Arsenal of Tools

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `flarevmarsenaloftools` | https://tryhackme.com/room/flarevmarsenaloftools | 01 Level Easy | TryHackMe | FLOSS / PEStudio / x64dbg / CFF Explorer / HxD / FTK Imager / Process Explorer / Procmon / Wireshark / análisis de malware | Defensivo: conocer el arsenal de FlareVM y usarlo para analizar muestras maliciosas (windows.exe, cobaltstrike.exe, cryptominer.bin). |

---

> **Objeto:** Familiarizarse con las herramientas incluidas en FlareVM (debuggers, editores PE, análisis estático y Sysinternals) y aplicar FLOSS, PEStudio, CFF Explorer, Wireshark y Process Explorer sobre las muestras de la sala para responder al análisis.

**Contexto:** Sala defensiva del catálogo de TryHackMe que presenta las utilidades de FlareVM, la máquina virtual de análisis de malware de Mandiant/FLARE. Primero se recorren las categorías de herramientas (ingeniería inversa, editores de archivos, análisis forense y Sysinternals), después se repasan las herramientas de uso habitual en investigaciones (FLOSS, PEStudio, etc.) y por último se ejecuta un análisis práctico completo sobre un binario sospechoso (`windows.exe`) y un beacon de C2 (`cobaltstrike.exe`) con su captura de red.

> **ES:** Elegir la herramienta correcta del arsenal de FlareVM para cada tarea (debug, edición PE, strings deofuscados, análisis estático) y aplicarlas a las muestras del laboratorio.
> **EN:** Pick the right FlareVM tool for each task (debugging, PE editing, deobfuscated strings, static analysis) and apply them to the lab samples.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala y del propósito de FlareVM: una máquina virtual repleta de herramientas forenses, de respuesta a incidentes y de investigación de malware. Solo hay que leer la introducción.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click to complete / Marca la tarea. | `No answer needed` |

### Task 2: Arsenal de herramientas / Arsenal of Tools

**Explicación:** Se pide asociar cada utilidad de FlareVM con su función principal: `x64dbg` es el debugger open-source para binarios x64/x32, `CFF Explorer` analiza y edita ejecutables PE, `Process Hacker` es un editor de memoria y observador de procesos sofisticado, `FTK Imager` realiza adquisición y análisis de imágenes de disco forense y `HxD` permite ver y editar un archivo binario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which tool is an Open-source debugger for binaries in x64 and x32 formats? | `x64dbg` |
| 2 | What tool is designed to analyze and edit Portable Executable (PE) files? | `CFF Explorer` |
| 3 | Which tool is considered a sophisticated memory editor and process watcher? | `Process Hacker` |
| 4 | Which tool is used for Disc image acquisition and analysis for forensic use? | `FTK Imager` |
| 5 | What tool can be used to view and edit a binary file? | `HxD` |

### Task 3: Herramientas habituales para la investigación (visión general) / Commonly Used Tools for Investigation: Overview

**Explicación:** Repaso de las herramientas clave para investigaciones de malware. `FLOSS` (ex FireEye FLARE Obfuscated String Solver) extrae y deofusca strings con técnicas estáticas avanzadas; `Process Explorer` inspecciona procesos y comportamiento; `System` muestra información detallada del sistema; `Procmon` monitoriza procesos, registro y sistema de archivos en tiempo real; y `PEStudio` permite el análisis estático de propiedades de un ejecutable sin ejecutarlo. Con PEStudio sobre `cryptominer.bin` (Desktop\Sample) se obtienen el SHA-256 `E9627EBAAC562067759681DCEBA8DDE8D83B1D813AF8181948C549E342F67C0E` y sus `102` funciones. Con CFF Explorer sobre `possible_medusa.txt` se obtienen el MD5 `646698572AFBBF24F50EC5681FEB2DB7` y su magic value `5A4D`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which tool was formerly known as FireEye Labs Obfuscated String Solver? | `FLOSS` |
| 2 | ¿Qué herramienta de Sysinternals inspecciona procesos y comportamiento del sistema? / Which Sysinternals tool inspects processes and system behavior? | `Process Explorer` |
| 3 | ¿Qué herramienta muestra información detallada del sistema? / Which tool shows system information? | `System` |
| 4 | ¿Qué herramienta monitoriza procesos, registro y sistema de archivos en tiempo real? / Which tool monitors processes, registry and filesystem in real time? | `Procmon` |
| 5 | Which tool can be used for static analysis or studying executable file properties without running your files? | `PEStudio` |
| 6 | Using the tool PEStudio to open the file cryptominer.bin in the Desktop\Sample folder, what is the sha256 value of the file? | `E9627EBAAC562067759681DCEBA8DDE8D83B1D813AF8181948C549E342F67C0E` |
| 7 | Using the tool PEStudio to open the file cryptominer.bin, how many functions does it have? | `102` |
| 8 | ¿Qué herramienta genera hashes, autentica la fuente de los archivos del sistema y valida su validez? / Which tool can generate hashes and validate file validity? | `CFF Explorer` |
| 9 | Using the tool CFF Explorer to open possible_medusa.txt, what is the MD5 of the file? | `646698572AFBBF24F50EC5681FEB2DB7` |
| 10 | What is the file magic of possible_medusa.txt? | `5A4D` |

### Task 4: Análisis de archivos maliciosos / Analyzing Malicious Files!

**Explicación:** Escenario: "A suspicious windows.exe file was downloaded by a user on 09/24/2024 at 3:43 AM. This download was flagged as a potential threat. The monitoring team has sent you an email requesting that you perform an analysis of it." El archivo está en `C:\Users\Administrator\Desktop\Sample`. Con `FLOSS.exe .\windows.exe > windows.txt` se extraen los strings deofuscados y, con PEStudio, se obtienen la versión del archivo (`7.999`), el `requestedExecutionLevel` del manifiesto (`requireAdministrator`) y las funciones/cadenas clave de las llamadas al sistema: `set_UseShellExecute` (la invocación que abre el proceso) y la clase `RijndaelManaged` (cifrado AES). Para `cobaltstrike.exe`, PEStudio entrega el Imphash `92EEF189FB188C541CBD83AC8BA4ACF5`; la captura `cobaltstrike_capture.pcapng` se abre en Wireshark filtrando `ip.addr == 47.120.46.210` para obtener la IP de C2 (defanged `47[.]120[.]46[.]210`) y el puerto `81`; y con Process Explorer se identifica que el proceso padre de `cobaltstrike.exe` es `explorer.exe`.

```powershell
FLOSS.exe .\windows.exe > windows.txt   # strings deofuscados con FLOSS
# PEStudio open windows.exe -> version 7.999, requestedExecutionLevel requireAdministrator
# PEStudio open cobaltstrike.exe -> Imphash 92EEF189FB188C541CBD83AC8BA4ACF5
# Wireshark open cobaltstrike_capture.pcapng, filter: ip.addr == 47.120.46.210
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the file version of windows.exe? / ¿Cuál es la versión del archivo windows.exe? | `7.999` |
| 2 | What is the requestedExecutionLevel of windows.exe? | `requireAdministrator` |
| 3 | ¿Qué método usa windows.exe para lanzar la shell? / Which .NET method does windows.exe use to open the shell? | `set_UseShellExecute` |
| 4 | ¿Qué clase .NET se usa para la rutina de cifrado? / What is the name of the encryption class used by the malware? | `RijndaelManaged` |
| 5 | What is the Imphash of cobaltstrike.exe? | `92EEF189FB188C541CBD83AC8BA4ACF5` |
| 6 | What is the defanged IP address to which the process cobaltstrike.exe is connecting? | `47[.]120[.]46[.]210` |
| 7 | What is the destination port number used by cobaltstrike.exe when connecting to its C2 IP Address? | `81` |
| 8 | What is the parent process of cobaltstrike.exe? | `explorer.exe` |

### Task 5: Conclusión / Conclusion

**Explicación:** Con las herramientas del arsenal de FlareVM se ha completado el análisis estático y dinámico de las muestras: identificando strings deofuscados, valores PE, la comunicación con el C2 y el proceso padre. Cierre de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click to complete / Marca la tarea. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click to complete / Marca la tarea. | `No answer needed` |
| 2 | Which tool is an Open-source debugger for binaries in x64 and x32 formats? | `x64dbg` |
| 3 | What tool is designed to analyze and edit Portable Executable (PE) files? | `CFF Explorer` |
| 4 | Which tool is considered a sophisticated memory editor and process watcher? | `Process Hacker` |
| 5 | Which tool is used for Disc image acquisition and analysis for forensic use? | `FTK Imager` |
| 6 | What tool can be used to view and edit a binary file? | `HxD` |
| 7 | Which tool was formerly known as FireEye Labs Obfuscated String Solver? | `FLOSS` |
| 8 | ¿Qué herramienta de Sysinternals inspecciona procesos y comportamiento del sistema? | `Process Explorer` |
| 9 | ¿Qué herramienta muestra información detallada del sistema? | `System` |
| 10 | ¿Qué herramienta monitoriza procesos, registro y sistema de archivos en tiempo real? | `Procmon` |
| 11 | Which tool can be used for static analysis or studying executable file properties without running your files? | `PEStudio` |
| 12 | What is the sha256 value of cryptominer.bin? | `E9627EBAAC562067759681DCEBA8DDE8D83B1D813AF8181948C549E342F67C0E` |
| 13 | How many functions does cryptominer.bin have? | `102` |
| 14 | ¿Qué herramienta genera hashes y valida la validez de los archivos? | `CFF Explorer` |
| 15 | What is the MD5 of possible_medusa.txt? | `646698572AFBBF24F50EC5681FEB2DB7` |
| 16 | What is the file magic of possible_medusa.txt? | `5A4D` |
| 17 | What is the file version of windows.exe? | `7.999` |
| 18 | What is the requestedExecutionLevel of windows.exe? | `requireAdministrator` |
| 19 | ¿Qué método usa windows.exe para lanzar la shell? | `set_UseShellExecute` |
| 20 | ¿Qué clase .NET se usa para la rutina de cifrado? | `RijndaelManaged` |
| 21 | What is the Imphash of cobaltstrike.exe? | `92EEF189FB188C541CBD83AC8BA4ACF5` |
| 22 | What is the defanged IP address to which cobaltstrike.exe is connecting? | `47[.]120[.]46[.]210` |
| 23 | What is the destination port of the C2 connection? | `81` |
| 24 | What is the parent process of cobaltstrike.exe? | `explorer.exe` |
| 25 | Click to complete / Marca la tarea. | `No answer needed` |

---

**Metodología:** Recorrer las categorías de herramientas de FlareVM para asociar cada una a su función. Repasar las herramientas habituales (FLOSS, PEStudio, Sysinternals, CFF Explorer) y aplicarlas sobre las muestras: FLOSS para strings deofuscados, PEStudio para versión/manifiesto/Imphash y conteo de funciones, CFF Explorer para hashes y magic value, Wireshark con el filtro de la IP del C2 sobre la captura, y Process Explorer para el proceso padre.

### Cadena de ataque / Attack Chain

```text
Arsenal de herramientas -> selección por categoría -> FLOSS (strings) -> PEStudio (estática: SHA-256, funciones, versión, Imphash) -> CFF Explorer (MD5, magic) -> Wireshark (pcapng C2: IP defanged + puerto) -> Process Explorer (proceso padre) -> informe de análisis
```

**Learning chain:** FlareVM toolset -> tool triage -> FLOSS -> PEStudio -> CFF Explorer -> Wireshark -> Process Explorer -> malware analysis report.

**Lección:** *Un análisis de malware eficaz combina estática y dinámica: FLOSS deofusca strings, PEStudio/CFF Explorer describen el PE y sus hashes, Wireshark revela el C2 y Process Explorer la cadena de procesos.*

**MITRE ATT&CK:** T1071.001 — Application Layer Protocol (beacon C2 de cobaltstrike)

**Fuente:** [TryHackMe - FlareVM_ Arsenal of Tools](https://tryhackme.com/room/flarevmarsenaloftools)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.