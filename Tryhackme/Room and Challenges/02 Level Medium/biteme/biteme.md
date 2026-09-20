# biteme
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `biteme` |
| **Link** | [TryHackMe](https://tryhackme.com/room/biteme) |
| **Sección** | Web Exploitation / Forensics |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | Web exploitation, forensics, file analysis, flag extraction |
| **Impacto** | Enseña a analizar archivos sospechosos, extraer artefactos forenses y explotar vulnerabilidades web para obtener flags. |
---
**Contexto:** biteme es una sala de TryHackMe que combina forensics y explotación web. El participante debe analizar archivos y extraer información oculta para resolver los retos y obtener las flags de cada task.
*EN: biteme is a TryHackMe room combining forensics and web exploitation. The participant must analyze files and extract hidden information to solve the challenges and obtain the flags for each task.*
## Solucionario
### Task 1 — Forensics Analysis
**Explicación:** Se analizan archivos proporcionados por la sala para extraer artefactos forenses. Mediante herramientas de análisis (strings, hexdump, file type analysis) se identifican y recuperan dos flags ocultas en los archivos.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first flag? | `THM{6fbf1fb7241dac060cd3abba70c33070}` |
| 2 | What is the second flag? | `THM{0e355b5c907ef7741f40f4a41cc6678d}` |
---
**Metodología:** Descarga de archivos → análisis de tipo (`file`) → extracción de cadenas (`strings`) → inspección hex → recuperación de flags ocultas en metadatos o contenido embebido.
**Learning chain:** archivos sospechosos → análisis estático → extracción de artefactos → flags forenses.
**Lección:** *Los archivos pueden contener datos ocultos en metadatos, capas no visibles o embebidos en estructuras que solo revela un análisis exhaustivo con herramientas adecuadas.*
**MITRE ATT&CK:** T1005 (Data from Local System), T1083 (File and Directory Discovery), T1027 (Obfuscated Files or Information).
**Fuente:** [TryHackMe - biteme](https://tryhackme.com/room/biteme)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
