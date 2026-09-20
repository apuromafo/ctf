# Carnage
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `carnage` |
| **Link** | [TryHackMe](https://tryhackme.com/room/carnage) |
| **Sección** | SOC / Malware Traffic Analysis |
| **Fuente** | Writeup de 4p3Ir0n (GitHub) |
| **Componentes** | Wireshark, ppcap, phishing (Word "Enable Content"), HTTP downloads (documents.zip, chart-1530076591.xls), LiteSpeed/PHP 7.2.34, Cobalt Strike C2 (185.106.96.158, 185.125.204.174), GoDaddy, OCSP (ocsp.verisign.com), post-infection (maldivehost.net), api.ipify.org, SMTP malspam (farshin@mailfa.com), análisis de tráfico/IOCs |
| **Impacto** | Sala Medium de malware traffic analysis: volcar el pcap en Wireshark y reconstruir todo el incidente — cadena de malspam/phishing, descargas maliciosas, servidores Cobalt Strike, tráfico post-infección y malspam SMTP de salida — contestando 20 preguntas de IOC extremos. |
---
**Contexto:** Sociedad, forense de red puro. El empleado Eric Fischer (Bartell Ltd) abrió un Word adjunto de un contacto conocido y activó "Enable Content"; el agente de endpoint alertó de conexiones sospechosas y se entregó el pcap al SOC. Con Wireshark se identifica el primer HTTP al IP malicioso (2021-09-24 16:44:38), la descarga de `documents.zip` desde `attirenepal.com` (LiteSpeed/PHP 7.2.34) que contiene `chart-1530076591.xls`, tres dominios adicionales de descarga, dos C2 de Cobalt Strike (185.106.96.158 y 185.125.204.174), tráfico post-infección hacia `maldivehost.net`, el check de IP pública (`api.ipify.org`) y finalmente spam mail de salida con MAIL FROM `farshin@mailfa.com`. Pcap cortesía de Brad Duncan.
*EN: Pure network forensics room. Employee Eric Fischer (Bartell Ltd) opened an attached Word doc from a known contact and clicked "Enable Content"; the endpoint agent alerted on suspicious connections and the pcap was handed to the SOC. With Wireshark, the first HTTP to the malicious IP is identified (2021-09-24 16:44:38), the download of `documents.zip` from `attirenepal.com` (LiteSpeed/PHP 7.2.34) containing `chart-1530076591.xls`, three additional download domains, two Cobalt Strike C2 servers (185.106.96.158 and 185.125.204.174), post-infection traffic to `maldivehost.net`, the public-IP check (`api.ipify.org`) and finally outbound malspam with MAIL FROM `farshin@mailfa.com`. Pcap courtesy of Brad Duncan.*
## Solucionario
### Task 1 — Deploy the Machine & Wireshark
**Explicación:** Desplegar la máquina y cargar el pcap de la carpeta Analysis del Desktop en Wireshark. Para responder los timestamps: View → Time Display Format → Date and Time of the day. Pregunta de preparación, sin respuesta.
*EN: Deploy the machine and load the pcap from the Analysis folder on the Desktop into Wireshark. To answer timestamps: View → Time Display Format → Date and Time of the day. Preparation step, no answer needed.*
### Task 2 — Initial Access (HTTP)
**Explicación:** Con `http.request`, ordenando por tiempo, se obtiene la primera conexión HTTP al IP malicioso. Sobre ese stream se identifican el zip descargado, el dominio que lo sirve, el archivo interno sin descargarlo y el servidor web. El XLS con formula "chart-1530076591.xls" es el siguiente eslabón.
*EN: Using `http.request`, sorted by time, the first HTTP connection to the malicious IP is obtained. On that stream, the downloaded zip, the serving domain, the inner file (without downloading it) and the web server are identified. The XLS named `chart-1530076591.xls` is the next link.*

```bash
# Filtros Wireshark
http.request
# Seguir stream HTTP para ver Server header y nombre de archivo.
```
### Task 3 — Second-Stage Downloads
**Explicación:** Ventana de tiempo 16:45:11–16:45:30 con `dns` para enumerar los dominios desde los que el host víctima baja payloads adicionales: `finejewels.com.au`, `thietbiagt.com`, `new.americold.com`. El primero presenta un certificado emitido por GoDaddy (seguir tcp.stream de su flujo).
*EN: Time window 16:45:11–16:45:30 with `dns` to enumerate the domains from which the victim host downloads additional payloads: `finejewels.com.au`, `thietbiagt.com`, `new.americold.com`. The first one presents a certificate issued by GoDaddy (follow its tcp.stream).*

```bash
dns && (frame.time >= "Sep 24, 2021 16:45:11") && (frame.time <= "Sep 24, 2021 16:45:30")
tcp.stream eq 90
```
### Task 4 — Cobalt Strike C2
**Explicación:** Con Statistics → Conversations ordenado por bytes se encuentran IPs externas que el host víctima contacta. Confirmadas en VirusTotal como C2 de Cobalt Strike: `185.106.96.158` y `185.125.204.174`. Para la primera, el Host header de su stream es `ocsp.verisign.com` y su dominio (passive DNS vía AlienVault OTX) es `survmeter.live`; para la segunda, `securitybusinpuff.com`.
*EN: Using Statistics → Conversations sorted by bytes, the external IPs the victim contacts are found. Confirmed on VirusTotal as Cobalt Strike C2: `185.106.96.158` and `185.125.204.174`. For the first one, the Host header of its stream is `ocsp.verisign.com` and its domain (passive DNS via AlienVault OTX) is `survmeter.live`; for the second, `securitybusinpuff.com`.*

```bash
ip.addr == 185.106.96.158     # seguir TCP stream -> Host: ocsp.verisign.com
ip.addr == 185.125.204.174    # dominio C2 -> securitybusinpuff.com
```
### Task 5 — Post-Infection Traffic
**Explicación:** El tráfico post-infección viaja por HTTP POST; siguiendo el stream se obtiene el dominio `maldivehost.net`. Los 11 primeros caracteres que el host víctima envía a ese dominio malicioso son `zLIisQRWZI9`, y el primer paquete hacia el C2 mide 281 bytes. El Server header del dominio es Apache/2.4.49 (cPanel) con mod_bwlimited (banner vulnerable, CVE-2021-41773). La máquina consulta `api.ipify.org` (check de IP) el 2021-09-24 17:00:04; y para cerrar, actividad malspam SMTP: el primer MAIL FROM es `farshin@mailfa.com` y el número total de paquetes SMTP observados, 1439.
*EN: Post-infection traffic travels over HTTP POST; following the stream yields the domain `maldivehost.net`. The first 11 characters the victim host sends to that malicious domain are `zLIisQRWZI9`, and the first packet to the C2 is 281 bytes long. The Server header of the domain is Apache/2.4.49 (cPanel) with mod_bwlimited (vulnerable banner, CVE-2021-41773). The machine queries `api.ipify.org` (IP check) on 2021-09-24 17:00:04; and to round out, SMTP malspam activity: the first MAIL FROM is `farshin@mailfa.com` and the total number of observed SMTP packets is 1439.*

```bash
http.request.method == "POST"            # seguir stream -> maldivehost.net
frame contains "zLIisQRWZI9"             # 11 primeros caracteres enviados
ip.addr == 10.9.23.102 && frame contains "api" && dns   # api.ipify.org
smtp + seguir tcp stream                 # MAIL FROM: farshin@mailfa.com
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What was the date and time for the first HTTP connection to the malicious IP? (answer format: yyyy-mm-dd hh:mm:ss) | `2021-09-24 16:44:38` |
| 2 | What is the name of the zip file that was downloaded? | `documents.zip` |
| 3 | What was the domain hosting the malicious zip file? | `attirenepal.com` |
| 4 | Without downloading the file, what is the name of the file in the zip file? | `chart-1530076591.xls` |
| 5 | What is the name of the webserver of the malicious IP from which the zip file was downloaded? | `LiteSpeed` |
| 6 | What is the version of the webserver from the previous question? | `PHP/7.2.34` |
| 7 | Malicious files were downloaded to the victim host from multiple domains. What were the three domains involved with this activity? | `finejewels.com.au, thietbiagt.com, new.americold.com` |
| 8 | Which certificate authority issued the SSL certificate to the first domain from the previous question? | `GoDaddy` |
| 9 | What are the two IP addresses of the Cobalt Strike servers? (answer format: enter the IP addresses in sequential order) | `185.106.96.158, 185.125.204.174` |
| 10 | What is the Host header for the first Cobalt Strike IP address from the previous question? | `ocsp.verisign.com` |
| 11 | What is the domain name for the first IP address of the Cobalt Strike server? | `survmeter.live` |
| 12 | What is the domain name of the second Cobalt Strike server IP? | `securitybusinpuff.com` |
| 13 | What is the domain name of the post-infection traffic? | `maldivehost.net` |
| 14 | What are the first eleven characters that the victim host sends out to the malicious domain involved in the post-infection traffic? | `zLIisQRWZI9` |
| 15 | What was the length for the first packet sent out to the C2 server? | `281` |
| 16 | What was the Server header for the malicious domain from the previous question? | `Apache/2.4.49 (cPanel) OpenSSL/1.1.1l mod_bwlimited/1.4` |
| 17 | The malware used an API to check for the IP address of the victim's machine. What was the date and time when the DNS query for the IP check domain occurred? (answer format: yyyy-mm-dd hh:mm:ss UTC) | `2021-09-24 17:00:04` |
| 18 | What was the domain in the DNS query from the previous question? | `api.ipify.org` |
| 19 | Looks like there was some malicious spam (malspam) activity going on. What was the first MAIL FROM address observed in the traffic? | `farshin@mailfa.com` |
| 20 | How many packets were observed for the SMTP traffic? | `1439` |
---
**Metodología:** Wireshark → filtrar `http.request` → primer contacto y descarga del zip → dominios de 2ª etapa por DNS (ventana temporal) → Conversations por bytes → confirmar C2 en VirusTotal → Host header y passive DNS (AlienVault OTX) → tráfico POST post-infección y tamaños de paquete → API de IP (DNS) → malspam SMTP (MAIL FROM y conteo) → 20 respuestas.
**Learning chain:** phishing Word → Get zip (documents.zip/attirenepal.com) → XLS dropper → 3 dominios de descarga → Cobalt Strike C2 (2 IPs) → OCSP/verisign como encubrimiento → post-infección (maldivehost.net, zLIisQRWZI9, 281) → banners Apache vulnerables → ipify (oexfiltración de IP) → SMTP malspam (farshin@mailfa.com, 1439 pkts).
**Lección:** *En un pcap, la cadena no se explica sola: se siguen los streams, se ordenan por tiempo, se cruzan IPs con Intel (VirusTotal/OTX) y se distinguen los canales reales de comando (HTTP POST) de los decorativos (OCSP). El "Enable Content" del usuario fue el único vector inicial; la detección llegó por red, no por el host.*
**MITRE ATT&CK:** T1566.001 (Phishing - Spearphishing Attachment), T1204.002 (User Execution - Malicious File), T1105 (Ingress Tool Transfer), T1071.001 (Web Protocols), T1071.003 (Mail Protocols - SMTP), T1573.001 (Encrypted Channel), T1041 (Exfiltration Over C2), T1020 (Automated Exfiltration).
**Fuente:** [TryHackMe - Carnage](https://tryhackme.com/room/carnage)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.