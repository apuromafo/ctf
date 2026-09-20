# Intro to LAN

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Info | walkthrough | `introtolan` | [TryHackMe](https://tryhackme.com/room/introtolan) | 00 Level Info | TryHackMe | LAN, topologías, subredes, ARP, DHCP | Introducción a las redes de área local: topologías, dispositivos, subredes, ARP y DHCP |

---

**Contexto:** Sala introductoria a las redes de área local (LAN): qué es una LAN, los dispositivos que la componen (switch, router), las topologías (bus y estrella), el direccionamiento con subredes y los protocolos ARP y DHCP. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Introducción a la LAN / Introduction to LAN

**Explicación:** Se presentan los conceptos básicos de la LAN y sus topologías: la respuesta `Local Area Network` define la propia LAN, `Routing` indica cómo se enrutan los datos entre redes, `Switch` es el dispositivo que conmuta y reenvía el tráfico, y las topologías estudiadas son la `Bus Topology` y la `Star Topology`; el ejercicio entrega la flag `THM{TOPOLOGY_FLAWS}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Local Area Network` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Routing` |
| 3 | *(Pregunta 3 no especificada en el original)* | `Switch` |
| 4 | *(Pregunta 4 no especificada en el original)* | `Bus Topology` |
| 5 | *(Pregunta 5 no especificada en el original)* | `Star Topology` |
| 6 | *(Pregunta 6 no especificada en el original)* | `THM{TOPOLOGY_FLAWS}` |

### Task 2: Subredes en la capa de red / Subnetting in the Network Layer

**Explicación:** Se estudia el direccionamiento de red: el concepto de `Subnetting` para dividir redes, la máscara con `32` bits, el rango de octetos `0-255`, y las direcciones de `Network Address`, `Host Address` y `Default Gateway` que estructuran cada subred.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Subnetting` |
| 2 | *(Pregunta 2 no especificada en el original)* | `32` |
| 3 | *(Pregunta 3 no especificada en el original)* | `0-255` |
| 4 | *(Pregunta 4 no especificada en el original)* | `Network Address` |
| 5 | *(Pregunta 5 no especificada en el original)* | `Host Address` |
| 6 | *(Pregunta 6 no especificada en el original)* | `Default Gateway` |

### Task 3: ARP / Address Resolution Protocol

**Explicación:** Se analiza el protocolo ARP (`Address Resolution Protocol`), que resuelve direcciones: se emite una `Request` de difusión para conocer la `MAC Address` de un host a partir de su `IP Address`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Address Resolution Protocol` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Request` |
| 3 | *(Pregunta 3 no especificada en el original)* | `MAC Address` |
| 4 | *(Pregunta 4 no especificada en el original)* | `IP Address` |

### Task 4: DHCP / Dynamic Host Configuration Protocol

**Explicación:** Se revisa el protocolo DHCP y su proceso de asignación de direcciones en tres pasos: `DHCP Discover`, `DHCP Request` y `DHCP ACK`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `DHCP Discover` |
| 2 | *(Pregunta 2 no especificada en el original)* | `DHCP Request` |
| 3 | *(Pregunta 3 no especificada en el original)* | `DHCP ACK` |

### Task 5: Conclusión / Conclusion

**Explicación:** Cierre de la sala, sin respuesta que introducir. Respuesta original: `No answer needed`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `Local Area Network` |
| 2 | *(Task 1, Pregunta 2 no especificada en el original)* | `Routing` |
| 3 | *(Task 1, Pregunta 3 no especificada en el original)* | `Switch` |
| 4 | *(Task 1, Pregunta 4 no especificada en el original)* | `Bus Topology` |
| 5 | *(Task 1, Pregunta 5 no especificada en el original)* | `Star Topology` |
| 6 | *(Task 1, Pregunta 6 no especificada en el original)* | `THM{TOPOLOGY_FLAWS}` |
| 7 | *(Task 2, Pregunta 1 no especificada en el original)* | `Subnetting` |
| 8 | *(Task 2, Pregunta 2 no especificada en el original)* | `32` |
| 9 | *(Task 2, Pregunta 3 no especificada en el original)* | `0-255` |
| 10 | *(Task 2, Pregunta 4 no especificada en el original)* | `Network Address` |
| 11 | *(Task 2, Pregunta 5 no especificada en el original)* | `Host Address` |
| 12 | *(Task 2, Pregunta 6 no especificada en el original)* | `Default Gateway` |
| 13 | *(Task 3, Pregunta 1 no especificada en el original)* | `Address Resolution Protocol` |
| 14 | *(Task 3, Pregunta 2 no especificada en el original)* | `Request` |
| 15 | *(Task 3, Pregunta 3 no especificada en el original)* | `MAC Address` |
| 16 | *(Task 3, Pregunta 4 no especificada en el original)* | `IP Address` |
| 17 | *(Task 4, Pregunta 1 no especificada en el original)* | `DHCP Discover` |
| 18 | *(Task 4, Pregunta 2 no especificada en el original)* | `DHCP Request` |
| 19 | *(Task 4, Pregunta 3 no especificada en el original)* | `DHCP ACK` |
| 20 | *(Task 5, Pregunta 1 no especificada en el original)* | `No answer needed` |

---

**Metodología:** Definir la LAN y sus dispositivos → estudiar las topologías (bus y estrella) → comprender el direccionamiento y las subredes → analizar el ARP para resolver IP a MAC → revisar el proceso DHCP de asignación de direcciones → cerrar con la flag.

### Cadena de ataque / Attack Chain

```text
LAN → topologías (bus/estrella) → subredes (máscaras, gateway) → ARP (IP → MAC) → DHCP (Discover/Request/ACK) → flag THM{TOPOLOGY_FLAWS}
```

**Learning chain:** Concepto de LAN → dispositivos y topologías → subredes → ARP → DHCP → flag

**Lección:** *En una LAN conviven capas muy distintas que se complementan: la topología define el cableado y la lógica de la red, mientras que ARP y DHCP mantienen en silencio el mapa y la configuración de cada host.*

**MITRE ATT&CK:** T1046 (Network Service Discovery), T1040 (Network Sniffing)

**Fuente:** [TryHackMe - Intro to LAN](https://tryhackme.com/room/introtolan)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.