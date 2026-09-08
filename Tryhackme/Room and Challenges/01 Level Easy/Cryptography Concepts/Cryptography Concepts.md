# Cryptography Concepts

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `cryptographyconcepts` |
| **Link** | [TryHackMe](https://tryhackme.com/room/cryptographyconcepts) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + juego estático "Secret Message Rescue" |
| **Componentes** | Cifrado simétrico (Caesar/ROT) / cifrado asimétrico (par de claves) / distribución de claves / HTTPS (handshake asimétrico + datos simétricos) |
| **Impacto** | Comprende los fundamentos de criptografía: por qué la distribución de claves es el problema central y por qué HTTPS combina cifrado asimétrico y simétrico. |

---

**Contexto:** La criptografía de clave **simétrica** usa UNA sola clave para cifrar y descifrar (ej. la clásica **cifra de César**: desplazar cada letra K posiciones). Su problema central es la **distribución de claves**: ¿cómo pasas la clave sin que la intercepten? La criptografía **asimétrica** lo resuelve con un **par de claves**: la **pública** (se comparte) y la **privada** (se queda secreta). Lo que cifras con la pública solo lo descifra la privada correspondiente. En **HTTPS**, el handshake usa asimétrica (RSA/ECDSA) para compartir una clave simétrica de sesión, y luego la **bulk data** viaja con cifrado **simétrico** (AES/GCM) porque es mucho más rápido. ROT13 (clave 13) es el caso especial de César donde el desplazamiento es la mitad del alfabeto: `FVZCYR PNRFNE PVCURE` = **SIMPLE CAESAR CIPHER**.

## Solucionario

### Task 1: Introducción

**Explicación:** Inicio de fundamentos criptográficos (Pre Security). Tarea de introducción, sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - start of crypto fundamentals. | `No answer needed` |

### Task 2: Escondiendo Información: Cifrado Simétrico

**Explicación:** El juego **"Secret Message Rescue"** es un simulador con varios niveles de cifrado de César; al completarlos todos entrega `THM{CAESAR_CIPHER_MASTER_2026}`. Para cifrar **CYBER** con la clave 5 se desplaza cada letra 5 posiciones: C→H, Y→D, B→G, E→J, R→W = `HDGJW`. La cadena `FVZCYR PNRFNE PVCURE` es **ROT13** (clave 13, la mitad del alfabeto la vuelve inversa): F→S, V→I, Z→M... = `SIMPLE CAESAR CIPHER`. El room pide la **clave** = `13` (el mensaje descifrado es "SIMPLE CAESAR CIPHER").

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the flag you received after completing all levels of the **Secret Message Rescue** game? | `THM{CAESAR_CIPHER_MASTER_2026}` |
| 2 | Using the Caesar cipher with a key of 5, what does **CYBER** become when encoded? (Uppercase, no spaces.) | `HDGJW` |
| 3 | Using the Caesar cipher, find the correct key and decode `FVZCYR PNRFNE PVCURE`. | `13` |

### Task 3: Compartiendo Claves con Seguridad: Cifrado Asimétrico

**Explicación:** La clave **privada** es la que permanece secreta; la pública se comparte abiertamente. "Yay" describe exactamente la propiedad del *public-key encryption*: cifrar con la pública ➜ descifrar solo con la privada. El problema central que resuelve la asimetría es la **distribución de claves** (negociar material de clave sin compartir el secreto por el canal). En **HTTPS** el handshake es asimétrico (autenticación + intercambio de clave de sesión) y a partir de ahí los datos masivos se cifran con **simétrico** por velocidad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | In asymmetric encryption, which key stays secret? | `Private key` |
| 2 | With asymmetric encryption, Alice can encrypt a message using Bob's public key, and only Bob's private key can decrypt it. Yay or Nay? | `Yay` |
| 3 | What problem does asymmetric solve that symmetric cannot? | `Key distribution` |
| 4 | After initial asymmetric exchange in HTTPS, what encryption type handles bulk data? | `Symmetric` |

### Task 4: Conclusión

**Explicación:** Punto de partida hacia RSA/AES, certificados y PKI. La lección clave: *las claves son el verdadero secreto* — el cifrado resiste ataques; lo que suele fallar es la distribución o el almacenamiento de las claves. Tarea de cierre, sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - room complete. | `No answer needed` |

---

**Metodología:**
1. Completar el minijuego de cifrado de César "Secret Message Rescue" (niveles 1..N) → flag `THM{CAESAR_CIPHER_MASTER_2026}`.
2. Cifrar "CYBER" con desplazamiento 5 letra a letra: C→H, Y→D, B→G, E→J, R→W = `HDGJW`.
3. Detectar que `FVZCYR PNRFNE PVCURE` aplica ROT13 (clave 13, la mitad del alfabeto que la vuelve inversa): F→S, V→I, Z→M… = `SIMPLE CAESAR CIPHER`; el room pide la **clave** = `13`.
4. Responder conceptos de asimétrico leyendo la sección: la private key es la que permanece secreta; "Yay" por la propiedad del public-key encryption; el problema central que resuelve es la key distribution; y en HTTPS el bulk data se cifra con simétrico por velocidad.

**Learning chain:** César/ROT (simétrica) → HDGJW, key=13, THM{CAESAR_CIPHER_MASTER_2026} → problema: compartir la clave (key distribution) → asimétrica (par de claves: private/public) → uso real en HTTPS: handshake asimétrico + bulk simétrico.

**MITRE ATT&CK:** T1573 (Encrypted Channel), T1573.002 (Asymmetric Cryptography), T1001 (Data Obfuscation).

**Fuente:** [TryHackMe - Cryptography Concepts](https://tryhackme.com/room/cryptographyconcepts)