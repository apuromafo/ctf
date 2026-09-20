# Digital Forensics Fundamentals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `digitalforensicsfundamentals` | https://tryhackme.com/room/digitalforensicsfundamentals | 01 Level Easy | TryHackMe | Forensia digital / write blocker / chain of custody / memoria / análisis de imágenes | Fundamentos de la forensia digital: proceso forense, integridad de la evidencia y análisis práctico de imágenes. |

---

**Contexto:** Fundamentos de la forensia digital. Se introduce la disciplina, el proceso de análisis forense (Analysis y Examination), las medidas para preservar la integridad de la evidencia (write blocker y chain of custody), los distintos tipos de imagen (incluida la imagen de memoria) y se cierra con un análisis práctico de una imagen en Autopsy.

> **ES:** Fundamentos de forensia digital: proceso (Analysis/Examination), integridad de evidencia (write blocker, chain of custody), memoria (Memory Image) y práctica de análisis forense.
> **EN:** Digital forensics fundamentals: process (Analysis/Examination), evidence integrity (write blocker, chain of custody), memory (Memory Image) and a practical forensics analysis.

## Solucionario

### Task 1: Introducción a la forensia digital / Introduction to Digital Forensics

**Explicación:** Se introduce la disciplina encargada de analizar dispositivos digitales en busca de evidencia: `digital forensics` (forensia digital).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la rama que analiza dispositivos digitales en busca de evidencia? / What is the branch that analyses digital devices for evidence called? | `digital forensics` |

### Task 2: Proceso de análisis forense / Digital Forensics Process

**Explicación:** El proceso forense incluye varias fases; además de la recolección e identificación, destacan la fase de análisis (`Analysis`) y la fase de examinación profunda (`Examination`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué fase corresponde al análisis de los datos recolectados? / Which phase corresponds to analysing the collected data? | `Analysis` |
| 2 | ¿Qué fase corresponde a la examinación detallada de la evidencia? / Which phase corresponds to the detailed examination of the evidence? | `Examination` |

### Task 3: Integridad de la evidencia / Evidence Integrity

**Explicación:** Para preservar la evidencia se usa un `write blocker` (bloqueador de escritura) que impide modificar el dispositivo origen, y se documenta la cadena de custodia (`chain of custody`) para registrar quién y cómo manipula la evidencia.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué dispositivo impide la escritura sobre la evidencia original? / Which device blocks writes to the original evidence? | `write blocker` |
| 2 | ¿Cómo se llama el registro que documenta el manejo de la evidencia? / What is the log that documents how the evidence is handled called? | `chain of custody` |

### Task 4: Tipos de imágenes / Types of Images

**Explicación:** Existen distintos tipos de adquisición forense; la imagen que captura el estado de la memoria volátil del sistema se denomina `Memory Image`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de imagen captura la memoria del sistema? / Which image type captures the system memory? | `Memory Image` |

### Task 5: Análisis práctico / Practical Analysis

**Explicación:** En el análisis práctico de la imagen se identifican los datos de la evidencia: el nombre de la persona es `Ann Gree Shepherd`, la dirección está en `Milk Street` y la cámara utilizada es una `Canon EOS R6`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre de la persona encontrado en la imagen? / What is the person's name found in the image? | `Ann Gree Shepherd` |
| 2 | ¿Cuál es la dirección encontrada? / What is the address found? | `Milk Street` |
| 3 | ¿Qué cámara se utiliza según los metadatos? / Which camera is used according to the metadata? | `Canon EOS R6` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la rama que analiza dispositivos digitales en busca de evidencia? | `digital forensics` |
| 2 | ¿Qué fase corresponde al análisis de los datos recolectados? | `Analysis` |
| 3 | ¿Qué fase corresponde a la examinación detallada de la evidencia? | `Examination` |
| 4 | ¿Qué dispositivo impide la escritura sobre la evidencia original? | `write blocker` |
| 5 | ¿Cómo se llama el registro que documenta el manejo de la evidencia? | `chain of custody` |
| 6 | ¿Qué tipo de imagen captura la memoria del sistema? | `Memory Image` |
| 7 | ¿Cuál es el nombre de la persona encontrado en la imagen? | `Ann Gree Shepherd` |
| 8 | ¿Cuál es la dirección encontrada? | `Milk Street` |
| 9 | ¿Qué cámara se utiliza según los metadatos? | `Canon EOS R6` |

---

**Metodología:** El room construye la base conceptual de la forensia digital: se define la disciplina, se recorre el proceso forense (Analysis y Examination), se explican las medidas de integridad de la evidencia (write blocker y chain of custody) y los tipos de imágenes (incluida la Memory Image). La última tarea es un análisis práctico de la imagen en el que se extraen la identidad (`Ann Gree Shepherd`), la dirección (`Milk Street`) y la cámara (`Canon EOS R6`).

### Cadena de ataque / Attack Chain

```text
Recolección (write blocker + chain of custody) -> imagen de disco / Memory Image -> fases de Analysis y Examination -> extracción de datos (Ann Gree Shepherd, Milk Street, Canon EOS R6)
```

**Learning chain:** digital forensics → proceso forense (Analysis/Examination) → write blocker → chain of custody → Memory Image → análisis en Autopsy → metadatos (persona, dirección, cámara).

**Lección:** *La validez de cualquier análisis forense depende de la integridad de la evidencia: un write blocker y una cadena de custodia estricta garantizan que los datos analizados (identidad, metadatos, memoria) sean admisibles y fiables.*

**MITRE ATT&CK:** No aplica directamente (sala formativa de forensia); el análisis de metadatos se relaciona con la recolección de evidence de host (T1082 - System Information Discovery en el lado ofensivo).

**Fuente:** [TryHackMe - Digital Forensics Fundamentals](https://tryhackme.com/room/digitalforensicsfundamentals)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.