# Packets & Frames

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Info | Walkthrough | `packetsframes` | https://tryhackme.com/room/packetsframes | 00 Level Info | TryHackMe | paquetes / tramas / TCP/IP / handshake / checksum / UDP/TCP / netcat | Fundamentos del tráfico de red: diferencia entre paquetes y tramas, protocolos TCP/UDP, handshake y conexiones |

---

**Contexto:** La sala explica los fundamentos del tráfico de red diferenciando paquetes (Packet) y tramas (Frame), repasa el modelo TCP/IP, el proceso de handshake y la función de checksums, y compara los protocolos TCP y UDP. Incluye ejercicios con conexiones de red reales que desbloquean flags.

> **ES:** Se aprende qué es un paquete y una trama, cómo funciona el handshake TCP y los checksums, cuándo usar TCP o UDP, y se abre una conexión real para obtener flags.
> **EN:** Learn what a packet and a frame are, how the TCP handshake and checksums work, when to use TCP or UDP, and open a real connection to get flags.

## Solucionario

### Task 1: Paquetes y tramas / Packets and Frames

**Explicación:** Se distingue el término "paquete" (datos que viajan por la red con cabecera de protocolo como IP) del término "trama" (la unidad dentro de la red local, con cabecera de capa de enlace). El mismo bloque de datos se llama distinto según la capa en la que se observe.

```text
1. 1. Packet
   2. Frame
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la unidad de datos en capa de red/IP? / What is the data unit at network/IP layer called? | `Packet` |
| 2 | ¿Cómo se llama la unidad de datos en capa de enlace? / What is the data unit at the data link layer called? | `Frame` |

### Task 2: Modelo TCP/IP y handshake / TCP/IP model and handshake

**Explicación:** Se explora el modelo TCP/IP y los mecanismos del protocolo TCP: el checksum que valida la integridad de los datos y el conocido handshake de tres pasos para establecer una conexión fiable, que intercambia los mensajes SYN, SYN/ACK y ACK.

```text
2. 1. checksum
   2. SYN,SYN/ACK,ACK
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué mecanismo valida la integridad de los datos? / What mechanism validates data integrity? | `checksum` |
| 2 | ¿Qué mensajes componen el handshake TCP? / What messages make up the TCP handshake? | `SYN,SYN/ACK,ACK` |

### Task 3: Flag del modelo TCP/IP / TCP/IP model flag

**Explicación:** Tras revisar el modelo TCP/IP se localiza la flag que acredita haber entendido el recorrido de los datos (el "chatter" TCP).

```text
3. THM{TCP_CHATTER}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de esta tarea? / What is the flag of this task? | `THM{TCP_CHATTER}` |

### Task 4: TCP frente a UDP / TCP vs UDP

**Explicación:** Se comparan los protocolos de transporte: UDP (User Datagram Protocol) es sin conexión y sin estado (stateless), mientras que TCP es orientado a conexión y fiable. Según la necesidad de fiabilidad o velocidad se elige uno.

```text
4. 1. User Datagram Protocol
   2. stateless
   3. TCP
   4. UDP
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué protocolo es el User Datagram Protocol? / Which protocol is the User Datagram Protocol? | `User Datagram Protocol` |
| 2 | ¿Cómo se describe un protocolo que no guarda estado? / How is a stateless protocol described? | `stateless` |
| 3 | ¿Qué protocolo es orientado a conexión? / Which protocol is connection-oriented? | `TCP` |
| 4 | ¿Qué protocolo es sin conexión? / Which protocol is connectionless? | `UDP` |

### Task 5: Conexión real y flag / Real connection and flag

**Explicación:** Se realiza una conexión real (por ejemplo, con netcat) contra un servicio de la sala para comprobar el establecimiento de una conexión TCP; al conectar, el servicio responde con la flag.

```text
5. THM{YOU_CONNECTED_TO_A_PORT}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la conexión? / What is the connection flag? | `THM{YOU_CONNECTED_TO_A_PORT}` |

### Task 6: Cierre / Conclusion

**Explicación:** Recapitulación del contenido de la sala: paquetes, tramas, TCP/UDP, handshake y conexiones. No hay preguntas que responder.

```text
6. 1. No answer needed
   2. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Terminar la sala. / Finish the room. | No answer needed |
| 2 | Leer la conclusión. / Read the conclusion. | No answer needed |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la unidad de datos en capa de red/IP? / What is the data unit at network/IP layer called? | `Packet` |
| 2 | ¿Cómo se llama la unidad de datos en capa de enlace? / What is the data unit at the data link layer called? | `Frame` |
| 3 | ¿Qué mecanismo valida la integridad de los datos? / What mechanism validates data integrity? | `checksum` |
| 4 | ¿Qué mensajes componen el handshake TCP? / What messages make up the TCP handshake? | `SYN,SYN/ACK,ACK` |
| 5 | ¿Cuál es la flag de esta tarea? / What is the flag of this task? | `THM{TCP_CHATTER}` |
| 6 | ¿Qué protocolo es el User Datagram Protocol? / Which protocol is the User Datagram Protocol? | `User Datagram Protocol` |
| 7 | ¿Cómo se describe un protocolo que no guarda estado? / How is a stateless protocol described? | `stateless` |
| 8 | ¿Qué protocolo es orientado a conexión? / Which protocol is connection-oriented? | `TCP` |
| 9 | ¿Qué protocolo es sin conexión? / Which protocol is connectionless? | `UDP` |
| 10 | ¿Cuál es la flag de la conexión? / What is the connection flag? | `THM{YOU_CONNECTED_TO_A_PORT}` |
| 11 | Terminar la sala. / Finish the room. | No answer needed |
| 12 | Leer la conclusión. / Read the conclusion. | No answer needed |

---

**Metodología:** Comprender la diferencia entre paquete y trama, revisar el modelo TCP/IP y el handshake (SYN/SYN-ACK/ACK), estudiar checksums, comparar TCP/UDP y, finalmente, abrir una conexión de red real para capturar las flags.

### Cadena de ataque / Attack Chain

```text
Packet vs Frame -> modelo TCP/IP -> checksum -> handshake SYN,SYN/ACK,ACK -> THM{TCP_CHATTER} -> TCP vs UDP (stateless) -> conexión real (netcat) -> THM{YOU_CONNECTED_TO_A_PORT}
```

**Learning chain:** Paquetes/tramas -> TCP/IP -> checksum -> handshake -> TCP vs UDP -> conexión real -> flags

**Lección:** *Comprender en qué capa viaja cada dato y cómo se establece una conexión TCP/UDP es imprescindible para interpretar sniffing, capturas y cualquier análisis de tráfico de red.*

**MITRE ATT&CK:** N/A (sala educativa de fundamentos de redes)

**Fuente:** [TryHackMe - Packets & Frames](https://tryhackme.com/room/packetsframes)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.