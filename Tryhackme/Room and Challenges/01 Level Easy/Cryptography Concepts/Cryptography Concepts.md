# Cryptography Concepts [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `cryptographyconcepts`
* **Link:** https://tryhackme.com/room/cryptographyconcepts
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + juego estático "Secret Message Rescue"
* **Componentes:** Cifrado simétrico (Caesar/ROT) · cifrado asimétrico (par de claves) · distribución de claves · HTTPS (handshake asimétrico + datos simétricos)
* **Impacto rol:** Fundamentos de criptografía; entender por qué HTTPS usa ambas familias de cifrado y por qué el problema de "compartir la clave" es el centro de la criptografía moderna.

## Solucionario de Tareas / Task Solutions

> **ES:** La criptografía de clave **simétrica** usa UNA sola clave para cifrar y descifrar (ej. la clásica **cifra de César**: desplazar cada letra K posiciones). Su problema central es la **distribución de claves**: ¿cómo pasas la clave sin que la intercepten? La criptografía **asimétrica** lo resuelve con un **par de claves**: la **pública** (se comparte) y la **privada** (se queda secreta). Lo que cifras con la pública solo lo descifra la privada correspondiente. En **HTTPS**, el handshake usa asimétrica (RSA/ECDSA) para compartir una clave simétrica de sesión, y luego la **bulk data** viaja con cifrado **simétrico** (AES/GCM) porque es mucho más rápido. ROT13 (clave 13) es el caso especial de César donde el desplazamiento es la mitad del alfabeto: `FVZCYR PNRFNE PVCURE` = **SIMPLE CAESAR CIPHER**.
> **EN:** **Symmetric** cryptography uses ONE shared key to encrypt and decrypt (e.g. the classic **Caesar cipher**: shift every letter by K positions). Its central problem is **key distribution**: how do you deliver the key without it being intercepted? **Asymmetric** cryptography solves this with a **key pair**: the **public** key (shared) and the **private** key (kept secret). Whatever is encrypted with the public key can only be decrypted by the matching private key. In **HTTPS**, the handshake uses asymmetric crypto (RSA/ECDSA) to agree a symmetric session key, then **bulk data** is transported with **symmetric** encryption (AES/GCM) because it's far faster. ROT13 (key 13) is the Caesar special case where the shift is half the alphabet: `FVZCYR PNRFNE PVCURE` = **SIMPLE CAESAR CIPHER**.

### Task 1 — Introducción / Introduction

* **Check:** `Let's get started.`
* **ES:** Inicio de fundamentos criptográficos (Pre Security).
* **EN:** Start of crypto fundamentals (Pre Security).

### Task 2 — Escondiendo Información: Cifrado Simétrico / Hiding Information — Symmetric Encryption *(static-site)*

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What's the flag you received after completing all levels of the **Secret Message Rescue** game? | `THM{CAESAR_CIPHER_MASTER_2026}` |
| Using the Caesar cipher with a key of 5, what does **CYBER** become when encoded? (Uppercase, no spaces.) | `HDGJW` |
| Using the Caesar cipher, find the correct key and decode `FVZCYR PNRFNE PVCURE`. | `13` |

* **Juego / Game:** "Secret Message Rescue" es un simulador con varios niveles de cifrado de César; al completarlos todos entrega `THM{CAESAR_CIPHER_MASTER_2026}`.
* **CYBER + 5:** desplaza cada letra 5 posiciones: C→H, Y→D, B→G, E→J, R→W = `HDGJW`.
* **`FVZCYR PNRFNE PVCURE`:** es **ROT13** (clave 13, la mitad del alfabeto la vuelve inversa): F→S, V→I, Z→M... = `SIMPLE CAESAR CIPHER`. La respuesta que pide el room es la **clave** = `13` (el mensaje descifrado es "SIMPLE CAESAR CIPHER").

### Task 3 — Compartiendo Claves con Seguridad: Cifrado Asimétrico / Sharing Keys Safely: Asymmetric Encryption

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| In asymmetric encryption, which key stays secret? | `Private key` |
| With asymmetric encryption, Alice can encrypt a message using Bob's public key, and only Bob's private key can decrypt it. Yay or Nay? | `Yay` |
| What problem does asymmetric solve that symmetric cannot? | `Key distribution` |
| After initial asymmetric exchange in HTTPS, what encryption type handles bulk data? | `Symmetric` |

* **Privada / Private key:** la que permanece secreta; la pública se comparte abiertamente.
* **Yay:** significado exacto de la propiedad del *public-key encryption* (cifrar con pública ➜ descifrar solo con la privada).
* **Problema central / Core problem:** la **distribución de claves**; el asimétrico permite negociar material de clave sin compartir el secreto por el canal.
* **HTTPS:** handshake asimétrico (autenticación + intercambio de clave de sesión) y a partir de ahí datos masivos con cifrado **simétrico** por velocidad.

### Task 4 — Conclusión / Conclusion

* **Check:** `I've completed the room!`
* **ES:** Punto de partida hacia RSA/AES, certificados y PKI.
* **EN:** Starting point toward RSA/AES, certificates and PKI.

## Metodología / Methodology

1. **Paso / Step:** Completar el minijuego de cifrado de César (niveles 1..N) → flag.
2. **Paso / Step:** Cifrar "CYBER" con desplazamiento 5 letra a letra.
3. **Paso / Step:** Detectar que `FVZCYR PNRFNE PVCURE` aplica ROT13 (clave 13) y descifrarlo.
4. **Paso / Step:** Responder conceptos de asimétrico leyendo la sección (private key, Yay, key distribution, symmetric).

### Cadena de aprendizaje / Learning Chain

```
César / ROT (simétrica)            -> HDGJW, key=13, THM{CAESAR_CIPHER_MASTER_2026}
  problema: compartir la clave (key distribution)
Asimétrica (par de claves)         -> private/public
  uso real en HTTPS: handshake asimétrico + bulk simétrico
```

**Mapeo MITRE ATT&CK / relacionado:** T1573 (Encrypted Channel) y T1573.002 (Asymmetric Cryptography) — cómo los C2 suelen cifrar; T1001 (Data Obfuscation). Defensivamente, el conocimiento de simétrica/asimétrica explica el "cifrado indescifrable" versus "cifrado con clave". Room teórico.

**Lección:** *Las claves son el verdadero secreto.* El cifrado resiste ataques; lo que falla suele ser la distribución o el almacenamiento de las claves.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.