# The Brochure

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `hh-thebrochure-081f3e36` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hh-thebrochure-081f3e36) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=hh-thebrochure-081f3e36` + websearch de walkthroughs) |
| **Componentes** | OSINT / Instagram / Twitter / search-engine dorking / alt-text |
| **Impacto** | OSINT de redes sociales: de las pistas de un folleto del hotel a la flag en una cuenta pública |

---

**Contexto:** Sala de OSINT del evento Hacker Holidays. Se entrega un folleto (brochure) del hotel con pistas: nombre comercial, hashtag, jugador/empleado. La bandera está en una cuenta pública: se busca el nombre en redes sociales (Instagram/Twitter principalmente) y en la bio o en un post (comentario o texto alternativo / alt-text) aparece la flag. También se puede usar *search-engine dorking* con el texto del folleto.

## Solucionario

### Task 1: The Brochure

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{V3r@s_aCC0unt_h4s_b33n_f0und!}` |

**Explicación:** A partir del folleto se extraen pistas de marca (nombre comercial, hashtag, jugador/empleado). Con esas pistas se hace OSINT: búsqueda del nombre en redes sociales (Instagram/Twitter) y localización de la cuenta pública. La flag aparece en la bio o en un post (comentario o texto alternativo / alt-text); alternativamente se combina con *search-engine dorking* sobre el texto del folleto → `THM{V3r@s_aCC0unt_h4s_b33n_f0und!}`.

---

**Metodología:**
1. **Lectura del folleto:** se analiza el brochure del hotel y se extraen las pistas de marca: nombre comercial, hashtag y jugador/empleado mencionado.
2. **Búsqueda OSINT:** se busca el nombre en redes sociales (principalmente Instagram/Twitter) y se localiza la cuenta pública asociada a la marca.
3. **Recolección de la flag:** en la bio o en un post (comentario o texto alternativo / alt-text) aparece la flag; como apoyo se usa *search-engine dorking* con el texto del folleto → `THM{V3r@s_aCC0unt_h4s_b33n_f0und!}`.

**Learning chain:** folleto / brochure → pistas de marca (nombre, hashtag, jugador/empleado) → búsqueda OSINT → red social (Instagram/Twitter) → cuenta pública → bio / post (comentario / alt-text) → flag → THM{V3r@s_aCC0unt_h4s_b33n_f0und!}

**MITRE ATT&CK:** T1593 (Search Open Websites/Domains), T1598 (Phishing for Information)

**Fuente:** [TryHackMe - The Brochure](https://tryhackme.com/room/hh-thebrochure-081f3e36)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
