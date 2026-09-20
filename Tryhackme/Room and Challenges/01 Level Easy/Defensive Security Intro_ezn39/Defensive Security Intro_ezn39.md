# Defensive Security Intro

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `defensivesecurityintroezn39` | [TryHackMe](https://tryhackme.com/r/room/defensivesecurityintroezn39) | Cyber Defense | THM | Network analysis, Firewall rules, Static-site | Fundamentos defensivos |

> **Objeto:** Introducirse en la seguridad defensiva como blue team: detectar tráfico sospechoso, identificar el ataque y bloquearlo mediante reglas de firewall en un laboratorio con la web FakeBank.

---

**Contexto:** Introducción a la seguridad defensiva: objetivos del blue team, análisis de tráfico de red, identificación de IPs maliciosas y bloqueo con reglas de firewall. Laboratorio práctico con sitio web FakeBank.

> **ES:** Introducción a la seguridad defensiva: objetivos del blue team, análisis de tráfico de red, identificación de IPs maliciosas y bloqueo con reglas de firewall. Laboratorio práctico con sitio web FakeBank.
> **EN:** Introduction to defensive security: blue team objectives, network traffic analysis, identification of malicious IPs and blocking with firewall rules. Hands-on lab with the FakeBank website.

## Solucionario

### Task 1: Think like a Defender / Piensa como un defensor
**Explicación:** Se repasa en qué consiste la seguridad defensiva y cuál es el objetivo principal del blue team.

¿Cuál es el objetivo principal de la seguridad defensiva?

| Pregunta | Respuesta |
|----------|-----------|
| ¿Cuál es el objetivo principal de la seguridad defensiva? | `Detect and respond to attacks` |

### Task 2: Detect Suspicious Activity / Detecta actividad sospechosa
**Explicación:** Se analiza el tráfico de red del analizador para detectar la actividad anómala y extraer la IP fuente del tráfico sospechoso.

Dirección IP fuente del tráfico sospechoso

| Pregunta | Respuesta |
|----------|-----------|
| Dirección IP fuente del tráfico sospechoso | `32.122.195.63` |

### Task 3: Identify the Attack / Identifica el ataque
**Explicación:** Se correlacionan los requests HTTP del analizador para identificar el objetivo del atacante.

URL más reciente que el atacante intentó encontrar

| Pregunta | Respuesta |
|----------|-----------|
| URL más reciente que el atacante intentó encontrar | `https://fakebank.com/admin` |

### Task 4: Stop the Attack / Detén el ataque
**Explicación:** Se aplica la regla de firewall para bloquear al atacante y se verifica la contención con el flag.

Copiar el flag tras bloquear el ataque

| Pregunta | Respuesta |
|----------|-----------|
| Copiar el flag tras bloquear el ataque | `THM{FAKEBANK-SECURED}` |

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | ¿Cuál es el objetivo principal de la seguridad defensiva? | `Detect and respond to attacks` |
| 2 | Dirección IP fuente del tráfico sospechoso | `32.122.195.63` |
| 3 | URL más reciente que el atacante intentó encontrar | `https://fakebank.com/admin` |
| 4 | Copiar el flag tras bloquear el ataque | `THM{FAKEBANK-SECURED}` |

---

**Metodología:** Identificar tráfico anómalo en el analizador → extraer la IP origen → rastrear las URLs consultadas → bloquear con regla de firewall → obtener el flag de confirmación.

### Cadena de ataque / Attack Chain

Análisis de tráfico del analizador → detección de la IP sospechosa → correlación de URLs consultadas → bloqueo con firewall → verificación del flag.

**Learning chain:** Detección de anomalías → análisis de IPs → correlación de requests HTTP → contención mediante firewall → verificación.

*Lección:* El blue team debe detectar, correlacionar y contener rápidamente el tráfico malicioso antes de que el atacante progrese.

**MITRE ATT&CK:** TA0001 Initial Access, TA0005 Defense Evasion, TA0009 Collection.

**Fuente:** [TryHackMe - Defensive Security Intro](https://tryhackme.com/room/defensivesecurityintroezn39)

> **Fuente original / Original source:** https://github.com/Cajac/TryHackMe-Writeups/blob/main/Walkthroughs/Info/Defensive_Security_Intro.md

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.