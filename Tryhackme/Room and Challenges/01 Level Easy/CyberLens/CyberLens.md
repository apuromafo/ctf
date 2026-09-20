# CyberLens

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `cyberlens` | [TryHackMe](https://tryhackme.com/room/cyberlens) | 01 Level Easy | THM | Esteganografía, Análisis de imagen, OCR, Escalada | Extracción de flags mediante análisis de imágenes |

> **Objeto:** Analizar imágenes con la herramienta CyberLens para descubrir los textos ocultos y obtener los flags de la sala.

---

**Contexto:** Sala práctica centrada en el análisis forense de imágenes: extraer el texto visible en capturas, aplicar técnicas de mejora de imagen y reconocimiento (OCR) para revelar los flags ocultos o difíciles de leer.

> **ES:** La tarea consiste en usar la vista de CyberLens para leer los textos incrustados en capturas y validar los flags.
> **EN:** The task consists of using the CyberLens view to read the texts embedded in the screenshots and validate the flags.

## Solucionario

### Task 1: Desafío / Challenge
**Explicación:** Se examinan las imágenes facilitadas por la sala para localizar los flags visibles u ocultos.

1. THM{T1k4-CV3-f0r-7h3-w1n}
2. THM{3lev@t3D-4-pr1v35c!}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1.1 | Primer flag | `THM{T1k4-CV3-f0r-7h3-w1n}` |
| 1.2 | Segundo flag | `THM{3lev@t3D-4-pr1v35c!}` |

---

**Metodología:** Visualización de las imágenes de laboratorio, inspección visual y ampliación de las capturas, lectura de los textos incrustados y validación de cada flag.

### Cadena de ataque / Attack Chain

Captura → inspección visual → lectura del texto oculto → validación del flag.

**Learning chain:** imagen → análisis visual → OCR → flag

*Lección:* Las imágenes pueden contener información sensible visible u oculta que debe revisarse con detalle en cualquier investigación.

**MITRE ATT&CK:** N/A.

**Fuente:** [TryHackMe - CyberLens](https://tryhackme.com/room/cyberlens)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.