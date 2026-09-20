# Network Discovery - Scan-ta Clause

| **Dificultad** | Easy | **Tipo** | CTF (Free Room) | **Slug** | `day07networkdiscoveryscantaclause` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) | | **Sección** | Advent of Cyber Tryhackme | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | Nmap / Netcat / Networking / DNS / FTP / MySQL / Enumeration | | **Impacto** | Día 07 del AoC 2025: descubrimiento de red y servicios (nmap, netcat) para componer la flag con las partes de la web, FTP, la app TBFC y los registros DNS |

---

**Contexto:** Día 07 del calendario Advent of Cyber 2025 ("Network Discovery - Scan-ta Clause"). Reto de reconocimiento de red: uso de nmap y netcat para descubrir servicios (SSH en 22, MySQL en 3306, DNS, FTP y web); las partes de la flag se consiguen desde la web (mensaje del atacante), el servidor FTP, la app TBFC (API) y los registros DNS, componiendo `Easter_is_the_new_Xmas`. Documento original bilingüe (ES/EN); se conservan apuntes y respuestas verbatim.

---

## Solucionario

### Día 07: Network Discovery - Scan-ta Clause

**Explicación:** Apuntes del laboratorio (notas bilingües originales):

- nmap: port scanning
- 22 -> default SSH port
- netcat: to manually interact with network services
- `dns` port: protocol that connects domain names to IP addresses
- 3306 port -> MySQL database management system

**Comandos Nmap / Nmap commands**

- `nmap -sn <network>` : tells us which machines are live
- `nmap <ip>` : scans the specified host for open ports
- `nmap -p <port> <ip>`: scans specified port

**Protocolos de transporte / Transport protocols**

- TCP (Transmission Control Protocol): used in case of web browsing, email, file transfer, SSH; connection based
- UDP (User Datagram Protocol): is connectionless

**Netcat / Netcat**

- `nc <ip> <port>` : connects to service

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What evil message do you see on top of the website? | `Pwned by HopSec` |
| 2 | What is the first key part found on the FTP server? | `3aster_` |
| 3 | What is the second key part found in the TBFC app? | `15_th3_` |
| 4 | What is the third key part found in the DNS records? | `n3w_xm45` |
| 5 | Which port was the MySQL database running on? | `3306` |
| 6 | Finally, what's the flag you found in the database? | `THM{4ll_s3rvice5_d1sc0vered}` |

---

**Metodología:**

1. Escaneo de puertos del target (`nmap`) y conexión manual a servicios con `nc`

2. Recopilación de las partes de la flag en web, FTP, app TBFC y DNS

3. Acceso a la base de datos MySQL (puerto 3306) para leer la flag final

**Learning chain:** nmap scan -> Service discovery (FTP/DNS/TBFC) -> MySQL database

**Lección:** *El descubrimiento de red (nmap + netcat) revela servicios como FTP, DNS y MySQL; las flags pueden estar repartidas en distintas partes de la infraestructura y hay que componerlas siguiendo el orden de la cadena.*

**MITRE ATT&CK:**

- T1046 - Network Service Discovery

- T1595.001 - Active Scanning: Scanning IP Blocks

- T1049 - System Network Connections Discovery

- T1078 - Valid Accounts (acceso a datos/servicios descubiertos)

**Fuente:** [TryHackMe - Network Discovery - Scan-ta Clause](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.