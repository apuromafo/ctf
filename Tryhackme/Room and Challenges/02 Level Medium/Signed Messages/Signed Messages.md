# Signed Messages

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `lafb2026e8` |
| **Link** | [TryHackMe](https://tryhackme.com/room/lafb2026e8) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | RSA / predictable PRNG / random.getrandbits / key reconstruction / signing / Love at First Breach 2026 |
| **Impacto** | Comprender cómo un PRNG no criptográfico al generar claves RSA rompe por completo la firma |

---

**Contexto:** Sala de evento (Love at First Breach 2026, listada en la API como "LoveNote") de dificultad Media. El tema es **criptografía/RSA con PRNG predecible**: un servicio de "love notes" firma mensajes con RSA generado a partir de un generador de números pseudoaleatorios sin seed criptográfica.

## Solucionario

### Task 1: LoveNote Signing

**Explicación:**

El servicio (un puerto criptográfico vía `nc` o web) expone firmar mensajes y verifica una firma maestra. Los primos RSA se generan con `random.getrandbits` o similar **sin semilla** (seed fija/derivada del tiempo). Con unas pocas firmas de prueba y el PRNG reproducible (o reconstruyendo el estado del generador a partir de la seed/timestamp) se obtienen `p` y `q` → `n` → `φ(n)` → clave privada (`e=65537`, `d=inv(e, φ(n))`). Se firma el mensaje/`challenge` que el servidor exige y se entrega la flag.

EN (nota adicional): The service (a crypto port via `nc` or a web endpoint) lets you sign messages and checks a master signature. The RSA primes are generated with `random.getrandbits` or similar **without a seed** (fixed/time-derived seed). With a few test signatures and the reproducible PRNG (or by recovering the generator state from the seed/timestamp) you obtain `p` and `q` → `n` → `φ(n)` → the private key (`e=65537`, `d=inv(e, φ(n))`). Sign the `challenge` the server demands and the flag is returned.

**Cadena de ataque / Attack Chain:**
```
servicio de firmas (love notes) -> nc/TCP o web
  -> firma de mensajes con RSA, e=65537
  -> PRNG no criptográfico: random.getrandbits sin seed (o seed predecible)
  -> replicar la secuencia -> p, q -> n -> phi(n) -> d
  -> firmar el challenge (sig = pow(m, d, n))
  -> verificación pasa -> THM{PR3D1CT4BL3_S33D5_BR34K_H34RT5}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag? | `THM{PR3D1CT4BL3_S33D5_BR34K_H34RT5}` |

---

**Metodología:**

1. **Reconocimiento:** Servicio de firmas de "love notes" (puerto `nc`/TCP o endpoint web). Pide firmar un mensaje y valida contra una clave maestra; `e=65537`.
2. **Análisis de la generación de claves:** El código/indicaciones revelan que `p` y `q` se obtienen con `random.getrandbits`/PRNG **no criptográfico**, sin seed aleatoria (semilla fija o derivable del timestamp).
3. **Reconstrucción de la clave:** Se regenera la misma secuencia de bits (misma seed/estado) → `p`, `q`; con `n=p*q` y `φ(n)=(p-1)(q-1)`, `d = pow(e, -1, φ(n))`.
4. **Firmar el reto:** Se firma el mensaje (`sig = pow(m, d, n)`) exigido por el servidor y se envía.
5. **Flag:** El servicio valida la firma como la "auténtica" y devuelve `THM{PR3D1CT4BL3_S33D5_BR34K_H34RT5}`.

**Learning chain:** signing service -> random.getrandbits -> predictable seed -> reconstruct p/q -> n -> φ(n) -> d -> sign challenge -> flag

**Lección:** *Generar claves RSA con un PRNG no criptográfico (o mal sembrado) rompe la firma por completo (FIPS 186-4 modo 'outdated'): la clave privada se reconstruye desde la seed, no desde el módulo.*

**MITRE ATT&CK:** T1600 (Weaken Encryption) · CWE-330 (Use of Insufficiently Random Values) · CWE-338 (Use of Cryptographically Weak PRNG) · CWE-327 (Broken Crypto)

**Fuente:** [TryHackMe - Signed Messages](https://tryhackme.com/room/lafb2026e8)
