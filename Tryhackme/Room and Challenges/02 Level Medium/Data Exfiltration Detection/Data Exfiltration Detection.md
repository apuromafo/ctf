# Data Exfiltration Detection [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `dataexfildetection`
* **Link:** https://tryhackme.com/room/dataexfildetection
* **Objeto:** Detectar exfiltración de datos analizando tráfico de red (Wireshark/tshark) y logs (Splunk) a través de DNS tunneling, FTP, HTTP raw e ICMP.

---

## Solucionario de Tareas / Task Solutions

> La detección efectiva depende de correlacionar telemetría de host, red y nube: quién accedió a los datos, qué se transfirió, cómo se hizo staging y a dónde se envió.
> Effective detection depends on correlating host, network and cloud telemetry: who accessed the data, what was transferred, how it was staged, and where it was sent.

### Tarea / Task — Overview

**Exfiltrar los datos a través de HTTP entra en qué técnica? / Exfiltrating the data through HTTP comes under which technique?**
`Network-based`

Fuente / Source: https://simontaplin.net/2025/10/05/answers-for-the-tryhackme-data-exfiltration-room/ · https://www.sharonjebitok.com/data-exfiltration-detection-tryhackme

### Tarea / Task — DNS Tunneling

**¿Cuál es el dominio sospechoso que recibe el tráfico DNS? / What is the suspicious domain receiving the DNS traffic?**
`tunnelcorp.net`

**¿Cuántos logs/tráfico sospechosos relacionados con DNS tunneling se observaron? / How many suspicious traffic/logs related to dns tunneling were observed?**
`315`

**¿Qué IP local envió el máximo número de peticiones sospechosas? / Which local IP sent the maximum number of suspicious requests?**
`192.168.1.103`

Fuente / Source: https://simontaplin.net/2025/10/05/answers-for-the-tryhackme-data-exfiltration-room/ · https://www.sharonjebitok.com/data-exfiltration-detection-tryhackme

### Tarea / Task — FTP

**¿Cuántas conexiones se observaron desde la cuenta guest? / How many connections were observed from the guest account?**
`5`

**Aplica el filtro; ¿cuál es el nombre del archivo relacionado con clientes (customer) exfiltrado desde la cuenta root? / Apply the filter; what is the name of the customer-related file exfiltrated from the root account?**
`customer_data.xlsx`

**¿Qué IP interna envió el payload más grande a una IP externa? / Which internal IP was found to be sending the largest payload to an external IP?**
`192.168.1.105`

**¿Cuál es la flag oculta dentro del stream FTP que transfiere el archivo CSV a la IP sospechosa? / What is the flag hidden inside the ftp stream transferring the CSV file to the suspicious IP?**
`THM{ftp_exfil_hidden_flag}`

Fuente / Source: https://simontaplin.net/2025/10/05/answers-for-the-tryhackme-data-exfiltration-room/ · https://www.sharonjebitok.com/data-exfiltration-detection-tryhackme

### Tarea / Task — HTTP

**¿Qué host interno comprometido se usó para exfiltrar estos datos sensibles? / Which internal compromised host was used to exfiltrate this sensitive data?**
`192.168.1.103`

**¿Cuál es la flag oculta dentro de los datos exfiltrados? / What's the flag hidden inside the exfiltrated data?**
`THM{http_raw_3xf1ltr4t10n_succ3ss}`

Fuente / Source: https://simontaplin.net/2025/10/05/answers-for-the-tryhackme-data-exfiltration-room/ · https://www.sharonjebitok.com/data-exfiltration-detection-tryhackme

### Tarea / Task — ICMP

**¿Cuál es la flag encontrada en los datos exfiltrados a través de ICMP? / What is the flag found in the exfiltrated data through ICMP?**
`THM{1cmp_3ch0_3xf1ltr4t10n_succ3ss}`

Fuente / Source: https://simontaplin.net/2025/10/05/answers-for-the-tryhackme-data-exfiltration-room/ · https://www.sharonjebitok.com/data-exfiltration-detection-tryhackme

---

*Documentación para propósitos educativos y registro de CTF.*
*Fuente de respuestas / Answer source: https://simontaplin.net/2025/10/05/answers-for-the-tryhackme-data-exfiltration-room/ · https://www.sharonjebitok.com/data-exfiltration-detection-tryhackme*
