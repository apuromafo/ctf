# Breakme
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `breakme` |
| **Link** | [TryHackMe](https://tryhackme.com/room/breakme) |
| **Sección** | Web Exploitation / Reverse Engineering |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | Web exploitation, binary analysis, file forensics, hash extraction |
| **Impacto** | Enseña a combinar explotación web con análisis de binarios y forensics de archivos para obtener múltiples flags en un entorno de reto. |
---
**Contexto:** Breakme es una sala de TryHackMe que combina explotación web, análisis de binarios y forensics de archivos. El participante debe resolver múltiples retos encadenados para obtener las tres flags, cada una en una fase diferente del ataque.
*EN: Breakme is a TryHackMe room combining web exploitation, binary analysis, and file forensics. The participant must solve multiple chained challenges to obtain the three flags, each in a different attack phase.*
## Solucionario
### Task 1 — Multi-stage Exploitation
**Explicación:** Se completa el reto en múltiples fases: explotación de la aplicación web, análisis de artefactos y obtención de las tres flags correspondientes a cada etapa del ataque.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first flag? | `5c3ea0d312568c7ac68d213785b26677` |
| 2 | What is the second flag? | `df5b1b7f4f74a416ae27673b22633c1b` |
| 3 | What is the third flag? | `e257d58481412f8772e9fb9fd47d8ca4` |
---
**Metodología:** Reconocimiento de la aplicación → explotación de vulnerabilidades web → análisis de binarios o archivos → extracción de artefactos → obtención de las tres flags en secuencia.
**Learning chain:** app web → vulnerabilidad → explotación → binario/archivo → análisis → flags múltiples.
**Lección:** *Los retos encadenados exigen combinar disciplinas: lo que no resuelve la web lo resuelve el reversing, y viceversa.*
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1027 (Obfuscated Files or Information), T1083 (File and Directory Discovery).
**Fuente:** [TryHackMe - Breakme](https://tryhackme.com/room/breakme)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
