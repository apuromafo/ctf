# Wireshark 101

| **Dificultad** | Easy |
| **Tipo** | Sala práctica (análisis de tráfico) |
| **Slug** | `wireshark` |
| **Link** | [TryHackMe](https://tryhackme.com/room/wireshark) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Wireshark / pcap / ARP / ICMP / DNS / HTTP / HTTPS / display filters / User-Agent / transaction ID |
| **Impacto** | Sala de introducción a Wireshark: desde la instalación y sus filtros hasta la lectura de capturas reales. Se analizan paquetes ARP (Opcode Request, MAC de origen, las 4 respuestas -Reply- de la captura), ICMP (types 8/0, timestamp y la secuencia de datos hexadecimal de un ping), DNS (la consulta `8.8.8.8.in-addr.arpa`, `www.wireshark.org` y su Transaction ID), HTTP (porcentaje del tráfico, servidor, User-Agent y URIs completas) y HTTPS (`apache_pb.png`, `back.gif` y el User-Agent de Firefox sobre localhost). |

---

**Contexto:** La sala enseña Wireshark con ejercicios con capturas de ejemplo. En el primer análisis (ARP) se identifica el Opcode `Request (1)` del paquete 6, la MAC origen `80:fb:06:f0:45:d7` del paquete 19, los paquetes de respuesta (Reply) `76,400,459,520` y la IP `10.251.23.1` asociada a esa MAC. En el segundo (ICMP/echo request-reply) el paquete 4 es de tipo `8` (echo request), el 5 de tipo `0` (echo reply), el timestamp del paquete 12 es `May 30, 2013` y el paquete 18 contiene la cadena de datos `08090a0b...` completa. En DNS, la consulta del paquete 1 es `8.8.8.8.in-addr.arpa` (PTR), el paquete 26 consulta `www.wireshark.org` con Transaction ID `0x2c58`. En HTTP se obtiene desde el porcentaje de DNS (`4.7`) hasta la URI completa de la solicitud. En HTTPS, las URIs son `https://localhost/icons/apache_pb.png` (paquete 31) y `https://localhost/icons/back.gif` (paquete 50) con el User-Agent de Firefox.

## Solucionario

### Task 1: Introducción

**Explicación:** Presenta Wireshark como analizador de protocolos y la estructura de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Instalación de Wireshark

**Explicación:** Instalación del paquete en tu máquina (Windows/Linux) para seguir los ejercicios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Instala Wireshark en tu equipo. | `No answer needed` |

### Task 3: Interfaz y captura

**Explicación:** Familiarización con la interfaz, la selección de interfaz de red y la captura de tráfico.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Practica la captura de tráfico con la interfaz de Wireshark. | `No answer needed` |

### Task 4: Filtros de visualización

**Explicación:** Uso de los display filters (`ip.addr`, `tcp.port`, etc.) en la barra de filtros.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Practica los filtros de visualización de la captura. | `No answer needed` |

### Task 5: Seguimiento de flujos y ojo de colores

**Explicación:** Las herramientas de seguimiento de flujo (Follow TCP/UDP stream) y los colores de la lista de paquetes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Practica el seguimiento de flujos TCP/UDP. | `No answer needed` |

### Task 6: Primer análisis: preparación

**Explicación:** Preparación de la captura de ejemplo y las preguntas del primer análisis de paquetes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Prepara la captura asignada para los primeros ejercicios. | `No answer needed` |

### Task 7: Análisis de paquetes 1 (ARP)

**Explicación:** En la captura ARP, el paquete 6 es una petición (Request). El paquete 19 es una respuesta con MAC de origen `80:fb:06:f0:45:d7`; los paquetes `76,400,459,520` son las respuestas (Reply) y la IP vinculada a la MAC que pregunta es `10.251.23.1`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el Opcode del paquete 6? | `Request (1)` |
| 2 | ¿Cuál es la dirección MAC de origen del paquete 19? | `80:fb:06:f0:45:d7` |
| 3 | ¿Qué 4 paquetes son paquetes Reply (respuesta)? | `76,400,459,520` |
| 4 | ¿Qué dirección IP está en `80:fb:06:f0:45:d7`? | `10.251.23.1` |

### Task 8: Análisis de paquetes 2 (ICMP)

**Explicación:** En la captura ICMP el paquete 4 es un echo request (type `8`) y el paquete 5 un echo reply (type `0`). El timestamp del paquete 12 es `May 30, 2013` y el paquete 18 contiene la secuencia de datos hexadecimal completa del ping.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el type del paquete 4? | `8` |
| 2 | ¿Cuál es el type del paquete 5? | `0` |
| 3 | ¿Cuál es el timestamp del paquete 12 (mes día, año)? | `May 30, 2013` |
| 4 | ¿Cuál es la cadena de datos completa del paquete 18? | `08090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637` |

### Task 9: Análisis de paquetes 3 (preparación)

**Explicación:** Preparación de la siguiente captura y las preguntas sobre protocolos en uso.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee y prepara el siguiente archivo de captura. | `No answer needed` |

### Task 10: Análisis de paquetes 4 (DNS)

**Explicación:** La consulta del paquete 1 es un PTR de `8.8.8.8.in-addr.arpa`. El paquete 26 consulta el sitio `www.wireshark.org` y su Transaction ID es `0x2c58`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué dominio se consulta en el paquete 1? | `8.8.8.8.in-addr.arpa` |
| 2 | ¿Qué sitio se consulta en el paquete 26? | `www.wireshark.org` |
| 3 | ¿Cuál es el Transaction ID del paquete 26? | `0x2c58` |

### Task 11: Análisis de paquetes 5 (HTTP)

**Explicación:** En la captura HTTP, el porcentaje de tráfico DNS de la captura es `4.7`; la dirección del servidor que responde es `145.254.160.237`; el User-Agent del paquete 4 es el de Internet Explorer (`Mozilla/5.0 ... Gecko/20040113`); la URI completa del paquete 18 es una solicitud de publicidad de pagead2 con la URL de destino embebida; el dominio consultado en el paquete 38 es `www.ethereal.com` y su URI completa es `http://www.ethereal.com/download.html`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué porcentaje de paquetes de la captura corresponde a DNS? | `4.7` |
| 2 | ¿Cuál es la IP del servidor (endpoint) que responde? | `145.254.160.237` |
| 3 | ¿Cuál es el User-Agent del paquete 4? | `Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6) Gecko/20040113\r\n` |
| 4 | ¿Cuál es la URI de petición completa del paquete 18? | `http://pagead2.googlesyndication.com/pagead/ads?client=ca-pub-2309191948673629&random=1084443430285&lmt=1082467020&format=468x60_as&output=html&url=http://www.ether.eal.com/.download.html&.color_bg=F_FFFFF&color_tex_t=333333&color_li_nk=000000&color_u_rl=666633&color__border=666633` |
| 5 | ¿Qué dominio se consulta en el paquete 38? | `www.ethereal.com` |
| 6 | ¿Cuál es la URI completa del paquete 38? | `http://www.ethereal.com/download.html` |

### Task 12: Análisis de paquetes 6 (HTTPS)

**Explicación:** En la captura HTTPS, el paquete 31 solicita `https://localhost/icons/apache_pb.png` y el paquete 50 `https://localhost/icons/back.gif`, con el User-Agent de Firefox `Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.2`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la URI de petición completa del paquete 31? | `https://localhost/icons/apache_pb.png` |
| 2 | ¿Cuál es la URI de petición completa del paquete 50? | `https://localhost/icons/back.gif` |
| 3 | ¿Cuál es el User-Agent del paquete 50? | `Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.2\r\n` |

### Task 13: Extensiones y herramientas

**Explicación:** Extensiones útiles, exportación de objetos y estadísticas de Wireshark.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee las extensiones y herramientas adicionales de Wireshark. | `No answer needed` |

### Task 14: Conclusión

**Explicación:** Resumen de la sala y siguientes pasos (sala "Wireshark: The Basics" para continuar).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. | `No answer needed` |

---

**Metodología:** instalación de Wireshark → display filters → apertura de las capturas → consulta de campos por paquete (Opcode, MAC, type, timestamp, Transaction ID, URI, User-Agent) → correlación de respuestas ARP/ICMP/DNS/HTTP/HTTPS.
**Learning chain:** interfaz y filtros → análisis ARP → análisis ICMP → análisis DNS → análisis HTTP → análisis HTTPS → cierre.
**MITRE ATT&CK:** T1040 (Network Sniffing), T1071.001 (Application Layer Protocol: Web), T1048.003 (Exfiltration Over Alternative Protocol: DNS), T1071.003 (Mail Protocols)
**Fuente:** [TryHackMe - Wireshark 101](https://tryhackme.com/room/wireshark)