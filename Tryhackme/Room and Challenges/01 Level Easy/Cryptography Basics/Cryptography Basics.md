# Cryptography Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Cryptography / Theory | `cryptographybasics` | https://tryhackme.com/room/cryptographybasics | 01 Level Easy | TryHackMe | Criptografía / PCI DSS / Caesar Cipher / DES / AES / XOR / módulo (%) / cifrado simétrico y asimétrico | Aprender los conceptos clave de criptografía (plaintext, ciphertext, cifrado/descifrado), estándares (PCI DSS), criptografía histórica (César), cifradores simétricos (AES) y bases matemáticas (XOR, módulo). |

---

**Contexto:** Sala introductoria de criptografía que parte de los términos esenciales (texto plano, texto cifrado, cifrado y descifrado), el estándar PCI DSS para datos de tarjetas, el cifrado de César y los principales algoritmos (DES vs AES), y termina con operaciones matemáticas básicas (XOR y módulo) usadas en criptografía.

> **ES:** "Aprende los conceptos básicos de criptografía y cifrado simétrico: términos clave, cifrado de César, DES/AES y matemáticas básicas."
> **EN:** "Learn the basics of cryptography and symmetric encryption: key terms, Caesar cipher, DES/AES and basic math."

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se presenta la sala y sus objetivos de aprendizaje. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Estoy listo para empezar a aprender sobre criptografía. / I'm ready to start learning about cryptography! | `No answer needed` |

---

### Task 2: Importancia de la criptografía / Importance of Cryptography

**Explicación:** Una empresa que maneja datos de tarjetas de crédito debe cumplir el Payment Card Industry Data Security Standard (PCI DSS), que obliga a cifrar los datos tanto en reposo como en tránsito.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el estándar requerido para manejar información de tarjetas de crédito? / What is the standard required for handling credit card information? | `PCI DSS` |

---

### Task 3: De texto plano a texto cifrado / Plaintext to Ciphertext

**Explicación:** El texto cifrado es el resultado de cifrar el plaintext (texto cifrado = encrypted plaintext), y el proceso que devuelve el plaintext original se denomina descifrado (decryption).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el plaintext que ya ha sido cifrado? / What do you call the encrypted plaintext? | `ciphertext` |
| 2 | ¿Cómo se llama el proceso que devuelve el plaintext? / What do you call the process that returns the plaintext? | `decryption` |

---

### Task 4: Cifrados históricos / Historical Ciphers

**Explicación:** El cifrado de César desplaza cada letra un número fijo de posiciones. Si `XRPCTCRGNEI` fue cifrado con César, desplazando hacia atrás se recupera el plaintext `ICANENCRYPT`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sabiendo que `XRPCTCRGNEI` se cifró con el cifrado de César, ¿cuál es el plaintext original? / Knowing that `XRPCTCRGNEI` was encrypted using Caesar Cipher, what is the original plaintext? | `ICANENCRYPT` |

---

### Task 5: Tipos de cifrado / Types of Encryption

**Explicación:** DES dejó de considerarse seguro (es sustituido por 3DES y luego por AES); AES fue adoptado como estándar en 2001 con tamaños de clave de 128, 192 o 256 bits. Por tanto, no hay que confiar en DES.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Deberías confiar en DES? (Sí/No) / Should you trust DES? (Yea/Nay) | `Nay` |
| 2 | ¿Cuándo fue adoptado AES como estándar de cifrado? / When was AES adopted as an encryption standard? | `2001` |

---

### Task 6: Matemáticas básicas / Basic Math

**Explicación:** Operaciones básicas con XOR (⊕) y módulo (%): `1001 ⊕ 1010` es un XOR bit a bit que da `0011`; `118613842 % 9091` da como resto `3565`; y `60 % 12` da resto `0`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuánto es 1001 ⊕ 1010? / What's 1001 ⊕ 1010? | `0011` |
| 2 | ¿Cuánto es 118613842 % 9091? / What's 118613842 % 9091? | `3565` |
| 3 | ¿Cuánto es 60 % 12? / What's 60 % 12? | `0` |

---

### Task 7: Resumen / Summary

**Explicación:** Antes de pasar a la siguiente sala hay que tener anotados todos los términos y conceptos clave presentados. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He anotado todos los términos y conceptos clave de la sala. / I've taken note of all the key terms and concepts introduced in this room. | `No answer needed` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | Introducción. / Introduction. | `No answer needed` |
| 2 | Task 2 | ¿Cuál es el estándar para datos de tarjetas? / What is the standard for credit card data? | `PCI DSS` |
| 3 | Task 3 | ¿Cómo se llama el plaintext cifrado? / What do you call the encrypted plaintext? | `ciphertext` |
| 4 | Task 3 | ¿Cómo se llama el proceso que devuelve el plaintext? / What process returns the plaintext? | `decryption` |
| 5 | Task 4 | Plaintext de `XRPCTCRGNEI` con César. / Plaintext of `XRPCTCRGNEI` with Caesar. | `ICANENCRYPT` |
| 6 | Task 5 | ¿Deberías confiar en DES? / Should you trust DES? | `Nay` |
| 7 | Task 5 | ¿Cuándo se adoptó AES? / When was AES adopted? | `2001` |
| 8 | Task 6 | 1001 ⊕ 1010 | `0011` |
| 9 | Task 6 | 118613842 % 9091 | `3565` |
| 10 | Task 6 | 60 % 12 | `0` |
| 11 | Task 7 | Resumen. / Summary. | `No answer needed` |

---

**Metodología:** Leer la teoría de cada sección -> responder con los términos definidos (ciphertext/decryption) -> aplicar el desplazamiento de César sobre `XRPCTCRGNEI` -> memorizar las fechas y estándares (PCI DSS, AES 2001, DES no confiable) -> resolver XOR y operaciones módulo.

### Cadena de ataque / Attack Chain

```text
Conceptos clave (plaintext/ciphertext) -> PCI DSS -> Caesar (XRPCTCRGNEI -> ICANENCRYPT) -> DES vs AES (2001) -> XOR (1001⊕1010=0011) -> módulo (3565, 0)
```

**Learning chain:** plaintext/ciphertext -> encryption/decryption -> PCI DSS -> Caesar Cipher -> DES/AES -> XOR -> módulo.

**Lección:** *La criptografía se apoya en pocos conceptos muy claros (cifrado/descifrado, simétrico/asimétrico) y unas pocas operaciones matemáticas; dominarlos hace que cualquier algoritmo posterior sea comprensible.*

**MITRE ATT&CK:** N/A (sala teórica de criptografía)

**Fuente:** [TryHackMe - Cryptography Basics](https://tryhackme.com/room/cryptographybasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.