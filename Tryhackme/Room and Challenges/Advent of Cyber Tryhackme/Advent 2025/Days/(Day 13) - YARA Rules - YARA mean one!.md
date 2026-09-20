# YARA Rules - YARA mean one!

| **Dificultad** | Easy | **Tipo** | walkthrough | **Slug** | `day13yararulesyarameanone` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber25) |
| **Sección** | Advent of Cyber Tryhackme |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | YARA / malware identification / strings / conditions / metadata / regex / nocase / wide / ascii / xor / base64 / man yara |
| **Impacto** | Crear y usar reglas YARA para identificar malware buscando patrones únicos en archivos |

---

**Contexto:** Día 13 del Advent of Cyber 2025. Se presenta YARA, una herramienta que identifica y clasifica malware buscando patrones únicos (las "huellas digitales" que dejan los atacantes). Se cubren los momentos de uso (análisis post-incidente, threat hunting, escaneos basados en inteligencia y análisis de memoria), los elementos de una regla (metadata, strings y conditions), los modificadores de strings (nocase, wide, ascii, xor, base64) y los flags útiles de `man yara` (`-r` para scan recursivo, `-s` para imprimir las strings que coinciden).

## Solucionario

### Día 13: YARA Rules - YARA mean one!

**Explicación:**

- YARA is a tool built to identify and classify malware by searching for unique patterns, the digital fingerprints left behind by attackers

- When to use YARA
    1. Post-incident analysis
    2. Threat Hunting
    3. Intelligence-based scans
    4. Memory analysis

- A YARA rule is built from several key elements:
     1. Metadata: information about the rule itself: who created it, when, and for what purpose.
     2. Strings: the clues YARA searches for: text, byte sequences, or regular expressions that mark suspicious content.
     3. Conditions: the logic that decides when the rule triggers, combining multiple strings or parameters into a single decision.

- Strings
     1. `nocase` modifier makes the match ignore letter casing
     2. Adding `wide` tells YARA to also look for this format, while `ascii` enforces a single-byte search
     3. `xor` modifier in YARA automatically checks all possible single-byte XOR variations of a string - revealing what attackers tried to conceal
     4. `Base64` command decodes the content and searches for the original pattern, even when it’s hidden in encoded form

- We can use the `man yara` command to find out what flags could be useful in our scenario, and we find the following:
    1. `-r` - Allows YARA to scan directories recursively and follow symlinks
    2. `-s` - Prints the strings found within files that match the rule

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many images contain the string TBFC? | `5` |
| 2 | What regex would you use to match a string that begins with TBFC: followed by one or more alphanumeric ASCII characters? | `/TBFC:[A-Za-z0-9]+/` |
| 3 | What is the message sent by McSkidy? | `Find me in HopSec Island` |

---

**Metodología:** Se escribió una regla YARA con la string `TBFC` (con modifiers como nocase/xor/base64 y condiciones adecuadas) y se usó `yara -r -s` para escanear recursivamente el directorio de imágenes y contar las que contienen la string. Se definió la regex `TBFC:[A-Za-z0-9]+` para cualquier string que comience con `TBFC:` seguida de caracteres alfanuméricos ASCII, y se extrajo el mensaje de McSkidy de la imagen coincidente.
**Learning chain:** YARA -> post-incident analysis / threat hunting / memory analysis -> metadata + strings + conditions -> modifiers (nocase/wide/ascii/xor/base64) -> yara -r -s -> regex TBFC -> mensaje de McSkidy

Cadena de ataque / Attack Chain:
```
regla YARA (strings $tb = "TBFC" + conditions) -> yara -r -s regla.yar ./imagenes -> 5 imágenes con TBFC -> regex /TBFC:[A-Za-z0-9]+/ -> decodificación del mensaje -> "Find me in HopSec Island"
```

**Lección:** *Una regla YARA bien formada (metadata + strings + conditions) convierte un patrón concreto en un detector accionable; los modificadores nocase/wide/xor/base64 amplían la caza a versiones ofuscadas que un byte exacto jamás encontraría.*

**MITRE ATT&CK:** T1027 - Obfuscated Files or Information (detección con YARA), T1204.002 - User Execution: Malicious File (detección con YARA)

**Fuente:** [TryHackMe - YARA Rules - YARA mean one!](https://tryhackme.com/room/adventofcyber25)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.