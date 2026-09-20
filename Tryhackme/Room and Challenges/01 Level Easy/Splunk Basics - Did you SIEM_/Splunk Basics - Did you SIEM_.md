# Splunk Basics - Did you SIEM?

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Medium | walkthrough | `splunkforloganalysis-aoc2025-x8fj2k4rqp` | [TryHackMe](https://tryhackme.com/r/room/splunkforloganalysis-aoc2025-x8fj2k4rqp) | Advent of Cyber 2025 | TryHackMe | Splunk, SPL, web logs, firewall logs | Alarmed — Web server compromise and C2 exfiltration detected |

---

**Contexto:** Durante Advent of Cyber 2025 Day 3, analizamos logs de web y firewall en Splunk para detectar el compromiso de un servidor web. Mediante consultas SPL identificamos la IP del atacante, los patrones de tráfico malicioso, intentos de path traversal y la exfiltración de datos hacia un servidor C2.

## Solucionario

### Task 1: Análisis de Logs con Splunk / Log Analysis with Splunk

**Explicación:** Se Utilizan consultas SPL en Splunk para analizar los logs web del servidor comprometido. Se Identifica la IP del atacante, el día de mayor tráfico, el recuento de eventos con user-agent Havij y los intentos de path traversal hacia archivos sensibles.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the attacker IP found attacking and compromising the web server? | `198.51.100.55` |
| 2 | Which day was the peak traffic in the logs? (Format: YYYY-MM-DD) | `2025-10-12` |
| 3 | What is the count of Havij user_agent events found in the logs? | `993` |
| 4 | How many path traversal attempts to access sensitive files on the server were observed? | `658` |

### Task 2: Análisis de Firewall / Firewall Analysis

**Explicación:** Se Analizan los logs de firewall para cuantificar la exfiltración de datos hacia la IP del servidor C2 desde el servidor web comprometido.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5 | Examine the firewall logs. How many bytes were transferred to the C2 server IP from the compromised web server? | `126167` |

---

**Metodología:** Se utilizaron consultas SPL en Splunk para filtrar y correlacionar logs de web y firewall, identificando la IP atacante, patrones de user-agent malicioso, intentos de path traversal y volumen de transferencia hacia el servidor C2.

### Cadena de ataque / Attack Chain

**Learning chain:** Splunk Fundamentals → SPL Queries → Log Correlation → Web Attack Analysis → C2 Detection

**Lección:** *La correlación de logs de web y firewall en un SIEM como Splunk permite reconstruir una cadena de ataque completa, desde la exploración inicial hasta la exfiltración de datos hacia un servidor C2.*

**MITRE ATT&CK:** T1190 — Exploit Public-Facing Application; T1041 — Exfiltration Over C2 Channel

**Fuente:** [TryHackMe - Splunk Basics - Did you SIEM?](https://tryhackme.com/r/room/splunkforloganalysis-aoc2025-x8fj2k4rqp)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.