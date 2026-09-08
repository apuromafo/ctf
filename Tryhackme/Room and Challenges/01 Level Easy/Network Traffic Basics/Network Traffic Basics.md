# Network Traffic Analysis Basics

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `networktrafficbasics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/networktrafficbasics) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=networktrafficbasics` + walkthroughs de Gensane) |
| **Componentes** | Wireshark / HTTP / DNS / TLS / Kerberos / SMB |
| **Impacto** | Fundamentos de análisis de tráfico de red: visibilidad de comunicaciones, detección de DNS tunneling y de session hijacking |

---

**Contexto:** El **Análisis de Tráfico de Red (NTA)** es el proceso de capturar, inspeccionar y analizar datos a medida que fluyen por una red para obtener visibilidad total de las comunicaciones. Esta sala cubre desde la teoría del stack TCP/IP hasta la identificación de ataques como DNS Tunneling y secuestro de sesiones.

**Nota de la sala:** Room gratuita (pre-Security), creadores: [tryhackme] y [Gensane]. Etiquetas: `#NTA` `#Networking` `#SOC-L1` `#TrafficAnalysis` `#Wireshark`.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Continue to discover the purpose of network traffic analysis. | `No answer needed` |

**Explicación:** Introducción al módulo de NTA. El análisis de tráfico da visibilidad sobre quién habla con quién, qué protocolos se usan y qué datos fluyen.

### Task 2: What is the Purpose of Network Traffic Analysis?

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the technique used to smuggle C2 commands via DNS? | `DNS tunneling` |

**Explicación:** El DNS tunneling oculta comandos de C2 dentro de consultas DNS: el atacante codifica instrucciones para la máquina comprometida en registros de subdominios aparentemente legítimos.

### Task 3: What Network Traffic Can We Observe?

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the size of the ZIP attachment included in the HTTP response? (In bytes). | `10485760` |
| 2 | Which attack do attackers use to try to evade an IDS? | `fragmentation` |
| 3 | What field in the TCP header can we use to detect session hijacking? | `sequence number` |

**Explicación:** Revisar el tamaño exacto de objetos (ZIP de 10485760 bytes), detectar fragmentación de paquetes para evadir IDS y, en la capa de transporte, vigilar el **sequence number** del TCP, signo de session hijacking.

### Task 4: Network Traffic Sources and Flows

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which category of devices generates the most traffic in a network? | `endpoint` |
| 2 | Before an SMB session can be established, which service needs to be contacted first for authentication? | `kerberos` |
| 3 | What does TLS stand for? | `Transport Layer Security` |

**Explicación:** Los **endpoints** son los dispositivos que más tráfico generan en una red; en Windows, el SMB necesita antes autenticación **Kerberos**; TLS significa **Transport Layer Security**.

### Task 5: How Can We Observe Network Traffic?

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag found in the HTTP traffic in scenario 1? | `THM{FoundTheMalware}` |
| 2 | What is the flag found in the DNS traffic in scenario 2? | `THM{C2CommandFound}` |

**Explicación:** Analizar capturas con Wireshark: en el escenario 1 el tráfico HTTP contiene `THM{FoundTheMalware}` y en el 2 el tráfico DNS contiene `THM{C2CommandFound}`.

### Task 6: Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I am ready to do some traffic analysis! | `No answer needed` |

**Explicación:** Conclusión del módulo. Ya tienes los fundamentos para comenzar el análisis de tráfico de red.

**Metodología:**
1. **Propósito del NTA:** el análisis de tráfico da visibilidad sobre quién habla con quién, qué protocolos se usan y qué datos fluyen; el DNS tunneling oculta comandos de C2 dentro de consultas DNS.
2. **Qué observar:** revisar el tamaño exacto de objetos (ZIP de 10485760 bytes), detectar fragmentación de paquetes para evadir IDS y, en la capa de transporte, vigilar el **sequence number** del TCP, signo de session hijacking.
3. **Fuentes y flujos:** los **endpoints** son los dispositivos que más tráfico generan; en Windows, el SMB necesita antes autenticación **Kerberos**; TLS significa **Transport Layer Security**.
4. **Cómo observar:** analizar capturas con Wireshark: en el escenario 1 el tráfico HTTP contiene `THM{FoundTheMalware}` y en el 2 el tráfico DNS contiene `THM{C2CommandFound}`.

**Learning chain:** teoría TCP/IP → propósito del NTA (DNS tunneling) → tráfico observable (ZIP/fragmentación/seq hijacking) → fuentes y flujos (endpoints, Kerberos, TLS) → Wireshark: flags HTTP → THM{FoundTheMalware}, DNS → THM{C2CommandFound}

**MITRE ATT&CK:** T1071.004 (Application Layer Protocol: DNS), T1027 (Obfuscated Files or Information), T1563 (Remote Service Session Hijacking)

**Fuente:** [TryHackMe - Network Traffic Analysis Basics](https://tryhackme.com/room/networktrafficbasics)
