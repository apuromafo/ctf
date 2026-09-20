# Brainstorm
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `brainstorm` |
| **Link** | [TryHackMe](https://tryhackme.com/room/brainstorm) |
| **Sección** | Reverse Engineering / Binary Analysis |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | Binary analysis, chat server exploitation, process identification, vulnerability research |
| **Impacto** | Enseña a analizar binarios de servidores de chat, identificar procesos en ejecución y explotar vulnerabilidades para obtener acceso y extraer flags. |
---
**Contexto:** Brainstorm es una sala de TryHackMe que presenta un servidor de chat vulnerable. El participante debe analizar el binario del servidor, identificar procesos relacionados y explotar vulnerabilidades para obtener las flags de cada task.
*EN: Brainstorm is a TryHackMe room presenting a vulnerable chat server. The participant must analyze the server binary, identify related processes, and exploit vulnerabilities to obtain the flags for each task.*
## Solucionario
### Task 1 — Reconnaissance
**Explicación:** Se realiza el reconocimiento inicial de la máquina: se identifican los servicios en ejecución y se obtiene información sobre la configuración de la sala.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Reconocimiento inicial. | `No answer needed` |
| 2 | ¿Cuántos servicios están abiertos? | `3` |
### Task 2 — Binary Analysis
**Explicación:** Se analiza el binario del servidor de chat para identificar su nombre y comportamiento. Se localiza el proceso principal en ejecución.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the process? | `chatserver.exe` |
### Task 3 — Exploitation
**Explicación:** Se explota la vulnerabilidad del servidor de chat para obtener acceso al sistema. Mediante la explotación se obtienen las respuestas restantes incluyendo la flag MD5.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Explotación del servidor. | `No answer needed` |
| 2 | Explotación del servidor. | `No answer needed` |
| 3 | Explotación del servidor. | `No answer needed` |
| 4 | Explotación del servidor. | `No answer needed` |
| 5 | What is the flag? | `5b1001de5a44eca47eee71e7942a8f8a` |
---
**Metodología:** Reconocimiento de puertos → identificación del servidor de chat → análisis del binario → identificación de procesos → explotación de vulnerabilidad → obtención de flag.
**Learning chain:** escaneo → chatserver.exe → análisis binario → vulnerabilidad → explotación → flag.
**Lección:** *Los servidores de chat custom son superficies de ataque ricas: cada funcionalidad (mensajes, archivos, autenticación) es un punto potencial de explotación si el binario no valida correctamente las entradas.*
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1059.004 (Unix Shell), T1068 (Exploitation for Privilege Escalation).
**Fuente:** [TryHackMe - Brainstorm](https://tryhackme.com/room/brainstorm)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
