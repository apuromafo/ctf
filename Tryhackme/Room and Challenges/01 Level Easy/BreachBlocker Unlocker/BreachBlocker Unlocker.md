# BreachBlocker Unlocker

| **Dificultad** | Hard |
| **Tipo** | challenge |
| **Slug** | `sq4-aoc2025-32LoZ4zePK` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/sq4-aoc2025-32LoZ4zePK) |
| **Sección** | Advent of Cyber 2025 (Side Quest 4) |
| **Fuente** | THM |
| **Componentes** | mobile app, timing attack, OTP bypass, SMTP |
| **Impacto** — Alto — bypass de autenticación móvil mediante timing attack y reintento OTP, con potencial de acceso a código fuente, servicios de streaming y banca |

---

**Contexto:** El Side Quest 4 plantea el análisis de una aplicación móvil de seguridad llamada BreachBlocker. El jugador debe encontrar la clave de desbloqueo, extraer código fuente de la app para descubrir vulnerabilidades, ejecutar un timing attack contra el mecanismo OTP, y finalmente explotar el bypass para obtener las flags de los distintos servicios (código, HopFlix y banco).

## Solucionario

### Task 1: Unlock

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Unlock key (from Day 21 HTA) | `throne123*` |

### Task 2: Challenges

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the CODE_FLAG? | `THM{eggsposed_source_code}` |
| 2 | What's the HOPFLIX_FLAG? | `THM{fluffier_things_season_4}` |
| 3 | What's the BANK_FLAG? | `THM{neggative_balance}` |

---

**Metodología:** Obtención de clave HTA del Day 21 → extracción y análisis de código fuente de la app móvil → identificación de endpoint OTP vulnerable a timing attack → explotación del bypass de verificación OTP → acceso progresivo a servicios (código → HopFlix → banco) → extracción de flags en cada servicio.
**Learning chain:** HTA extraction → mobile APK decompilation → source code review → timing attack → OTP bypass → multi-service flag hunting
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1040 (Network Sniffing — timing side-channel), T1078 (Valid Accounts)
**Fuente:** [TryHackMe - BreachBlocker Unlocker](https://tryhackme.com/r/room/sq4-aoc2025-32LoZ4zePK)
