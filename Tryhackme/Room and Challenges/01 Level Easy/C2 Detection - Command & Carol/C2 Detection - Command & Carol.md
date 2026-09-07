# C2 Detection - Command & Carol

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `detecting-c2-with-rita-aoc2025-m9n2b5v8c1` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/detecting-c2-with-rita-aoc2025-m9n2b5v8c1) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | RITA, beaconing, threat modifiers, network detection |
| **Impacto** | Detección de communicationes C2 en tráfico de red |

---

**Contexto:** RITA (Real Intelligence Threat Analytics) es una herramienta de análisis de tráfico de red que detecta patrones de beaconing y comunicaciones con dominios maliciosos. En esta práctica se analizan logs de red para identificar hosts comprometidos que se comunican con servidores C2, aplicando filtros de amenaza y modificadores de severidad.

## Solucionario

### Task 1: RITA Analysis

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many hosts are communicating with malhare.net? | `6` |
| 2 | Which Threat Modifier tells us the number of hosts communicating to a certain destination? | `prevalence` |
| 3 | What is the highest number of connections to rabbithole.malhare.net? | `40` |

### Task 2: Advanced Filtering

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | Which search filter would you use to search for all entries that communicate to rabbithole.malhare.net with a beacon score greater than 70% and sorted by connection duration (descending)? | `dst:rabbithole.malhare.net beacon:>=70 sort:duration-desc` |
| 5 | Which port did the host 10.0.0.13 use to connect to rabbithole.malhare.net? | `80` |

---

**Metodología:** Se utilizó RITA para analizar logs de red Zeek, identificando dominios maliciosos y patrones de beaconing. Se aplicaron modificadores de amenaza (threat modifiers) como `prevalence` para cuantificar la propagación. Se usaron filtros avanzados para aislar las comunicaciones más sospechosas y determinar puertos de conexión específicos.
**Learning chain:** Network log analysis → RITA → beaconing detection → threat modifiers → advanced filtering → IOC extraction
**MITRE ATT&CK:** T1071.001 - Application Layer Protocol: Web Protocols, T1573.002 - Encrypted Channel: Asymmetric Cryptography
**Fuente:** [TryHackMe - C2 Detection - Command & Carol](https://tryhackme.com/r/room/detecting-c2-with-rita-aoc2025-m9n2b5v8c1)