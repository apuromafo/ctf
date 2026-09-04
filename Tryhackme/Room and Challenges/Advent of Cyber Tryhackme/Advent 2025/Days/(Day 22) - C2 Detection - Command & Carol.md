# Advent 2025\Days [N/A]

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

## Respuestas / Answers:
- How many hosts are communicating with malhare.net? : `6`
- Which Threat Modifier tells us the number of hosts communicating to a certain destination? : `prevalence`
- What is the highest number of connections to rabbithole.malhare.net? : `40`
- Which search filter would you use to search for all entries that communicate to rabbithole.malhare.net with a beacon score greater than 70% and sorted by connection duration (descending)? : `dst:rabbithole.malhare.net beacon:>=70 sort:duration-desc`
- Which port did the host 10.0.0.13 use to connect to rabbithole.malhare.net? : `80`

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
