# Introductory Networking

| **Dificultad** | Easy |
| **Tipo** | Conceptos de redes (teórico-práctico) |
| **Slug** | `introtonetworking` |
| **Link** | [TryHackMe](https://tryhackme.com/room/introtonetworking) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Modelo OSI / Modelo TCP/IP / Encapsulación / Three-way handshake / ping / traceroute / whois / DNS |
| **Impacto** | Sala introductoria de redes: cubre el modelo OSI y su encapsulación, el modelo TCP/IP, el protocolo TCP y su three-way handshake, y las herramientas de diagnóstico y consulta (ping, traceroute, whois y DNS) con preguntas de investigación práctica. |

---

**Contexto:** La sala explica los fundamentos de las redes informáticas. Comienza con el modelo OSI: qué hace cada una de sus capas y cómo se encapsula la información (Frames, Datagrams, De-encapsulation, trailer de la capa de enlace). Después compara el modelo TCP/IP con el OSI y detalla el protocolo TCP orientado a conexión (SYN, SYN/ACK y ACK). Finaliza con la práctica de herramientas: ping y sus opciones (`-i`, `-4`, `-v`), traceroute y sus switches (`-i`, `-T`), la consulta whois para dominios como facebook.com y microsoft.com, y el funcionamiento del DNS (servidor recursivo, TLD, archivo de hosts y TTL).

## Solucionario

### Task 1: Comenzando

**Explicación:** Despliegue de la máquina atacante (AttackBox u otra) para realizar la parte práctica con ping, traceroute y whois.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega el atacante y haz clic en "Start Machine" para comenzar. | `No answer needed` |

### Task 2: El modelo OSI

**Explicación:** Las 7 capas OSI: la capa 4 (Transport) elige TCP o UDP; la capa 2 (Data Link) comprueba integridad y formatea los datos; la capa 1 (Physical) transmite/recibe bits; la capa 6 (Presentation) cifra/transforma; la capa 5 (Session) mantiene el diálogo; la capa 7 (Application) atiende a las aplicaciones (FTP); y la capa 3 (Network) hace el direccionamiento lógico. Los datos TCP en caja se llaman `Segments`; el streaming usa `UDP`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué capa elige enviar los datos por TCP o UDP? | `4` |
| 2 | ¿Qué capa comprueba la información recibida para asegurarse de que no se ha corrompido? | `2` |
| 3 | ¿En qué capa se formatean los datos para preparar su transmisión? | `2` |
| 4 | ¿Qué capa transmite y recibe los datos? | `1` |
| 5 | ¿Qué capa cifra, comprime o transforma de otra forma los datos iniciales para darles un formato estandarizado? | `6` |
| 6 | ¿Qué capa realiza el seguimiento de las comunicaciones entre el host y los ordenadores receptores? | `5` |
| 7 | ¿Qué capa acepta las peticiones de comunicación de las aplicaciones? | `7` |
| 8 | ¿Qué capa gestiona el direccionamiento lógico? | `3` |
| 9 | Al enviar datos por TCP, ¿cómo llamarías a las piezas de datos de "tamaño de bocado"? | `Segments` |
| 10 | [Investigación] ¿Con qué capa se comunicaría el protocolo FTP? | `7` |
| 11 | ¿Qué protocolo de la capa de transporte sería el más adecuado para transmitir un video en directo? | `UDP` |

### Task 3: Encapsulación

**Explicación:** En la encapsulación, los datos en la capa 2 se llaman `Frames`; con UDP se llaman `Datagrams` (con TCP, Segments). El receptor hace `De-encapsulation`. La única capa que añade un trailer es la `Data Link` (FCS), y la encapsulación sí aporta una capa extra de seguridad (`Aye`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo te referirías a los datos en la capa 2 del proceso de encapsulación (con el modelo OSI)? | `Frames` |
| 2 | ¿Cómo te referirías a los datos en la capa 4 del proceso de encapsulación si se ha seleccionado el protocolo UDP? | `Datagrams` |
| 3 | ¿Qué proceso realizaría un ordenador sobre un mensaje recibido? | `De-encapsulation` |
| 4 | ¿Cuál es la única capa del modelo OSI que añade un trailer durante la encapsulación? | `Data Link` |
| 5 | ¿La encapsulación aporta una capa extra de seguridad? (Aye/Nay) | `Aye` |

### Task 4: El modelo TCP/IP

**Explicación:** El modelo `TCP/IP` (4 capas) se introdujo antes que el OSI: su capa `Transport` equivale a la Transport del OSI; la `Application` cubre Session/Presentation/Application; la `Network Interface` cubre Data Link y `Physical`; y la `Internet` cubre la capa Network. TCP es orientado a conexión (`Connection-based`): `SYN` = Synchronise, segundo paso `SYN/ACK` y cierre con `ACK` (Acknowledgement).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué modelo se introdujo primero, el OSI o el TCP/IP? | `TCP/IP` |
| 2 | ¿Qué capa del modelo TCP/IP cubre la funcionalidad de la capa Transport del modelo OSI (nombre completo)? | `Transport` |
| 3 | ¿Qué capa del modelo TCP/IP cubre la funcionalidad de la capa Session del modelo OSI (nombre completo)? | `Application` |
| 4 | La capa Network Interface del modelo TCP/IP cubre la funcionalidad de dos capas del modelo OSI: Data Link y ¿cuál (nombre completo)? | `Physical` |
| 5 | ¿Qué capa del modelo TCP/IP gestiona la funcionalidad de la capa Network del modelo OSI? | `Internet` |
| 6 | ¿Qué tipo de protocolo es TCP? | `Connection-based` |
| 7 | ¿Qué significa SYN? | `Synchronise` |
| 8 | ¿Cuál es el segundo paso del three-way handshake? | `SYN/ACK` |
| 9 | ¿Cuál es el nombre corto del segmento "Acknowledgement" en el three-way handshake? | `ACK` |

### Task 5: Herramientas de red - Ping

**Explicación:** `ping bbc.co.uk` responde con la IPv4 `217.160.0.152`. Opciones de ping: `-i` cambia el intervalo entre peticiones, `-4` fuerza IPv4 y `-v` verbosidad.

```bash
ping bbc.co.uk
ping -i 2 -v bbc.co.uk
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando usarías para hacer ping al sitio web bbc.co.uk? | `ping bbc.co.uk` |
| 2 | ¿Cuál es la dirección IPv4 que responde? | `217.160.0.152` |
| 3 | ¿Qué switch permite cambiar el intervalo de envío de las peticiones de ping? | `-i` |
| 4 | ¿Qué switch restringe las peticiones a IPv4? | `-4` |
| 5 | ¿Qué switch proporciona una salida más verbosa? | `-v` |

### Task 6: Herramientas de red - Traceroute

**Explicación:** `traceroute` traza la ruta hasta un destino. Switches: `-i` especifica la interfaz y `-T` usa peticiones TCP SYN. En Windows, traceroute por defecto usa ICMP (capa `Internet` del TCP/IP).

```bash
traceroute -T target.com
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Utiliza traceroute para trazar la ruta a un destino. | `No answer needed` |
| 2 | ¿Qué switch usarías para especificar una interfaz al usar Traceroute? | `-i` |
| 3 | ¿Qué switch usarías para usar peticiones TCP SYN al trazar la ruta? | `-T` |
| 4 | [Pensamiento lateral] ¿En qué capa del modelo TCP/IP se ejecuta traceroute por defecto (Windows)? | `Internet` |

### Task 7: Herramientas de red - WHOIS

**Explicación:** `whois facebook.com` revela que su registrante tiene el código postal `94025` y que el dominio se registró el `29/03/1997`. `whois microsoft.com` muestra que el registrante está en `Redmond`, cerca del `Bellevue Golf Course`, y da el email técnico `msnhst@microsoft.com`.

```bash
whois facebook.com
whois microsoft.com
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Consume la herramienta whois contra un dominio. | `No answer needed` |
| 2 | ¿Cuál es el código postal del registrante de facebook.com? | `94025` |
| 3 | ¿Cuándo se registró por primera vez el dominio facebook.com (formato: DD/MM/YYYY)? | `29/03/1997` |
| 4 | Realiza la consulta whois sobre el dominio que prefieras. | `No answer needed` |
| 5 | ¿En qué ciudad se basa el registrante? | `Redmond` |
| 6 | [OSINT] ¿Cómo se llama el campo de golf cercano a la dirección del registrante de microsoft.com? | `Bellevue Golf Course` |
| 7 | ¿Cuál es el email técnico registrado para microsoft.com? | `msnhst@microsoft.com` |

### Task 8: Herramientas de red - DNS

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa DNS? | `Domain Name System` |
| 2 | ¿Cuál es el primer tipo de servidor DNS que consultaría tu ordenador al buscar un dominio? | `Recursive` |
| 3 | ¿Qué tipo de servidor DNS contiene registros específicos para las extensiones de dominio (p. ej. .com, .co.uk)? Usa la versión larga del nombre. | `Top-Level Domain` |
| 4 | ¿Dónde buscaría tu ordenador en primer lugar la dirección IP de un dominio? | `Hosts File` |
| 5 | [Investigación] Google ejecuta dos servidores DNS públicos. Uno se puede consultar con la IP 8.8.8.8; ¿cuál es la IP del otro? | `8.8.4.4` |
| 6 | Si una consulta DNS tiene un TTL de 24 horas, ¿qué número mostraría la consulta "dig"? | `86400` |

### Task 9: Poniéndolo en práctica

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realiza la actividad práctica final de la sala. | `No answer needed` |

---

**Metodología:** La parte teórica recorre el modelo OSI capa por capa (qué capa elige TCP/UDP, verifica, formatea, transmite o direcciona) y el proceso de encapsulación/desencapsulación con sus términos (Frames, Datagrams y trailer de la capa Data Link). Después se compara el modelo TCP/IP con el OSI y se analiza el three-way handshake del protocolo TCP orientado a conexión. La parte práctica aplica ping (opciones `-i`, `-4`, `-v`) sobre bbc.co.uk, traceroute (`-i`, `-T`), consultas whois a facebook.com y microsoft.com para extraer datos de registro, y consultas DNS (servidor recursivo, TLD, archivo de hosts, servidores públicos de Google y cálculo de TTL).

**Learning chain:** modelo OSI → encapsulación → modelo TCP/IP → three-way handshake → ping → traceroute → whois → DNS.

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1016 (System Network Configuration Discovery), T1589.001 (Gather Victim Identity Information: Credentials)

**Fuente:** [TryHackMe - Introductory Networking](https://tryhackme.com/room/introtonetworking)