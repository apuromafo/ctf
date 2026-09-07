# Traffic Analysis Pitfalls

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `trafficanalysispitfalls` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/trafficanalysispitfalls) |
| **Sección** | Network Traffic Analysis |
| **Fuente** | THM |
| **Componentes** | Fortigate logs, Zeek, DNS, DoH, beaconing, exfiltration |
| **Impacto** | Medium |

---

**Contexto:** Este room explora las trampas comunes del análisis de tráfico de red, donde los patrones de tráfico legítimo pueden enmascarar actividades maliciosas. Usaremos logs de FortiGate y Zeek para identificar tráfico sospechoso como beaconing, DNS over HTTPS (DoH) encubierto, exfiltración de datos y conexiones a infraestructura de Tor. El foco está en ir más allá de lo obvio y encontrar lo que se esconde en el volumen normal de tráfico.
**Learning chain:** FortiGate Logs → Zeek DNS → QUIC Analysis → DoH Detection → Beaconing Patterns → Exfiltration Tracing
**MITRE ATT&CK:** T1567 (Exfiltration Over Web Service), T1071.004 (Application Layer Protocol: DNS), T1090 (Proxy), T1048 (Exfiltration Over Alternative Protocol)
**Fuente:** [TryHackMe - Traffic Analysis Pitfalls](https://tryhackme.com/r/room/trafficanalysispitfalls)

---

## Solucionario

### Task 1: FortiGate Analysis

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many connections in the Fortigate logs have a dst_category of Bulletproof Hosting? | `4` |
| 2 | Looking at the hourly beaconing results, What is the minimum min_b value in the hourly results, representing the beacon keepalive size in bytes? | `800` |

### Task 2: QUIC and Anomalous Sessions

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run the transport breakdown query. How many port 443 sessions in the Zeek logs use QUIC (UDP/443)? | `6946` |
| 2 | Run the anomalous QUIC session query. What is the duration in seconds of the session that exceeds one hour? | `15180` |

### Task 3: DNS over HTTPS (DoH)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run the all-hosts DNS timechart below. On what date does WKST-MKTG-07 (10.10.12.23) first appear with zero UDP/53 queries? (Answer Format: YYYY-MM-DD) | `2026-03-27` |
| 2 | From the DoH confirmation query results, how many total DoH connections does WKST-MKTG-07 make on 2026-03-27 across both resolvers? | `26` |

### Task 4: Process Attribution

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run the process count query against 172.67.153.42. Which process is responsible for the most connections to this destination? | `C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE` |

### Task 5: Tor and Risk Scoring

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run the baseline enrichment query. How many FortiGate connections resolve to a dst_category of Tor Exit / Anonymisation? | `6` |
| 2 | Run the high-risk filter query. What is the srcname of the workstation connecting to a Tor exit relay? | `WKST-HR-02` |

### Task 6: Exfiltration Analysis

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many bytes were transferred outbound in the April 2 exfiltration event? | `847823104` |
| 2 | Run the process count query. How many connections does EXCEL.EXE make to 172.67.153.42? | `6108` |
| 3 | What is the last_seen timestamp for EXCEL.EXE (PID 4812)? | `2026-04-06 21:55:44` |

---

**Metodología:** El room avanza por capas de análisis: primero se revisan logs de FortiGate para identificar hosting bulletproof y patrones de beaconing, luego se inspeccionan sesiones QUIC anómalas, se detecta migración de DNS legítimo a DoH encubierto, se atribuye tráfico a procesos específicos (EXCEL.EXE), se filtra tráfico de alto riesgo (Tor), y finalmente se cuantifica un evento de exfiltración con métricas de bytes y volumen de conexiones.
