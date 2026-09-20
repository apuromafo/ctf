# Protocols and Servers

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `protocolsandservers` | https://tryhackme.com/room/protocolsandservers | 01 Level Easy | THM | Telnet, HTTP, FTP, SMTP, POP3, IMAP | Interacción directa con protocolos y servidores de red |

---

**Contexto:** Room de la ruta Security Engineer/Pre-Security que enseña los protocolos fundamentales de red: Telnet, HTTP, FTP, SMTP, POP3 e IMAP. Mediante conexiones directas con telnet y clientes FTP/mail, el participante interactúa con los servicios en su nivel más bajo, identificando puertos por defecto, recuperando flags y comprendiendo la naturaleza en texto claro de estos protocolos.

> **ES:** Room que enseña los protocolos fundamentales de red (Telnet, HTTP, FTP, SMTP, POP3, IMAP) interactuando con ellos de forma directa mediante telnet y clientes FTP/mail, recuperando flags y entendiendo su funcionamiento de bajo nivel.
> **EN:** A room teaching the fundamental network protocols (Telnet, HTTP, FTP, SMTP, POP3, IMAP) by interacting directly with them via telnet and FTP/mail clients, recovering flags and understanding their low-level operation.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se introduce el concept- del room: los datos viajan por la red en texto claro a través de protocolos, y herramientas como Wireshark y tcpdump permiten ver el tráfico. Antes de empezar, se debe conectar a la máquina por VPN o AttackBox.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's get started | `No answer needed` |

### Task 2: Telnet / Telnet

**Explicación:** Telnet es un protocolo de administración remota antiguo que transmite todo en texto claro. Se conecta por el puerto 23 por defecto y no cifra credenciales, por lo que es inseguro frente a sniffing.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the standard port used for the Telnet protocol? | `23` |

### Task 3: HTTP (Hipertexto) / HTTP (Hypertext Transfer Protocol)

**Explicación:** HTTP es el protocolo de transferencia de hipertexto que usan los navegadores. Por defecto escucha en el puerto 80, y los requests se envían en texto claro. Se descarga la página web de la máquina para localizar la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag found in the HTTP server? | `THM{e3eb0a1df437f3f97a64aca5952c8ea0}` |

### Task 4: FTP (Transferencia de archivos) / FTP (File Transfer Protocol)

**Explicación:** FTP es el protocolo de transferencia de archivos, también en texto claro, que escucha en el puerto 21. Se conecta de forma anónima y se listan los archivos del directorio para recuperar la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag found in the FTP server? | `THM{364db6ad0e3ddfe7bf0b1870fb06fbdf}` |

### Task 5: SMTP (Correo electrónico saliente) / SMTP (Simple Mail Transfer Protocol)

**Explicación:** SMTP es el protocolo de envío de correos electrónicos, escucha en el puerto 25 y se usa por telnet para interactuar con el servidor. Se lee el correo de bienvenida que contiene la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag found in the SMTP server? | `THM{5b31ddfc0c11d81eba776e983c35e9b5}` |

### Task 6: POP3 (Recepción de correo) / POP3 (Post Office Protocol)

**Explicación:** POP3 es el protocolo de recepción de correo, escucha en el puerto 110. Se conecta con telnet, se autentica y se cuenta el número de mensajes en el buzón; el banner de bienvenida revela el estado del servidor.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | After connecting to the POP3 server, what is the banner displayed? | `+OK 0 0` |
| 2 | What is the number of messages in the mailbox? | `0` |

### Task 7: IMAP (Acceso a buzones) / IMAP (Internet Message Access Protocol)

**Explicación:** IMAP permite acceder a los buzones de correo manteniendo los mensajes en el servidor (a diferencia de POP3). Su puerto por defecto es el 143, que es el que se devuelve como respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the standard port used by IMAP? | `143` |

### Task 8: Resumen / Summary

**Explicación:** Se resumen los protocolos vistos y la necesidad de cifrar las comunicaciones (HTTPS, SFTP) frente al paso de la información en texto claro. Es el cierre del room.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Keep your data encrypted | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's get started | `No answer needed` |
| 2 | What is the standard port used for the Telnet protocol? | `23` |
| 3 | What is the flag found in the HTTP server? | `THM{e3eb0a1df437f3f97a64aca5952c8ea0}` |
| 4 | What is the flag found in the FTP server? | `THM{364db6ad0e3ddfe7bf0b1870fb06fbdf}` |
| 5 | What is the flag found in the SMTP server? | `THM{5b31ddfc0c11d81eba776e983c35e9b5}` |
| 6 | After connecting to the POP3 server, what is the banner displayed? | `+OK 0 0` |
| 7 | What is the number of messages in the mailbox? | `0` |
| 8 | What is the standard port used by IMAP? | `143` |
| 9 | Keep your data encrypted | `No answer needed` |

---

**Metodología:** Conectar a la máquina, identificar los puertos/servicios y usar telnet (o clientes equivalentes) para interactuar con HTTP, FTP, SMTP, POP3 e IMAP, recuperando en cada servicio la flag o el dato solicitado y verificando que los protocolos transmiten en texto claro.

### Cadena de ataque / Attack Chain

```text
Conectar a la máquina → identificar puertos (23, 80, 21, 25, 110, 143) → interactuar vía telnet con cada servicio → recuperar flags (HTTP/FTP/SMTP) y datos (POP3/IMAP) → entender riesgos de texto claro
```

**Learning chain:** Introducción a protocolos → Telnet → HTTP → FTP → SMTP → POP3 → IMAP → Resumen

**Lección:** *Los protocolos legados (Telnet, HTTP, FTP, SMTP, POP3, IMAP) transmiten datos en texto claro, por lo que cualquier sniffing de la red expone credenciales e información. Siempre que sea posible, deben usarse versiones cifradas (SSH, HTTPS, SFTP, SMTPS, IMAPS).*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1041 (Exfiltration Over C2 Channel)

**Fuente:** [TryHackMe - Protocols and Servers](https://tryhackme.com/room/protocolsandservers)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.