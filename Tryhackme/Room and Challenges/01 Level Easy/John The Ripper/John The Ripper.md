# John The Ripper

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| EASY | Walkthrough | `johntheripper0` | https://tryhackme.com/room/johntheripper0 | 01 Level Easy | TryHackMe | John the Ripper / identificación de hashes (hashid) / single crack mode / custom rules / zip2john / rar2john / ssh2john / rockyou.txt | Aprender a usar John the Ripper para crackear hashes: básicos, autenticación Windows (NT), /etc/shadow, ZIP/RAR y claves SSH. |

> **Fuente original / Original source:** GitHub (thmrevenant), Medium (ronnielatte, 0xOG, Saiaditya, Shamsher Khan), M01's Tech Space (mahirm01.page)

---

**Contexto:** Sala que enseña a usar John the Ripper, una herramienta poderosa y adaptable para crackear hashes. Se cubre desde la instalación y configuración hasta técnicas avanzadas como reglas personalizadas, crackeo de archivos protegidos con contraseña (ZIP, RAR) y claves SSH.

> **ES:** Esta sala enseña a usar John the Ripper, una herramienta poderosa y adaptable para crackear hashes. Se cubre desde la instalación y configuración hasta técnicas avanzadas como reglas personalizadas, crackeo de archivos protegidos con contraseña (ZIP, RAR) y claves SSH.
> **EN:** This room teaches how to use John the Ripper, a powerful and adaptable hash-cracking tool. It covers everything from installation and configuration to advanced techniques like custom rules, cracking password-protected files (ZIP, RAR), and SSH keys.

## Solucionario

### Task 1: John Who?

**Explicación:** Introducción conceptual a John the Ripper: un hash es una representación criptográfica de datos (normalmente una contraseña) que no puede revertirse fácilmente, y John intenta adivinarlo probando combinaciones de contraseñas hasta encontrar una que coincida.

> **ES:** John the Ripper es una herramienta de crackeo de hashes. Un hash es una representación criptográfica de datos (generalmente una contraseña) que no se puede revertir fácilmente. John the Ripper intenta adivinar el hash probando diferentes combinaciones de contraseñas hasta encontrar una que coincida.
> **EN:** John the Ripper is a hash-cracking tool. A hash is a cryptographic representation of data (usually a password) that cannot be easily reversed. John the Ripper attempts to guess the hash by trying different password combinations until a match is found.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (No answer needed - conceptual introduction) | `No answer needed` |

### Task 2: Setting Up John the Ripper

**Explicación:** La versión más popular extended de John the Ripper es **Jumbo John**, que incluye soporte para muchos más formatos de hash que la versión original.

> **ES:** La versión más popular extendida de John the Ripper es **Jumbo John**, que incluye soporte para muchos más formatos de hash que la versión original.
> **EN:** The most popular extended version of John the Ripper is **Jumbo John**, which includes support for many more hash formats than the original version.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the most popular extended version of John the Ripper? | `Jumbo John` |

### Task 3: Wordlists

**Explicación:** La wordlist `rockyou.txt` proviene de una brecha de seguridad en el sitio web **rockyou.com**, que expuso millones de contraseñas en texto plano.

> **ES:** La wordlist `rockyou.txt` fue creada a partir de una brecha de seguridad en el sitio web **rockyou.com**, que expuso millones de contraseñas en texto plano.
> **EN:** The `rockyou.txt` wordlist was created from a security breach on the **rockyou.com** website, which exposed millions of plaintext passwords.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which website's breach was the rockyou.txt wordlist created from? | `rockyou.com` |

### Task 4: Cracking Basic Hashes

**Explicación:** Para crackear hashes básicos se identifica primero el tipo de hash usando herramientas como `hash-identifier` o hashid. Luego se usa John con el formato correcto y la wordlist. Los hashes identificados son: hash1.txt (MD5), hash2.txt (SHA1), hash3.txt (SHA256), hash4.txt (Whirlpool).

> **ES:** Para crackear hashes básicos, primero se identifica el tipo de hash usando herramientas como `hash-identifier` o hashid. Luego se usa John con el formato correcto y la wordlist. Los hashes identificados son: hash1.txt (MD5), hash2.txt (SHA1), hash3.txt (SHA256), hash4.txt (Whirlpool).
> **EN:** To crack basic hashes, first identify the hash type using tools like `hash-identifier` or hashid. Then use John with the correct format and wordlist. The identified hashes are: hash1.txt (MD5), hash2.txt (SHA1), hash3.txt (SHA256), hash4.txt (Whirlpool).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of hash is hash1.txt? | `md5` |
| 2 | What is the cracked value of hash1.txt? | `biscuit` |
| 3 | What type of hash is hash2.txt? | `sha1` |
| 4 | What is the cracked value of hash2.txt? | `kangeroo` |
| 5 | What type of hash is hash3.txt? | `sha256` |
| 6 | What is the cracked value of hash3.txt? | `microphone` |
| 7 | What type of hash is hash4.txt? | `whirlpool` |
| 8 | What is the cracked value of hash4.txt? | `colossal` |

### Task 5: Cracking Windows Authentication Hashes

**Explicación:** Los hashes de autenticación Windows (NTHash/NTLM) se crackean usando el formato `NT`. Se ejecuta: `john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt ntlm.txt`

> **ES:** Los hashes de autenticación Windows (NTHash/NTLM) se crackean usando el formato `NT`. Se ejecuta: `john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt ntlm.txt`
> **EN:** Windows authentication hashes (NTHash/NTLM) are cracked using the `NT` format. Run: `john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt ntlm.txt`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What do we need to set the `--format` flag to in order to crack this hash? | `NT` |
| 2 | What is the cracked value of this password? | `mushroom` |

### Task 6: Cracking /etc/shadow Hashes

**Explicación:** Para crackear hashes de `/etc/shadow` de Linux se usa el formato `sha512crypt`. Se ejecuta: `john --format=sha512crypt --wordlist=/usr/share/wordlists/rockyou.txt etchashes.txt`

> **ES:** Para crackear hashes de `/etc/shadow` de Linux, se usa el formato `sha512crypt`. Se ejecuta: `john --format=sha512crypt --wordlist=/usr/share/wordlists/rockyou.txt etchashes.txt`
> **EN:** To crack Linux `/etc/shadow` hashes, use the `sha512crypt` format. Run: `john --format=sha512crypt --wordlist=/usr/share/wordlists/rockyou.txt etchashes.txt`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the root password? | `1234` |

### Task 7: Single Crack Mode

**Explicación:** El modo single crack de John utiliza el nombre de usuario como parte de las contraseñas probadas. Se debe anteponer el nombre de usuario y dos puntos al hash (ej: `Joker:hash`). Se ejecuta: `john --single --format=raw-md5 hash07.txt`

> **ES:** El modo single crack de John utiliza el nombre de usuario como parte de las contraseñas probadas. Se debe anteponer el nombre de usuario y dos puntos al hash (ej: `Joker:hash`). Se ejecuta: `john --single --format=raw-md5 hash07.txt`
> **EN:** John's single crack mode uses the username as part of the tested passwords. You must prepend the username and colon to the hash (e.g., `Joker:hash`). Run: `john --single --format=raw-md5 hash07.txt`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is Joker's password? | `Jok3r` |

### Task 8: Custom Rules

**Explicación:** Las reglas personalizadas permiten explotar la **predecibilidad de la complejidad de contraseñas**. Para agregar todas las letras mayúsculas al final de una palabra se usa la regla `Az"[A-Z]"`. Para llamar a una regla personalizada llamada "THMRules" se usa el flag `--rule=THMRules`.

> **ES:** Las reglas personalizadas permiten explotar la **predecibilidad de la complejidad de contraseñas**. Para agregar todas las letras mayúsculas al final de una palabra se usa la regla `Az"[A-Z]"`. Para llamar a una regla personalizada llamada "THMRules" se usa el flag `--rule=THMRules`.
> **EN:** Custom rules allow exploiting **password complexity predictability**. To add all capital letters to the end of a word, use the rule `Az"[A-Z]"`. To call a custom rule called "THMRules", use the flag `--rule=THMRules`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What do custom rules allow us to exploit? | `Password complexity predictability` |
| 2 | What rule would we use to add all capital letters to the end of the word? | `Az"[A-Z]"` |
| 3 | What flag would we use to call a custom rule called THMRules? | `--rule=THMRules` |

### Task 9: Cracking Password Protected Zip Files

**Explicación:** Para crackear archivos ZIP protegidos se usa `zip2john` para convertir el ZIP a un hash, y luego John con rockyou.txt. Se ejecuta: `zip2john secure.zip > hash.txt && john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`

> **ES:** Para crackear archivos ZIP protegidos, se usa `zip2john` para convertir el ZIP a un hash, luego John con rockyou.txt. Se ejecuta: `zip2john secure.zip > hash.txt && john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`
> **EN:** To crack password-protected ZIP files, use `zip2john` to convert the ZIP to a hash, then John with rockyou.txt. Run: `zip2john secure.zip > hash.txt && john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password for the secure.zip file? | `pass123` |
| 2 | What is the contents of the flag inside the zip file? | `THM{w3ll_d0n3_h4sh_r0y4l}` |

### Task 10: Cracking Password Protected RAR Archives

**Explicación:** Para crackear archivos RAR protegidos se usa `rar2john` para convertir el RAR a un hash, y luego John con rockyou.txt. Se ejecuta: `rar2john secure.rar > hash.txt && john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`

> **ES:** Para crackear archivos RAR protegidos, se usa `rar2john` para convertir el RAR a un hash, luego John con rockyou.txt. Se ejecuta: `rar2john secure.rar > hash.txt && john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`
> **EN:** To crack password-protected RAR files, use `rar2john` to convert the RAR to a hash, then John with rockyou.txt. Run: `rar2john secure.rar > hash.txt && john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password for the secure.rar file? | `password` |
| 2 | What are the contents of the flag inside the rar file? | `THM{r4r_4rch1ve}` |

### Task 11: Cracking SSH Keys with John

**Explicación:** Para crackear claves SSH privadas (id_rsa) se usa `ssh2john.py` para extraer el hash de la clave privada, y luego John con rockyou.txt. Se ejecuta: `python3 /opt/john/ssh2john.py id_rsa > id_rsa_hash.txt && john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt`

> **ES:** Para crackear claves SSH privadas (id_rsa), se usa `ssh2john.py` para extraer el hash de la clave privada, luego John con rockyou.txt. Se ejecuta: `python3 /opt/john/ssh2john.py id_rsa > id_rsa_hash.txt && john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt`
> **EN:** To crack SSH private keys (id_rsa), use `ssh2john.py` to extract the hash from the private key, then John with rockyou.txt. Run: `python3 /opt/john/ssh2john.py id_rsa > id_rsa_hash.txt && john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt`

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the SSH private key password? | `mango` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the most popular extended version of John the Ripper? | `Jumbo John` |
| 2 | Which website's breach was the rockyou.txt wordlist created from? | `rockyou.com` |
| 3 | What type of hash is hash1.txt? | `md5` |
| 4 | What is the cracked value of hash1.txt? | `biscuit` |
| 5 | What type of hash is hash2.txt? | `sha1` |
| 6 | What is the cracked value of hash2.txt? | `kangeroo` |
| 7 | What type of hash is hash3.txt? | `sha256` |
| 8 | What is the cracked value of hash3.txt? | `microphone` |
| 9 | What type of hash is hash4.txt? | `whirlpool` |
| 10 | What is the cracked value of hash4.txt? | `colossal` |
| 11 | What do we need to set the `--format` flag to in order to crack this hash? | `NT` |
| 12 | What is the cracked value of this password? | `mushroom` |
| 13 | What is the root password? | `1234` |
| 14 | What is Joker's password? | `Jok3r` |
| 15 | What do custom rules allow us to exploit? | `Password complexity predictability` |
| 16 | What rule would we use to add all capital letters to the end of the word? | `Az"[A-Z]"` |
| 17 | What flag would we use to call a custom rule called THMRules? | `--rule=THMRules` |
| 18 | What is the password for the secure.zip file? | `pass123` |
| 19 | What is the contents of the flag inside the zip file? | `THM{w3ll_d0n3_h4sh_r0y4l}` |
| 20 | What is the password for the secure.rar file? | `password` |
| 21 | What are the contents of the flag inside the rar file? | `THM{r4r_4rch1ve}` |
| 22 | What is the SSH private key password? | `mango` |

---

**Metodología:** 

1. **Paso / Step - Identificación del tipo de hash:** Usar herramientas como `hash-identifier`, `hashid` o sitios web como hashed.com para determinar el algoritmo de hash utilizado.
2. **Paso / Step - Selección del formato correcto en John:** Mapear el tipo de hash identificado al formato correspondiente de John (raw-md5, raw-SHA1, raw-SHA256, whirlpool, NT, sha512crypt, etc.).
3. **Paso / Step - Ejecución del crackeo básico:** Ejecutar `john --format=<formato> --wordlist=/usr/share/wordlists/rockyou.txt <archivo_hash>`.
4. **Paso / Step - Uso de herramientas auxiliares:** Para archivos especiales (ZIP, RAR, SSH), usar convertidores como `zip2john`, `rar2john` y `ssh2john.py` antes de ejecutar John.
5. **Paso / Step - Modo single crack:** Cuando se conoce el nombre de usuario, anteponerlo al hash para que John lo use como semilla de contraseñas.
6. **Paso / Step - Reglas personalizadas:** Definir reglas para generar variaciones de contraseñas que exploten la predecibilidad de la complejidad humana.
7. **Paso / Step - Verificación de resultados:** Usar `john --show` para mostrar las contraseñas crackeadas y verificar los resultados.

### Cadena de ataque / Attack Chain

```text
Obtención del hash (archivo, servicio, etc.)
        |
        v
Identificación del tipo de hash (hash-identifier/hashid)
        |
        v
Selección del formato John (raw-md5, NT, sha512crypt, etc.)
        |
        v
 Crackeo con wordlist (rockyou.txt)
        |
        v
 Si falla: modo single / reglas personalizadas
        |
        v
Verificación con john --show
        |
        v
 Extracción de flag o credenciales
```

**Learning chain:** hash -> hashid/hash-identifier -> formato John -> wordlist -> single/custom rules -> john --show -> flag.

**Lección:** *John the Ripper es una herramienta versátil que puede crackear prácticamente cualquier tipo de hash; la clave está en identificar correctamente el formato del hash y seleccionar la estrategia de crackeo adecuada (wordlist, single mode, reglas personalizadas).*

**MITRE ATT&CK:** T1110.002 (Password Cracking), T1110 (Brute Force)

**Fuente:** [TryHackMe - John The Ripper](https://tryhackme.com/room/johntheripper0)
---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.