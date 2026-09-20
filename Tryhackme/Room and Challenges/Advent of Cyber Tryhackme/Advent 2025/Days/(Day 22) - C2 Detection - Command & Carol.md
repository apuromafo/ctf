# C2 Detection - Command & Carol

| **Dificultad** | Easy | **Tipo** | Sala diaria (Advent of Cyber) | **Slug** | `day22c2detectioncommandcarol` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) | | **Sección** | Advent of Cyber Tryhackme | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | C2 / Command and Control / PCAP / Zeek / RITA / beaconing / DNS tunnelling / threat intel | | **Impacto** | Detección de tráfico C2 (beaconing, DNS tunnelling, exfiltración) analizando PCAPs con Zeek (extracción de metadata) y RITA (correlación y análisis) |

---

**Contexto:** Día 22 del Advent of Cyber 2025. Se analiza un PCAP grande con **Zeek** y **RITA** para detectar tráfico de Command and Control (C2). Zeek se encarga de la extracción de datos (convierte el PCAP en logs estructurados: `conn.log`, `dns.log`, `ssl.log`), mientras que RITA es un framework open-source que correlaciona patrones (no firmas) para identificar comportamiento C2: beaconing, DNS tunnelling, conexiones de larga duración, exfiltración de datos, comportamiento TLS sospechoso e IPs/dominios maliciosos conocidos (threat intel). Se analiza la infraestructura de `malhare.net` y `rabbithole.malhare.net`.

> **Note (EN mirror):** Day 22 of AoC 2025. Analysing a large PCAP for C2 behaviour using **Zeek** (data extraction -> structured logs) and **RITA** (analytics & correlation, not signatures). RITA detects beaconing, DNS tunnelling, long-lived connections, data exfiltration, suspicious TLS and known-bad endpoints. RITA does not ingest PCAPs directly.

---

## Solucionario

### Día 22: C2 Detection - Command & Carol

**Explicación:**
- C2 -> Command and Control traffic 
- analyzing large PCAP using **Zeek** and **RITA**
- Rita -> an open-source framework used to identify C2 behaviour in network traffic; correlates patterns (not signatures)
- Zeek = data extraction ; RITA = analytics & correlation
- Rita detects (RITA does not ingest PCAPs directly)
     1. C2 beaconing
     2. DNS tunnelling
     3. Long-lived connections
     4. Data exfiltration
     5. Suspicious TLS behaviour
     6. Known malicious IPs/domains (Threat Intel)

- Use of Zeek 
     1. Observes traffic
     2. Extracts metadata
     3. Produces structured logs (conn.log, dns.log, ssl.log, etc.)
     4. Does NOT block traffic (not IDS/IPS)

### Comandos / Commands
- `zeek readpcap pcaps/AsyncRAT.pcap zeek_logs/asyncrat` : Converting PCAP to Zeek Logs
- `rita import --logs ~/zeek_logs/asyncrat/ --database asyncrat` : Importing Logs into RITA
- `rita view asyncrat` : view results

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | How many hosts are communicating with malhare.net? | `6` |
| 2 | Which Threat Modifier tells us the number of hosts communicating to a certain destination? | `prevalence` |
| 3 | What is the highest number of connections to rabbithole.malhare.net? | `40` |
| 4 | Which search filter would you use to search for all entries that communicate to rabbithole.malhare.net with a beacon score greater than 70% and sorted by connection duration (descending)? | `dst:rabbithole.malhare.net beacon:>=70 sort:duration-desc` |
| 5 | Which port did the host 10.0.0.13 use to connect to rabbithole.malhare.net? | `80` |

---

**Metodología:**

1. Convertir el PCAP a logs de Zeek: `zeek readpcap pcaps/AsyncRAT.pcap zeek_logs/asyncrat`
2. Importar los logs a RITA: `rita import --logs ~/zeek_logs/asyncrat/ --database asyncrat`
3. Ver los resultados agregados: `rita view asyncrat`
4. Aplicar filtros y threat modifiers (`prevalence`, `beacon`, `sort`) para reducir y responder

**Learning chain:** PCAP -> Zeek (conn/dns/ssl logs) -> RITA import -> view -> beacon scores -> filtros -> malhare.net / rabbithole.malhare.net

Cadena de ataque / Attack Chain:
```text
AsyncRAT.pcap -> Zeek (metadata: conn.log, dns.log, ssl.log) -> RITA (beaconing / DNS tunnelling / exfil)
-> prevalence=6 hosts -> rabbithole.malhare.net beacon >= 70% -> port 80 (10.0.0.13)
```

**Lección:** *La detección de C2 no requiere firmas: correlacionando patrones estadísticos (beaconing, prevalencia, duración de conexiones) con Zeek + RITA se puede identificar infraestructura de mando y control en tráfico aparentemente normal.*

**MITRE ATT&CK:**

- T1071 - Application Layer Protocol (C2)
- T1071.001 - Web Protocols
- T1041 - Exfiltration Over C2 Channel
- T1573 - Encrypted Channel
- T1008 - Fallback Channels

**Fuente:** [TryHackMe - C2 Detection - Command & Carol](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.