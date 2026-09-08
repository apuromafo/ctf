# Nmap

| **Dificultad** | Easy |
| **Tipo** | Escaneo de redes y servicios (laboratorio) |
| **Slug** | `furthernmap` |
| **Link** | [TryHackMe](https://tryhackme.com/room/furthernmap) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Nmap / SYN scan / UDP scan / TCP (RFC 9293) / NSE (Lua) / smb-os-discovery.nse / smb-brute / evasión de firewalls / ping sweep |
| **Impacto** | Sala de profundización en Nmap: cómo se dirigen los paquetes usando puertos (0–65535), los tipos de escaneo (SYN/half-open, UDP, Xmas), los interruptores principales (-sS, -sU, -O, -sV, -A, -T5, -oA/-oN/-oG, --script/-p) y el Nmap Scripting Engine (lenguaje Lua, categorías como intrusive), junto con técnicas de evasión (--data-length) y escaneo de la red 172.16.0.0/16 mediante ping sweep. |

---

**Contexto:** La sala extiende el uso de Nmap más allá del escaneo básico. Arranca con la teoría de puertos: los puertos dirigen el tráfico hacia la aplicación correcta de un servidor, hay `65535` en total y `1024` se consideran bien conocidos. Después repasa los interruptores de la herramienta (`-sS`, `-sU`, `-O`, `-sV`, `-v/-vv`, `-oA/-oN/-oG`, `-A`, `-T5`, `-p`, `--script`, `--script=vuln`). Entra en detalle del escaneo TCP (definido por `RFC 9293`, donde la conexión cerrada se notifica con el flag `RST`), el escaneo SYN "half-open"/stealth, el escaneo UDP (estados `open|filtered` y el uso de `ICMP`), el escaneo Xmas para saltarse firewalls, y la evasión con `--data-length`. También cubre el NSE: scripts escritos en `Lua` y la categoría `intrusive`, el argumento `maxlist` para limitar resultados, y scripts SMB como `smb-os-discovery.nse` y `smb-brute`. Finaliza con un escaneo práctico de la red 172.16.0.0/16 (`nmap -sn`) y un ejercicio sobre el estado de distintos puertos.

## Solucionario

### Task 1: Conectando

**Explicación:** Presentación de la sala y despliegue de la máquina objetivo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina y prepárate para escanear. | `No answer needed` |

### Task 2: Introducción

**Explicación:** El tráfico de red se dirige hacia la aplicación correcta de un servidor mediante los `Ports` (puertos). Cada equipo habilitado para red dispone de `65535` puertos posibles en cada dirección (trama/local), de los cuales los primeros `1024` se consideran puertos "bien conocidos" (well-known).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué constructo de red se usa para dirigir el tráfico hacia la aplicación correcta de un servidor? | `Ports` |
| 2 | ¿Cuántos de estos hay disponibles en cualquier equipo habilitado para red? | `65535` |
| 3 | ¿Cuántos de estos se consideran "bien conocidos" (well-known)? | `1024` |

### Task 3: Interruptores de Nmap

**Explicación:** Tabla de interruptores de Nmap: `-sS` realiza un SYN scan, `-sU` un UDP scan, `-O` detecta el sistema operativo, `-sV` detecta la versión del servicio, `-v` aumenta la verbosidad, `-vv` la duplica, `-oA` exporta la salida en todos los formatos, `-oN` la guarda en formato normal, `-oG` en formato "grepable", `-A` es un escaneo agresivo (SO + versión + scripts), `-T5` aplica la plantilla de temporización más rápida, `-p 80` escanea el puerto 80, `-p 1000-1500` escanea un rango de puertos, `-p-` escanea todos los puertos, `--script` ejecuta scripts NSE y `--script=vuln` ejecuta los scripts de vulnerabilidades.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué interruptor realiza un SYN scan? | `-sS` |
| 2 | ¿Qué interruptor realiza un UDP scan? | `-sU` |
| 3 | ¿Qué interruptor detecta el sistema operativo del host? | `-O` |
| 4 | ¿Qué interruptor detecta la versión de los servicios? | `-sV` |
| 5 | ¿Qué interruptor aumenta la verbosidad de la salida? | `-v` |
| 6 | ¿Qué interruptor la aumenta todavía más? | `-vv` |
| 7 | ¿Qué interruptor guarda la salida en todos los formatos a la vez? | `-oA` |
| 8 | ¿Qué interruptor guarda la salida en formato normal? | `-oN` |
| 9 | ¿Qué interruptor guarda la salida en formato "grepable"? | `-oG` |
| 10 | ¿Qué interruptor realiza un escaneo agresivo (SO, versión, scripts)? | `-A` |
| 11 | ¿Qué interruptor aplica la plantilla de temporización más rápida? | `-T5` |
| 12 | ¿Cómo escanearías únicamente el puerto 80? | `-p 80` |
| 13 | ¿Cómo escanearías los puertos 1000 a 1500? | `-p 1000-1500` |
| 14 | ¿Qué interruptor escanea todos los puertos? | `-p-` |
| 15 | ¿Qué interruptor ejecuta los scripts del motor NSE? | `--script` |
| 16 | ¿Qué interruptor ejecuta únicamente los scripts relacionados con vulnerabilidades? | `--script=vuln` |

### Task 4: Desplegando el objetivo

**Explicación:** Se arranca la máquina objetivo sobre la que se realizarán los escaneos prácticos de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Arranca la máquina objetivo y comprueba la conectividad. | `No answer needed` |

### Task 5: Escaneo TCP

**Explicación:** El comportamiento del protocolo TCP está definido por el `RFC 9293`. Cuando un puerto está cerrado o se rechaza una conexión, el host responde con el flag `RST` (reset), que notifica el fin o el rechazo de la conexión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué RFC define el comportamiento apropiado del protocolo TCP? | `RFC 9293` |
| 2 | ¿Con qué flag se notifica que una conexión está cerrada o rechazada? | `RST` |

### Task 6: Escaneo SYN

**Explicación:** El SYN scan envía únicamente el paquete SYN y, si recibe SYN/ACK, responde con RST sin completar el handshake. Por eso se conoce como escaneo `Half-Open` (medio abierto) o `Stealth`: nunca se llega a establecer una conexión completa, por lo que no se registra como conexión en la mayoría de aplicaciones; es un escaneo que no es considerado "completo" (N).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se conoce al SYN scan por no completar el handshake de tres vías? | `Half-Open, Stealth` |
| 2 | ¿Este tipo de escaneo se completa con la conexión TCP? (Y/N) | `N` |

### Task 7: Escaneo UDP

**Explicación:** El protocolo UDP no establece conexión ni envía acuses de recibo. Cuando un puerto UDP no responde, Nmap lo clasifica como `open|filtered`, ya que no puede distinguir entre un puerto abierto que ignora los paquetes y uno filtrado por firewall. Para probar la conectividad básica de un host se usa el protocolo `ICMP` (el que emplea la utilidad ping).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Cuando un puerto UDP no responde, ¿cómo lo clasifica Nmap? | `open|filtered` |
| 2 | ¿Qué protocolo usa el comando ping para comprobar la conectividad? | `ICMP` |

### Task 8: Tipos de escaneo y evasión

**Explicación:** El escaneo Xmas envía paquetes con los flags FIN, PSH y URG activados (como un árbol de Navidad), lo que le permite evadir ciertos firewalls e IDS: por eso pertenece a la categoría `Firewall Evasion`. Con ese tipo de escaneo en la práctica se detecta que el sistema operativo del objetivo es `Microsoft Windows`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué nombre recibe el escaneo que envía paquetes con los flags FIN, PSH y URG? | `xmas` |
| 2 | ¿Cómo se denomina la categoría de escaneos que usan técnicas para saltarse los firewalls? | `Firewall Evasion` |
| 3 | Según el escaneo práctico, ¿qué sistema operativo detectamos en el objetivo? | `Microsoft Windows` |

### Task 9: Ping sweep

**Explicación:** Para descubrir qué hosts están vivos en una subred sin escanear puertos se usa el "ping sweep": `nmap -sn 172.16.0.0/16` envía sondeos de descubrimiento (ICMP/ARP) a toda la red 172.16.0.0/16 y lista los hosts que responden.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo realizarías un ping sweep sobre la red 172.16.0.0/16? | `nmap -sn 172.16.0.0/16` |

### Task 10: Motor de scripts NSE

**Explicación:** El Nmap Scripting Engine permite ampliar Nmap con scripts. Los scripts NSE se escriben en `Lua`. Las categorías agrupan scripts por propósito; la categoría `intrusive` reúne los scripts que pueden activar contramedidas en el objetivo (alarmas, bloqueos, logs) por lo que se consideran intrusivos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué lenguaje están escritos los scripts del NSE? | `Lua` |
| 2 | ¿Qué categoría de scripts NSE podría llamar la atención del administrador o de un IDS por su comportamiento agresivo? | `intrusive` |

### Task 11: Argumentos de scripts

**Explicación:** Algunos scripts NSE aceptan argumentos para limitar su ejecución; por ejemplo, `maxlist` controla el número máximo de resultados que devuelve el script de enumeración.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué argumento de script permite limitar el número máximo de resultados devueltos? | `maxlist` |

### Task 12: Scripts SMB

**Explicación:** Los scripts NSE cubren servicios como SMB. `smb-os-discovery.nse` obtiene información del sistema operativo del servidor SMB (nombre, versión, dominio) y `smb-brute` realiza un ataque de fuerza bruta de credenciales contra el servicio SMB.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué script NSE identifica el sistema operativo del servidor SMB? | `smb-os-discovery.nse` |
| 2 | ¿Qué script NSE realiza un ataque de fuerza bruta sobre SMB? | `smb-brute` |

### Task 13: Evasión con datos

**Explicación:** Para esquivar filtros sencillos e IDS que inspeccionan el tamaño o el contenido de los paquetes se puede añadir datos aleatorios con `--data-length` (en bytes). Si el objetivo bloquea el escaneo por TCP, se puede usar `ICMP` como protocolo auxiliar para detectar la apertura de puertos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué protocolo se puede usar para comprobar si un puerto está abierto cuando el firewall bloquea el TCP? | `ICMP` |
| 2 | ¿Qué interruptor de Nmap permite añadir datos aleatorios a los paquetes para evadir el filtrado? | `--data-length` |

### Task 14: Escaneo práctico

**Explicación:** Sobre la máquina objetivo se aplica un escaneo práctico para observar los distintos estados de puertos. Analizando los resultados: el puerto 22 no aparece en el primer escaneo (N), el puerto `999` destaca como filtrado, el puerto analizado sin respuesta muestra el estado `No Response`, aparecen `5` puertos en estado filtrado y el puerto HTTPS aparece finalmente `Y` (sí) como abierto.

```bash
nmap -sS -p- <IP>
nmap -sU <IP>
nmap -p999 <IP>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿El escaneo inicial muestra el puerto 22 abierto? (Y/N) | `N` |
| 2 | ¿Qué puerto aparece en estado filtrado durante el análisis? | `999` |
| 3 | ¿Cuál es el estado del puerto que no contesta a las sondas UDP? | `No Response` |
| 4 | ¿Cuántos puertos quedan en estado filtrado? | `5` |
| 5 | ¿El puerto HTTPS aparece como abierto para la máquina objetivo? (Y/N) | `Y` |

### Task 15: Conclusión

**Explicación:** Resumen de los tipos de escaneo, interruptores y técnicas de evasión aprendidas con Nmap.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¡Lo has conseguido! Termina la sala. | `No answer needed` |

---

**Metodología:** Se repasa la teoría de puertos y de TCP/UDP (RFC 9293, flags, estados open|filtered), después se practica cada interruptor de Nmap por separado y en combinación: SYN scan (-sS) para detectar puertos, ping sweep (-sn) sobre 172.16.0.0/16 para descubrir hosts, escaneo Xmas y --data-length para evasión, y scripts NSE (smb-os-discovery.nse, smb-brute, argumento maxlist) para profundizar en servicios SMB; finalmente se analiza el estado de los puertos del objetivo en un escaneo real.
**Learning chain:** puertos y teoría TCP/UDP → interruptores de Nmap → escaneo SYN y UDP → evasión de firewalls (Xmas, -T5, --data-length) → NSE (Lua, categorías, scripts SMB) → ping sweep 172.16.0.0/16 → escaneo práctico y análisis de estados.
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1595.001 (Active Scanning: Scanning IP Blocks), T1040 (Network Sniffing), T1018 (Remote System Discovery), T1057 (Process Discovery)
**Fuente:** [TryHackMe - Nmap](https://tryhackme.com/room/furthernmap)