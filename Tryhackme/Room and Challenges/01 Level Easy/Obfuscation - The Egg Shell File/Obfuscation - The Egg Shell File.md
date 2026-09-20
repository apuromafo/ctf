# Obfuscation - The Egg Shell File

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `obfuscation-aoc2025-e5r8t2y6u9` | [TryHackMe](https://tryhackme.com/room/obfuscation-aoc2025-e5r8t2y6u9) | `Advent of Cyber 2025` | THM | Obfuscation, C2 URL, API keys, encoding | N/A |

> **Objeto:** Desofuscar una URL de C2 y ofuscar una API key en un script malicioso (Advent of Cyber 2025, Día 18), aplicando el pie de claves de descodificación para revelar los flags ocultos.

---

**Contexto:** En esta sala del Advent of Cyber 2025 (Día 18), se desofusca una URL de C2 y se ofusca una API key en un script malicioso. Se utiliza un pie de claves de descodificación para aplicar codificaciones inversas y revelar los flags ocultos.

> **ES:** En esta sala del Advent of Cyber 2025 (Día 18), se desofusca una URL de C2 y se ofusca una API key en un script malicioso. Se utiliza un pie de claves de descodificación para aplicar codificaciones inversas y revelar los flags ocultos.

> **EN:** In this Advent of Cyber 2025 room (Day 18), a C2 URL is deobfuscated and an API key is obfuscated inside a malicious script. A decoding key table is used to apply reverse encodings and reveal the hidden flags.

## Solucionario

### Task 1: Day 18 - Obfuscation / Day 18 - Obfuscation

**Explicación:** La tarea consiste en revertir la ofuscación de una URL de C2 y ofuscar una API key siguiendo el pie de claves de descodificación del script malicioso, aplicando las codificaciones inversas en el orden correcto hasta recuperar las banderas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the first flag after deobfuscating the C2 URL? | `THM{C2_De0bfuscation_29838}` |
| 2 | What is the second flag after obfuscating the API key? | `THM{API_Obfusc4tion_ftw_0283}` |

---

**Metodología:** Se utilizó una tabla de claves de descodificación para revertir la ofuscación de la URL C2 (reversal, desplazamiento de caracteres, XOR) y revelar el primer flag. Luego se aplicó la ofuscación inversa a la API key para obtener el segundo flag.

### Cadena de ataque / Attack Chain

1. Localizar el script malicioso y el pie de claves de descodificación.
2. Aplicar las codificaciones inversas a la URL de C2 (fase de desofuscación).
3. Recuperar el primer flag: `THM{C2_De0bfuscation_29838}`.
4. Ofuscar la API key siguiendo la tabla para obtener el segundo flag: `THM{API_Obfusc4tion_ftw_0283}`.

**Learning chain:** obfuscation techniques → C2 URL deobfuscation → API key obfuscation → encoding tables → flag extraction

**Lección:** *La ofuscación es un mecanismo de evasión que se revierte identificando primero el tipo de codificación aplicado y ejecutando la transformación inversa paso a paso, sin saltarse ningún eslabón de la cadena.*

**MITRE ATT&CK:** T1027 - Obfuscated Files or Information, T1071.001 - Application Layer Protocol: Web Protocols

**Fuente:** [TryHackMe - Obfuscation - The Egg Shell File](https://tryhackme.com/room/obfuscation-aoc2025-e5r8t2y6u9)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.