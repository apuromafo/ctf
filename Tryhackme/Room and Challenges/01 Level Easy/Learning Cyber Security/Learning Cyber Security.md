# Learning Cyber Security

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `learningcybersecurity` | [TryHackMe](https://tryhackme.com/room/learningcybersecurity) | 01 Level Easy | TryHackMe | Ataques cibernéticos, fuerza bruta, conceptos de seguridad | Aprender los conceptos básicos de ciberseguridad y cómo se ejecutan los ataques reales (fuerza bruta, phishing). |

---

**Contexto:** La sala "Learning Cyber Security" enseña los fundamentos del hacking ético y de la ciberseguridad. Durante el desarrollo se explora un ataque de fuerza bruta contra una máquina vulnerable, se obtienen credenciales con el usuario `Ben.Spring` y se recupera la flag `THM{BRUTEFORCING}`. Además se habla del impacto económico de los ciberataques (pérdida de 300 millones de dólares) y se recuerda qué son los equipos ofensivos y defensivos.

> **ES:** Guía de introducción a la ciberseguridad: concepto de hacking, fuerza bruta contra un objetivo, credenciales de `Ben.Spring`, flag `THM{BRUTEFORCING}`, impacto económico ($300 million) y qué es un hacker.
> **EN:** Intro to cybersecurity guide: hacking concept, brute-forcing a vulnerable machine, `Ben.Spring` credentials, `THM{BRUTEFORCING}` flag, economic impact ($300 million) and what a hacker is.

## Solucionario

### Task 1: Fuerza bruta / Brute force
**Explicación:** En esta tarea se observa un ataque de fuerza bruta en acción. La primera pregunta no requiere respuesta, se identifica el nombre de usuario (`Ben.Spring`) y se obtiene la flag tras un ataque de fuerza bruta (`THM{BRUTEFORCING}`).

```text
1. 1. No answer needed
   2. Ben.Spring
   3. THM{BRUTEFORCING}
```

### Task 2: Impacto / Impact
**Explicación:** Se cuantifica el impacto de un ciberataque real. La primera pregunta no requiere respuesta y la segunda responde con la cifra de 300 millones de dólares.

```text
2. 1. No answer needed
   2. $300 million
```

### Task 3: Concepto de hacker / What is a hacker
**Explicación:** Explicación de qué es un hacker (ofensivo o defensivo). No requiere respuesta.

```text
3. No answer needed
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Introducción a la tarea | `No answer needed` |
| 1 | Nombre de usuario obtenido | `Ben.Spring` |
| 1 | Flag del ataque de fuerza bruta | `THM{BRUTEFORCING}` |
| 2 | Introducción al impacto | `No answer needed` |
| 2 | Pérdida económica causada | `$300 million` |
| 3 | Concepto de hacker | `No answer needed` |

---

**Metodología:** Tras leer la teoría de los conceptos de seguridad, se reprodujo un ataque de fuerza bruta contra una máquina vulnerable para descubrir credenciales del usuario `Ben.Spring` y capturar la flag. Se comparó el impacto real de un ataque ($300 millions) y se cerró explicando el rol de los hackers.

### Cadena de ataque / Attack Chain

```text
Aprendizaje de conceptos -> objetivo vulnerable -> fuerza bruta de credenciales -> acceso -> flag THM{BRUTEFORCING} -> impacto económico ($300 million) -> conclusión
```

**Learning chain:** intro to security -> brute force -> credential harvesting -> flag -> business impact

**Lección:** *La fuerza bruta sigue siendo un vector de entrada efectivo cuando las contraseñas son débiles; conocer su funcionamiento es clave tanto para atacar como para defender los accesos de una organización.*

**MITRE ATT&CK:** T1110 (Brute Force), T1110.001 (Password Guessing), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Learning Cyber Security](https://tryhackme.com/room/learningcybersecurity)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.