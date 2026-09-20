# EXT Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Forense / Sistema de archivos Linux | extanalysis | https://tryhackme.com/room/extanalysis | 02 Level Medium | TryHackMe | ext4_super_block, inodes, timestomping, recuperación de borrados | Análisis forense del sistema de archivos ext2/ext3/ext4 |

---

**Contexto:** **EXT Analysis** es una sala de forense centrada en el sistema de archivos **ext4** (Linux). Se examina la estructura del `ext4_super_block` (como `s_first_data_block` y el offset de `s_blocks_count_lo`), se identifican inodos de archivos concretos (`/etc/passwd`), se estudian los timestamps de creación (`btime`), se detecta **timestomping** (manipulación de fechas) y se recuperan archivos eliminados desde el sistema montado en `/mnt/ext_exercises` para extraer la flag.

## Solucionario

### Task 1: Introduction
**Explicación:**

Introducción a la sala: uso de herramientas nativas de Linux y software forense para detectar técnicas anti-forenses (timestomping), recuperar archivos borrados e interpretar metadatos ext/ext4. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 2: ext4_super_block
**Explicación:**

Miembro de la estructura `ext4_super_block` que contiene el offset del primer bloque de datos: **`s_first_data_block`**. Y en formato decimal, el offset donde se encuentra el miembro `s_blocks_count_lo` dentro de la estructura es **4**.

Respuestas del lab (contenido original):

```
1. s_first_data_block
2. 4
```

### Task 3: Análisis de inodos (VM)
**Explicación:**

El inodo correspondiente al archivo `/etc/passwd` en la VM es el **10083**.

**Respuesta:** `10083`

### Task 4: Timestamps (btime)
**Explicación:**

La marca de tiempo de creación (`btime`) del archivo `/etc/passwd` es `2024-11-28 21:52:28.724316576`.

**Respuesta:** `2024-11-28 21:52:28.724316576`

### Task 5: normal_file.txt y timestomping
**Explicación:**

Seleccionando la imagen `ext4_case.img` en la pestaña File Metadata (Autopsy/Data Sources), el archivo `normal_file.txt` tiene el inodo **12**. El archivo **timestomped.txt** tiene una fecha de creación manipulada de `2025-01-06 03:34:09`, evidencia clara de la técnica anti-forense.

Respuestas del lab (contenido original):

```
1. 12
2. 2025-01-06 03:34:09
```

### Task 6: Fichero timestomped y archivo borrado
**Explicación:**

Identificando el archivo timestomped en `/mnt/ext_exercises`, su fecha de creación original es `2025-01-09 02:27:53` (la original de los metadatos). La flag de la sala se encuentra en el archivo eliminado cuyo contenido empieza por "FFFFFFFFFF": `TMH{sup3r-d3l3Ted-fil3-you-g0tit-nice}`.

Respuestas del lab (contenido original):

```
1. 2025-01-09 02:27:53
2. TMH{sup3r-d3l3Ted-fil3-you-g0tit-nice}
```

### Task 7: Conclusion
**Explicación:**

Cierre de la sala. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 (Introduction) | `No answer needed` |
| 2 | ¿Qué miembro de ext4_super_block guarda el offset del primer data block? | `s_first_data_block` |
| 3 | ¿En qué offset está `s_blocks_count_lo`? (decimal) | `4` |
| 4 | ¿Cuál es el inodo de /etc/passwd en la VM? | `10083` |
| 5 | ¿Cuál es el btime de /etc/passwd? | `2024-11-28 21:52:28.724316576` |
| 6 | ¿Cuál es el inodo de normal_file.txt (ext4_case.img)? | `12` |
| 7 | ¿Cuál es la fecha de creación de timestomped.txt? | `2025-01-06 03:34:09` |
| 8 | ¿Cuál es la fecha de creación original del archivo timestomped? | `2025-01-09 02:27:53` |
| 9 | Flag en el archivo borrado (empieza por "FFFFFFFFFF") | `TMH{sup3r-d3l3Ted-fil3-you-g0tit-nice}` |
| 10 | Conclusion | `No answer needed` |

---

**Metodología:** Inspección de la estructura `ext4_super_block`, localización de inodos mediante herramientas nativas de Linux y Autopsy, comparación de timestamps de creación para detectar timestomping y recuperación manual de archivos borrados en el sistema montado.

**Learning chain:** Introducción → Superblock ext4 → Localización de inodos → Timestamps/btime → Detección de timestomping → Recuperación de borrados → Conclusion.

**Lección:** *El sistema de archivos ext4 conserva metadatos muy ricos (btime, superblock, inodos); el timestomping altera solo parte de ellos y los archivos borrados siguen recuperables, por lo que comparar fechas y mirar los bloques residuales desmonta la técnica anti-forense.*

**MITRE ATT&CK:** T1070.006 Indicator Removal on Host: Timestomp · T1005 Data from Local System · T1036 Masquerading · T1552.001 Unsecured Credentials: Credentials In Files.

**Fuente:** [TryHackMe - EXT Analysis](https://tryhackme.com/room/extanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.