# MalDoc Static Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Malware / Análisis de documentos | maldocstaticanalysis | https://tryhackme.com/room/maldocstaticanalysis | 02 Level Medium | TryHackMe | oledump, documentos maliciosos, VBA, macros, C2 | Identificación de macromalware y su infraestructura de segunda etapa |

---

**Contexto:** La sala **MalDoc Static Analysis** (Malicious Document) enseña a analizar documentos de Office maliciosos mediante **análisis estático**, principalmente con `oledump.py`. Se inspeccionan los streams OLE incrustados, se extraen las macros VBA, se identifican los IOC (URLs, dominios, autores) y se examina el artefacto de segunda etapa que la macro intenta descargar, siguiendo la cadena completa del ataque de phishing.

## Solucionario

### Task 1: Aprovisionamiento del laboratorio
**Explicación:**

Presentación de la sala y despliegue del entorno de análisis.

Respuesta: `No answer needed`

### Task 2: Entorno de trabajo
**Explicación:**

Configuración y herramientas necesarias para el análisis del documento sospechoso.

Respuesta: `No answer needed`

### Task 3: Clasificación inicial del documento
**Explicación:**

Se identifica que la amenaza relacionada con los documentos de Office es un **macro** malicioso distribuido como adjunto de phishing, técnica mapeada como `T1566.001` (Phishing: Spearphishing Attachment). La carga payload del artefacto es de tipo `ransomware`.

1. `ransomware`
2. `T1566.001`

### Task 4: Extracción de macros
**Explicación:**

Se voltean los streams OLE y se extraen las macros VBA del documento para ser examinadas de forma estática.

Respuesta: `No answer needed`

### Task 5: Autor del documento
**Explicación:**

De los metadatos del documento se obtiene el autor del archivo analizado.

Respuesta: `ben`

### Task 6: Análisis de la macro
**Explicación:**

Repasando las macros embebidas se recupera la flag incluida en el propio documento, se identifican los streams relevantes y las líneas/sectores que contienen el código dañino.

1. `THM{Luckily_This_Isn't_Harmful}`
2. `1`
3. `2`
4. `15,18`

### Task 7: IOC de red
**Explicación:**

Del código de la macro se extraen los indicadores de red: el archivo correlación de URLs, el número de entradas inspeccionadas y la URL ofuscada que contacta el malware.

1. `urls.json`
2. `9`
3. `hxxp://aristonbentre[.]com/slideshow/O1uPzXd2YscA/`

### Task 8: Artefacto de segunda etapa
**Explicación:**

Se identifica el equipo/creador del stage 2, el número de streams del artefacto y la URL desde la que se descargará la siguiente carga útil.

1. `CMNatic`
2. `2`
3. `http://thmredteam.thm/stage2.exe`

### Task 9: Detalles del payload
**Explicación:**

Se inspecciona el payload final: el tamaño indicado en las peticiones, el nombre del recurso embebido y el número de peticiones esperadas.

1. `15000`
2. `index1.png`
3. `6`

### Task 10: Cierre de la sala
**Explicación:**

Revisión final de la cadena de ataque documentada en el laboratorio.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Aprovisionamiento del laboratorio | `No answer needed` |
| 2 | Entorno de trabajo | `No answer needed` |
| 3.1 | Tipo de payload final | `ransomware` |
| 3.2 | Técnica MITRE de distribución | `T1566.001` |
| 4 | Extracción de macros | `No answer needed` |
| 5 | Autor del documento | `ben` |
| 6.1 | Flag de la macro | `THM{Luckily_This_Isn't_Harmful}` |
| 6.2 | Stream principal | `1` |
| 6.3 | Segundo stream relevante | `2` |
| 6.4 | Líneas con el código dañino | `15,18` |
| 7.1 | Archivo de correlación de URLs | `urls.json` |
| 7.2 | Número de entradas | `9` |
| 7.3 | URL ofuscada del C2 | `hxxp://aristonbentre[.]com/slideshow/O1uPzXd2YscA/` |
| 8.1 | Equipo / autor del stage2 | `CMNatic` |
| 8.2 | Streams del artefacto stage2 | `2` |
| 8.3 | URL de descarga del stage2 | `http://thmredteam.thm/stage2.exe` |
| 9.1 | Tamaño indicado en la petición | `15000` |
| 9.2 | Recurso embebido | `index1.png` |
| 9.3 | Número de peticiones | `6` |
| 10 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Análisis estático de documentos OLE con oledump: localización de streams, extracción de macros VBA, identificación de IOC (autor, URLs, stage2) y reconstrucción de la cadena de ataque.

**Learning chain:** Documento → streams OLE → macros → IOC → payload de segunda etapa → reconstrucción de la campaña.

**Lección:** *Un documento de Office con macros puede parecer benigno, pero el análisis estático de sus streams revela el C2 y la siguiente fase; la fuerza está en no ejecutarlo nunca.*

**MITRE ATT&CK:** T1566.001 Phishing: Spearphishing Attachment · T1059.005 Command and Scripting Interpreter: Visual Basic.

**Fuente:** [TryHackMe - MalDoc Static Analysis](https://tryhackme.com/room/maldocstaticanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.