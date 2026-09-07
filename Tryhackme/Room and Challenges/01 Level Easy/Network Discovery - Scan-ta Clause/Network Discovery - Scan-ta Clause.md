# Network Discovery - Scan-ta Clause

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `networkservices-aoc2025-jnsoqbxgky` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/networkservices-aoc2025-jnsoqbxgky) |
| **Sección** | Advent of Cyber 2025 |
| **Fuente** | THM |
| **Componentes** | nmap, FTP, netcat, DNS dig, MySQL |
| **Impacto** | Medio — descubrimiento completo de servicios expuestos en la red TBFC permitiendo recopilación de credenciales y datos fragmentados |

---

**Contexto:** En el día 7 de Advent of Cyber 2025, la red de TBFC se ha caído y se requiere realizar reconocimiento de servicios para restaurar las operaciones. Se explora el sitio "Pwned by HopSec" y se emplean herramientas de descubrimiento de red (nmap, netcat, dig, mysql client) para localizar fragmentos de una key distribuida entre FTP, aplicaciones web, registros DNS y una base de datos MySQL.

## Solucionario

### Task 1: Reconocimiento Inicial

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What evil message do you see on top of the website? | `Pwned by HopSec` |

### Task 2: FTP Discovery

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first key part found on the FTP server? | `3aster_` |

### Task 3: Web App Discovery

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the second key part found in the TBFC app? | `15_th3_` |

### Task 4: DNS Discovery

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the third key part found in the DNS records? | `n3w_xm45` |

### Task 5: MySQL Discovery

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which port was the MySQL database running on? | `3306` |
| 2 | Finally, what's the flag you found in the database? | `THM{4ll_s3rvice5_d1sc0vered}` |

---

**Metodología:** Se inició con escaneo de puertos mediante nmap para descubrir servicios activos (FTP, HTTP, DNS, MySQL). Se accedió por FTP para recuperar la primera parte de la key. Se navegó la aplicación web TBFC para obtener la segunda parte. Se consultaron registros DNS con dig para localizar la tercera parte. Finalmente, se conectó al MySQL en el puerto 3306 para extraer la flag completa.
**Learning chain:** nmap port scan → FTP anonymous access → web app inspection → DNS record enumeration with dig → MySQL client connection → flag assembly from distributed key parts
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1021.003 (Remote Services: DCOM), T1078.003 (Valid Accounts: Local Accounts)
**Fuente:** [TryHackMe - Network Discovery - Scan-ta Clause](https://tryhackme.com/r/room/networkservices-aoc2025-jnsoqbxgky)
