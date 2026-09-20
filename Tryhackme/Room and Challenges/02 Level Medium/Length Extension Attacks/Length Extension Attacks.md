# Length Extension Attacks

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough (Premium) | lengthextensionattacks | https://tryhackme.com/room/lengthextensionattacks | Crypto / Web | Writeup de thmrevenant (GitHub) | SHA-256, Merkle-Damgard, Padding, HMAC, MAC forjado | Forja de firmas/mensajes en MAC basados en secret\|\|message |

---

**Contexto:** La sala explora los **ataques de extensión de longitud** (length extension attacks) sobre hash basados en la construcción Merkle-Damgard como **SHA-256**. Se cubren las propiedades criptográficas de los hash (resistencia a preimagen y a colisiones), la estructura interna del algoritmo (bloque de 512 bits, función de padding, estado interno de 8 palabras) y cómo abusar del padding para extender mensajes firmados sin conocer la clave secreta. La resolución parte de la teoría y termina forjando un mensaje/sesión administrativa.

> **ES:** Esta sala explora los ataques de extensión de longitud (length extension attacks) sobre hash basados en Merkle-Damgard como SHA-256. Cubre propiedades criptográficas, la estructura interna del algoritmo y cómo abusar del padding para extender mensajes firmados sin conocer la clave secreta.
> **EN:** This room explores length extension attacks on Merkle-Damgard based hashes like SHA-256. It covers cryptographic properties, the algorithm's internal structure and how to abuse padding to extend signed messages without knowing the secret key.

## Solucionario

### Task 1: Propiedades Criptográficas / Cryptographic Properties
**Explicación:**

Se repasan las propiedades fundamentales de las funciones hash: la que impide invertir el hash para recuperar la entrada original y la que garantiza que dos mensajes distintos no produzcan el mismo hash.

| Pregunta | Respuesta |
|----------|-----------|
| What property prevents an attacker from reversing a hash to get the original input? | `Pre-image Resistance` |
| What property ensures that no two different messages produce the same hash? | `Collision Resistance` |

### Task 2: Estructura Interna de SHA-256 / SHA-256 Internals
**Explicación:**

Se analiza la construcción interna de SHA-256: el tamaño de bloque que procesa, la función de relleno (padding) que alinea los datos al tamaño de bloque y el número de palabras que componen su estado interno.

| Pregunta | Respuesta |
|----------|-----------|
| What block size does SHA-256 use? | `512` |
| What function ensures data is aligned to fit block size requirements? | `Padding` |
| How many words does SHA-256's internal state have? | `8` |

### Task 3: Mitigación y Explotación / Mitigation & Exploitation
**Explicación:**

Se identifica qué construcción previene los ataques de extensión de longitud (**HMAC**) y se explota la vulnerabilidad añadiendo padding y datos extra a un mensaje firmado con `secret||message` para forjar un mensaje extendido sin conocer la clave. Se capturan las dos flags del reto (una oculta en una imagen y la final del panel de administración).

| Pregunta | Respuesta |
|----------|-----------|
| What hashing method prevents length extension attacks by using a secret key? | `HMAC` |
| What is the flag in the image? | `THM{L3n6th_3Xt33ns10nssss}` |
| What is the flag? | `THM{l3n6th_2_4dM1n}` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What property prevents an attacker from reversing a hash to get the original input? | `Pre-image Resistance` |
| 1 | What property ensures that no two different messages produce the same hash? | `Collision Resistance` |
| 2 | What block size does SHA-256 use? | `512` |
| 2 | What function ensures data is aligned to fit block size requirements? | `Padding` |
| 2 | How many words does SHA-256's internal state have? | `8` |
| 3 | What hashing method prevents length extension attacks by using a secret key? | `HMAC` |
| 3 | What is the flag in the image? | `THM{L3n6th_3Xt33ns10nssss}` |
| 3 | What is the flag? | `THM{l3n6th_2_4dM1n}` |

---

**Metodología:**

1. **Paso 1:** Se comprenden las propiedades criptográficas de las funciones hash: resistencia a preimagen y resistencia a colisiones.
2. **Paso 2:** Se analiza la estructura interna de SHA-256: tamaño de bloque de 512 bits, la función de relleno (padding) que alinea los datos y el estado interno de 8 palabras.
3. **Paso 3:** Se aprende que HMAC previene los ataques de extensión de longitud, y se explota la vulnerabilidad añadiendo padding y datos extra a un mensaje firmado para obtener acceso administrativo sin conocer la clave secreta.

### Cadena de ataque / Attack Chain

```
Comprensión de propiedades hash → Análisis de estructura SHA-256 (bloque 512, padding, estado 8 palabras) → Identificación de hash vulnerable a extensión de longitud → Añadido de padding + datos malignos → Forja de firma/mensaje extendido → Acceso administrativo no autorizado
```

**Learning chain:** Comprensión de propiedades hash → Análisis de estructura SHA-256 (bloque 512, padding, estado 8 palabras) → Identificación de hash vulnerable a extensión de longitud → Añadido de padding + datos malignos → Forja de firma/mensaje extendido → Acceso administrativo no autorizado.

**Lección:** *Los hash basados en construcción Merkle-Damgard (como SHA-256) son vulnerables a ataques de extensión de longitud cuando se usan como MAC con concatenación secret\|\|message. La solución segura es usar HMAC u otras construcciones que no sean susceptibles a este tipo de ataque.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1566.001 Phishing (escenario) · T1059 Command and Scripting Interpreter · T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - Length Extension Attacks](https://tryhackme.com/room/lengthextensionattacks)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.