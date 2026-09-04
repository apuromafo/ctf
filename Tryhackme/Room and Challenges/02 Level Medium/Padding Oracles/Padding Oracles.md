# Padding Oracles [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `paddingoracles`
* **Link:** https://tryhackme.com/room/paddingoracles
* **Sección / Section:** Crypto / Web
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Estudio y explotación de ataques de padding oracle sobre cifrado por bloques en modo CBC, cubriendo conceptos de padding, descifrado manual y automatizado, y la fórmula base del ataque.
> **EN:** Study and exploitation of padding oracle attacks on block cipher encryption in CBC mode, covering padding concepts, manual and automated decryption, and the fundamental formula of the attack.

---

### Task 1 — Fundamentos de Padding y Cifrado

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In cryptography, extra bytes are added to fill the remaining space in the last block during encryption, or decryption is called? | `Padding` |
| What is the byte value padded after padding the term HelloWorld? | `06` |
| The encryption mode in which each plaintext block is XORed with the previous ciphertext block before being encrypted is called? | `Cipher Block Chaining` |
| What is the last byte after encrypting the word Hacker using the secret MyActualSecrets1? | `54` |

---

### Task 2 — Descifrado y Ataques de Padding Oracle

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the plaintext after decrypting b1e090de4abbc8b54769ba79a98a4cffaf59a89e58bcc474794d1e8b7e5315b2 using the secret key abcdefghijklmnop? | `THM{Encryption_007}` |
| What should the IV size be in bytes if you try decrypting a string using AES (16-byte block size)? | `16` |
| What is the flag value after decrypting the ciphertext? | `THM-{brUt3-f0rC3}` |
| While performing a padding oracle attack, what is the expected value for the last plaintext byte if you only modify the 16th byte of the modified IV? Use notations like 01, 02, 03, etc. only. | `01` |
| The foundation of the padding oracle lies in the formula Pi = Dk(Ci) {OPERATOR} Ci−1. What is the missing operator in the formula? | `XOR` |

---

### Task 3 — Identificación y Prevención

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the status code shown on the page when an "Invalid padding" error occurs? | `400` |
| What is the decrypted value (ASCII) for the ciphertext 31323334353637383930313233343536bdcc4a2319946dc9b30203d89dba9fce with a block size of 16? | `Got_The_Flag007` |
| Is it a good practice to display padding errors on the production server (yea/nay)? | `nay` |

---

## Metodología / Methodology

1. **Paso / Step:** Comprender el concepto de padding en cifrado por bloques y el modo CBC / Understand the concept of padding in block cipher encryption and CBC mode.
2. **Paso / Step:** Practicar el cálculo de valores de padding y bytes de cifrado con secretos conocidos / Practice calculating padding values and cipher bytes with known secrets.
3. **Paso / Step:** Aplicar las fórmulas de descifrado (Pi = Dk(Ci) XOR Ci-1) para obtener texto plano / Apply decryption formulas (Pi = Dk(Ci) XOR Ci-1) to obtain plaintext.
4. **Paso / Step:** Ejecutar ataques de padding oracle manipulando el IV y observando las respuestas del servidor / Execute padding oracle attacks by manipulating the IV and observing server responses.
5. **Paso / Step:** Interpretar los códigos de estado (400 para padding inválido) como oráculo de validación / Interpret status codes (400 for invalid padding) as validation oracle.

### Cadena de ataque / Attack Chain

```
Entender padding y modo CBC
  -> Practicar cálculos manuales de cifrado/descifrado
    -> Identificar el oráculo de validación (status code 400 para padding inválido)
      -> Manipular el IV byte a byte
        -> Verificar padding válido (01, 02, 03...) para cada byte
          -> Recuperar texto plano byte a byte:
              THM{Encryption_007}
              THM-{brUt3-f0rC3}
              Got_The_Flag007
            -> Conclusión: no exponer errores de padding en producción
```

**Lección:** Un padding oracle convierte un servidor en una máquina de descifrado. Nunca se deben mostrar errores de padding detallados en producción, y se debe utilizar cifrado autenticado (AEAD) para evitar este tipo de ataques.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
