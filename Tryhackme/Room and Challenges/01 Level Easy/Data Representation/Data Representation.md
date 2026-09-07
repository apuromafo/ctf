# Data Representation

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `datarepresentation` |
| **Link** | [TryHackMe](https://tryhackme.com/room/datarepresentation) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + ejercicios estáticos interactivos de color y números |
| **Componentes** | Colores (hex ↔ canales RGB) / sistemas de numeración: binario, decimal, hexadecimal |
| **Impacto** | Fundamentos puros: entender que un ordenador representa todo (incluido el "color verde") como números binarios explica luego cifrado, encoding, debugging y forense. |

---

**Contexto:** Un ordenador solo manipula bits. El color se representa con 3 bytes RGB (Red, Green, Blue): `#3BC81E` = rojo `3B`, verde `C8`, azul `1E` en hexadecimal. Convertir `C8` (hex) = `200` decimal = `11001000` binario explica el verde. Lo mismo aplica a números: `FF` hex = `255` decimal = `11111111` binario; y `FFFFFF` = 16.777.215 ≈ **17 millones** (de ahí los "millones de colores" de las pantallas modernas). Convertir mentalmente hex↔decimal↔binario es una skill esencial para CTF y análisis de memoria.

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - dive into computer colors. | `No answer needed` |

### Task 2: Representando Colores

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preview the color `#3BC81E`. In one word, what does this color appear to be? | `green` |
| 2 | What is the binary representation of the color `#EB0037`? | `11101011 00000000 00110111` |
| 3 | What is the decimal representation of the color `#D4D8DF`? | `212 216 223` |

### Task 3: Números: De Decimal a Hexadecimal

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the hexadecimal `FF` in binary? | `11111111` |
| 2 | What is the hexadecimal `AB` in decimal? | `171` |
| 3 | Convert the hexadecimal `FF FF FF` to decimal. After you round up the decimal value to the nearest million, **how many millions is that**? | `17` |

### Task 4: Conclusión

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - conclusion. | `No answer needed` |

---

**Metodología:**
1. Usar el convertidor del room (estático) o cálculo mental: hex→bin (cada dígito = 4 bits: F=`1111` → `FF`=`11111111`), hex→dec (`d·16^1 + u`: `AB` = `10·16 + 11` = `171`), bin→dec.
2. En colores, dividir los 6 dígitos en 3 pares (R, G, B) y convertir cada par: `#EB0037` → `EB`=`11101011`, `00`=`00000000`, `37`=`00110111`; `#D4D8DF` → `D4`=`212`, `D8`=`216`, `DF`=`223`.
3. Para `FFFFFF` calcular los 3 bytes: `255·65536 + 255·256 + 255` = `16.777.215`; redondear al millón más cercano → **17 millones** (respuesta `17`).

**Learning chain:** bit / byte → sistema decimal (base 10) → sistema binario (base 2) [FF = 11111111] → sistema hexadecimal (base 16) [AB = 171] → colores RGB = 3 bytes [#FFFFFF ≈ 17 millones de colores].

**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1140 (Deobfuscate/Decode Files or Information).

**Fuente:** [TryHackMe - Data Representation](https://tryhackme.com/room/datarepresentation)