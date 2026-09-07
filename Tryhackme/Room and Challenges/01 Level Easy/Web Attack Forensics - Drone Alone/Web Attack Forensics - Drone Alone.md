# Web Attack Forensics - Drone Alone

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `webattackforensics-aoc2025-b4t7c1d5f8` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/webattackforensics-aoc2025-b4t7c1d5f8) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | Web attack forensics, command injection, log analysis |
| **Impacto** | Alarmed — Command injection exploited on web application |

---

**Contexto:** Durante Advent of Cyber 2025 Day 15, investigamos un ataque contra la aplicación web DroneManager que utilizó command injection para ejecutar comandos arbitrarios. Analizando los logs del servidor, identificamos los ejecutables que el atacante utilizó para reconocimiento y ejecución de código malicioso.

## Solucionario

### Task 1: Análisis del Ataque Web

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the reconnaissance executable file name? | `whoami.exe` |
| 2 | What executable did the attacker attempt to run through the command injection? | `powershell.exe` |

---

**Metodología:** Se revisaron los logs de la aplicación web para identificar parámetros vulnerables a command injection, rastreando los ejecutables invocados por el atacante — primero para reconnaissance (`whoami.exe`) y luego para ejecución de código (`powershell.exe`).
**Learning chain:** Web Log Analysis → Command Injection → Forensic Artifact Extraction → Attack Chain Reconstruction
**MITRE ATT&CK:** T1059.001 — Command and Scripting Interpreter: PowerShell; T1059.003 — Windows Command Shell
**Fuente:** [TryHackMe - Web Attack Forensics - Drone Alone](https://tryhackme.com/r/room/webattackforensics-aoc2025-b4t7c1d5f8)
