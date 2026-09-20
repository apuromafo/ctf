# Google Dorking

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `googledorking` | [TryHackMe](https://tryhackme.com/room/googledorking) | 01 Level Easy | THM | Google Dorking, SEO, Robots.txt, Sitemaps, Operadores | OSINT mediante búsquedas avanzadas en Google |

---

**Contexto:** Sala que introduce el Google Dorking: cómo funcionan los buscadores y el SEO/crawling, qué es robots.txt y los sitemaps, y cómo usar operadores de búsqueda (site:, filetype:, intitle:) para localizar información sensible en Internet.

> **ES:** Comprender buscadores y SEO, leer robots.txt y sitemaps, y aplicar dorks de Google para OSINT.
> **EN:** Understand search engines and SEO, read robots.txt and sitemaps, and apply Google dorks for OSINT.

## Solucionario

### Task 1: Buscadores / Search Engines

**Explicación:** Presentación de la sala y de cómo funcionan los buscadores.

No answer needed

### Task 2: SEO / SEO

**Explicación:** Repaso de los conceptos de SEO: indexación, rastreo (crawling) y keywords.

1. `Index`
2. `Crawling`
3. `Keywords`

### Task 3: Introducción al dorking / Intro to Dorking

**Explicación:** Introducción a la idea de usar operadores avanzados de búsqueda.

No answer needed

### Task 4: Robots.txt / Robots.txt

**Explicación:** Análisis del archivo robots.txt: las páginas que se deben descargar, el sitemap referenciado, el user-agent bloqueado, la ruta disallow y la extensión que se quiere ocultar.

1. `ablog.com/robots.txt`
2. `/sitemap.xml`
3. `User-agent: Bingbot`
4. `Disallow: /dont-index-me/`
5. `.conf`

### Task 5: Sitemaps / Sitemaps

**Explicación:** Los sitemaps aportan la estructura del contenido indexable; se identifican sus elementos principales.

1. `XML`
2. `Map`
3. `Route`

### Task 6: Dorking / Dorking

**Explicación:** Aplicación de dorks reales: filtrar por dominio con `site:`, por tipo de archivo con `filetype:` y por título con `intitle:`.

1. `site: bbc.co.uk flood defences`
2. `filetype:`
3. `intitle: login`

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Concepto de SEO 1 | `Index` |
| 2.2 | Concepto de SEO 2 | `Crawling` |
| 2.3 | Concepto de SEO 3 | `Keywords` |
| 3 | — | `No answer needed` |
| 4.1 | Página de ejemplo con robots.txt | `ablog.com/robots.txt` |
| 4.2 | Sitemap referenciado | `/sitemap.xml` |
| 4.3 | User-agent bloqueado | `User-agent: Bingbot` |
| 4.4 | Ruta disallow | `Disallow: /dont-index-me/` |
| 4.5 | Extensión a ocultar | `.conf` |
| 5.1 | Tipo de sitemap | `XML` |
| 5.2 | Elemento del sitemap | `Map` |
| 5.3 | Elemento del sitemap | `Route` |
| 6.1 | Dork por dominio | `site: bbc.co.uk flood defences` |
| 6.2 | Dork por tipo de archivo | `filetype:` |
| 6.3 | Dork por título | `intitle: login` |

---

**Metodología:** Comprender la indexación y el SEO, inspeccionar robots.txt y los sitemaps para conocer lo que el sitio permite indexar, y aplicar operadores (site:, filetype:, intitle:) para descubrir contenido sensible no expuesto directamente.

### Cadena de ataque / Attack Chain

```text
Buscadores/SEO -> robots.txt (sitemap, user-agents, disallow) -> sitemaps -> dorks (site:, filetype:, intitle:) -> datos sensibles indexados
```

**Learning chain:** Search engines → SEO → robots.txt → Sitemaps → Google Dorking

**Lección:** *Los buscadores indexan más de lo que parece: revisar robots.txt y usar dorks como `site:`, `filetype:` e `intitle:` expone contenido que el dueño del sitio confiaba en ocultar.*

**MITRE ATT&CK:** N/A (Room de OSINT/reconocimiento)

**Fuente:** [TryHackMe - Google Dorking](https://tryhackme.com/room/googledorking)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.