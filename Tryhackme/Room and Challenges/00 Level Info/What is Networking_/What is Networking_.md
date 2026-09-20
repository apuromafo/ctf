# What is Networking?

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Info | walkthrough | `whatisnetworking` | [TryHackMe](https://tryhackme.com/room/whatisnetworking) | 00 Level Info | THM | Redes, Internet, IP, MAC, Octetos, ICMP, ping, LAN | Fundamentos de redes informáticas y verificación de conectividad |

---

**Contexto:**
> **ES:** Introducción a los fundamentos de redes: qué es una red, qué es Internet, identificación de dispositivos mediante IP y MAC, divisiones de una dirección IP (octetos) y verificación de conectividad con ICMP/ping, con un laboratorio interactivo y una invitación al siguiente módulo (Intro to LAN).
> **EN:** Introduction to networking fundamentals: what a network is, what the Internet is, device identification via IP and MAC, IP address sections (octets) and connectivity verification with ICMP/ping, including an interactive lab and a follow-up module (Intro to LAN).

## Solucionario

### Task 1: ¿Qué es la Red? / What is Networking?
**Explicación:**
1. Network

### Task 2: ¿Qué es Internet? / What is the Internet?
**Explicación:**
2. Tim Berners-Lee

### Task 3: Identificando Dispositivos en una Red / Identifying Devices on a Network
**Explicación:**
1. Internet Protocol
2. Octet
3. 4
4. Media Access Control
5. THM{YOU_GOT_ON_TRYHACKME}

### Task 4: Ping (ICMP) / Ping (ICMP)
**Explicación:**
1. ICMP
2. ping 10.10.10.10
3. THM{I_PINGED_THE_SERVER}

### Task 5: Continúa tu Aprendizaje: Intro a LAN / Continue Your Learning: Intro to LAN
**Explicación:**
5. No answer needed

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the key term for devices that are connected together? | `Network` |
| 2 | Who invented the World Wide Web? | `Tim Berners-Lee` |
| 3.1 | What does the term "IP" stand for? | `Internet Protocol` |
| 3.2 | What is each section of an IP address called? | `Octet` |
| 3.3 | How many sections (in digits) does an IP address have? | `4` |
| 3.4 | What does the term "MAC" stand for? | `Media Access Control` |
| 3.5 | Deploy the interactive lab using the "View Site" button and spoof your MAC address to access the site. What is the flag? | `THM{YOU_GOT_ON_TRYHACKME}` |
| 4.1 | What protocol does ping use? | `ICMP` |
| 4.2 | What is the syntax to ping 10.10.10.10? | `ping 10.10.10.10` |
| 4.3 | What flag do you get when you ping 8.8.8.8? | `THM{I_PINGED_THE_SERVER}` |
| 5 | Read the above. | `No answer needed` |

---

**Metodología:**
Estudio de los conceptos básicos de red (dispositivos conectados e Internet), identificación de hosts por dirección IP (octetos) y dirección MAC, y comprobación de conectividad mediante el protocolo ICMP (ping), complementado con un laboratorio interactivo de suplantación de MAC.

### Cadena de ataque / Attack Chain
1. Identificación de los dispositivos conectados a una red.
2. Distinción entre direccionamiento IP (octetos) y direccionamiento MAC.
3. Suplantación de la dirección MAC en el laboratorio interactivo para acceder al sitio.
4. Verificación de conectividad con ICMP/ping hacia los hosts.
5. Captura de los flags del laboratorio.

**Learning chain:**
Network -> Internet -> IP Addressing -> MAC Address -> Interactive Lab -> Ping (ICMP)

**Lección:** *Una red queda definida por dispositivos interconectados identificables por IP y MAC; herramientas como ping (ICMP) permiten verificar la conectividad y obtener flags en los laboratorios.*

**MITRE ATT&CK:**
- T1046 — Network Service Discovery (asociado al reconocimiento con ping/ICMP en el contexto del lab)

**Fuente:** [TryHackMe - What is Networking?](https://tryhackme.com/room/whatisnetworking)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.