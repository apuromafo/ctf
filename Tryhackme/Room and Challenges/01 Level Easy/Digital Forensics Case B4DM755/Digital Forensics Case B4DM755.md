# Digital Forensics Case B4DM755

| **Dificultad** | Easy |
| **Tipo** | Forense digital (laboratorio) |
| **Slug** | `caseb4dm755` |
| **Link** | [TryHackMe](https://tryhackme.com/room/caseb4dm755) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Autopsy / ExifTool / Cadena de custodia / Adquisición de evidencias |
| **Impacto** | Sala de forensia digital que simula un caso real: identificación del rol del analista, preservación y adquisición de evidencias, análisis de una imagen de disco con Autopsy, extracción de metadatos con ExifTool y preparación de la evidencia para el juicio. |

---

**Contexto:** El laboratorio plantea el caso forense B4DM755 desde la perspectiva de un laboratorio de análisis: primero se elige el rol correcto de cada profesional y qué se busca en una escena, después se aplican los métodos de preservación y adquisición de evidencias (cifrado, hash y copia, sellado y etiquetado). La parte práctica se realiza con Autopsy sobre una imagen de disco (SSD/flash) y con ExifTool sobre los metadatos de fotografías (modelo de cámara, GPS, autor y credenciales). Finaliza con el recorrido de la evidencia por las fases de un juicio.

## Solucionario

### Task 1: Introducción

**Explicación:** Presentación del laboratorio forense B4DM755: un caso simulado de principio a fin (rol del analista, adquisición, análisis y juicio). Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción del caso forense. | `No answer needed` |

### Task 2: El rol del analista forense

**Explicación:** Roles en el proceso: el `Forensics Lab Analyst` clasifica y prioriza pruebas/artefactos; el `DFIR First Responder` es el primero en llegar a la escena. Allí los agentes buscan `digital artefacts and evidence`, pero antes necesitan una orden de registro (`search warrant`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué rol es el encargado de clasificar y priorizar las pruebas y los artefactos? | `Forensics Lab Analyst` |
| 2 | ¿Qué rol es la primera persona que responde en la escena del delito o del incidente? | `DFIR First Responder` |
| 3 | ¿Qué buscan los agentes en la escena? | `digital artefacts and evidence` |
| 4 | ¿Qué documento debes obtener antes de acceder a la escena y a las pruebas? | `search warrant` |

### Task 3: Preservación de evidencias

**Explicación:** Métodos de preservación: `drive encryption` protege la confidencialidad; `Hash and copy` crea una copia perfecta verificable; `Bag, Seal, and Tag` asegura físicamente los artefactos y mantiene la cadena de custodia.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué medida de protección garantiza la confidencialidad de los datos de la evidencia? | `drive encryption` |
| 2 | ¿Qué método de preservación crea una copia perfecta de la evidencia? | `Hash and copy` |
| 3 | ¿Qué método de preservación asegura físicamente los artefactos obtenidos? | `Bag, Seal, and Tag the obtained artefacts` |

### Task 4: Adquisición de evidencias

**Explicación:** La imagen forense se guarda en un dispositivo auxiliar (`flash drive`); el método correcto es `Taking an image` (copia bit a bit del disco original) y todo el proceso debe quedar documentado (`Ensure proper documentation`) para ser admisible.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de dispositivo de almacenamiento se utiliza para guardar la imagen de la evidencia? | `flash drive` |
| 2 | ¿Qué método captura una imagen bit a bit del disco original? | `Taking an image` |
| 3 | ¿Qué paso garantiza que se registra correctamente todo el proceso de adquisición? | `Ensure proper documentation` |

### Task 5: Análisis con Autopsy

**Explicación:** El análisis de la imagen se hace sin tocar el original gracias a un `write-blocking device`. En Autopsy, el `Evidence Tree Pane` muestra el árbol de directorios y el `File List Pane` los archivos de la selección. En el sistema analizado NO existe un usuario llamado Bob (`N`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Abre el caso en Autopsy y comienza el análisis de la imagen. | `No answer needed` |
| 2 | ¿Qué dispositivo evita que se modifique el disco de la evidencia durante el análisis? | `write-blocking device` |
| 3 | ¿Qué panel de Autopsy muestra el árbol de directorios de los datos? | `Evidence Tree Pane` |
| 4 | ¿Existe un usuario llamado Bob en el sistema analizado? (Y/N) | `N` |
| 5 | ¿Qué panel de Autopsy muestra los archivos del directorio actualmente seleccionado? | `File List Pane` |

### Task 6: Vistas de Autopsy

**Explicación:** El `Viewer Pane` muestra el contenido del archivo seleccionado. La imagen analizada tiene el hash `d82f393a67c6fc87a023b50c785a7247ab1ac395`; Autopsy soporta `8` sistemas de archivos, tiene `6` vistas principales y en el caso se añadieron `3` imágenes de disco.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué panel de Autopsy muestra el contenido del archivo seleccionado? | `Viewer Pane` |
| 2 | ¿Cuál es el hash de la imagen de disco analizada? | `d82f393a67c6fc87a023b50c785a7247ab1ac395` |
| 3 | ¿Cuántos sistemas de archivos soporta Autopsy? | `8` |
| 4 | ¿Cuántas vistas principales tiene la interfaz de Autopsy? | `6` |
| 5 | ¿Cuántas imágenes de disco añadiste al caso? | `3` |

### Task 7: Análisis de metadatos con ExifTool

**Explicación:** Con ExifTool (`exiftool-12.47`) se examinan las evidencias: un `.pdf` y una `.jpg` del `ONEPLUS A6013` (también conocido como `Mi 9 Lite`). La foto contiene GPS (`Y`, en `14°26'25.7"N 120°59'00.8"E`), autor `Karl Renato Abelardo` y metadatos que revelan la contraseña `DarkVault$Pandora=DONOTOPEN!K1ngCr1ms0n!`, la cuenta de `SwiftSpend Financial` de `Mr. Giovanni Vittorio DeVentura`. Todo conduce a la flag del caso `THM{sCr0LL_sCr0LL_cL1cK_cL1cK_4TT3NT10N_2_D3T41L5_15_CRUC14L!!}`.

```bash
exiftool foto.jpg
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué versión de ExifTool se está utilizando? | `exiftool-12.47` |
| 2 | ¿Cuál es el tipo de archivo de la primera evidencia? | `.pdf` |
| 3 | ¿Cuál es el tipo de archivo de la segunda evidencia? | `.jpg` |
| 4 | ¿Cuál es el modelo de cámara con el que se tomó la fotografía? | `ONEPLUS A6013` |
| 5 | ¿Cuál es el nombre comercial alternativo del dispositivo de la fotografía? | `Mi 9 Lite` |
| 6 | ¿Contiene la imagen datos de localización GPS? (Y/N) | `Y` |
| 7 | ¿Quién aparece como autor de la imagen en los metadatos? | `Karl Renato Abelardo` |
| 8 | ¿Cuáles son las coordenadas GPS registradas en la imagen? | `14°26'25.7"N 120°59'00.8"E` |
| 9 | ¿Qué contraseña encontraste en los metadatos? | `DarkVault$Pandora=DONOTOPEN!K1ngCr1ms0n!` |
| 10 | ¿A qué banco pertenece la cuenta encontrada? | `SwiftSpend Financial` |
| 11 | ¿Quién es el titular de la cuenta bancaria? | `Mr. Giovanni Vittorio DeVentura` |
| 12 | ¿Cuál es la bandera del caso? | `THM{sCr0LL_sCr0LL_cL1cK_cL1cK_4TT3NT10N_2_D3T41L5_15_CRUC14L!!}` |

### Task 8: El caso en el juzgado

**Explicación:** En el proceso judicial: la búsqueda previa a la recogida es la fase `Pre-search`, la posterior es `Post-search`, y en la fase del `Trial` se presentan y exponen las evidencias al tribunal.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué fase de búsqueda se realiza antes de la recogida de evidencias? | `Pre-search` |
| 2 | ¿Qué fase de búsqueda se realiza después de la recogida de evidencias? | `Post-search` |
| 3 | ¿En qué fase del proceso judicial se presentan y exponen las evidencias? | `Trial` |

---

**Metodología:** Se parte de la escena del caso: identificar el papel del laboratorio frente al primer respondedor, obtener la orden de registro y definir qué artefactos buscar. La preservación exige cifrado del almacenamiento, copia verificada con hash y sellado/etiquetado de las piezas. La adquisición se realiza sobre un dispositivo auxiliar (flash) mediante imagen forense con documentación completa. El análisis de la imagen se hace con Autopsy (panel de árbol, lista de archivos, visor y actividades) sin modificar el disco gracias al write-blocker. Por último, los metadatos de las imágenes se extraen con ExifTool para recuperar modelo de cámara, coordenadas GPS, autor y credenciales que permiten resolver el caso y seguirlo en las fases del juicio.

**Learning chain:** roles forenses → preservación → adquisición → análisis con Autopsy → metadatos con ExifTool → testimonio judicial.

**MITRE ATT&CK:** T1204.001 (User Execution: Malicious Link), T1552.001 (Unsecured Credentials: Credentials In Files), T1600.002 (Modify Authentication Process: Multi-Factor Authentication)

**Fuente:** [TryHackMe - Digital Forensics Case B4DM755](https://tryhackme.com/room/caseb4dm755)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
