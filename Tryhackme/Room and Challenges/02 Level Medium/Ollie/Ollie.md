# Ollie

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | ollie | https://tryhackme.com/room/ollie | 02 Level Medium | TryHackMe | phpIPAM 1.4.5, SQL injection autenticada, cron jobs/timers, escalada de privilegios | Compromiso de la máquina: explotación de una SQLi autenticada en phpIPAM 1.4.5 para ganar una shell inicial y abuso de una tarea programada (binary feedme / timer) para escalar a root. |

---

**Contexto:** La sala **Ollie** es un reto CTF de dificultad media ambientado en torno a la mascota *Ollie el perro*. El vector inicial es una **instalación de phpIPAM 1.4.5** con una **inyección SQL autenticada** que permite exfiltrar datos y obtener una shell en el sistema. La escalada a root aprovecha un binario o tarea de mantenimiento con privilegios elevados gestionada mediante un **timer/cron** del sistema. La tarea de entrada lleva por título **ROOF ROOF** (guiño al ladrido de un perro) y las dos preguntas del reto son las flags de `user.txt` y `root.txt`.

> **ES:** CTF medio que explota una SQLi autenticada en phpIPAM 1.4.5 y escala a root abusando de una tarea programada del sistema.
> **EN:** A medium CTF exploiting an authenticated SQL injection in phpIPAM 1.4.5 and escalating to root by abusing a scheduled system task.

## Solucionario

### Task 1: ROOF ROOF / ROOF ROOF
**Explicación:** Entrada temática del reto (el ladrido de Ollie). Tras explotar la SQLi de phpIPAM para obtener una shell inicial, se accede al directorio del usuario y se lee la flag de `user.txt`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user.txt flag? / ¿Cuál es la flag de user.txt? | `THM{Ollie_boi_is_daH_Cut3st}` |

### Task 2: Root / Root Flag
**Explicación:** Se identifica una tarea programada ejecutada con privilegios elevados (binary procesado por el sistema mediante un timer). Modificando o abusando del binario/script involucrado se consigue ejecución como root y se lee la flag de `root.txt`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the root.txt flag? / ¿Cuál es la flag de root.txt? | `THM{Ollie_Luvs_Chicken_Fries}` |

### Tabla unificada de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (ROOF ROOF) What is the user.txt flag? / ¿Cuál es la flag de user.txt? | `THM{Ollie_boi_is_daH_Cut3st}` |
| 2 | (Root) What is the root.txt flag? / ¿Cuál es la flag de root.txt? | `THM{Ollie_Luvs_Chicken_Fries}` |

---

**Metodología:** Reconocimiento (puertos 80/443 con phpIPAM) → autenticación en la aplicación → detección y explotación de la SQLi (exfiltración de datos y escritura/lectura de archivos) → shell inicial como usuario → enumeración de tareas programadas (timer/cron) → abuso del binario con privilegios elevados → shell root → extracción de `user.txt` y `root.txt`.

**Learning chain:** phpIPAM 1.4.5 → SQLi autenticada → file read/write → shell inicial → enumeración de cron/timers → abuso de binario con privilegios → root.

**Lección:** *Las aplicaciones web con panel de login no son una frontera: una sola consulta inyectable en una app como phpIPAM puede escalar hasta la lectura de archivos del sistema y el control total del host.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application) · T1190.003 (Exploit via Alternative Channel) · T1053.003/005 (Scheduled Task/Job: Cron) · T1068 (Exploitation for Privilege Escalation) · T1505.003 (Web Shell).

**Fuente:** [TryHackMe - Ollie](https://tryhackme.com/room/ollie)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.