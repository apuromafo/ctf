# Data Representation [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `datarepresentation`
* **Link:** https://tryhackme.com/room/datarepresentation
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + ejercicios estáticos interactivos de color y números
* **Componentes:** Colores (hex ↔ canales RGB) · sistemas de numeración: binario, decimal, hexadecimal
* **Impacto rol:** Fundamentos puros; entender que un ordenador representa todo (incluido el "color verde") como números binarios explica luego cifrado, encoding, debugging y forense.

## Solucionario de Tareas / Task Solutions

> **ES:** Un ordenador solo manipula bits. El color se representa con 3 bytes RGB (Red, Green, Blue): `#3BC81E` = rojo `3B`, verde `C8`, azul `1E` en hexadecimal. Convertir `C8` (hex) = `200` decimal = `11001000` binario explica el verde. Lo mismo aplica a números: `FF` hex = `255` decimal = `11111111` binario; y `FFFFFF` = 16.777.215 ≈ **17 millones** (de ahí los "millones de colores" de las pantallas modernas). Convertir mentalmente hex↔decimal↔binario es una skill esencial para CTF y análisis de memoria.
> **EN:** A computer only manipulates bits. Colour is represented with 3 RGB bytes (Red, Green, Blue): `#3BC81E` means red `3B`, green `C8`, blue `1E` in hexadecimal. Converting `C8` (hex) = `200` decimal = `11001000` binary explains the green. Same applies to numbers: `FF` hex = `255` decimal = `11111111` binary; `FFFFFF` = 16,777,215 ≈ **17 million** (hence "millions of colours" on modern displays). Fluently converting hex↔decimal↔binary is a core CTF and memory-analysis skill.

### Task 1 — Introducción / Introduction

* **Check:** `It is time to dive into computer colors!`
* **ES:** Fundamentos de la representación de datos en el ordenador (parte de Pre Security).
* **EN:** Data-representation fundamentals (part of Pre Security).

### Task 2 — Representando Colores / Representing Colors *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Preview the color `#3BC81E`. In one word, what does this color appear to be? | `green` |
| What is the binary representation of the color `#EB0037`? | `11101011 00000000 00110111` |
| What is the decimal representation of the color `#D4D8DF`? | `212 216 223` |

* **Método / Method:** el simulador visual de color te da el hex y calcula el valor de cada canal.
* **`#EB0037`:** `EB`=`11101011`, `00`=`00000000`, `37`=`00110111` → les alcanza con 8 bits por canal.
* **`#D4D8DF`:** `D4`=`212`, `D8`=`216`, `DF`=`223` (D=13→13·16=208+4=212; D8=13·16+8=216; DF=13·16+15=223).

### Task 3 — Números: De Decimal a Hexadecimal / Numbers: From Decimal to Hexadecimal *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the hexadecimal `FF` in binary? | `11111111` |
| What is the hexadecimal `AB` in decimal? | `171` |
| Convert the hexadecimal `FF FF FF` to decimal. After you round up the decimal value to the nearest million, **how many millions is that**? | `17` |

* **`FF` binario:** F=`1111` → `FF`=`11111111`.
* **`AB` decimal:** A=`10`, B=`11` → `10·16 + 11` = `171`.
* **`FFFFFF` decimal:** `255·65536 + 255·256 + 255` = `16.777.215`; redondeado al millón más cercano → **17 millones** (respuesta: `17`).

### Task 4 — Conclusión / Conclusion

* **Check:** `It is time to join the Data Encoding room and dive deeper into bits.`
* **ES:** Cierra el bloque de numeración; el siguiente paso es cómo los ordenadores codifican caracteres (Data Encoding).
* **EN:** Wraps up number systems; the next step is how computers encode characters (Data Encoding).

## Metodología / Methodology

1. **Paso / Step:** Usar el convertidor del room (estático) o cálculo mental: hex→bin (cada dígito = 4 bits), hex→dec (`d·16^1 + u`), bin→dec.
2. **Paso / Step:** En colores, dividir el 6 dígitos en 3 pares (R, G, B) y convertir cada par.
3. **Paso / Step:** Para `FFFFFF` hacer el cálculo de los 3 bytes y redondear a millones.

### Cadena de aprendizaje / Learning Chain

```
bit / byte
  -> sistema decimal (base 10)
  -> sistema binario (base 2)  [FF = 11111111]
  -> sistema hexadecimal (base 16) [AB = 171]
  -> colores RGB = 3 bytes  [#FFFFFF ≈ 17 millones de colores]
```

**Mapeo MITRE ATT&CK / relacionado:** ninguno directo; es material de base para técnicas de encoding posterior (p. ej. entender payloads maliciosos "encodificados" en hex/bin en análisis de malware y análisis de memoria).

**Lección:** *Todo es números.* Antes de hablar de enfcriptar, exfiltrar o analizar un dump de memoria, hay que leer binario/hex/decimal.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.