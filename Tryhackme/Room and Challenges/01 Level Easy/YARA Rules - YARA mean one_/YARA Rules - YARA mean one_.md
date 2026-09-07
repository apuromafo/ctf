# YARA Rules - YARA mean one!

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `yara-aoc2025-q9w1e3y5u7` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/yara-aoc2025-q9w1e3y5u7) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | YARA rules, regex, image scanning |
| **Impacto** | Detection of hidden strings in files using pattern-matching rules |

---

**Contexto:** El equipo SOC-mas debe escribir reglas YARA para escanear imágenes y detectar cadenas ocultas de un adversario navideño. Se requiere encontrar cuántas imágenes contienen la cadena `TBFC`, construir una regex válida para YARA, y descifrar el mensaje final de McSkidy.

## Solucionario

### Task 1: Writing YARA Rules

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many images contain the string TBFC? | `5` |
| 2 | What regex would you use to match a string that begins with TBFC: followed by one or more alphanumeric ASCII characters? | `/TBFC:[A-Za-z0-9]+/` |
| 3 | What is the message sent by McSkidy? | `Find me in HopSec Island` |

---

**Metodología:** Se escanearon imágenes con `yara` en la terminal para detectar la cadena `TBFC`. Se construyó una regla YARA con la regex `/TBFC:[A-Za-z0-9]+/` para identificar patrones específicos, y se leyó el mensaje oculto en las imágenes marcadas.
**Learning chain:** YARA rule syntax → regex in YARA (`/pattern/`) → scanning files with `yara` CLI → string/pattern enumeration → steganographic message extraction
**MITRE ATT&CK:** N/A (defensive walkthrough)
**Fuente:** [TryHackMe - YARA Rules - YARA mean one!](https://tryhackme.com/r/room/yara-aoc2025-q9w1e3y5u7)
