# Missing Person

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `missingperson` |
| **Link** | [TryHackMe](https://tryhackme.com/room/missingperson) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=missingperson` + websearch de walkthroughs) |
| **Componentes** | exiftool / reverse image search / Google Maps / OSINT / Facebook |
| **Impacto** | Rastreo OSINT de imagen completo: del plato al circuito, del restaurante al DJ, de la cueva al teléfono de un negocio antiguo |

---

**Contexto:** Sala de OSINT de rastreo de imagen: a partir de un `.zip` con dos fotos (una de comida y una de MotoGP) se reconstruye el itinerario completo de una persona desaparecida — circuito, fecha, restaurante, hora, dirección, DJ y cueva — hasta su número de contacto de un negocio antiguo.

## Solucionario

### Task 1: Investigate the case

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the commercial name of the circuit (full commercial name)? | `Pertamina Mandalika International Street Circuit` |
| 2 | When did the event take place? Format: DD-DD/MM/YYYY | `03-05/10/2025` |
| 3 | What is the name of the Mexican restaurant? | `Cantina Mexicana` |
| 4 | What time was the photo taken? Format: HH:MM:SS | `19:55:30` |
| 5 | What is the full address of the location? Format: As per google maps | `Jl. Raya Kuta, Kuta, Kec. Pujut, Kabupaten Lombok Tengah, Nusa Tenggara Bar.` |
| 6 | What is the DJ's stage name? | `Bong Leleh` |
| 7 | What is the name of the cave? | `Gua Sumur` |
| 8 | What is the phone number linked to his old business? Format: Full number, no country code | `085333137345` |

**Explicación:** Se extrae el `.zip` con `food.jpg` y `MotoGP.jpg`. Con `exiftool` se obtienen los timestamps: comida a 2025-10-05 19:55:30 y MotoGP a 2025-10-05 12:33:12 (mismo día). Reverse image de la comida → restaurante Cantina Mexicana; de la moto → 2025 MotoGP en el Pertamina Mandalika International Street Circuit (evento 03-05/10/2025). El mensaje ("MotoGP after party… bar") apunta al Surfers Bar de Kuta Lombok (dirección exacta en Google Maps). El poster del evento cita al DJ `Bong Leleh`. La página de Facebook `@bongleleh` menciona "Gua Sumur Lombok" → la cueva Gua Sumur; el número del negocio en la página de FB es `085333137345`. 8 preguntas.

**Metodología:**
1. **Extraer y metadatos:** se abre el `.zip` y se ejecuta `exiftool` sobre `food.jpg` (timestamp 2025-10-05 19:55:30) y `MotoGP.jpg` (2025-10-05 12:33:12), ambos del mismo día.
2. **Circuito y fecha:** reverse image de la moto → 2025 MotoGP en el Pertamina Mandalika International Street Circuit (evento 03-05/10/2025).
3. **Restaurante:** reverse image de la comida → Cantina Mexicana.
4. **Bar y dirección:** el mensaje "MotoGP after party… bar" apunta al Surfers Bar de Kuta Lombok; dirección exacta `Jl. Raya Kuta, Kuta, Kec. Pujut, Kabupaten Lombok Tengah, Nusa Tenggara Bar.`
5. **DJ:** el poster del evento cita al DJ `Bong Leleh`.
6. **Cueva y teléfono:** la página de Facebook `@bongleleh` menciona "Gua Sumur Lombok" → cueva Gua Sumur; el número del negocio en la página de FB es `085333137345`.

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

**Learning chain:** .zip (food.jpg + MotoGP.jpg) → exiftool (timestamps 19:55:30 / 12:33:12) → reverse image comida → Cantina Mexicana → reverse image moto → Pertamina Mandalika International Street Circuit (03-05/10/2025) → Surfers Bar Kuta Lombok → dirección Google Maps → poster → DJ Bong Leleh → FB @bongleleh → Gua Sumur → número 085333137345

**MITRE ATT&CK:** T1593 (Search Open Websites/Domains), T1596 (Search Technical Databases)

**Fuente:** [TryHackMe - Missing Person](https://tryhackme.com/room/missingperson)
