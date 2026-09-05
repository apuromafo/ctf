# Water Bottle [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF
* **Slug:** `waterbottle`
* **Link:** https://tryhackme.com/room/waterbottle
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=waterbottle` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de OSINT temporal: hay que identificar un negocio desaparecido (una estación de agua) a partir de la máscara del flag y de imágenes históricas de Street View, y luego cruzar el nombre con su número de contacto para armar la flag.
> **EN:** Temporal OSINT room: a vanished business (a water station) must be identified from the flag mask and historical Street View imagery, and then the name is cross-referenced with its contact number to build the flag.

### Task 1 - Find the water station

> **ES:** La máscara del flag es `THM{<Water Station name en lowercase>_<Contact Number>}`, es decir, nombre de 8 caracteres + `_` + 12 dígitos. `63922` se descompone como prefijo de país PH (`63`) + prefijo de red Globe (`922`) → `63-922-XXX-XXXX`. En Street View histórico de 2014 sobre Boni Ave (Mandaluyong) se lee "A******t Water Refilling Station", es decir "Aquabest". Buscando "Aquabest Mandaluyong Boni" se llega a su página con contacto, que da la dirección y el móvil `+63 922 872 1228`; el flag en formato es `aquabest` + `639228721228`. 1 pregunta.
> **EN:** The flag mask is `THM{<Water Station name in lowercase>_<Contact Number>}`, i.e. an 8-char name + `_` + 12 digits. `63922` decomposes as the PH country code (`63`) + Globe network prefix (`922`) → `63-922-XXX-XXXX`. In 2014 historical Street View on Boni Ave (Mandaluyong) the sign reads "A******t Water Refilling Station", i.e. "Aquabest". Searching "Aquabest Mandaluyong Boni" reaches its contact page, giving the address and mobile `+63 922 872 1228`; the formatted flag is `aquabest` + `639228721228`. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{aquabest_639228721228}` |

## Metodología / Methodology

1. **Paso / Step - Máscara del flag:** El formato exige nombre en lowercase + `_` + 12 dígitos (nº de contacto).
2. **Paso / Step - Deconstruir el número:** `63922...` → `63` = código de país de Filipinas, `922` = prefijo Globe, quedando `63-922-XXX-XXXX`.
3. **Paso / Step - Street View histórico:** En Boni Ave (Mandaluyong) la vista histórica de 2014 muestra "A******t Water Refilling Station" → Aquabest.
4. **Paso / Step - Identificar el negocio:** Buscando "Aquabest Mandaluyong Boni" se localiza la página con contacto del negocio.
5. **Paso / Step - Contacto:** La página da el móvil `+63 922 872 1228`.
6. **Paso / Step - Flag:** Se arma el formato: `aquabest` + `639228721228`.

### Cadena de ataque / Attack Chain

```
formato del flag (nombre lowercase + _ + 12 dígitos)
  -> 63922... -> 63 = PH (Filipinas) + 922 = prefijo Globe
  -> Street View histórico 2014 en Boni Ave -> "A******t Water Refilling Station" -> Aquabest
  -> buscar Aquabest Mandaluyong Boni -> página de contacto
  -> móvil +63 922 872 1228
  -> aquabest_639228721228 -> THM{aquabest_639228721228}
```

**Lección:** Los metadatos históricos de Street View preservan negocios ya desaparecidos, algo clave para el OSINT temporal.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
