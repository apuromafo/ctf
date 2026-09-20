# Active Reconnaissance

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `activereconnaissance` | https://tryhackme.com/room/activereconnaissance | 01 Level Easy | TryHackMe | DevTools / ping (ICMP) / traceroute / telnet / netcat (nc) | Reconocimiento activo: interactuar directamente con el objetivo usando el navegador (DevTools), ping, traceroute, telnet y netcat para recopilar información. |

---

**Contexto:** Segunda room del módulo Network Security. A diferencia del reconocimiento pasivo, el *active reconnaissance* interacciona directamente con el target: navegador con Developer Tools (JavaScript embebido), ping (ICMP con flags `-s`, count `-c`), traceroute (hops), y conexiones manuales con telnet y netcat a puertos de servicio para leer banners del servidor. Cada herramienta permite extraer datos concretos del objetivo desplegado en el laboratorio.

> **ES:** Reconocimiento activo: navegador/DevTools, ping, traceroute, telnet y netcat. Cada tarea ataca directamente al objetivo para obtener información y banners.
> **EN:** Active reconnaissance: browser/DevTools, ping, traceroute, telnet and netcat. Each task interacts directly with the target to gather information and banners.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se introduce el reconocimiento activo: al tocar directamente el sistema objetivo dejamos rastro de nuestra actividad. Se comparan las fases del Unified Kill Chain y las herramientas que se usarán (ping, traceroute, telnet, nc). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la room. | `No answer needed` |

### Task 2: Navegador web / Web Browser

**Explicación:** Se usa Firefox del AttackBox con Developer Tools abiertas para inspeccionar el sitio web de práctica. En la pestaña Network se carga el script `script.js`, cuyo código fuente define un array `questions` con distintas opciones de speaking/answer_*. Contando las entradas del array se determina el número total de preguntas del challenge.

```javascript
// script.js (fragmento estructural del challenge)
let questions = { 1 : {...}, 2 : {...}, ... };
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Browse to the following website and ensure that you have opened your Developer Tools on AttackBox Firefox. Using the Developer Tools, figure out the total number of questions. / Abre las Developer Tools sobre el sitio e inspecciona script.js. ¿Cuál es el número total de preguntas? | `8` |

### Task 3: Ping

**Explicación:** Ping usa ICMP Echo Request/Reply. El switch `-s` fija el tamaño de los datos (payload) del mensaje ICMP; la cabecera ICMP ocupa 8 bytes. Por defecto el firewall de Windows bloquea el ping, y desde el AttackBox se envía `ping -c 10 MACHINE_IP`, recibiendo 10 replies.

```bash
ping -c 10 MACHINE_IP
# 10 packets transmitted, 10 received, 0% packet loss
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which option would you use to set the size of the data carried by the ICMP echo request? / ¿Qué opción usarías para fijar el tamaño de los datos del ICMP echo request? | `-s` |
| 2 | What is the size of the ICMP header in bytes? / ¿Cuántos bytes ocupa la cabecera ICMP? | `8` |
| 3 | Does MS Windows Firewall block ping by default? (Y/N) / ¿El firewall de Windows bloquea el ping por defecto? (Y/N) | `Y` |
| 4 | Deploy the VM for this task and using the AttackBox terminal, issue the command ping -c 10 MACHINE_IP. How many ping replies did you get back? / Despliega la VM y ejecuta ping -c 10 MACHINE_IP. ¿Cuántas respuestas de ping recibiste? | `10` |

### Task 4: Traceroute

**Explicación:** Traceroute (o tracert en Windows) muestra la ruta de los paquetes hasta el destino, revelando los routers intermedios. Se comparan dos traceroutes (A y B) hacia tryhackme.com: la última IP antes del destino en la traza A es `172.67.69.208` y en la B `104.26.11.229` (primeras respuestas del Cloudflare). La traza B entre los dos sistemas atraviesa 26 routers.

```bash
traceroute tryhackme.com
# ...
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In Traceroute A, what is the IP address of the last router/hop before reaching tryhackme.com? / En la traza A, ¿cuál es la IP del último salto antes de tryhackme.com? | `172.67.69.208` |
| 2 | In Traceroute B, what is the IP address of the last router/hop before reaching tryhackme.com? / En la traza B, ¿cuál es la IP del último salto antes de tryhackme.com? | `104.26.11.229` |
| 3 | In Traceroute B, how many routers are between the two systems? / En la traza B, ¿cuántos routers hay entre los dos sistemas? | `26` |
| 4 | Revisa el resto del contenido de la tarea. | `No answer needed` |

### Task 5: Telnet

**Explicación:** telnet permite conectarse manualmente a un puerto y hablar el protocolo. Con la VM del Task 3 arrancada se conecta a su puerto 80 y se envía una petición HTTP básica (`GET / HTTP/1.1` + `host: telnet`). La respuesta HTTP incluye la cabecera `Server`, revelando el servidor web y su versión: Apache y 2.4.61.

```bash
telnet MACHINE_IP 80
GET / HTTP/1.1
host: telnet

HTTP/1.1 200 OK
Server: Apache/2.4.61 (Debian)
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Start the attached VM from Task 3 if it is not already started. On the AttackBox, open the terminal and use the telnet client to connect to the VM on port 80. What is the name of the running server? / Con telnet hacia el puerto 80, ¿cuál es el nombre del servidor que está corriendo? | `Apache` |
| 2 | What is the version of the running server (on port 80 of the VM)? / ¿Cuál es la versión del servidor que corre en el puerto 80? | `2.4.61` |

### Task 6: Netcat

**Explicación:** nc (Netcat) funciona igual que telnet como cliente y además puede actuar de servidor. Con la VM arrancada se conecta con nc al puerto 21 (FTP): al recibir el banner del servicio se lee la versión del servidor FTP que está escuchando.

```bash
nc MACHINE_IP 21
# banner del servicio -> versión del servidor
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Start the VM and open the AttackBox. Once the AttackBox loads, use Netcat to connect to the VM port 21. What is the version of the running server? / Usa netcat para conectarte al puerto 21. ¿Cuál es la versión del servidor que está escuchando? | `0.17` |

### Task 7: Poniéndolo todo junto / Putting it all together

**Explicación:** Resumen de la room: herramientas activas (browser, ping, traceroute, telnet, netcat) frente a pasivas (whois, nslookup, dig). No requiere respuesta y enlaza con la siguiente room de Nmap.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el resumen de la room. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Using the Developer Tools, figure out the total number of questions. | `8` |
| 2 | Which option would you use to set the size of the data carried by the ICMP echo request? | `-s` |
| 3 | What is the size of the ICMP header in bytes? | `8` |
| 4 | Does MS Windows Firewall block ping by default? (Y/N) | `Y` |
| 5 | Deploy the VM for this task and using the AttackBox terminal, issue the command ping -c 10 MACHINE_IP. How many ping replies did you get back? | `10` |
| 6 | In Traceroute A, what is the IP address of the last router/hop before reaching tryhackme.com? | `172.67.69.208` |
| 7 | In Traceroute B, what is the IP address of the last router/hop before reaching tryhackme.com? | `104.26.11.229` |
| 8 | In Traceroute B, how many routers are between the two systems? | `26` |
| 9 | What is the name of the running server (telnet -> port 80)? | `Apache` |
| 10 | What is the version of the running server (on port 80 of the VM)? | `2.4.61` |
| 11 | Use Netcat to connect to the VM port 21. What is the version of the running server? | `0.17` |

---

**Metodología:** Reconocimiento activo progresivo: primero el navegador (DevTools + JS) para entender el challenge; luego ICMP con `ping -s` y `-c`; traceroute para mapear la ruta; telnet y netcat para hablar con los servicios y leer banners (HTTP y FTP). Toda la información sale directamente del objetivo desplegado.

### Cadena de ataque / Attack Chain

```text
Browser/DevTools (script.js) -> ping (ICMP) -> traceroute (hops/IPs) -> telnet :80 (banner HTTP) -> netcat :21 (banner FTP)
```

**Learning chain:** DevTools/JS -> ping/ICMP flags -> traceroute -> telnet HTTP -> netcat FTP -> banners.

**Lección:** *El reconocimiento activo se nota en el objetivo: cada conexión deja rastro, pero banners de servicios y trazas de red son una fuente inmediata de información verificable.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1595 (Active Scanning): T1595.001 (Scanning IP Blocks), T1595.002 (Vulnerability Scanning)

**Fuente:** [TryHackMe - Active Reconnaissance](https://tryhackme.com/room/activereconnaissance)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.