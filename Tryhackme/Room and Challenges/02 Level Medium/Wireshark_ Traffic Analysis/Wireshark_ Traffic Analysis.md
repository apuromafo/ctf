# Wireshark_ Traffic Analysis

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | wiresharktrafficanalysis | https://tryhackme.com/room/wiresharktrafficanalysis | 02 Level Medium | TryHackMe | Wireshark, pcap, Network Forensics | Análisis forense de capturas de tráfico de red con Wireshark en múltiples escenarios de ataque |

---

**Contexto:** La sala **Wireshark: Traffic Analysis** entrena la inspección forense de capturas pcap con Wireshark. A lo largo de varios escenarios el alumno identifica escaneos TCP, intentos de fuerza bruta, conexiones a redes WiFi, protocolos de exfiltración, transferencias de archivos (resume.doc), reglas de firewall y URL de malware, terminando con la flag de la sala: `FLAG{THM-PACKETMASTER}`.

## Solucionario

### Task 1: Overview

**Explicación:**

La sala presenta las capturas y la metodología de análisis de tráfico de red que se aplicará en los escenarios siguientes.

Respuesta: `No answer needed`

### Task 2: Escenario 1 - Análisis de tráfico

**Explicación:**

Se analiza el primer escenario: el número de paquetes capturados, el método de conexión utilizado (TCP Connect), el número de frames involucrados y el conteo de conexiones realizado.

1. `1000`
2. `TCP Connect`
3. `1083`
4. `68`

### Task 3: Escenario 2 - Ataque de fuerza bruta

**Explicación:**

Se examina un ataque de fuerza bruta registrado en la captura: el número de paquetes enviados, los puertos implicados, la cantidad de combinaciones y las respuestas obtenidas (mensaje en el banner y mensaje de éxito).

1. `284`
2. `90`
3. `6`
4. `clientnothere!`
5. `Nice work!`

### Task 4: Escenario 3 - Red WiFi

**Explicación:**

Se analiza una red WiFi capturada: la dirección MAC del cliente, el número de paquetes relacionados, el modelo del dispositivo (Galaxy-A12), la dirección IP (defensivamente ofuscada) y el password de la red WiFi.

1. `9a:81:41:cb:96:6c`
2. `16`
3. `Galaxy-A12`
4. `10[.]1[.]12[.]2`
5. `xp1$`

### Task 5: Escenario 4 - Protocolos y exfiltración

**Explicación:**

Se identifica el protocolo utilizado para la comunicación (SSH) y el dominio de exfiltración de datos (ofuscado deflecto).

1. `SSH`
2. `dataexfil[.]com`

### Task 6: Escenario 5 - Transferencia de archivos

**Explicación:**

Se desglosa la transferencia de un archivo en la captura: número de paquetes, tamaño total de la transferencia, nombre del archivo transferido (resume.doc) y el permiso aplicado mediante el comando CHMOD.

1. `737`
2. `39424`
3. `resume.doc`
4. `CHMOD 777`

### Task 7: Escenario 6 - Tráfico sospechoso

**Explicación:**

Se analiza un tráfico sospechoso adicional: el conteo de paquetes de una sesión, el número de frames, el código de respuesta/estado y la dirección IP del servidor implicado (ofuscada).

1. `6 `
2. `52`
3. `444`
4. `62[.]210[.]130[.]250`

### Task 8: Escenario 7 - Detección final

**Explicación:**

En el escenario final se identifican las características de la amenaza: número de paquetes, frames, el dominio del servicio de navegación segura (safebrowsing.googleapis.com) y la flag de la sala.

1. `16`
2. `115`
3. `safebrowsing[.]googleapis[.]com`
4. `FLAG{THM-PACKETMASTER}`

### Task 9: Escenario 8

**Explicación:**

Se responden las últimas métricas del análisis de tráfico: el número de paquetes y de frames de la sesión estudiada.

1. `237`
2. `170`

### Task 10: Reglas de firewall

**Explicación:**

Se traducen las observaciones de la captura en reglas de firewall sintácticamente correctas: denegar el tráfico IP desde la IP sospechosa y permitir el tráfico del MAC identificado.

1. `add deny ip from 10.121.70.151 to any in`
2. `add allow MAC 00:d0:59:aa:af:80 any in`

### Task 11: Conclusión

**Explicación:**

La sala concluye el análisis forense de tráfico de red con la consolidación de todas las técnicas de Wireshark aplicadas.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Overview de la sala | `No answer needed` |
| 2.1 | Número de paquetes | `1000` |
| 2.2 | Método de conexión | `TCP Connect` |
| 2.3 | Frames | `1083` |
| 2.4 | Conexiones | `68` |
| 3.1 | Paquetes del ataque | `284` |
| 3.2 | Puertos | `90` |
| 3.3 | Combinaciones | `6` |
| 3.4 | Mensaje del banner | `clientnothere!` |
| 3.5 | Mensaje de éxito | `Nice work!` |
| 4.1 | MAC del cliente | `9a:81:41:cb:96:6c` |
| 4.2 | Paquetes WiFi | `16` |
| 4.3 | Dispositivo | `Galaxy-A12` |
| 4.4 | IP del cliente | `10[.]1[.]12[.]2` |
| 4.5 | Password WiFi | `xp1$` |
| 5.1 | Protocolo usado | `SSH` |
| 5.2 | Dominio de exfiltración | `dataexfil[.]com` |
| 6.1 | Paquetes de la transferencia | `737` |
| 6.2 | Tamaño de la transferencia | `39424` |
| 6.3 | Archivo transferido | `resume.doc` |
| 6.4 | Permiso aplicado | `CHMOD 777` |
| 7.1 | Paquetes de la sesión | `6 ` |
| 7.2 | Frames | `52` |
| 7.3 | Código de estado | `444` |
| 7.4 | IP del servidor | `62[.]210[.]130[.]250` |
| 8.1 | Paquetes de la amenaza | `16` |
| 8.2 | Frames | `115` |
| 8.3 | Dominio de navegación segura | `safebrowsing[.]googleapis[.]com` |
| 8.4 | Flag de la sala | `FLAG{THM-PACKETMASTER}` |
| 9.1 | Paquetes del escenario 8 | `237` |
| 9.2 | Frames del escenario 8 | `170` |
| 10.1 | Regla de denegación IP | `add deny ip from 10.121.70.151 to any in` |
| 10.2 | Regla de permitir MAC | `add allow MAC 00:d0:59:aa:af:80 any in` |
| 11 | Conclusión | `No answer needed` |

---

**Metodología:** Análisis forense de tráfico de red con Wireshark: conteo de paquetes y frames, identificación de conexiones y protocolos, detección de fuerza bruta, análisis de transferencias de archivos y derivación de reglas de firewall a partir del tráfico observado.

**Learning chain:** Overview → escaneo → fuerza bruta → WiFi → protocolos → transferencia de archivos → tráfico sospechoso → flag → reglas de firewall → conclusión.

**Lección:** *Cada escenario de la captura responde a un patrón: el conteo de paquetes, los puertos y los mensajes de banner permiten reconstruir el ataque observado.*

**MITRE ATT&CK:** T1046 Network Service Discovery · T1110 Brute Force · T1041 Exfiltration Over C2 Channel · T1071 Application Layer Protocol.

**Fuente:** [TryHackMe - Wireshark_ Traffic Analysis](https://tryhackme.com/room/wiresharktrafficanalysis)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.