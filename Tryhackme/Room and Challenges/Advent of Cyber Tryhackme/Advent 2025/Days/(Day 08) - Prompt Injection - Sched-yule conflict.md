# Prompt Injection - Sched-yule conflict

| **Dificultad** | Easy | **Tipo** | CTF (Free Room) | **Slug** | `day08promptinjectionschedyuleconflict` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) | | **Sección** | Advent of Cyber Tryhackme | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | Prompt Injection / AI / LLM / Calendar / SOC-mas | | **Impacto** | Día 08 del AoC 2025: inyección de prompts contra un asistente/cronómetro de calendario para restaurar la SOC-mas |

---

**Contexto:** Día 08 del calendario Advent of Cyber 2025 ("Prompt Injection - Sched-yule conflict"). Reto de IA: la agenda del calendario (SOC-mas) ha sido saboteada y hay que usar inyección de prompts contra el asistente para recuperar los eventos y restaurar el calendario, obteniendo la flag final. Documento original bilingüe (ES/EN); se conservan apuntes y respuesta verbatim.

---

## Solucionario

### Día 08: Prompt Injection - Sched-yule conflict

**Explicación:** Apuntes del laboratorio (notas bilingües originales):

Prompt Injection – Sched-yule conflict

- La inyección de prompts consiste en introducir instrucciones maliciosas/alternativas dentro del sistema conversacional para alterar su comportamiento.
- Vector: asistente de calendario SOC-mas; se restaura el calendario siguiendo el guion del reto.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the flag provided when SOC-mas is restored in the calendar? | `THM{XMAS_IS_COMING__BACK}` |

---

**Metodología:**

1. Interactuar con el asistente del calendario (chat/agenda)

2. Practicar inyección de prompts para alterar/reparar el comportamiento del LLM

3. Restaurar la SOC-mas en el calendario y leer la flag

**Learning chain:** AI assistant -> Prompt injection -> Flag (restored calendar)

**Lección:** *La inyección de prompts es una amenaza real de la IA conversacional: si un asistente procesa texto no confiable (agenda, entradas del usuario), un atacante puede manipular su comportamiento; validar y sanear las entradas es crítico.*

**MITRE ATT&CK:**

- T1059 - Command and Scripting Interpreter (manipulación de la sesión)

- T1190 - Exploit Public-Facing Application (vector web del asistente)

- T1566 - Phishing (contexto de ingeniería social en la demo)

**Fuente:** [TryHackMe - Prompt Injection - Sched-yule conflict](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.