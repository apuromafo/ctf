# Wireshark: Packet Operations

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `wiresharkpacketoperations` | [TryHackMe](https://tryhackme.com/room/wiresharkpacketoperations) | 01 Level Easy | TryHackMe | Wireshark / pcapng / Resolved Addresses / Conversations / Endpoints / display filters / TTL / TCP checksum | Análisis de capturas con Wireshark a nivel de paquete: estadísticas, filtros, operadores y funciones para localizar eventos de interés |

---

**Contexto:** Segunda sala de la trilogía de Wireshark, centrada en el análisis detallado de paquetes: estadísticas (Summary, Resolved Addresses, Conversations, Endpoints), filtros de visualización con operadores y funciones, búsqueda de servidores IIS, filtrado por TTL/checksum y perfiles personalizados para encontrar la aguja en el pajar.

> **ES:** La sala avanza en el manejo de Wireshark: resolver direcciones (bbc), conversaciones IPv4, endpoints (Micro-St), protocolos, filtros avanzados (TTL, puertos, GET) y perfil "Checksum Control" para detectar paquetes corruptos.
> **EN:** This room advances Wireshark skills: resolved addresses (bbc), IPv4 conversations, endpoints (Micro-St), protocol stats, advanced display filters (TTL, ports, HTTP GET) and the "Checksum Control" profile to spot bad TCP checksums.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Pregunta introductoria de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¡Empecemos! | `No answer needed` |

### Task 2: Estadísticas - Resumen / Statistics | Summary
**Explicación:** Se usan las estadísticas de Wireshark. Resolved Addresses muestra que `199.232.24.81` está vinculado al hostname que empieza por "bbc", hay 435 conversaciones IPv4, la MAC "Micro-St" transfirió 7474 bytes (k), "Kansas City" tiene 4 direcciones IP asociadas y `188.246.82.7` está vinculado a la organización AS Blicnet. Contenido original de la sala (verbatim): `199.232.24.81`, `435`, `7474`, `4`, `188.246.82.7`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Investiga las direcciones resueltas. ¿Cuál es la IP del hostname que empieza por "bbc"? | `199.232.24.81` |
| ¿Cuál es el número de conversaciones IPv4? | `435` |
| ¿Cuántos bytes (k) se transfirieron desde la dirección MAC "Micro-St"? | `7474` |
| ¿Cuál es el número de direcciones IP vinculadas con "Kansas City"? | `4` |
| ¿Qué IP está vinculada con la Organización AS "Blicnet"? | `188.246.82.7` |

### Task 3: Estadísticas - Información de protocolo / Statistics | Protocol Information
**Explicación:** Se examinan los protocolos: la dirección IPv4 destino más usada es `10.100.1.33`, el tiempo máximo de respuesta de los paquetes DNS es `0.467897` y `39` es el número de peticiones HTTP realizadas por "rad[.]msn[.]com". Contenido original de la sala (verbatim): `10.100.1.33`, `0.467897`, `39`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es la dirección IPv4 destino más usada? | `10.100.1.33` |
| ¿Cuál es el tiempo máximo de servicio de request-response de los paquetes DNS? | `0.467897` |
| ¿Cuál es el número de peticiones HTTP realizadas por "rad[.]msn[.]com"? | `39` |

### Task 4: Análisis / Analysing the packets
**Explicación:** Pregunta de transición de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Analiza los paquetes | `No answer needed` |

### Task 5: Filtros - Operadores / Filtering | Operators
**Explicación:** Se practican los operadores de filtrado: hay 81420 paquetes IP, 66 paquetes con TTL menor que 10, 632 paquetes que usan el puerto TCP 4444, 527 peticiones HTTP GET al puerto 80 y 51 consultas DNS de tipo A. Contenido original de la sala (verbatim): `81420`, `66`, `632`, `527`, `51`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Cuál es el número de paquetes IP? | `81420` |
| ¿Cuál es el número de paquetes con "TTL value less than 10"? | `66` |
| ¿Cuál es el número de paquetes que usan "TCP port 4444"? | `632` |
| ¿Cuál es el número de peticiones "HTTP GET" enviadas al puerto "80"? | `527` |
| ¿Cuál es el número de "type A DNS Queries"? | `51` |

### Task 6: Filtros - Búsqueda / Filtering | Searching
**Explicación:** Se buscan los servidores Microsoft IIS: 21 paquetes no originados en el puerto 80, 71 paquetes con "version 7.5". Además, 2235 paquetes usan los puertos 3333, 4444 o 9999, 77289 paquetes tienen números TTL pares, 34185 paquetes tienen "Bad TCP Checksum" (perfil Checksum Control) y el botón de filtro existente muestra 261 paquetes. Contenido original de la sala (verbatim): `21`, `71`, `2235`, `77289`, `34185`, `261`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| Encuentra todos los servidores Microsoft IIS. ¿Cuál es el número de paquetes que no se originaron en el "puerto 80"? | `21` |
| Encuentra todos los servidores Microsoft IIS. ¿Cuál es el número de paquetes con "version 7.5"? | `71` |
| ¿Cuál es el número total de paquetes que usan los puertos 3333, 4444 o 9999? | `2235` |
| ¿Cuál es el número de paquetes con "números TTL pares"? | `77289` |
| Cambia el perfil a "Checksum Control". ¿Cuál es el número de paquetes con "Bad TCP Checksum"? | `34185` |
| Usa el botón de filtrado existente para filtrar el tráfico. ¿Cuál es el número de paquetes mostrados? | `261` |

### Task 7: Conclusión / Conclusion
**Explicación:** Pregunta final de cierre de la sala. No requiere respuesta. Contenido original de la sala (verbatim): `No answer needed`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| ¿Preparado para continuar? | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¡Empecemos! | `No answer needed` |
| 2 | IP del hostname que empieza por "bbc" | `199.232.24.81` |
| 3 | Número de conversaciones IPv4 | `435` |
| 4 | Bytes (k) transferidos desde "Micro-St" | `7474` |
| 5 | IPs vinculadas con "Kansas City" | `4` |
| 6 | IP vinculada con la AS "Blicnet" | `188.246.82.7` |
| 7 | Dirección IPv4 destino más usada | `10.100.1.33` |
| 8 | Máximo tiempo request-response de DNS | `0.467897` |
| 9 | Peticiones HTTP de "rad[.]msn[.]com" | `39` |
| 10 | Analiza los paquetes | `No answer needed` |
| 11 | Número de paquetes IP | `81420` |
| 12 | Paquetes con TTL menor que 10 | `66` |
| 13 | Paquetes que usan TCP port 4444 | `632` |
| 14 | HTTP GET requests al puerto 80 | `527` |
| 15 | Type A DNS Queries | `51` |
| 16 | Paquetes no originados en el puerto 80 (IIS) | `21` |
| 17 | Paquetes IIS con "version 7.5" | `71` |
| 18 | Paquetes que usan puertos 3333/4444/9999 | `2235` |
| 19 | Paquetes con TTL pares | `77289` |
| 20 | "Bad TCP Checksum" packets | `34185` |
| 21 | Paquetes mostrados por el botón de filtro | `261` |
| 22 | ¿Preparado para continuar? | `No answer needed` |

---

**Metodología:** Se emplean las estadísticas de Wireshark (Summary, Resolved Addresses, Conversations, Endpoints) y filtros de visualización con operadores y funciones: `ip.ttl < 10`, `tcp.port eq 4444`, `http.request.method eq GET`, `http.server matches "IIS.*7.5"`, `tcp.port in {3333 4444 9999}`, la expresión regex para TTL pares y el perfil "Checksum Control" con `tcp.checksum.status == bad`.

### Cadena de ataque / Attack Chain

```text
Resolved addresses (bbc -> 199.232.24.81) -> Conversations (435 IPv4) -> Endpoints (Micro-St 7474k) -> Protocol info (10.100.1.33, DNS 0.467897) -> display filters: ip.ttl < 10 / tcp.port 4444 / HTTP GET / DNS type A -> http.server IIS 7.5 -> tcp.port in {3333 4444 9999} -> even TTL regex -> Checksum Control profile -> prebuilt filter button (261)
```

**Learning chain:** Wireshark statistics (Resolved Addresses, Conversations, Endpoints) --> protocol information (DNS, HTTP) --> display filters (operators) --> TTL filtering --> HTTP IIS server search --> multi-port filter --> even TTL regex --> Checksum Control profile --> bad TCP checksums --> prebuilt filter button

**Lección:** *Wireshark es mucho más que abrir un pcap: el dominio de sus estadísticas y de los filtros de visualización (operadores, funciones y perfiles) permite aislar rápidamente el evento de interés entre miles de paquetes.*

**MITRE ATT&CK:** T1071 (Application Layer Protocol)

**Fuente:** [TryHackMe - Wireshark: Packet Operations](https://tryhackme.com/room/wiresharkpacketoperations)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.