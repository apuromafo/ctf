# Hashing - Crypto 101

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Room | hashingcrypto101 | https://tryhackme.com/room/hashingcrypto101 | 02 Level Medium | TryHackMe | MD5, SHA1, SHA256, bcrypt, sha512crypt, NTLM, rainbow tables, john, hashcat, HMAC | Comprensión práctica de hashing y cracking |

---

**Contexto:** **Hashing - Crypto 101** es una sala teórico-práctica sobre funciones hash. Repasa los términos clave (encoding vs hashing), las propiedades de las funciones hash (MD5 128 bits, colisiones, SHA256), los usos (almacenamiento de passwords, rainbow tables, salting), el reconocimiento de hashes Unix/Windows por prefijos y longitudes, el cracking con john/hashcat/online tools y la verificación de integridad con SHA1/HMAC. Todas las respuestas documentan el output de los ejercicios de cracking.

## Solucionario

### Task 1: Key Terms

**Explicación:** Se repasan los términos (plaintext, encoding, hash, brute force, cryptanalysis). Base64 no es cifrado: es una representación de datos (encoding), inmediatamente reversible.

Respuestas de la tarea:

1. `encoding`

### Task 2: What is a hash function?

**Explicación:** Una función hash produce un digest de tamaño fijo. MD5 genera 128 bits = 16 bytes. Las colisiones son inevitables (Nay), y con un hash de 8 bits hay 2^8 = 256 valores posibles.

Respuestas de la tarea:

1. `16`
2. `Nay`
3. `256`

### Task 3: Uses for hashing

**Explicación:** El almacenamiento de passwords debe usar hash + salt, no cifrado. Se crackea `d0199f51d2728db6011945145a1b607a` manualmente con la rainbow table (basketball) y `5b31f93c09ad1d065c0491b764d04933` con una herramienta online (tryhackme). Cifrar passwords requiere guardar la clave, así que no: `Nay`.

Respuestas de la tarea:

1. `basketball`
2. `tryhackme`
3. `Nay`

### Task 4: Recognising password hashes

**Explicación:** Los hashes Unix se reconocen por prefijo (`$1$` md5crypt, `$2$`/`$2a$`/`$2b$`/`$2x$`/`$2y$` bcrypt, `$6$` sha512crypt; formato `$format$rounds$salt$hash`), y Windows (SAM) por contexto (NTLM, 32 caracteres). Con la página de ejemplo de Hashcat se responde: sha512crypt usa 5000 rounds por defecto; el ejemplo de Citrix Netscaler es `1765058016a22f1b4e076dccd1c3df4e8e5c0839ccded98ea`; un NTLM son 32 caracteres.

Respuestas de la tarea:

1. `5000`
2. `1765058016a22f1b4e076dccd1c3df4e8e5c0839ccded98ea`
3. `32`

### Task 5: Password Cracking

**Explicación:** Se crackean 4 hashes con john y herramientas online usando rockyou/identificadores. bcrypt ($2a$06$...) = 85208520; sha256 (9eb7ee7f...) = halloween; sha512crypt ($6$GQXV...)= spaceman; MD5 (b6b0d451...) = funforyou.

```bash
sudo gzip -d rockyou.txt.gz
echo '$2a$06$7yoU3Ng8dHTXphAg913cyO6Bjs3K5lBnwq5FJyA6d01pMSrddr1ZG' > hash.txt
john hash.txt --format=bcrypt --wordlist=/usr/share/wordlists/rockyou.txt
echo '9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1' > hash256.txt
john hash256.txt --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt
echo '$6$GQXVvW4EuM$ehD6jWiMsfNorxy5SINsgdlxmAEl3.yif0/c3NqzGLa0P.S7KRDYjycw5bnYkF5ZtB8wQy8KnskuWQS3Yr1wQ0' > hash512crypt.txt
john hash512crypt.txt --format=sha512crypt --wordlist=/usr/share/wordlists/rockyou.txt
# MD5 final vía https://hashes.com/en/decrypt/hash
```

Respuestas de la tarea:

1. `85208520`
2. `halloween`
3. `spaceman`
4. `funforyou`

### Task 6: Hashing for integrity checking

**Explicación:** Se verifica integridad: el SHA1SUMS del Kali 2019.4 amd64 ISO contiene `186c5227e24ceb60deb711f1bdc34ad9f4718ff9`. El modo de hashcat para HMAC-SHA512 (key = $pass) es `1750` (example hashes de hashcat); HMAC añade autenticidad + integridad con una clave secreta (la VPN de TryHackMe usa HMAC-SHA512).

Respuestas de la tarea:

1. `186c5227e24ceb60deb711f1bdc34ad9f4718ff9`
2. `1750`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Read the words, and understand the meanings! Is base64 encryption or encoding? | `encoding` |
| 2.1 | What is the output size in bytes of the MD5 hash function? | `16` |
| 2.2 | Can you avoid hash collisions? (Yea/Nay) | `Nay` |
| 2.3 | If you have an 8 bit hash output, how many possible hashes are there? | `256` |
| 3.1 | Crack the hash "d0199f51d2728db6011945145a1b607a" using the rainbow table manually. | `basketball` |
| 3.2 | Crack the hash "5b31f93c09ad1d065c0491b764d04933" using online tools | `tryhackme` |
| 3.3 | Should you encrypt passwords? Yea/Nay | `Nay` |
| 4.1 | How many rounds does sha512crypt ($6$) use by default? | `5000` |
| 4.2 | What's the hashcat example hash (from the website) for Citrix Netscaler hashes? | `1765058016a22f1b4e076dccd1c3df4e8e5c0839ccded98ea` |
| 4.3 | How long is a Windows NTLM hash, in characters? | `32` |
| 5.1 | Crack this hash: $2a$06$7yoU3Ng8dHTXphAg913cyO6Bjs3K5lBnwq5FJyA6d01pMSrddr1ZG | `85208520` |
| 5.2 | Crack this hash: 9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1 | `halloween` |
| 5.3 | Crack this hash: $6$GQXVvW4EuM$ehD6jWiMsfNorxy5SINsgdlxmAEl3.yif0/c3NqzGLa0P.S7KRDYjycw5bnYkF5ZtB8wQy8KnskuWQS3Yr1wQ0 | `spaceman` |
| 5.4 | Bored of this yet? Crack this hash: b6b0d451bbf6fed658659a9e7e5598fe | `funforyou` |
| 6.1 | What's the SHA1 sum for the amd64 Kali 2019.4 ISO? http://old.kali.org/kali-images/kali-2019.4/ | `186c5227e24ceb60deb711f1bdc34ad9f4718ff9` |
| 6.2 | What's the hashcat mode number for HMAC-SHA512 (key = $pass)? | `1750` |

---

**Metodología:** Estudio de teoría de hashing, identificación de algoritmos por prefijo/longitud, cracking con john/hashcat/online tools sobre rockyou y verificación de integridad oficial (SHA1SUMS) y de modo de hashcat para HMAC (OSINT de documentación + práctica de cracking).

**Learning chain:** encoding vs hashing → MD5/SHA256 (tamaño, colisiones) → rainbow tables + salt → reconocimiento de prefijos ($1$/$2a$/$6$/NTLM) → john (bcrypt, raw-sha256, sha512crypt) → online tools (MD5) → integridad (SHA1SUMS Kali) → HMAC-SHA512 (modo 1750) → verificación de autenticidad.

**Lección:** *Identificar el algoritmo por el prefijo o la longitud correctos es la mitad del cracking: `$6$` es sha512crypt, bcrypt aguanta el GPU cracking, y HMAC — no el hash plano — es lo que asegura autenticidad e integridad.*

**MITRE ATT&CK:** T1110.002 Password Cracking (john/hashcat) · T1003.001 OS Credential Dumping (reconocimiento de hashes) · T1573 Encrypted Channel (no aplica) · T1552 Unsecured Credentials (cracking de hashes).

**Fuente:** [TryHackMe - Hashing - Crypto 101](https://tryhackme.com/room/hashingcrypto101)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.