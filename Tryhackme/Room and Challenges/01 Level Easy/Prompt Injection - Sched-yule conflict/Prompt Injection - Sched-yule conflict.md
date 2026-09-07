# Prompt Injection - Sched-yule conflict

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `promptinjection-aoc2025-sxUMnCkvLO` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/promptinjection-aoc2025-sxUMnCkvLO) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | prompt injection, LLM, calendar app |
| **Impacto** | Manipulating LLM-powered apps to restore deleted calendar entries |

---

**Contexto:** Un adversario ha borrado los eventos de SOC-mas de la aplicación de calendario impulsada por un LLM. Mediante inyección de prompts, debemos convencer al asistente de restaurar los eventos eliminados y recuperar el acceso al calendario de Navidad.

## Solucionario

### Task 1: Restoring SOC-mas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag provided when SOC-mas is restored in the calendar? | `THM{XMAS_IS_COMING__BACK}` |

---

**Metodología:** Se exploró la interfaz del calendario y se identificó el campo de interacción con el LLM. Se formuló un prompt injection para manipular al asistente y restaurar los eventos eliminados de SOC-mas, obteniendo el flag como confirmación.
**Learning chain:** LLM-powered app analysis → prompt crafting → instruction override → calendar event restoration → flag extraction
**MITRE ATT&CK:** N/A (defensive walkthrough)
**Fuente:** [TryHackMe - Prompt Injection - Sched-yule conflict](https://tryhackme.com/r/room/promptinjection-aoc2025-sxUMnCkvLO)
