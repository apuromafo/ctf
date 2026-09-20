# Passive Reconnaissance

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `passivereconnaissance` | https://tryhackme.com/room/passivereconnaissance | 01 Level Easy | TryHackMe | Whois, nslookup, dig, DNSDumpster, Shodan.io | Recopilación de información sobre un objetivo sin contacto directo con él, utilizando fuentes públicas |

---

**Contexto:** El reconocimiento pasivo consiste en recopilar información sobre un objetivo sin interactuar directamente con él, en contraste con el activo (whois, nslookup, dig, DNSDumpster, Shodan) que sí contacta los sistemas. Este room enseña las herramientas fundamentales de OSINT para reconocimiento no intrusivo de dominios y redes.

> **ES:** Aprende a usar whois para consultar el registro de dominios, nslookup/dig para resolución DNS, DNSDumpster para mapear la infraestructura de red y Shodan.io para identificar servicios expuestos públicamente. Ejercicio práctico de reconocimiento pasivo.
> **EN:** Learn to use whois for domain registration queries, nslookup/dig for DNS resolution, DNSDumpster for network infrastructure mapping, and Shodan.io for identifying publicly exposed services. A hands-on passive reconnaissance exercise.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se presenta el concepto de reconocimiento pasivo vs activo: el pasivo recopila información sin tocar el objetivo, el activo sí envía tráfico. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click me to proceed / Proceder | `No answer needed` |

### Task 2: Reconocimiento pasivo vs activo / Passive Versus Active Recon

**Explicación:** Se distingue entre recon pasivo (no toca el sistema objetivo, es legal en la mayoría de jurisdicciones) y activo (envía paquetes al objetivo, requiere autorización). Las tres preguntas miden esta distinción: visitar una red social es pasivo; hacer ping o ingeniería social en persona son actividades activas (el atacante interactúa directamente).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | You visit the Facebook page of the target company, hoping to get some of their employee names. What kind of reconnaissance activity is this? (A for active, P for passive) | `P` |
| 2 | You ping the IP address of the company webserver to check if ICMP traffic is blocked. What kind of reconnaissance activity is this? (A for active, P for passive) | `A` |
| 3 | You happen to meet the IT administrator of the target company at a party. You try to use social engineering to get more information about their systems and network infrastructure. What kind of reconnaissance activity is this? (A for active, P for passive) | `A` |

### Task 3: Whois

**Explicación:** La herramienta `whois` consulta los registros de dominio en las bases de datos WHOIS de los registradores. Se buscó la información de TryHackMe.com: fecha de registro 2018-07-05, registrador Namecheap y servidores DNS alojados en Cloudflare.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When was TryHackMe.com registered? | `20180705` |
| 2 | What is the registrar of TryHackMe.com? | `namecheap.com` |
| 3 | Which company is TryHackMe.com using for name servers? | `cloudflare.com` |

### Task 4: nslookup y dig

**Explicación:** `nslookup` y `dig` son herramientas de resolución DNS. Se consultaron los registros TXT de `thmlabs.com` (vía `dig thmlabs.com TXT` o nslookup en el modo interactivo) y se obtuvo la flag oculta en uno de esos registros. Los registros TXT son una ubicación común para flags en retos de TryHackMe porque se usan legítimamente para verificación (SPF, DKIM) y pueden albergar texto arbitrario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Check the TXT records of thmlabs.com. What is the flag there? | `THM{a5b83929888ed36acb0272971e438d78}` |

### Task 5: DNSDumpster

**Explicación:** DNSDumpster es un servicio de mapeo DNS que genera un informe con subdominios, servidores de nombres, registros MX y un mapa gráfico de la infraestructura. Se buscó `tryhackme.com` y, entre los resultados (excluding `www` y `blog`), apareció el subdominio `remote`, que corresponde al portal de acceso remoto de la plataforma.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lookup tryhackme.com on DNSDumpster. What is one interesting subdomain that you would discover in addition to www and blog? | `remote` |

### Task 6: Shodan.io

**Explicación:** Shodan.io indexa servidores y servicios expuestos en Internet. Los tres últimos ejercicios explotan la interfaz web del buscador: buscas "apache" y compruebas el primer país en número de servidores públicos (United States), el puerto más común en el tercer puesto para Apache (8080) y el tercer puerto más común para nginx (888). Shodan es una herramienta fundamental para el reconocimiento pasivo de activos expuestos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | According to Shodan.io, what is the first country in the world in terms of the number of publicly accessible Apache servers? | `United States` |
| 2 | Based on Shodan.io, what is the 3rd most common port used for Apache? | `8080` |
| 3 | Based on Shodan.io, what is the 3rd most common port used for nginx? | `888` |

### Task 7: Resumen / Summary

**Explicación:** Cierre del room. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click me to finish / Finalizar | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click me to proceed / Proceder | `No answer needed` |
| 2 | You visit the Facebook page of the target company, hoping to get some of their employee names. What kind of reconnaissance activity is this? (A for active, P for passive) | `P` |
| 3 | You ping the IP address of the company webserver to check if ICMP traffic is blocked. What kind of reconnaissance activity is this? (A for active, P for passive) | `A` |
| 4 | You happen to meet the IT administrator of the target company at a party. You try to use social engineering to get more information about their systems and network infrastructure. What kind of reconnaissance activity is this? (A for active, P for passive) | `A` |
| 5 | When was TryHackMe.com registered? | `20180705` |
| 6 | What is the registrar of TryHackMe.com? | `namecheap.com` |
| 7 | Which company is TryHackMe.com using for name servers? | `cloudflare.com` |
| 8 | Check the TXT records of thmlabs.com. What is the flag there? | `THM{a5b83929888ed36acb0272971e438d78}` |
| 9 | Lookup tryhackme.com on DNSDumpster. What is one interesting subdomain that you would discover in addition to www and blog? | `remote` |
| 10 | According to Shodan.io, what is the first country in the world in terms of the number of publicly accessible Apache servers? | `United States` |
| 11 | Based on Shodan.io, what is the 3rd most common port used for Apache? | `8080` |
| 12 | Based on Shodan.io, what is the 3rd most common port used for nginx? | `888` |
| 13 | Click me to finish / Finalizar | `No answer needed` |

---

**Metodología:** Recopilación de información sin contacto directo con el objetivo: consulta WHOIS de registros de dominio (registrador, fecha, name servers), resolución DNS con nslookup/dig para registros TXT, mapeo de infraestructura con DNSDumpster y búsqueda de servicios expuestos con Shodan.io.

### Cadena de ataque / Attack Chain

```text
Whois (dominio -> registrador, name servers, fecha) -> nslookup/dig (TXT -> flag) -> DNSDumpster (subdominios) -> Shodan.io (servicios/puertos abiertos) -> reconocimiento completo sin tocar al objetivo
```

**Learning chain:** passive vs active recon → WHOIS → nslookup → dig → DNS records (TXT) → DNSDumpster → Shodan.io → OSINT tools for network mapping

**Lección:** *El reconocimiento pasivo es legal y poderoso: con herramientas gratuitas (WHOIS, DNSDumpster, Shodan) se puede construir un mapa detallado de la superficie de ataque de cualquier organización sin que esta reciba una sola petición.*

**MITRE ATT&CK:** T1593 (Search Open Websites/Domains), T1596 (Search Open Technical Databases)

**Fuente:** [TryHackMe - Passive Reconnaissance](https://tryhackme.com/room/passivereconnaissance)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.