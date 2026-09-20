# The Great Disappearing Act

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|--------------|---------|
| Hard | challenge | `sq1-aoc2025-FzPnrt2SAu` | [TryHackMe](https://tryhackme.com/r/room/sq1-aoc2025-FzPnrt2SAu) | Advent of Cyber 2025 (Side Quest 1) | THM | escape room, SCADA, keypad, web | Alto — cadena completa de control de infraestructura industrial |

---

**Contexto:**

> **ES:** Se trata de una sala de escape virtual con temática SCADA dentro del evento Advent of Cyber 2025. El jugador debe resolver puzzles encadenados: descifrar un código PIN, manipular un panel SCADA, identificar credenciales ocultas y ejecutar scripts de verificación para conseguir las flags. Cada paso depende del anterior, simulando una cadena de compromiso en un entorno industrial.
> **EN:** This is a SCADA-themed virtual escape room within the Advent of Cyber 2025 event. The player must solve chained puzzles: decipher a PIN code, manipulate a SCADA panel, identify hidden credentials and run verification scripts to get the flags. Each step depends on the previous one, simulating a compromise chain in an industrial environment.

## Solucionario

### Task 1: Unlock

**Explicación:**

La primera tarea consiste en desbloquear el acceso al entorno de la sala de escape. Las respuestas del room se conservan de forma literal:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Unlock key (side quest key) | `now_you_see_me` |

### Task 2: Challenges

**Explicación:**

En esta tarea se resuelven los puzzles encadenados: PIN del keypad, código del panel SCADA, credenciales descubiertas y las tres flags de la cadena. Las respuestas del room se conservan de forma literal:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | PIN keypad code | `115879` |
| 2 | SCADA UNLOCK_CODE | `739184627` |
| 3 | Discovered credentials | `guard.hopkins@hopsecasylum.com` / `Johnnyboy1982!` |
| 4 | What is the first flag? | `THM{h0pp1ing_m4d}` |
| 5 | What is the second flag? | `THM{Y0u_h4ve_b3en_j3stered_739138}` |
| 6 | What is the third flag? | `THM{p0p_go3s_THe_W3as3l}` |

### Task 3: Next Room

**Explicación:**

La tarea final verifica el estado de la cadena mediante un script y entrega el código de invitación a la siguiente sala. Las respuestas del room se conservan de forma literal:

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Next-room invite code (from escape_check.sh) | `THM{There.is.no.EASTmas.without.Hopper}` |

### Tabla Unificada de Preguntas y Respuestas

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 - Unlock | Unlock key (side quest key) | `now_you_see_me` |
| 2 | Task 2 - Challenges | PIN keypad code | `115879` |
| 3 | Task 2 - Challenges | SCADA UNLOCK_CODE | `739184627` |
| 4 | Task 2 - Challenges | Discovered credentials | `guard.hopkins@hopsecasylum.com` / `Johnnyboy1982!` |
| 5 | Task 2 - Challenges | What is the first flag? | `THM{h0pp1ing_m4d}` |
| 6 | Task 2 - Challenges | What is the second flag? | `THM{Y0u_h4ve_b3en_j3stered_739138}` |
| 7 | Task 2 - Challenges | What is the third flag? | `THM{p0p_go3s_THe_W3as3l}` |
| 8 | Task 3 - Next Room | Next-room invite code (from escape_check.sh) | `THM{There.is.no.EASTmas.without.Hopper}` |

---

**Metodología:** Puzzle secuencial estilo escape room: resolución de PIN de keypad → obtención de código SCADA → descubrimiento de credenciales vía enumeración → ejecución de flags por cada puzzle resuelto → verificación final con escape_check.sh para el código de invitación.

### Cadena de ataque / Attack Chain

- Primer acceso con la unlock key (side quest key)
- Descifrado del PIN del keypad
- Compromiso del panel SCADA mediante el UNLOCK_CODE
- Enumeración de credenciales (guard.hopkins@hopsecasylum.com / Johnnyboy1982!)
- Ejecución de flags por cada puzzle de la cadena
- Verificación con escape_check.sh → código de invitación a la siguiente sala

**Learning chain:** SCADA basics → keypad logic → credential discovery → flag extraction → shell scripting verification

**Lección:** *Los entornos industriales ocultan cadenas de compromiso: cada credencial y cada código verifican el paso anterior, y la automatización con scripts de verificación consolida el resultado de la escalada.*

**MITRE ATT&CK:** N/A (defensive/educational room)

**Fuente:** [TryHackMe - The Great Disappearing Act](https://tryhackme.com/r/room/sq1-aoc2025-FzPnrt2SAu)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.