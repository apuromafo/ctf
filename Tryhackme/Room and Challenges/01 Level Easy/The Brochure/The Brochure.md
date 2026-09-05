# The Brochure [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Evento "Hacker Holidays 2026: The Byte Lotus Hotel")
* **Slug:** `hh-thebrochure-081f3e36`
* **Link:** https://tryhackme.com/room/hh-thebrochure-081f3e36
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=hh-thebrochure-081f3e36` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de OSINT del evento Hacker Holidays. Se entrega un folleto (brochure) del hotel con pistas: nombre comercial, hashtag, jugador/empleado. La bandera está en una cuenta pública: se busca el nombre en redes sociales (Instagram/Twitter principalmente) y en la bio o en un post (comentario o texto alternativo / alt-text) aparece la flag. También se puede usar *search-engine dorking* con el texto del folleto.
> **EN:** OSINT room from the Hacker Holidays event. A hotel brochure is given with clues: brand name, hashtag, player/employee. The flag is on a public account: search the name on social networks (mainly Instagram/Twitter) and the flag appears in the bio or in a post (comment or alt-text). *Search-engine dorking* with the brochure text is also a valid path.

### Task 1 - The Brochure

> **ES:** A partir del folleto se extraen pistas de marca (nombre comercial, hashtag, jugador/empleado). Con esas pistas se hace OSINT: búsqueda del nombre en redes sociales (Instagram/Twitter) y localización de la cuenta pública. La flag aparece en la bio o en un post (comentario o texto alternativo / alt-text); alternativamente se combina con *search-engine dorking* sobre el texto del folleto.
> **EN:** Extract brand clues from the brochure (brand name, hashtag, player/employee). Use those clues for OSINT: search the name on social networks (Instagram/Twitter) and locate the public account. The flag appears in the bio or in a post (comment or alt-text); alternatively combine it with *search-engine dorking* over the brochure text.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{V3r@s_aCC0unt_h4s_b33n_f0und!}` |

## Metodología / Methodology

1. **Paso / Step - Lectura del folleto:** Se analiza el brochure del hotel y se extraen las pistas: nombre comercial, hashtag y jugador/empleado mencionado.
2. **Paso / Step - Búsqueda OSINT:** Se busca el nombre en redes sociales (principalmente Instagram/Twitter) y se localiza la cuenta pública asociada a la marca.
3. **Paso / Step - Recolección de la flag:** En la bio o en un post (comentario o texto alternativo / alt-text) aparece la flag; como apoyo se usa *search-engine dorking* con el texto del folleto.

### Cadena de ataque / Attack Chain

```
folleto / brochure -> pistas de marca (nombre, hashtag, jugador/empleado)
  -> búsqueda OSINT -> red social (Instagram/Twitter) -> cuenta pública
  -> bio / post (comentario / alt-text) -> flag
  -> THM{V3r@s_aCC0unt_h4s_b33n_f0und!}
```

**Lección:** La información "pública" en perfiles es recolectable; cuidado con la higiene de datos personales.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
