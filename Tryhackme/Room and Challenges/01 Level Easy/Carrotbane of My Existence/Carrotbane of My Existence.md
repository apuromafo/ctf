# Carrotbane of My Existence

| **Dificultad** | Medium |
| **Tipo** | challenge |
| **Slug** | `sq3-aoc2025-bk3vvbcgiT` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/sq3-aoc2025-bk3vvbcgiT) |
| **Sección** | Advent of Cyber 2025 (Side Quest 3) |
| **Fuente** | THM |
| **Componentes** | AI email assistant, DNS MX/SMTP, Ollama, tickets |
| **Impacto** | Medio — explotación de asistente AI desplegado localmente para obtener acceso y levantar tickets fraudulentos |

---

**Contexto:** El Side Quest 3 presenta un escenario donde un asistente de IA para gestión de emails (basado en Ollama con el modelo sir-carrotbane) ha sido desplegado en un entorno Docker. El jugador debe enumerar la infraestructura DNS/SMTP, descubrir credenciales débiles, acceder al modelo de lenguaje, y explotar el sistema de tickets para obtener las flags. Se requiere resolución en vivo para algunas flags.

## Solucionario

### Task 1: Unlock

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Unlock key (Day 17) | *Requiere resolverse en vivo* |

### Task 2: Challenges

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of flag 1? | `THM{9cd687b330554bd807a717e62910e3d0}` |
| 2 | What is the value of flag 2? | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |
| 3 | What is the value of flag 3? | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |
| 4 | What is the value of flag 4? | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Session Intel conocido:**
- Admin password: `v3rys3cur3p@ssw0rd!`
- Modelo Ollama: `sir-carrotbane`
- Host Ollama: `172.17.0.1:11434`

---

**Metodología:** Enumeración DNS MX/SMTP del dominio → descubrimiento de host Ollama → conexión a la API del modelo `sir-carrotbane` → inyección de prompts para obtener credenciales → acceso a panel de tickets → generación de tickets fraudulentos → obtención de flags.
**Learning chain:** DNS enumeration → SMTP recon → Ollama API interaction → prompt injection → ticket fraud → flag extraction
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059.007 (JavaScript — LLM interaction), T1078 (Valid Accounts)
**Fuente:** [TryHackMe - Carrotbane of My Existence](https://tryhackme.com/r/room/sq3-aoc2025-bk3vvbcgiT)
