# WebOSINT [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `webosint`
* **Link:** https://tryhackme.com/room/webosint
* **Sección / Section:** OSINT
* **Fuente / Source:** Writeup de Ayush Kumar (InfoSec Write-ups) + Carson Shaffer (Medium)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Realizar investigación básica de inteligencia de fuentes abiertas (OSINT) sobre un sitio web. La room se centra en el dominio "RepublicofKoffee.com" y usa whois, Wayback Machine y ViewDNS.info.
> **EN:** Conducting basic open source intelligence research on a website. The room focuses on the domain "RepublicofKoffee.com" and uses whois, Wayback Machine and ViewDNS.info.

---

### Task 1 — When A Website Does Not Exist

El dominio objetivo es `RepublicofKoffee.com`, que no existe. Buscar el dominio en Google con comillas: `"RepublicofKoffee.com"`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Preguntas de lectura / reading questions) | `No answer needed` |

---

### Task 2 — Whois Registration

Usar `lookup.icann.org` y `dawhois.com` para obtener información del registro del dominio.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the company the domain was registered with? | `Namecheap Inc` |
| What phone number is listed for the registration company? (do not include country code or special characters/spaces) | (encontrar en el Raw Registrar RDAP Response) |
| What is the first nameserver listed for the site? | (buscar en el historial whois, p.ej. whoxy.com) |
| What is listed for the name of the registrant? | `Redacted for privacy` (WhoisGuard) |
| What country is listed for the registrant? | (buscar en el historial whois) |

---

### Task 3 — Ghosts of Websites Past

Usar la **Wayback Machine** (archive.org) para ver las versiones archivadas del sitio.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the first name of the blog's author? | (buscar en el archivo de 2015) |

---

### Task 4 — Taking Off The Training Wheels

Usar **ViewDNS.info** para ver el historial de IPs del dominio.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the second nameserver listed for the domain? | (buscar en ICANN Lookup) |
| What IP address was the domain listed on as of December 2011? | (buscar en ViewDNS.info) |

---

### Task 5 — Final Exam: Connect the Dots

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Use the tools in Task 4 to confirm the link between the two sites. | (buscar el propietario de la IP compartida, añadir ", L.L.C") |

---

### Task 6 — Debriefing

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Click to complete | `No answer needed` |

---

### Task 7 — Wrap-up

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Update me.. | `No answer needed` |

---

## Metodología / Methodology

1. **Google search:** buscar el dominio con comillas para encontrar información.
2. **Whois:** usar `lookup.icann.org` y `dawhois.com` para obtener datos de registro (registrar, nameservers, registrant).
3. **Wayback Machine:** ver versiones archivadas del sitio para encontrar contenido antiguo.
4. **ViewDNS.info:** ver el historial de IPs y conexiones entre dominios.

**Lección:** los registros ICANN, ViewDNS y la Wayback Machine revelan mucha información sobre un sitio web. Nota: muchas flags de esta room están desactualizadas porque usan sitios web reales que cambian.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
