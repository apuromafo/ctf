# ICS/Modbus - Claus for Concern

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Medium | walkthrough | `ICS-modbus-aoc2025-g3m6n9b1v4` | https://tryhackme.com/r/room/ICS-modbus-aoc2025-g3m6n9b1v4 | Advent of Cyber 2025 | TryHackMe | Modbus TCP, ICS, PLC registers, port 502 | Control de infraestructura industrial - acceso a PLCs |

---

**Contexto:** Modbus TCP es un protocolo de comunicación industrial utilizado en sistemas de control (ICS/SCADA) para interactuar con PLCs y dispositivos en red. En esta práctica se explora la exposición de puertos 502 y la lectura de registros industriales, demostrando el impacto de un entorno ICS mal configurado durante la temporada navideña.

> **ES:** Interactúa con un PLC vía Modbus TCP (puerto 502), lee sus registros y recupera la flag de la sala.
> **EN:** Interact with a PLC over Modbus TCP (port 502), read its registers and retrieve the room flag.

## Solucionario

### Task 1: ICS/Modbus

**Explicación:** Se identifica el puerto estándar de Modbus TCP (502) y se interactúa con el PLC del laboratorio: conectando al servicio y leyendo los registros Modbus se localiza la bandera oculta del entorno ICS.

1. 1. 502
   2. THM{eGgMas0V3r}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What port is commonly used by Modbus TCP? | `502` |
| 2 | What's the flag? | `THM{eGgMas0V3r}` |

---

| Task | # | Pregunta | Respuesta |
|------|---|----------|-----------|
| 1 | 1 | What port is commonly used by Modbus TCP? | `502` |
| 1 | 2 | What's the flag? | `THM{eGgMas0V3r}` |

---

**Metodología:** Se realizó reconocimiento del protocolo Modbus TCP identificando el puerto estándar 502. Posteriormente se accedió a los registros del PLC para obtener la bandera oculta.

### Cadena de ataque / Attack Chain

```text
escaneo puerto 502 -> protocolo Modbus TCP -> lectura de registros del PLC -> flag
```

**Learning chain:** Modbus TCP → puerto 502 → lectura de registros PLC → bandera

**Lección:** *Los servicios industriales como Modbus TCP (puerto 502) expuestos en la red permiten a un atacante leer y escribir los registros de los PLCs; conviene aislar las redes ICS y proteger el acceso a los controladores.*

**MITRE ATT&CK:** T0831 - Manipulation of Control

**Fuente:** [TryHackMe - ICS/Modbus - Claus for Concern](https://tryhackme.com/r/room/ICS-modbus-aoc2025-g3m6n9b1v4)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
