# IR Timeline Analysis

| **Dificultad** | MEDIUM | **Tipo** | Walkthrough | **Slug** | `dfirtimelineanalysis` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dfirtimelineanalysis) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | DFIR / Plaso / log2timeline / Timeline Analysis / Forensics / Super Timelines | **Impacto** | Evalúa la construcción y análisis de líneas temporales forenses con la suite plaso |

---

**Contexto:** Sala de Digital Forensics and Incident Response (DFIR) centrada en timeline analysis: construir y analizar líneas temporales de eventos a partir de imágenes de disco. Se estudian las fuentes de datos (metadatos del sistema de archivos), la conversión a UTC y la creación de super timelines con la suite de plaso/log2timeline (`log2timeline`, `pinfo.py`, `psort.py`), aplicándolo después a dos casos prácticos (Jimmy y el challenge final) para responder preguntas sobre programas ejecutados, búsquedas, cronjobs y accesos SSH.

## Solucionario

### Task 1: Introducción

**Explicación:** Presentación de la sala: por qué ordenar los eventos de un incidente de forma secuencial es fundamental para reconstruir qué ocurrió, cuándo y con qué herramientas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Tarea de introducción / Introduction task) | `No answer needed` |

### Task 2: Conceptos de Timeline Analysis

**Explicación:** Se repasan los conceptos clave: analizar eventos revisándolos secuencialmente contra el tiempo; el sello temporal de creación de un archivo ("Birth"); y la normalización de marcas de tiempo a UTC (sincronización temporal), imprescindible para correlacionar datos de distintas zonas horarias.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When security events are reviewed sequentially against time, what is this known as? | `Timeline analysis` |
| 2 | When a file is created, what timestamp tag would it have? | `Birth` |
| 3 | Converting event timestamps into UTC can be described as? | `Time synchronization` |

### Task 3: Fuentes de datos

**Explicación:** Se describen las fuentes de datos que alimentan una timeline: metadatos del sistema de archivos (MFT, MACB times), registros, historiales de navegación, logs de eventos de Windows, etc., cada uno con parsers específicos dentro de plaso.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What specific data source provides detailed information regarding user interactions within a digital environment? | `File system metadata` |
| 2 | (Tarea práctica / Practical task) | `No answer needed` |

### Task 4: Timelines con Log2Timeline

**Explicación:** Se crea una timeline desde una imagen con `log2timeline`. El argumento `--storage-file` define el fichero de salida (`.plaso`); después, `pinfo.py` resume las fuentes de eventos parseadas y `psort.py` filtra y ordena los eventos. El caso de Jimmy responde a preguntas sobre fuentes parseadas, eventos de `firefox_history` y la hora de creación de `interview.txt`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What argument is used with Log2Timeline to indicate our output file? | `--storage-file` |
| 2 | Based on the Jimmy_timeline.plaso file, how many event sources are parsed after running pinfo.py against the storage file? | `4982` |
| 3 | On the same timeline file, how many events were generated for the firefox_history? | `50` |
| 4 | Based on the B4DM755 timeline, what time was the interview.txt file created? (hh:mm:ss) | `14:02:34` |

### Task 5: Análisis de timelines

**Explicación:** Con la super timeline ya generada se analizan los datos: tipos de datos del sketch de Jimmy en la herramienta de visualización, las entradas de la EVTX Gap Analysis, el buscador empleado por Jimmy Wilson ("how to disappear without a trace?") y la ruta del programa que lanzó el Microsoft Antimalware Service.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many data types were in the Jimmy Supertimeline sketch? | `48` |
| 2 | How many entries were in the EVTX Gap Analysis under the Jimmy Supertimeline? | `34870` |
| 3 | Which search engine did Jimmy Wilson use to search for "how to disappear without a trace?" | `Bing` |
| 4 | What is the path of the program that was called to initiate Microsoft Antimalware Service? | `C:\Program Files\Microsoft Security Client\MsMpEng.exe` |

### Task 6: Práctica de Timeline Analysis

**Explicación:** En el caso práctico final se trabaja sobre `Timeline_Challenge.plaso` con `psort.py`, aplicando análisis y tagging (por ejemplo `-o null --analysis tagging --tagging-file tag_linux.txt`). Se responde sobre fuentes de eventos totales, eventos del parser `dpkg`, número de tags, el elemento más etiquetado (`login_failed`), el usuario del cronjob que ejecuta `app.py` (`smokey`) y el hash del login SSH exitoso con PID 1669.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many event sources were identified? | `189100` |
| 2 | How many events were generated from the dpkg parser? | `14718` |
| 3 | How many total tags were set? | `5408` |
| 4 | What is the highest tagged element? | `login_failed` |
| 5 | Under which username does the cronjob that executes app.py run? | `smokey` |
| 6 | What is the hash of the successful SSH login with the PID 1669? | `a2407e0f3c80d01d2369f15e2b8aa279e790eaa0b1d20ab71cd35c2c7f5aee71` |

### Task 7: Conclusión

**Explicación:** Cierre de la sala: la correcta construcción de timelines y el etiquetado de eventos permiten identificar rápidamente artefactos relevantes, priorizar investigaciones y documentar la secuencia completa de un incidente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Tarea de cierre / Wrap-up task) | `No answer needed` |

---

**Metodología:**
1. Adquisición: se parte de una imagen de disco (E01/raw) del sistema afectado, punto de partida de cualquier análisis forense.
2. Generar la timeline: `log2timeline --storage-file <nombre>.plaso <imagen>` procesa los artefactos y guarda los eventos en un almacén de plaso.
3. Inventario de fuentes: `pinfo.py` muestra las fuentes de eventos y los parsers que han trabajado sobre el almacén (MFT, EVTX, dpkg, firefox_history, etc.).
4. Procesar la super timeline: `psort.py` ordena, filtra y exporta los eventos a CSV/JSON; combinado con tagging (`--analysis tagging --tagging-file tag_linux.txt`) se enriquecen los eventos con etiquetas de interés.
5. Análisis focalizado: se consulta el CSV por parser, usuario o artefacto para responder preguntas concretas (programas ejecutados, búsquedas web, accesos SSH, cronjobs).
6. Correlación temporal: las marcas de tiempo normalizadas a UTC permiten encadenar eventos de distintas fuentes y reconstruir el orden exacto de la intrusión.

**Learning chain:** Imagen de disco (E01/raw) → log2timeline --storage-file timeline.plaso <imagen> → pinfo.py (resumen de fuentes y parsers) → psort.py (super timeline CSV/JSON + tagging) → Análisis por parser/artefacto (firefox, dpkg, evtx, ssh...) → Búsquedas y filtros (login_failed, smokey, PID 1669) → Secuencia de eventos reconstruida

**Lección:** *Una timeline bien construida y etiquetada convierte montañas de artefactos en una cronología accionable; la normalización UTC y el etiquetado de eventos son lo que separa un volcado de datos de una reconstrucción forense real.*

**MITRE ATT&CK:** T1005 - Data from Local System; T1078 - Valid Accounts; T1053 - Scheduled Task/Job; T1560 - Archive Collected Data; (DFIR/analítica, orientado a detección y reconstrucción)

**Fuente:** [TryHackMe - IR Timeline Analysis](https://tryhackme.com/room/dfirtimelineanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
