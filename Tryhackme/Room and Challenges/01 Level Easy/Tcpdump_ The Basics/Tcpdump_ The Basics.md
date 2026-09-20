# Tcpdump_ The Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `tcpdumpthebasics` | https://tryhackme.com/room/tcpdumpthebasics | 01 Level Easy | TryHackMe | tcpdump / libpcap / pcap / filtros (host, port, protocolo) / tcp[tcpflags] / ARP / DNS / salidas -n / -e / -A / -X | Aprender a capturar, guardar, filtrar y mostrar paquetes con tcpdump, analizando traffic.pcap: ICMP, ARP, DNS, TCP RST y tamaños de paquete. |

---

**Contexto:** Room de la ruta Cyber Security 101 que introduce tcpdump y su librería `libpcap` (escrita en C/C++, muy estable y rápida, portada a Windows como WinPcap). Se aprende a capturar paquetes vía interfaz, guardarlos en un pcap, leerlos con `-r`, y aplicar filtros de host, puerto, protocolo y flags TCP (por ejemplo `tcp[tcpflags] == tcp-rst`), además de controlar el formato de salida (`-n`, `-e`, `-A`, `-X`). Las preguntas se responden analizando el fichero `traffic.pcap` proporcionado.

> **ES:** Guía básica de tcpdump: capturar y guardar paquetes, filtrar por ICMP/ARP/DNS/TCP y analizar traffic.pcap con expresiones y counts ('26' ICMP, '192.168.124.148' en ARP, 'mirrors.rockylinux.org' en DNS, '57' RST, '185.117.80.53' >15000 bytes, MAC '52:54:00:7c:d3:5b').
> **EN:** Basic tcpdump guide: capture and save packets, filter by ICMP/ARP/DNS/TCP and analyze traffic.pcap with expressions and counts ('26' ICMP, '192.168.124.148' in ARP, 'mirrors.rockylinux.org' in DNS, '57' RST, '185.117.80.53' >15000 bytes, MAC '52:54:00:7c:d3:5b').

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tcpdump está asociado a la librería `libpcap`, su base también de otras herramientas de red actuales (y portada a Windows como WinPcap).

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es el nombre de la librería asociada a tcpdump? / What is the name of the library that is associated with tcpdump? | `libpcap` |

### Task 2: Captura básica de paquetes / Basic Packet Capture

**Explicación:** Se usan las opciones básicas: `-i` para elegir interfaz (o `-i any`), `-w FILE.pcap` para escribir a fichero, `-r FILE.pcap` para leer capturas guardadas, `-c COUNT` para limitar paquetes y `-n` para mostrar direcciones solo en formato numérico (sin resolución DNS).

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué opción puedes añadir a tu comando para mostrar las direcciones solo en formato numérico? / What option can you add to your command to display addresses only in numeric format? | `-n` |

### Task 3: Expresiones de filtrado / Filtering Expressions

**Explicación:** Se filtran paquetes por host (`host`, `src host`, `dst host`), puerto (`port 53`, `src port`, `dst port`) y protocolo (`ip`, `ip6`, `udp`, `tcp`, `icmp`, `arp`), combinables con `and`, `or` y `not`. Sobre `traffic.pcap`: `tcpdump -r traffic.pcap icmp | wc -l` cuenta los ICMP; `tcpdump -r traffic.pcap arp` muestra quién pide la MAC de `192.168.124.137`; `tcpdump -r traffic.pcap port 53 | head -n1` revela el primer query DNS.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | How many packets in traffic.pcap use the ICMP protocol? / ¿Cuántos paquetes de traffic.pcap usan el protocolo ICMP? | `26` |
| 2 | What is the IP address of the host that asked for the MAC address of 192.168.124.137? / ¿Cuál es la IP del host que pidió la MAC de 192.168.124.137? | `192.168.124.148` |
| 3 | What hostname (subdomain) appears in the first DNS query? / ¿Qué hostname (subdominio) aparece en el primer query DNS? | `mirrors.rockylinux.org` |

### Task 4: Filtrado avanzado / Advanced Filtering

**Explicación:** Se evalúan tamaños (`greater LENGTH`, `less LENGTH`) y campos de cabecera con `proto[expr:size]`. Para flags TCP se usan alias como `tcp-syn`, `tcp-ack`, `tcp-fin`, `tcp-rst`: `tcpdump -r traffic.pcap "tcp[tcpflags] == tcp-rst" | wc -l` cuenta los paquetes con solo RST; `tcpdump -r traffic.pcap greater 15000 -n | head -n1` localiza paquetes mayores de 15000 bytes.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | How many packets have only the TCP Reset (RST) flag set? / ¿Cuántos paquetes tienen solo la flag TCP Reset (RST)? | `57` |
| 2 | What is the IP address of the host that sent packets larger than 15000 bytes? / ¿Cuál es la IP del host que envió paquetes mayores de 15000 bytes? | `185.117.80.53` |

### Task 5: Mostrar paquetes / Displaying Packets

**Explicación:** Opciones de salida: `-q` (resumen breve), `-e` (cabeceras de nivel de enlace y MACs), `-A` (contenido ASCII), `-xx` (hex completo), `-X` (hex + ASCII). Con `tcpdump -r traffic.pcap arp -e` se obtiene la cabecera link-layer del ARP Request y su MAC origen.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the MAC address of the host that sent an ARP request? / ¿Cuál es la dirección MAC del host que envió una petición ARP? | `52:54:00:7c:d3:5b` |

### Task 6: Conclusión / Conclusion

**Explicación:** Cierre de la room: tcpdump es la primera herramienta en el flujo de análisis de tráfico de red para analistas de seguridad. Sin respuesta que rellenar.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Completa la conclusión. / Complete the conclusion. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Cuál es el nombre de la librería asociada a tcpdump? / What is the name of the library that is associated with tcpdump? | `libpcap` |
| 2 | ¿Qué opción puedes añadir a tu comando para mostrar las direcciones solo en formato numérico? / What option can you add to your command to display addresses only in numeric format? | `-n` |
| 3 | How many packets in traffic.pcap use the ICMP protocol? | `26` |
| 4 | What is the IP address of the host that asked for the MAC address of 192.168.124.137? | `192.168.124.148` |
| 5 | What hostname (subdomain) appears in the first DNS query? | `mirrors.rockylinux.org` |
| 6 | How many packets have only the TCP Reset (RST) flag set? | `57` |
| 7 | What is the IP address of the host that sent packets larger than 15000 bytes? | `185.117.80.53` |
| 8 | What is the MAC address of the host that sent an ARP request? | `52:54:00:7c:d3:5b` |
| 9 | Completa la conclusión. / Complete the conclusion. | `No answer needed` |

---

**Metodología:** Introducción a libpcap -> opciones básicas de captura (-i, -w, -r, -c, -n) -> filtros de host, puerto y protocolo con and/or/not -> análisis de traffic.pcap (ICMP -> 26; ARP quien pide MAC 192.168.124.137 -> 192.168.124.148; primer query DNS -> mirrors.rockylinux.org) -> filtrado avanzado (RST -> 57; greater 15000 -> 185.117.80.53) -> formato de salida (-e para MACs -> 52:54:00:7c:d3:5b) -> conclusión.

### Cadena de ataque / Attack Chain

```text
traffic.pcap -> tcpdump -r -> icmp | wc -l -> 26 -> arp -> quién pide 192.168.124.137 -> 192.168.124.148 -> port 53 | head -n1 -> mirrors.rockylinux.org -> tcp[tcpflags]==tcp-rst | wc -l -> 57 -> greater 15000 -n -> 185.117.80.53 -> arp -e -> 52:54:00:7c:d3:5b
```

**Learning chain:** libpcap -> captura -> almacenamiento (pcap) -> filtros host/port/proto -> protocolos (ICMP/ARP/DNS) -> flags TCP -> tamaño de paquete -> formato de salida -e/-A/-X.

**Lección:** *tcpdump es la navaja suiza del análisis de tráfico: con filtros simples (`icmp`, `arp`, `port 53`) y avanzados (`tcp[tcpflags] == tcp-rst`, `greater`) y el flag `-e` para nivel de enlace, cualquier pcap se puede diseccionar sin abrir Wireshark.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1036 (Masquerading) - herramientas de análisis de tráfico en laboratorio.

**Fuente:** [TryHackMe - Tcpdump_ The Basics](https://tryhackme.com/room/tcpdumpthebasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.