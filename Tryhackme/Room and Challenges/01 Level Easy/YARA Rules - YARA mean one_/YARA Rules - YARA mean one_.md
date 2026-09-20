# YARA Rules - YARA mean one!

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `yara-aoc2025-q9w1e3y5u7` | https://tryhackme.com/room/yara-aoc2025-q9w1e3y5u7 | Advent of Cyber 2025 | TryHackMe | YARA rules, regex, image scanning | Detection of hidden strings in files using pattern-matching rules |

---

**Contexto:** El equipo SOC-mas debe escribir reglas YARA para escanear imágenes y detectar cadenas ocultas de un adversario navideño. Se requiere encontrar cuántas imágenes contienen la cadena `TBFC`, construir una regex válida para YARA, y descifrar el mensaje final de McSkidy.

> **ES:** El equipo SOC-mas debe escribir reglas YARA para escanear imágenes y detectar cadenas ocultas de un adversario navideño. Se requiere encontrar cuántas imágenes contienen la cadena `TBFC`, construir una regex válida para YARA, y descifrar el mensaje final de McSkidy.
> **EN:** The SOC-mas team must write YARA rules to scan images and detect hidden strings from a festive adversary. Find how many images contain the string `TBFC`, build a valid YARA regex, and decipher McSkidy's final message.

## Solucionario

### Task 1: Writing YARA Rules

**Explicación:** La tarea 1 (y única) de la sala es el reto de escritura de reglas YARA: escanear imágenes para localizar la cadena `TBFC`, construir la regex `/TBFC:[A-Za-z0-9]+/` y leer el mensaje enviado por McSkidy.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many images contain the string TBFC? | `5` |
| 2 | What regex would you use to match a string that begins with TBFC: followed by one or more alphanumeric ASCII characters? | `/TBFC:[A-Za-z0-9]+/` |
| 3 | What is the message sent by McSkidy? | `Find me in HopSec Island` |

---

**Metodología:** Se escanearon imágenes con `yara` en la terminal para detectar la cadena `TBFC`. Se construyó una regla YARA con la regex `/TBFC:[A-Za-z0-9]+/` para identificar patrones específicos, y se leyó el mensaje oculto en las imágenes marcadas.

### Cadena de ataque / Attack Chain

```text
definir regex /TBFC:[A-Za-z0-9]+/ -> escanear imágenes con yara -> contar coincidencias (5) -> localizar imágenes marcadas -> leer el mensaje de McSkidy
```

**Learning chain:** YARA rule syntax → regex in YARA (`/pattern/`) → scanning files with `yara` CLI → string/pattern enumeration → steganographic message extraction

**Lección:** *Una regex bien construida dentro de una regla YARA permite localizar patrones ocultos en imágenes y en cualquier otro archivo, convirtiendo el escaneo de strings en una técnica de detección precisa.*

**MITRE ATT&CK:** N/A (defensive walkthrough)

**Fuente:** [TryHackMe - YARA Rules - YARA mean one!](https://tryhackme.com/room/yara-aoc2025-q9w1e3y5u7)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.