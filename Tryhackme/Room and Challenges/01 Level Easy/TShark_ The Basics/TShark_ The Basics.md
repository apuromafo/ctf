# TShark_ The Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `tsharkthebasics` | [TryHackMe](https://tryhackme.com/room/tsharkthebasics) | 01 Level Easy | THM | tshark, captura de tráfico, filtros, estadísticas, HTTP streams | Manejo de tshark para capturar, filtrar y analizar tráfico desde la línea de comandos |

---

**Contexto:**

> **ES:** La sala es una guía práctica de tshark, el analizador de paquetes en línea de comandos: instalación y verificación, versión e interfaces, flags TCP, opciones de captura y filtros (`-b`, `-f`, `-Y`), estadísticas y seguimiento de streams HTTP, con ejercicios guiados al final.

> **EN:** This room is a hands-on guide to tshark, the command-line packet analyzer: installation and verification, version and interfaces, TCP flags, capture options and filters (`-b`, `-f`, `-Y`), statistics, and HTTP stream following, ending with guided exercises.

## Solucionario

### Task 1: Configuración / Setup

**Explicación:**

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Guided introduction to tshark. | `No answer needed` |

### Task 2: Instalación y verificación / Installation and Verification

**Explicación:**

2. 1. No answer needed
   2. 6ef5f0c165a1db4a3cad3116b0c5bcc0cf6b9ab7

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Guided installation step. | `No answer needed` |
| 2 | What is the hash of the capture file? | `6ef5f0c165a1db4a3cad3116b0c5bcc0cf6b9ab7` |

### Task 3: Versión e interfaces / Version and Interfaces

**Explicación:**

3. 1. 3.2.3
   2. 12

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What version of tshark is in use? | `3.2.3` |
| 2 | How many interfaces are available? | `12` |

### Task 4: Flags y paquetes / Flags and Packets

**Explicación:**

4. 1. PSH, ACK
   2. 12421
   3. 9660

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which TCP flags do the captured packets show? | `PSH, ACK` |
| 2 | What is the value related to the stream length? | `12421` |
| 3 | What is the related segment size value? | `9660` |

### Task 5: Opciones de captura / Capture Options

**Explicación:**

5. 1. -b
   2. y

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which option configures multiple/rolling capture files? | `-b` |
| 2 | Which value confirms the prompted action? | `y` |

### Task 6: Filtros / Filters

**Explicación:**

6. 1. -f
   2. -Y

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which option specifies a capture filter? | `-f` |
| 2 | Which option specifies a display filter? | `-Y` |

### Task 7: Estadísticas / Statistics

**Explicación:**

7. 1. 2
   2. 7
   3. 8

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Provide the first value of the statistics exercise. | `2` |
| 2 | Provide the second value of the statistics exercise. | `7` |
| 3 | Provide the third value of the statistics exercise. | `8` |

### Task 8: Seguimiento HTTP / HTTP Streams

**Explicación:**

8. 1. 34
   2. 7
   3. 20
   4. 37

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Provide the first value of the HTTP stream exercise. | `34` |
| 2 | Provide the second value of the HTTP stream exercise. | `7` |
| 3 | Provide the third value of the HTTP stream exercise. | `20` |
| 4 | Provide the fourth value of the HTTP stream exercise. | `37` |

### Task 9: Conclusión / Conclusion

**Explicación:**

9. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Guided closing of the room. | `No answer needed` |

---

**Metodología:** Se instala y verifica tshark, se comprueba la versión y las interfaces disponibles y se analiza una pcap de ejemplo: identificación de flags TCP, longitudes de streams y tamaños de segmento. Después se practican las opciones de captura (`-b`), los filtros de captura y visualización (`-f`, `-Y`) y, finalmente, las estadísticas y el seguimiento de streams HTTP sobre la captura.

### Cadena de ataque / Attack Chain

Installation → verification hash → capture analysis → TCP flags → capture and display filters → statistics → HTTP stream following.

**Learning chain:** tshark setup → capture file analysis → filters → statistics → HTTP streams

**Lección:** *tshark devuelve exactamente lo que le pides: dominar sus filtros es dominar lo que ves de la red.*

**MITRE ATT&CK:** T1071.001 (Application Layer Protocol: Web Protocols)

**Fuente:** [TryHackMe - TShark_ The Basics](https://tryhackme.com/room/tsharkthebasics)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.