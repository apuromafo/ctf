# Digital Footprint

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `osintchallengeiv` |
| **Link** | [TryHackMe](https://tryhackme.com/room/osintchallengeiv) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=osintchallengeiv` + websearch de walkthroughs) |
| **Componentes** | OSINT / EXIF / GPS / Wayback Machine / Archive Team WARC Grabs / metadatos ODF / meta.xml / YouTube |
| **Impacto** | Geolocaliza por EXIF, recupera webs archivadas fuera de Wayback, identifica un monumento y extrae metadatos ODF para revelar al autor y la flag final. |

---

**Contexto:** Sala de OSINT en 4 tareas: geolocalización por EXIF, recuperación de una web archivada fuera de Wayback, identificación de un monumento y extracción de metadatos de un documento ODF para revelar al autor y la flag final.

## Solucionario

### Task 1: The Leaked Photo

**Explicación:** La foto filtrada tiene EXIF con las coordenadas GPS `26°12'14.76"S 28°2'50.28"E`, que sitúan la ciudad en Johannesburgo (Sudáfrica). 1 pregunta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In which city was the photo taken? | `Johannesburg` (`THM{Johannesburg}`) |

### Task 2: Archived Company Website

**Explicación:** `warc-acme.com` no aparece en Wayback Machine. Se acude a los WARC Grabs de Archive Team (archive.org); el item `acme.com/jef/` contiene el campo `Firstfiledate` con valor `20160210224602`, que indica la primera publicación de la web. 1 pregunta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When was the website first published on the internet? | `20160210224602` (`THM{20160210224602}`) |

### Task 3: Mysterious Landmark

**Explicación:** La imagen muestra "The Spire of Dublin". El edificio que lleva el letrero gaélico "ARD OIFIG AN PHOIST" es el General Post Office (GPO) de Dublín. 1 pregunta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the landmark? | `General Post Office` (`THM{General Post Office}`) |

### Task 4: Internal Documents

**Explicación:** El documento `.odt` contiene `meta.xml` cuyo metadato de autor es `markwilliams7243`. Buscando ese username se halla un perfil de YouTube con un único post que contiene la flag final. 1 pregunta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the final flag? | `THM{Y0u_f0und_7h3_fin4l_fl4g!}` |

---

**Metodología:**
1. **Task 1 (EXIF):** se extraen los metadatos de la foto filtrada; el GPS `26°12'14.76"S 28°2'50.28"E` sitúa la ciudad en Johannesburgo (Sudáfrica).
2. **Task 2 (Archivo):** `warc-acme.com` no aparece en Wayback Machine; en los WARC Grabs de Archive Team (archive.org) el item `acme.com/jef/` contiene el campo `Firstfiledate` con valor `20160210224602`.
3. **Task 3 (Monumento):** la imagen muestra "The Spire of Dublin"; el edificio que lleva el letrero gaélico "ARD OIFIG AN PHOIST" es el General Post Office (GPO) de Dublín.
4. **Task 4 (Documento):** el `.odt` contiene `meta.xml` cuyo metadato de autor es `markwilliams7243`; buscando ese username se halla un perfil de YouTube con un único post que contiene la flag final.

**Learning chain:** Task 1 → exif foto → GPS → Johannesburgo → THM{Johannesburg} → Task 2 → warc-acme.com NO en Wayback → Archive Team WARC Grabs → Firstfiledate=20160210224602 → Task 3 → Spire of Dublin + letrero → General Post Office → Task 4 → .odt → meta.xml → markwilliams7243 → YouTube → flag final.

**Lección:** Wayback no es el único archivo: los WARC Grabs de Archive Team guardan lo que Wayback no vio, y los metadatos ODF (meta.xml) filtran a los autores de documentos.

**MITRE ATT&CK:** T1596 (Search Open Technical Databases), T1593 (Search Open Websites/Domains), T1589 (Gather Victim Identity Information).

**Fuente:** [TryHackMe - Digital Footprint](https://tryhackme.com/room/osintchallengeiv)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
