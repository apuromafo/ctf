# Traffic Analysis Pitfalls

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `trafficanalysispitfalls` | [TryHackMe](https://tryhackme.com/room/trafficanalysispitfalls) | Network Traffic Analysis | THM | Fortigate logs, Zeek, DNS, DoH, beaconing, exfiltration | Medium |

---

**Contexto:**

> **ES:** Este room explora las trampas comunes del análisis de tráfico de red, donde los patrones de tráfico legítimo pueden enmascarar actividades maliciosas. Usaremos logs de FortiGate y Zeek para identificar tráfico sospechoso como beaconing, DNS over HTTPS (DoH) encubierto, exfiltración de datos y conexiones a infraestructura de Tor. El foco está en ir más allá de lo obvio y encontrar lo que se esconde en el volumen normal de tráfico.

> **EN:** This room explores the common pitfalls of network traffic analysis, where legitimate traffic patterns can mask malicious activity. We will use FortiGate and Zeek logs to identify suspicious traffic such as beaconing, covert DNS over HTTPS (DoH), data exfiltration, and connections to Tor infrastructure. The focus is on going beyond the obvious and finding what hides in the normal volume of traffic.

## Solucionario

### Task 1: FortiGate Analysis / FortiGate Analysis

**Explicación:**

Análisis inicial de los logs de FortiGate para localizar hosting bulletproof y patrones de beaconing.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many connections in the Fortigate logs have a dst_category of Bulletproof Hosting? | `4` |
| 2 | Looking at the hourly beaconing results, What is the minimum min_b value in the hourly results, representing the beacon keepalive size in bytes? | `800` |

### Task 2: QUIC and Anomalous Sessions / QUIC and Anomalous Sessions

**Explicación:**

Inspección de sesiones QUIC anómalas en los logs de Zeek que superan los umbrales normales de duración.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run the transport breakdown query. How many port 443 sessions in the Zeek logs use QUIC (UDP/443)? | `6946` |
| 2 | Run the anomalous QUIC session query. What is the duration in seconds of the session that exceeds one hour? | `15180` |

### Task 3: DNS over HTTPS (DoH) / DNS over HTTPS (DoH)

**Explicación:**

Detección de la migración de DNS legítimo a DoH encubierto en el tráfico de un equipo específico de la red.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run the all-hosts DNS timechart below. On what date does WKST-MKTG-07 (10.10.12.23) first appear with zero UDP/53 queries? (Answer Format: YYYY-MM-DD) | `2026-03-27` |
| 2 | From the DoH confirmation query results, how many total DoH connections does WKST-MKTG-07 make on 2026-03-27 across both resolvers? | `26` |

### Task 4: Process Attribution / Process Attribution

**Explicación:**

Atribución del tráfico sospechoso al proceso responsable de las conexiones hacia los destinos analizados.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run the process count query against 172.67.153.42. Which process is responsible for the most connections to this destination? | `C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE` |

### Task 5: Tor and Risk Scoring / Tor and Risk Scoring

**Explicación:**

Filtrado del tráfico de alto riesgo mediante puntuación, identificando conexiones a relays de salida de Tor.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Run the baseline enrichment query. How many FortiGate connections resolve to a dst_category of Tor Exit / Anonymisation? | `6` |
| 2 | Run the high-risk filter query. What is the srcname of the workstation connecting to a Tor exit relay? | `WKST-HR-02` |

### Task 6: Exfiltration Analysis / Exfiltration Analysis

**Explicación:**

Cuantificación del evento de exfiltración de abril con métricas de bytes transferidos y volumen de conexiones del proceso implicado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many bytes were transferred outbound in the April 2 exfiltration event? | `847823104` |
| 2 | Run the process count query. How many connections does EXCEL.EXE make to 172.67.153.42? | `6108` |
| 3 | What is the last_seen timestamp for EXCEL.EXE (PID 4812)? | `2026-04-06 21:55:44` |

---

**Metodología:** El room avanza por capas de análisis: primero se revisan logs de FortiGate para identificar hosting bulletproof y patrones de beaconing, luego se inspeccionan sesiones QUIC anómalas, se detecta migración de DNS legítimo a DoH encubierto, se atribuye tráfico a procesos específicos (EXCEL.EXE), se filtra tráfico de alto riesgo (Tor), y finalmente se cuantifica un evento de exfiltración con métricas de bytes y volumen de conexiones.

### Cadena de ataque / Attack Chain

FortiGate logs → beaconing → QUIC anomalies → DNS over HTTPS → process attribution → Tor traffic → exfiltration.

**Learning chain:** FortiGate Logs → Zeek DNS → QUIC Analysis → DoH Detection → Beaconing Patterns → Exfiltration Tracing

**Lección:** *Lo que no se ve en el tráfico importa tanto como lo que se ve: el DoH y el beaconing sobreviven al filtrado superficial.*

**MITRE ATT&CK:** T1567 (Exfiltration Over Web Service), T1071.004 (Application Layer Protocol: DNS), T1090 (Proxy), T1048 (Exfiltration Over Alternative Protocol)

**Fuente:** [TryHackMe - Traffic Analysis Pitfalls](https://tryhackme.com/r/room/trafficanalysispitfalls)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.