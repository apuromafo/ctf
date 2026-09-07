# ICS/Modbus - Claus for Concern

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `ICS-modbus-aoc2025-g3m6n9b1v4` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/ICS-modbus-aoc2025-g3m6n9b1v4) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | Modbus TCP, ICS, PLC registers, port 502 |
| **Impacto** | Control de infraestructura industrial - acceso a PLCs |

---

**Contexto:** Modbus TCP es un protocolo de comunicación industrial utilizado en sistemas de control (ICS/SCADA) para interactuar con PLCs y dispositivos en red. En esta práctica se explora la exposición de puertos 502 y la lectura de registros industriales, demostrando el impacto de un entorno ICS mal configurado durante la temporada navideña.

## Solucionario

### Task 1: ICS/Modbus

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What port is commonly used by Modbus TCP? | `502` |
| 2 | What's the flag? | `THM{eGgMas0V3r}` |

---

**Metodología:** Se realizó reconocimiento del protocolo Modbus TCP identificando el puerto estándar 502. Posteriormente se accedió a los registros del PLC para obtener la bandera oculta.
**Learning chain:** Modbus TCP → puerto 502 → lectura de registros PLC → bandera
**MITRE ATT&CK:** T0831 - Manipulation of Control
**Fuente:** [TryHackMe - ICS/Modbus - Claus for Concern](https://tryhackme.com/r/room/ICS-modbus-aoc2025-g3m6n9b1v4)