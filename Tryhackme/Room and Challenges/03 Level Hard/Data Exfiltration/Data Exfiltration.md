# Data Exfiltration

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | Walkthrough | `dataxexfilt` | https://tryhackme.com/room/dataxexfilt | 03 Level Hard | TryHackMe | HTTP/HTTPS tunneling / DNS tunneling / ICMP exfiltration / dnscat2 / iodine / tcpdump / wireshark | Sala teórico-práctica sobre exfiltración de datos: distintas técnicas de tunneling (HTTP, HTTP/HTTPS, ICMP, DNS) para robar información de una red vigilada, con flags que validan cada método. |

---

**Contexto:** Sala dedicada a la exfiltración de datos. Se recorren las técnicas clásicas para sacar información de una red monitorizada: el tunneling frente a la exfiltración tradicional, el uso de protocolos no estándar, el túnel HTTP/HTTPS, la exfiltración por ICMP y el tunneling por DNS (con sus herramientas y flags de validación). Incluye valores concretos del laboratorio como la IP del equipo interno, tamaños de paquetes y flags de cada ejercicio.

> **ES:** "Aprende a exfiltrar datos mediante tunneling HTTP, HTTPS, ICMP y DNS, y valida cada técnica con las flags del laboratorio."
> **EN:** "Learn to exfiltrate data through HTTP, HTTPS, ICMP and DNS tunneling, and validate each technique with the lab flags."

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea de presentación de la sala sobre exfiltración de datos. No requiere respuesta. Contenido original de la tarea:

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la sala. | `No answer needed` |

### Task 2: Configuración del entorno / Environment setup

**Explicación:** Se prepara el laboratorio y el entorno de monitorización de red. No requiere respuesta. Contenido original de la tarea:

```text
2. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preparar el entorno del laboratorio. | `No answer needed` |

### Task 3: Tunneling frente a exfiltración tradicional / Tunneling vs traditional exfiltration

**Explicación:** La sala distingue entre el tunneling (encapsular otro protocolo) y la exfiltración tradicional de datos. Respuestas literales de la tarea. Contenido original de la tarea:

```text
3. 1. Tunneling
   2. traditional data exfiltration
   3. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta 1 de la tarea (reconocimiento del concepto). | `Tunneling` |
| 2 | Respuesta 2 de la tarea (reconocimiento del concepto). | `traditional data exfiltration` |
| 3 | Completar el paso práctico de la tarea. | `No answer needed` |

### Task 4: Protocolo no estándar / Non-standard protocol

**Explicación:** Se identifica el uso de un protocolo no estándar en la exfiltración. Contenido original de la tarea:

```text
4. 1. non-standard
   2. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta literal de la tarea (tipo de protocolo). | `non-standard` |
| 2 | Completar el paso práctico de la tarea. | `No answer needed` |

### Task 5: Túnel HTTP / HTTP tunnel

**Explicación:** Se configura el túnel HTTP del laboratorio. Contenido original de la tarea:

```text
5. 1. T
   2. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta literal de la tarea (opción seleccionada). | `T` |
| 2 | Completar el paso práctico de la tarea. | `No answer needed` |

### Task 6: Flags del túnel HTTP / HTTP tunnel flags

**Explicación:** Se validan las dos flags del ejercicio de tunneling HTTP. Contenido original de la tarea:

```text
6. 1. THM{H77P-G37-15-f0un6}
   2. THM{H77p_7unn3l1n9_l1k3_l337}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del túnel HTTP. | `THM{H77P-G37-15-f0un6}` |
| 2 | Flag 2 del túnel HTTP. | `THM{H77p_7unn3l1n9_l1k3_l337}` |

### Task 7: Exfiltración ICMP / ICMP exfiltration

**Explicación:** Se exfiltran datos encapsulados en paquetes ICMP. Contenido original de la tarea:

```text
7. 1. Data
   2. THM{g0t-1cmp-p4k3t!}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta literal de la tarea (tipo de dato exfiltrado). | `Data` |
| 2 | Flag del ejercicio de exfiltración por ICMP. | `THM{g0t-1cmp-p4k3t!}` |

### Task 8: Datagrama ICMP / ICMP datagram

**Explicación:** Se analiza el datagrama ICMP del laboratorio y se identifica la dirección del equipo desde el que se envia la exfiltración. Contenido original de la tarea:

```text
8. 172.20.0.120
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Dirección IP del equipo interno que exfiltra los datos. | `172.20.0.120` |

### Task 9: Exfiltración DNS / DNS exfiltration

**Explicación:** Se practica la exfiltración usando el protocolo DNS: tamaños del registro TTL y número de subdominios, junto con la flag del ejercicio. Contenido original de la tarea:

```text
9. 1. 63
   2. 255
   3. THM{C-tw0-C0mmun1c4t10ns-0v3r-DN5}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta 1 de la tarea (TTL en el tráfico DNS). | `63` |
| 2 | Respuesta 2 de la tarea (TTL en el tráfico DNS). | `255` |
| 3 | Flag del ejercicio de exfiltración por DNS. | `THM{C-tw0-C0mmun1c4t10ns-0v3r-DN5}` |

### Task 10: Tunneling DNS / DNS tunneling

**Explicación:** Se explota el tunneling por DNS con su herramienta y su interfaz de resolución, y se valida con la flag del ejercicio. Contenido original de la tarea:

```text
10. 1. 4
    2. dns0
    3. THM{DN5-Tunn311n9-1s-c00l}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta 1 de la tarea (configuración del túnel DNS). | `4` |
| 2 | Respuesta 2 de la tarea (interfaz del túnel DNS). | `dns0` |
| 3 | Flag del ejercicio de tunneling por DNS. | `THM{DN5-Tunn311n9-1s-c00l}` |

### Task 11: Conclusión / Conclusion

**Explicación:** Tarea de cierre de la sala; no requiere respuesta. Contenido original de la tarea:

```text
11. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la sala. | `No answer needed` |
| 2 | Preparar el entorno del laboratorio. | `No answer needed` |
| 3 | Respuesta 1 de la tarea (reconocimiento del concepto). | `Tunneling` |
| 4 | Respuesta 2 de la tarea (reconocimiento del concepto). | `traditional data exfiltration` |
| 5 | Completar el paso práctico de la tarea. | `No answer needed` |
| 6 | Respuesta literal de la tarea (tipo de protocolo). | `non-standard` |
| 7 | Completar el paso práctico de la tarea. | `No answer needed` |
| 8 | Respuesta literal de la tarea (opción seleccionada). | `T` |
| 9 | Completar el paso práctico de la tarea. | `No answer needed` |
| 10 | Flag 1 del túnel HTTP. | `THM{H77P-G37-15-f0un6}` |
| 11 | Flag 2 del túnel HTTP. | `THM{H77p_7unn3l1n9_l1k3_l337}` |
| 12 | Respuesta literal de la tarea (tipo de dato exfiltrado). | `Data` |
| 13 | Flag del ejercicio de exfiltración por ICMP. | `THM{g0t-1cmp-p4k3t!}` |
| 14 | Dirección IP del equipo interno que exfiltra los datos. | `172.20.0.120` |
| 15 | Respuesta 1 de la tarea (TTL en el tráfico DNS). | `63` |
| 16 | Respuesta 2 de la tarea (TTL en el tráfico DNS). | `255` |
| 17 | Flag del ejercicio de exfiltración por DNS. | `THM{C-tw0-C0mmun1c4t10ns-0v3r-DN5}` |
| 18 | Respuesta 1 de la tarea (configuración del túnel DNS). | `4` |
| 19 | Respuesta 2 de la tarea (interfaz del túnel DNS). | `dns0` |
| 20 | Flag del ejercicio de tunneling por DNS. | `THM{DN5-Tunn311n9-1s-c00l}` |
| 21 | Leer la conclusión de la sala. | `No answer needed` |

---

**Metodología:**
1. Introducción y configuración del laboratorio de exfiltración de datos.
2. Comparar el tunneling con la exfiltración tradicional y elegir el uso del protocolo no estándar.
3. Montar el túnel HTTP/HTTPS del laboratorio y capturar sus flags.
4. Practicar la exfiltración por ICMP (paquetes con datos) y anotar la IP del equipo emisor.
5. Realizar la exfiltración por DNS (TTLs y subdominios) y validar con la flag.
6. Montar el tunneling por DNS (herramienta e interfaz `dns0`) y validar con su flag.

### Cadena de ataque / Attack Chain

```text
Reconocimiento del entorno -> Tunneling vs exfiltración tradicional -> Túnel HTTP -> flags H77P -> ICMP exfiltration -> flag ICMP -> DNS exfiltration (TTL) -> flag C-tw0-C0mmun1c4t10ns -> DNS tunneling (dns0) -> flag DN5-Tunn311n9
```

**Learning chain:** `HTTP/HTTPS tunnel -> ICMP exfiltration -> DNS exfiltration -> DNS tunneling -> dnscat2/iodine -> captura de flags`

**Lección:** *La exfiltración puede camuflarse en cualquier protocolo permitido por el firewall: HTTP, ICMP y especialmente DNS, donde los tamaños de subdominio y los TTLs delaten el tráfico anómalo.*

**MITRE ATT&CK:** T1041 (Exfiltration Over C2 Channel), T1048 (Exfiltration Over Alternative Protocol), T1071.004 (Application Layer Protocol: DNS), T1572 (Protocol Tunneling)

**Fuente:** [TryHackMe - Data Exfiltration](https://tryhackme.com/room/dataxexfilt)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.