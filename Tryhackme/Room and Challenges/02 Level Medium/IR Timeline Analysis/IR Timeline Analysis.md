# IR Timeline Analysis [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough
* **Slug:** `dfirtimelineanalysis`
* **Link:** https://tryhackme.com/room/dfirtimelineanalysis
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Writeups públicos de 0xOG (Medium) y thmrevenant.

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de Digital Forensics and Incident Response (DFIR) centrada en timeline analysis: construir y analizar líneas temporales de eventos a partir de imágenes de disco. Se estudian las fuentes de datos (metadatos del sistema de archivos), la conversión a UTC y la creación de super timelines con la suite de plaso/log2timeline (`log2timeline`, `pinfo.py`, `psort.py`), aplicándolo después a dos casos prácticos (Jimmy y el challenge final) para responder preguntas sobre programas ejecutados, búsquedas, cronjobs y accesos SSH.
> **EN:** A Digital Forensics and Incident Response (DFIR) room focused on timeline analysis: building and analyzing chronological event timelines from disk images. Data sources (filesystem metadata), UTC conversion and super timeline creation with the plaso/log2timeline suite (`log2timeline`, `pinfo.py`, `psort.py`) are covered, then applied to two practical cases (Jimmy and the final challenge) to answer questions about executed programs, searches, cronjobs and SSH access.

### Task 1 - Introducción / Introduction

> **ES:** Presentación de la sala: por qué ordenar los eventos de un incidente de forma secuencial es fundamental para reconstruir qué ocurrió, cuándo y con qué herramientas.
> **EN:** Room presentation: why ordering an incident's events sequentially is essential to reconstruct what happened, when, and with which tools.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Tarea de introducción / Introduction task) | `No answer needed` |

### Task 2 - Conceptos de Timeline Analysis / Timeline Analysis Concepts

> **ES:** Se repasan los conceptos clave: analizar eventos revisándolos secuencialmente contra el tiempo; el sello temporal de creación de un archivo ("Birth"); y la normalización de marcas de tiempo a UTC (sincronización temporal), imprescindible para correlacionar datos de distintas zonas horarias.
> **EN:** Key concepts are reviewed: analyzing events by reviewing them sequentially against time; the creation timestamp of a file ("Birth"); and the normalization of timestamps to UTC (time synchronization), essential to correlate data from different time zones.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| When security events are reviewed sequentially against time, what is this known as? | `Timeline analysis` |
| When a file is created, what timestamp tag would it have? | `Birth` |
| Converting event timestamps into UTC can be described as? | `Time synchronization` |

### Task 3 - Fuentes de datos / Data Sources

> **ES:** Se describen las fuentes de datos que alimentan una timeline: metadatos del sistema de archivos (MFT, MACB times), registros, historiales de navegación, logs de eventos de Windows, etc., cada uno con parsers específicos dentro de plaso.
> **EN:** The data sources feeding a timeline are described: filesystem metadata (MFT, MACB times), registry, browser history, Windows event logs, etc., each with specific parsers inside plaso.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What specific data source provides detailed information regarding user interactions within a digital environment? | `File system metadata` |
| (Tarea práctica / Practical task) | `No answer needed` |

### Task 4 - Timelines con Log2Timeline / Timelines with Log2Timeline

> **ES:** Se crea una timeline desde una imagen con `log2timeline`. El argumento `--storage-file` define el fichero de salida (`.plaso`); después, `pinfo.py` resume las fuentes de eventos parseadas y `psort.py` filtra y ordena los eventos. El caso de Jimmy responde a preguntas sobre fuentes parseadas, eventos de `firefox_history` y la hora de creación de `interview.txt`.
> **EN:** A timeline is created from an image with `log2timeline`. The `--storage-file` argument defines the output file (`.plaso`); then `pinfo.py` summarizes the parsed event sources and `psort.py` filters and sorts events. The Jimmy case answers questions about parsed sources, `firefox_history` events and the creation time of `interview.txt`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What argument is used with Log2Timeline to indicate our output file? | `--storage-file` |
| Based on the Jimmy_timeline.plaso file, how many event sources are parsed after running pinfo.py against the storage file? | `4982` |
| On the same timeline file, how many events were generated for the firefox_history? | `50` |
| Based on the B4DM755 timeline, what time was the interview.txt file created? (hh:mm:ss) | `14:02:34` |

### Task 5 - Análisis de timelines / Timeline Analysis

> **ES:** Con la super timeline ya generada se analizan los datos: tipos de datos del sketch de Jimmy en la herramienta de visualización, las entradas de la EVTX Gap Analysis, el buscador empleado por Jimmy Wilson ("how to disappear without a trace?") y la ruta del programa que lanzó el Microsoft Antimalware Service.
> **EN:** With the super timeline generated, the data is analysed: data types of Jimmy's sketch in the visualization tool, the entries of the EVTX Gap Analysis, the search engine used by Jimmy Wilson ("how to disappear without a trace?") and the path of the program that launched Microsoft Antimalware Service.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| How many data types were in the Jimmy Supertimeline sketch? | `48` |
| How many entries were in the EVTX Gap Analysis under the Jimmy Supertimeline? | `34870` |
| Which search engine did Jimmy Wilson use to search for "how to disappear without a trace?" | `Bing` |
| What is the path of the program that was called to initiate Microsoft Antimalware Service? | `C:\Program Files\Microsoft Security Client\MsMpEng.exe` |

### Task 6 - Práctica de Timeline Analysis / Timeline Analysis Practical

> **ES:** En el caso práctico final se trabaja sobre `Timeline_Challenge.plaso` con `psort.py`, aplicando análisis y tagging (por ejemplo `-o null --analysis tagging --tagging-file tag_linux.txt`). Se responde sobre fuentes de eventos totales, eventos del parser `dpkg`, número de tags, el elemento más etiquetado (`login_failed`), el usuario del cronjob que ejecuta `app.py` (`smokey`) y el hash del login SSH exitoso con PID 1669.
> **EN:** In the final practical case, `Timeline_Challenge.plaso` is processed with `psort.py`, applying analysis and tagging (e.g. `-o null --analysis tagging --tagging-file tag_linux.txt`). Questions cover total event sources, events from the `dpkg` parser, number of tags, the most tagged element (`login_failed`), the user of the cronjob that runs `app.py` (`smokey`) and the hash of the successful SSH login with PID 1669.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| How many event sources were identified? | `189100` |
| How many events were generated from the dpkg parser? | `14718` |
| How many total tags were set? | `5408` |
| What is the highest tagged element? | `login_failed` |
| Under which username does the cronjob that executes app.py run? | `smokey` |
| What is the hash of the successful SSH login with the PID 1669? | `a2407e0f3c80d01d2369f15e2b8aa279e790eaa0b1d20ab71cd35c2c7f5aee71` |

### Task 7 - Conclusión / Conclusion

> **ES:** Cierre de la sala: la correcta construcción de timelines y el etiquetado de eventos permiten identificar rápidamente artefactos relevantes, priorizar investigaciones y documentar la secuencia completa de un incidente.
> **EN:** Room wrap-up: properly building timelines and tagging events makes it possible to quickly identify relevant artefacts, prioritize investigations and document the full sequence of an incident.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Tarea de cierre / Wrap-up task) | `No answer needed` |

## Metodología / Methodology

1. **Paso / Step - Adquisición:** se parte de una imagen de disco (E01/raw) del sistema afectado, punto de partida de cualquier análisis forense.
2. **Paso / Step - Generar la timeline:** `log2timeline --storage-file <nombre>.plaso <imagen>` procesa los artefactos y guarda los eventos en un almacén de plaso.
3. **Paso / Step - Inventario de fuentes:** `pinfo.py` muestra las fuentes de eventos y los parsers que han trabajado sobre el almacén (MFT, EVTX, dpkg, firefox_history, etc.).
4. **Paso / Step - Procesar la super timeline:** `psort.py` ordena, filtra y exporta los eventos a CSV/JSON; combinado con tagging (`--analysis tagging --tagging-file tag_linux.txt`) se enriquecen los eventos con etiquetas de interés.
5. **Paso / Step - Análisis focalizado:** se consulta el CSV por parser, usuario o artefacto para responder preguntas concretas (programas ejecutados, búsquedas web, accesos SSH, cronjobs).
6. **Paso / Step - Correlación temporal:** las marcas de tiempo normalizadas a UTC permiten encadenar eventos de distintas fuentes y reconstruir el orden exacto de la intrusión.

### Cadena de ataque / Attack Chain

```
Imagen de disco (E01/raw)
        |
log2timeline --storage-file timeline.plaso <imagen>
        |
pinfo.py -> resumen de fuentes de eventos y parsers
        |
psort.py -> super timeline (CSV/JSON) + tagging
        |
Análisis por parser/artefacto (firefox, dpkg, evtx, ssh...)
        |
Búsquedas y filtros (login_failed, smokey, PID 1669)
        |
Secuencia de eventos reconstruida -> preguntas del caso
```

**Lección:** Una timeline bien construida y etiquetada convierte montañas de artefactos en una cronología accionable; la normalización UTC y el etiquetado de eventos son lo que separa un volcado de datos de una reconstrucción forense real.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.