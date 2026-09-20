# Race Conditions Challenge

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Race Condition | raceconditionschallenge | https://tryhackme.com/room/raceconditionschallenge | 02 Level Medium | TryHackMe | Race conditions, TOCTOU, concurrencia, comprobaciones de seguridad | Bypass de comprobaciones de seguridad y explotación de condiciones de carrera |

> **Objeto:** Explotar condiciones de carrera (race conditions) en el sistema de ficheros y en comprobaciones de seguridad para obtener acceso no autorizado, superar las validaciones de forma concurrente y capturar las tres flags que acreditan el compromiso del desafío.

---

**Contexto:** La sala **Race Conditions Challenge** plantea un escenario práctico de explotación de condiciones de carrera. Una condición de carrera se produce cuando el resultado de la ejecución depende del orden o del momento en que se ejecutan los accesos al sistema (patrón **TOCTOU** - *Time of Check to Time of Use*). El desafío consiste en ganar la carrera entre una comprobación de seguridad y el uso posterior del recurso, logrando ejecutar operaciones o acceder a datos antes de que la validación tenga efecto. Las tres preguntas del laboratorio entregan una flag cada una y permiten validar el compromiso de forma incremental.

## Solucionario

### Task 1: Flags de la condición de carrera / Race condition flags
**Explicación:**

La resolución del desafío consiste en abusar de las condiciones de carrera presentes en el sistema: en primer lugar una condición de carrera sobre el sistema de ficheros (patrón TOCTOU) que gana la competición frente a la comprobación de seguridad, y en último término una carrera orientada a conseguir el beneficio económico flaggeado ("sweet money") de forma concurrente. Las tres respuestas corresponden a las flags de los tres objetivos del laboratorio:

1. `THM{R4c3_c0nd1710n5_1n_7h3_f1l35y573m}`
2. `THM{R4c1n6_f4573r_7h4n_y0ur_53cur17y_ch3ck5}`
3. `THM{R4c1n6_f0r_7h47_5w337_m0n3y_$$$$$}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la condición de carrera en el sistema de ficheros | `THM{R4c3_c0nd1710n5_1n_7h3_f1l35y573m}` |
| 2 | Flag de comprobaciones superadas por la carrera | `THM{R4c1n6_f4573r_7h4n_y0ur_53cur17y_ch3ck5}` |
| 3 | Flag del reto económico ("sweet money") | `THM{R4c1n6_f0r_7h47_5w337_m0n3y_$$$$$}` |

---

**Metodología:** Identificación de condiciones de carrera (TOCTOU y competición sobre comprobaciones de seguridad), lanzamiento concurrente de peticiones/procesos para ganar la carrera, escalado de la explotación hacia el objetivo económico y captura de las tres flags del laboratorio.

**Learning chain:** Reconocimiento de la superficie → análisis de tiempos de comprobación frente a uso → explotación de la condición de carrera → verificación del compromiso con las flags.

**Lección:** *Una validación de seguridad solo es segura si la comprobación y el uso del recurso se hacen de forma atómica; cualquier ventana TOCTOU puede ser explotada ganando la carrera.*

**MITRE ATT&CK:** T1059 Command and Scripting Interpreter · T1068 Exploitation for Privilege Escalation · TA0005 Defense Evasion.

**Fuente:** [TryHackMe - Race Conditions Challenge](https://tryhackme.com/room/raceconditionschallenge)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.