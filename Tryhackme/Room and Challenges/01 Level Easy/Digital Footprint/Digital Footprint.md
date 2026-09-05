# Digital Footprint [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF
* **Slug:** `osintchallengeiv`
* **Link:** https://tryhackme.com/room/osintchallengeiv
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=osintchallengeiv` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de OSINT en 4 tareas: geolocalización por EXIF, recuperación de una web archivada fuera de Wayback, identificación de un monumento y extracción de metadatos de un documento ODF para revelar al autor y la flag final.
> **EN:** OSINT room in 4 tasks: EXIF geolocation, recovery of an archived website outside Wayback, identification of a landmark and metadata extraction from an ODF document to reveal the author and the final flag.

### Task 1 - The Leaked Photo

> **ES:** La foto filtrada tiene EXIF con las coordenadas GPS `26°12'14.76"S 28°2'50.28"E`, que sitúan la ciudad en Johannesburgo (Sudáfrica). 1 pregunta.
> **EN:** The leaked photo has EXIF with GPS coordinates `26°12'14.76"S 28°2'50.28"E`, placing the city in Johannesburg (South Africa). 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In which city was the photo taken? | `Johannesburg` (`THM{Johannesburg}`) |

### Task 2 - Archived Company Website

> **ES:** `warc-acme.com` no aparece en Wayback Machine. Se acude a los WARC Grabs de Archive Team (archive.org); el item `acme.com/jef/` contiene el campo `Firstfiledate` con valor `20160210224602`, que indica la primera publicación de la web. 1 pregunta.
> **EN:** `warc-acme.com` does not appear in the Wayback Machine. The Archive Team WARC Grabs (archive.org) are used; the item `acme.com/jef/` contains the `Firstfiledate` field with value `20160210224602`, indicating the first publication of the site. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| When was the website first published on the internet? | `20160210224602` (`THM{20160210224602}`) |

### Task 3 - Mysterious Landmark

> **ES:** La imagen muestra "The Spire of Dublin". El edificio que lleva el letrero gaélico "ARD OIFIG AN PHOIST" es el General Post Office (GPO) de Dublín. 1 pregunta.
> **EN:** The image shows "The Spire of Dublin". The building carrying the Gaelic sign "ARD OIFIG AN PHOIST" is the General Post Office (GPO) in Dublin. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the landmark? | `General Post Office` (`THM{General Post Office}`) |

### Task 4 - Internal Documents

> **ES:** El documento `.odt` contiene `meta.xml` cuyo metadato de autor es `markwilliams7243`. Buscando ese username se halla un perfil de YouTube con un único post que contiene la flag final. 1 pregunta.
> **EN:** The `.odt` document contains `meta.xml` whose author metadata is `markwilliams7243`. Searching that username finds a YouTube profile with a single post containing the final flag. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the final flag? | `THM{Y0u_f0und_7h3_fin4l_fl4g!}` |

## Metodología / Methodology

1. **Paso / Step - Task 1 (EXIF):** Se extraen los metadatos de la foto; el GPS `26°12'14.76"S 28°2'50.28"E` → Johannesburgo.
2. **Paso / Step - Task 2 (Archivo):** `warc-acme.com` no está en Wayback; en los WARC Grabs de Archive Team el item `acme.com/jef/` tiene `Firstfiledate = 20160210224602`.
3. **Paso / Step - Task 3 (Monumento):** La imagen muestra la Spire de Dublín; el edificio con el letrero gaélico "ARD OIFIG AN PHOIST" es el General Post Office.
4. **Paso / Step - Task 4 (Documento):** El `.odt` → `meta.xml` → autor `markwilliams7243` → perfil de YouTube → post con la flag final.

### Cadena de ataque / Attack Chain

```
Task 1 -> exif foto -> GPS 26°12'14.76"S 28°2'50.28"E -> Johannesburgo -> THM{Johannesburg}
Task 2 -> warc-acme.com NO en Wayback -> Archive Team WARC Grabs (archive.org)
       -> item acme.com/jef/ -> Firstfiledate=20160210224602 -> THM{20160210224602}
Task 3 -> imagen -> Spire of Dublin + letrero "ARD OIFIG AN PHOIST"
       -> General Post Office -> THM{General Post Office}
Task 4 -> .odt -> meta.xml -> markwilliams7243 -> YouTube -> post -> THM{Y0u_f0und_7h3_fin4l_fl4g!}
```

**Lección:** Wayback no es el único archivo: los WARC Grabs de Archive Team guardan lo que Wayback no vio, y los metadatos ODF (meta.xml) filtran a los autores de documentos.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
