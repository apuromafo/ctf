# Signed Messages [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Evento "Love at First Breach 2026" - Módulo LAFB CTF 2026)
* **Slug:** `lafb2026e8`
* **Link:** https://tryhackme.com/room/lafb2026e8
* **Sección / Section:** 02 Level Medium
* **Fuente / Source:** Web (API THM `api/v2/rooms/tasks?roomCode=lafb2026e8` + websearch de walkthroughs)

## Solucionario de Tareas / Task Solutions

> **ES:** Sala de evento (Love at First Breach 2026, listada en la API como "LoveNote") de dificultad Media. El tema es **criptografía/RSA con PRNG predecible**: un servicio de "love notes" firma mensajes con RSA generado a partir de un generador de números pseudoaleatorios sin seed criptográfica. Reconstruyendo `p` y `q` (y con `e=65537`) se regenera la clave privada y se firma el reto que pide el servidor.
> **EN:** Event room (Love at First Breach 2026, listed in the API as "LoveNote") of Medium difficulty. The theme is **cryptography/RSA with a predictable PRNG**: a "love notes" service signs messages with RSA generated from a pseudo-random number generator lacking a cryptographic seed. By reconstructing `p` and `q` (and with `e=65537`) you regenerate the private key and sign the challenge the server asks for.

### Task 1 - LoveNote Signing

> **ES:** El servicio (puerto criográfico vía `nc` o web) expone firmar mensajes y verifica una firma maestra. Los primos RSA se generan con `random.getrandbits` o similar **sin semilla** (seed fija/derivada del tiempo). Con unas pocas firmas de prueba y el PRNG reproducible (o reconstruyendo el estado del generador a partir de la seed/timestamp) se obtienen `p` y `q` → `n` → `φ(n)` → clave privada (`e=65537`, `d=inv(e, φ(n))`). Se firma el mensaje/`challenge` que el servidor exige y se entrega la flag. 1 pregunta.
> **EN:** The service (a crypto port via `nc` or a web endpoint) lets you sign messages and checks a master signature. The RSA primes are generated with `random.getrandbits` or similar **without a seed** (fixed/time-derived seed). With a few test signatures and the reproducible PRNG (or by recovering the generator state from the seed/timestamp) you obtain `p` and `q` → `n` → `φ(n)` → the private key (`e=65537`, `d=inv(e, φ(n))`). Sign the `challenge` the server demands and the flag is returned. 1 question.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag? | `THM{PR3D1CT4BL3_S33D5_BR34K_H34RT5}` |

## Metodología / Methodology

1. **Paso / Step - Reconocimiento:** Servicio de firmas de "love notes" (puerto `nc`/TCP o endpoint web). Pide firmar un mensaje y valida contra una clave maestra; `e=65537`.
2. **Paso / Step - Análisis de la generación de claves:** El código/indicaciones revelan que `p` y `q` se obtienen con `random.getrandbits`/PRNG **no criptográfico**, sin seed aleatoria (semilla fija o derivable del timestamp).
3. **Paso / Step - Reconstrucción de la clave:** Se regenera la misma secuencia de bits (misma seed/estado) → `p`, `q`; con `n=p*q` y `φ(n)=(p-1)(q-1)`, `d = pow(e, -1, φ(n))`.
4. **Paso / Step - Firmar el reto:** Se firma el mensaje (`sig = pow(m, d, n)`) exigido por el servidor y se envía.
5. **Paso / Step - Flag:** El servicio valida la firma como la "auténtica" y devuelve `THM{PR3D1CT4BL3_S33D5_BR34K_H34RT5}`.

### Cadena de ataque / Attack Chain

```
servicio de firmas (love notes) -> nc/TCP o web
  -> firma de mensajes con RSA, e=65537
  -> PRNG no criptográfico: random.getrandbits sin seed (o seed predecible)
  -> replicar la secuencia -> p, q -> n -> phi(n) -> d
  -> firmar el challenge (sig = pow(m, d, n))
  -> verificación pasa -> THM{PR3D1CT4BL3_S33D5_BR34K_H34RT5}
```

**Lección:** Generar claves RSA con un PRNG no criptográfico (o mal sembrado) rompe la firma por completo (FIPS 186-4 modo 'outdated'): la clave privada se reconstruye desde la seed, no desde el múdulo.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.