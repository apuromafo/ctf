# Forensics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Forensics | forensics | [Forensics](https://tryhackme.com/room/forensics) | 03 Level Hard | TryHackMe | Sistema, Perfil, Red, Dominios, IPs | Alto |

---

**Contexto:**

> **ES:** Room de análisis forense: primeramente sobre un volcado de memoria Windows (sistema, build y perfil de archivos borrados), después sobre tráfico de red (protocolo/puerto, tamaños de paquete) y, finalmente, sobre dominios, IPs y cabeceras de caché de tráfico malicioso.
> **EN:** Forensics room: first on a Windows memory dump (OS, build and deleted-files profile), then on network traffic (protocol/port, packet sizes) and finally on malicious traffic domains, IPs and cache headers.

## Solucionario

### Task 1: Análisis de memoria / Memory analysis

**Explicación:**

El contenido original de la tarea es el siguiente:

1. 1. No answer needed
   2. windows
   3. 2180
   4. deleted_files

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 1 | ¿Hay respuesta para la primera pregunta? / Is there an answer for the first question? | `No answer needed` |
| 1 | ¿Qué sistema operativo se identifica en el volcado? / What operating system is identified in the dump? | `windows` |
| 1 | ¿Cuál es el número de build del sistema? / What is the system build number? | `2180` |
| 1 | ¿Qué perfil/categoría destaca en el análisis? / Which profile/category stands out in the analysis? | `deleted_files` |

### Task 2: Análisis de red / Network analysis

**Explicación:**

El contenido original de la tarea es el siguiente:

2. 1. UDP:5005
   2. 1860;1820;2464

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 2 | ¿Qué protocolo y puerto de exfiltración se detecta? / Which exfiltration protocol and port are detected? | `UDP:5005` |
| 2 | ¿Qué tamaños de paquete están asociados? / What packet sizes are associated? | `1860;1820;2464` |

### Task 3: Dominios y tráfico malicioso / Malicious domains and traffic

**Explicación:**

El contenido original de la tarea es el siguiente:

3. 1. www.goporn.ru
   2. www.ikaka.com
   3. www.icsalabs.com
   4. 202.107.233.211
   5. 209.200.12.164
   6. 209.190.122.186
   7. OANOCACHE

| Task | Pregunta / Question | Respuesta |
|---|---|---|
| 3 | ¿Cuál es el primer dominio malicioso? / What is the first malicious domain? | `www.goporn.ru` |
| 3 | ¿Cuál es el segundo dominio malicioso? / What is the second malicious domain? | `www.ikaka.com` |
| 3 | ¿Cuál es el tercer dominio malicioso? / What is the third malicious domain? | `www.icsalabs.com` |
| 3 | ¿Cuál es la primera IP asociada? / What is the first associated IP? | `202.107.233.211` |
| 3 | ¿Cuál es la segunda IP asociada? / What is the second associated IP? | `209.200.12.164` |
| 3 | ¿Cuál es la tercera IP asociada? / What is the third associated IP? | `209.190.122.186` |
| 3 | ¿Cuál es la cabecera/cadena de caché detectada? / What is the cache header/string detected? | `OANOCACHE` |

---

**Metodología:**

Análisis de volcados de memoria con herramientas de forensia (perfil del sistema, build, archivos borrados), análisis de tráfico de red (protocolos, puertos y tamaños de paquete) y correlación de dominios, IPs y cabeceras HTTP de tráfico sospechoso.

### Cadena de ataque / Attack Chain

1. Identificación del sistema operativo y perfil del volcado de memoria.
2. Localización de los artefactos del sistema (build y archivos borrados).
3. Análisis del tráfico de red y detección de exfiltración vía `UDP:5005`.
4. Correlación de dominios maliciosos, IPs y cabeceras de caché.

**Learning chain:**

`Forensics` → memoria → windows/build → deleted_files → UDP:5005 → paquetes → dominios → IPs → OANOCACHE.

**Lección:** *La memoria y el tráfico de red cuentan la misma historia desde dos ángulos: cruzar el perfil del sistema con los dominios y puertos de exfiltración convierte datos sueltos en una cadena de compromiso completa.*

**MITRE ATT&CK:** T1005 Data from Local System, T1041 Exfiltration Over C2 Channel, T1071.001 Web Protocols.

**Fuente:** [TryHackMe - Forensics](https://tryhackme.com/room/forensics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.