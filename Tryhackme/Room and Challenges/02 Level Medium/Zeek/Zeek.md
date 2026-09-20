# Zeek
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `zeek` |
| **Link** | [TryHackMe](https://tryhackme.com/room/zeek) |
| **Sección** | SOC Level 1 / Traffic Analysis |
| **Fuente** | TryHackMe - Zeek (https://tryhackme.com/room/zeek) |
| **Componentes** | Zeek (Bro), ZeekControl, zeek-cut, logs (conn.log, dhcp.log, dns.log, http.log, files.log, intel.log, notice.log, signatures.log, loaded_scripts.log), firmas `.sig` (http-password, ftp-admin/ftp-brute), scripts `.zeek` (103, 201, hash-demo, file-extract, intelligence-demo, sumstats-counttable), frameworks (Intel, File Analysis, extracción de ficheros), paquetes zkg (zeek-sniffpass, geoip-conn), pcaps (sample.pcap, http.pcap, ftp.pcap, smallFlows.pcap, bigFlows.pcap, case1.pcap, case2.pcap, ftp-brute.pcap) |
| **Impacto** | Sala Medium del path SOC Level 1: hands-on de monitorización de tráfico y detección de amenazas con Zeek (antes Bro) — arquitectura, ZeekControl, logs y zeek-cut, CLI Kung-Fu, firmas `.sig`, scripting `.zeek`, frameworks (Intel/File Analysis/extract_files) y paquetes zkg (sniffpass, geoip) — sobre capturas reales: credenciales en claro, brute-force FTP, descargas de malware y actividad C2/DNS. |

---
**Contexto:** Zeek (antes Bro) es un analizador de tráfico de red open-source y comercial, originalmente creado por Lawrence Berkeley Labs, que actúa como Network Security Monitor (NSM). A diferencia de un IDS clásico como Snort (basado únicamente en firmas y payloads), Zeek genera 50+ logs estructurados en 7 categorías y dispone de un lenguaje de scripting orientado a eventos para correlacionar y detectar amenazas complejas. En esta sala se recorre su arquitectura (Event Engine + Policy Script Interpreter), la gestión del servicio con ZeekControl, la lectura y extracción de campos con zeek-cut, la escritura de firmas `.sig` y scripts `.zeek`, y el uso de frameworks (Intel, File Analysis, extracción de ficheros) y paquetes zkg. Todo se aplica sobre capturas reales: credenciales HTTP en claro, brute-force FTP, descargas de malware y actividad C2/DNS.
*EN: Zeek (formerly Bro) is an open-source and commercial network traffic analyser, originally created by Lawrence Berkeley Labs, acting as a Network Security Monitor (NSM). Unlike classic IDS such as Snort (based only on signatures and payloads), Zeek generates 50+ structured logs in 7 categories and has an event-driven scripting language to correlate and detect complex threats. This room covers its architecture (Event Engine + Policy Script Interpreter), service management with ZeekControl, log reading and field extraction with zeek-cut, writing `.sig` signatures and `.zeek` scripts, and using frameworks (Intel, File Analysis, file extraction) and zkg packages. All applied to real captures: cleartext HTTP credentials, FTP brute-force, malware downloads and C2/DNS activity.*

## Solucionario
### Task 1 — Introducción / Introduction
**Explicación:** Presentación de la sala: Zeek (antes Bro) es la plataforma líder de monitorización de seguridad de red (NSM), pasiva, open-source y con edición comercial (Corelight). Se recomienda tener conocimiento básico de Linux y fundamentos de redes (path Network Fundamentals). La máquina del room se opera con la vista "Split View" (no SSH/RDP) y los ficheros de ejercicios se encuentran en el escritorio; cada carpeta de tarea incluye un script `clear-logs.sh`. No hay pregunta práctica.
*EN: Room introduction: Zeek (formerly Bro) is the leading network security monitoring (NSM) platform, passive, open-source and with a commercial edition (Corelight). Basic Linux and network fundamentals are recommended (Network Fundamentals path). The room machine is operated via "Split View" (no SSH/RDP) and the exercise files are on the desktop; each task folder includes a `clear-logs.sh` script. No hands-on question.*
```text
1. No answer needed
```

### Task 2 — Monitorización de Red y Zeek / Network Security Monitoring and Zeek
**Explicación:** Distingue Network Monitoring (estado de assets IT) frente a Network Security Monitoring (anomalías y sospechas en el tráfico, dentro del SOC) y describe la arquitectura de Zeek: capa "Event Engine" (procesa paquetes y los divide en sesiones) y capa "Policy Script Interpreter" (correlación semántica con scripts), además de sus frameworks (Logging, File Analysis, Intel, Notice, GeoLocation, etc.) y las salidas por defecto (50+ logs, 7 categorías, ubicación `/opt/zeek/logs/`). En la parte práctica se comprueba la versión instalada con `zeek -v` (4.2.1), la versión del módulo ZeekControl con `zeekctl` (2.4.0) y, tras procesar `sample.pcap` con `zeek -C -r`, el número de logs generados (8).
*EN: Distinguishes Network Monitoring (IT asset health) from Network Security Monitoring (traffic anomalies, within the SOC) and describes Zeek's architecture: the "Event Engine" layer (processes packets and splits them into sessions) and the "Policy Script Interpreter" layer (semantic correlation using scripts), plus its frameworks (Logging, File Analysis, Intel, Notice, GeoLocation, etc.) and default outputs (50+ logs, 7 categories, stored in `/opt/zeek/logs/`). Practically you check the installed version with `zeek -v` (4.2.1), the ZeekControl module version with `zeekctl` (2.4.0) and, after processing `sample.pcap` with `zeek -C -r`, the number of generated logs (8).*
```bash
zeek -v
zeekctl
zeek -C -r sample.pcap
ls -la
ls -1 *.log | wc -l
```
```text
1. No answer needed
2. 4.2.1
3. 2.4.0
4. 8
```

### Task 3 — Logs de Zeek / Zeek Logs
**Explicación:** Presenta la estructura tabular de los logs de Zeek (campos tipados separados por tabulador), las 7 categorías de logs (Network, Files, NetControl, Detection, Network Observations, Miscellaneous, Zeek Diagnostic) y el auxiliar `zeek-cut` para extraer columnas concretas usando los nombres de campo del propio log. Los ejercicios procesan `sample.pcap`: el `host_name` del dhcp.log (Microknoppix), el número de consultas DNS únicas del dns.log (2) y la duración más larga de conexión del conn.log (332.319364).
*EN: Presents the tabular structure of Zeek logs (typed fields separated by tabs), the 7 log categories (Network, Files, NetControl, Detection, Network Observations, Miscellaneous, Zeek Diagnostic) and the `zeek-cut` helper to extract specific columns using the field names from the log itself. The exercises process `sample.pcap`: the `host_name` of dhcp.log (Microknoppix), the number of unique DNS queries in dns.log (2) and the longest connection duration in conn.log (332.319364).*
```bash
zeek -C -r sample.pcap
cat dhcp.log | zeek-cut host_name
cat dns.log | zeek-cut query | sort -u | wc -l
cat conn.log | zeek-cut duration | sort -rn | head
```
```text
1. No answer needed
2. Microknoppix
3. 2
4. 332.319364
```

### Task 4 — Repaso de CLI: procesar logs de Zeek / CLI Kung-Fu Recall: Processing Zeek Logs
**Explicación:** Cheat-sheet de comandos CLI esenciales para tratar los logs tabulados de Zeek: `cat`, `head`, `tail`, `cut -f`, `grep`, `sort -n/-nr`, `uniq`/`uniq -c`, `wc -l`, `nl`, `sed`, `awk`, `rev`, `column -t` y `zeek-cut`, incluyendo el manejo de `history` (`!10`, `!!`) y la combinación `grep -rin <valor> * | column -t | less -S`. Tarea de lectura únicamente, sin preguntas prácticas.
*EN: Cheat-sheet of essential CLI commands for Zeek tab-separated logs: `cat`, `head`, `tail`, `cut -f`, `grep`, `sort -n/-nr`, `uniq`/`uniq -c`, `wc -l`, `nl`, `sed`, `awk`, `rev`, `column -t` and `zeek-cut`, including `history` usage (`!10`, `!!`) and the combination `grep -rin <value> * | column -t | less -S`. Reading-only task, no hands-on questions.*
```text
1. No answer needed
```

### Task 5 — Firmas de Zeek / Zeek Signatures
**Explicación:** Introducción al formato de firmas `.sig` de Zeek, compuestas por signature id, condiciones (Header: `src-ip`, `dst-ip`, `src-port`, `dst-port`, `ip-proto`; Content: `payload`, `http-request`, `http-request-header/body`, `http-reply-header/body`, `ftp`; Context: `same-ip`) y action (`event`). Las firmas se ejecutan con `zeek -C -r <pcap> -s <firma>.sig` y los matches generan `signatures.log` y `notice.log`. En la práctica se escriben la firma HTTP de credenciales en claro (`http-password`), la firma FTP de brute-force global (`ftp-username` + `ftp-brute`), y se extraen la IP y puertos de los eventos, el total de paquetes enviados/recibidos del puerto 38706 y los recuentos del notice.log/signatures.log.
*EN: Introduces Zeek's `.sig` signature format, composed of signature id, conditions (Header: `src-ip`, `dst-ip`, `src-port`, `dst-port`, `ip-proto`; Content: `payload`, `http-request`, `http-request-header/body`, `http-reply-header/body`, `ftp`; Context: `same-ip`) and action (`event`). Signatures run with `zeek -C -r <pcap> -s <signature>.sig` and matches generate `signatures.log` and `notice.log`. In practice you write the cleartext-credentials HTTP signature (`http-password`) and the global FTP brute-force signature (`ftp-username` + `ftp-brute`), then extract the event IP and ports, the total packets sent/received from port 38706 and the notice.log/signatures.log counts.*
```bash
zeek -C -r http.pcap -s http-password.sig
cat signatures.log | zeek-cut src_addr src_port
cat conn.log | zeek-cut id.orig_p orig_pkts resp_pkts | grep 38706
zeek -C -r ftp.pcap -s ftp-bruteforce.sig
cat notice.log | zeek-cut uid | sort -u | wc -l
cat signatures.log | zeek-cut event_msg | grep 'FTP Brute-force' | wc -l
```
```text
1. No answer needed
2. 10.10.57.178
3. 38712
4. 20
5. 1413
6. 1410
```

### Task 6 — Scripts de Zeek | Fundamentos / Zeek Scripts | Fundamentals
**Explicación:** Zeek usa un lenguaje de scripting orientado a eventos (extension `.zeek`). Los scripts base residen en `/opt/zeek/share/zeek/base` (no deben modificarse), los de política en `/opt/zeek/share/zeek/policy`, y los del usuario en `/opt/zeek/share/zeek/site/local.zeek`; pueden cargarse con `@load` y pasar como argumento a `zeek`. Como ejemplo se escribe un evento `dhcp_message` que imprime el `host_name`. En los ejercicios se analizan smallFlows.pcap y bigFlows.pcap: el dominio del host "vinlap01" (astaro_vineyard), el número de hostnames únicos en el dhcp.log (17) y el dominio identificado (jaalam.net).
*EN: Zeek uses an event-driven scripting language (`.zeek` files). Base scripts live in `/opt/zeek/share/zeek/base` (never modify them), policy scripts in `/opt/zeek/share/zeek/policy`, and user scripts in `/opt/zeek/share/zeek/site/local.zeek`; they can be loaded with `@load` and passed as arguments to `zeek`. As an example a `dhcp_message` event is written to print the `host_name`. The exercises analyse smallFlows.pcap and bigFlows.pcap: the domain of the "vinlap01" host (astaro_vineyard), the number of unique hostnames in dhcp.log (17) and the identified domain (jaalam.net).*
```bash
zeek -C -r smallFlows.pcap dhcp-hostname.zeek
cat dhcp.log | zeek-cut host_name domain
zeek -C -r bigFlows.pcap
cat dhcp.log | zeek-cut host_name | sort -nr | uniq | wc -l
cat dhcp.log | zeek-cut domain | sort | uniq
```
```text
1. No answer needed
2. astaro_vineyard
3. 17
4. jaalam.net
```

### Task 7 — Scripts de Zeek | Scripts y Firmas / Zeek Scripts | Scripts and Signatures
**Explicación:** Combina scripting y firmas: el script `103.zeek` reacciona al evento `new_connection` e imprime información de cada nueva conexión; `201.zeek` escucha `signature_match` y cuenta hits de la firma `ftp-admin`; el comando automágico `local` carga todos los scripts locales de Zeek (cuantificados en `loaded_scripts.log`); y el script de política `/opt/zeek/share/zeek/policy/protocols/ftp/detect-bruteforcing.zeek` detecta brute-force FTP vía `notice.log`. En la práctica: nuevas conexiones detectadas (87), hits de firma (1401), detecciones del usuario "administrator" (731), scripts cargados (498) y detecciones de brute-force (2).
*EN: Combines scripting and signatures: `103.zeek` reacts to the `new_connection` event and prints information about every new connection; `201.zeek` listens to `signature_match` and counts hits of the `ftp-admin` signature; the `local` convenience command loads all local Zeek scripts (counted in `loaded_scripts.log`); and the policy script `/opt/zeek/share/zeek/policy/protocols/ftp/detect-bruteforcing.zeek` detects FTP brute-force via `notice.log`. In practice: detected new connections (87), signature hits (1401), "administrator" user detections (731), loaded scripts (498) and brute-force detections (2).*
```bash
zeek -C -r sample.pcap 103.zeek | grep 'New Connection' | wc -l
zeek -C -r ftp.pcap -s ftp-admin.sig 201.zeek | wc -l
cat signatures.log | zeek-cut sub_msg | grep administrator | wc -l
zeek -C -r ftp.pcap local
cat loaded_scripts.log | zeek-cut name | wc -l
zeek -C -r ftp-brute.pcap /opt/zeek/share/zeek/policy/protocols/ftp/detect-bruteforcing.zeek
cat notice.log | zeek-cut msg | wc -l
```
```text
1. No answer needed
2. 87
3. 1401
4. 731
5. 498
6. 2
```

### Task 8 — Scripts de Zeek | Frameworks
**Explicación:** Carga de frameworks de Zeek con `@load`. El framework File Analysis permite (a) el hasheo de ficheros con `hash-all-files.zeek` (MD5/SHA1/SHA256 en `files.log`) y (b) la extracción de ficheros con `extract-all-files.zeek` (carpeta `extract_files/`). El framework Intelligence genera `intel.log` a partir de un feed tabulado (`/opt/zeek/intel/zeek_intel.txt`) con el script `intelligence-demo.zeek`. Sobre `case1.pcap`: dónde se detectó el intel en el segundo hallazgo (HTTP::IN_HOST_HEADER), el nombre del `.exe` descargado (knr.exe), su hash MD5 en `files.log` (cc28e40b46237ab6d5282199ef78c464) y el contenido del fichero de texto extraído (Microsoft NCSI).
*EN: Loads Zeek frameworks with `@load`. The File Analysis framework allows (a) hashing files with `hash-all-files.zeek` (MD5/SHA1/SHA256 in `files.log`) and (b) extracting files with `extract-all-files.zeek` (`extract_files/` folder). The Intelligence framework generates `intel.log` from a tab-delimited feed (`/opt/zeek/intel/zeek_intel.txt`) with the `intelligence-demo.zeek` script. On `case1.pcap`: where the intel was seen in the second finding (HTTP::IN_HOST_HEADER), the name of the downloaded `.exe` (knr.exe), its MD5 in `files.log` (cc28e40b46237ab6d5282199ef78c464) and the content of the extracted text file (Microsoft NCSI).*
```bash
zeek -C -r case1.pcap /opt/zeek/share/zeek/policy/frameworks/files/hash-all-files.zeek
zeek -C -r case1.pcap /opt/zeek/share/zeek/policy/frameworks/files/extract-all-files.zeek
zeek -C -r case1.pcap intelligence-demo.zeek
head intel.log | zeek-cut seen.indicator seen.where
cat http.log | zeek-cut uri orig_filenames resp_mime_types
cat files.log | zeek-cut fuid filename mime_type md5
cd extract_files
file *
cat extract-1561667874.743959-HTTP-Fpgan59p6uvNzLFja ; echo
```
```text
1. No answer needed
2. IN_HOST_HEADER
3. knr.exe
4. cc28e40b46237ab6d5282199ef78c464
5. Microsoft NCSI
```

### Task 9 — Scripts de Zeek | Paquetes / Zeek Scripts | Packages
**Explicación:** El Zeek Package Manager (`zkg`) instala, lista, elimina y actualiza paquetes de terceros (se requieren privilegios root). Los paquetes se invocan por script (`@load`), por ruta o por nombre. Como demostración se instalan e usan dos paquetes: `zeek-sniffpass` (detecta contraseñas en claro en HTTP POST y notifica en `notice.log`) y `geoip-conn` (geolocalización de IPs en `conn.log` usando la BD GeoLite2-City). Sobre http.pcap y case2.pcap: usuario con más hits del módulo (BroZeek), ciudad identificada (Chicago), IP asociada (23.77.86.54) y número de códigos de estado en el tráfico con `sumstats-counttable.zeek` (4).
*EN: The Zeek Package Manager (`zkg`) installs, lists, removes and updates third-party packages (root privileges required). Packages are invoked via script (`@load`), by path or by name. Two packages are installed and used as a demo: `zeek-sniffpass` (detects cleartext passwords in HTTP POST and notifies in `notice.log`) and `geoip-conn` (IP geolocation in `conn.log` using the GeoLite2-City DB). On http.pcap and case2.pcap: the username with more module hits (BroZeek), the identified city (Chicago), the associated IP (23.77.86.54) and the number of status codes in the traffic with `sumstats-counttable.zeek` (4).*
```bash
zkg install zeek/cybera/zeek-sniffpass
zkg list
zeek -C -r http.pcap zeek-sniffpass
cat notice.log | zeek-cut msg | sort | uniq -c | sort -rn
zeek -C -r case2.pcap geoip-conn
head conn.log | zeek-cut geo.orig.city geo.resp.city id.resp_h
zeek -C -r case2.pcap sumstats-counttable.zeek | grep 'status code' | cut -d':' -f2 | cut -d',' -f1 | sort -u | wc -l
```
```text
1. No answer needed
2. BroZeek
3. Chicago
4. 23.77.86.54
5. 4
```

### Task 10 — Conclusión / Conclusion
**Explicación:** Cierre de la sala: resumen de qué es Zeek, cómo opera y cómo usarlo para investigar amenazas, con invitación a practicar en el room Zeek Exercises y referencias a la documentación oficial. No hay pregunta práctica.
*EN: Room wrap-up: summary of what Zeek is, how it operates and how to use it to investigate threats, plus an invitation to practice in the Zeek Exercises room and references to the official docs. No hands-on question.*
```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
| 2 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
| 3 | What is the installed Zeek instance version number? | `4.2.1` |
| 4 | What is the version of the ZeekControl module? | `2.4.0` |
| 5 | Investigate the "sample.pcap" file. What is the number of generated alert files? | `8` |
| 6 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
| 7 | Investigate the sample.pcap file. Investigate the dhcp.log file. What is the available hostname? | `Microknoppix` |
| 8 | Investigate the dns.log file. What is the number of unique DNS queries? | `2` |
| 9 | Investigate the conn.log file. What is the longest connection duration? | `332.319364` |
| 10 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
| 11 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
| 12 | Investigate the http.pcap file. Create the HTTP signature shown in the task and investigate the pcap. What is the source IP of the first event? | `10.10.57.178` |
| 13 | What is the source port of the second event? | `38712` |
| 14 | Investigate the conn.log. What is the total number of the sent and received packets from source port 38706? | `20` |
| 15 | Create the global rule shown in the task and investigate the ftp.pcap file. Investigate the notice.log. What is the number of unique events? | `1413` |
| 16 | What is the number of ftp-brute signature matches? | `1410` |
| 17 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
| 18 | Investigate the smallFlows.pcap file. Investigate the dhcp.log file. What is the domain value of the "vinlap01" host? | `astaro_vineyard` |
| 19 | Investigate the bigFlows.pcap file. Investigate the dhcp.log file. What is the number of identified unique hostnames? | `17` |
| 20 | Investigate the dhcp.log file. What is the identified domain value? | `jaalam.net` |
| 21 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
| 22 | Investigate the sample.pcap file with 103.zeek script. Investigate the terminal output. What is the number of the detected new connections? | `87` |
| 23 | Investigate the ftp.pcap file with ftp-admin.sig signature and 201.zeek script. Investigate the signatures.log file. What is the number of signature hits? | `1401` |
| 24 | Investigate the signatures.log file. What is the total number of "administrator" username detections? | `731` |
| 25 | Investigate the ftp.pcap file with all local scripts, and investigate the loaded_scripts.log file. What is the total number of loaded scripts? | `498` |
| 26 | What is the total number of brute-force detections? | `2` |
| 27 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
| 28 | Investigate the intel.log file. Look at the second finding, where was the intel info found? | `IN_HOST_HEADER` |
| 29 | Investigate the http.log file. What is the name of the downloaded .exe file? | `knr.exe` |
| 30 | Investigate the files.log file. What is the MD5 hash of the downloaded .exe file? | `cc28e40b46237ab6d5282199ef78c464` |
| 31 | Investigate the "extract_files" folder. Review the contents of the text file. What is written in the file? | `Microsoft NCSI` |
| 32 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
| 33 | Investigate the notice.log file. Which username has more module hits? | `BroZeek` |
| 34 | Investigate the conn.log file. What is the name of the identified City? | `Chicago` |
| 35 | Which IP address is associated with the identified City? | `23.77.86.54` |
| 36 | How many types of status codes are there in the given traffic capture? | `4` |
| 37 | Pregunta de lectura de la tarea (sin respuesta requerida). | `No answer needed` |
---
**Metodología:** Arrancar la VM y comprobar versión/ZeekControl (`zeek -v`, `zeekctl`) → procesar cada captura con `zeek -C -r <pcap>` (añadiendo `-s <firma>.sig`, scripts `.zeek`, frameworks o paquetes según la tarea) → inspeccionar los logs generados (conn, dhcp, dns, http, files, intel, notice, signatures, loaded_scripts) con `zeek-cut` y comandos CLI (cat, head, sort, uniq -c, grep, wc -l) → correlacionar registros por UID/fuids entre logs → cargar frameworks (File Analysis/hash y extraction, Intelligence) y paquetes zkg (sniffpass, geoip) para enriquecer la detección → validar los indicadores (URI, MD5, mensajes de notice/sig).

### Cadena de análisis / Analysis Chain
```text
sample.pcap → zeek -C -r → logs conn/dhcp/dns (8 ficheros) → Microknoppix, 2 queries DNS, dur. máx 332.319364
http.pcap + http-password.sig → credenciales HTTP en claro → src 10.10.57.178:38706/38712 → 20 paquetes en 38706
ftp.pcap + ftp-username/ftp-brute.sig → 1413 eventos únicos en notice.log → 1410 hits ftp-brute
smallFlows.pcap / bigFlows.pcap + dhcp-hostname.zeek → astaro_vineyard, 17 hostnames, jaalam.net
sample.pcap + 103.zeek / ftp.pcap + ftp-admin.sig + 201.zeek → 87 conexiones nuevas, 1401/731 hits, 498 scripts, 2 brute-force
case1.pcap + intelligence-demo.zeek → intel.log (smart-fax.com en IN_HOST_HEADER) → knr.exe (MD5 cc28e40b...) → Microsoft NCSI
http.pcap + zeek-sniffpass → BroZeek (3 hits) | case2.pcap + geoip-conn/sumstats → Chicago (23.77.86.54), 4 status codes
```
**Learning chain:** pcap → logs Zeek (conn, dns, http, files, signatures, notice, loaded_scripts) → zeek-cut + CLI Kung-Fu → firmas `.sig` → scripts `.zeek` → frameworks (Intel/File Analysis/extract_files) → paquetes zkg (sniffpass, geoip) → IoCs y recuentos.
**Lección:** *Zeek brilla cuando dejas de mirar "paquetes sueltos" y pasas a logs estructurados correlacionables: con zeek-cut + Unix (sort/uniq/grep) resuelves los recuentos, y con firmas `.sig`, scripts `.zeek`, frameworks (Intel/File Analysis) y paquetes zkg detectas lo que las reglas clásicas de un IDS basado en firmas no ven.*
**MITRE ATT&CK:** T1110 (Brute Force - FTP), T1071.001 (Application Layer Protocol: Web - credenciales en claro), T1105 (Ingress Tool Transfer - knr.exe), T1204.002 (User Execution: Malicious File), T1043 (Commonly Used Port - C2), T1048.003 (Exfiltration Over Alternative Protocol - DNS).
**Fuente:** [TryHackMe - Zeek](https://tryhackme.com/room/zeek)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.