# Attacking ECB Oracles

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto • Criptografía | attackingecboracles | https://tryhackme.com/room/attackingecboracles | 03 Level Hard | TryHackMe | AES-ECB, Padding Oracle, Bloques, Difusión | Alto |

---

**Contexto:**
> **ES:** Laboratorio de criptografía orientado a explotar oráculos basados en AES en modo ECB: historia del algoritmo, padding, difusión, size de bloque y offset para romper el cifrado por bloques.
> **EN:** Cryptography lab focused on exploiting AES-ECB-based oracles: algorithm history, padding, diffusion, block size and offset to break block ciphers.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**
1. No answer needed

### Task 2: Historia del algoritmo / Algorithm history
**Explicación:**
1. 1997
2. Rijndael Cipher
3. Symmetric

### Task 3: Padding Oracle / Padding Oracle
**Explicación:**
1. padding
2. c35a97106295a3101b6be8a9af954d198462b30f0af7f669d46766cbeea7eabf

### Task 4: Difusión y análisis / Diffusion and analysis
**Explicación:**
1. diffusion
2. images

### Task 5: Tamaño y offset de bloque / Block size and offset
**Explicación:**
1. Block Size
2. Offset
3. O
4. OracleKnows

### Task 6: Laboratorio / Lab
**Explicación:**
1. No answer needed

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |
| 2.1 | `1997` |
| 2.2 | `Rijndael Cipher` |
| 2.3 | `Symmetric` |
| 3.1 | `padding` |
| 3.2 | `c35a97106295a3101b6be8a9af954d198462b30f0af7f669d46766cbeea7eabf` |
| 4.1 | `diffusion` |
| 4.2 | `images` |
| 5.1 | `Block Size` |
| 5.2 | `Offset` |
| 5.3 | `O` |
| 5.4 | `OracleKnows` |
| 6 | `No answer needed` |

---

**Metodología:**
Estudio del cifrado por bloques AES en modo ECB: elección del algoritmo (Rijndael), efecto del padding, propiedades de difusión, determinación del tamaño de bloque y del offset para interactuar con el oráculo.

### Cadena de ataque / Attack Chain
1. Identificación del cifrado de bloque en modo ECB.
2. Corrección del padding y observación del oráculo.
3. Medición del tamaño de bloque y del offset.
4. Recuperación incremental de los bytes secretos consultando el oráculo.
5. Obtención del texto plano completo.

**Learning chain:**
Bloques -> Padding -> Difusión -> Offset -> Oráculo -> Recuperación del secreto.

**Lección:** *AES-ECB filtra información por su estructura de bloques; un oráculo de padding convierte esa debilidad en una extracción byte a byte.*

**MITRE ATT&CK:**
- No aplica (debilidad criptográfica AES-ECB / oráculo de padding — CWE-327).

**Fuente:** [TryHackMe - Attacking ECB Oracles](https://tryhackme.com/room/attackingecboracles)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.