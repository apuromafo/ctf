# Intro to SSRF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introtossrf` | [TryHackMe](https://tryhackme.com/room/introtossrf) | 01 Level Easy | TryHackMe | SSRF, Server-Side Request Forgery, Blind, AWS Metadata, Open Redirect, Allow List, Deny List | Fundamentos de Server-Side Request Forgery: definición, tipos, metadata cloud, bypass de defensas y práctica con flags |

> **Objeto:** Comprender qué es un Server-Side Request Forgery (SSRF): su significado, el tipo ciego, ejemplos de ataque, detección de URLs vulnerables, bypass de defensas comunes (Open Redirect, Allow List, Deny List), el abuso de la IP de metadata (169.254.169.254) y la práctica final con flags.

---

**Contexto:** Sala que enseña el SSRF desde cero: qué significa, el tipo ciego (Blind) frente al regular, ejemplos prácticos en un sitio web con flag (SSRF Examples), cómo detectar por simple observación qué URLs son más vulnerables, cómo vencer las defensas (Open Redirect, Allow List y Deny List, metadata de cloud en 169.254.169.254) y un ejercicio práctico final donde se explota /private mediante el parámetro de avatar y directory traversal.

> **ES:** Sala de introducción al SSRF: definición, tipos, ejemplos, detección, defensas (allow/deny list, open redirect), metadata de cloud y práctica con flags.
> **EN:** Introduction to SSRF room: definition, types, examples, detection, defenses (allow/deny lists, open redirect), cloud metadata and practical flags.

## Solucionario

### Task 1: ¿Qué es el SSRF? / What is SSRF?
**Explicación:** Se define Server-Side Request Forgery (SSRF) y se aprende el otro tipo de SSRF, el ciego (Blind), frente al SSRF regular.

1. Server-Side Request Forgery
2. Blind

### Task 2: Ejemplos de SSRF / SSRF Examples
**Explicación:** Se explota un sitio web de ejemplo modificando un parámetro susceptible de SSRF y se captura la flag de la página.

THM{SSRF_MASTER}

### Task 3: Encontrando un SSRF / Finding an SSRF
**Explicación:** Por simple observación de las URLs, se identifica cuál de ellas es más probablemente vulnerable a SSRF (la que controla un parámetro de fichero y servidor).

3

### Task 4: Venciendo las defensas comunes / Defeating Common SSRF Defenses
**Explicación:** Se aprenden las defensas de SSRF y cómo vencerlas: el Open Redirect para saltarse reglas estrictas, la IP de metadata (169.254.169.254) que contiene datos sensibles en la nube, la Allow List para permitir solo ciertas entradas y la Deny List para bloquear ciertas entradas.

1. Open Redirect
2. 169.254.169.254
3. Allow List
4. Deny List

### Task 5: Práctica de SSRF / SSRF Practical
**Explicación:** Ejercicio práctico: se explota el parámetro de avatar del sitio con encoding Base64 y directory traversal para acceder al directorio /private y obtener la flag.

THM{YOU_WORKED_OUT_THE_SSRF}

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1.1 | ¿Qué significa SSRF? | `Server-Side Request Forgery` |
| 1.2 | A diferencia del SSRF regular, ¿cuál es el otro tipo? | `Blind` |
| 2.1 | Flag del sitio de ejemplos de SSRF | `THM{SSRF_MASTER}` |
| 3.1 | Por simple observación, ¿cuál de las URLs es más probable que sea vulnerable a SSRF? | `3` |
| 4.1 | ¿Qué método se puede usar para saltarse reglas estrictas? | `Open Redirect` |
| 4.2 | ¿Qué IP puede contener datos sensibles en un entorno cloud? | `169.254.169.254` |
| 4.3 | ¿Qué tipo de lista se usa para permitir solo ciertas entradas? | `Allow List` |
| 4.4 | ¿Qué tipo de lista se usa para bloquear ciertas entradas? | `Deny List` |
| 5.1 | Flag del directorio /private | `THM{YOU_WORKED_OUT_THE_SSRF}` |

---

**Metodología:** Definición conceptual del SSRF y sus tipos, explotación de un sitio de ejemplos mediante el parámetro vulnerable, identificación por observación de URLs candidatas a SSRF, revisión de las defensas comunes (open redirect, allow/deny list, metadata de cloud) y explotación práctica del parámetro de avatar con Base64 y directory traversal hasta obtener la flag del directorio /private.

### Cadena de ataque / Attack Chain

Parámetro vulnerable -> SSRF -> Blind/non-blind -> modificación de URL -> flag (SSRF Examples) -> detección por observación -> defensas (open redirect, allow/deny list) -> metadata 169.254.169.254 -> explotación de avatar (Base64 + traversal) -> flag /private

**Learning chain:** SSRF -> server-side request forgery -> blind SSRF -> detection -> open redirect -> allow/deny lists -> cloud metadata -> practical exploitation

**Lección:** *Un único parámetro que controla una petición del servidor puede convertirse en un SSRF capaz de acceder a metadata interna de la nube; conocer las defensas allow/deny y sus bypasses es esencial para explotarlo y mitigarlo.*

**MITRE ATT&CK:** T1552.005 (Unsecured Credentials: Cloud Instance Metadata API) / T1190 (Exploit Public-Facing Application).

**Fuente:** [TryHackMe - Intro to SSRF](https://tryhackme.com/room/introtossrf)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.