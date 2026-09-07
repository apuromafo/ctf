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

---

**Metodología:**
1. **Lectura del folleto:** se analiza el brochure del hotel y se extraen las pistas de marca: nombre comercial, hashtag y jugador/empleado mencionado.
2. **Búsqueda OSINT:** se busca el nombre en redes sociales (principalmente Instagram/Twitter) y se localiza la cuenta pública asociada a la marca.
3. **Recolección de la flag:** en la bio o en un post (comentario o texto alternativo / alt-text) aparece la flag; como apoyo se usa *search-engine dorking* con el texto del folleto → `THM{V3r@s_aCC0unt_h4s_b33n_f0und!}`.

**Learning chain:** folleto / brochure → pistas de marca (nombre, hashtag, jugador/empleado) → búsqueda OSINT → red social (Instagram/Twitter) → cuenta pública → bio / post (comentario / alt-text) → flag → THM{V3r@s_aCC0unt_h4s_b33n_f0und!}

**MITRE ATT&CK:** T1593 (Search Open Websites/Domains), T1598 (Phishing for Information)

**Fuente:** [TryHackMe - The Brochure](https://tryhackme.com/room/hh-thebrochure-081f3e36)