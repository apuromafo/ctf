# Threat Intelligence Tools

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `threatintelligencetools` | [TryHackMe - Threat Intelligence Tools](https://tryhackme.com/room/threatintelligencetools) | 01 Level Easy | THM | Threat intelligence, OSINT, IP lookup, malware analysis | Uso de herramientas de inteligencia de amenazas para investigar indicadores |

---

**Contexto:** Ejercicio práctico con herramientas de inteligencia de amenazas: análisis de IPs, dominios, correos de phishing y payloads de malware (Dridex) mediante diversas fuentes de investigación.

> **ES:** La sala guía el uso de herramientas de inteligencia de amenazas para investigar indicadores de compromiso: IPs, dominios, cuentas de correo y muestras de malware.
> **EN:** The room guides the use of threat intelligence tools to investigate indicators of compromise: IPs, domains, email accounts and malware samples.

## Solucionario

### Task 1: Respuestas del ejercicio / Exercise answers

**Explicación:** Solución del laboratorio de Threat Intelligence Tools, donde cada bloque corresponde a una investigación de indicadores (ASN, nameservers, correos, dominios y malware).

1. No answer needed
2. No answer needed
3. 1. 345612
   2. 13
   3. NAMECHEAP INC
   4. 2606:4700:10::ac43:1b0a
4. 1. Katana
   2. Dridex
   3. DIGITALOCEAN-ASN
   4. Georgia
5. 1. LinkedIn
   2. darkabutla@sc500.whpservers.com
   3. cabbagecare@hotsmail.com
   4. 204[.]93[.]183[.]11
   5. 4
6. 1. scnet.net
   2. Complete Web Reviews
7. 1. chris.lyons@supercarcenterdetroit.com
   2. HIDDENEXT/Worm.Gen
8. 1. Sales_Receipt 5606.xls
   2. Dridex
9. No answer needed

### Tabla unificada de preguntas / Unified Q&A

| # | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |
| 2 | `No answer needed` |
| 3 | `345612` / `13` / `NAMECHEAP INC` / `2606:4700:10::ac43:1b0a` |
| 4 | `Katana` / `Dridex` / `DIGITALOCEAN-ASN` / `Georgia` |
| 5 | `LinkedIn` / `darkabutla@sc500.whpservers.com` / `cabbagecare@hotsmail.com` / `204[.]93[.]183[.]11` / `4` |
| 6 | `scnet.net` / `Complete Web Reviews` |
| 7 | `chris.lyons@supercarcenterdetroit.com` / `HIDDENEXT/Worm.Gen` |
| 8 | `Sales_Receipt 5606.xls` / `Dridex` |
| 9 | `No answer needed` |

---

**Metodología:** Se aplicaron herramientas de inteligencia de amenazas para resolver cada bloque: identificación del dominio del nameserver, búsquedas WHOIS y ASN (NAMECHEAP INC, DIGITALOCEAN-ASN, 2606:4700:10::ac43:1b0a), rastreo de campañas de Dridex (Katana), investigación de correos de phishing y dominios de C2, y análisis de payloads maliciosos (Sales_Receipt 5606.xls) detectados por motores como HIDDENEXT/Worm.Gen.

### Cadena de ataque / Attack Chain

1. Recopilación de indicadores (IPs, dominios, hashes, correos).
2. Consulta WHOIS, ASN y nameservers de los dominios.
3. Correlación de campañas conocidas (Dridex) con los payloads.
4. Investigación de cuentas de correo y dominios de mando y control.
5. Verificación de detección del payload en motores antivirus.

**Learning chain:** IOC collection → WHOIS/ASN lookup → campaign correlation → email & domain investigation → malware sample analysis

**Lección:** *Las herramientas de inteligencia de amenazas permiten enriquecer indicadores técnicos y correlacionarlos con campañas conocidas para caracterizar al adversario.*

**MITRE ATT&CK:** T1566.002 - Phishing: Spearphishing Link, T1071.001 - Application Layer Protocol: Web Protocols, T1195.002 - Supply Chain Compromise: Compromise of Software Supply Chain

**Fuente:** [TryHackMe - Threat Intelligence Tools](https://tryhackme.com/room/threatintelligencetools)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.