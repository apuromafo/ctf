# IP and Domain Threat Intel

| **Dificultad** | MEDIUM | **Tipo** | Premium (requiere suscripción) | **Slug** | `ipanddomainthreatintel` |
| **Link** | [TryHackMe](https://tryhackme.com/room/ipanddomainthreatintel) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Threat Intelligence / RDAP / WHOIS / Shodan / Censys / crt.sh / Passive DNS / ASN | **Impacto** | Evalúa el enriquecimiento de indicadores de infraestructura con intel open-source |

---

**Contexto:** Sala centrada en indicadores de infraestructura (dominios, IPs, certificados, relaciones de red) usando RDAP, Shodan, Censys y crt.sh. Laboratorio 3 de la serie Threat Intelligence. Enriquecer IPs y dominios con intel de amenazas open-source: registros DNS, RDAP/WHOIS, ASN, geolocalización, servicios expuestos, certificados TLS, VirusTotal y WHOIS histórico.

## Solucionario

### Task 1: IP Building Blocks

**Explicación:** Del informe descargable se extraen las IPs del registro A del dominio señalado `advanced-ip-sccanner[.]com` y las direcciones de nameserver asociadas a la IP (defangadas). Del informe descargable, ¿cuáles son las IPs del registro A asociado al dominio señalado advanced-ip-sccanner[.]com?

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are the IP addresses for the A Record associated with our flagged domain, advanced-ip-sccanner[.]com? | `172.67.189.143,104.21.9.202` |
| 2 | What nameserver addresses are associated with the IP address? Defang the addresses. | `jaziel[.]ns[.]cloudflare[.]com, summer[.]ns[.]cloudflare[.]com` |

### Task 2: IP Enrichment: Geolocation and ASN

**Explicación:** Abrir `client.rdap.org` para identificar la fecha de registro de la IP 64[.]31[.]63[.]194, los roles de la entidad Entity NOC2791-ARIN, el país y el Sistema Autónomo vinculado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Open client.rdap.org and identify when the 64[.]31[.]63[.]194 IP was logged for registration. | `12/27/2010, 3:51:03 PM` |
| 2 | What roles are assigned to the entity Entity NOC2791-ARIN associated with the IP address 64[.]31[.]63[.]194? | `administrative,technical` |
| 3 | What is the country's name for the IP 64[.]31[.]63[.]194? | `France` |
| 4 | Can you identify the Autonomous System linked with the IP 64[.]31[.]63[.]194? | `AS136258` |

### Task 3: Service Exposure

**Explicación:** Usando shodan.io para identificar el servicio principal de la IP 85[.]188[.]1[.]133 y el número de puertos abiertos; search.censys.io para el fingerprint del certificado TLS; crt.sh para Certificate Transparency logs.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Using shodan.io, find which service is primarily associated with the IP address 85[.]188[.]1[.]133. | `ftp` |
| 2 | How many ports have been identified as open on the server? | `6` |
| 3 | Using search.censys.io, identify the TLS certificate fingerprint for the IP address. | `48d6057099841bd18809fd61aa990b17779176de7799f301dac24879da553456` |
| 4 | According to crt.sh, are there Certificate Transparency log entries captured associated with the TLS certificate identified above? (Yay or Nay) | `Yay` |

### Task 4: Reputation Checks and Passive DNS

**Explicación:** Con VirusTotal y WHOIS histórico se identifica el archivo vinculado a la IP 166[.]1.160[.]118 y la organización en los lookups históricos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What file has been linked to the IP 166[.]1.160[.]118? | `ff4c287c60ede1990442115bddd68201d25a735458f76786a938a0aa881d14ef.exe` |
| 2 | What organisation is identified on historical WHOIS lookups? | `Ace Data Centers, Inc` |

### Task 5: Challenge

**Explicación:** Desafío integrador: RIR de 170[.]130[.]202[.]134 (ARIN), ASN conectado (AS62904), registros NS del dominio santagift[.]shop (4), SOA (ns-298.awsdns-37.com) y fecha de registro del dominio (30/10/2022).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the RIR associated with 170[.]130[.]202[.]134? | `ARIN` |
| 2 | What ASN is the IP connected with? | `AS62904` |
| 3 | Identify the number of NS records for the domain santagift[.]shop. | `4` |
| 4 | Which NS is identified as the Start of Authority (SOA) for the domain? | `ns-298.awsdns-37.com` |
| 5 | When was the domain registered? (DD/MM/YYYY) | `30/10/2022` |

---

**Metodología:**
1. Análisis de registros DNS (A record, NS, SOA) y defang de direcciones.
2. Enriquecimiento RDAP/WHOIS: fecha de registro, roles de entidad, país y ASN.
3. Enriquecimiento de servicios expuestos: Shodan (servicio/puertos), Censys (fingerprint TLS), crt.sh (Certificate Transparency).
4. Reputación y Passive DNS: VirusTotal, WHOIS histórico.
5. Resolución del challenge correlacionando todos los indicadores.

**Learning chain:** DNS (A/NS/SOA) → RDAP/WHOIS (registro, roles, país, ASN) → Shodan (servicios/puertos) → Censys (TLS fingerprint) → crt.sh (CT logs) → VirusTotal/WHOIS histórico (archivos y organización) → Challenge (RIR/ASN/NS/SOA/fecha)

**Lección:** *La inteligencia de amenazas de infraestructura se construye con fuentes open-source complementarias: RDAP/WHOIS da registro y propiedad, Shodan/Censys exponen la superficie, y crt.sh/passive DNS revelan las relaciones del dominio con el resto de la infraestructura.*

**MITRE ATT&CK:** T1595 - Active Scanning; T1596 - Search Open Technical Databases; T1598 - Phishing for Information; T1590 - Gather Victim Network Information

**Fuente:** [TryHackMe - IP and Domain Threat Intel](https://tryhackme.com/room/ipanddomainthreatintel)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
