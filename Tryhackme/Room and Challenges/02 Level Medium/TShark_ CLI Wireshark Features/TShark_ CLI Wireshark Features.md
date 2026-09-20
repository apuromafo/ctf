# TShark_ CLI Wireshark Features

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Forense / Análisis de tráfico | tsharkcliwiresharkfeatures | https://tryhackme.com/room/tsharkcliwiresharkfeatures | 02 Level Medium | TryHackMe | TShark, Wireshark CLI, PCAP, display filters, HTTP, TTL, frames | Análisis exhaustivo de captura de red con la CLI de Wireshark |

---

**Contexto:** La sala **TShark_ CLI Wireshark Features** profundiza en el uso de la interfaz de línea de comandos de Wireshark (TShark) para responder preguntas sobre una captura de red. Se analizan campos de nivel 2 (frames), nivel 3 (TTL, IP como `145[.]254[.]160[.]237`) y nivel 4 (puertos, flags SYN, temporalidades), así como tráfico HTTP (`hxxp[://]www[.]ethereal[.]com/download[.]html`). El reto obliga a dominar display filters avanzados y la extracción de campos con `-T fields -e` para correlacionar paquetes y responder las preguntas de la captura.

## Solucionario

### Task 1: Pre-Reqs / Requisitos
**Explicación:**

Se prepara el entorno (Kali/AttackBox con TShark instalado) y se descarga la captura con la que se trabajará.

| Pregunta | Respuesta |
|----------|-----------|
| Install and configure the attack box | `No answer needed` |

### Task 2: TShark Basics / Conceptos básicos
**Explicación:**

Se usan los comandos básicos de TShark sobre la captura: lectura con `-r`, conteo de paquetes, filtros de visualización y consulta de campos de red. En esta tarea se obtienen el número total de frames (62), el rango de TTL observado (40-79), la identificación del primer paquete de handshake TCP (SYN: servidor puerto 80) y una IP de origen (`145[.]254[.]160[.]237`).

```bash
tshark -r <capture>.pcap
tshark -r <capture>.pcap | wc -l
tshark -r <capture>.pcap -Y "tcp.flags.syn==1 and tcp.flags.ack==0"
```

| Pregunta | Respuesta |
|----------|-----------|
| How many frames are in the capture? | `62` |
| What is the TTL range? | `40-79` |
| What is the first packet that establishes a three-way handshake? | `Connection establish request (SYN): server port 80` |
| What is the source IP address? | `145[.]254[.]160[.]237` |

### Task 3: HTTP Requests / Peticiones HTTP
**Explicación:**

Se enfoca el análisis al protocolo HTTP de la captura: se identifica la IP del servidor web destino, la distribución porcentual del tráfico, la IP del cliente que realiza las peticiones y el tiempo medio de servicio (valores en milisegundos).

```bash
tshark -r <capture>.pcap -Y "http"
tshark -r <capture>.pcap -Y "http.response" -T fields -e ip.dst | sort | uniq -c
```

| Pregunta | Respuesta |
|----------|-----------|
| What is the server web IP address? | `216[.]239[.]59[.]99` |
| What percentage of the capture is HTTP traffic? | `6.98%` |
| What is the client IP address? | `145[.]253[.]2[.]203` |
| How long does it take to get the index page? | `29.00` |

### Task 4: DNS Analysis / Análisis DNS
**Explicación:**

Se inspecciona el tráfico DNS: se localiza el socket/puerto origen desde el que se realiza la consulta (`145[.]254[.]160[.]237:3009`), el nombre de dominio (URL) consultado y el tamaño de la respuesta.

```bash
tshark -r <capture>.pcap -Y "dns"
tshark -r <capture>.pcap -Y "dns" -T fields -e dns.qry.name
```

| Pregunta | Respuesta |
|----------|-----------|
| What is the source socket for the DNS query? | `145[.]254[.]160[.]237:3009` |
| What is the URL queried? | `hxxp[://]www[.]ethereal[.]com/download[.]html` |
| What is the size of the response? | `75` |

### Task 5: TCP SYN Requests / Peticiones TCP SYN
**Explicación:**

Se filtran y cuentan los paquetes TCP con la bandera SYN activada y se localiza la marca temporal del paquete de interés.

```bash
tshark -r <capture>.pcap -Y "tcp.flags.syn==1"
tshark -r <capture>.pcap -Y "tcp.flags.syn==1" -T fields -e frame.time
```

| Pregunta | Respuesta |
|----------|-----------|
| How many SYN requests are there? | `27` |
| What is the timestamp of the (last) SYN request? | `May 13, 2004 10:17:08.222534000 UTC` |

### Task 6: TCP Analysis / Análisis TCP
**Explicación:**

Se responde a varias preguntas sobre el tráfico TCP de la captura: número de paquetes TCP con bandera ACK, de SYN-ACK, identificación de puertos/flags concretos, conteo y una dirección IP involucrada (`172[.]16[.]172[.]129`).

```bash
tshark -r <capture>.pcap -Y "tcp.flags.ack==1"
tshark -r <capture>.pcap -Y "tcp.flags.syn==1 and tcp.flags.ack==1"
tshark -r <capture>.pcap -Y "tcp" -T fields -e ip.src | sort | uniq -c
```

| Pregunta | Respuesta |
|----------|-----------|
| How many TCP packets with ACK are there? | `30` |
| How many SYN/ACK packets are there? | `12` |
| How many FIN packets are there? | `472` |
| How many TCP packets with SYN flag set? | `12` |
| What is the IP address of the host sending the TCP packets? | `172[.]16[.]172[.]129` |

### Task 7: Content / Contenido
**Explicación:**

Tarea final de comprensión del conjunto de la sala una vez dominada la CLI de TShark.

| Pregunta | Respuesta |
|----------|-----------|
| Content | `No answer needed` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Install and configure the attack box | `No answer needed` |
| 2 | How many frames are in the capture? | `62` |
| 2 | What is the TTL range? | `40-79` |
| 2 | What is the first packet that establishes a three-way handshake? | `Connection establish request (SYN): server port 80` |
| 2 | What is the source IP address? | `145[.]254[.]160[.]237` |
| 3 | What is the server web IP address? | `216[.]239[.]59[.]99` |
| 3 | What percentage of the capture is HTTP traffic? | `6.98%` |
| 3 | What is the client IP address? | `145[.]253[.]2[.]203` |
| 3 | How long does it take to get the index page? | `29.00` |
| 4 | What is the source socket for the DNS query? | `145[.]254[.]160[.]237:3009` |
| 4 | What is the URL queried? | `hxxp[://]www[.]ethereal[.]com/download[.]html` |
| 4 | What is the size of the response? | `75` |
| 5 | How many SYN requests are there? | `27` |
| 5 | What is the timestamp of the (last) SYN request? | `May 13, 2004 10:17:08.222534000 UTC` |
| 6 | How many TCP packets with ACK are there? | `30` |
| 6 | How many SYN/ACK packets are there? | `12` |
| 6 | How many FIN packets are there? | `472` |
| 6 | How many TCP packets with SYN flag set? | `12` |
| 6 | What is the IP address of the host sending the TCP packets? | `172[.]16[.]172[.]129` |
| 7 | Content | `No answer needed` |

---

**Metodología:** Conteos y filtros de visualización de TShark sobre la captura, análisis de campos de capa 2/3/4 (TTL, IP, puertos, flags TCP), correlación de HTTP/DNS y lectura de marcas temporales para responder las preguntas del reto.

### Cadena de ataque / Attack Chain

```
tshark -r (frames totales) → filtros de capa 3/4 (TTL, SYN, ACK, puertos) → análisis HTTP (respuestas/cliente/servidor) → campo DNS (socket/query/tamaño) → temporales de SYN → conteos TCP → respuestas
```

**Learning chain:** CLI tooling → display filters → extracción de campos → análisis multi-capa (L2-L4) → correlación de protocolos (HTTP/DNS/TCP).

**Lección:** *El dominio fluido de TShark convierte una captura opaca en respuestas precisas mediante combinación de filtros (`-Y`) y extracción de campos (`-T fields -e`); la práctica con pcap histórico (Ethereal, 2004) demuestra la reutilidad de la herramienta.*

**MITRE ATT&CK:** T1040 Network Sniffing · T1046 Network Service Discovery · T1560.001 Archive Collected Data.

**Fuente:** [TryHackMe - TShark_ CLI Wireshark Features](https://tryhackme.com/room/tsharkcliwiresharkfeatures)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.