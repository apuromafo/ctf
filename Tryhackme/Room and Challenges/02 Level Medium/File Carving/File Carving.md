# File Carving

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Forense / Recuperación de archivos | filecarving | https://tryhackme.com/room/filecarving | 02 Level Medium | TryHackMe | Magic bytes/File signatures, Autopsy, slack space, carveo manual | Recuperación forense de archivos mediante file carving |

---

**Contexto:** **File Carving** es una sala forense orientada a la recuperación de archivos mediante *file carving*. Se estudian las **file signatures** o magic bytes (JPEG `FFD8FFE0`, atajos de Windows `4C00000001140200`), y se practica el carveo manual sobre imágenes de disco (`Challenge1_Manual_Carve_usb.img`), la extracción de datos del **slack space** (`Challenge2_slack_space.img`), el carveo automático de PDFs e imágenes, y el análisis de sistemas de archivos borrados para recuperar flags ocultas.

## Solucionario

### Task 1: Introduction
**Explicación:**

Introducción a los conceptos de file signatures (magic bytes) y file carving. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 2: File signatures
**Explicación:**

Los magic bytes permiten identificar el formato real de un archivo aunque la extensión haya sido cambiada. La firma que identifica archivos **JPEG** es `FFD8FFE0`, y la firma de los archivos **Windows Shortcut** (LNK) es `4C00000001140200` (sin espacios).

Respuestas del lab (contenido original):

```
1. FFD8FFE0
2. 4C00000001140200
```

### Task 3: Preparación del laboratorio
**Explicación:**

Se cargan las imágenes de disco en la herramienta del laboratorio para los ejercicios de carveo. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 4: Challenge 1 - Manual carving y slack space
**Explicación:**

Carveo manual sobre `Challenge1_Manual_Carve_usb.img`: el offset final del archivo PNG recuperado es `0001526426` y esconde la flag `THM{F1le_Carving_1s_FuN}`. Sobre `Challenge2_slack_space.img`, el archivo recuperado ocupa **31** KB, el archivo extraído sin extensión se llama **randomstuff** y contiene la flag `THM{Fragm3nt_C@rv1ng}`.

Respuestas del lab (contenido original):

```
1. 0001526426
2. THM{F1le_Carving_1s_FuN}
3. 31
4. randomstuff
5. THM{Fragm3nt_C@rv1ng}
```

### Task 5: Carveo automatizado (PDF e imagen)
**Explicación:**

El PDF recuperado se llamaba originalmente **DataSyncTHM_project_phoenix.txt** y contiene `THM{ProjectPhoenix_123}`; la imagen recuperada por carveo esconde `THM{Aut0mat3d_C@rv1ng}`.

Respuestas del lab (contenido original):

```
1. DataSyncTHM_project_phoenix.txt
2. THM{ProjectPhoenix_123}
3. THM{Aut0mat3d_C@rv1ng}
```

### Task 6: Sistema de archivos borrado
**Explicación:**

Análisis del sistema de archivos borrado: los offsets del área relevante son `134946816,135012619`, el formato de la imagen recuperada es **SVG**, su tamaño es **18.29** (unidad del laboratorio) y en ella se esconde la flag `THM{D4t3_0f_D3l3t10n_2024-12-10}`.

Respuestas del lab (contenido original):

```
1. 134946816,135012619
2. SVG
3. 18.29
4. THM{D4t3_0f_D3l3t10n_2024-12-10}
```

### Task 7: Conclusion
**Explicación:**

Cierre de la sala. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 (Introduction) | `No answer needed` |
| 2 | Firma de archivos JPEG | `FFD8FFE0` |
| 3 | Firma de archivos Windows Shortcut (sin espacios) | `4C00000001140200` |
| 4 | ¿Listo para el laboratorio? | `No answer needed` |
| 5 | Offset final del PNG en Challenge1_Manual_Carve_usb.img | `0001526426` |
| 6 | Flag oculta en el archivo recuperado (Challenge 1) | `THM{F1le_Carving_1s_FuN}` |
| 7 | Tamaño del archivo recuperado de Challenge2_slack_space.img (KB) | `31` |
| 8 | Nombre del archivo extraído sin extensión | `randomstuff` |
| 9 | Flag oculta en el archivo recuperado (slack space) | `THM{Fragm3nt_C@rv1ng}` |
| 10 | Nombre original del PDF recuperado | `DataSyncTHM_project_phoenix.txt` |
| 11 | Flag dentro del PDF | `THM{ProjectPhoenix_123}` |
| 12 | Flag en la imagen recuperada por carveo automático | `THM{Aut0mat3d_C@rv1ng}` |
| 13 | Offsets del sistema de archivos borrado | `134946816,135012619` |
| 14 | Formato de la imagen recuperada | `SVG` |
| 15 | Tamaño de la imagen recuperada | `18.29` |
| 16 | Flag oculta en la imagen (fecha de borrado 2024-12-10) | `THM{D4t3_0f_D3l3t10n_2024-12-10}` |
| 17 | Conclusion | `No answer needed` |

---

**Metodología:** Identificación de magic bytes, carveo manual de archivos mediante offsets, recuperación de datos desde el slack space, carveo automatizado de PDF/imágenes y análisis de sistemas de archivos borrados para extraer las flags.

**Learning chain:** Introducción → File signatures → Preparación del lab → Carveo manual → Slack space → Carveo automatizado → Sistema de archivos borrado → Conclusion.

**Lección:** *Los archivos borrados rara vez desaparecen por completo: sus magic bytes y bloques residuales (incluido el slack space) permiten reconstruirlos y extraer datos sensibles, por lo que el borrado no es garantía de eliminación.*

**MITRE ATT&CK:** T1005 Data from Local System · T1070.004 Indicator Removal on Host: File Deletion · T1552.001 Unsecured Credentials: Credentials In Files · T1560 Archive Collected Data.

**Fuente:** [TryHackMe - File Carving](https://tryhackme.com/room/filecarving)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.