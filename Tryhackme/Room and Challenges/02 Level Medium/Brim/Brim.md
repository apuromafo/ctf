# Brim
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `brim` |
| **Link** | [TryHackMe](https://tryhackme.com/room/brim) |
| **Sección** | SOC Level 1 / Traffic Analysis |
| **Fuente** | Writeup de Jasper Alblas (jalblas.com) y rogervinas (GitHub) |
| **Componentes** | Brim, Zeek logs (dns, ntp, conn, stats, http), alertas Suricata, pcap/pcapng, Cobalt Strike, IcedID, criptominería, MITRE ATT&CK TA0040, VirusTotal |
| **Impacto** | Sala Medium del path SOC Level 1: análisis de tráfico de red (pcap) con Brim, correlación entre logs Zeek y alertas Suricata, exercise de threat hunting de C2 (Cobalt Strike/IcedID) y de criptominería. |
---
**Contexto:** Brim es una aplicación de escritorio open-source que procesa archivos pcap y logs estructurados Zeek, integrando también alertas Suricata. Su interfaz tipo "grep sobre logs" permite buscar, filtrar, correlacionar y resumir grandes volúmenes de tráfico sin tocar la línea de comandos, y de ahí saltar a Wireshark o VirusTotal. En esta sala se procesan varios pcaps de ejemplo para dominar el panel de detalles y las 12 queries predefinidas, y terminar con dos ejercicios de threat hunting: detección de C2 de Cobalt Strike con canal secundario IcedID y detección de criptominería.
*EN: Brim is an open-source desktop app that processes pcap files and structured Zeek logs, also integrating Suricata alerts. Its grep-on-logs GUI lets you search, filter, correlate and summarize large volumes of traffic without touching the command line, then jump to Wireshark or VirusTotal. This room processes several sample pcaps to master the log details panel and the 12 default queries, ending with two threat-hunting exercises: Cobalt Strike C2 detection with an IcedID secondary channel and crypto-mining detection.*
## Solucionario
### Task 1 — Introduction
**Explicación:** Introducción a la sala: se espera que conozcas conceptos básicos de seguridad y logs Zeek (recomiendan el path Network Fundamentals y la sala Zeek). La pregunta es de lectura únicamente.
*EN: Room introduction: basic security knowledge and Zeek log processing are expected (Network Fundamentals path and the Zeek room are recommended). The question is read-only.*
### Task 2 — What is Brim?
**Explicación:** Brim es una herramienta de escritorio para análisis de pcap y logs que usa Zeek (logs) y Suricata (firmas): es una alternativa GUI a Wireshark/Zeek, ideal para pcaps medianos-grandes y correlación de logs (no soporta sniffing ni pcaps enormes). La pregunta es de lectura únicamente.
*EN: Brim is a desktop analysis tool for pcaps and logs that uses Zeek (logs) and Suricata (signatures): a GUI-based alternative to Wireshark/Zeek, ideal for medium/large pcaps and log correlation (no sniffing support and not suitable for huge pcaps). The question is read-only.*
### Task 3 — The Basics
**Explicación:** Importa `sample.pcap` en Brim y usa el panel de detalles (clic derecho > Open details) sobre el primer log de cada tipo: DNS, NTP y STATS. Las respuestas salen de los campos `qclass_name`, `duration` y `reassem_tcp_size`.
*EN: Import `sample.pcap` in Brim and use the details panel (right-click > Open details) on the first log of each type: DNS, NTP and STATS. Answers come from the `qclass_name`, `duration` and `reassem_tcp_size` fields.*

```bash
# Brim (interfaz): importar sample.pcap y abrir detalles de cada log
# DNS  -> qclass_name:                    C_INTERNET
# NTP  -> duration:                       0.005
# STATS -> reassem_tcp_size:              540
```
### Task 4 — Default Queries
**Explicación:** Con las queries predefinidas de Brim (File Activity, Unique Connections, Suricata Alerts by Category) se inspeccionan archivos, nombres de ciudad del log `conn` y alertas Suricata. Para las ciudades se usa `_path=="conn"` y para la firma Suricata una query con `event_type=="alert"`.
*EN: Using Brim's default queries (File Activity, Unique Connections, Suricata Alerts by Category) you inspect files, city names from the `conn` log and Suricata alerts. The `_path=="conn"` filter is used for cities and an `event_type=="alert"` query for the Suricata signature.*

```bash
_path=="conn" | cut geo.resp.city | sort | uniq -c
event_type=="alert" | count() by alert.severity,alert.category,alert.signature,alert.signature_id | sort count
```
### Task 5 — Use Cases
**Explicación:** Repaso de queries de análisis habituales: hosts comunicados, puertos activos, transferencias de datos, DNS/HTTP sospechosos, actividad SMB y revisión de alertas (`_path=="dns"`, `_path=="http"`, `event_type=="alert"`...). La pregunta es de lectura únicamente.
*EN: Review of common analysis queries: communicated hosts, active ports, data transfers, suspicious DNS/HTTP, SMB activity and alert review (`_path=="dns"`, `_path=="http"`, `event_type=="alert"`...). The question is read-only.*
### Task 6 — Exercise: Threat Hunting with Brim | Malware C2 Detection
**Explicación:** Con `task6-malware-c2.pcap`, se detecta la descarga de `4564.exe` desde la IP 104.168.44.45 (Cobalt Strike, confirmada en VirusTotal). La query `_path=="conn" and id.resp_h==104.168.44.45 and id.resp_p==443 | count()` da 328 conexiones. Las alertas Suricata revelan el canal secundario: IcedID (BokBot), que actúa como broker de acceso inicial y C2 alternativo.
*EN: Using `task6-malware-c2.pcap`, the download of `4564.exe` from IP 104.168.44.45 (Cobalt Strike, confirmed on VirusTotal) is detected. The query `_path=="conn" and id.resp_h==104.168.44.45 and id.resp_p==443 | count()` returns 328 connections. Suricata alerts reveal the secondary channel: IcedID (BokBot), acting as initial access broker and backup C2.*

```bash
_path=="http" | cut id.orig_h, id.resp_h, id.resp_p, method, host, uri | uniq -c | sort value.uri
_path=="conn" and id.resp_h==104.168.44.45 and id.resp_p==443 | count()
event_type=="alert" | cut alert.signature | sort -r | uniq -c | sort -r count
```
### Task 7 — Exercise: Threat Hunting with Brim | Crypto Mining
**Explicación:** Con `task7-crypto-mine.pcapng` se detectan puertos inusuales de criptominería: 22 conexiones al puerto 19999, servicio `irc` en 6666 y un total de 3,729 bytes transferidos a 101.201.172.235:8888. Las alertas Suricata mapean la táctica MITRE de impacto: TA0040.
*EN: Using `task7-crypto-mine.pcapng` unusual mining ports are detected: 22 connections to port 19999, `irc` service on 6666 and 3,729 total bytes sent to 101.201.172.235:8888. Suricata alerts map the Impact MITRE tactic: TA0040.*

```bash
_path=="conn" id.resp_p == 19999 | cut id.resp_p | uniq -c
_path=="conn" id.resp_p == 6666 | cut service | uniq -c
_path=="conn" id.resp_h == 101.201.172.235 id.resp_p == 8888 | summarize sum(orig_bytes + resp_bytes)
event_type=="alert" | cut alert.metadata.mitre_tactic_id | sort | uniq -c
```
### Task 8 — Conclusion
**Explicación:** Cierre de la sala: se recomienda continuar con la sala reto Masterminds para practicar Brim. La pregunta es de lectura únicamente.
*EN: Room wrap-up: continue with the Masterminds challenge room to practice Brim. The question is read-only.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Process the "sample.pcap" file and look at the details of the first DNS log that appear on the dashboard. What is the "qclass_name"? | `C_INTERNET` |
| 2 | Look at the details of the first NTP log that appear on the dashboard. What is the "duration" value? | `0.005` |
| 3 | Look at the details of the STATS packet log that is visible on the dashboard. What is the "reassem_tcp_size"? | `540` |
| 4 | Investigate the files. What is the name of the detected GIF file? | `cat01_with_hidden_text.gif` |
| 5 | Investigate the conn logfile. What is the number of the identified city names? | `2` |
| 6 | Investigate the Suricata alerts. What is the Signature id of the alert category "Potential Corporate Privacy Violation"? | `2,012,887` |
| 7 | What is the name of the file downloaded from the CobaltStrike C2 connection? | `4564.exe` |
| 8 | What is the number of CobaltStrike connections using port 443? | `328` |
| 9 | There is an additional C2 channel in used the given case. What is the name of the secondary C2 channel? | `IcedID` |
| 10 | How many connections used port 19999? | `22` |
| 11 | What is the name of the service used by port 6666? | `irc` |
| 12 | What is the amount of transferred total bytes to "101.201.172.235:8888"? | `3,729` |
| 13 | What is the detected MITRE tactic id? | `TA0040` |
---
**Metodología:** Procesar pcap en Brim → revisar panel de detalles y queries predefinidas (File Activity, Activity Overview, Suricata Alerts) → correlacionar logs Zeek (dns, conn, http) → confirmar IoCs en VirusTotal (dominios/IPs C2) → usar queries tipo `_path=="conn" | cut ... | sort/uniq -c` para conteos y `event_type=="alert"` para detectar firmas/tácticas MITRE → mapear a ATT&CK.
**Learning chain:** pcap → Zeek logs + Suricata en Brim → correlación de logs → detección de descarga de binario malicioso → identificación de C2 (Cobalt Strike) y canal secundario (IcedID) → detección de criptominería y mapeo a táctica MITRE.
**Lección:** *Con Brim no hace falta scripting complejo: las queries agregadas sobre logs Zeek (count, summarize, uniq -c) y las alertas Suricata bastan para correlacionar descargas, C2 y minería en un pcap.*
**MITRE ATT&CK:** T1105 (Ingress Tool Transfer - 4564.exe), T1071.001 (Web Protocols/443), T1190, T1496 (Resource Hijacking - crypto mining), T1036, TA0040 (Impact), T1043.
**Fuente:** [TryHackMe - Brim](https://tryhackme.com/room/brim)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.