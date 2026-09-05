# Missing Person [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** CTF
* **Slug:** `missingperson`
* **Link:** https://tryhackme.com/room/missingperson
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=missingperson` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de OSINT de rastreo de imagen: a partir de un `.zip` con dos fotos (una de comida y una de MotoGP) se reconstruye el itinerario completo de una persona desaparecida — circuito, fecha, restaurante, hora, dirección, DJ y cueva — hasta su número de contacto de un negocio antiguo.
> **EN:** Image-trace OSINT room: from a `.zip` with two photos (one of food and one of MotoGP) the complete itinerary of a missing person is reconstructed — circuit, date, restaurant, time, address, DJ and cave — down to the contact number of an old business.

### Task 1 - Investigate the case

> **ES:** Se extrae el `.zip` con `food.jpg` y `MotoGP.jpg`. Con `exiftool` se obtienen los timestamps: comida a 2025-10-05 19:55:30 y MotoGP a 2025-10-05 12:33:12 (mismo día). Reverse image de la comida → restaurante Cantina Mexicana; de la moto → 2025 MotoGP en el Pertamina Mandalika International Street Circuit (evento 03-05/10/2025). El mensaje ("MotoGP after party… bar") apunta al Surfers Bar de Kuta Lombok (dirección exacta en Google Maps). El poster del evento cita al DJ `Bong Leleh`. La página de Facebook `@bongleleh` menciona "Gua Sumur Lombok" → la cueva Gua Sumur; el número del negocio en la página de FB es `085333137345`. 8 preguntas.
> **EN:** The `.zip` is extracted with `food.jpg` and `MotoGP.jpg`. Using `exiftool` the timestamps are obtained: food at 2025-10-05 19:55:30 and MotoGP at 2025-10-05 12:33:12 (same day). Reverse image of the food → Cantina Mexicana restaurant; of the bike → 2025 MotoGP at the Pertamina Mandalika International Street Circuit (event 03-05/10/2025). The message ("MotoGP after party… bar") points to the Surfers Bar in Kuta Lombok (exact address on Google Maps). The event poster names DJ `Bong Leleh`. The Facebook page `@bongleleh` mentions "Gua Sumur Lombok" → the Gua Sumur cave; the business number on the FB page is `085333137345`. 8 questions.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the commercial name of the circuit (full commercial name)? | `Pertamina Mandalika International Street Circuit` |
| When did the event take place? Format: DD-DD/MM/YYYY | `03-05/10/2025` |
| What is the name of the Mexican restaurant? | `Cantina Mexicana` |
| What time was the photo taken? Format: HH:MM:SS | `19:55:30` |
| What is the full address of the location? Format: As per google maps | `Jl. Raya Kuta, Kuta, Kec. Pujut, Kabupaten Lombok Tengah, Nusa Tenggara Bar.` |
| What is the DJ's stage name? | `Bong Leleh` |
| What is the name of the cave? | `Gua Sumur` |
| What is the phone number linked to his old business? Format: Full number, no country code | `085333137345` |

## Metodología / Methodology

1. **Paso / Step - Extraer y metadatos:** Se abre el `.zip` y se ejecuta `exiftool` sobre `food.jpg` (2025-10-05 19:55:30) y `MotoGP.jpg` (2025-10-05 12:33:12).
2. **Paso / Step - Circuito y fecha:** Reverse image de la moto → 2025 MotoGP en el Pertamina Mandalika International Street Circuit, evento del 03-05/10/2025.
3. **Paso / Step - Restaurante:** Reverse image de la comida → Cantina Mexicana.
4. **Paso / Step - Bar y dirección:** El mensaje "MotoGP after party… bar" → Surfers Bar en Kuta Lombok; dirección exacta `Jl. Raya Kuta, Kuta, Kec. Pujut, Kabupaten Lombok Tengah, Nusa Tenggara Bar.`
5. **Paso / Step - DJ:** El poster del evento nombra al DJ `Bong Leleh`.
6. **Paso / Step - Cueva y teléfono:** La página de Facebook `@bongleleh` menciona "Gua Sumur Lombok" → Gua Sumur; el número del negocio en la página es `085333137345`.

### Cadena de ataque / Attack Chain

```
.zip (food.jpg + MotoGP.jpg)
  -> exiftool -> timestamps (food 05-10-2025 19:55:30 / MotoGP 05-10-2025 12:33:12)
  -> reverse image comida -> Cantina Mexicana
  -> reverse image moto -> Pertamina Mandalika International Street Circuit (03-05/10/2025)
  -> mensaje "MotoGP after party... bar" -> Surfers Bar Kuta Lombok
  -> Jl. Raya Kuta, Kuta, Kec. Pujut, Kabupaten Lombok Tengah, Nusa Tenggara Bar.
  -> poster del evento -> DJ Bong Leleh
  -> FB @bongleleh -> "Gua Sumur Lombok" -> Gua Sumur
  -> número del negocio en FB -> 085333137345
```

**Lección:** Los metadatos EXIF y el rastreo inverso de imágenes reconstruyen un viaje completo, y las redes del objetivo filtran su red de negocios.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
