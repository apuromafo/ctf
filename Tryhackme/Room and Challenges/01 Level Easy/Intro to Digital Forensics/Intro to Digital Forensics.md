# Intro to Digital Forensics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `introtodigitalforensics` | https://tryhackme.com/room/introtodigitalforensics | 01 Level Easy | TryHackMe | análisis de evidencias / Chain of Custody / pdfinfo / exiftool / EXIF / metadatos | Aplicar el proceso forense en un caso práctico de secuestro: identificar evidencias, documentar la cadena de custodia y extraer metadatos de un PDF y una foto. |

---

**Contexto:** La room presenta los fundamentos de la forensia digital: qué es, cuál es la evidencia más relevante en una escena (además del smartphone, la cámara y las tarjetas SD: el **laptop**), y la importancia de la **Chain of Custody** (cadena de custodia) para que la evidencia sea admisible. El caso práctico es un secuestro: con **pdfinfo** se obtiene el autor del PDF adjunto, y con **exiftool** se extraen los metadatos EXIF de la foto (calle **Milk Street** y cámara **Canon EOS R6**) que delata dónde se tomó la imagen.

> **ES:** Fundamentos de forensia digital y caso práctico: evidencias en la escena, cadena de custodia y extracción de metadatos con pdfinfo (autor del PDF) y exiftool (ubicacion de la foto y modelo de la camara).
> **EN:** Digital forensics fundamentals and a practical case: scenes evidence, chain of custody and metadata extraction with pdfinfo (PDF author) and exiftool (photo location and camera model).

## Solucionario

### Task 1: Introduction To Digital Forensics / Introducción a la forensia digital

**Explicación:** Se introduce la forensia digital: la ciencia de investigar delitos mediante el análisis de datos digitales (ordenadores, teléfonos, cámaras, tarjetas de memoria...). En la foto del escritorio del caso, además del smartphone, la cámara y las tarjetas SD, el elemento más interesante para la forensia digital es el **laptop** (portátil), por su capacidad de almacenar correos, documentos y actividad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Consider the desk in the photo above. In addition to the smartphone, camera, and SD cards, what would be interesting for digital forensics? / Considera el escritorio de la foto. Además del smartphone, la cámara y las tarjetas SD, ¿qué sería interesante para la forensia digital? | `laptop` |

### Task 2: Digital Forensics Process / Proceso de forensia digital

**Explicación:** El proceso forense debe ser metódico y documentado. Es esencial registrar quién maneja la evidencia en cada momento para que sea admisible en un tribunal. La documentación que registra quién la tuvo y qué responsabilidades la acompañan es la **Chain of Custody** (cadena de custodia).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | It is essential to keep track of who is handling it at any point in time to ensure that evidence is admissible in the court of law. What is the name of the documentation that would help establish that? / Es esencial registrar quién maneja la evidencia en cada momento para asegurar su admisibilidad judicial. ¿Cómo se llama la documentación que ayuda a establecerlo? | `Chain of Custody` |

### Task 3: Practical Example of Digital Forensics / Ejemplo práctico de forensia digital

**Explicación:** Caso práctico de secuestro: se recibe un PDF de rescate con una foto adjunta. Con **pdfinfo** (de poppler) se leen los metadatos del PDF y se obtiene el autor: **Ann Gree Shepherd**. Con **exiftool** (o herramientas similares) se extraen los metadatos EXIF de la imagen adjunta: los campos GPS/ubicación revelan la calle **Milk Street** donde se tomó la foto, y el campo del modelo revela que la cámara era una **Canon EOS R6**.

```bash
pdfinfo ransom-letter.pdf
exiftool photo.jpg
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Using pdfinfo, find out the author of the attached PDF file. / Usando pdfinfo, averigua el autor del archivo PDF adjunto. | `Ann Gree Shepherd` |
| 2 | Using exiftool or any similar tool, try to find where the kidnappers took the image they attached to their document. What is the name of the street? / Usando exiftool o una herramienta similar, intenta encontrar dónde tomaron la imagen adjunta. ¿Cuál es el nombre de la calle? | `Milk Street` |
| 3 | What is the model name of the camera used to take this photo? / ¿Cuál es el modelo de la cámara usada para tomar la foto? | `Canon EOS R6` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Consider the desk in the photo above. In addition to the smartphone, camera, and SD cards, what would be interesting for digital forensics? | `laptop` |
| 2 | It is essential to keep track of who is handling it at any point in time to ensure that evidence is admissible in the court of law. What is the name of the documentation that would help establish that? | `Chain of Custody` |
| 3 | Using pdfinfo, find out the author of the attached PDF file. | `Ann Gree Shepherd` |
| 4 | Using exiftool or any similar tool, try to find where the kidnappers took the image they attached to their document. What is the name of the street? | `Milk Street` |
| 5 | What is the model name of the camera used to take this photo? | `Canon EOS R6` |

---

**Metodología:** Del concepto al caso resuelto: (1) identificar la evidencia relevante en la escena (laptop); (2) establecer y documentar la cadena de custodia; (3) en el caso práctico, extraer metadatos del PDF con `pdfinfo` (autor), y de la foto con `exiftool` (ExifTool) para obtener ubicación (EXIF GPS) y modelo de cámara que sitúan a los secuestradores.

### Cadena de ataque / Attack Chain

```text
Escena (laptop) -> cadena de custodia documentada -> ransom letter.pdf -> pdfinfo (autor: Ann Gree Shepherd) -> foto adjunta -> exiftool (Milk Street + Canon EOS R6) -> localizacion del equipo
```

**Learning chain:** Que es la forensia -> evidencia en escena -> cadena de custodia -> pdfinfo -> exiftool/EXIF -> cierre del caso.

**Lección:** *Los metadatos mienten menos que los humanos: el autor de un PDF y las coordenadas EXIF de una foto sobreviven al borrado casual y convierten una nota de rescate en una pista hacia la ubicacion del atacante.*

**MITRE ATT&CK:** T1204.002 (User Execution: Malicious File), T1560 (Archive Collected Data), T1113 (Screen Capture)

**Fuente:** [TryHackMe - Intro to Digital Forensics](https://tryhackme.com/room/introtodigitalforensics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.