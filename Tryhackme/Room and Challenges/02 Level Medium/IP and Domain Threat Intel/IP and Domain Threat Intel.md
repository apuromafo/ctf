# IP and Domain Threat Intel [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `ipanddomainthreatintel`
* **Link:** https://tryhackme.com/room/ipanddomainthreatintel
* **Objeto:** Enriquecer IPs y dominios con intel de amenazas open-source: registros DNS, RDAP/WHOIS, ASN, geolocalización, servicios expuestos, certificados TLS, VirusTotal y WHOIS histórico.

---

## Solucionario de Tareas / Task Solutions

> Sala centrada en indicadores de infraestructura (dominios, IPs, certificados, relaciones de red) usando RDAP, Shodan, Censys y crt.sh. Laboratorio 3 de la serie Threat Intelligence.
> Room focused on infrastructure indicators (domains, IPs, certificates, network relationships) using RDAP, Shodan, Censys and crt.sh. Lab 3 of the Threat Intelligence series.

### Tarea 1-2 / Task 1-2 — IP Building Blocks

**Del informe descargable, ¿cuáles son las IPs del registro A asociado al dominio señalado advanced-ip-sccanner[.]com? / From the downloadable report, what are the IP addresses for the A Record associated with our flagged domain, advanced-ip-sccanner[.]com?**
`172.67.189.143,104.21.9.202`

**¿Qué direcciones de nameserver están asociadas a la IP? Defanga las direcciones. / What nameserver addresses are associated with the IP address? Defang the addresses.**
`jaziel[.]ns[.]cloudflare[.]com, summer[.]ns[.]cloudflare[.]com`

Fuente / Source: https://simontaplin.net/2025/09/04/answers-for-the-tryhackme-ip-and-domain-threat-intel-room/ · https://motasem-notes.net/cyber-threat-intelligence-how-to-investigate-ips-and-domains-tryhackme-walkthrough/

### Tarea 3 / Task 3 — IP Enrichment: Geolocation and ASN

**Abre client.rdap.org e identifica cuándo se registró la IP 64[.]31[.]63[.]194. (UTC: MM/DD/YYYY, H:MM:SS AM/PM) / Open client.rdap.org and identify when the 64[.]31[.]63[.]194 IP was logged for registration.**
`12/27/2010, 3:51:03 PM`

**¿Qué roles asignados a la entidad Entity NOC2791-ARIN asociada a la IP 64[.]31[.]63[.]194? / What roles are assigned to the entity Entity NOC2791-ARIN associated with the IP address 64[.]31[.]63[.]194?**
`administrative,technical`

**¿Cuál es el nombre del país de la IP 64[.]31[.]63[.]194? / What is the country's name for the IP 64[.]31[.]63[.]194?**
`France`

**¿Puedes identificar el Sistema Autónomo vinculado a la IP 64[.]31[.]63[.]194? / Can you identify the Autonomous System linked with the IP 64[.]31[.]63[.]194?**
`AS136258`

Fuente / Source: https://simontaplin.net/2025/09/04/answers-for-the-tryhackme-ip-and-domain-threat-intel-room/

### Tarea 4 / Task 4 — Service Exposure

**Usando shodan.io, ¿qué servicio se asocia principalmente a la IP 85[.]188[.]1[.]133? / Using shodan.io, find which service is primarily associated with the IP address 85[.]188[.]1[.]133.**
`ftp`

**¿Cuántos puertos están identificados como abiertos en el servidor? / How many ports have been identified as open on the server?**
`6`

**Usando search.censys.io, identifica la huella (fingerprint) del certificado TLS para la IP. / Using search.censys.io, identify the TLS certificate fingerprint for the IP address.**
`48d6057099841bd18809fd61aa990b17779176de7799f301dac24879da553456`

**Según crt.sh, ¿hay entradas de log de Certificate Transparency asociadas al certificado TLS anterior? (Yay o Nay) / According to crt.sh, are there Certificate Transparency log entries captured associated with the TLS certificate identified above? (Yay or Nay)**
`Yay`

Fuente / Source: https://simontaplin.net/2025/09/04/answers-for-the-tryhackme-ip-and-domain-threat-intel-room/

### Tarea 5 / Task 5 — Reputation Checks and Passive DNS

**¿Qué archivo ha sido vinculado a la IP 166[.]1.160[.]118? / What file has been linked to the IP 166[.]1.160[.]118?**
`ff4c287c60ede1990442115bddd68201d25a735458f76786a938a0aa881d14ef.exe`

**¿Qué organización se identifica en los lookups de WHOIS históricos? / What organisation is identified on historical WHOIS lookups?**
`Ace Data Centers, Inc`

Fuente / Source: https://simontaplin.net/2025/09/04/answers-for-the-tryhackme-ip-and-domain-threat-intel-room/

### Tarea 7 / Task 7 — Challenge

**¿Cuál es el RIR asociado a 170[.]130[.]202[.]134? / What is the RIR associated with 170[.]130[.]202[.]134?**
`ARIN`

**¿Con qué ASN está conectada la IP? / What ASN is the IP connected with?**
`AS62904`

**Identifica el número de registros NS para el dominio santagift[.]shop. / Identify the number of NS records for the domain santagift[.]shop.**
`4`

**¿Qué NS está identificado como Start of Authority (SOA) para el dominio? / Which NS is identified as the Start of Authority (SOA) for the domain?**
`ns-298.awsdns-37.com`

**¿Cuándo se registró el dominio? (DD/MM/YYYY) / When was the domain registered? (DD/MM/YYYY)**
`30/10/2022`

Fuente / Source: https://simontaplin.net/2025/09/04/answers-for-the-tryhackme-ip-and-domain-threat-intel-room/

*Fuente de respuestas / Answer source: https://simontaplin.net/2025/09/04/answers-for-the-tryhackme-ip-and-domain-threat-intel-room/ · https://motasem-notes.net/cyber-threat-intelligence-how-to-investigate-ips-and-domains-tryhackme-walkthrough/ · https://www.dfirhive.com/post/tryhackme-ip-domain-threat-intelligence-walkthrough*

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
