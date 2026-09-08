# Defensive Security Intro

| **Dificultad** | Easy |
| **Tipo** | Informativo (defensa) |
| **Slug** | `defensivesecurityintroezn39` |
| **Link** | [TryHackMe](https://tryhackme.com/room/defensivesecurityintroezn39) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Blue teaming / SOC / Incident response / WAF / Rate limiting |
| **Impacto** | Introducción a la seguridad defensiva: roles de un equipo azul, el Security Operations Center y un ejercicio práctico de detección y bloqueo de un ataque a un banco falso. |

---

**Contexto:** La sala explica en qué consiste la seguridad defensiva y presenta los perfiles que componen un equipo azul (análisis forense, respuesta a incidentes, etc.). Tras los conceptos del SOC, un ejercicio interactivo plantea un ataque de Web Content Scanner contra un banco falso: hay que bloquear la IP del atacante, aplicar rate limiting en la API y añadir una regla WAF para detener el patrón, obteniendo así la flag.

## Solucionario

### Task 1: Introducción a la seguridad defensiva

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la disciplina que se centra en defender los sistemas (blue teaming o red teaming)? | `Blue Teaming` |

### Task 2: Los perfiles de la defensa

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | De los perfiles descritos en el ejemplo de la sala, ¿quién es la persona encargada de la respuesta a incidentes? | `Aaliyah` |

### Task 3: Security Operations Center

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la abreviatura de Security Operations Center? | `SOC` |

### Task 4: Ejercicio práctico - Asegurando el banco falso

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Detecta el ataque, bloquea al atacante y aplica las medidas de protección. ¿Cuál es la flag? | `THM{FAKEBANK-SECURED}` |

---

**Metodología:** En la tarea de ejemplo se detecta un ataque de "Web Content Scanner" contra la entidad FAKEBANK. Las acciones defensivas aplicadas en orden son: bloquear la IP atacante `32.122.195.63` durante 72 horas, implementar rate limiting en los endpoints de la API y añadir una regla WAF que rechace ese patrón de peticiones. Completadas las tres medidas, el sistema queda asegurado y entrega la flag.

**Learning chain:** blue teaming → incident response → SOC → detección de ataques web → mitigación (bloqueo, rate limiting, WAF).

**MITRE ATT&CK:** T1595 (Active Scanning), T1071 (Application Layer Protocol), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Defensive Security Intro](https://tryhackme.com/room/defensivesecurityintroezn39)