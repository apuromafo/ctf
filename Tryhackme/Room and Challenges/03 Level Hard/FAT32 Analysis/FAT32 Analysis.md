# FAT32 Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Forensics | fat32analysis | [FAT32 Analysis](https://tryhackme.com/room/fat32analysis) | 03 Level Hard | TryHackMe | Malware, Tácticas, Valores hex, Archivos, Timestamps, Flags | Alto |

---

**Contexto:**

> **ES:** Room de análisis forense sobre una imagen de sistema de archivos FAT32. Se examinan malware, tácticas MITRE, valores de clúster y sector, archivos borrados, timestamps manipulados, entradas FAT y una exfiltración de datos documentada con sus flags.
> **EN:** Forensics room analysing a FAT32 filesystem image. It covers malware, MITRE tactics, cluster/sector values, deleted files, manipulated timestamps, FAT entries and a documented data exfiltration with its flags.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:**

El contenido original de la tarea es el siguiente:

1. No answer needed

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 1 | ¿Hay respuesta para esta tarea? / Is there an answer for this task? | `No answer needed` |

### Task 2: Configuración del análisis / Analysis setup

**Explicación:**

El contenido original de la tarea es el siguiente:

2. No answer needed

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 2 | ¿Hay respuesta para esta tarea? / Is there an answer for this task? | `No answer needed` |

### Task 3: Identificación de malware / Malware identification

**Explicación:**

El contenido original de la tarea es el siguiente:

3. 1. Stuxnet
   2. Defense Evasion

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 3 | ¿Qué malware se identificó en el análisis? / What malware was identified in the analysis? | `Stuxnet` |
| 3 | ¿Qué táctica MITRE ATT&CK está asociada? / What MITRE ATT&CK tactic is associated? | `Defense Evasion` |

### Task 4: Análisis de volúmenes / Volume analysis

**Explicación:**

El contenido original de la tarea es el siguiente:

4. 1. 10000000
   2. 00387E00

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 4 | ¿Cuál es el primer valor hexadecimal encontrado? / What is the first hexadecimal value found? | `10000000` |
| 4 | ¿Cuál es el segundo valor hexadecimal encontrado? / What is the second hexadecimal value found? | `00387E00` |

### Task 5: Recuperación de archivos / File recovery

**Explicación:**

El contenido original de la tarea es el siguiente:

5. 1. careers.txt
   2. F484

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 5 | ¿Cuál es el nombre del archivo localizado? / What is the name of the located file? | `careers.txt` |
| 5 | ¿Cuál es el valor asignado? / What is the assigned value? | `F484` |

### Task 6: Análisis de estructura / Structure analysis

**Explicación:**

El contenido original de la tarea es el siguiente:

6. Directory Structure and File Name Analysis

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 6 | ¿Cuál es la técnica de análisis aplicada? / What analysis technique was applied? | `Directory Structure and File Name Analysis` |

### Task 7: Archivos ocultos / Hidden files

**Explicación:**

El contenido original de la tarea es el siguiente:

7. 1. BEMYVA~1
   2. THM{F0uNdTh3H!Dd3nF1l3}

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 7 | ¿Cuál es el alias 8.3 del archivo oculto? / What is the 8.3 alias of the hidden file? | `BEMYVA~1` |
| 7 | ¿Cuál es la flag de la tarea? / What is the task flag? | `THM{F0uNdTh3H!Dd3nF1l3}` |

### Task 8: Timestamps / Timestamps

**Explicación:**

El contenido original de la tarea es el siguiente:

8. 1. 2018-01-10 00:00:00
   2. THM{T1m3St0Mp3D}

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 8 | ¿Cuál es la fecha/hora del timestamp manipulado? / What is the manipulated timestamp date/time? | `2018-01-10 00:00:00` |
| 8 | ¿Cuál es la flag de la tarea? / What is the task flag? | `THM{T1m3St0Mp3D}` |

### Task 9: Entradas FAT / FAT entries

**Explicación:**

El contenido original de la tarea es el siguiente:

9. 1. E5
   2. THM{r3Tr!3v3D_3v!d3nC3}

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 9 | ¿Cuál es la marca de entrada FAT encontrada? / What is the FAT entry marker found? | `E5` |
| 9 | ¿Cuál es la flag de la tarea? / What is the task flag? | `THM{r3Tr!3v3D_3v!d3nC3}` |

### Task 10: Exfiltración de datos / Data exfiltration

**Explicación:**

El contenido original de la tarea es el siguiente:

10. 1. 0020FC00
    2. Exfiltrated_data
    3. THM{D@t@3xf!lL}
    4. 10862
    5. Reverseshell.py
    6. THM{B@ckD00rF0unD}
    7. Legal_Affairs_Notes.txt
    8. THM{D@t@g@tH3r!nG} 

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 10 | ¿Cuál es el offset hexadecimal? / What is the hexadecimal offset? | `0020FC00` |
| 10 | ¿Cuál es el nombre del directorio de exfiltración? / What is the exfiltration directory name? | `Exfiltrated_data` |
| 10 | ¿Cuál es la flag de exfiltración? / What is the exfiltration flag? | `THM{D@t@3xf!lL}` |
| 10 | ¿Cuál es el valor de tamaño? / What is the size value? | `10862` |
| 10 | ¿Cuál es el nombre del archivo de reverso? / What is the reverse shell file name? | `Reverseshell.py` |
| 10 | ¿Cuál es la flag de la puerta trasera? / What is the backdoor flag? | `THM{B@ckD00rF0unD}` |
| 10 | ¿Cuál es el nombre del archivo de notas legales? / What is the legal affairs notes file name? | `Legal_Affairs_Notes.txt` |
| 10 | ¿Cuál es la flag final de la exfiltración? / What is the final exfiltration flag? | `THM{D@t@g@tH3r!nG} ` |

### Task 11: Conclusión / Conclusion

**Explicación:**

El contenido original de la tarea es el siguiente:

11. No answer needed

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 11 | ¿Hay respuesta para esta tarea? / Is there an answer for this task? | `No answer needed` |

---

**Metodología:**

Análisis forense de imagen FAT32: inspección de entradas de directorio, cadena de clústeres, alias 8.3, marcas de entrada `E5`, comparación de timestamps (timestomp), recuperación de archivos borrados y correlación de artefactos de exfiltración.

### Cadena de ataque / Attack Chain

1. Conteo de clústeres y sectores de la imagen FAT32.
2. Identificación de malware (Stuxnet) y la táctica MITRE asociada (Defense Evasion).
3. Localización de archivos borrados (`careers.txt`, `BEMYVA~1`) y su análisis estructural.
4. Detección de timestamps manipulados y recuperación de entrada `E5`.
5. Documentación de la exfiltración: directorio, datos, archivos y flags.

**Learning chain:**

`FAT32` → volumen → clústeres → directorios → entradas FAT → timestamps → archivos borrados → exfiltración → flags.

**Lección:** *Los sistemas de archivos guardan una huella forense completa incluso después del borrado: cada entrada, timestamp y alias 8.3 cuenta una historia que permite reconstruir malware, puertas traseras y fugas de datos.*

**MITRE ATT&CK:** T1005 Data from Local System, T1070.006 Timestomp, T1048.003 Exfiltration Over Unencrypted Non-C2 Protocol, T1505.003 Web Shell.

**Fuente:** [TryHackMe - FAT32 Analysis](https://tryhackme.com/room/fat32analysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.