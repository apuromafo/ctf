# Linux Threat Detection 1

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough (Premium) | linuxthreatdetection1 | https://tryhackme.com/room/linuxthreatdetection1 | Linux / Threat Detection | TryHackMe | /opt/trypingme/main.py, procesos (Python), logs, Supply Chain Compromise, Process Tree Analysis | Detección de amenazas en Linux |

---

**Contexto:** La sala **Linux Threat Detection 1** es el primer laboratorio de la serie de detección de amenazas en Linux (Premium): se analiza un host comprometido mediante logs y análisis de procesos, se reconstruye la línea temporal del incidente (fechas de modificación, usuarios implicados e IP atacante), se examina el script vulnerable `/opt/trypingme/main.py`, se identifican los procesos Python y sus PIDs, y se clasifican los hallazgos con técnicas MITRE como **Supply Chain Compromise** y **Process Tree Analysis**.

## Solucionario

### Task 1
**Explicación:**

Acceso al entorno y preparación del análisis de detección.

`No answer needed`

### Task 2
**Explicación:**

Se determina la fecha de modificación del archivo alterado por el atacante y se confirma si la web significa un punto de entrada (Yea/Nay).

1. `2024-10-22`
2. `Yea`

### Task 3
**Explicación:**

Se reconstruye la actividad inicial: fecha, usuarios implicados (root, roy, sol, user) e IP origen del ataque.

1. `2025-08-21`
2. `root, roy, sol, user`
3. `91.224.92.79`

### Task 4
**Explicación:**

Se localiza el script vulnerable de la aplicación web TryPingMe y se obtiene la flag de vulnerabilidad.

1. `/opt/trypingme/main.py`
2. `THM{i_am_vulnerable!}`

### Task 5
**Explicación:**

Análisis de procesos: PIDs asociados y lenguaje de programación del proceso comprometido.

1. `1018`
2. `577`
3. `Python`

### Task 6
**Explicación:**

Clasificación de la técnica de compromiso y de la metodología de detección utilizada.

1. `Supply Chain Compromise`
2. `Process Tree Analysis`

### Task 7
**Explicación:**

Cierre y consolidación del análisis de detección de amenazas.

`No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 - Respuesta | `No answer needed` |
| 2.1 | Task 2 - Respuesta 1 | `2024-10-22` |
| 2.2 | Task 2 - Respuesta 2 | `Yea` |
| 3.1 | Task 3 - Respuesta 1 | `2025-08-21` |
| 3.2 | Task 3 - Respuesta 2 | `root, roy, sol, user` |
| 3.3 | Task 3 - Respuesta 3 | `91.224.92.79` |
| 4.1 | Task 4 - Respuesta 1 | `/opt/trypingme/main.py` |
| 4.2 | Task 4 - Respuesta 2 | `THM{i_am_vulnerable!}` |
| 5.1 | Task 5 - Respuesta 1 | `1018` |
| 5.2 | Task 5 - Respuesta 2 | `577` |
| 5.3 | Task 5 - Respuesta 3 | `Python` |
| 6.1 | Task 6 - Respuesta 1 | `Supply Chain Compromise` |
| 6.2 | Task 6 - Respuesta 2 | `Process Tree Analysis` |
| 7 | Task 7 - Respuesta | `No answer needed` |

---

**Metodología:** Revisión de logs y modificaciones de archivos → reconstrucción de la línea temporal (fechas, usuarios, IP) → análisis del script de la web app y sus procesos → clasificación MITRE (Supply Chain Compromise, Process Tree Analysis).

**Learning chain:** Fecha de modificación → punto de entrada → usuarios e IP → script vulnerable (main.py) → procesos Python (PIDs) → clasificación MITRE.

**Lección:** *Detectar una amenaza Linux exige reconstruir el atacante desde sus huellas frías: timestamps de archivos, usuarios implicados, IPs y el árbol de procesos que apunta al binario comprometido de la aplicación web.*

**MITRE ATT&CK:** T1195.001 Supply Chain Compromise: Compromise Software Dependencies · T1059.006 Command and Scripting Interpreter: Python · T1083 File and Directory Discovery · T1036.005 Masquerading: Match Legitimate Name or Location.

**Fuente:** [TryHackMe - Linux Threat Detection 1](https://tryhackme.com/room/linuxthreatdetection1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.