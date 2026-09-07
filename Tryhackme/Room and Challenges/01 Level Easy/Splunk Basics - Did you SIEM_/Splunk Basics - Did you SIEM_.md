# Splunk Basics - Did you SIEM?

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `splunkforloganalysis-aoc2025-x8fj2k4rqp` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/splunkforloganalysis-aoc2025-x8fj2k4rqp) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | Splunk, SPL, web logs, firewall logs |
| **Impacto** | Alarmed — Web server compromise and C2 exfiltration detected |

---

**Contexto:** Durante Advent of Cyber 2025 Day 3, analizamos logs de web y firewall en Splunk para detectar el compromiso de un servidor web. Mediante consultas SPL identificamos la IP del atacante, los patrones de tráfico malicioso, intentos de path traversal y la exfiltración de datos hacia un servidor C2.

## Solucionario

### Task 1: Análisis de Logs con Splunk

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the attacker IP found attacking and compromising the web server? | `198.51.100.55` |
| 2 | Which day was the peak traffic in the logs? (Format: YYYY-MM-DD) | `2025-10-12` |
| 3 | What is the count of Havij user_agent events found in the logs? | `993` |
| 4 | How many path traversal attempts to access sensitive files on the server were observed? | `658` |

### Task 2: Análisis de Firewall

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5 | Examine the firewall logs. How many bytes were transferred to the C2 server IP from the compromised web server? | `126167` |

---

**Metodología:** Se utilizaron consultas SPL en Splunk para filtrar y correlacionar logs de web y firewall, identificando la IP atacante, patrones de user-agent malicioso, intentos de path traversal y volumen de transferencia hacia el servidor C2.
**Learning chain:** Splunk Fundamentals → SPL Queries → Log Correlation → Web Attack Analysis → C2 Detection
**MITRE ATT&CK:** T1190 — Exploit Public-Facing Application; T1041 — Exfiltration Over C2 Channel
**Fuente:** [TryHackMe - Splunk Basics - Did you SIEM?](https://tryhackme.com/r/room/splunkforloganalysis-aoc2025-x8fj2k4rqp)
