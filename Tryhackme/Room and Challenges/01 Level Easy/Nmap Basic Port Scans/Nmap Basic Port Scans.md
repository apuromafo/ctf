# Nmap Basic Port Scans

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `nmapbasicportscans` | https://tryhackme.com/room/nmapbasicportscans | 01 Level Easy | TryHackMe | nmap, escaneo de puertos, SYN/RST, servicios | Formativo — escaneo básico de puertos con Nmap y reconocimiento de servicios |

---

**Contexto:** Sala de Nmap dedicada a los escaneos de puertos básicos: estados de puerto (Open), tipos de escaneo (SYN con respuesta RST), mapeo puerto→servicio (110 POP3, 6667 IRC, 53 domain) y opciones para personalizar el escaneo (`-p5000-5500`, `--min-parallelism=64`, `-T0`).

> **ES:** Escaneos de puertos básicos con Nmap: estados de puerto, respuestas SYN/RST, mapeo puerto/servicio y opciones de rango, paralelismo y temporización.
> **EN:** Basic Nmap port scans: port states, SYN/RST responses, port-to-service mapping and range, parallelism and timing options.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala sobre los escaneos de puertos básicos con Nmap. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Tipos de Escaneo / Scan Types

**Explicación:** Identificación de servicios y estados en el escaneo básico: los puertos abiertos y los servicios asociados al objetivo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué servicio se identifica en esta parte del escaneo? | `DNS` |
| 2 | ¿Qué servicio adicional se identifica en el escaneo? | `SSH` |
| 3 | ¿Cuántos puertos de interés se detectan? | `6` |
| 4 | ¿Qué estado de puerto se reporta? | `Open` |

### Task 3: Respuesta SYN / RST

**Explicación:** Comportamiento de un escaneo SYN: el puerto cerrado responde con `RST` y el escaneo se basa en la respuesta SYN del objetivo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué respuesta devuelve el puerto cerrado en un escaneo SYN? | `RST` |
| 2 | ¿Qué tipo de paquete dispara el escaneo de este ejercicio? | `SYN` |

### Task 4: Puerto 110 / POP3

**Explicación:** Mapeo del puerto 110 al servicio POP3.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el número de puerto del servicio indicado? | `110` |
| 2 | ¿Qué servicio corre en el puerto indicado? | `POP3` |

### Task 5: Puerto 6667 / IRC

**Explicación:** Mapeo del puerto 6667 al servicio IRC.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el número de puerto del servicio indicado? | `6667` |
| 2 | ¿Qué servicio corre en el puerto indicado? | `IRC` |

### Task 6: Puerto 53 / Domain

**Explicación:** Mapeo del puerto 53 al servicio domain (DNS).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el número de puerto del servicio indicado? | `53` |
| 2 | ¿Qué servicio corre en el puerto indicado? | `domain` |

### Task 7: Opciones de Escaneo / Scan Options

**Explicación:** Opciones de personalización del escaneo: rango de puertos `-p5000-5500`, paralelismo `--min-parallelism=64` y temporización `-T0`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué opción indica el rango de puertos 5000-5500? | `-p5000-5500` |
| 2 | ¿Qué opción fija un mínimo de 64 conexiones paralelas? | `--min-parallelism=64` |
| 3 | ¿Qué opción configura la temporización más lenta del escaneo? | `-T0` |

### Task 8: Cierre / Wrap-up

**Explicación:** Cierre de la sala con repaso de los escaneos de puertos básicos. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa los conceptos finales de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Qué servicio se identifica en esta parte del escaneo? | `DNS` |
| 3 | ¿Qué servicio adicional se identifica en el escaneo? | `SSH` |
| 4 | ¿Cuántos puertos de interés se detectan? | `6` |
| 5 | ¿Qué estado de puerto se reporta? | `Open` |
| 6 | ¿Qué respuesta devuelve el puerto cerrado en un escaneo SYN? | `RST` |
| 7 | ¿Qué tipo de paquete dispara el escaneo de este ejercicio? | `SYN` |
| 8 | ¿Cuál es el número de puerto del servicio indicado? | `110` |
| 9 | ¿Qué servicio corre en el puerto indicado? | `POP3` |
| 10 | ¿Cuál es el número de puerto del servicio indicado? | `6667` |
| 11 | ¿Qué servicio corre en el puerto indicado? | `IRC` |
| 12 | ¿Cuál es el número de puerto del servicio indicado? | `53` |
| 13 | ¿Qué servicio corre en el puerto indicado? | `domain` |
| 14 | ¿Qué opción indica el rango de puertos 5000-5500? | `-p5000-5500` |
| 15 | ¿Qué opción fija un mínimo de 64 conexiones paralelas? | `--min-parallelism=64` |
| 16 | ¿Qué opción configura la temporización más lenta del escaneo? | `-T0` |
| 17 | Repasa los conceptos finales de la sala. | `No answer needed` |

---

**Metodología:** Se revisan los fundamentos de los escaneos de puertos con Nmap: estados de puerto (Open), la respuesta SYN/RST de un escaneo SYN, la asignación puerto→servicio (110/POP3, 6667/IRC, 53/domain) y las opciones de rango (`-p5000-5500`), paralelismo (`--min-parallelism=64`) y temporización (`-T0`) para escaneos específicos.

### Cadena de ataque / Attack Chain

```text
Tipos de escaneo -> estados de puerto (Open) -> respuesta SYN/RST -> mapeo puerto/servicio (110-POP3, 6667-IRC, 53-domain) -> opciones -p/--min-parallelism/-T0 -> cierre
```

**Learning chain:** estados de puerto → escaneo SYN → servicios por puerto → opciones de personalización → cierre.

**Lección:** *Leer correctamente las respuestas (SYN/RST) y los servicios asociados a cada puerto es la base para elegir el escaneo adecuado antes de enumerar versiones.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1595.001 (Scanning IP Blocks), T1595.002 (Vulnerability Scanning)

**Fuente:** [TryHackMe - Nmap Basic Port Scans](https://tryhackme.com/room/nmapbasicportscans)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.