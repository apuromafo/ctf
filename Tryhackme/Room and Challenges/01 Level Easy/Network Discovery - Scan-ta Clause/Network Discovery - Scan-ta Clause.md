# Network Discovery - Scan-ta Clause

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `networkservices-aoc2025-jnsoqbxgky` | https://tryhackme.com/room/networkservices-aoc2025-jnsoqbxgky | Advent of Cyber 2025 | TryHackMe | nmap, FTP, netcat, DNS dig, MySQL | Medio — descubrimiento completo de servicios expuestos en la red TBFC permitiendo recopilación de credenciales y datos fragmentados |

---

**Contexto:** En el día 7 de Advent of Cyber 2025, la red de TBFC se ha caído y se requiere realizar reconocimiento de servicios para restaurar las operaciones. Se explora el sitio "Pwned by HopSec" y se emplean herramientas de descubrimiento de red (nmap, netcat, dig, mysql client) para localizar fragmentos de una key distribuida entre FTP, aplicaciones web, registros DNS y una base de datos MySQL.

> **ES:** Reconocimiento de red en la red TBFC: escaneo con nmap, acceso FTP, revisión de la aplicación web TBFC, consulta de registros DNS con dig y conexión a una base de datos MySQL para descubrir servicios expuestos y reconstruir una key distribuida en fragmentos.
> **EN:** Network discovery across the TBFC network: nmap scanning, FTP access, review of the TBFC web app, DNS records lookup with dig and a MySQL database connection to discover exposed services and reassemble a key split into fragments.

## Solucionario

### Task 1: Reconocimiento Inicial

**Explicación:** Se inspecciona la portada del sitio comprometido en la red TBFC: aparece el mensaje "Pwned by HopSec", confirmando el defacement del sitio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What evil message do you see on top of the website? | `Pwned by HopSec` |

### Task 2: FTP Discovery

**Explicación:** Se accede por FTP (acceso anónimo) al servidor de TBFC y se recupera la primera parte de la key: `3aster_`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first key part found on the FTP server? | `3aster_` |

### Task 3: Web App Discovery

**Explicación:** Se explora la aplicación web TBFC, donde aparece la segunda parte de la key: `15_th3_`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the second key part found in the TBFC app? | `15_th3_` |

### Task 4: DNS Discovery

**Explicación:** Se consultan los registros DNS con dig: la tercera parte de la key se encuentra en los registros DNS.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the third key part found in the DNS records? | `n3w_xm45` |

### Task 5: MySQL Discovery

**Explicación:** Se localiza el servicio MySQL corriendo en el puerto 3306; conectándose a la base de datos se recupera la flag final que agrupa todas las partes de la key: `THM{4ll_s3rvice5_d1sc0vered}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which port was the MySQL database running on? | `3306` |
| 2 | Finally, what's the flag you found in the database? | `THM{4ll_s3rvice5_d1sc0vered}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What evil message do you see on top of the website? | `Pwned by HopSec` |
| 2 | What is the first key part found on the FTP server? | `3aster_` |
| 3 | What is the second key part found in the TBFC app? | `15_th3_` |
| 4 | What is the third key part found in the DNS records? | `n3w_xm45` |
| 5 | Which port was the MySQL database running on? | `3306` |
| 6 | Finally, what's the flag you found in the database? | `THM{4ll_s3rvice5_d1sc0vered}` |

---

**Metodología:** Se inició con escaneo de puertos mediante nmap para descubrir servicios activos (FTP, HTTP, DNS, MySQL). Se accedió por FTP para recuperar la primera parte de la key. Se navegó la aplicación web TBFC para obtener la segunda parte. Se consultaron registros DNS con dig para localizar la tercera parte. Finalmente, se conectó al MySQL en el puerto 3306 para extraer la flag completa.

### Cadena de ataque / Attack Chain

```text
nmap (Network Service Discovery) -> FTP anonymous (key part 1: 3aster_) -> TBFC web app (key part 2: 15_th3_) -> DNS dig (key part 3: n3w_xm45) -> MySQL :3306 (flag THM{4ll_s3rvice5_d1sc0vered})
```

**Learning chain:** nmap port scan → FTP anonymous access → web app inspection → DNS record enumeration with dig → MySQL client connection → flag assembly from distributed key parts

**Lección:** *El descubrimiento de servicios no debe detenerse en un solo protocolo: repartir los fragmentos entre FTP, web, DNS y base de datos demuestra que la enumeración completa es la clave para reconstruir datos críticos.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1021.003 (Remote Services: DCOM), T1078.003 (Valid Accounts: Local Accounts)

**Fuente:** [TryHackMe - Network Discovery - Scan-ta Clause](https://tryhackme.com/room/networkservices-aoc2025-jnsoqbxgky)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.