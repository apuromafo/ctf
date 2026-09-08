# Data Encoding

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `dataencoding` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dataencoding) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + ejercicios estáticos interactivos de ASCII y Unicode |
| **Componentes** | ASCII (7 bits) / Unicode (UTF-16, UTF-32) / puntos de código U+XXXX / encoding vs cifrado |
| **Impacto** | Fundamentos: saber cómo se asignan números a caracteres es la base del encoding/decoding en CTFs, del malware encoding (ofuscación en ASCII/Unicode) y del manejo de BOM/UTF en forense. |

---

**Contexto:** Un carácter no es más que un número asignado por un estándar. **ASCII** reserva 7 bits (0–127): `@` = **64**, `#` = **35**, y el 7 es el carácter de control **BEL ("Bell", la campanilla de los sistemas antiguos)**. **Unicode** amplía el repertorio con *code points* U+XXXX: un carácter como 😌 (relief, U+1F60C) se escribe en UTF-32 con 4 bytes `0001F60C`; un carácter BMP como シ (katakana "shi", U+30B7) cabe en UTF-16 como `30B7`; y a la inversa, `U+2615` = ☕ (hot beverage) y `U+2658` = ♘ (white chess knight). Distinguir **encoding** (representación interna de un carácter) de **cifrado** es crucial: el encoding es reversible y público, el cifrado requiere clave.

## Solucionario

### Task 1: Introducción

**Explicación:** Segundo bloque de representación de datos (Pre Security); continúa de Data Representation. Introduce que un carácter no es más que un número asignado por un estándar. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - dive into encoding. | `No answer needed` |

### Task 2: ASCII

**Explicación:** El estándar ASCII reserva 7 bits (0–127). **`@` = 64:** primer símbolo del bloque de "signos" tras las mayúsculas. **35 = `#`:** el símbolo hash/number sign. **7 = `Bell`:** carácter de control (los primeros 32 códigos ASCII son control characters; el 7 hacía sonar la campanilla del terminal). Consultar la tabla ASCII o el conversor del room.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the ASCII code in decimal for the character `@`? | `64` |
| 2 | What is the character that has the ASCII code of 35 in decimal? | `#` |
| 3 | What is the name of the character that has the ASCII code of 7? | `Bell` |

### Task 3: Unicode

**Explicación:** Unicode amplía el repertorio con *code points* U+XXXX. **UTF-32** fija 4 bytes por code point → `0001F60C` (relleno a 8 dígitos hex) para 😌. **UTF-16** usa 2 bytes por code point BMP → `30B7` para シ (katakana "shi"). A la inversa, **U+2615 → ☕** (hot beverage / taza caliente) y **U+2658 → ♘** (white chess knight / caballo de ajedrez blanco).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the UTF-32 encoding of 😌 (U+1F60C)? | `0001F60C` |
| 2 | What is the UTF-16 encoding of シ (U+30B7)? Note that 😌 and シ are two different characters. | `30B7` |
| 3 | What is the character that has the following UTF-16 encoding `U+2615`? | `☕` |
| 4 | What is the character that has the following UTF-16 encoding `U+2658`? | `♘` |

### Task 4: Conclusión

**Explicación:** Cierra el bloque: tras colores y numeración, ahora sabes codificar caracteres. Encolar con el room de Python Demo (si existe) para ver manipulación real de bits. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - conclusion. | `No answer needed` |

---

**Metodología:**
1. Consultar la tabla ASCII (o el conversor del room) para los códigos 64, 35 y 7: `@` = 64 (primer símbolo del bloque de signos tras las mayúsculas), 35 = `#`, y 7 = `Bell` (carácter de control; los primeros 32 códigos ASCII son control characters).
2. En Unicode, anotar el *code point* U+XXXX de cada carácter y convertirlo a UTF-16 (igual si es BMP, 2 bytes por code point) o UTF-32 (4 bytes fijos, relleno a 8 dígitos hex): 😌 = `0001F60C`, シ = `30B7`.
3. Para la inversa, mapear el U+ al glifo: U+2615 → ☕ (hot beverage), U+2658 → ♘ (white chess knight).

**Learning chain:** carácter → code point (U+XXXX) → UTF-16 (2 bytes BMP) [シ = 30B7] → UTF-32 (4 bytes) [😌 = 0001F60C] → ASCII (7 bits) [@ = 64, # = 35, 7 = Bell] → encoding != cifrado (reversible vs. requiere clave).

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1140 (Deobfuscate/Decode Files or Information).

**Fuente:** [TryHackMe - Data Encoding](https://tryhackme.com/room/dataencoding)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
