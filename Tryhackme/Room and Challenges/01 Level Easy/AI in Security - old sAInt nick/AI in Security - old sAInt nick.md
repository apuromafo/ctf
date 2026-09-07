# AI in Security - old sAInt nick

| **Dificultad** | Easy |
| **Tipo** | challenge |
| **Slug** | `AIforcyber-aoc2025-y9wWQ1zRgB` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/AIforcyber-aoc2025-y9wWQ1zRgB) |
| **Sección** | Advent of Cyber 2025 |
| **Fuente** | THM |
| **Componentes** | AI security, LLM agents, SQLi exploit |
| **Impacto** | Todas las preguntas resueltas, Writeup completo |

---

**Contexto:** Durante el Advent of Cyber 2025 (Día 4), Santa despliega un "AI Showcase" donde un agente de IA de red team automatiza el análisis de aplicaciones web vulnerables. El reto combina una demo interactiva del agente con un exploit real de SQL injection entregado por el propio agente. El objetivo es completar la showcase para obtener la bandera de validación y posteriormente ejecutar el payload proporcionado para demostrar el impacto real en el host `MACHINE_IP:5000`.

## Solucionario

### Task 1: AI Showcase

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the AI showcase by progressing through all of the stages. What is the flag presented to you? | `THM{AI_MANIA}` |

### Task 2: Exploiting the Vulnerable Application

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Execute the exploit provided by the red team agent against the vulnerable web application hosted at MACHINE_IP:5000. What flag is provided in the script's output after it? | `THM{SQLI_EXPLOIT}` |

---

**Metodología:** El flujo empieza en la demo del agente de IA (red team), donde avanzamos por los distintos stages del showcase hasta que el agente entrega el payload de SQLi. Completar todos los pasos de la showcase otorga la primera bandera. Luego tomamos el script de exploit generado por el agente y lo ejecutamos contra la app vulnerable en el puerto 5000; la salida del script revela la segunda bandera, demostrando que la IA fue capaz de identificar y explotar una inyección SQL de forma autónoma.

**Learning chain:** AI agents de red team → automatización de recon → generación de exploits → SQL injection → validación del compromiso en producción.

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1189 (Drive-by Compromise), T1112 (hunting via agentic IA).

**Fuente:** [TryHackMe - AI in Security - old sAInt nick](https://tryhackme.com/r/room/AIforcyber-aoc2025-y9wWQ1zRgB)
