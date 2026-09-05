# Hidden Deep Into my Heart [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF (Evento "Love at First Breach 2026" - Módulo LAFB CTF 2026)
* **Slug:** `lafb2026e9`
* **Link:** https://tryhackme.com/room/lafb2026e9
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e9` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Love at First Breach 2026, listada en la API como "Deep Into my Heart") de dificultad Fácil. El tema es **OSINT/crawl básico sobre una web de citas**: el fichero `/robots.txt` (y/o `/sitemap.xml`) desvela rutas ocultas del sitio que no están enlazadas; una de ellas contiene la flag. Lección de higiene: los ficheros de exclusión de rastreadores no son control de acceso.
> **EN:** Event room (Love at First Breach 2026, listed in the API as "Deep Into my Heart") of Easy difficulty. The theme is **basic OSINT/crawling over a dating web**: the `/robots.txt` file (and/or `/sitemap.xml`) reveals hidden routes that are not linked from the site; one of them holds the flag. Hygiene lesson: crawler-exclusion files are not access control.

### Task 1 - Robots and Hidden Routes

> **ES:** La web de citas no enlaza la sección secreta, pero `GET /robots.txt` lista las rutas prohibidas de los rastreadores (`Disallow`). Entre ellas aparece la ruta oculta (`/hidden` o `/secret-deeper`); a veces también `/sitemap.xml`. Accediendo a esa ruta (posiblemente con una segunda página/archivo) se encuentra la flag. 1 pregunta.
> **EN:** The dating web does not link the secret section, but `GET /robots.txt` lists the crawlers' forbidden routes (`Disallow`). Among them is the hidden route (`/hidden` or `/secret-deeper`); sometimes `/sitemap.xml` is also helpful. Accessing that route (possibly a second page/file) you find the flag. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{l0v3_is_in_th3_r0b0ts_txt}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Web de citas. `nmap`/`curl -I` confirman el servidor; se revisa la home y el rastreo manual.
2. **Paso / Step - robots.txt:** `curl http://<target>/robots.txt` → `User-agent: *` y varias rutas `Disallow`. Una de ellas llama la atención por su nombre (la parte "más profunda del corazón", p. ej. `/secret-deeper` o similar).
3. **Paso / Step - Sitemap (opcional):** Si `/robots.txt` también referencia o no aclara, `GET /sitemap.xml` confirma el listado de páginas no enlazadas.
4. **Paso / Step - Ruta oculta:** Se accede a `GET <ruta>`; el contenido de esa página (o un archivo enlazado desde ella) muestra la flag.
5. **Paso / Step - Flag:** `THM{l0v3_is_in_th3_r0b0ts_txt}`.

### Cadena de ataque / Attack Chain

```
web de citas -> GET /robots.txt
  -> Disallow RutaOculta (p. ej. /secret-deeper, /hidden)
  -> GET RutaOculta (no enlazada, desindexada)
  -> contenido/página con la flag
  -> THM{l0v3_is_in_th3_r0b0ts_txt}
```

**Lección:** `robots.txt`/`sitemap.xml` no son control de acceso: solo piden a los rastreadores educados que no indexen. Cualquier "ruta secreta" listada ahí es, en la práctica, publicidad.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.