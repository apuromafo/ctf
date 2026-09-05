# Letter [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF
* **Slug:** `letter`
* **Link:** https://tryhackme.com/room/letter
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=letter` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de OSINT que arranca de un archivo `.zip` con un sobre postal dañado, un recorte de periódico en francés y una nota personal. Se decodifica el código de barras postal para obtener el código postal y se triangula una identidad histórica con hemerotecas y archivos locales.
> **EN:** OSINT room starting from a `.zip` file with a damaged envelope, a French newspaper clipping and a personal note. The postal barcode is decoded to get the postal code and a historical identity is triangulated using newspaper archives and local records.

### Task 1 - Letter from the past

> **ES:** El `.zip` contiene: un sobre dañado (código de barras postal PLANET/French, marca "Lettre Verte" y logotipo SNSM), un recorte de periódico y una nota escrita en francés. Decodificando el código de barras postal con dcode se obtiene `29760` (Penmarc'h, Finistère). El recorte de L'Ouest-Éclair trata de la expedición de Amundsen (21-may-1925) y de Painlevé (presidente del Consejo desde abril de 1925), lo que fecha la escena ≈ 23 de mayo de 1925 (Gallica). La nota dice que el abuelo era "le benjamin de l'équipe" y sin carnet de conducir. Revisando el historial local de Penmarc'h, la tripulación del bote salvavidas Arche-d'Alliance incluye a Yves-Marie Gourlaouen, mousse, 15 años, medalla de plata. 2 preguntas.
> **EN:** The `.zip` contains: a damaged envelope (PLANET/French postal barcode, "Lettre Verte" mark and SNSM logo), a newspaper clipping and a handwritten French note. Decoding the postal barcode with dcode gives `29760` (Penmarc'h, Finistère). The L'Ouest-Éclair clipping is about the Amundsen expedition (21-May-1925) and Painlevé (Council president since April 1925), dating the scene ≈ 23 May 1925 (Gallica). The note says the grandfather was "le benjamin de l'équipe" and had no driving licence. Checking Penmarc'h local records, the crew of the Arche-d'Alliance lifeboat includes Yves-Marie Gourlaouen, a 15-year-old cabin boy, silver medal. 2 questions.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the postal code of the delivery address on the envelope? | `29760` |
| What is the flag? | `THM{Yves-Marie_Gourlaouen_15}` |

## Metodología / Methodology

1. **Paso / Step - Descargar y extraer:** Se abre el `.zip`; contiene el sobre, el recorte y la nota.
2. **Paso / Step - Código de barras:** Se decodifica el código de barras postal PLANET/French con dcode → `29760` (Penmarc'h, Finistère).
3. **Paso / Step - Datación:** El recorte de L'Ouest-Éclair menciona la expedición de Amundsen (21-may-1925) y a Painlevé como presidente del Consejo (desde abril de 1925) → fecha ≈ 23 de mayo de 1925 (Gallica).
4. **Paso / Step - La nota:** El abuelo era "le benjamin de l'équipe" y no tenía carnet de conducir (demasiado joven).
5. **Paso / Step - Historial local:** En el archivo de Penmarc'h, la tripulación del bote salvavidas Arche-d'Alliance incluye a Yves-Marie Gourlaouen, mousse de 15 años con medalla de plata.

### Cadena de ataque / Attack Chain

```
.zip
  -> sobre dañado (código de barras + Lettre Verte + SNSM)
  -> decodificar código de barras postal PLANET/French (dcode)
  -> 29760 (Penmarc'h, Finistère)
  -> recorte L'Ouest-Éclair (Amundsen 21-may-1925 + Painlevé) -> fecha ≈ 23-may-1925
  -> nota en francés ("le benjamin de l'équipe", sin carnet de conducir)
  -> historial local Penmarc'h -> tripulación Arche-d'Alliance
  -> Yves-Marie Gourlaouen, mousse, 15 años, medalla de plata
  -> THM{Yves-Marie_Gourlaouen_15}
```

**Lección:** El OSINT con fuentes históricas (hemerotecas y archivos locales) triangula identidades del pasado, y los códigos de barras postales son datos que no se deben ignorar.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
