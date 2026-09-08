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

**Explicación:** Fundamentos de la representación de datos en el ordenador (parte de Pre Security): un ordenador solo manipula bits, y todo (incluido el "color verde") se representa como números binarios. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - dive into computer colors. | `No answer needed` |

### Task 2: Representando Colores

**Explicación:** El color se representa con 3 bytes RGB (Red, Green, Blue). El simulador visual de color te da el hex y calcula el valor de cada canal. **`#EB0037`:** `EB`=`11101011`, `00`=`00000000`, `37`=`00110111` (8 bits por canal). **`#D4D8DF`:** `D4`=`212`, `D8`=`216`, `DF`=`223` (D4=13·16+4=212; D8=13·16+8=216; DF=13·16+15=223).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preview the color `#3BC81E`. In one word, what does this color appear to be? | `green` |
| 2 | What is the binary representation of the color `#EB0037`? | `11101011 00000000 00110111` |
| 3 | What is the decimal representation of the color `#D4D8DF`? | `212 216 223` |

### Task 3: Números: De Decimal a Hexadecimal

**Explicación:** **`FF` binario:** cada dígito hex = 4 bits → F=`1111` → `FF`=`11111111`. **`AB` decimal:** A=`10`, B=`11` → `10·16 + 11` = `171`. **`FFFFFF` decimal:** `255·65536 + 255·256 + 255` = `16.777.215`; redondeado al millón más cercano → **17 millones** (respuesta: `17`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the hexadecimal `FF` in binary? | `11111111` |
| 2 | What is the hexadecimal `AB` in decimal? | `171` |
| 3 | Convert the hexadecimal `FF FF FF` to decimal. After you round up the decimal value to the nearest million, **how many millions is that**? | `17` |

### Task 4: Conclusión

**Explicación:** Cierra el bloque de numeración; el siguiente paso es cómo los ordenadores codifican caracteres (Data Encoding). Sin respuesta requerida.

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

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
