# Network Discovery - Scan-ta Clause [EASY]

### Información de la Sala / Room Information

| Propiedad / Property | Valor / Value |
| --- | --- |
| **Nombre / Name** | Network Discovery - Scan-ta Clause |
| **Evento / Event** | Advent of Cyber 2025 — Día 07 |
| **Sala / Room URL** | https://tryhackme.com/room/adventofcyber25 |
| **Dificultad / Difficulty** | Easy |
| **Descripción / Description** | Día 07 del calendario AoC 2025 (Network Discovery - Scan-ta Clause). Solución/respuestas del reto diario. |

---


- nmap: port scanning
- 22 -> default SSH port
- netcat: to manually interact with network services
- `dns` port: protocol that connects domain names to IP addresses
- 3306 port -> MySQL database management system  

## Comandos Nmap / Nmap commands
- `nmap -sn <network>` : tells us which machines are live
- `nmap <ip>` : scans the specified host for open ports
- `nmap -p <port> <ip>`: scans specified port

## Protocolos de transporte / Transport protocols 
- TCP(Transmission Control Protocol): used in case of web browsing, email, file transfer, SSH; connection based 
- UDP(User Datagram Protocol): is connectionless

## Netcat / Netcat
- `nc <ip> <port>` : connects to service 

## Respuestas / Answers:
- What evil message do you see on top of the website? : `Pwned by HopSec`
- What is the first key part found on the FTP server? : `3aster_`
- What is the second key part found in the TBFC app? : `15_th3_`
- What is the third key part found in the DNS records? : `n3w_xm45`
- Which port was the MySQL database running on? : `3306`
- Finally, what's the flag you found in the database? : `THM{4ll_s3rvice5_d1sc0vered}`

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
