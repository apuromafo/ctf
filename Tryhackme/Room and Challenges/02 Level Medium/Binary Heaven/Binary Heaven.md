# Binary Heaven
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `binaryheaven` |
| **Link** | [TryHackMe](https://tryhackme.com/room/binaryheaven) |
| **Sección** | Reverse Engineering / Binary Exploitation |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | Reverse engineering, binary analysis, privilege escalation, root access |
| **Impacto** | Desarrolla habilidades de ingeniería inversa sobre binarios, escalada de privilegios y obtención de root en un entorno controlado. |
---
**Contexto:** Binary Heaven es un reto de TryHackMe que combina ingeniería inversa y explotación de binarios. El participante debe analizar ejecutables, identificar vulnerabilidades y escalar privilegios hasta obtener root en la máquina objetivo. La sala pone a prueba el manejo de herramientas de análisis estático y dinámico.
*EN: Binary Heaven is a TryHackMe challenge combining reverse engineering and binary exploitation. The participant must analyze executables, identify vulnerabilities, and escalate privileges to root on the target machine. The room tests proficiency with static and dynamic analysis tools.*
## Solucionario
### Task 1 — Intro
**Explicación:** Introducción a la sala. Se presenta el entorno y los objetivos del reto. Tarea informativa sin respuesta requerida.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a la sala. | `No answer needed` |
### Task 2 — Binary Analysis
**Explicación:** Se analiza el binario para identificar el guardian (usuario) y su contraseña que protegen el acceso. Mediante ingeniería inversa (strings, análisis estático o dinámico) se extraen las credenciales y la flag del reto.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the username of the guardian? | `guardian` |
| 2 | What is the password of the guardian? | `GOg0esGrrr!` |
| 3 | What is the flag you get after bypassing the guardian? | `THM{crack3d_th3_gu4rd1an}` |
### Task 3 — Privilege Escalation
**Explicación:** Tras obtener acceso inicial, se explota una vulnerabilidad en el binario para escalar privilegios y obtener una shell de usuario elevado, revelando la segunda flag.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag you get after exploiting the binary? | `THM{b1n3xg0d_pwn3d}` |
### Task 4 — Root Access
**Explicación:** Se completa la escalada de privilegios hasta llegar a root, obteniendo la flag final del reto.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the root flag? | `THM{r00t_of_th3_he4v3n}` |
### Task 5 — Outro
**Explicación:** Cierre de la sala. Se invita a reflexionar sobre las técnicas aprendidas. Tarea de cierre sin respuesta requerida.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cierre de la sala. | `No answer needed` |
---
**Metodología:** Reconocimiento del binario → análisis estático (strings, objdump, gdb) → extracción de credenciales → explotación de vulnerabilidad → escalada de privilegios → obtención de root.
**Learning chain:** binario protegido → ingeniería inversa → bypass de guardian → explotación → root shell → flag final.
**Lección:** *Los binarios protegidos por credenciales hardcoded son triviales de vencer con análisis estático; la verdadera seguridad no depende de ocultar contraseñas en el código.*
**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1059.004 (Unix Shell), T1548.001 (Setuid and Setgid), T1068 (Exploitation for Privilege Escalation).
**Fuente:** [TryHackMe - Binary Heaven](https://tryhackme.com/room/binaryheaven)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
