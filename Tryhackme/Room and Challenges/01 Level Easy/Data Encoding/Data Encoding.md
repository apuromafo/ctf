# Data Encoding [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `dataencoding`
* **Link:** https://tryhackme.com/room/dataencoding
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + ejercicios estáticos interactivos de ASCII y Unicode
* **Componentes:** ASCII (7 bits) · Unicode (UTF-16, UTF-32) · puntos de código U+XXXX
* **Impacto rol:** Fundamentos; entender cómo se asignan números a caracteres es la base del encoding/decoding en CTFs, del **malware encoding** (ofuscación en ASCII/Unicode) y del manejo de BOM/UTF en análisis forense.

## Solucionario de Tareas / Task Solutions

> **ES:** Un carácter no es más que un número asignado por un estándar. **ASCII** reserva 7 bits (0–127): `@` = **64**, `#` = **35**, y el 7 es el carácter de control **BEL ("Bell", la campanilla de los sistemas antiguos)**. **Unicode** amplía el repertorio con *code points* U+XXXX: un carácter como 😌 (relief, U+1F60C) se escribe en UTF-32 con 4 bytes `0001F60C`; un carácter BMP como シ (katakana "shi", U+30B7) cabe en UTF-16 como `30B7`; y a la inversa, `U+2615` = ☕ (hot beverage) y `U+2658` = ♘ (white chess knight). Saber distinguir **encoding** (representación interna de un carácter) de **cifrado** es crucial: el encoding es reversible y público, el cifrado requiere clave.
> **EN:** A character is just a number assigned by a standard. **ASCII** uses 7 bits (0–127): `@` = **64**, `#` = **35**, and 7 is the control character **BEL ("Bell", ring the terminal)**. **Unicode** extends the repertoire with *code points* U+XXXX: a character like 😌 (relief, U+1F60C) is written in UTF-32 as 4 bytes `0001F60C`; a BMP character like シ (katakana "shi", U+30B7) fits in UTF-16 as `30B7`; and conversely, `U+2615` = ☕ (hot beverage) and `U+2658` = ♘ (white chess knight). Knowing the difference between **encoding** (internal byte representation of a character) and **encryption** is key: encoding is reversible and public, encryption needs a key.

### Task 1 — Introducción / Introduction

* **Check:** `It is time to dive into encoding.`
* **ES:** Segundo bloque de representación de datos (Pre Security); continua de Data Representation.
* **EN:** Second data-representation block (Pre Security); follows Data Representation.

### Task 2 — ASCII *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the ASCII code in decimal for the character `@`? | `64` |
| What is the character that has the ASCII code of 35 in decimal? | `#` |
| What is the name of the character that has the ASCII code of 7? | `Bell` |

* **`@` = 64:** primer símbolo del bloque de "signos" tras las mayúsculas (0-...-64).
* **35 = `#`:** el símbolo hash/number sign.
* **7 = `Bell`:** carácter de control (los primeros 32 códigos ASCII son control characters; el 7 hacía sonar la campanilla del terminal).

### Task 3 — Unicode *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the UTF-32 encoding of 😌 (U+1F60C)? | `0001F60C` |
| What is the UTF-16 encoding of シ (U+30B7)? Note that 😌 and シ are two different characters. | `30B7` |
| What is the character that has the following UTF-16 encoding `U+2615`? | `☕` |
| What is the character that has the following UTF-16 encoding `U+2658`? | `♘` |

* **UTF-32:** fija 4 bytes por code point → `0001F60C` (relleno a 8 dígitos hex).
* **UTF-16:** 2 bytes por code point BMP → `30B7` (シ, katakana "shi").
* **U+2615 → ☕** (hot beverage / taza caliente); **U+2658 → ♘** (white chess knight / caballo de ajedrez blanco).

### Task 4 — Conclusión / Conclusion

* **Check:** `If you are curious to see how computers manipulate data, join the Python Demo room (coming soon).`
* **ES:** Cierra el bloque: tras colores y numeración, ahora sabes codificar caracteres. Encadenar con Python Demo (si existe) para ver manipulación real de bits.
* **EN:** Wraps up the block: colours, numbers and now characters. Next step is the (optional) Python Demo room to see real bit manipulation.

## Metodología / Methodology

1. **Paso / Step:** Consultar la tabla ASCII (o el conversor del room) para los códigos 64, 35 y 7.
2. **Paso / Step:** En Unicode, anotar el *code point* U+XXXX de cada carácter y convertirlo a UTF-16 (igual si es BMP) o UTF-32 (relleno a 4 bytes/8 dígitos).
3. **Paso / Step:** Para la inversa, mapear el U+ al glifo: U+2615 → ☕, U+2658 → ♘.

### Cadena de aprendizaje / Learning Chain

```
carácter -> code point (U+XXXX)
  -> UTF-16 (2 bytes BMP)  [シ = 30B7]
  -> UTF-32 (4 bytes)      [😌 = 0001F60C]
  -> ASCII (7 bits)        [@ = 64, # = 35, 7 = Bell]
  -> encoding != cifrado   (reversible vs. requiere clave)
```

**Mapeo MITRE ATT&CK / relacionado:** T1027 (Obfuscated Files/Information) — el encoding ASCII/Unicode se usa para ofuscar payloads y comandos; T1140 (Deobfuscate/Decode Files) — decodificar. El room es teórico de fundamentos.

**Lección:** *Encoding no es cifrado.* Cualquiera puede revertir un encoding estándar; la defensa ante "datos ofuscados" empieza por saber reconocer y decodificar ASCII/Unicode/UTF-*.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.