# Traffic Analysis Essentials

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `trafficanalysisessentials` | [TryHackMe](https://tryhackme.com/room/trafficanalysisessentials) | 01 Level Easy | THM | análisis de tráfico, seguridad de red, Cyber Kill Chain, SOAR, load balancing, SOC | Fundamentos del análisis de tráfico para la detección temprana de intrusos en el SOC |

---

**Contexto:**

> **ES:** La sala cubre los fundamentos del análisis de tráfico y la seguridad de red: el papel del analista SOC, los sistemas de seguridad (administración, balanceo de carga y SOAR) y la Cyber Kill Chain aplicada a la detección de intrusos, con flags de verificación.

> **EN:** This room covers the fundamentals of traffic analysis and network security: the SOC analyst's role, security systems (administration, load balancing, and SOAR), and the Cyber Kill Chain applied to intrusion detection, with verification flags.

## Solucionario

### Task 1: Cómo funciona / How it works

**Explicación:**

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Guided introduction to the room. | `No answer needed` |

### Task 2: Seguridad de Red y Análisis de Tráfico / Network Security and Traffic Analysis

**Explicación:**

2. 1. Administrative
   2. Load Balancing
   3. SOAR

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which system performs administrative security tasks? | `Administrative` |
| 2 | Which system distributes traffic using load balancing? | `Load Balancing` |
| 3 | Which platform provides Security Orchestration, Automation and Response? | `SOAR` |

### Task 3: Cyber Kill Chain / Cyber Kill Chain

**Explicación:**

3. 1. THM{PACKET_MASTER}
   2. THM{DETECTION_MASTER}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Apply the Cyber Kill Chain and obtain the first flag. | `THM{PACKET_MASTER}` |
| 2 | Apply the Cyber Kill Chain and obtain the second flag. | `THM{DETECTION_MASTER}` |

### Task 4: Conclusión / Conclusion

**Explicación:**

4. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Guided closing of the room. | `No answer needed` |

---

**Metodología:** Se revisa la teoría de seguridad de red y análisis de tráfico, se identifican los sistemas de seguridad por su función (administración, balanceo de carga y SOAR) y se aplica la Cyber Kill Chain para relacionar eventos de un ataque, obteniendo las flags de verificación y cerrando con las conclusiones de la sala.

### Cadena de ataque / Attack Chain

Reconocimiento de sistemas de seguridad → identificación de funciones (administración, load balancing, SOAR) → modelado de la Cyber Kill Chain → validación con flags.

**Learning chain:** SOC analyst role → network security systems → Cyber Kill Chain → detection flags

**Lección:** *El análisis de tráfico no es leer paquetes, sino conectar cada evento a una fase de la cadena de ataque.*

**MITRE ATT&CK:** T1071 (Application Layer Protocol), T1560 (Archive Collected Data), T1204 (User Execution)

**Fuente:** [TryHackMe - Traffic Analysis Essentials](https://tryhackme.com/room/trafficanalysisessentials)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.