# OSI Model

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Info | Walkthrough | `osimodelzi` | https://tryhackme.com/room/osimodelzi | 00 Level Info | TryHackMe | Modelo OSI / capas / protocolos / encapsulación / TCP/UDP | Explicación completa del modelo OSI de 7 capas, sus protocolos y el proceso de encapsulamiento de datos |

---

**Contexto:** La sala explica el modelo de referencia OSI (Open Systems Interconnection) capa por capa: desde la capa física hasta la de aplicación, pasando por los protocolos que trabajan en cada nivel, el concepto de encapsulación y los identificadores de capa. Es una base teórica fundamental para entender cómo viajan los datos en redes y donde se sitúan protocolos como IP, TCP, UDP o HTTP.

> **ES:** Recorrido por las 7 capas del modelo OSI con sus protocolos característicos, el encapsulado de datos y una flag intermedia por completar la demostración.
> **EN:** A tour through the 7 layers of the OSI model with their characteristic protocols, data encapsulation and an intermediate flag for completing the demo.

## Solucionario

### Task 1: Introducción al modelo OSI / Introduction to the OSI model

**Explicación:** Se presenta el modelo OSI como marco conceptual para estandarizar la comunicación en red. Se repasa su denominación completa (Open Systems Interconnection), el número total de capas (7) y el proceso mediante el cual los datos se envuelven en cada nivel, conocido como encapsulación.

```text
1. 1. Open Systems Interconnection
   2. 7
   3. encapsulation
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el modelo? / What is the model called? | `Open Systems Interconnection` |
| 2 | ¿Cuántas capas tiene? / How many layers does it have? | `7` |
| 3 | ¿Cómo se llama el proceso de envolver los datos? / What is the process of wrapping data called? | `encapsulation` |

### Task 2: Capa 1 - Física / Layer 1 - Physical

**Explicación:** La capa física se encarga de la transmisión en bruto de bits por el medio. Sus elementos característicos son el tipo de señalización (binaria), los medios de transmisión (por ejemplo, cables Ethernet) y los dispositivos que trabajan en este nivel.

```text
2. 1. Physical
   2. Binary
   3. Ethernet Cables
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué capa trabaja con el hardware físico? / Which layer works with physical hardware? | `Physical` |
| 2 | ¿En qué formato se transmiten los datos? / In what format are data transmitted? | `Binary` |
| 3 | ¿Con qué elemento se transmite físicamente? / Which element is used to physically transmit? | `Ethernet Cables` |

### Task 3: Capa 2 - Enlace de datos / Layer 2 - Data Link

**Explicación:** La capa de enlace de datos transfiere datos entre nodos en la misma red local. Sus protagonistas son la propia capa y los dispositivos de direccionamiento a nivel de hardware, como las tarjetas de red (Network Interface Card).

```text
3. 1. Data Link
   2. Network Interface Card
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué capa se encarga de la comunicación local? / Which layer handles local communication? | `Data Link` |
| 2 | ¿Qué dispositivo trabaja en esta capa? / What device works at this layer? | `Network Interface Card` |

### Task 4: Capa 3 - Red / Layer 3 - Network

**Explicación:** La capa de red se encarga del direccionamiento lógico y el enrutamiento entre redes. Trabaja con direcciones IP y protocolos de enrutamiento como OSPF (Open Shortest Path First) y RIP (Routing Information Protocol).

```text
4. 1. Network
   2. Y
   3. Open Shortest Path First
   4. Routing Information Protocol
   5. IP Addresses
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué capa enruta entre redes? / Which layer routes between networks? | `Network` |
| 2 | ¿Pertenece a esta capa? / Does it belong to this layer? | `Y` |
| 3 | ¿Qué protocolo usa primero la ruta más corta? / Which protocol uses the shortest path first? | `Open Shortest Path First` |
| 4 | ¿Qué protocolo usa un enrutamiento simple por saltos? / Which protocol uses simple hop routing? | `Routing Information Protocol` |
| 5 | ¿Con qué direcciones trabaja? / What addresses does it work with? | `IP Addresses` |

### Task 5: Capa 4 - Transporte / Layer 4 - Transport

**Explicación:** La capa de transporte proporciona comunicación extremo a extremo. Sus protocolos principales son TCP (Transmission Control Protocol, orientado a conexión y fiable) y UDP (User Datagram Protocol, sin conexión). Según la necesidad de fiabilidad o velocidad se elige uno u otro.

```text
5. 1. Transport
   2. Transmission Control Protocol
   3. User Datagram Protocol
   4. TCP
   5. UDP
   6. TCP
   7. TCP
   8. UDP
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué capa garantiza la entrega fiable? / Which layer guarantees reliable delivery? | `Transport` |
| 2 | ¿Qué protocolo es orientado a conexión? / Which protocol is connection-oriented? | `Transmission Control Protocol` |
| 3 | ¿Qué protocolo es sin conexión? / Which protocol is connectionless? | `User Datagram Protocol` |
| 4 | ¿Cuál es fiable y ordenado? / Which one is reliable and ordered? | `TCP` |
| 5 | ¿Cuál es rápido y sin garantías? / Which one is fast and best-effort? | `UDP` |
| 6 | ¿Cuál usa establecimiento de conexión? / Which one uses connection establishment? | `TCP` |
| 7 | ¿Cuál reintenta la pérdida de datos? / Which one retries lost data? | `TCP` |
| 8 | ¿Cuál no reintenta los datos perdidos? / Which one does not retry lost data? | `UDP` |

### Task 6: Capa 5 - Sesión / Layer 5 - Session

**Explicación:** La capa de sesión establece, mantiene y termina las sesiones de comunicación entre aplicaciones. Tanto el nombre de la capa como el concepto que gestiona (la sesión) son la respuesta de esta tarea.

```text
6. 1. Session
   2. Session
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué capa maneja las sesiones? / Which layer manages sessions? | `Session` |
| 2 | ¿Qué concepto gestiona? / What concept does it manage? | `Session` |

### Task 7: Capa 6 - Presentación / Layer 6 - Presentation

**Explicación:** La capa de presentación se encarga de la traducción, compresión y cifrado de los datos para que sean entendibles por la capa de aplicación. Se le asocia la figura del traductor (translator).

```text
7. 1. Presentation
   2. Translator
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué capa traduce y da formato a los datos? / Which layer translates and formats data? | `Presentation` |
| 2 | ¿Con qué figura se le asocia? / What figure is it associated with? | `Translator` |

### Task 8: Capa 7 - Aplicación / Layer 7 - Application

**Explicación:** La capa de aplicación es la más cercana al usuario y proporciona los servicios de red a las aplicaciones. Incluye los protocolos y las interfaces gráficas con las que interactúa el usuario, como la Graphical User Interface (GUI).

```text
8. 1. Application
   2. Graphical User Interface
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué capa es la más cercana al usuario? / Which layer is closest to the user? | `Application` |
| 2 | ¿Qué interfaz usa el usuario? / What interface does the user use? | `Graphical User Interface` |

### Task 9: Flag de la demo / Demo flag

**Explicación:** Al completar la demostración interactiva de las capas se libera una flag que confirma haber entendido el recorrido de los datos a través del modelo OSI.

```text
9. THM{OSI_DUNGEON_ESCAPED}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la demo? / What is the demo flag? | `THM{OSI_DUNGEON_ESCAPED}` |

### Task 10: Cierre / Conclusion

**Explicación:** Recapitulación final de las 7 capas del modelo OSI y su papel conjunto. Solamente se revisa el contenido ya visto, sin necesidad de responder nada.

```text
10. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Terminar la sala. / Finish the room. | No answer needed |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el modelo? / What is the model called? | `Open Systems Interconnection` |
| 2 | ¿Cuántas capas tiene? / How many layers does it have? | `7` |
| 3 | ¿Cómo se llama el proceso de envolver los datos? / What is the process of wrapping data called? | `encapsulation` |
| 4 | ¿Qué capa trabaja con el hardware físico? / Which layer works with physical hardware? | `Physical` |
| 5 | ¿En qué formato se transmiten los datos? / In what format are data transmitted? | `Binary` |
| 6 | ¿Con qué elemento se transmite físicamente? / Which element is used to physically transmit? | `Ethernet Cables` |
| 7 | ¿Qué capa se encarga de la comunicación local? / Which layer handles local communication? | `Data Link` |
| 8 | ¿Qué dispositivo trabaja en esta capa? / What device works at this layer? | `Network Interface Card` |
| 9 | ¿Qué capa enruta entre redes? / Which layer routes between networks? | `Network` |
| 10 | ¿Pertenece a esta capa? / Does it belong to this layer? | `Y` |
| 11 | ¿Qué protocolo usa primero la ruta más corta? / Which protocol uses the shortest path first? | `Open Shortest Path First` |
| 12 | ¿Qué protocolo usa un enrutamiento simple por saltos? / Which protocol uses simple hop routing? | `Routing Information Protocol` |
| 13 | ¿Con qué direcciones trabaja? / What addresses does it work with? | `IP Addresses` |
| 14 | ¿Qué capa garantiza la entrega fiable? / Which layer guarantees reliable delivery? | `Transport` |
| 15 | ¿Qué protocolo es orientado a conexión? / Which protocol is connection-oriented? | `Transmission Control Protocol` |
| 16 | ¿Qué protocolo es sin conexión? / Which protocol is connectionless? | `User Datagram Protocol` |
| 17 | ¿Cuál es fiable y ordenado? / Which one is reliable and ordered? | `TCP` |
| 18 | ¿Cuál es rápido y sin garantías? / Which one is fast and best-effort? | `UDP` |
| 19 | ¿Cuál usa establecimiento de conexión? / Which one uses connection establishment? | `TCP` |
| 20 | ¿Cuál reintenta la pérdida de datos? / Which one retries lost data? | `TCP` |
| 21 | ¿Cuál no reintenta los datos perdidos? / Which one does not retry lost data? | `UDP` |
| 22 | ¿Qué capa maneja las sesiones? / Which layer manages sessions? | `Session` |
| 23 | ¿Qué concepto gestiona? / What concept does it manage? | `Session` |
| 24 | ¿Qué capa traduce y da formato a los datos? / Which layer translates and formats data? | `Presentation` |
| 25 | ¿Con qué figura se le asocia? / What figure is it associated with? | `Translator` |
| 26 | ¿Qué capa es la más cercana al usuario? / Which layer is closest to the user? | `Application` |
| 27 | ¿Qué interfaz usa el usuario? / What interface does the user use? | `Graphical User Interface` |
| 28 | ¿Cuál es la flag de la demo? / What is the demo flag? | `THM{OSI_DUNGEON_ESCAPED}` |
| 29 | Terminar la sala. / Finish the room. | No answer needed |

---

**Metodología:** Estudiar el modelo OSI capa por capa desde la física hasta la aplicación, identificar el protocolo o dispositivo característico de cada nivel, comprender el proceso de encapsulación y completar la demo para obtener la flag final.

### Cadena de ataque / Attack Chain

```text
OSI intro (7 capas / encapsulación) -> Física (Binary / Ethernet) -> Enlace (NIC) -> Red (IP / OSPF / RIP) -> Transporte (TCP / UDP) -> Sesión -> Presentación → Aplicación (GUI) -> demo -> THM{OSI_DUNGEON_ESCAPED}
```

**Learning chain:** Modelo OSI -> 7 capas -> Encapsulación -> Protocolos por capa (IP, OSPF, RIP, TCP, UDP) -> Dispositivos y medios -> Demo interactiva -> Flag

**Lección:** *El modelo OSI organiza la comunicación en red en 7 capas bien definidas; saber qué protocolo y dispositivo vive en cada nivel permite diagnosticar dónde falla y qué tecnología interviene en cada tramo de una conexión.*

**MITRE ATT&CK:** N/A (sala educativa de fundamentos de redes)

**Fuente:** [TryHackMe - OSI Model](https://tryhackme.com/room/osimodelzi)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.