# Critical

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Defensive Security / Memory Forensics | `critical` | https://tryhackme.com/room/critical | 01 Level Easy | TryHackMe | Volatility 3 / windows.info / windows.netscan / windows.pslist / windows.pstree / windows.filescan / windows.mftscan / LIME / vol -h | Adquirir y analizar un volcado de memoria (memory forensics) con Volatility para reconstruir una infección: perfil del sistema, procesos, conexiones y artefactos del atacante. |

---

**Contexto:** Sala de memory forensics donde se parte de un volcado de memoria de una máquina Windows infectada. Con Volatility 3 se identifica el perfil y la arquitectura del sistema, se analizan los procesos (encontrando uno con el nombre truncado `critical_updat` y su proceso hijo), se listan las conexiones de red (puerto 80 hacia `msedge.exe`) y se rastrean los ficheros maliciosos (`critical_update.exe`) y servidores usados por el atacante (`SimpleHTTP/0.6 Python/3.10.4`).

> **ES:** "Analiza el volcado de memoria de una máquina comprometida con Volatility 3 para identificar la infección: perfiles, procesos, conexiones de red y los ficheros que dejó el atacante."
> **EN:** "Analyze the memory dump of a compromised machine with Volatility 3 to identify the infection: profiles, processes, network connections and the files left by the attacker."

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se introduce la sala y el caso: una máquina ha sido comprometida y se dispone de una imagen de memoria para analizar con Volatility 3. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He leído la introducción del caso. / I've read the introduction of the case. | `No answer needed` |

---

### Task 2: Fundamentos de memoria / Memory fundamentals

**Explicación:** Los datos volátiles de una máquina (procesos, conexiones, contenido de la RAM) viven en la memoria principal; por eso la RAM suele ser el primer objetivo de un atacante que quiere robar credenciales o evadir el disco. Capturar el contenido de la RAM antes de apagar el sistema se denomina adquisición de memoria (Memory Acquisition).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué componente contiene los datos volátiles que un atacante quiere robar? / What component holds the volatile data an attacker wants to steal? | `RAM` |
| 2 | ¿Cómo se llama el proceso de capturar el contenido de la memoria volátil? / What is the process of capturing the contents of volatile memory called? | `Memory Acquisition` |

---

### Task 3: Trabajando con Volatility / Working with Volatility

**Explicación:** Para empezar el análisis se usa `vol` (Volatility 3). El plugin `windows.info` vuelca información del sistema: perfil, arquitectura, versiones de Kernel y base del kernel. El volcado de memoria en este entorno tiene extensión/format LIME, y `vol -h` muestra la ayuda con todos los plugins disponibles.

```bash
python3 vol.py -f critical.img windows.info
python3 vol.py -h
# Los volcados utilizados en la sala son ficheros .lime (LIME).
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué plugin muestra la información del sistema operativo (OS)? / Which plugin displays the operating system (OS) information? | `Windows.info` |
| 2 | ¿Cuál es la extensión/formato del volcado de memoria del lab? / What is the extension/format of the lab memory dump? | `LIME` |
| 3 | ¿Qué comando muestra el menú de ayuda de Volatility? / Which command displays the help menu using Volatility? | `vol -h` |

---

### Task 4: Perfil y arquitectura / Profile and architecture

**Explicación:** Volcando la información con `windows.info` se confirma que el volcado es válido para Volatility, que la arquitectura es x64 (64 bits), que la versión del sistema operativo es Windows 10 y que la base del kernel se localiza en `0xf8066161b000`. Estos datos son la referencia para el resto de plugins.

```bash
python3 vol.py -f critical.img windows.info
# Username: WIN-...  -> Is the architecture x64? Y -> OS version: 10 -> kernel base: 0xf8066161b000
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Es la arquitectura de la máquina x64 (64 bits)? (Y/N) / Is the architecture of the machine x64 (64bit) Y/N? | `Y` |
| 2 | ¿Cuál es la versión del sistema operativo Windows? / What is the version of the Windows OS? | `10` |
| 3 | ¿Cuál es la dirección base del kernel? / What is the base address of the kernel? | `0xf8066161b000` |

---

### Task 5: Conexiones y procesos / Connections and processes

**Explicación:** Con el plugin `windows.netscan` se identifican las conexiones que usaron el puerto 80: la conexión se establece contra la IP `192.168.182.128` y el proceso dueño de esa conexión es `msedge.exe`. Revisando el árbol de procesos de `windows.pstree`/`windows.pslist` se encuentra el proceso malicioso con el nombre truncado `critical_updat`: su proceso hijo tiene el PID `1612` y su timestamp es `2024-02-24 22:51:50.000000`.

```bash
python3 vol.py -f critical.img windows.netscan
python3 vol.py -f critical.img windows.pstree
python3 vol.py -f critical.img windows.pslist
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Usando `windows.netscan`, ¿qué IP estableció una conexión en el puerto 80? / Using `windows.netscan`, what IP address established a connection on port 80? | `192.168.182.128` |
| 2 | Usando `windows.netscan`, ¿qué programa (dueño) usó el puerto 80? / Using `windows.netscan`, what is the program (owner) used to access through port 80? | `msedge.exe` |
| 3 | Analizando los procesos del volcado, ¿cuál es el PID del proceso hijo de `critical_updat`? / What is the PID of the child process of `critical_updat`? | `1612` |
| 4 | ¿Cuál es el timestamp del proceso con el nombre truncado `critical_updat`? / What is the time stamp for the process with the truncated name `critical_updat`? | `2024-02-24 22:51:50.000000` |

---

### Task 6: Ficheros e infraestructura del atacante / Files and attacker infrastructure

**Explicación:** Con `windows.filescan` se recupera la ruta completa del binario malicioso en disco: `C:\Users\user01\Documents\critical_update.exe`. Con `windows.mftscan` se obtiene la fecha de creación del documento `important_document.pdf` (`2024-02-24 20:39:42.000000`). Finalmente, extrayendo y analizando la memoria del proceso `updater.exe` se observa la petición HTTP y el servidor usado por el atacante para servir el archivo: `SimpleHTTP/0.6 Python/3.10.4`.

```bash
python3 vol.py -f critical.img windows.filescan | grep -i critical
python3 vol.py -f critical.img windows.mftscan.MFTScan
# Extraer y analizar la memoria del proceso updater.exe -> SimpleHTTP/0.6 Python/3.10.4
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Analizando `windows.filescan`, ¿cuál es la ruta y nombre completos de `critical_updat`? / Analyzing `windows.filescan`, what is the full path and name for `critical_updat`? | `C:\Users\user01\Documents\critical_update.exe` |
| 2 | Analizando `windows.mftscan`, ¿cuál es el timestamp de creación de `important_document.pdf`? / What is the timestamp for the created date of `important_document.pdf`? | `2024-02-24 20:39:42.000000` |
| 3 | Analizando la memoria de `updater.exe`, ¿qué servidor HTTP usó el atacante? / Analyzing the `updater.exe` memory, what HTTP server did the attacker use? | `SimpleHTTP/0.6 Python/3.10.4` |

---

### Task 7: Conclusión / Conclusion

**Explicación:** Se cierra la sala resumiendo el flujo de análisis que permitió reconstruir la infección desde la memoria. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He completado el análisis forense del volcado. / I've completed the forensic analysis of the dump. | `No answer needed` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | Introducción. / Introduction. | `No answer needed` |
| 2 | Task 2 | ¿Qué componente contiene los datos volátiles? / What component holds volatile data? | `RAM` |
| 3 | Task 2 | ¿Cómo se llama la captura de memoria? / What is capturing memory called? | `Memory Acquisition` |
| 4 | Task 3 | ¿Qué plugin muestra la info del SO? / Which plugin shows OS info? | `Windows.info` |
| 5 | Task 3 | ¿Cuál es el formato del volcado? / What is the dump format? | `LIME` |
| 6 | Task 3 | ¿Qué comando muestra la ayuda? / Which command shows help? | `vol -h` |
| 7 | Task 4 | ¿Es x64? (Y/N) / Is it x64? (Y/N) | `Y` |
| 8 | Task 4 | ¿Cuál es la versión del SO? / What is the OS version? | `10` |
| 9 | Task 4 | ¿Cuál es la base del kernel? / What is the kernel base address? | `0xf8066161b000` |
| 10 | Task 5 | IP de la conexión en el puerto 80. / IP that established a connection on port 80. | `192.168.182.128` |
| 11 | Task 5 | Programa que usó el puerto 80. / Program (owner) used to access through port 80. | `msedge.exe` |
| 12 | Task 5 | PID del hijo de `critical_updat`. / PID of the child process of `critical_updat`. | `1612` |
| 13 | Task 5 | Timestamp de `critical_updat`. / Time stamp of `critical_updat`. | `2024-02-24 22:51:50.000000` |
| 14 | Task 6 | Ruta completa de `critical_updat`. / Full path and name for `critical_updat`. | `C:\Users\user01\Documents\critical_update.exe` |
| 15 | Task 6 | Fecha de creación de `important_document.pdf`. / Created date of `important_document.pdf`. | `2024-02-24 20:39:42.000000` |
| 16 | Task 6 | Servidor HTTP del atacante. / HTTP server used by the attacker. | `SimpleHTTP/0.6 Python/3.10.4` |
| 17 | Task 7 | Conclusión. / Conclusion. | `No answer needed` |

---

**Metodología:** Identificar el volcado y su formato -> `vol -h` para conocer los plugins -> `windows.info` para perfil, arquitectura, versión y base del kernel -> `windows.netscan` para conexiones de red -> `windows.pslist`/`windows.pstree` para procesos e identificar el malicioso -> `windows.filescan` y `windows.mftscan` para localizar ficheros y timestamps -> extracción de la memoria del proceso para reconstruir la infraestructura del atacante.

### Cadena de ataque / Attack Chain

```text
vol -h -> windows.info -> perfil (x64, Win10, kernel base 0xf8066161b000) -> windows.netscan -> IP 192.168.182.128 / msedge.exe -> windows.pstree -> critical_updat (hijo PID 1612, timestamp) -> windows.filescan -> critical_update.exe -> windows.mftscan -> important_document.pdf -> memoria de updater.exe -> SimpleHTTP/0.6
```

**Learning chain:** adquisición (LIME) -> vol.py -> windows.info -> netscan -> pslist/pstree -> filescan/mftscan -> proceso updater.exe -> atribución servidor.

**Lección:** *La memoria es una fuente de verdad forense: conexiones, procesos y ficheros borrados desaparecen del disco, pero dejan rastro en el volcado de RAM.*

**MITRE ATT&CK:** N/A (sala defensiva de memory forensics; el incidente analizado incluye T1190/initial access y descarga de binarios - T1105)

**Fuente:** [TryHackMe - Critical](https://tryhackme.com/room/critical)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.