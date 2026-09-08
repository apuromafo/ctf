# Data Exfiltration Detection

| **Dificultad** | MEDIUM | **Tipo** | Premium | **Slug** | `dataexfildetection` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dataexfildetection) | **Sección** | 02 Level Medium | **Fuente** | simontaplin.net + sharonjebitok.com (writeups) |
| **Componentes** | Network Forensics / DNS Tunneling / FTP / HTTP Raw / ICMP / Wireshark / tshark / Splunk | **Impacto** | Enseña a detectar exfiltración de datos correlacionando telemetría de host, red y nube |

---

**Contexto:** La detección efectiva de exfiltración de datos depende de correlacionar telemetría de host, red y nube: quién accedió a los datos, qué se transfirió, cómo se hizo staging y a dónde se envió. Effective detection depends on correlating host, network and cloud telemetry: who accessed the data, what was transferred, how it was staged, and where it was sent.

## Solucionario

### Task 1: Overview

**Explicación:** Se analiza el tráfico de red (Wireshark/tshark) y logs (Splunk) para detectar exfiltración de datos. Exfiltrar los datos a través de HTTP entra en la técnica de exfiltración basada en red (Network-based).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Exfiltrating the data through HTTP comes under which technique? | `Network-based` |

### Task 2: DNS Tunneling

**Explicación:** El tráfico DNS es un canal común para exfiltración. Se identifica el dominio sospechoso que recibe el tráfico DNS (`tunnelcorp.net`), el número de logs sospechosos observados y la IP local que envió el máximo número de peticiones sospechosas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the suspicious domain receiving the DNS traffic? | `tunnelcorp.net` |
| 2 | How many suspicious traffic/logs related to dns tunneling were observed? | `315` |
| 3 | Which local IP sent the maximum number of suspicious requests? | `192.168.1.103` |

### Task 3: FTP

**Explicación:** Se analizan las conexiones FTP observadas desde la cuenta guest, el archivo de clientes exfiltrado desde la cuenta root, la IP interna que envió el payload más grande a una IP externa, y la flag oculta dentro del stream FTP que transfiere el archivo CSV a la IP sospechosa.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many connections were observed from the guest account? | `5` |
| 2 | Apply the filter; what is the name of the customer-related file exfiltrated from the root account? | `customer_data.xlsx` |
| 3 | Which internal IP was found to be sending the largest payload to an external IP? | `192.168.1.105` |
| 4 | What is the flag hidden inside the ftp stream transferring the CSV file to the suspicious IP? | `THM{ftp_exfil_hidden_flag}` |

### Task 4: HTTP

**Explicación:** Se identifica el host interno comprometido usado para exfiltrar los datos sensibles y la flag oculta dentro de los datos exfiltrados por HTTP raw.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which internal compromised host was used to exfiltrate this sensitive data? | `192.168.1.103` |
| 2 | What's the flag hidden inside the exfiltrated data? | `THM{http_raw_3xf1ltr4t10n_succ3ss}` |

### Task 5: ICMP

**Explicación:** Se busca la flag encontrada en los datos exfiltrados a través de ICMP (echos de ping con payload de datos).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag found in the exfiltrated data through ICMP? | `THM{1cmp_3ch0_3xf1ltr4t10n_succ3ss}` |

---

**Metodología:**
1. Correlacionar la telemetría de host, red y nube para identificar qué datos se transfirieron, cómo se hizo staging y a dónde se enviaron.
2. Analizar el tráfico DNS para detectar tunneling y el dominio sospechoso que lo recibe.
3. Filtrar el tráfico FTP para identificar el archivo exfiltrado, la cuenta y la IP origen, y la flag oculta en el stream.
4. Revisar el tráfico HTTP raw para encontrar el host comprometido y la flag embebida en los datos exfiltrados.
5. Examinar el tráfico ICMP para localizar la flag oculta en los echos de ping.

**Learning chain:** HTTP → Network-based → DNS Tunneling → tunnelcorp.net → 315 logs → 192.168.1.103 → FTP → guest 5 connections → customer_data.xlsx → 192.168.1.105 → ftp EOF flag → HTTP → 192.168.1.103 → http_raw flag → ICMP → ICMP echo flag

**Lección:** *La detección efectiva de exfiltración de datos correlaciona telemetría de host, red y nube; los protocolos DNS, FTP, HTTP y ICMP son los canales más comunes a inspeccionar.*

**MITRE ATT&CK:** T1048.003 (Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol), T1041 (Exfiltration Over C2 Channel), T1048.002 (Exfiltration Over Asymmetric Encrypted Non-C2 Protocol)

**Fuente:** [TryHackMe - Data Exfiltration Detection](https://tryhackme.com/room/dataexfildetection)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
