# Public Key Cryptography Basics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `publickeycryptographybasics` | https://tryhackme.com/room/publickeycryptographybasics | 01 Level Easy | THM | RSA, Diffie-Hellman, SSH, HTTPS, GPG | Fundamentos de criptografía asimétrica |

---

**Contexto:** Room introductorio de criptografía asimétrica en la ruta Cyber Security 101. Cubre RSA (factorización de primos, claves pública/privada), Diffie-Hellman (intercambio de claves sobre canales inseguros), SSH (autenticación por claves), certificados digitales (CA, TLS) y PGP/GPG (cifrado y firmas), con ejercicios prácticos sobre una máquina virtual.

> **ES:** Room introductorio de criptografía asimétrica que cubre RSA, Diffie-Hellman, SSH, certificados digitales (TLS) y PGP/GPG, con ejercicios prácticos: cifrado/descifrado, intercambio de claves y uso de GPG.
> **EN:** An introductory asymmetric cryptography room covering RSA, Diffie-Hellman, SSH, digital certificates (TLS) and PGP/GPG, with hands-on exercises: encryption/decryption, key exchange and GPG usage.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se realiza una primera aproximación a la idea de datos privados en el equipo (cifrado de disco completo) y se prepara el entorno de trabajo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's start! | `No answer needed` |

### Task 2: Uso común del cifrado asimétrico / Common Use of Asymmetric Encryption

**Explicación:** Se explica el cifrado asimétrico (par de claves pública/privada) y su uso frecuente en el cifrado de datos en tránsito.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's a good example of asymmetric encryption that you interact with? | `Lock` |

### Task 3: RSA / RSA

**Explicación:** RSA se apoya en la factorización de dos primos grandes. Se usa la máquina virtual para realizar los cálculos de la clave privada y del descifrado del mensaje.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is d (the private key)? | `29239669` |
| 2 | What is m (the integer of the plaintext)? | `29228620` |

### Task 4: Intercambio de claves Diffie-Hellman / Diffie-Hellman Key Exchange

**Explicación:** Diffie-Hellman permite a dos partes acordar una clave secreta sobre un canal inseguro. Se calculan las claves públicas A y B y la clave compartida que ambas derivan.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of A? | `7` |
| 2 | What is the value of B? | `9` |
| 3 | What is the value of the shared secret computed by B? | `24` |
| 4 | What is the value of the shared secret computed by A? | `24` |

### Task 5: SSH / SSH

**Explicación:** SSH usa un protocolo de intercambio de claves y autenticación asimétrica para establecer conexiones seguras.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What asymmetric mechanism does SSH use? | `RSA` |

### Task 6: Firmas digitales y certificados / Digital Signatures and Certificates

**Explicación:** Los certificados digitales vinculan una identidad con una clave pública mediante una autoridad certificadora (CA). Se genera un certificado de prueba con la CA Let's Encrypt sobre la máquina virtual.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the mechanism that binds a public key to a trusted entity? | `Certificate` |
| 2 | What is the name of the certificate authority used for the test certificate? | `Let's Encrypt` |

### Task 7: PGP y GPG / PGP and GPG

**Explicación:** GPG es la implementación de código abierto del estándar PGP para cifrar y firmar datos con claves asimétricas. Se descifra un archivo cifrado con la clave pública del destinatario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the content of the decrypted message? | `Pineapple` |

### Task 8: Conclusión / Conclusion

**Explicación:** Se recapitulan los conceptos clave de los cifrados asimétricos vistos en el room (RSA, Diffie-Hellman, SSH, certificados y GPG).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the room | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's start! | `No answer needed` |
| 2 | What's a good example of asymmetric encryption that you interact with? | `Lock` |
| 3 | What is d (the private key)? | `29239669` |
| 4 | What is m (the integer of the plaintext)? | `29228620` |
| 5 | What is the value of A? | `7` |
| 6 | What is the value of B? | `9` |
| 7 | What is the value of the shared secret computed by B? | `24` |
| 8 | What is the value of the shared secret computed by A? | `24` |
| 9 | What asymmetric mechanism does SSH use? | `RSA` |
| 10 | What is the mechanism that binds a public key to a trusted entity? | `Certificate` |
| 11 | What is the name of the certificate authority used for the test certificate? | `Let's Encrypt` |
| 12 | What is the content of the decrypted message? | `Pineapple` |
| 13 | Complete the room | `No answer needed` |

---

**Metodología:** Desplegar la máquina virtual con las herramientas (RSA, GPG, openssl), resolver los cálculos de RSA y Diffie-Hellman, comprobar el uso de RSA en SSH, generar el certificado TLS con la CA y descifrar el mensaje con GPG.

### Cadena de ataque / Attack Chain

```text
Desplegar MV de trabajo → calcular clave privada d y desencriptar m (RSA) → calcular A, B y clave compartida (Diffie-Hellman) → verificar RSA en SSH → generar certificado con CA → descifrar mensaje GPG → conceptos consolidados
```

**Learning chain:** Introducción → Uso común del cifrado asimétrico → RSA → Diffie-Hellman → SSH → Certificados → GPG → Conclusión

**Lección:** *El cifrado asimétrico resuelve el intercambio de secretos y la autenticación sobre canales inseguros gracias a pares de claves pública/privada y funciones matemáticas como la factorización (RSA) y el logaritmo discreto (Diffie-Hellman).*

**MITRE ATT&CK:** N/A (Room teórico-práctico de criptografía)

**Fuente:** [TryHackMe - Public Key Cryptography Basics](https://tryhackme.com/room/publickeycryptographybasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.