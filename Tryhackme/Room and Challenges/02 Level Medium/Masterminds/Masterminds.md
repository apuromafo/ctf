# Masterminds

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | masterminds |
| **Link** | [TryHackMe](https://tryhackme.com/room/masterminds) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=masterminds` + walkthrough) |
| **Componentes** | Brim (Zeek + Suricata), Wireshark, VirusTotal, URLhaus, OSINT |
| **Impacto** | Medio — análisis forense de red (DFIR): 3 máquinas comprometidas por phishing y USB infectado (Emotet, RedLine Stealer, Phorphiex/Trik) |

---

**Contexto:** Tres máquinas del departamento de Finanzas de Pfeffer PLC fueron comprometidas. El origen sospechado es una campaña de **phishing** y un **USB infectado**. El equipo de IR capturó los logs de tráfico de red de los endpoints y hay que investigarlos con **Brim** (plataforma de análisis basada en Zeek + Suricata) para determinar quién está detrás de los ataques.

**Nota importante de la room:** NO interactuar directamente con los dominios e IPs del challenge (solo hacer OSINT indirecto con VirusTotal/URLhaus y búsquedas entre comillas).

## Solucionario

### Task 1: Detect the compromise using Brim

**Explicación:** Tarea introductoria. Al desplegar la máquina (vista split). Todos los PCAPs están en `/home/ubuntu/Desktop/PCAPs`. Para preguntas con varias respuestas, se separan con **coma**. El reto se resuelve cargando las capturas `Infection1`, `Infection2` e `Infection3` en Brim y usando el lenguaje de consulta de Zeek.

| # | Pregunta | Respuesta |
| 1 | (Confirmación: leer lo anterior) | `No answer needed` |

---

### Task 2: Infection 1

**Explicación:** Análisis de la primera captura. Consultas útiles en Brim:

```
suricata alert "Trojan was detected"
filter: 192.168.75.249 status_code==404
filter: 192.168.75.249 response_body_len==1309
filter: dns query=="CAB.MYKFN.COM"
filter: bhaktivrind.com
filter: _path=="http" host=="hdmilg.xyz"
```

Encuentros clave:
- La víctima (IPs `192.168.75.249`) intentó conectar HTTP con estado **404** a `cambiasuhistoria.growlab.es` y `www.letscompareonline.com`.
- Una conexión con `response_body_len` 1309 (contenido sin comprimir 1.309 bytes) apunta a `ww25.gocphongthe.com` con IP `199.59.242.153`.
- **7** consultas DNS únicas al dominio `cab[.]myfkn[.]com` (incluyendo la versión en mayúsculas).
- El dominio `bhaktivrind[.]com` se contactó por la URI `/cgi-bin/JBbb8/`.
- Desde `hdmilg.xyz` (IP `185.239.243.112`) se descargó el ejecutable `/catzx.exe`.
- Al subir `catzx.exe` a VirusTotal (o consultar la comunidad), el resultado es **Emotet** (informe `malware.me/report/15424`, MD5 `5b86fcaf5ab130c47731cc168a2ca852`).

IOC adicional: el malware comparte similitudes con la cadena Emotet descrita por Sophos ("Emotet 101 — Stage 3, the Emotet executables").

| # | Pregunta | Respuesta |
| 1 | Provide the victim's IP address. | `192.168.75.249` |
| 2 | The victim attempted to make HTTP connections to two suspicious domains with the status '404 Not Found'. Provide the hosts/domains requested. | `cambiasuhistoria.growlab.es,www.letscompareonline.com` |
| 3 | The victim made a successful HTTP connection to one of the domains and received the response_body_len of 1,309. Provide the domain and the destination IP address. | `ww25.gocphongthe.com,199.59.242.153` |
| 4 | How many unique DNS requests were made to cab[.]myfkn[.]com domain (including the capitalized domain)? | `7` |
| 5 | Provide the URI of the domain bhaktivrind[.]com that the victim reached out over HTTP. | `/cgi-bin/JBbb8/` |
| 6 | Provide the IP address of the malicious server and the executable that the victim downloaded from the server. | `185.239.243.112,catzx.exe` |
| 7 | Based on the information gathered from the second question, provide the name of the malware using VirusTotal. | `Emotet` |

---

### Task 3: Infection 2

**Explicación:** Segunda captura (`Infection2`). Consultas clave:

```
filter: event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip
filter: 192.168.75.146 method=="POST"
filter: _path=="dns" | count() by query | sort -r
filter: hypercustom.top
```

Hallazgos:
- Víctima: `192.168.75.146`. Realizó conexiones **POST** a la IP `5.181.156.252` — exactamente **3**.
- Desde el dominio `hypercustom.top` se descargó el binario `/jollion/apines.exe` alojado en `45.95.203.28`.
- Hay **2** alertas Suricata "A Network Trojan was detected" con src/dest `192.168.75.146,45.95.203.28`.
- Consultando URLhaus (`urlhaus.abuse.ch`) por `hypercustom.top`, el stealer es **RedLine Stealer**.

| # | Pregunta | Respuesta |
| 1 | Provide the IP address of the victim machine. | `192.168.75.146` |
| 2 | Provide the IP address the victim made the POST connections to. | `5.181.156.252` |
| 3 | How many POST connections were made to the IP address in the previous question? | `3` |
| 4 | Provide the domain where the binary was downloaded from. | `hypercustom.top` |
| 5 | Provide the name of the binary including the full URI. | `/jollion/apines.exe` |
| 6 | Provide the IP address of the domain that hosts the binary. | `45.95.203.28` |
| 7 | There were 2 Suricata "A Network Trojan was detected" alerts. What were the source and destination IP addresses? | `192.168.75.146,45.95.203.28` |
| 8 | Taking a look at .top domain in HTTP requests, provide the name of the stealer involved in this packet capture using URLhaus Database. | `Redline Stealer` |

---

### Task 4: Infection 3

**Explicación:** Tercera captura (`Infection3`). Consultas clave:

```
filter: event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip
filter: _path=="http" | cut id.orig_h, id.resp_h, id.resp_p, method,host, uri | uniq -c
filter: dns 63.251.106.25
filter: 63.251.106.25 method=="GET" uri!="/s/VNEW=1"
filter: _path=="dns" | count()
```

Hallazgos:
- Víctima: `192.168.75.232`. Tres dominios C2 descargando binarios: `xfhoahegue.ru`, `afhoahegue.ru`, `efhoahegue.ru` con IPs `63.251.106.25`, `199.21.76.77`, `162.217.98.146`.
- **2** queries DNS únicas hacia el dominio asociado a la primera IP, y **5** binarios descargados en total desde ese dominio.
- El user-agent usado para descargar los binarios es `Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0`.
- **986** conexiones DNS en total en la captura.
- OSINT sobre `xfhoahegue.ru` (sin terminar en `.ru`, entre comillas) → **Phorphiex** (worm de la campaña "Phorphiex/Trik Botnet Campaign Leads to Multiple Infections" de AppRiver, relacionado con ransomware, banking trojans y cryptojacking).

| # | Pregunta | Respuesta |
| 1 | Provide the IP address of the victim machine. | `192.168.75.232` |
| 2 | Provide three C2 domains from which the binaries were downloaded (starting from the earliest to the latest in the timestamp) | `efhoahegue.ru,afhoahegue.ru,xfhoahegue.ru` |
| 3 | Provide the IP addresses for all three domains in the previous question. | `162.217.98.146,199.21.76.77,63.251.106.25` |
| 4 | How many unique DNS queries were made to the domain associated from the first IP address from the previous answer? | `2` |
| 5 | How many binaries were downloaded from the above domain in total? | `5` |
| 6 | Provided the user-agent listed to download the binaries. | `Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0` |
| 7 | Provide the amount of DNS connections made in total for this packet capture. | `986` |
| 8 | With some OSINT skills, provide the name of the worm using the first domain you have managed to collect from Question 2. (Use quotation marks, don't use .ru in your search, and DO NOT interact with the domain directly). | `phorphiex` |

---

**Metodología:** DFIR / Análisis de tráfico de red (NIST SP 800-115, fase de análisis): correlación de alertas Suricata y logs Zeek/DNS en Brim, seguimiento del flujo HTTP y DNS de cada víctima y enriquecimiento con OSINT (VirusTotal, URLhaus).

**Learning chain:** Carga de PCAPs en Brim → consultas Zeek (`_path=="http"`, `method=="POST"`, `count() by query`) → filtrado por víctima (status_code, response_body_len, host) → identificación de descargas de binarios y dominios C2 → confirmación del malware con VirusTotal/URLhaus (Emotet → RedLine Stealer → Phorphiex) → reporte de IOCs.

**MITRE ATT&CK:** T1566 – Phishing; T1091 – Replication Through Removable Media (USB infectado); T1071.001 – Application Layer Protocol: Web Protocols (C2); T1105 – Ingress Tool Transfer; T1573.001 – Encrypted Channel: Symmetric Cryptography.

**Fuente:** [TryHackMe - Masterminds](https://tryhackme.com/room/masterminds)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
