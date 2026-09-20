# Rocket

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `rocket` | https://tryhackme.com/room/rocket | 03 Level Hard | TryHackMe | CTF / cohete / enumeración / flags | Reto CTF de temática espacial: una tarea introductoria sin respuesta y una segunda con las dos flags del reto. |

---

**Contexto:** Sala de reto CTF compuesta por dos tareas: la primera es una tarea de introducción sin respuesta ("No answer needed") y la segunda entrega las dos flags del reto. El contenido original recogido es únicamente esa estructura de respuestas.

> **ES:** "Completa la tarea introductoria y entrega las dos flags del reto espacial."
> **EN:** "Complete the introductory task and submit the two flags of the space challenge."

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea introductoria de la sala; no requiere respuesta. Contenido original de la tarea:

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea introductoria sin respuesta. | `No answer needed` |

### Task 2: Flags del reto / Challenge flags

**Explicación:** Las dos flags del reto, obtenidas tras completar el recorrido de la sala. Contenido original de la tarea:

```text
2. 1. THM{9f87696626a585380d3c1697087e5b5b}
   2. THM{6613b7f76a88b32230eac584b0e18cfd}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del reto. | `THM{9f87696626a585380d3c1697087e5b5b}` |
| 2 | Flag 2 del reto. | `THM{6613b7f76a88b32230eac584b0e18cfd}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea introductoria sin respuesta. | `No answer needed` |
| 2 | Flag 1 del reto. | `THM{9f87696626a585380d3c1697087e5b5b}` |
| 3 | Flag 2 del reto. | `THM{6613b7f76a88b32230eac584b0e18cfd}` |

---

**Metodología:**
1. Completar la tarea de introducción de la sala.
2. Enumerar el objetivo del reto espacial.
3. Resolver la cadena del reto y entregar la primera flag.
4. Cerrar el recorrido con la segunda flag.

### Cadena de ataque / Attack Chain

```text
Introducción -> recon -> THM{9f87696626a585380d3c1697087e5b5b} -> THM{6613b7f76a88b32230eac584b0e18cfd}
```

**Learning chain:** `Intro -> recon -> flags del reto`

**Lección:** *Los CTF con una tarea "No answer needed" separan la parte teórica de la práctica: la resolución final se valida con las flags, copiadas siempre de forma literal.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1190 (Exploit Public-Facing Application)

**Fuente:** [TryHackMe - Rocket](https://tryhackme.com/room/rocket)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.