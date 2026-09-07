# Data Encoding

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `dataencoding` |
| **Link** | [TryHackMe](https://tryhackme.com/room/dataencoding) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + ejercicios estáticos interactivos de ASCII y Unicode |
| **Componentes** | ASCII (7 bits) / Unicode (UTF-16, UTF-32) / puntos de código U+XXXX / encoding vs cifrado |
| **Impacto** | Fundamentos: saber cómo se asignan números a caracteres es la base del encoding/decoding en CTFs, del malware encoding y del manejo de BOM/UTF en forense. |

---

**Contexto:** Un carácter no es más que un número asignado por un estándar. **ASCII** reserva 7 bits (0–127): `@` = **64**, `#` = **35**, y el 7 es el carácter de control **BEL ("Bell", la campanilla de los sistemas antiguos)**. **Unicode** amplía el repertorio con *code points* U+XXXX: un carácter como 😌 (relief, U+1F60C) se escribe en UTF-32 con 4 bytes `0001F60C`; un carácter BMP como シ (katakana "shi", U+30B7) cabe en UTF-16 como `30B7`; y a la inversa, `U+2615` = ☕ (hot beverage) y `U+2658` = ♘ (white chess knight). Distinguir **encoding** de **cifrado** es crucial: el encoding es reversible y público, el cifrado requiere clave.

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - dive into encoding. | `No answer needed` |

### Task 2: ASCII

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the ASCII code in decimal for the character `@`? | `64` |
| 2 | What is the character that has the ASCII code of 35 in decimal? | `#` |
| 3 | What is the name of the character that has the ASCII code of 7? | `Bell` |

### Task 3: Unicode

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the UTF-32 encoding of 😌 (U+1F60C)? | `0001F60C` |
| 2 | What is the UTF-16 encoding of シ (U+30B7)? Note that 😌 and シ are two different characters. | `30B7` |
| 3 | What is the character that has the following UTF-16 encoding `U+2615`? | `☕` |
| 4 | What is the character that has the following UTF-16 encoding `U+2658`? | `♘` |

### Task 4: Conclusión

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