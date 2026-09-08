# WebOSINT

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `webosint` |
| **Link** | [TryHackMe](https://tryhackme.com/room/webosint) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de Ayush Kumar (InfoSec Write-ups) + Carson Shaffer (Medium) |
| **Componentes** | whois / ICANN Lookup / Wayback Machine / ViewDNS.info / OSINT / DNS history |
| **Impacto** | Investigación básica de OSINT sobre un dominio: registro whois, archivos históricos (Wayback) y correlación de IPs con ViewDNS |

---

**Contexto:** Realizar investigación básica de inteligencia de fuentes abiertas (OSINT) sobre un sitio web. La room se centra en el dominio "RepublicofKoffee.com" y usa whois, Wayback Machine y ViewDNS.info para reconstruir la historia del dominio (registro, nameservers, IPs, contenido archivado y conexiones entre sitios).

## Solucionario

### Task 1: When A Website Does Not Exist

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Preguntas de lectura / reading questions) | `No answer needed` |

**Explicación:** Introducción de OSINT. La idea: cuando un sitio ya no existe (como RepublicofKoffee.com), sus huellas quedan en whois, archivos web y registros DNS históricos. Se empieza con una búsqueda con comillas (`"RepublicofKoffee.com"`) para encontrar referencias públicas.

### Task 2: Whois Registration

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the company the domain was registered with? | `Namecheap Inc` |
| 2 | What phone number is listed for the registration company? (do not include country code or special characters/spaces) | (encontrar en el Raw Registrar RDAP Response) |
| 3 | What is the first nameserver listed for the site? | (buscar en el historial whois, p.ej. whoxy.com) |
| 4 | What is listed for the name of the registrant? | `Redacted for privacy` (WhoisGuard) |
| 5 | What country is listed for the registrant? | (buscar en el historial whois) |

**Explicación:** Con **whois** (ICANN Lookup o dawhois.com) y el **Raw Registrar RDAP Response** se obtiene la información de registro del dominio RepublicofKoffee.com: registrar = **Namecheap Inc**, teléfono de la empresa registradora en el raw RDAP, primer nameserver en el historial whois (p. ej. whoxy.com). El registrant aparece como **Redacted for privacy** gracias a WhoisGuard, y el país del registrant se busca en el historial whois.

### Task 3: Ghosts of Websites Past

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first name of the blog's author? | (buscar en el archivo de 2015) |

**Explicación:** Usando la **Wayback Machine** (archive.org) se ven las versiones archivadas del sitio; el archivo de 2015 (el más antiguo/visible) contiene el nombre del autor del blog. Es una técnica clave de OSINT para recuperar contenido eliminado.

### Task 4: Taking Off The Training Wheels

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the second nameserver listed for the domain? | (buscar en ICANN Lookup) |
| 2 | What IP address was the domain listed on as of December 2011? | (buscar en ViewDNS.info) |

**Explicación:** Con **ICANN Lookup** se confirma el segundo nameserver del dominio (además del primero visto en whois). Con **ViewDNS.info** se consulta el historial de IPs: en la entrada de diciembre de 2011 se obtiene la IP en la que estaba publicado el dominio. Estas herramientas reconstruyen la infraestructura histórica del dominio.

### Task 5: Final Exam: Connect the Dots

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Use the tools in Task 4 to confirm the link between the two sites. | (buscar el propietario de la IP compartida, añadir ", L.L.C") |

**Explicación:** Las herramientas de la Task 4 (ViewDNS.info / ICANN Lookup) sirven para confirmar la conexión entre los dos sitios: ambos comparten la misma IP/historial. Se busca el **propietario de la IP compartida** y se añade ", L.L.C" para componer la respuesta final.

### Task 6: Debriefing

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click to complete | `No answer needed` |

**Explicación:** Cierre del flujo OSINT; no requiere respuesta.

### Task 7: Wrap-up

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Update me.. | `No answer needed` |

**Explicación:** Actualización/cierre del room; no requiere respuesta.

---

**Metodología:**
1. **Google search:** buscar el dominio objetivo `RepublicofKoffee.com` con comillas (`"RepublicofKoffee.com"`) para encontrar referencias públicas, sabiendo que el dominio ya no existe.
2. **Whois:** usar `lookup.icann.org` y `dawhois.com` para obtener la información del registro del dominio (registrar = **Namecheap Inc**; registrar del raw RDAP, nameservers, registrant = **Redacted for privacy** / WhoisGuard, país del registrant en el historial whois tipo whoxy.com).
3. **Wayback Machine:** usar archive.org para ver las versiones archivadas del sitio; el archivo de 2015 contiene el nombre del autor del blog.
4. **ViewDNS.info:** ver el historial de IPs del dominio y, con ICANN Lookup, confirmar el segundo nameserver; en el historial de diciembre de 2011 se obtiene la IP en la que estaba publicado el dominio.
5. **Exam final:** usar las herramientas de la Task 4 para confirmar la conexión entre los dos sitios: buscar el propietario de la IP compartida y añadir ", L.L.C".

**Learning chain:** `"RepublicofKoffee.com"` → whois (Namecheap Inc, WhoisGuard registrant) → Wayback Machine (archivo 2015 → autor del blog) → ViewDNS.info (historial IPs + nameservers) → IP compartida → propietario de la IP → ", L.L.C"

**MITRE ATT&CK:** T1593 (Search Open Websites/Domains), T1596 (Search Technical Databases), T1590 (Gather Victim Network Information)

**Fuente:** [TryHackMe - WebOSINT](https://tryhackme.com/room/webosint)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
