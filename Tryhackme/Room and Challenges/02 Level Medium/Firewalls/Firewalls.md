# Firewalls

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Redes / Evasión de firewalls | firewalls | https://tryhackme.com/room/firewalls | 02 Level Medium | TryHackMe | Nmap, iptables/netfilter, MAC/IP spoofing, port tunneling | Evasión de firewalls y sistemas de filtrado de red |

---

**Contexto:** **Firewalls** (room `redteamfirewalls`) es una sala de Red Team sobre técnicas de evasión de firewalls. Se repasan los tipos de firewall (Packet-Filtering y Next-Generation), el control del origen (MAC, IP, puerto) con Nmap (`-D` decoys, `-S`, `-g`, OUI de MAC), fragmentación y MTU, modificación de cabeceras, **port hopping** y **port tunneling** con `ncat`, y el uso de puertos no estándar y NGFW. Incluye una máquina desplegable donde se recupera una flag vía túnel.

## Solucionario

### Task 1: Introduction
**Explicación:**

Introducción a la sala y a los conceptos de evasión de firewalls (control del origen, fragmentación, cabeceras, port hopping/tunneling y NGFW). Respuestas de puertos TCP de la ronda de preguntas: `23` (telnet), `443` (HTTPS), `8080` (HTTP alternate) y `5161` (snmpssh).

Respuestas del lab (contenido original):

```
1. 23
2. 443
3. 8080
4. 5161
```

### Task 2: Types of Firewalls
**Explicación:**

El tipo de firewall más básico es el **Packet-Filtering Firewall**; el más avanzado que puede instalarse on-premise es el **Next-Generation Firewall** (NGFW).

Respuestas del lab (contenido original):

```
1. Packet-Filtering Firewall
2. Next-Generation Firewall
```

### Task 3: Evasion via Controlling the Source MAC/IP/Port
**Explicación:**

Pruebas con Nmap controlando el origen. Con decoys (`-D RND,10.10.55.33,ME,RND -F`) se esperan aproximadamente **800** paquetes. Con `--proxies 10.10.13.37` el origen que ve el objetivo es **10.10.13.37**. El OUI `00:02:DC` pertenece a **Fujitsu General Ltd**. Para suplantar la IP origen con `10.10.0.254` se añade **`-S 10.10.0.254`**, y para fijar el puerto origen **53** se usa **`-g 53`**. Las cifras `44`, `0`, `200` corresponden a los campos/cálculos de paquetes y del escaneo presentados en el laboratorio.

Respuestas del lab (contenido original):

```
1. 44
2. 0
3. 200
4. 800
5. 10.10.13.37
6. Fujitsu General Ltd
7. -S 10.10.0.254
8. -g 53
9. No answer needed
```

### Task 4: Evasion via Forcing Fragmentation, MTU, and Data Length
**Explicación:**

Al forzar la fragmentación y modificar el MTU/longitud de datos, el laboratorio arroja los tamaños/cálculos `28`, `36`, `56` y `148` (relacionados con cabeceras IP/TCP y opciones `-f`/`--mtu`/`--data-length`). La última subpregunta es de práctica y no requiere respuesta.

Respuestas del lab (contenido original):

```
1. 28
2. 36
3. 56
4. 148
5. No answer needed
```

### Task 5: Evasion via Modifying Header Fields
**Explicación:**

La máquina del laboratorio requiere el ajuste de cabeceras (`--badsum` etc.) y respuestas `3` y `0` sobre los resultados del escaneo modificado; una subpregunta es de práctica.

Respuestas del lab (contenido original):

```
1. No answer needed
2. 3
3. 0
4. No answer needed
```

### Task 6: Evasion Using Port Hopping
**Explicación:**

En el laboratorio de port hopping, el tráfico del servicio bloqueado debe dirigirse al puerto **21** del servidor.

**Respuesta:** `21`

### Task 7: Evasion Using Port Tunneling
**Explicación:**

Con `ncat` se monta un túnel: `ncat -lvnp 8008 -c "ncat <IP> 80"` reenvía el puerto bloqueado para alcanzar el servidor web y recuperar la flag. El túnel sobre puerto 8080 entrega **`THM{1298331956}`**.

**Respuesta:** `THM{1298331956}`

### Task 8: Evasion Using Non-Standard Ports
**Explicación:**

El usuario con el que se accede/identifica en este laboratorio de puertos no estándar es **thmredteam**.

**Respuesta:** `thmredteam`

### Task 9: Next-Generation Firewalls
**Explicación:**

En el ejercicio conceptual sobre NGFW (inspección de protocolo, dirección origen y destino), la respuesta vale **7**.

**Respuesta:** `7`

### Task 10: Conclusion
**Explicación:**

Cierre de la sala. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Puertos TCP: 23, 443, 8080 y 5161 (`snmpssh`) | `23`, `443`, `8080`, `5161` |
| 2 | ¿Cuál es el firewall más básico? | `Packet-Filtering Firewall` |
| 3 | ¿Cuál es el firewall on-premise más avanzado? | `Next-Generation Firewall` |
| 4 | Paquetes esperados con decoys Nmap | `800` |
| 5 | Origen visible con `--proxies 10.10.13.37` | `10.10.13.37` |
| 6 | Compañía del OUI 00:02:DC | `Fujitsu General Ltd` |
| 7 | Opción para suplantar IP origen | `-S 10.10.0.254` |
| 8 | Opción para fijar el puerto origen | `-g 53` |
| 9 | Resultados de paquetes/cálculos del laboratorio | `44`, `0`, `200` |
| 10 | Tamaños/cálculos de fragmentación y MTU | `28`, `36`, `56`, `148` |
| 11 | Resultados del escaneo con cabeceras modificadas | `3`, `0` |
| 12 | Puerto usado en port hopping | `21` |
| 13 | Flag del puerto tunneling | `THM{1298331956}` |
| 14 | Usuario del lab de puertos no estándar | `thmredteam` |
| 15 | Valor del ejercicio NGFW | `7` |
| 16 | Conclusion | `No answer needed` |

---

**Metodología:** Escaneo y evasión con Nmap (decoys `-D`, fuente `-S`, puerto `-g`, proxies, fragmentación `-f`/`--mtu`/`--data-length`), análisis de OUIs de MAC con herramientas WHOIS, montaje de túneles con `ncat` y acceso web a través de puertos no estándar.

**Learning chain:** Introducción → Tipos de firewall → Control del origen (MAC/IP/port) → Fragmentación y MTU → Modificación de cabeceras → Port hopping → Port tunneling → Puertos no estándar → NGFW → Conclusion.

**Lección:** *Los firewalls basados en filtrado estático se eluden controlando origen, fragmentando paquetes y saltando de puerto; solo un NGFW con inspección de protocolo detecta estas técnicas, y los túneles `ncat` sortean incluso restricciones de puerto.*

**MITRE ATT&CK:** T1046 Network Service Discovery · T1071.001 Application Layer Protocol: Web Protocols · T1090 Proxy · T1572 Protocol Tunneling.

**Fuente:** [TryHackMe - Firewalls](https://tryhackme.com/room/firewalls)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.