# Autopsy

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `autopsy` |
| **Link** | [TryHackMe](https://tryhackme.com/room/autopsy) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Autopsy, Sleuth Kit, análisis forense, artefactos, Eraser, anti-forensics |
| **Impacto** | Realización de un análisis forense completo con Autopsy sobre una imagen de disco: creación de casos, extracción de datos, detección de herramientas anti-forenses y recuperación de flags. |

---

**Contexto:** La sala introduce **Autopsy** como herramienta forense de código abierto para el análisis de imágenes de disco. Se aprende a crear un caso, a identificar la extensión de los casos de Autopsy, a comparar la herramienta con alternativas comerciales como **EnCase** y a extraer información del sistema analizado. En el caso práctico se detectan herramientas anti-forenses como **Eraser**, se recuperan datos del sistema (sistema operativo, porcentajes, procesos como `googledrivesync.exe`), se investigan los artefactos de la máquina (usuario, IP, categorías de casos) y se obtienen las flags y fechas relevantes.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de Autopsy, del Sleuth Kit y del ecosistema de análisis forense que utilizará el laboratorio. Se explica el flujo de trabajo de la sala. Tarea informativa sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción a Autopsy y al análisis forense. | `No answer needed` |

### Task 2: Crear un caso / Creating a Case

**Explicación:** Se crea el caso forense en Autopsy importando la imagen de disco del sistema a analizar. La extensión que usa Autopsy para guardar los proyectos/casos es `.aut`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la extensión de los casos creados por Autopsy? | `.aut` |
| 2 | Completar los pasos de creación del caso con la imagen de disco. | `No answer needed` |

### Task 3: Herramientas similares / Similar Tools

**Explicación:** Pregunta teórica sobre el ecosistema forense: la herramienta comercial más conocida equivalente a Autopsy es **EnCase**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué herramienta forense comercial es similar a Autopsy? | `EnCase` |

### Task 4: Primeros pasos / Getting Started

**Explicación:** Se configuran los módulos de ingesta de Autopsy (hash, strings, etc.) y se espera a que termine el procesado de la imagen antes de comenzar el análisis. Paso práctico sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Configurar la ingesta y esperar al procesado de la imagen. | `No answer needed` |

### Task 5: Análisis inicial / Initial Analysis

**Explicación:** Se analizan los resultados de la ingesta: el número de extensiones/tipos de archivo detectados y los procesos vinculados a artefactos del sistema. Se identifica el proceso **googledrivesync.exe** relacionado con Google Drive.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor encontrado en el análisis (paso 1)? | `4` |
| 2 | ¿Cuál es el valor encontrado en el análisis (paso 2)? | `10` |
| 3 | ¿Qué proceso asociado a Google Drive se detecta en el análisis? | `googledrivesync.exe` |

### Task 6: Datos del sistema / System Data

**Explicación:** A partir de los artefactos del sistema se recupera la información básica de la máquina analizada: el sistema operativo instalado, el porcentaje de espacio/sectores procesado y el número de registros relevante.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué sistema operativo ejecuta la máquina analizada? | `Windows 7 Ultimate Service Pack 1` |
| 2 | ¿Qué porcentaje se indica en el análisis del sistema? | `40.8%` |
| 3 | ¿Qué valor numérico del sistema se facilita en el análisis? | `10` |

### Task 7: Investigación del caso / Investigating the Case

**Explicación:** Se profundiza en la investigación del caso forense: se detecta la herramienta anti-forense **Eraser**, el usuario implicado (`IAMAN`), la dirección IP `10.11.11.128`, las categorías del caso (information leakage cases / anti-forensic tools), la flag del caso y la nota de texto que cierra la investigación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué herramienta anti-forense se detecta en el sistema? | `Eraser` |
| 2 | ¿Qué usuario está implicado en el caso? | `IAMAN` |
| 3 | ¿Qué dirección IP aparece asociada al caso? | `10.11.11.128` |
| 4 | ¿Qué categoría de caso se identifica? | `information leakage cases` |
| 5 | ¿Qué tipo de herramientas se encuentran documentadas? | `anti-forensic tools` |
| 6 | ¿Cuál es la flag del caso forense? | `fe18b02e890f7a789c576be8abccdc99` |
| 7 | ¿Cuál es la nota/mensaje encontrado al final de la investigación? | `Tomorrow...Everything will be OK...` |

### Task 8: Banderas finales / Final Flags

**Explicación:** Se recopilan los últimos datos estadísticos del caso: el número de resultados relevante y la fecha asociada al evento de la máquina.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor estadístico que cierra el análisis? | `46` |
| 2 | ¿Qué fecha se asocia al evento investigado? | `March 25, 2015` |

### Task 9: Conclusión / Conclusion

**Explicación:** Recapitulación de la sala: el valor de Autopsy para el análisis forense de imágenes y la importancia de detectar herramientas anti-forenses. No hay respuesta que enviar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción a Autopsy y al análisis forense. | `No answer needed` |
| 2 | ¿Cuál es la extensión de los casos creados por Autopsy? | `.aut` |
| 3 | Completar los pasos de creación del caso con la imagen de disco. | `No answer needed` |
| 4 | ¿Qué herramienta forense comercial es similar a Autopsy? | `EnCase` |
| 5 | Configurar la ingesta y esperar al procesado de la imagen. | `No answer needed` |
| 6 | ¿Cuál es el valor encontrado en el análisis (paso 1)? | `4` |
| 7 | ¿Cuál es el valor encontrado en el análisis (paso 2)? | `10` |
| 8 | ¿Qué proceso asociado a Google Drive se detecta en el análisis? | `googledrivesync.exe` |
| 9 | ¿Qué sistema operativo ejecuta la máquina analizada? | `Windows 7 Ultimate Service Pack 1` |
| 10 | ¿Qué porcentaje se indica en el análisis del sistema? | `40.8%` |
| 11 | ¿Qué valor numérico del sistema se facilita en el análisis? | `10` |
| 12 | ¿Qué herramienta anti-forense se detecta en el sistema? | `Eraser` |
| 13 | ¿Qué usuario está implicado en el caso? | `IAMAN` |
| 14 | ¿Qué dirección IP aparece asociada al caso? | `10.11.11.128` |
| 15 | ¿Qué categoría de caso se identifica? | `information leakage cases` |
| 16 | ¿Qué tipo de herramientas se encuentran documentadas? | `anti-forensic tools` |
| 17 | ¿Cuál es la flag del caso forense? | `fe18b02e890f7a789c576be8abccdc99` |
| 18 | ¿Cuál es la nota/mensaje encontrado al final de la investigación? | `Tomorrow...Everything will be OK...` |
| 19 | ¿Cuál es el valor estadístico que cierra el análisis? | `46` |
| 20 | ¿Qué fecha se asocia al evento investigado? | `March 25, 2015` |
| 21 | Leer la conclusión de la sala. | `No answer needed` |

---

**Metodología:**

1. Se presenta Autopsy y se crea un caso forense con extensión `.aut`, importando la imagen de disco del sistema.
2. Se configuran los módulos de ingesta (hash, strings) y se espera al procesado de la imagen.
3. Se analizan los resultados: extensiones de archivos, procesos (como `googledrivesync.exe`) y datos del sistema operativo (`Windows 7 Ultimate Service Pack 1`).
4. Se investigan los artefactos del caso: herramienta anti-forense **Eraser**, usuario `IAMAN`, IP `10.11.11.128` y categorías del caso.
5. Se recuperan la flag `fe18b02e890f7a789c576be8abccdc99` y la nota `Tomorrow...Everything will be OK...`.
6. Se cierra el análisis con los valores estadísticos y la fecha relevante del caso.

### Cadena de ataque / Attack Chain

```
Crear caso (.aut) -> importar imagen de disco
  -> Ingesta (hash/strings) -> procesar
  -> Análisis de archivos y procesos (googledrivesync.exe)
  -> Datos del sistema (Windows 7 Ultimate SP1, 40.8%)
  -> Artefactos: Eraser, IAMAN, 10.11.11.128
  -> Categorías: information leakage / anti-forensic tools
  -> Flag + nota final (Tomorrow...Everything will be OK...)
```

**Learning chain:** Autopsy → Creación de caso → Ingesta → Análisis de archivos → Datos del sistema → Artefactos → Anti-forense → Flags

**Lección:** *El análisis forense metódico con Autopsy permite reconstruir la actividad de un sistema incluso cuando se han utilizado herramientas anti-forenses como Eraser, y la categorización de los hallazgos es esencial para documentar el caso.*

**MITRE ATT&CK:** T1005 (Data from Local System), T1074 (Data Staged), T1070 (Indicator Removal on Host)

**Fuente:** [TryHackMe - Autopsy](https://tryhackme.com/room/autopsy)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.