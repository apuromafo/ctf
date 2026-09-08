# Water Bottle

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `waterbottle` |
| **Link** | [TryHackMe](https://tryhackme.com/room/waterbottle) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=waterbottle` + websearch de walkthroughs) |
| **Componentes** | OSINT / Google Street View / reconocimiento de imágenes / búsqueda de negocio / números de contacto |
| **Impacto** | OSINT temporal: identificar un negocio desaparecido con Street View histórico y triangular su número de contacto para componer la flag |

---

**Contexto:** Sala de OSINT temporal: hay que identificar un negocio desaparecido (una estación de agua) a partir de la máscara del flag y de imágenes históricas de Street View, y luego cruzar el nombre con su número de contacto para armar la flag.

## Solucionario

### Task 1: Find the water station

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{aquabest_639228721228}` |

**Explicación:** La flag tiene el formato `THM{<Water Station name en lowercase>_<Contact Number>}`, es decir, nombre de 8 caracteres + `_` + ese número (12 dígitos). El número `63922...` se descompone como `63` = código de país de Filipinas + `922` = prefijo de red Globe → queda `63-922-XXX-XXXX`. En Street View histórico de **2014** en Boni Ave (Mandaluyong) se ve "A******t Water Refilling Station" → **Aquabest**. Buscando "Aquabest Mandaluyong Boni" se localiza la página de contacto del negocio con el móvil `+63 922 872 1228` → se arma el formato `aquabest` + `639228721228` → `THM{aquabest_639228721228}`.

---

**Metodología:**
1. **Máscara del flag:** el formato es `THM{<Water Station name en lowercase>_<Contact Number>}`, es decir, nombre de 8 caracteres + `_` + ese número.
2. **Deconstruir el número:** `63922...` se descompone como `63` = código de país de Filipinas + `922` = prefijo de red Globe → queda `63-922-XXX-XXXX` (12 dígitos).
3. **Street View histórico:** en Boni Ave (Mandaluyong), la vista histórica de **2014** muestra "A******t Water Refilling Station" → **Aquabest**.
4. **Identificar el negocio:** buscando "Aquabest Mandaluyong Boni" se localiza la página de contacto del negocio, que da la dirección y el móvil `+63 922 872 1228`.
5. **Flag:** se arma el formato: `aquabest` + `639228721228` → `THM{aquabest_639228721228}`.

**Learning chain:** formato del flag (nombre lowercase + `_` + 12 dígitos) → 63922... → 63 = PH (Filipinas) + 922 = prefijo Globe → Street View histórico 2014 en Boni Ave → "A******t Water Refilling Station" → Aquabest → buscar Aquabest Mandaluyong Boni → página de contacto → móvil +63 922 872 1228 → aquabest_639228721228 → THM{aquabest_639228721228}

**MITRE ATT&CK:** T1593 (Search Open Websites/Domains), T1596 (Search Technical Databases)

**Fuente:** [TryHackMe - Water Bottle](https://tryhackme.com/room/waterbottle)