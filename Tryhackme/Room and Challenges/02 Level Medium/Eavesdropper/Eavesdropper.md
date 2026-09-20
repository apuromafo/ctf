# Eavesdropper

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `eavesdropper` |
| **Link** | [TryHackMe](https://tryhackme.com/room/eavesdropper) |
| **Sección** | 02 Level Medium |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | Captura de tráfico / Wireshark / sniffing / flags |
| **Impacto** | Análisis de una captura de red para extraer información sensible que viaja en claro y obtener la flag del reto |

---

**Contexto:** Eavesdropper es un reto de red centrado en escuchar el tráfico (eavesdropping). Se analiza una captura de red (PCAP) en busca de la información que viaja en claro por la red. Con Wireshark se siguen las conversaciones y se recupera la flag del reto.

## Solucionario

### Task 1: Presentación del reto

**Explicación:** Tarea introductoria que presenta el reto de captura de tráfico y la máquina a desplegar. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Presentación y despliegue del entorno | `No answer needed` |

### Task 2: Flag del reto

**Explicación:** Analizando la captura con Wireshark se siguen las conversaciones de red hasta localizar la flag que viaja en texto plano: **flag{14370304172628f784d8e8962d54a600}**.

1. flag{14370304172628f784d8e8962d54a600}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag que viaja en la captura? | `flag{14370304172628f784d8e8962d54a600}` |

---

**Metodología:**

1. Abrir la captura (PCAP) con Wireshark.
2. Examinar los flujos/conversaciones de red (Follow Stream) en busca de datos legibles.
3. Extraer el contenido que viaja en claro y localizar la flag.

**Learning chain:** Red -> Captura PCAP -> Wireshark -> Follow Stream -> Datos en claro -> Flag

**Lección:** *El tráfico que viaja en claro puede ser leído por cualquier oyente de la red: la sniffing pasiva (eavesdropping) expone datos sensibles y flags en redes sin cifrado.*

**MITRE ATT&CK:** T1040 (Network Sniffing), T1071.001 (Web Protocols)

**Fuente:** [TryHackMe - Eavesdropper](https://tryhackme.com/room/eavesdropper)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.