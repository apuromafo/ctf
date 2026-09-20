# Break it
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `breakit` |
| **Link** | [TryHackMe](https://tryhackme.com/room/breakit) |
| **Sección** | Cryptography / Steganography |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | Base encoding, Vigenère cipher, ROT ciphers, cryptographic analysis |
| **Impacto** | Enseña a descifrar múltiples capas de codificación (base16/32/64, Vigenère, ROT) para recuperar texto plano de cadenas ofuscadas. |
---
**Contexto:** Break it es una sala de TryHackMe dedicada a la criptografía y el análisis de codificaciones. El participante debe descifrar cadenas que emplean diferentes técnicas de codificación (bases múltiples, cifrado Vigenère y ROT) para obtener las flags de cada task.
*EN: Break it is a TryHackMe room dedicated to cryptography and encoding analysis. The participant must decrypt strings using multiple encoding techniques (multiple bases, Vigenère cipher, and ROT) to obtain the flags for each task.*
## Solucionario
### Task 1 — Base Encoding
**Explicación:** Se decodifican cadenas codificadas en múltiples formatos de base (base16/hex, base32, base64 y combinaciones). Cada cadena requiere identificar el tipo de codificación y aplicar la decodificación correspondiente.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag for easy_base32? | `easy_base32` |
| 2 | What is the flag for double_bases? | `double_bases` |
| 3 | What is the flag for base16_is_hex? | `base16_is_hex` |
| 4 | What is the flag for that_is_a_lot_of_bases? | `that_is_a_lot_of_bases` |
| 5 | What is the flag for defense_the_base? | `defense_the_base` |
### Task 2 — Classical Ciphers
**Explicación:** Se aplican técnicas de criptografía clásica: manipulación de caracteres (hacer girar letras), cifrado Vigenère y combinaciones de decodificación con ROT. Cada reto requiere identificar el cifrado correcto y aplicar la operación inversa.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag for make_13_spin? | `make_13_spin` |
| 2 | What is the flag for I luv vigenere cipher? | `I luv vigenere cipher` |
| 3 | What is the flag for decode_and_rot? | `decode_and_rot` |
| 4 | What is the flag for you are a real code cracker? | `you are a real code cracker` |
### Task 3 — Advanced Cryptanalysis
**Explicación:** Se aplica análisis de desplazamiento (shift) lógico y aritmético para descifrar cadenas que combinan múltiples técnicas de transformación.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag for shift logic like a boss? | `shift logic like a boss` |
| 2 | What is the flag for shift arithmetic like a boss? | `shift arithmetic like a boss` |
| 3 | What is the flag for God of shifs? | `God of shifs` |
---
**Metodología:** Identificación de tipo de codificación → decodificación por capas (hex → base32 → base64) → análisis de cifrado clásico (Vigenère, ROT13) → decodificación secuencial → flags.
**Learning chain:** cadenas codificadas → identificar formato → decodificar → cifrado clásico → clave → texto plano → flags.
**Lección:** *La mayoría de "cifrados" en CTF son codificaciones, no cifrados reales: probar bases (16/32/64), ROT y Vigenère en secuencia resuelve casi todo.*
**MITRE ATT&CK:** T1027 (Obfuscated Files or Information), T1140 (Deobfuscate/Decode Files or Information).
**Fuente:** [TryHackMe - Break it](https://tryhackme.com/room/breakit)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
