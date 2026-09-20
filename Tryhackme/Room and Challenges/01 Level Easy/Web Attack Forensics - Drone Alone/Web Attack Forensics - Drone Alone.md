# Web Attack Forensics - Drone Alone

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Medium | walkthrough | `webattackforensics-aoc2025-b4t7c1d5f8` | https://tryhackme.com/room/webattackforensics-aoc2025-b4t7c1d5f8 | Advent of Cyber 2025 | TryHackMe | Web attack forensics, command injection, log analysis | Alarmed — Command injection exploited on web application |

---

**Contexto:** Durante Advent of Cyber 2025 Day 15, investigamos un ataque contra la aplicación web DroneManager que utilizó command injection para ejecutar comandos arbitrarios. Analizando los logs del servidor, identificamos los ejecutables que el atacante utilizó para reconocimiento y ejecución de código malicioso.

> **ES:** La investigación forense de los logs de DroneManager revela un command injection: el atacante ejecutó `whoami.exe` para el reconocimiento y `powershell.exe` para la ejecución de código malicioso.
> **EN:** Forensic review of the DroneManager logs reveals a command injection: the attacker ran `whoami.exe` for reconnaissance and `powershell.exe` for the malicious code execution.

## Solucionario

### Task 1: Análisis del Ataque Web / Web Attack Analysis

**Explicación:** Se analizan los logs de la aplicación web DroneManager para reconstruir el ataque. El atacante explotó un command injection en un parámetro vulnerable y, tras el reconocimiento con `whoami.exe`, intentó ejecutar código malicioso mediante `powershell.exe`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the reconnaissance executable file name? | `whoami.exe` |
| 2 | What executable did the attacker attempt to run through the command injection? | `powershell.exe` |

---

**Metodología:** Se revisaron los logs de la aplicación web para identificar parámetros vulnerables a command injection, rastreando los ejecutables invocados por el atacante — primero para reconnaissance (`whoami.exe`) y luego para ejecución de código (`powershell.exe`).

### Cadena de ataque / Attack Chain

```text
DroneManager (web app) -> parámetro vulnerable a command injection -> whoami.exe (reconnaissance) -> powershell.exe (ejecución de código) -> logs del servidor evidencian la cadena de ataque
```

**Learning chain:** Web Log Analysis → Command Injection → Forensic Artifact Extraction → Attack Chain Reconstruction

**Lección:** *El análisis de los logs web permite reconstruir una cadena de command injection: los ejecutables invocados delatan primero el reconocimiento (`whoami.exe`) y después la ejecución de código (`powershell.exe`).*

**MITRE ATT&CK:** T1059.001 — Command and Scripting Interpreter: PowerShell; T1059.003 — Windows Command Shell

**Fuente:** [TryHackMe - Web Attack Forensics - Drone Alone](https://tryhackme.com/room/webattackforensics-aoc2025-b4t7c1d5f8)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.