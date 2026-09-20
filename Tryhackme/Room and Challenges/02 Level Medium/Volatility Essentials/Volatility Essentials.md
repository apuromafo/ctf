# Volatility Essentials

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | Forense de memoria / Memory Forensics | volatilityessentials | https://tryhackme.com/room/volatilityessentials | 02 Level Medium | TryHackMe | Volatility 2, Memory Dumps, Windows XP, WannaCry | Alta - análisis de memoria RAM en incidentes |

> **Objeto:** Analizar un memory dump de Windows mediante Volatility para extraer el perfil del sistema, procesos, DLLs y evidencias de actividad maliciosa (ransomware WannaCry).

---

**Contexto:** Esta habitación introduce la forensia de memoria volátil con Volatility sobre una imagen de Windows XP. Se emplean módulos `imageinfo`, `pslist`, `dlllist`, `psxview` y `filescan` para identificar el perfil correcto, reconstruir el escenario y detectar la infección por WannaCry a partir de procesos y archivos inyectados.

> **ES:** El laboratorio enseña a trabajar con volcados de memoria (RAM) y a extraer artefactos forenses mediante Volatility.
> **EN:** This lab teaches how to work with memory dumps (RAM) and extract forensic artifacts using Volatility.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Configurar el entorno, descargar Volatility y el fichero de memoria que se va a inspeccionar.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Interactuar con la máquina? / Do we need to interact? | No answer needed |

### Task 2: Obtención de la imagen / Obtain the memory dump

**Explicación:** El dump ya está disponible en el escritorio de la máquina víctima; comprobar su integridad y disponerlo para el análisis.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Interactuar con la máquina? / Do we need to interact? | No answer needed |

### Task 3: Perfil e imagen / Profile & Image Date

**Explicación:** Ejecutar `vol.py -f <dump> imageinfo` para identificar el perfil de Volatility y la fecha de creación de la imagen.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es el perfil? / What is the profile? | 2600.xpsp.080413-2111 |
| ¿Qué fecha tiene la imagen? / What is the image date? | 2012-07-22 02:45:08 |

### Task 4: Procesos / Processes

**Explicación:** Usar `vol.py -f <dump> --profile=<perfil> pslist` para listar los procesos y responder sobre el proceso inicial, PID, PPID y eventos de la imagen.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es el proceso que el usuario estaba ejecutando? / Which process was the user executing? | C:\Program Files\Adobe\Reader 9.0\Reader\Reader_sl.exe |
| ¿Cuál es el proceso con PID 1484? / Which process has PID 1484? | explorer.exe |
| ¿Cuál es el PID del proceso `reader_sl.exe`? / What is the PID of `reader_sl.exe`? | 1484 |
| ¿Cuál es el PPID del proceso `reader_sl.exe`? / What is the PPID of `reader_sl.exe`? | 3 |
| ¿Qué evento aparece en el árbol de procesos? / Which event appears in the process tree? | CritSecOutOfMemoryEvent |

### Task 5: Hijos del proceso / Child processes

**Explicación:** Analizar con `pstree` los procesos que cuelgan de `explorer.exe` para detectar el proceso lanzado por el documento malicioso.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué procesos son hijos del proceso inicial? / Which processes are children of the initial process? | explorer.exe,reader_sl.exe |

### Task 6: Volcado de proceso / Process memory dump

**Explicación:** Usar el módulo `memdump` para volcar la memoria del proceso malicioso y localizar su dirección base.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la dirección base del proceso malicioso? / What is the base address of the malicious process? | 0x8056e27c |

### Task 7: WannaCry / WannaCry Detection

**Explicación:** Emplear `psxview`, `filescan` y `skeleton` para confirmar la inyección de código del ransomware WannaCry: procesos ocultos, binario @WanaDecryptor@ y archivos implicados.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Qué nombre ventana tiene el proceso malicioso? / What window name does the malicious process use? | @WanaDecryptor@ |
| ¿Qué ruta completa tiene el binario? / What is the full path of the binary? | C:\Intel\ivecuqmanpnirkt615\@WanaDecryptor@.exe |
| ¿Qué proceso lanza el ransomware? / Which process launches the ransomware? | tasksche.exe |
| ¿Cómo se llama el ransomware? / What is the name of the ransomware? | Wannacry |
| ¿Qué módulo se usó para detectarlo? / Which module was used to detect it? | windows.filescan |

### Task 8: Finalización / Wrap up

**Explicación:** Revisar las conclusiones del análisis y los artefactos extraídos.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Necesitas responder algo más? / Is there anything else to answer? | No answer needed |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Interactuar con la máquina? / Do we need to interact? | `No answer needed` |
| 2 | ¿Interactuar con la máquina? / Do we need to interact? | `No answer needed` |
| 3 | ¿Cuál es el perfil? / What is the profile? | `2600.xpsp.080413-2111` |
| 3 | ¿Qué fecha tiene la imagen? / What is the image date? | `2012-07-22 02:45:08` |
| 4 | ¿Cuál es el proceso que el usuario estaba ejecutando? / Which process was the user executing? | `C:\Program Files\Adobe\Reader 9.0\Reader\Reader_sl.exe` |
| 4 | ¿Cuál es el proceso con PID 1484? / Which process has PID 1484? | `explorer.exe` |
| 4 | ¿Cuál es el PID del proceso `reader_sl.exe`? / What is the PID of `reader_sl.exe`? | `1484` |
| 4 | ¿Cuál es el PPID del proceso `reader_sl.exe`? / What is the PPID of `reader_sl.exe`? | `3` |
| 4 | ¿Qué evento aparece en el árbol de procesos? / Which event appears in the process tree? | `CritSecOutOfMemoryEvent` |
| 5 | ¿Qué procesos son hijos del proceso inicial? / Which processes are children of the initial process? | `explorer.exe,reader_sl.exe` |
| 6 | ¿Cuál es la dirección base del proceso malicioso? / What is the base address of the malicious process? | `0x8056e27c` |
| 7 | ¿Qué nombre ventana tiene el proceso malicioso? / What window name does the malicious process use? | `@WanaDecryptor@` |
| 7 | ¿Qué ruta completa tiene el binario? / What is the full path of the binary? | `C:\Intel\ivecuqmanpnirkt615\@WanaDecryptor@.exe` |
| 7 | ¿Qué proceso lanza el ransomware? / Which process launches the ransomware? | `tasksche.exe` |
| 7 | ¿Cómo se llama el ransomware? / What is the name of the ransomware? | `Wannacry` |
| 7 | ¿Qué módulo se usó para detectarlo? / Which module was used to detect it? | `windows.filescan` |
| 8 | ¿Necesitas responder algo más? / Is there anything else to answer? | `No answer needed` |

---

**Metodología:**

1. Identificación del perfil de memoria con `imageinfo`.
2. Listado de procesos con `pslist` y `pstree`.
3. Análisis de DLLs y árbol de procesos.
4. Volcado y análisis de procesos sospechosos (`memdump`).
5. Detección de malware conocido (WannaCry) con `psxview`, `filescan` y `skeleton`.

### Cadena de ataque / Attack Chain

El fichero `@WanaDecryptor@.exe` se ejecuta desde `C:\Intel\ivecuqmanpnirkt615\`, es lanzado por `tasksche.exe`, y su actividad se confirma mediante `windows.filescan`:

```text
reader_sl.exe (PID 1484, PPID 3) -> explorer.exe -> tasksche.exe -> @WanaDecryptor@.exe (Wannacry)
```

**Learning chain:**

- El primer paso de cualquier análisis de memoria es determinar el perfil correcto (`imageinfo`).
- `pslist`/`pstree` revelan la cadena de ejecución y los procesos inyectados.
- WannaCry puede identificarse por su ventana `@WanaDecryptor@` y los archivos de `C:\Intel\`.

**Lección:** *El análisis de memoria debe empezar siempre por el perfil correcto; sin él, los demás módulos de Volatility producen resultados erróneos.*

**MITRE ATT&CK:**
- T1006 - Direct Volume Access
- T1059 - Command and Scripting Interpreter
- T1486 - Data Encrypted for Impact
- T1569 - System Services / Service Execution

**Fuente:** [TryHackMe - Volatility Essentials](https://tryhackme.com/room/volatilityessentials)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.