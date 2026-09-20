# Cryptography for Dummies

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | Cryptography / Theory | `cryptographyfordummies` | https://tryhackme.com/room/cryptographyfordummies | 01 Level Easy | TryHackMe | Criptografía simétrica y asimétrica / claves pública y privada / MD5 / hash / Base64 / encoding | Entender los tipos de criptografía (simétrica vs asimétrica), las claves pública y privada, qué es un hash (MD5) y las diferencias entre codificación y cifrado. |

---

**Contexto:** Sala fundamental de criptografía ("para dummies") que distingue cifrado simétrico y asimétrico y explica el papel de la clave pública y la clave privada. Después introduce los hashes (MD5: qué significa y quién lo creó) y aterriza el concepto de codificación con ejemplos en Base64.

> **ES:** "Cubre los conceptos básicos de criptografía: tipos (simétrico/asimétrico), hashes y codificación Base64, para dar una base sólida sobre cómo se usa en internet."
> **EN:** "We are going to cover the basics, to give you a basic understanding. It is used by a wide range of applications, almost everywhere in the internet."

## Solucionario

### Task 1: Intro / Intro

**Explicación:** Se presenta la sala: entender por qué la criptografía es importante y qué se va a aprender. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Entiendo por qué la criptografía es importante. / I understand why cryptography is important! | `No answer needed` |

---

### Task 2: Tipos de criptografía / Types of cryptography

**Explicación:** La criptografía se divide en simétrica (una sola clave, más rápida) y asimétrica (par de claves: pública para cifrar y privada para descifrar, más segura pero más lenta). La asimétrica es más segura, y nunca se debe cifrar un mensaje confiando solo en simétrica para intercambio de claves.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de criptografía es más segura? / What type of cryptography is more secure? | `asymmetric` |
| 2 | ¿Qué tipo de criptografía es más rápida? / What type of cryptography is faster? | `symmetric` |
| 3 | ¿Qué tipo de criptografía es más lenta pero más segura? / What type of cryptography is slower but more secure? | `asymmetric` |
| 4 | ¿Cómo se llama la clave que se usa para cifrar? / What is the key used for encryption called? | `public key` |
| 5 | ¿Cómo se llama la clave que se usa para descifrar? / What is the key used for decryption called? | `private key` |
| 6 | ¿Deberías usar solo un algoritmo simétrico para cifrar mensajes? (Yea/Nay) / Should you use a symmetric algorithm to encrypt messages? (Yea/Nay) | `nay` |

---

### Task 3: Hashing

**Explicación:** Un hash es una huella digital de longitud fija de un dato. Se calcula el hash MD5 del texto del ejercicio (resultado `f762d32e3c160900d94b683e927555b9`), MD5 significa Message Digest 5 y fue diseñado por Ronald Rivest.

```bash
echo -n "<cadena del ejercicio>" | md5sum
# f762d32e3c160900d94b683e927555b9
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Calcula el hash MD5 del texto indicado en el ejercicio. / Compute the MD5 hash of the string given in the exercise. | `No answer needed` |
| 2 | ¿Cuál es el hash MD5 obtenido? / What is the MD5 hash obtained? | `f762d32e3c160900d94b683e927555b9` |
| 3 | ¿Qué significan las siglas MD5? / What does MD5 stand for? | `Message Digest 5` |
| 4 | ¿Quién desarrolló MD5? / Who developed MD5? | `Ronald Rivest` |

---

### Task 4: Codificación / Encoding

**Explicación:** Base64 es una codificación, no un cifrado. Se codifica la cadena `cryptographyisuseful` y se nos pide descifrar (decodificar) `dGhlIHNlY3JldCB3b3JkIGlzIDogd2F0ZXJtZWxvbg==`, que revela "the secret word is : watermelon", es decir, la palabra secreta `watermelon`.

```bash
echo -n "cryptographyisuseful" | base64          # Y3J5cHRvZ3JhcGh5aXN1c2VmdWw=
echo "dGhlIHNlY3JldCB3b3JkIGlzIDogd2F0ZXJtZWxvbg==" | base64 -d
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Codifica la cadena `cryptographyisuseful` con Base64. / Encode the string `cryptographyisuseful` with Base64. | `Y3J5cHRvZ3JhcGh5aXN1c2VmdWw=` |
| 2 | Decodifica `dGhlIHNlY3JldCB3b3JkIGlzIDogd2F0ZXJtZWxvbg==`. ¿Cuál es la palabra secreta? / Decode the string `dGhlIHNlY3JldCB3b3JkIGlzIDogd2F0ZXJtZWxvbg==`. What's the secret word? | `watermelon` |

---

### Task 5: Fin / Thanks for reading

**Explicación:** Cierre de la sala con un resumen de los conceptos vistos. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Gracias por leer, ¡saludos y buen hacking! / Thanks for reading, cheers and happy hacking! | `No answer needed` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | Intro. / Intro. | `No answer needed` |
| 2 | Task 2 | ¿Qué tipo de criptografía es más segura? / What type of cryptography is more secure? | `asymmetric` |
| 3 | Task 2 | ¿Qué tipo es más rápido? / What type is faster? | `symmetric` |
| 4 | Task 2 | ¿Qué tipo es más lento pero más seguro? / What type is slower but more secure? | `asymmetric` |
| 5 | Task 2 | Clave de cifrado. / Encryption key. | `public key` |
| 6 | Task 2 | Clave de descifrado. / Decryption key. | `private key` |
| 7 | Task 2 | ¿Cifrar solo con simétrico? (Yea/Nay) / Symmetric only? (Yea/Nay) | `nay` |
| 8 | Task 3 | Calcula el hash. / Compute the hash. | `No answer needed` |
| 9 | Task 3 | Hash MD5 del ejercicio. / MD5 hash of the exercise. | `f762d32e3c160900d94b683e927555b9` |
| 10 | Task 3 | ¿Qué significa MD5? / What does MD5 stand for? | `Message Digest 5` |
| 11 | Task 3 | ¿Quién desarrolló MD5? / Who developed MD5? | `Ronald Rivest` |
| 12 | Task 4 | Codifica `cryptographyisuseful` en Base64. / Encode `cryptographyisuseful` with Base64. | `Y3J5cHRvZ3JhcGh5aXN1c2VmdWw=` |
| 13 | Task 4 | Palabra secreta de la cadena Base64. / Secret word of the Base64 string. | `watermelon` |
| 14 | Task 5 | Fin. / Thanks for reading. | `No answer needed` |

---

**Metodología:** Comparar simétrica vs asimétrica conceptos teóricos -> identificar clave pública/privada -> calcular el hash MD5 del texto del ejercicio con `md5sum` -> aplicar Base64 con el comando `base64` tanto para codificar como para decodificar -> responder con los valores exactos obtenidos.

### Cadena de ataque / Attack Chain

```text
Conceptos (simétrica/asimétrica) -> claves pública y privada -> MD5 (f762d32e3c160900d94b683e927555b9) -> Message Digest 5 / Ronald Rivest -> base64 encode (Y3J5cHRvZ3JhcGh5aXN1c2VmdWw=) -> base64 decode (watermelon)
```

**Learning chain:** symmetric/asymmetric -> public/private key -> hashing (MD5) -> encoding (Base64) -> decode.

**Lección:** *La criptografía asimétrica es más segura pero más lenta; el hash no es reversible y la codificación (Base64) no es cifrado: conocer estas diferencias evita malentendidos básicos de seguridad.*

**MITRE ATT&CK:** N/A (sala teórica de criptografía)

**Fuente:** [TryHackMe - Cryptography for Dummies](https://tryhackme.com/room/cryptographyfordummies)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.