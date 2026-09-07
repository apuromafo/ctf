# The Great Disappearing Act

| **Dificultad** | Hard |
| **Tipo** | challenge |
| **Slug** | `sq1-aoc2025-FzPnrt2SAu` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/sq1-aoc2025-FzPnrt2SAu) |
| **Sección** | Advent of Cyber 2025 (Side Quest 1) |
| **Fuente** | THM |
| **Componentes** | escape room, SCADA, keypad, web |
| **Impacto** | Alto — cadena completa de control de infraestructura industrial |

---

**Contexto:** Se trata de una sala de escape virtual con temática SCADA dentro del evento Advent of Cyber 2025. El jugador debe resolver puzzles encadenados: descifrar un código PIN, manipular un panel SCADA, identificar credenciales ocultas y ejecutar scripts de verificación para conseguir las flags. Cada paso depende del anterior, simulando una cadena de compromiso en un entorno industrial.

## Solucionario

### Task 1: Unlock

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Unlock key (side quest key) | `now_you_see_me` |

### Task 2: Challenges

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | PIN keypad code | `115879` |
| 2 | SCADA UNLOCK_CODE | `739184627` |
| 3 | Discovered credentials | `guard.hopkins@hopsecasylum.com` / `Johnnyboy1982!` |
| 4 | What is the first flag? | `THM{h0pp1ing_m4d}` |
| 5 | What is the second flag? | `THM{Y0u_h4ve_b3en_j3stered_739138}` |
| 6 | What is the third flag? | `THM{p0p_go3s_THe_W3as3l}` |

### Task 3: Next Room

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Next-room invite code (from escape_check.sh) | `THM{There.is.no.EASTmas.without.Hopper}` |

---

**Metodología:** Puzzle secuencial estilo escape room: resolución de PIN de keypad → obtención de código SCADA → descubrimiento de credenciales vía enumeración → ejecución de flags por cada puzzle resuelto → verificación final con escape_check.sh para el código de invitación.
**Learning chain:** SCADA basics → keypad logic → credential discovery → flag extraction → shell scripting verification
**MITRE ATT&CK:** N/A (defensive/educational room)
**Fuente:** [TryHackMe - The Great Disappearing Act](https://tryhackme.com/r/room/sq1-aoc2025-FzPnrt2SAu)
