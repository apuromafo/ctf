# Password Attacks

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|------|------|------|---------|--------|-------------|---------|
| Hard | Walkthrough | `passwordattacks` | [TryHackMe](https://tryhackme.com/room/passwordattacks) | 03 Level Hard | Web (API THM `api/v2/rooms/tasks?roomCode=passwordattacks` + websearch de walkthroughs) | Password Cracking / Hashcat / John the Ripper / Crunch / Hash Rules / Auxiliary modules (Metasploit) / Hydra / cURL personalizado | Metodología completa de ataque a contraseñas: conceptos teóricos, cracking local, credenciales por defecto, generación de diccionarios, identificación de hashes, reglas de hashcat, fuerza bruta de formularios/FTP y password spraying contra SSH. |

---

**Contexto:**

> **ES:** **Password Attacks** es una sala-teoría de TryHackMe, clasificada Hard, que sienta las bases de toda la disciplina de "Password Attacks". Cubre desde los conceptos básicos (cómo funciona el cracking y los tipos de ataque: local/offline vs. remoto/online) hasta el uso de Hashcat y John the Ripper, la generación de diccionarios con `crunch`, la identificación de formatos de hash, las reglas de transformación de Hashcat, los módulos auxiliares de Metasploit para credenciales por defecto y fuerza bruta sobre FTP, y el famoso ataque de password spraying. Las preguntas se responden (en su mayoría) con el resultado exacto de los comandos propuestos en cada tarea, reflejando fielmente los flags y contraseñas que produce la sala según se ejecutan los ejemplos.
> **EN:** **Password Attacks** is a theory-focused TryHackMe room, classified Hard, that lays the foundations of the whole "Password Attacks" discipline. It covers from the basics (how cracking works and the attack types: local/offline vs. remote/online) to the use of Hashcat and John the Ripper, dictionary generation with `crunch`, hash format identification, Hashcat transformation rules, Metasploit auxiliary modules for default credentials and FTP brute force, and the famous password spraying attack. The questions are answered (mostly) with the exact output of the commands proposed in each task, faithfully reflecting the flags and passwords the room produces as the examples are executed.

---

## Solucionario

### Task 1: Bienvenida y conceptos / Welcome and Concepts

**Explicación:**
La primera tarea es puramente introductoria: explica el concepto de ataque a contraseñas y no requiere respuesta.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

---

### Task 2: Ataques de contraseña / Password Attacks

**Explicación:**
Introduce los dos grandes tipos de ataque: local (offline) y remoto (online), y pregunta cuál de ellos se ejecuta de forma local ("locally").

2. Password cracking

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Which type of password attack is performed locally? | `Password cracking` |

---

### Task 3: Herramientas para servicios de red / Tools for Network Services

**Explicación:**
Se utiliza el módulo auxiliar de Metasploit `auxiliary/scanner/telnet/telnet_version` contra el ISG (Juniper). La pregunta pide las credenciales por defecto de un Juniper ISG 2000.

3. netscreen:netscreen

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | What are the default credentials for a Juniper ISG 2000? | `netscreen:netscreen` |

---

### Task 4: Generando diccionarios / Generating Wordlists

**Explicación:**
Uso de `crunch` para generar wordlists personalizadas. Se calcula el tamaño de un diccionario con patrones específicos y se usa la sintaxis `-t` con un "placeholder" `^` para caracteres desconocidos.

4. 1. 81
   2. crunch 5 5 -t "THM^^" -o tryhackme.txt

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | 1. What is the size of the wordlist? | `81` |
| 4 | 2. Generate a wordlist based on the syntax `THM^^`. What command should be used? | `crunch 5 5 -t "THM^^" -o tryhackme.txt` |

---

### Task 5: Identificación de hashes / Hash Identification

**Explicación:**
La tarea usa la herramienta `hashid` para identificar el tipo de hash y luego se crackean: la primera pregunta pide el formato identificado, la segunda la contraseña de un hash concreto (MD5), y la tercera el flag que se obtiene al crackear un tercer hash.

5. 1. sha-1
   2. sunshine
   3. 1337

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5 | 1. Which format is the hash? | `sha-1` |
| 5 | 2. What is the password? | `sunshine` |
| 5 | 3. What is the flag? | `1337` |

---

### Task 6: Reglas en Hashcat / Hashcat Rules

**Explicación:**
Se crea una regla personalizada para Hashcat que fuerza un patrón de contraseña concreto: dos letras mayúsculas, dos dígitos y un carácter especial al final. La pregunta pide la regla exacta.

6. Az"[0-9][0-9]" ^[!@]

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | What rule should be specified to add two numbers and a special character at the end? | `Az"[0-9][0-9]" ^[!@]` |

---

### Task 7: Post-explotación: menor privilegio / Post-exploitation: least privilege

**Explicación:**
Parte teórica que explica los principios de menor privilegio a aplicar después de obtener acceso. No requiere respuesta.

7. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 7 | No answer needed | `No answer needed` |

---

### Task 8: Caso de práctica: IBM Lotus / Practical: IBM Lotus

**Explicación:**
Escenario práctico completo sobre un servidor IBM Lotus dominotes: se aplica un diccionario personalizado sobre el formulario de login (técnica de brute-forcing de credenciales por "blind cURL"), se validan las credenciales en FTP y se aplican reglas. Las respuestas son el flag de la aplicación, la contraseña de la cuenta objetivo y los flags obtenidos al terminar los ataques.

8. 1. THM{d0abe799f25738ad739c20301aed357b}
   2. !multidisciplinary00
   3. THM{33c5d4954da881814420f3ba39772644}
   4. THM{f8e3750cc0ccbb863f2706a3b2933227}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 8 | 1. What is the web app's flag? | `THM{d0abe799f25738ad739c20301aed357b}` |
| 8 | 2. What is the password? | `!multidisciplinary00` |
| 8 | 3. What is the flag? | `THM{33c5d4954da881814420f3ba39772644}` |
| 8 | 4. The last flag has another format. Look for its value. | `THM{f8e3750cc0ccbb863f2706a3b2933227}` |

---

### Task 9: Password spraying contra SSH / Password Spraying against SSH

**Explicación:**
Aplicación del ataque de password spraying: probar una misma contraseña frente a muchos usuarios SSH para evitar los bloqueos por varios intentos fallidos. La pregunta pide el flag que se obtiene tras acceder.

9. THM{a97a26e86d09388bbea148f4b870277d}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 9 | What is the flag? | `THM{a97a26e86d09388bbea148f4b870277d}` |

---

### Task 10: Conclusión / Conclusion

**Explicación:**
Cierre de la sala con un resumen de lo aprendido. No requiere respuesta.

10. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 10 | No answer needed | `No answer needed` |

---

**Metodología:**

**Ataques offline (locales):** `hashid` / `hashcat --identify` para reconocer el formato → `hashcat -m <modo> hash.txt wordlist` (o `john --wordlist`) → reglas (`-r`) y máscaras para ampliar el espacio de búsqueda.

**Generación de wordlists:** `crunch <min> <max> -t "patrón" -o salida.txt` con `@`, `,`, `%` y `^` como placeholders de minúsculas, mayúsculas, números y cualquier carácter respectivamente; `-d` para repeticiones; `-s` para el valor inicial; y PPS para conocer el tamaño en bytes iniciales.

**Identificación de credenciales por defecto:** catálogo de devices (p.ej. Juniper ISG 2000: `netscreen:netscreen`) con módulos auxiliares de Metasploit (FTP/Telnet/SSH).

**Ataques online:** Hydra (FTP, RDP, SSH, Web-Forms...) y "blind cURL" para brute-forcing de formularios; ajustar el "Login Accepted" para saber cuándo una password es correcta; usar POST digest auth "401 Form-Based (Insecure)".

**Reglas de Hashcat:** transformaciones azules (`a`/`A`, `z`/`Z`, `$`, `^`), construcciones `Az"[0-9][0-9]" ^[!@]` para añadir números y caracteres especiales al final, y `#`/`"` para definir literales con símbolos.

**Password spraying:** una única contraseña probada contra muchos usuarios (evita el "account lockout"), idealmente sobre servicios como SSH con una lista de usuarios válidos.

### Cadena de ataque / Attack Chain

`Fase teoría (hashing, tipos de ataque local/remoto) → Cracking local: hashid → hashcat/john → Wordlist generation con crunch → Reglas de hashcat → Credenciales por defecto (Metasploit aux) → Password spraying (SSH) → Post-exploitation con menor privilegio`

**Learning chain:**

Conceptos base (qué es un hash, por qué el cracking funciona, salt y los tipos de ataque) → Herramientas: hashcat, john, hashid → Generación de diccionarios personalizados (crunch) → Reglas y máscaras (mutaciones) → Ataques a servicios de red (default creds, fuerza bruta FTP/formularios con Hydra/cURL) → Password spraying en SSH → Buenas prácticas post-explotación (least privilege).

*Lección:* Atacar contraseñas no es solo "echar rockyou": la diferencia entre éxito y fracaso la marcan la identificación correcta del formato de hash, las reglas de transformación bien afinadas y elegir el ataque online u offline adecuado. Además, el password spraying existe precisamente para eludir los bloqueos de cuenta que genera la fuerza bruta tradicional por usuario.

**MITRE ATT&CK:**

T1110.001 (Brute Force: Password Guessing), T1110.002 (Brute Force: Password Cracking), T1110.003 (Brute Force: Password Spraying), T1110.004 (Brute Force: Credential Stuffing), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Password Attacks](https://tryhackme.com/room/passwordattacks)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.