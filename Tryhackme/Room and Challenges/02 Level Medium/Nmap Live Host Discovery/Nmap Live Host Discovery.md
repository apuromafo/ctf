# Nmap Live Host Discovery

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
| Medium | Módulo / Laboratorio | nmaplivehostdiscovery | https://tryhackme.com/room/nmaplivehostdiscovery | Red Network Security / Nmap | TryHackMe | Nmap, ARP, ICMP, TCP ping, DNS | Medium |

> **Objeto:** Aprender los métodos de descubrimiento de hosts vivos con Nmap: escaneo por lista/de la subred, ARP en redes locales, ICMP (echo, timestamp y máscara), TCP SYN/ACK ping, la resolución inversa de DNS con `-R` y cuándo usar cada técnica según el escenario de la red.

---

**Contexto:**

Esta sala del módulo de Nmap enseña a descubrir cuáles son los hosts activos de una red. Se usa el simulador interactivo para resolver el escaneo de la subred (contar hosts vivos), escaneos ARP (ARP Request/Response), ICMP con las opciones `-PE`, `-PP` y `-PM`, TCP ping con `-PS` (SYN) y `-PA` (ACK), y la resolución DNS inversa con `-R` para descubrir los hostnames de los equipos activos.

> **ES:** El laboratorio plantea descubrir hosts en una subred, identificando cuántos están vivos y confirmando con respuestas. Se practican los paquetes ARP (Request/Response), las opciones de ICMP (`-PP`, `-PM`, `-PE`), TCP SYN/ACK Ping (`-PS23`) y la opción `-R` que resuelve los nombres de los hosts vivos como `router` y `computer5`.

> **EN:** The lab proposes discovering hosts in a subnet, identifying how many are alive and confirming with responses. ARP packets (Request/Response), ICMP options (`-PP`, `-PM`, `-PE`), TCP SYN/ACK Ping (`-PS23`) and the `-R` option that resolves the names of live hosts like `router` and `computer5` are practiced.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Se presenta la sala dedicada al descubrimiento de hosts vivos con Nmap.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |

### Task 2: Escaneo por Subred / Subnet Scan
**Explicación:**

Se ejecuta el descubrimiento sobre la subred y se cuentan los hosts que responden como vivos, anotando cuántos están activos y cuántos están inactivos (`N`/`Y` según si responden o no).

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Hosts vivos en la subred | `4` |
| 2. ¿Algún host inactivo? / N | `N` |
| 3. Hosts que responden | `4` |
| 4. ¿Confirmado? / Y | `Y` |

### Task 3: Actividad por Dirección IP / IP Activity
**Explicación:**

Se correlacionan las direcciones IP de la subred con los equipos activos y sus puertos/identificadores para responder los ejercicios.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Dirección IP del host | `10.10.12.8` |
| 2. Puerto/identificador | `6400` |

### Task 4: Escaneo ARP / ARP Scan
**Explicación:**

Se analiza el tráfico ARP generado por el escaneo: se distinguen los paquetes de solicitud (ARP Request) y de respuesta (ARP Response), se cuenta el número de paquetes de una categoría y se identifican los hosts que responden a la resolución (`router`, `computer5`), anotando además los que no responden (`N`).

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Tipo de paquete enviado | `ARP Request` |
| 2. Tipo de paquete recibido | `ARP Response` |
| 3. Número de respuestas | `1` |
| 4. Host que responde | `router` |
| 5. Host adicional que responde | `computer5` |
| 6. ¿Algún host sin respuesta? / N | `N` |

### Task 5: Escaneo ICMP / ICMP Scan
**Explicación:**

Se determina cuántos de los destinos probados responden al escaneo ICMP de descubrimiento.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 5. Hosts que responden a ICMP | `3` |

### Task 6: Opciones de ICMP / ICMP Options
**Explicación:**

Se identifican las opciones de Nmap para los distintos tipos de ICMP: timestamp (`-PP`), mascara de subred (`-PM`) y echo request (`-PE`).

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Escaneo timestamp | `-PP` |
| 2. Escaneo máscara | `-PM` |
| 3. Escaneo echo | `-PE` |

### Task 7: TCP Ping / TCP Ping
**Explicación:**

Se usan los métodos TCP de descubrimiento: SYN Ping, ACK Ping, y la especificación de puertos concretos como `-PS23`.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 1. Ping SYN | `TCP SYN Ping` |
| 2. Ping ACK | `TCP ACK Ping` |
| 3. Opción con puerto | `-PS23` |

### Task 8: Resolución DNS inversa / Reverse DNS Resolution
**Explicación:**

Se usa la opción de Nmap que resuelve los nombres de los hosts activos a partir de sus direcciones IP (reverse DNS).

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 8. Opción de resolución inversa | `-R` |

### Task 9: Conclusión / Conclusion
**Explicación:**

Cierre de la sala de descubrimiento de hosts vivos.

| Pregunta / Question | Respuesta / Answer |
|---|---|
| 9 | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Task 1 | `No answer needed` |
| 2 | 1. Hosts vivos | `4` |
| 2 | 2. ¿Inactivo? | `N` |
| 2 | 3. Hosts que responden | `4` |
| 2 | 4. Confirmación | `Y` |
| 3 | 1. IP del host | `10.10.12.8` |
| 3 | 2. Puerto | `6400` |
| 4 | 1. Paquete enviado | `ARP Request` |
| 4 | 2. Paquete recibido | `ARP Response` |
| 4 | 3. Número de respuestas | `1` |
| 4 | 4. Equipo 1 | `router` |
| 4 | 5. Equipo 2 | `computer5` |
| 4 | 6. Sin respuesta | `N` |
| 5 | Hosts ICMP | `3` |
| 6 | 1. Timestamp | `-PP` |
| 6 | 2. Máscara | `-PM` |
| 6 | 3. Echo | `-PE` |
| 7 | 1. SYN Ping | `TCP SYN Ping` |
| 7 | 2. ACK Ping | `TCP ACK Ping` |
| 7 | 3. Opción -PS23 | `-PS23` |
| 8 | Resolución inversa | `-R` |
| 9 | Task 9 | `No answer needed` |

---

**Metodología:**

1. Escaneo de la subred y conteo de hosts vivos en el simulador.
2. Correlación de IPs activas y puertos (`10.10.12.8` / `6400`).
3. Análisis del tráfico ARP (Request/Response) e identificación de equipos (`router`, `computer5`).
4. Práctica de ICMP (`-PP`, `-PM`, `-PE`) y TCP ping (SYN/ACK, `-PS23`).
5. Uso de `-R` para resolución DNS inversa de los hosts vivos.

### Cadena de ataque / Attack Chain

```
Descubrir subred: 4 hosts vivos (10.10.12.8 ...)
        |
        v
ARP: Request/Response --> router, computer5
        |
        v
ICMP: -PP / -PM / -PE  --> 3 hosts responden
        |
        v
TCP: SYN Ping, ACK Ping (-PS23)
        |
        v
Reverse DNS (-R) --> nombres de los hosts vivos
```

**Learning chain:**

- ¿Cuándo es útil el escaneo ARP frente a ICMP/TCP en el descubrimiento de hosts?
- ¿Qué diferencias hay entre SYN Ping y ACK Ping?
- ¿Cómo ayuda la resolución DNS inversa (`-R`) a montar el mapa de la red?

**Lección:**

*Descubrir qué hosts están vivos es el primer paso de todo compromiso, y saber combinar ARP, ICMP y TCP ping según el escenario de la red es lo que separa un escaneo rápido de uno inútil.*

**MITRE ATT&CK:**

- T1595.001 (Active Scanning: Scanning IP Blocks)
- T1046 (Network Service Discovery)
- T1018 (Remote System Discovery)

**Fuente:** [TryHackMe - Nmap Live Host Discovery](https://tryhackme.com/room/nmaplivehostdiscovery)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.