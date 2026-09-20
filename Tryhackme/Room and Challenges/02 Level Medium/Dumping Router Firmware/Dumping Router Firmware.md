# Dumping Router Firmware

| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `dumpingrouterfirmware` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dumpingrouterfirmware) |
| **Sección** | 02 Level Medium |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | binwalk / firmware / uImage / SquashFS / router / busybox / dropbear / sqlite3 |
| **Impacto** | Extracción y análisis completo del firmware de un router (Linksys WRT1900ACS): cabeceras uImage, sistema de archivos, binarios, servicios y credenciales |

---

**Contexto:** La sala enseña a extraer y analizar el firmware de un router (Linksys WRT1900ACS) desde una imagen de actualización. Primero se reconocen las firmas y cabeceras (uImage), se extraen las particiones con binwalk (`-e`) y se identifican la arquitectura ARM, el kernel y los metadatos de la imagen. Después se monta el sistema de archivos (SquashFS) y se inspeccionan binarios (busybox, dropbear, sqlite3), rutas, tablas de configuración y credenciales por defecto.

## Solucionario

### Task 1: Presentación del reto

**Explicación:** Tarea introductoria que presenta la metodología de extracción de firmware y el router objetivo (Linksys WRT1900ACS). No requiere respuesta: solo despliegue del entorno y descarga de la imagen.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Presentación de la sala y del objeto de análisis | `No answer needed` |

### Task 2: Identificación y extracción del firmware

**Explicación:** La imagen descargada corresponde al **Linksys WRT1900ACS Router**, que corre sobre **Linux**. El análisis con binwalk identifica la cabecera **uImage header** (formato), la fecha **2020-04-22 11:07:26**, el checksum **0xABEBC439** y un tamaño de **4229755 bytes**. La arquitectura es **ARM**, el kernel es la versión **3.10.39** y con `-e` se extraen las particiones. Las restantes sub-preguntas de esta tarea son de tipo informativo.

1. Linksys WRT1900ACS Router
2. Linux
3. (informativo)
4. (informativo)
5. -e
6. uImage header
7. 2020-04-22 11:07:26
8. 0xABEBC439
9. 4229755 bytes
10. ARM
11. Yes
12. 3.10.39
13. (informativo)
14. (informativo)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué router se analiza en la sala? | `Linksys WRT1900ACS Router` |
| 2 | ¿Qué sistema operativo corre el router? | `Linux` |
| 3 | Sub-pregunta informativa | `No answer needed` |
| 4 | Sub-pregunta informativa | `No answer needed` |
| 5 | ¿Con qué parámetro extrae binwalk las particiones? | `-e` |
| 6 | ¿Qué cabecera/firma detecta binwalk? | `uImage header` |
| 7 | ¿Qué fecha/timestamp reporta la imagen? | `2020-04-22 11:07:26` |
| 8 | ¿Qué checksum reporta la imagen? | `0xABEBC439` |
| 9 | ¿Qué tamaño tiene la imagen? | `4229755 bytes` |
| 10 | ¿Qué arquitectura tiene el firmware? | `ARM` |
| 11 | ¿Se puede ejecutar directamente el firmware? | `Yes` |
| 12 | ¿Qué versión de kernel utiliza? | `3.10.39` |
| 13 | Sub-pregunta informativa | `No answer needed` |
| 14 | Sub-pregunta informativa | `No answer needed` |

### Task 3: Exploración del sistema de archivos

**Explicación:** Una vez extraído el SquashFS se explora el sistema de archivos: el intérprete de comandos principal está en **/bin/busybox** (que también da nombre al binario: **busybox**), el directorio temporal es **/tmp/**, el directorio web es **/www/**, la librería de base de datos es **sqlite3**, la fecha de extracción del árbol es **2020-04-22 11:44**, el servidor SSH es **dropbear** y el vendor de la configuración es **Cisco**. En la base de datos se revisan las tablas **services** y **system_defaults**, con versión **2.0.3.201002** y las interfaces **guest_lan, lan, wan**. La última sub-pregunta es informativa.

1. /bin/busybox
2. /tmp/
3. /www/
4. busybox
5. sqlite3
6. 2020-04-22 11:44
7. dropbear
8. Cisco
9. services
10. system_defaults
11. 2.0.3.201002
12. guest_lan, lan, wan
13. (informativo)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la ruta del busybox? | `/bin/busybox` |
| 2 | ¿Cuál es el directorio de temporales? | `/tmp/` |
| 3 | ¿Cuál es el directorio web? | `/www/` |
| 4 | ¿Qué comando/binario da nombre al intérprete? | `busybox` |
| 5 | ¿Qué librería/herramienta de base de datos se encuentra? | `sqlite3` |
| 6 | ¿Qué fecha se asocia al árbol de archivos? | `2020-04-22 11:44` |
| 7 | ¿Qué servidor SSH se identifica? | `dropbear` |
| 8 | ¿Qué vendor se identifica en la configuración? | `Cisco` |
| 9 | ¿Qué tabla de servicios se revisa? | `services` |
| 10 | ¿Qué tabla de valores por defecto se revisa? | `system_defaults` |
| 11 | ¿Qué versión de firmware/software se reporta? | `2.0.3.201002` |
| 12 | ¿Qué interfaces aparecen en la configuración? | `guest_lan, lan, wan` |
| 13 | Sub-pregunta informativa | `No answer needed` |

---

**Metodología:**

1. Descargar la imagen de firmware del router Linksys WRT1900ACS e identificarla (Linux, uImage, ARM).
2. Extraer las particiones con `binwalk -e` y anotar los metadatos de la cabecera (fecha, checksum, tamaño, kernel).
3. Montar/descomprimir la imagen extraída para acceder al sistema de archivos (SquashFS).
4. Explorar directorios y binarios clave: `/bin/busybox`, `/tmp/`, `/www/`, `sqlite3`, `dropbear`.
5. Revisar las tablas de configuración de la base de datos del router (services, system_defaults) y anotar las interfaces y credenciales.

**Learning chain:** Firmware router -> Identificación (Linux/ARM) -> binwalk -e -> uImage header -> kernel 3.10.39 -> Extracción -> SquashFS -> busybox -> dropbear -> sqlite3 -> Configuración (Cisco) -> Credenciales/interfaces

**Lección:** *Con binwalk y la extracción de cabeceras se reconstruye el sistema de archivos de un router, exponiendo binarios, servicios y credenciales embebidas en la configuración.*

**MITRE ATT&CK:** N/A (análisis de firmware / ingeniería inversa de hardware, no una técnica ofensiva específica)

**Fuente:** [TryHackMe - Dumping Router Firmware](https://tryhackme.com/room/dumpingrouterfirmware)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.