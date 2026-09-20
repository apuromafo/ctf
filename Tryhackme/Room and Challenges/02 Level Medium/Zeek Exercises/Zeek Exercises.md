# Zeek Exercises
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `zeekexercises` |
| **Link** | [TryHackMe](https://tryhackme.com/room/zeekexercises) |
| **Sección** | SOC Level 1 / Traffic Analysis |
| **Fuente** | TryHackMe - Zeek Exercises (https://tryhackme.com/room/zeekexercises) |
| **Componentes** | Zeek, zeek-cut, logs (conn.log, dns.log, http.log, files.log, signatures.log, log4j.log), pcaps (dns-tunneling.pcap, phishing.pcap, log4shell.pcapng), scripts (hash-demo.zeek, detection-log4j.zeek), VirusTotal, CyberChef, base64, DNS AAAA/TXT túneles DNS, VBA macro, Log4Shell (CVE-2021-44228) |
| **Impacto** | Sala Medium del path SOC Level 1: reto de análisis de tráfico con Zeek para confirmar tres positivos de SIEM — túnel DNS (Anomalous DNS Activity), phishing con macro VBA (Phishing Attempt) y explotación Log4Shell (Log4J Exploitation Attempt) — extrayendo IPs, dominios, hashes MD5, ficheros maliciosos y payloads base64 desde los logs Zeek. |

---
**Contexto:** Zeek Exercises es la continuación práctica del room "Zeek": se investigan tres capturas de tráfico (dns-tunneling.pcap, phishing.pcap y log4shell.pcapng) correspondientes a tres alertas de SIEM que el alumno debe confirmar como positivos reales (o descartarlos). El flujo combina el procesado de pcaps con Zeek, la extracción de campos con zeek-cut, la correlación de logs (conn/dns/http/files/signatures/log4j), la consulta de ficheros en VirusTotal y la decodificación de payloads en CyberChef. Las respuestas de IPs y dominios se introducen en formato defanged (p. ej. `10[.]6[.]27[.]102`).
*EN: Zeek Exercises is the practical follow-up to the "Zeek" room: three traffic captures are investigated (dns-tunneling.pcap, phishing.pcap and log4shell.pcapng) matching three SIEM alerts that the student must confirm as true positives (or dismiss). The flow combines pcap processing with Zeek, field extraction with zeek-cut, log correlation (conn/dns/http/files/signatures/log4j), file lookups on VirusTotal and payload decoding in CyberChef. IP and domain answers are submitted in defanged format (e.g. `10[.]6[.]27[.]102`).*

## Solucionario
### Task 1 — Introducción / Introduction
**Explicación:** Presentación del reto: se recomienda haber completado antes la sala "Zeek". La idea es investigar series de tráfico capturado y detener la actividad maliciosa en distintos escenarios. No hay pregunta práctica.
*EN: Challenge introduction: completing the "Zeek" room first is recommended. The goal is to investigate captured traffic series and stop malicious activity in different scenarios. No hands-on question.*
```text
1. No answer needed
```

### Task 2 — DNS Anómalo / Anomalous DNS
**Explicación:** Alerta disparada: "Anomalous DNS Activity". Se procesa `dns-tunneling.pcap` y se investiga el `dns.log`: los registros AAAA (IPv6) son la anomalía — 320 registros ligados a IPv6. Sobre `conn.log` se localiza la duración máxima de conexión (9.420791). En `dns.log` se filtran las consultas únicas de dominio: hay una ingente cantidad de consultas a `cisco-update.com` (túnel DNS), y contando dominios base (quitando el patrón principal) quedan 6. Finalmente, en `conn.log` se identifica el host origen de esa actividad: 10.20.57.3.
*EN: Triggered alert: "Anomalous DNS Activity". `dns-tunneling.pcap` is processed and `dns.log` investigated: the AAAA (IPv6) records are the anomaly — 320 records linked to IPv6. Over `conn.log` the longest connection duration is found (9.420791). In `dns.log` unique domain queries are filtered: a huge amount of queries go to `cisco-update.com` (DNS tunnel), and counting base domains (removing the main pattern) leaves 6. Finally, `conn.log` reveals the source host: 10.20.57.3.*
```bash
zeek -C -r dns-tunneling.pcap
cat dns.log | zeek-cut qtype_name | sort | uniq -c
cat conn.log | zeek-cut duration | sort -r | head -n 1
cat dns.log | zeek-cut query | rev | cut -d '.' -f 1-2 | rev | sort | uniq | wc -l
cat conn.log | zeek-cut id.orig_h | sort | uniq -c
```
```text
1. 320
2. 9.420791
3. 6
4. 10.20.57.3
```

### Task 3 — Phishing
**Explicación:** Alerta disparada: "Phishing Attempt". Se procesa `phishing.pcap`; en `conn.log` hay un único host origen sospechoso, 10.6.27.102 (se responde defanged como `10[.]6[.]27[.]102`). En `http.log` los ficheros maliciosos se descargan desde `smart-fax[.]com`. Con el script `hash-demo.zeek` se obtienen los hashes MD5 de `files.log` para consultar cada artefacto en VirusTotal: el documento malicioso arrastra VBA (macros), el `.exe` extraído responde al nombre `PleaseWaitWindow.exe` y contacta con `hopto[.]org` (defanged), y la petición HTTP del `.exe` descargado es `knr.exe`.
*EN: Triggered alert: "Phishing Attempt". `phishing.pcap` is processed; `conn.log` shows a single suspicious source host, 10.6.27.102 (answered defanged as `10[.]6[.]27[.]102`). In `http.log` the malicious files are downloaded from `smart-fax[.]com`. Using `hash-demo.zeek` the MD5 hashes in `files.log` are obtained to query each artefact on VirusTotal: the malicious document carries VBA (macros), the extracted `.exe` is known as `PleaseWaitWindow.exe` and contacts `hopto[.]org` (defanged), and the HTTP request of the downloaded `.exe` is `knr.exe`.*
```bash
zeek -Cr phishing.pcap
cat conn.log | zeek-cut id.orig_h | sort | uniq -c
cat http.log | zeek-cut uri host
zeek -Cr phishing.pcap hash-demo.zeek
cat files.log | zeek-cut mime_type md5
```
```text
1. 10[.]6[.]27[.]102
2. smart-fax[.]com
3. VBA
4. PleaseWaitWindow.exe
5. hopto[.]org
6. knr.exe
```

### Task 4 — Log4J
**Explicación:** Alerta disparada: "Log4J Exploitation Attempt" (Log4Shell, CVE-2021-44228). Se procesa `log4shell.pcapng` con el script `detection-log4j.zeek`; en `signatures.log` se cuentan 3 hits de firma. En `http.log` el `user_agent` revela la herramienta de escaneo (Nmap), y el campo `uri` muestra el fichero de explotación con extensión `.class` (JNDI). En `log4j.log` se filtran los valores con la palabra `Base64` y, decodificando esos payloads, se obtiene el nombre del fichero creado: `pwned`.
*EN: Triggered alert: "Log4J Exploitation Attempt" (Log4Shell, CVE-2021-44228). `log4shell.pcapng` is processed with the `detection-log4j.zeek` script; `signatures.log` shows 3 signature hits. In `http.log` the `user_agent` reveals the scanning tool (Nmap), and the `uri` field shows the exploit file with `.class` extension (JNDI). In `log4j.log` values containing `Base64` are filtered and, decoding those payloads, the name of the created file is obtained: `pwned`.*
```bash
zeek -Cr log4shell.pcapng detection-log4j.zeek
cat signatures.log | zeek-cut sig_id | wc -l
cat http.log | zeek-cut user_agent | sort | uniq -c
cat http.log | zeek-cut uri | sort | uniq
cat log4j.log | zeek-cut value | grep Base64
```
```text
1. 3
2. Nmap
3. .class
4. pwned
```

### Task 5 — Conclusión / Conclusion
**Explicación:** Cierre del reto de prácticas con Zeek aplicado a casos reales de SOC. No hay pregunta práctica.
*EN: Wrap-up of the Zeek practice challenge applied to real SOC cases. No hands-on question.*
```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
| 2 | Investigate the dns-tunneling.pcap file. Investigate the dns.log file. What is the number of DNS records linked to the IPv6 address? | `320` |
| 3 | Investigate the conn.log file. What is the longest connection duration? | `9.420791` |
| 4 | Investigate the dns.log file. Filter all unique DNS queries. What is the number of unique domain queries? | `6` |
| 5 | There are a massive amount of DNS queries sent to the same domain. This is abnormal. Let's find out which hosts are involved in this activity. Investigate the conn.log file. What is the IP address of the source host? | `10.20.57.3` |
| 6 | Investigate the logs. What is the suspicious source address? Enter your answer in defanged format. | `10[.]6[.]27[.]102` |
| 7 | Investigate the http.log file. Which domain address were the malicious files downloaded from? Enter your answer in defanged format. | `smart-fax[.]com` |
| 8 | Investigate the malicious document in VirusTotal. What kind of file is associated with the malicious document? | `VBA` |
| 9 | Investigate the extracted malicious .exe file. What is the given file name in Virustotal? | `PleaseWaitWindow.exe` |
| 10 | Investigate the malicious .exe file in VirusTotal. What is the contacted domain name? Enter your answer in defanged format. | `hopto[.]org` |
| 11 | Investigate the http.log file. What is the request name of the downloaded malicious .exe file? | `knr.exe` |
| 12 | Investigate the log4shell.pcapng file with detection-log4j.zeek script. Investigate the signature.log file. What is the number of signature hits? | `3` |
| 13 | Investigate the http.log file. Which tool is used for scanning? | `Nmap` |
| 14 | Investigate the http.log file. What is the extension of the exploit file? | `.class` |
| 15 | Investigate the log4j.log file. Decode the base64 commands. What is the name of the created file? | `pwned` |
| 16 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
---
**Metodología:** Procesar cada pcap con `zeek -C/-Cr` añadiendo el script indicado (hash-demo.zeek, detection-log4j.zeek) → inspeccionar los logs generados (conn, dns, http, files, signatures, log4j) con `zeek-cut` y combinaciones de sort/uniq/grep/wc para recuentos → correlacionar IPs y dominios de los logs → defangear los indicadores para la respuesta (CyberChef) → sacar los hashes MD5 de files.log y consultarlos en VirusTotal (tipo de fichero, macros VBA, nombre y dominios contactados) → decodificar los payloads base64 del log4j.log para recuperar la evidencia final.

### Cadena de ataque / Attack Chain
```text
dns-tunneling.pcap → qtype AAAA (320) + dur. máx 9.420791 + dominios únicos (6) → origen 10.20.57.3 → túnel DNS confirmado
phishing.pcap → único src 10[.]6[.]27[.]102 → dominio smart-fax[.]com → hash-demo.zeek → files.log MD5 → VirusTotal: VBA + PleaseWaitWindow.exe + hopto[.]org + petición knr.exe
log4shell.pcapng + detection-log4j.zeek → 3 hits de firma → user_agent Nmap → uri .class → log4j.log Base64 → decode → fichero "pwned"
```
**Learning chain:** alerta de SIEM → pcap → logs Zeek (conn/dns/http/files/signatures/log4j) → zeek-cut + sort/uniq/wc → hashes MD5 → VirusTotal → defanging (CyberChef) → decodificación base64 → veredicto true positive.
**Lección:** *Confirmar un positivo de SIEM con Zeek es un pipeline: los logs estructurados (AAAA, duración, consultas únicas, user_agent, uri) responden el "qué" y el "cuánto", los hashes de files.log mueven la investigación a VirusTotal, y el defanging + base64 cierran el caso con la evidencia exacta.*
**MITRE ATT&CK:** T1048.003 (Exfiltration Over Alternative Protocol - túnel DNS), T1572 (Protocol Tunneling - DNS), T1566.001 (Phishing - Spearphishing Attachment), T1204.002 (User Execution - Malicious File), T1059.005 (Command and Scripting Interpreter - VBA), T1105 (Ingress Tool Transfer - knr.exe), T1190 (Exploit Public-Facing Application - Log4Shell), T1059.007 (Command and Scripting Interpreter - JS/JNDI base64), T1071.001 (Application Layer Protocol: Web).
**Fuente:** [TryHackMe - Zeek Exercises](https://tryhackme.com/room/zeekexercises)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.