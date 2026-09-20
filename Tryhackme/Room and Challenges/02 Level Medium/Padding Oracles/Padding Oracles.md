# Padding Oracles

| **Dificultad** | MEDIUM | **Tipo** | Walkthrough (Free) | **Slug** | `paddingoracles` |
| **Link** | [TryHackMe](https://tryhackme.com/room/paddingoracles) | **Sección** | Crypto / Web | **Fuente** | Writeup de thmrevenant (GitHub) |
| **Componentes** | Criptografía, Cifrado por bloques CBC, PKCS#7 Padding, Ataques de Padding Oracle, AES, Descifrado manual y automatizado | **Impacto** | Descifrado completo de datos cifrados por bloques (modo CBC) sin conocer la clave, convirtiendo al servidor en un oráculo de descifrado |

---

**Contexto:** Esta sala estudia y explota los ataques de padding oracle sobre cifrado por bloques en modo CBC. Cubre conceptos de padding (PKCS#7), el cálculo de bytes de padding y cifrado con secretos conocidos, la fórmula fundamental de descifrado Pi = Dk(Ci) XOR Ci-1, y el descifrado manual y automatizado mediante la manipulación del IV y las respuestas del servidor. Finaliza con la identificación del oráculo (código de estado 400) y las medidas de prevención.

> **ES:** Estudio y explotación de ataques de padding oracle sobre cifrado por bloques en modo CBC, cubriendo conceptos de padding, descifrado manual y automatizado, y la fórmula base del ataque.
> **EN:** Study and exploitation of padding oracle attacks on block cipher encryption in CBC mode, covering padding concepts, manual and automated decryption, and the fundamental formula of the attack.

## Solucionario

### Task 1: Fundamentos de Padding y Cifrado / Padding and Encryption Fundamentals

**Explicación:** En criptografía, los bytes extra que se añaden para rellenar el espacio restante en el último bloque durante el cifrado o descifrado se llaman Padding. Al rellenar el término HelloWorld, el byte de padding aplicado es 06. El modo de cifrado en el que cada bloque de texto plano se hace XOR con el bloque de cifrado anterior antes de cifrarse es Cipher Block Chaining. Tras cifrar la palabra Hacker con el secreto MyActualSecrets1, el último byte es 54.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In cryptography, extra bytes are added to fill the remaining space in the last block during encryption, or decryption is called? | `Padding` |
| What is the byte value padded after padding the term HelloWorld? | `06` |
| The encryption mode in which each plaintext block is XORed with the previous ciphertext block before being encrypted is called? | `Cipher Block Chaining` |
| What is the last byte after encrypting the word Hacker using the secret MyActualSecrets1? | `54` |

### Task 2: Descifrado y Ataques de Padding Oracle / Decryption and Padding Oracle Attacks

**Explicación:** Se descifra el texto cifrado b1e090de4abbc8b54769ba79a98a4cffaf59a89e58bcc474794d1e8b7e5315b2 con la clave abcdefghijklmnop, obteniendo el texto plano THM{Encryption_007}. El IV debe ser de 16 bytes si se descifra con AES (tamaño de bloque 16). Al descifrar el ciphertext se obtiene la flag THM-{brUt3-f0rC3}. Durante un ataque de padding oracle, al modificar solo el byte 16 del IV modificado, el valor esperado para el último byte del texto plano es 01. La fórmula que fundamenta el ataque es Pi = Dk(Ci) XOR Ci-1, siendo el operador faltante XOR.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the plaintext after decrypting b1e090de4abbc8b54769ba79a98a4cffaf59a89e58bcc474794d1e8b7e5315b2 using the secret key abcdefghijklmnop? | `THM{Encryption_007}` |
| What should the IV size be in bytes if you try decrypting a string using AES (16-byte block size)? | `16` |
| What is the flag value after decrypting the ciphertext? | `THM-{brUt3-f0rC3}` |
| While performing a padding oracle attack, what is the expected value for the last plaintext byte if you only modify the 16th byte of the modified IV? Use notations like 01, 02, 03, etc. only. | `01` |
| The foundation of the padding oracle lies in the formula Pi = Dk(Ci) {OPERATOR} Ci−1. What is the missing operator in the formula? | `XOR` |

### Task 3: Identificación y Prevención / Identification and Prevention

**Explicación:** El código de estado mostrado en la página cuando ocurre un error de "Invalid padding" es 400. Al descifrar el ciphertext 31323334353637383930313233343536bdcc4a2319946dc9b30203d89dba9fce con tamaño de bloque 16 se obtiene el valor ASCII Got_The_Flag007. No es una buena práctica mostrar errores de padding en el servidor de producción (`nay`).

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the status code shown on the page when an "Invalid padding" error occurs? | `400` |
| What is the decrypted value (ASCII) for the ciphertext 31323334353637383930313233343536bdcc4a2319946dc9b30203d89dba9fce with a block size of 16? | `Got_The_Flag007` |
| Is it a good practice to display padding errors on the production server (yea/nay)? | `nay` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | In cryptography, extra bytes are added to fill the remaining space in the last block during encryption, or decryption is called? | `Padding` |
| 1.2 | What is the byte value padded after padding the term HelloWorld? | `06` |
| 1.3 | The encryption mode in which each plaintext block is XORed with the previous ciphertext block before being encrypted is called? | `Cipher Block Chaining` |
| 1.4 | What is the last byte after encrypting the word Hacker using the secret MyActualSecrets1? | `54` |
| 2.1 | What is the plaintext after decrypting b1e090de4abbc8b54769ba79a98a4cffaf59a89e58bcc474794d1e8b7e5315b2 using the secret key abcdefghijklmnop? | `THM{Encryption_007}` |
| 2.2 | What should the IV size be in bytes if you try decrypting a string using AES (16-byte block size)? | `16` |
| 2.3 | What is the flag value after decrypting the ciphertext? | `THM-{brUt3-f0rC3}` |
| 2.4 | While performing a padding oracle attack, what is the expected value for the last plaintext byte if you only modify the 16th byte of the modified IV? Use notations like 01, 02, 03, etc. only. | `01` |
| 2.5 | The foundation of the padding oracle lies in the formula Pi = Dk(Ci) {OPERATOR} Ci−1. What is the missing operator in the formula? | `XOR` |
| 3.1 | What is the status code shown on the page when an "Invalid padding" error occurs? | `400` |
| 3.2 | What is the decrypted value (ASCII) for the ciphertext 31323334353637383930313233343536bdcc4a2319946dc9b30203d89dba9fce with a block size of 16? | `Got_The_Flag007` |
| 3.3 | Is it a good practice to display padding errors on the production server (yea/nay)? | `nay` |

---

**Metodología:**

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

**Learning chain:** Conceptos de padding y modo CBC → Cálculos manuales con secretos conocidos → Fórmula de descifrado Pi = Dk(Ci) XOR Ci-1 → Identificación del oráculo (código 400) → Manipulación del IV byte a byte → Recuperación del texto plano (THM{Encryption_007}, THM-{brUt3-f0rC3}, Got_The_Flag007) → Prevención con cifrado autenticado.

**Lección:** *Un padding oracle convierte un servidor en una máquina de descifrado. Nunca se deben mostrar errores de padding detallados en producción, y se debe utilizar cifrado autenticado (AEAD) para evitar este tipo de ataques.*

**MITRE ATT&CK:** T1557.001 (Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay), T1040 (Network Sniffing), T1656 (Impersonation)

**Fuente:** [TryHackMe - Padding Oracles](https://tryhackme.com/room/paddingoracles)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.