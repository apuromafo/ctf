# Secure Network Architecture

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Teoría (Network Security) | securenetworkarchitecture | https://tryhackme.com/room/securenetworkarchitecture | 02 Level Medium | TryHackMe | Segmentación de red (VLANs/trunks), zonas de seguridad, ACL y políticas, zone-pairs, firewalls, inspección SSL/TLS, UTM, DHCP snooping, Dynamic ARP Inspection, VyOS | Diseño e implementación de una arquitectura de red segura: segmentación por zonas, control de tráfico con ACL/zone-pairs, UTM y protección de capa 2 frente a ataques DHCP/ARP |

---

**Contexto:** La sala **Secure Network Architecture** (del learning path de ingeniería de seguridad) explica cómo diseñar redes segmentadas y seguras. Parte de la **segmentación por VLANs** y la configuración de **trunks** (bridges en VyOS) para separar el tráfico, y continúa con las **zonas de seguridad** (External, DMZ, Restricted) que determinan qué o quién reside en cada región. Después se estudian las **políticas de control de acceso** (ACL), las **zone-pairs** y las **firewalls** con su reglas *drop/accept*, incluyendo la **inspección SSL/TLS** y las **plataformas UTM**. El tramo final cubre la defensa de capa 2: **DHCP snooping** (con su Binding Database y el manejo de DHCPRELEASE) y **Dynamic ARP Inspection**, que valida MAC/IP usando esa misma base de datos.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de los objetivos (segmentación y controles de seguridad de red). No se requiere respuesta.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Leer el material introductorio | `No answer needed` |

### Task 2: Segmentación de red (VyOS) / Network Segmentation
**Explicación:** Revisando la configuración de VyOS se cuentan los *trunks* (conexiones switch-router configuradas como bridges) y se obtiene el VLAN tag de la interfaz de ejemplo.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | How many trunks are present in this configuration? | `4` |
| 2 | What is the VLAN tag ID for interface eth12? | `30` |

### Task 3: Zonas de seguridad comunes / Common Secure Network Architecture
**Explicación:** Según la tabla de zonas: un usuario que se conecta a un servidor web público está completamente fuera de control (External), el servidor web público vive en la DMZ, y el controlador de dominio central se coloca en la zona Restricted (servidor de alto riesgo).

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | From the above table, what zone would a user connecting to a public web server be in? | `External` |
| 2 | From the above table, what zone would a public web server be in? | `DMZ` |
| 3 | From the above table, what zone would a core domain controller be placed in? | `Restricted` |

### Task 4: Políticas de seguridad de red y ACL / Network Security Policies and Controls
**Explicación:** Según la política ACL correspondiente se determina si el primer y el segundo paquete de ejemplo producen un *accept* o un *drop*.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | According to the corresponding ACL policy, will the first packet result in a drop or accept? | `accept` |
| 2 | According to the corresponding ACL policy, will the second packet result in a drop or accept? | `drop` |

### Task 5: Zone-pairs y filtrado / Zone-Pair Policies and Filtering
**Explicación:** Se completan los huecos del sitio estático sobre zone-pairs y políticas por dirección para obtener la flag.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the flag found after filling in all blanks on the static site? | `THM{M05tly_53cure}` |

### Task 6: Validación de tráfico (SSL/TLS y UTM) / Validating Network Traffic
**Explicación:** La inspección SSL/TLS usa un proxy man-in-the-middle (respuesta Y). Los datos descifrados por el proxy se envían a una plataforma **UTM** (Unified Threat Management) para su procesamiento profundo (web filters, IPS, etc.).

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Does SSL inspection require a man-in-the-middle proxy? (Y/N) | `Y` |
| 2 | What platform processes data sent from an SSL proxy? | `Unified Threat Management` |

### Task 7: Ataques comunes (DHCP snooping y DAI) / Addressing Common Attacks
**Explicación:** **DHCP snooping** almacena las direcciones IP arrendadas de los hosts no confiables en la **DHCP Binding Database**; el switch **drop** (descarta) los paquetes DHCPRELEASE que no coinciden con la base de datos. **Dynamic ARP Inspection** usa esa misma base de datos y valida que la dirección IP coincida con la **MAC Address** declarada en el paquete ARP.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Where does DHCP snooping store leased IP addresses from untrusted hosts? | `DHCP Binding Database` |
| 2 | Will a switch drop or accept a DHCPRELEASE packet? | `Drop` |
| 3 | Does dynamic ARP inspection use the DHCP binding database? (Y/N) | `Y` |
| 4 | Dynamic ARP inspection will match an IP address and what other packet detail? | `MAC Address` |

### Task 8: Conclusión / Conclusion
**Explicación:** Cierre de la sala resumiendo el diseño seguro de arquitectura de red. No se requiere respuesta.

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | Leer el material de cierre | `No answer needed` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many trunks are present in this configuration? | `4` |
| 2 | What is the VLAN tag ID for interface eth12? | `30` |
| 3 | From the above table, what zone would a user connecting to a public web server be in? | `External` |
| 4 | From the above table, what zone would a public web server be in? | `DMZ` |
| 5 | From the above table, what zone would a core domain controller be placed in? | `Restricted` |
| 6 | According to the corresponding ACL policy, will the first packet result in a drop or accept? | `accept` |
| 7 | According to the corresponding ACL policy, will the second packet result in a drop or accept? | `drop` |
| 8 | What is the flag found after filling in all blanks on the static site? | `THM{M05tly_53cure}` |
| 9 | Does SSL inspection require a man-in-the-middle proxy? (Y/N) | `Y` |
| 10 | What platform processes data sent from an SSL proxy? | `Unified Threat Management` |
| 11 | Where does DHCP snooping store leased IP addresses from untrusted hosts? | `DHCP Binding Database` |
| 12 | Will a switch drop or accept a DHCPRELEASE packet? | `Drop` |
| 13 | Does dynamic ARP inspection use the DHCP binding database? (Y/N) | `Y` |
| 14 | Dynamic ARP inspection will match an IP address and what other packet detail? | `MAC Address` |

---

**Metodología:** Revisión de la configuración de virtualización de red (VLANs y trunks) → diseño de zonas de seguridad y colocación de activos → aplicación de políticas de tráfico (ACL y zone-pairs) → validación de tráfico cifrado con SSL/TLS + UTM → protección de capa 2 mediante DHCP snooping y Dynamic ARP Inspection basada en el binding database.

**Learning chain:** Segmentación VLAN y trunks → zonas de seguridad (External/DMZ/Restricted) → políticas de red (ACL, drop/accept, zone-pairs) → inspección SSL/TLS y UTM → defensa de capa 2: DHCP snooping y DAI → flag del ejercicio interactivo.

**Lección:** *El diseño seguro de red combina segmentación por VLAN/zonas, políticas direccionales de tráfico (zone-pairs/ACL) y controles de capa 2 (DHCP snooping + ARP inspection) para reducir la superficie de ataque y contener movimientos laterales.*

**MITRE ATT&CK:** Sala principalmente defensiva (arquitectura y controles). Referencia de tácticas ofensivas mitigadas: T1043 Commonly Used Port (limitado por filtrado) · T1090 Proxy (blindado por inspección SSL/TLS + UTM) · T1557 Adversary-in-the-Middle (mitigado por DHCP snooping + Dynamic ARP Inspection) · T1200 Hardware Additions/rogue DHCP (contenido por el binding database).

**Fuente:** [TryHackMe - Secure Network Architecture](https://tryhackme.com/room/securenetworkarchitecture)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.