# Advent 2025\Days [N/A]

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

## Respuestas / Answers
- How many images contain the string TBFC? : `5`
- What regex would you use to match a string that begins with TBFC: followed by one or more alphanumeric ASCII characters? : `/TBFC:[A-Za-z0-9]+/`
- What is the message sent by McSkidy? : `Find me in HopSec Island`

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
