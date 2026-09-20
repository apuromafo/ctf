# Networking Essentials

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `networkingessentials` | https://tryhackme.com/room/networkingessentials | 01 Level Easy | TryHackMe | Direccionamiento IP, MAC, TTL, EIGRP, rutas | Formativo — fundamentos de direccionamiento, encabezados IP y protocolos de enrutamiento |

---

**Contexto:** Sala de esenciales de redes: direccionamiento (máscaras, dirección de broadcast `255.255.255.255`, `0.0.0.0`), direcciones MAC (`44:df:65:d8:fe:6c`), campos del encabezado IP (tamaño 40, TTL), protocolos de enrutamiento dinámico (EIGRP), direcciones de ruta y destino, con la flag de validación `THM{computer_is_happy}`.

> **ES:** Esenciales de redes: direccionamiento IP (máscaras/broadcast), direcciones MAC, campos del encabezado IP, protocolos de enrutamiento dinámico (EIGRP) y captura de la flag de laboratorio.
> **EN:** Networking essentials: IP addressing (masks/broadcast), MAC addresses, IP header fields, dynamic routing protocols (EIGRP) and lab flag capture.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Introducción de la sala de esenciales de redes. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Direccionamiento / Addressing

**Explicación:** Conceptos de direccionamiento IP: un valor que representa la cantidad de dirección de broadcast, la dirección de broadcast `255.255.255.255` y la dirección de wildcard `0.0.0.0`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cantidad de dirección de broadcast se indica? | `4` |
| 2 | ¿Cuál es la dirección de broadcast indicada? | `255.255.255.255` |
| 3 | ¿Qué dirección se identifica como wildcard? | `0.0.0.0` |

### Task 3: Direcciones MAC / MAC Addresses

**Explicación:** Se identifica la dirección MAC de la interfaz del laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué dirección de red no especifica ningún valor (all zeros)? | `0.0.0.0` |
| 2 | ¿Cuál es la dirección MAC indicada en el ejercicio? | `44:df:65:d8:fe:6c` |

### Task 4: Encabezado IP / IP Header

**Explicación:** Campos del encabezado IP en el ejercicio: el tamaño (40) y el campo TTL.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el tamaño del encabezado IP indicado? | `40` |
| 2 | ¿Qué campo del encabezado se indica en el ejercicio? | `TTL` |

### Task 5: Enrutamiento / Routing

**Explicación:** Protocolo de enrutamiento dinámico identificado en el ejercicio: `EIGRP`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué protocolo de enrutamiento dinámico se indica en el ejercicio? | `EIGRP` |

### Task 6: Rutas / Routes

**Explicación:** Dirección de destino y prefijo de la tabla de rutas del laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la dirección de destino indicada en la tabla de rutas? | `212.3.4.5` |
| 2 | ¿Cuál es el prefijo/máscara de la ruta indicada? | `65` |

### Task 7: Flag de Validación / Validation Flag

**Explicación:** Tras recopilar la información de red del laboratorio, se captura la flag de validación y se cierra la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag se captura en el laboratorio? | `THM{computer_is_happy}` |
| 2 | Repasa los conceptos finales de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Qué cantidad de dirección de broadcast se indica? | `4` |
| 3 | ¿Cuál es la dirección de broadcast indicada? | `255.255.255.255` |
| 4 | ¿Qué dirección se identifica como wildcard? | `0.0.0.0` |
| 5 | ¿Qué dirección de red no especifica ningún valor (all zeros)? | `0.0.0.0` |
| 6 | ¿Cuál es la dirección MAC indicada en el ejercicio? | `44:df:65:d8:fe:6c` |
| 7 | ¿Cuál es el tamaño del encabezado IP indicado? | `40` |
| 8 | ¿Qué campo del encabezado se indica en el ejercicio? | `TTL` |
| 9 | ¿Qué protocolo de enrutamiento dinámico se indica en el ejercicio? | `EIGRP` |
| 10 | ¿Cuál es la dirección de destino indicada en la tabla de rutas? | `212.3.4.5` |
| 11 | ¿Cuál es el prefijo/máscara de la ruta indicada? | `65` |
| 12 | ¿Qué flag se captura en el laboratorio? | `THM{computer_is_happy}` |
| 13 | Repasa los conceptos finales de la sala. | `No answer needed` |

---

**Metodología:** Se repasan los esenciales de red: direccionamiento con máscaras, dirección de broadcast y wildcard; direcciones MAC y campos del encabezado IP (tamaño y TTL); protocolos de enrutamiento dinámico (EIGRP) y tablas de rutas con dirección de destino, cerrando con la captura de la flag del laboratorio.

### Cadena de ataque / Attack Chain

```text
Direccionamiento (broadcast/0.0.0.0) -> direcciones MAC -> encabezado IP (TTL, 40) -> enrutamiento dinámico (EIGRP) -> tabla de rutas -> flag THM{computer_is_happy}
```

**Learning chain:** direccionamiento IP → MAC → campo TTL → EIGRP → tablas de rutas → flag de laboratorio.

**Lección:** *Dominar el encabezado IP y el direccionamiento es imprescindible para leer tráfico y entender el resultado de un compromiso en el laboratorio.*

**MITRE ATT&CK:** T1016 (System Network Configuration Discovery), T1046 (Network Service Discovery)

**Fuente:** [TryHackMe - Networking Essentials](https://tryhackme.com/room/networkingessentials)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.