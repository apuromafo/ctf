# Networking Concepts

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `networkingconcepts` | https://tryhackme.com/room/networkingconcepts | 01 Level Easy | TryHackMe | Modelo OSI/TCP-IP, TCP/UDP, direccionamiento IP, lighttpd, telnet | Formativo — consolidación de conceptos de red y práctica con servicios de laboratorio |

---

**Contexto:** Sala de conceptos de redes: repasa las unidades de datos en las distintas capas (Frame, Datagram, Segment), el direccionamiento (validación de IPs, TCP como protocolo de transporte y capas del modelo), y cierra practicando contra un servicio real identificado como `lighttpd/1.4.63` vía telnet, con la flag `THM{TELNET_MASTER}`.

> **ES:** Conceptos fundamentales de redes: unidades de datos por capa, direccionamiento IP, protocolo TCP y práctica con un servicio de laboratorio (lighttpd) para capturar la flag.
> **EN:** Core networking concepts: per-layer data units, IP addressing, TCP protocol and hands-on practice with a lab service (lighttpd) to capture the flag.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Introducción de la sala de conceptos de redes. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Capas del Modelo / Model Layers

**Explicación:** Identificación de las capas del modelo de referencia: cuatro valores numéricos que corresponden a las funciones de red preguntadas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer valor de capa indicado en el ejercicio? | `4` |
| 2 | ¿Cuál es el segundo valor de capa indicado en el ejercicio? | `3` |
| 3 | ¿Cuál es el tercer valor de capa indicado en el ejercicio? | `6` |
| 4 | ¿Cuál es el cuarto valor de capa indicado en el ejercicio? | `2` |

### Task 3: Capa de Aplicación / Application Layer

**Explicación:** Se identifica la capa de aplicación en su nombre completo (`Application Layer`) y un valor numérico de capa (3).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la capa de aplicación en su nombre completo? | `Application Layer` |
| 2 | ¿Qué valor de capa se indica en esta parte del ejercicio? | `3` |

### Task 4: Direccionamiento IP / IP Addressing

**Explicación:** Validación de direcciones IP del ejercicio: una dirección válida (`49.69.147.197`) y una dirección inválida (`192.168.305.19`), cuyo tercer octeto supera el rango permitido.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera dirección IP evaluada en el ejercicio? | `49.69.147.197` |
| 2 | ¿Cuál es la segunda dirección IP evaluada en el ejercicio? | `192.168.305.19` |

### Task 5: Protocolo de Transporte / Transport Protocol

**Explicación:** Se identifica TCP como protocolo de transporte del ejercicio y un valor numérico adicional.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué protocolo de transporte se identifica en el ejercicio? | `TCP` |
| 2 | ¿Qué valor numérico acompaña a la respuesta del protocolo? | `65` |

### Task 6: Unidades de Datos / Data Units

**Explicación:** Se enumeran las unidades de datos según la capa del proceso de encapsulación: Frame, Datagram y Segment.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera unidad de datos indicada? | `Frame` |
| 2 | ¿Cuál es la segunda unidad de datos indicada? | `Datagram` |
| 3 | ¿Cuál es la tercera unidad de datos indicada? | `Segment` |

### Task 7: Práctica con Servicio / Hands-on Service

**Explicación:** Práctica contra el servicio de laboratorio: el banner revela el servidor `lighttpd/1.4.63` y se obtiene la flag `THM{TELNET_MASTER}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué servidor y versión revela el banner del servicio? | `lighttpd/1.4.63` |
| 2 | ¿Qué flag se obtiene en la práctica con el servicio? | `THM{TELNET_MASTER}` |

### Task 8: Cierre / Wrap-up

**Explicación:** Cierre de la sala con repaso de los conceptos de redes vistos. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa los conceptos finales de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Cuál es el primer valor de capa indicado en el ejercicio? | `4` |
| 3 | ¿Cuál es el segundo valor de capa indicado en el ejercicio? | `3` |
| 4 | ¿Cuál es el tercer valor de capa indicado en el ejercicio? | `6` |
| 5 | ¿Cuál es el cuarto valor de capa indicado en el ejercicio? | `2` |
| 6 | ¿Cuál es la capa de aplicación en su nombre completo? | `Application Layer` |
| 7 | ¿Qué valor de capa se indica en esta parte del ejercicio? | `3` |
| 8 | ¿Cuál es la primera dirección IP evaluada en el ejercicio? | `49.69.147.197` |
| 9 | ¿Cuál es la segunda dirección IP evaluada en el ejercicio? | `192.168.305.19` |
| 10 | ¿Qué protocolo de transporte se identifica en el ejercicio? | `TCP` |
| 11 | ¿Qué valor numérico acompaña a la respuesta del protocolo? | `65` |
| 12 | ¿Cuál es la primera unidad de datos indicada? | `Frame` |
| 13 | ¿Cuál es la segunda unidad de datos indicada? | `Datagram` |
| 14 | ¿Cuál es la tercera unidad de datos indicada? | `Segment` |
| 15 | ¿Qué servidor y versión revela el banner del servicio? | `lighttpd/1.4.63` |
| 16 | ¿Qué flag se obtiene en la práctica con el servicio? | `THM{TELNET_MASTER}` |
| 17 | Repasa los conceptos finales de la sala. | `No answer needed` |

---

**Metodología:** La parte teórica recorre las capas del modelo de referencia y las unidades de datos según la encapsulación (Frame, Datagram, Segment). Después se practica la validación de direcciones IP y la elección del protocolo de transporte (TCP). La parte final interacciona con el servicio de laboratorio para leer su banner (`lighttpd/1.4.63`) y capturar la flag `THM{TELNET_MASTER}`.

### Cadena de ataque / Attack Chain

```text
Teoría de capas -> unidades de datos (Frame/Datagram/Segment) -> validación de IPs -> protocolo TCP -> banner lighttpd/1.4.63 -> flag THM{TELNET_MASTER}
```

**Learning chain:** capas del modelo → encapsulación → direccionamiento IP → protocolo TCP → banner de servicio → flag.

**Lección:** *Identificar correctamente el servicio y su banner en el laboratorio consolida la teoría de redes con una validación real sobre el protocolo.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1016 (System Network Configuration Discovery), T1071.001 (Application Layer Protocol: Web)

**Fuente:** [TryHackMe - Networking Concepts](https://tryhackme.com/room/networkingconcepts)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.