# Letter

| **Dificultad** | Easy |
| **Tipo** | CTF |
| **Slug** | `letter` |
| **Link** | [TryHackMe](https://tryhackme.com/room/letter) |
| **Sección** | 01 Level Easy |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=letter` + websearch de walkthroughs) |
| **Componentes** | OSINT / dcode (código de barras postal) / Gallica / archivos históricos |
| **Impacto** | OSINT con fuentes históricas: del código postal de un sobre al tripulante de un bote salvavidas de 1925 |

---

**Contexto:** Sala de OSINT que arranca de un archivo `.zip` con un sobre postal dañado, un recorte de periódico en francés y una nota personal. Se decodifica el código de barras postal para obtener el código postal y se triangula una identidad histórica con hemerotecas y archivos locales.

## Solucionario

### Task 1: Letter from the past

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the postal code of the delivery address on the envelope? | `29760` |
| 2 | What is the flag? | `THM{Yves-Marie_Gourlaouen_15}` |

---

**Metodología:**
1. **Descargar y extraer:** se abre el `.zip` con el sobre dañado (código de barras postal PLANET/French, marca "Lettre Verte" y logotipo SNSM), un recorte de periódico y una nota en francés.
2. **Código de barras:** decodificar el código postal PLANET/French con dcode → `29760` (Penmarc'h, Finistère).
3. **Datación:** el recorte de L'Ouest-Éclair trata de la expedición de Amundsen (21-may-1925) y de Painlevé como presidente del Consejo (desde abril de 1925) → fecha ≈ 23 de mayo de 1925 (verificable en Gallica).
4. **La nota:** el abuelo era "le benjamin de l'équipe" y no tenía carnet de conducir (demasiado joven).
5. **Historial local:** en el archivo de Penmarc'h, la tripulación del bote salvavidas Arche-d'Alliance incluye a Yves-Marie Gourlaouen, mousse de 15 años con medalla de plata.
6. **Flag:** la identidad triangulada compone `THM{Yves-Marie_Gourlaouen_15}`.

**Learning chain:** .zip → sobre + recorte + nota → barcode PLANET (dcode) → 29760 Penmarc'h → recorte Amundsen/Painlevé → fecha 23-may-1925 → nota ("le benjamin de l'équipe", sin carnet) → archivo local Arche-d'Alliance → Yves-Marie Gourlaouen, 15 años → THM{Yves-Marie_Gourlaouen_15}

**MITRE ATT&CK:** T1593 (Search Open Websites/Domains), T1596 (Search Technical Databases)

**Fuente:** [TryHackMe - Letter](https://tryhackme.com/room/letter)