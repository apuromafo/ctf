# Encryption - Crypto 101

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Criptografía / Teoría | encryptioncrypto101 | https://tryhackme.com/room/encryptioncrypto101 | 02 Level Medium | TryHackMe | RSA, cifrado simétrico/asimétrico, SSH, GPG/PGP | Fundamentos de criptografía aplicada y rotura de claves débiles |

---

**Contexto:** **Encryption - Crypto 101** es una sala teórico-práctica que introduce el cifrado simétrico y asimétrico, las matemáticas detrás de RSA, las firmas digitales y certificados, la autenticación SSH y el uso práctico de PGP/GPG y AES. Incluye ejercicios con módulo (`%`), el cálculo de `n = p × q`, el crackeo de la passphrase de una clave privada SSH con John the Ripper (`ssh2john` + `rockyou`) y la descifrado de un mensaje GPG. El resultado es una comprensión sólida de cuándo y cómo usar cada primitiva criptográfica.

## Solucionario

### Task 1: Room Overview
**Explicación:**

No requiere respuesta. Es la introducción a la sala, donde se listan los temas: por qué la criptografía importa en seguridad y CTFs, tipos de cifrado, RSA, intercambio de claves (Diffie-Hellman), firmas y certificados.

**Respuesta:** `No answer needed`

### Task 2: Key terms
**Explicación:**

Se pregunta si las claves SSH están protegidas con una passphrase o con una password. A diferencia de una contraseña, la **passphrase** cifra la propia clave privada para protegerla. La definición aparece directamente en el texto del laboratorio.

Respuestas del lab (contenido original):

```
1. No answer needed
2. passphrase
```

### Task 3: Why is Encryption important?
**Explicación:**

Se identifica el acrónimo **SSH** (Secure Shell), el mecanismo que usan los servidores web para demostrar su identidad (**certificates**) y el estándar requerido si se almacenan o procesan datos de tarjetas de pago (**PCI-DSS**). Estas respuestas están en la sección de lectura de la sala.

Respuestas del lab (contenido original):

```
1. Secure Shell
2. certificates
3. PCI-DSS
```

### Task 4: Crucial Crypto Maths
**Explicación:**

Ejercicios de módulo. `30 % 5 = 0`, `25 % 7 = 4` y `118613842 % 9091 = 3565`. El operador `%` devuelve el resto de la división y es la base matemática del cifrado modular (RSA).

Respuestas del lab (contenido original):

```
1. 0
2. 4
3. 3565
```

### Task 5: Types of Encryption
**Explicación:**

Sobre los tipos de cifrado: **DES** ya no es seguro (**Nay**), el intento de hacerlo más seguro fue **Triple DES**, y compartir la clave pública es correcto (**Yea**) porque solo la privada debe mantenerse secreta.

Respuestas del lab (contenido original):

```
1. Nay
2. Triple DES
3. Yea
```

### Task 6: RSA - Rivest Shamir Adleman
**Explicación:**

RSA se basa en multiplicar dos números primos grandes: `p = 4391` y `q = 6659`. Calculando `n = p × q = 29239669`. Factorizar ese `n` es computacionalmente costoso, lo que hace seguro a RSA. La segunda subpregunta es de validación (no requiere respuesta escrita).

Respuestas del lab (contenido original):

```
1. 29239669
2. No answer needed
```

### Task 7: Establishing Keys Using Asymmetric Cryptography
**Explicación:**

Pregunta de comprensión sobre el establecimiento de claves usando criptografía asimétrica. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 8: Digital signatures and Certificates
**Explicación:**

Las firmas digitales prueban la autenticidad de los archivos y quién los creó o modificó. Se produce la firma con la clave privada y se verifica con la pública. La forma más simple: cifrar el documento con la clave privada y descifrarlo con la pública para comprobarlo.

**Respuesta:** `Digital Signature`

### Task 9: SSH Authentication
**Explicación:**

Se practica la autenticación SSH: descargar la clave privada (no requiere respuesta), copiarla/convertirla (no requiere respuesta), identificar el algoritmo de la clave viendo la cabecera del archivo (**RSA**) y crackear su passphrase convirtiendo la clave con `ssh2john` y ejecutando John contra `rockyou`.

Respuestas del lab (contenido original):

```
1. No answer needed
2. No answer needed
3. RSA
4. delicious
```

### Task 10: PGP, GPG and AES
**Explicación:**

Tarea práctica: descargar el archivo comprimido con los artefactos GPG. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Task 11: PGP, GPG and AES (lab GPG)
**Explicación:**

Se descomprime el archivo, se importa la clave con `gpg --import tryhackme.key` y se descifra con `gpg --decrypt message.gpg`. El mensaje revela la palabra secreta: **Pineapple**.

Respuestas del lab (contenido original):

```
1. No answer needed
2. Pineapple
```

### Task 12: The Future - Quantum Computers and Encryption
**Explicación:**

Sección final sobre la amenaza de la computación cuántica a los sistemas criptográficos actuales. No requiere respuesta escrita.

**Respuesta:** `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I agree not to complain too much about how theory heavy this room is | `No answer needed` |
| 2 | ¿Las claves SSH están protegidas con passphrase o password? | `passphrase` |
| 3 | ¿Qué significa SSH? | `Secure Shell` |
| 4 | ¿Cómo demuestran su identidad los servidores web? | `certificates` |
| 5 | ¿Cuál es el estándar obligatorio al almacenar datos de tarjetas? | `PCI-DSS` |
| 6 | ¿Cuál es el resultado de 30 % 5? | `0` |
| 7 | ¿Cuál es el resultado de 25 % 7? | `4` |
| 8 | ¿Cuál es el resultado de 118613842 % 9091? | `3565` |
| 9 | ¿Deberías confiar en DES? (Yea/Nay) | `Nay` |
| 10 | ¿Cuál fue el resultado del intento de hacer DES más seguro? | `Triple DES` |
| 11 | ¿Es correcto compartir tu clave pública? (Yea/Nay) | `Yea` |
| 12 | p = 4391, q = 6659. ¿Cuál es n? | `29239669` |
| 13 | ¿Entiendes RSA lo suficiente para continuar? | `No answer needed` |
| 14 | ¿Entiendes cómo se establecen claves con criptografía asimétrica? | `No answer needed` |
| 15 | ¿Qué mecanismo prueba la autenticidad de un archivo? | `Digital Signature` |
| 16 | ¿Qué algoritmo usa la clave SSH descargada? | `RSA` |
| 17 | ¿Cuál es la passphrase de la clave SSH (John + rockyou)? | `delicious` |
| 18 | Time to try some GPG (descarga el archivo adjunto) | `No answer needed` |
| 19 | ¿Cuál es la palabra secreta tras descifrar message.gpg? | `Pineapple` |
| 20 | ¿Qué piensas sobre el futuro de la criptografía cuántica? | `No answer needed` |

---

**Metodología:** Lectura conceptual de criptografía, cálculos modulares, cómputo de `n = p × q` en RSA, crackeo de passphrase de clave privada SSH con `ssh2john` + `john --wordlist`, e importar/descifrar mensajes GPG con `gpg`.

**Learning chain:** Fundamentos → Términos clave → Importancia del cifrado → Matemáticas modulares → Tipos de cifrado → RSA → Intercambio de claves → Firmas y certificados → SSH → PGP/GPG/AES → Futuro cuántico.

**Lección:** *La criptografía asimétrica separa la clave pública de la privada, pero una passphrase débil o un material de clave mal protegido anula toda la matemática subyacente; herramientas como John y GPG demuestran ese eslabón débil en la práctica.*

**MITRE ATT&CK:** T1552.004 Unsecured Credentials: Private Keys · T1110 Brute Force · T1059 Command and Scripting Interpreter · T1600.002 Cryptography: Disable Crypto Hardware Acceleration.

**Fuente:** [TryHackMe - Encryption - Crypto 101](https://tryhackme.com/room/encryptioncrypto101)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.