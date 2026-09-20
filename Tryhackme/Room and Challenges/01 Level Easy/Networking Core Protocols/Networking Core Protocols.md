# Networking Core Protocols

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `networkingcoreprotocols` | https://tryhackme.com/room/networkingcoreprotocols | 01 Level Easy | TryHackMe | DNS (AAAA/MX), HTTP, FTP, correo (POP3/IMAP, Dovecot), telnet | Formativo — interacción manual con protocolos core (DNS, HTTP, FTP y correo) y obtención de flags de validación |

---

**Contexto:** Sala de protocolos núcleo de red: consultas DNS con registros `AAAA` y `MX`, fechas de registro de dominios, interacción manual con HTTP (flag `THM{TELNET-HTTP}`) y FTP (flag `THM{FAST-FTP}`, comandos `DATA` y la terminación de transferencia con `.`), y correo electrónico con Dovecot y comandos IMAP como `FETCH 4 body[]`, rematando con la flag `THM{TELNET_RETR_EMAIL}`.

> **ES:** Protocolos core de red: registros DNS (AAAA/MX), fechas de domino, HTTP y FTP hablados manualmente, protocolos de correo (Dovecot, IMAP) y sus flags de validación.
> **EN:** Core networking protocols: DNS records (AAAA/MX), domain dates, hand-spoken HTTP and FTP, mail protocols (Dovecot, IMAP) and their validation flags.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Introducción de la sala sobre los protocolos núcleo de red. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Registros DNS / DNS Records

**Explicación:** Identificación de los tipos de registro DNS consultados en el ejercicio: `AAAA` y `MX`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer registro DNS indicado? | `AAAA` |
| 2 | ¿Cuál es el segundo registro DNS indicado? | `MX` |

### Task 3: Fechas de Registro / Registration Dates

**Explicación:** Fechas obtenidas de la consulta sobre los dominios del ejercicio: `1993-04-02` y `2000-01-21`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera fecha de registro indicada? | `1993-04-02` |
| 2 | ¿Cuál es la segunda fecha de registro indicada? | `2000-01-21` |

### Task 4: HTTP por Telnet / HTTP over Telnet

**Explicación:** Se prueba el protocolo HTTP manualmente: la flag que valida la interacción es `THM{TELNET-HTTP}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag valida la interacción HTTP vía telnet? | `THM{TELNET-HTTP}` |

### Task 5: FTP / FTP

**Explicación:** Se practica el protocolo FTP: la flag de validación es `THM{FAST-FTP}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag valida la práctica con FTP? | `THM{FAST-FTP}` |

### Task 6: Comandos FTP / FTP Commands

**Explicación:** Comandos y marcadores del protocolo FTP vistos en la sala: el comando `DATA` y el carácter `.` que marca la terminación de la transferencia.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando FTP se indica en el ejercicio? | `DATA` |
| 2 | ¿Qué carácter marca la terminación de una transferencia FTP? | `.` |

### Task 7: Correo Electrónico / Email

**Explicación:** Protocolos de correo del laboratorio: el servidor identificado es `Dovecot` y la flag que valida la lectura de correo es `THM{TELNET_RETR_EMAIL}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué servidor de correo se identifica en el ejercicio? | `Dovecot` |
| 2 | ¿Qué flag valida la recuperación del correo? | `THM{TELNET_RETR_EMAIL}` |

### Task 8: Comandos IMAP / IMAP Commands

**Explicación:** Comando IMAP utilizado para recuperar el cuerpo de un mensaje: `FETCH 4 body[]`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando IMAP recupera el cuerpo del mensaje 4? | `FETCH 4 body[]` |

### Task 9: Cierre / Wrap-up

**Explicación:** Cierre de la sala con repaso de los protocolos core vistos. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa los conceptos finales de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Cuál es el primer registro DNS indicado? | `AAAA` |
| 3 | ¿Cuál es el segundo registro DNS indicado? | `MX` |
| 4 | ¿Cuál es la primera fecha de registro indicada? | `1993-04-02` |
| 5 | ¿Cuál es la segunda fecha de registro indicada? | `2000-01-21` |
| 6 | ¿Qué flag valida la interacción HTTP vía telnet? | `THM{TELNET-HTTP}` |
| 7 | ¿Qué flag valida la práctica con FTP? | `THM{FAST-FTP}` |
| 8 | ¿Qué comando FTP se indica en el ejercicio? | `DATA` |
| 9 | ¿Qué carácter marca la terminación de una transferencia FTP? | `.` |
| 10 | ¿Qué servidor de correo se identifica en el ejercicio? | `Dovecot` |
| 11 | ¿Qué flag valida la recuperación del correo? | `THM{TELNET_RETR_EMAIL}` |
| 12 | ¿Qué comando IMAP recupera el cuerpo del mensaje 4? | `FETCH 4 body[]` |
| 13 | Repasa los conceptos finales de la sala. | `No answer needed` |

---

**Metodología:** Repaso de los protocolos core: consultas DNS (tipos de registro `AAAA`/`MX` y fechas de los dominios), HTTP y FTP hablados manualmente por telnet para leer banners y respuestas (comando `DATA` y el punto de fin de transferencia), y el acceso al correo con Dovecot mediante comandos IMAP/POP3 como `FETCH 4 body[]`.

### Cadena de ataque / Attack Chain

```text
DNS (AAAA/MX, fechas) -> HTTP por telnet -> flag THM{TELNET-HTTP} -> FTP (DATA, .) -> flag THM{FAST-FTP} -> correo Dovecot/IMAP -> flag THM{TELNET_RETR_EMAIL} -> FETCH 4 body[] -> cierre
```

**Learning chain:** registros DNS → fechas de dominio → HTTP manual → FTP manual → protocolos de correo → comandos IMAP.

**Lección:** *Hablar los protocolos manualmente (telnet) revela banners y flags, y demuestra por qué los analizadores de red trabajan a nivel de protocolo y no de herramienta.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1071.001 (Application Layer Protocol), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Networking Core Protocols](https://tryhackme.com/room/networkingcoreprotocols)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.