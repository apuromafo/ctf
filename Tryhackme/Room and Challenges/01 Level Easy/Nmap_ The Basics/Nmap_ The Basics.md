# Nmap_ The Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `nmapthebasics` | https://tryhackme.com/room/nmapthebasics | 01 Level Easy | TryHackMe | nmap, host discovery, detección de versiones, Connect Scan | Formativo — fundamentos de Nmap: descubrimiento de hosts, puertos, servicios y versiones |

---

**Contexto:** Primera sala de Nmap: descubrimiento de hosts (`192.168.0.31`), detección de puertos, servicios y versiones (`lighttpd 1.4.74`), tipos de escaneo (Connect Scan), perfiles de temporización (`-T aggressive`) y opciones de depuración (`-d`), con la flag `THM{SECRET_PAGE_38B9P6}` oculta tras un puerto secreto del laboratorio.

> **ES:** Fundamentos de Nmap: descubrimiento de hosts y puertos, detección de versiones (lighttpd), temporización, depuración y el Connect Scan, con la flag de la página secreta.
> **EN:** Nmap basics: host and port discovery, version detection (lighttpd), timing, debugging and the Connect Scan, with the secret-page flag.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Introducción de la sala de fundamentos de Nmap. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Descubrimiento de Host / Host Discovery

**Explicación:** El descubrimiento de hosts identifica la máquina objetivo del laboratorio: `192.168.0.31`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué IP se identifica como máquina objetivo en el descubrimiento de hosts? | `192.168.0.31` |

### Task 3: Escaneo de Puertos / Port Scanning

**Explicación:** El escaneo de puertos descubre los puertos relevantes del objetivo y revela la página secreta con la flag `THM{SECRET_PAGE_38B9P6}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos puertos relevantes se descubren en el escaneo? | `6` |
| 2 | ¿Qué flag revela la página secreta del laboratorio? | `THM{SECRET_PAGE_38B9P6}` |

### Task 4: Servicios y Versiones / Services & Versions

**Explicación:** La detección de versiones identifica el servidor web del laboratorio: `lighttpd 1.4.74`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué servidor y versión se identifica en el objetivo? | `lighttpd 1.4.74` |

### Task 5: Temporización / Timing

**Explicación:** El perfil de temporización agresivo de Nmap se aplica con `-T aggressive`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué perfil de temporización agresivo se usa en Nmap? | `-T aggressive` |

### Task 6: Depuración / Debugging

**Explicación:** La opción de depuración de Nmap es `-d`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué opción de depuración utiliza Nmap? | `-d` |

### Task 7: Tipos de Escaneo / Scan Types

**Explicación:** Cuando el escaneo SYN requiere privilegios de raw sockets, se emplea el Connect Scan (TCP connect).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de escaneo conecta por TCP completo al puerto objetivo? | `Connect Scan` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Qué IP se identifica como máquina objetivo en el descubrimiento de hosts? | `192.168.0.31` |
| 3 | ¿Cuántos puertos relevantes se descubren en el escaneo? | `6` |
| 4 | ¿Qué flag revela la página secreta del laboratorio? | `THM{SECRET_PAGE_38B9P6}` |
| 5 | ¿Qué servidor y versión se identifica en el objetivo? | `lighttpd 1.4.74` |
| 6 | ¿Qué perfil de temporización agresivo se usa en Nmap? | `-T aggressive` |
| 7 | ¿Qué opción de depuración utiliza Nmap? | `-d` |
| 8 | ¿Qué tipo de escaneo conecta por TCP completo al puerto objetivo? | `Connect Scan` |

---

**Metodología:** Recorrido por los fundamentos de Nmap: descubrimiento de hosts, escaneo y conteo de puertos, detección de versiones (`lighttpd 1.4.74`), perfiles de temporización (`-T aggressive`), opciones de depuración (`-d`) y el Connect Scan como alternativa cuando no se dispone de raw sockets.

### Cadena de ataque / Attack Chain

```text
Host discovery -> IP objetivo (192.168.0.31) -> port scan (6 puertos) -> versiones (lighttpd 1.4.74) -> timing -T aggressive -> debug -d -> Connect Scan -> flag THM{SECRET_PAGE_38B9P6}
```

**Learning chain:** descubrimiento de hosts → puertos → versiones → temporización → tipos de escaneo → flag.

**Lección:** *Combinar descubrimiento, escaneo y detección de versiones permite pasar del mapa de puertos a la selección del exploit; el Connect Scan cubre los entornos sin privilegios.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1595.001 (Scanning IP Blocks), T1595.002 (Vulnerability Scanning)

**Fuente:** [TryHackMe - Nmap_ The Basics](https://tryhackme.com/room/nmapthebasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.