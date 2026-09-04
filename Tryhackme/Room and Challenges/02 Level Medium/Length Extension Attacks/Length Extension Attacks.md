# Length Extension Attacks [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `lengthextensionattacks`
* **Link:** https://tryhackme.com/room/lengthextensionattacks
* **Sección / Section:** Crypto / Web
* **Fuente / Source:** Writeup de thmrevenant (GitHub)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Esta sala explora los ataques de extensión de longitud (length extension attacks) sobre hash basados en Merkle-Damgard como SHA-256. Cubre propiedades criptográficas, la estructura interna del algoritmo y cómo abusar del padding para extender mensajes firmados sin conocer la clave secreta.
> **EN:** This room explores length extension attacks on Merkle-Damgard based hashes like SHA-256. It covers cryptographic properties, the algorithm's internal structure and how to abuse padding to extend signed messages without knowing the secret key.

---

### Task 1 — Propiedades Criptográficas / Cryptographic Properties

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What property prevents an attacker from reversing a hash to get the original input? | `Pre-image Resistance` |
| What property ensures that no two different messages produce the same hash? | `Collision Resistance` |

---

### Task 2 — Estructura Interna de SHA-256 / SHA-256 Internals

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What block size does SHA-256 use? | `512` |
| What function ensures data is aligned to fit block size requirements? | `Padding` |
| How many words does SHA-256's internal state have? | `8` |

---

### Task 3 — Mitigación y Explotación / Mitigation & Exploitation

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What hashing method prevents length extension attacks by using a secret key? | `HMAC` |
| What is the flag in the image? | `THM{L3n6th_3Xt33ns10nssss}` |
| What is the flag? | `THM{l3n6th_2_4dM1n}` |

---

## Metodología / Methodology

1. **Paso 1 / Step 1:** Se comprenden las propiedades criptográficas de las funciones hash: resistencia a preimagen y resistencia a colisiones.
2. **Paso 2 / Step 2:** Se analiza la estructura interna de SHA-256: tamaño de bloque de 512 bits, la función de relleno (padding) que alinea los datos y el estado interno de 8 palabras.
3. **Paso 3 / Step 3:** Se aprende que HMAC previene los ataques de extensión de longitud, y se explota la vulnerabilidad añadiendo padding y datos extra a un mensaje firmado para obtener acceso administrativo sin conocer la clave secreta.

### Cadena de ataque / Attack Chain

```
Comprensión de propiedades hash → Análisis de estructura SHA-256 (bloque 512, padding, estado 8 palabras) → Identificación de hash vulnerable a extensión de longitud → Añadido de padding + datos malignos → Forja de firma/mensaje extendido → Acceso administrativo no autorizado
```

**Lección:** Los hash basados en construcción Merkle-Damgard (como SHA-256) son vulnerables a ataques de extensión de longitud cuando se usan como MAC con concatenación secret||message. La solución segura es usar HMAC u otras construcciones que no sean susceptibles a este tipo de ataque.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
