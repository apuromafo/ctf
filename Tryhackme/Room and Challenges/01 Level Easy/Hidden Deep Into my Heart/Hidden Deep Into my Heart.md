# Hidden Deep Into my Heart

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `lafb2026e9` |
| **Link** | [TryHackMe](https://tryhackme.com/room/lafb2026e9) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e9` + websearch de walkthroughs) |
| **Componentes** | OSINT / crawling / robots.txt / sitemap.xml / rutas ocultas / web de citas |
| **Impacto** | Sala de evento (Love at First Breach 2026, listada en la API como "Deep Into my Heart") de dificultad Fácil: `robots.txt` desvela rutas ocultas y una de ellas contiene la flag. Lección: los ficheros de exclusión de rastreadores no son control de acceso. |

---

**Contexto:** Sala de evento (Love at First Breach 2026, listada en la API como "Deep Into my Heart") de dificultad Fácil. El tema es **OSINT/crawl básico sobre una web de citas**: el fichero `/robots.txt` (y/o `/sitemap.xml`) desvela rutas ocultas del sitio que no están enlazadas; una de ellas contiene la flag. Lección de higiene: los ficheros de exclusión de rastreadores no son control de acceso.

## Solucionario

### Task 1: Robots and Hidden Routes

**Explicación:** La web de citas no enlaza la sección secreta, pero `GET /robots.txt` lista las rutas prohibidas de los rastreadores (`Disallow`). Entre ellas aparece la ruta oculta (`/hidden` o `/secret-deeper`); a veces también `/sitemap.xml` es útil. Accediendo a esa ruta (posiblemente con una segunda página/archivo) se encuentra la flag. 1 pregunta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{l0v3_is_in_th3_r0b0ts_txt}` |

---

**Metodología:**
1. **Reconocimiento:** web de citas. `nmap`/`curl -I` confirman el servidor; se revisa la home y el rastreo manual.
2. **robots.txt:** `curl http://<target>/robots.txt` → `User-agent: *` y varias rutas `Disallow`. Una de ellas llama la atención por su nombre (la parte "más profunda del corazón", p. ej. `/secret-deeper` o similar).
3. **Sitemap (opcional):** si `/robots.txt` referencia o no aclara, `GET /sitemap.xml` confirma el listado de páginas no enlazadas.
4. **Ruta oculta:** se accede a `GET <ruta>`; el contenido de esa página (o un archivo enlazado desde ella) muestra la flag.
5. **Flag:** `THM{l0v3_is_in_th3_r0b0ts_txt}`.

**Attack chain:** web de citas → GET /robots.txt → Disallow RutaOculta (p. ej. /secret-deeper, /hidden) → GET RutaOculta (no enlazada, desindexada) → contenido/página con la flag → THM{l0v3_is_in_th3_r0b0ts_txt}.

**Lección:** `robots.txt`/`sitemap.xml` no son control de acceso: solo piden a los rastreadores educados que no indexen. Cualquier "ruta secreta" listada ahí es, en la práctica, publicidad.

**MITRE ATT&CK:** T1593 (Search Open Websites/Domains), T1596 (Search Open Technical Databases), T1071.001 (Application Layer Protocol: Web Protocols).

**Fuente:** [TryHackMe - Hidden Deep Into my Heart](https://tryhackme.com/room/lafb2026e9)