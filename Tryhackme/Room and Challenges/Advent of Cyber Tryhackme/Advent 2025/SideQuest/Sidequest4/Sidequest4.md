# BreachBlocker Unlocker

| **Dificultad** | HARD | **Tipo** | CTF (Free Room) | **Slug** | sq4-aoc2025-32LoZ4zePK | | **Link** | [TryHackMe](https://tryhackme.com/room/sq4-aoc2025-32LoZ4zePK) | | **Seccion** | Advent of Cyber Tryhackme / Advent 2025 Side Quest 4 | | **Fuente** | walkthrough propio + [jaxafed](https://jaxafed.github.io/posts/tryhackme-aoc2025_sidequest_four/) + [id-root](https://github.com/id-root/BreachBlocker-Unlocker) + [djalilayed](https://github.com/djalilayed/tryhackme/tree/main/Advent_of_Cyber_Side_Quest_2025/BreachBlocker_Unlocker) | | **Componentes** | web / fuzzing / reverse-engineering / python / timing-attack / side-channel / smtp / email-parsing | | **Impacto** | Hopper necesita la llave final de la sala del trono; reto avanzado multitecnica |

---

**Contexto:** Cuarto Side Quest del Advent of Cyber 2025. Hopper necesita tu ayuda para obtener la llave final de la sala del trono. Este reto requiere habilidades avanzadas en web, fuzzing, reverse engineering, Python, timing attacks, side-channel analysis, SMTP y email parsing.

**Egg Decode Password:** 	hrone123*`r

---

## Solucionario

### Task 1: CODE_FLAG

**Explicacion:** Reverse engineering del codigo fuente del BreachBlocker para encontrar la flag oculta en el codigo. Se accedio al source code y se exploto la logica del bloqueador.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What's the CODE_FLAG? | THM{eggsposed_source_code} |

### Task 2: HOPFLIX_FLAG

**Explicacion:** Analisis de la plataforma Hopflix dentro del reto, involucrando timing-attack y side-channel para obtener la contrasena de la temporada 4.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 2 | What's the HOPFLIX_FLAG? | THM{fluffier_things_season_4} |

### Task 3: BANK_FLAG

**Explicacion:** Explotacion de vulnerabilidades en el sistema bancario del trono para obtener la balance negativa (neggative).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 3 | What's the BANK_FLAG? | THM{neggative_balance} |

---

**Metodologia:**

1. Egg Decode con password 	hrone123*`r

2. Fuzzing del endpoint de codigo

3. Reverse engineering del source code

4. Timing attack / side channel en Hopflix

5. SMTP / email parsing para Bank

6. Compilacion de las 3 flags

**Learning chain:** Egg Decode -> Web Fuzzing -> Reverse Engineering -> Timing Attack -> Side Channel -> SMTP -> Email Parsing -> 3 Flags

**Leccion:** *Los retos de HARD requieren combinar multiples tecnicas de seguridad ofensiva; el source code exposure es una vulnerabilidad critica que puede comprometer todo el sistema.*

**MITRE ATT&CK:**

- T1027 - Obfuscated Files or Information

- T1190 - Exploit Public-Facing Application

- T1592 - Gather Victim Host Information

**Fuente:** [TryHackMe - BreachBlocker Unlocker](https://tryhackme.com/room/sq4-aoc2025-32LoZ4zePK)