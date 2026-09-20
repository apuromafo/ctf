# IDS Fundamentals

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `idsfundamentals` | [TryHackMe](https://tryhackme.com/room/idsfundamentals) | 01 Level Easy | THM | IDS, NIDS, Hybrid IDS, Snort, Packet Logging Mode, rules | Comprensión de los sistemas de detección de intrusos y de la configuración de reglas de Snort |

> **Objeto:** Conocer los sistemas de detección de intrusos (IDS), diferenciar Network Intrusion Detection System (NIDS) e Hybrid IDS, y manejar los modos y archivos de configuración de Snort.

---

**Contexto:** Sala introductoria de TryHackMe sobre los fundamentos de los sistemas de detección de intrusos (IDS). Explica los tipos de IDS (basado en red NIDS e híbrido), los modos de operación de Snort (Packet Logging Mode y NIDS Mode), la estructura de su configuración en `/etc/snort`, y el mecanismo de las reglas que detectan tráfico como pings ICMP.

> **ES:** Una sala guiada sobre los fundamentos de los IDS: tipos de sistemas de detección, modos de Snort y configuración de reglas para monitorizar el tráfico de red.
> **EN:** A guided room on Intrusion Detection System fundamentals: types of detection systems, Snort modes, and rule configuration to monitor network traffic.

## Solucionario

### Task 1: Sistemas de detección de intrusos / Intrusion Detection Systems

**Explicación:** Introducción a los IDS y sus variantes: el NIDS analiza el tráfico de la red, mientras que el Hybrid IDS combina la detección de host y de red.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Un IDS es capaz de pertenecer a la red de registro de una organización? / Is the statement correct? | `Nay` |
| 2.1 | Identifique el primer tipo de sistema / Identify the first type of system | `Network Intrusion Detection System` |
| 2.2 | Identifique el segundo tipo de sistema / Identify the second type of system | `Hybrid IDS` |

### Task 2: Modos de Snort / Snort Modes

**Explicación:** Snort ofrece distintos modos de funcionamiento: capturar paquetes (Packet Logging Mode) o analizarlos en tiempo real como sistema de detección (Network Intrusion Detection System Mode).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3.1 | Identifique el primer modo / Identify the first mode | `Packet Logging Mode` |
| 3.2 | Identifique el segundo modo / Identify the second mode | `Network Intrusion Detection System Mode` |

### Task 3: Configuración de Snort / Snort Configuration

**Explicación:** Los archivos y variables clave de Snort: el directorio de configuración `/etc/snort`, la regla `rev`, el protocolo `icmp` y el archivo de reglas locales `local.rules`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4.1 | ¿Cuál es el directorio de configuración de Snort? / Which is the Snort configuration directory? | `/etc/snort` |
| 4.2 | Identifique la cláusula de revisión / Identify the revision clause | `rev` |
| 4.3 | Identifique el protocolo implicado / Identify the protocol involved | `icmp` |
| 4.4 | ¿Cuál es el archivo de reglas locales? / Which is the local rules file? | `local.rules` |

### Task 4: Práctica con reglas / Practice with Rules

**Explicación:** Ejercicio práctico de detección: la regla dispara contra el host `10.11.90.211` generando la alerta `Ping Detected` con el número de regla de referencia.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5.1 | ¿Cuál es la IP que dispara la regla? / Which is the IP that triggers the rule? | `10.11.90.211` |
| 5.2 | ¿Qué alerta se genera? / Which alert is generated? | `Ping Detected` |
| 5.3 | ¿Cuál es el número de referencia de la regla? / Which is the rule reference number? | `1000002` |

---

**Metodología:** Se estudiaron los tipos de IDS y su papel en la monitorización de red, y se revisaron los modos de Snort. Para la configuración se inspeccionó `/etc/snort` y las reglas locales (`local.rules`), identificando el protocolo (`icmp`), la revisión (`rev`) y validando la detección de un ping contra `10.11.90.211`, que genera la alerta `Ping Detected` con referencias al número de la regla.

### Cadena de ataque / Attack Chain

Reconocimiento de conceptos IDS → diferenciación NIDS / Hybrid IDS → selección del modo Snort (Packet Logging / NIDS Mode) → inspección de configuración en `/etc/snort` → análisis de `local.rules` (icmp, rev) → verificación de detección de ping → lectura de la alerta y su número de regla.

**Learning chain:** Definición de IDS → NIDS vs Hybrid IDS → modos de Snort → configuración `/etc/snort` → reglas (`local.rules`, `rev`, `icmp`) → detección de ping → alerta `Ping Detected`.

**Lección:** *Un IDS no bloquea el tráfico, lo observa; su eficacia depende de una configuración correcta de reglas y de conocer los modos de captura y detección. La monitorización activa (como alertas de ping) es el primer paso hacia la detección temprana de actividad maliciosa.*

**MITRE ATT&CK:** T1046 (Network Service Scanning), T1204 (User Execution), T1059 (Command and Scripting Interpreter), T1071 (Application Layer Protocol).

**Fuente:** [TryHackMe - IDS Fundamentals](https://tryhackme.com/room/idsfundamentals)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.