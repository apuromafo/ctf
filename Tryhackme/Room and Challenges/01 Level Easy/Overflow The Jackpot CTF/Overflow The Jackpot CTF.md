# Overflow The Jackpot CTF

| **Dificultad** | Medium |
| **Tipo** | challenge |
| **Slug** | `thm-ctf-jackpot-overflow` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/thm-ctf-jackpot-overflow) |
| **Sección** | CTF |
| **Fuente** | THM |
| **Componentes** | crypto, web, forensics, detection engineering, boot2root |
| **Impacto** | Resolución completa de los 5 retos del CTF DEF CON |

---

**Contexto:** "Overflow The Jackpot" es un CTF de la DEF CON que combina cinco desafíos independientes que recorren todo el ciclo ofensivo-defensivo: criptoanálisis, explotación web, forense de red, ingeniería de detección y un boot2root completo. Cada reto entrega una bandera que no está publicada públicamente, por lo que se documenta la metodología de resolución confirmada y las credenciales descubiertas durante la explotación.

## Solucionario

### Task 1: B1t Recovery (Crypto)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Recuperar la clave y descifrar la bandera cifrada | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Método confirmado:** Ataque de known-plaintext XOR. Dado que las banderas de TryHackMe comienzan con el prefijo `THM{`, alineamos ese texto conocido contra el ciphertext y recuperamos la clave de 4 bytes (repetida). Con la clave determinada, se descifra el resto del mensaje para obtener la bandera completa.

### Task 2: Lost Fortune Included (Web)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer el archivo de bandera del servidor | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Método confirmado:** El sitio es vulnerable a inclusión de archivos vía `php://filter`. Se abusó de `php://filter/convert.base64-encode/resource=...` para leer el contenido arbitrario del servidor, obteniendo así `/var/www/flag.txt` (bandera en base64 decodificada).

### Task 3: Casino Heist (Forensics)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descifrar la bandera exfiltrada en la captura de red | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Método confirmado:** Análisis de pcap: se identificó tráfico de exfiltración cifrado con AES-128-CBC. Claves recuperadas del tráfico: clave `J4ckp0tH4ck3rKey` e IV `Iv_For_Exf1ltr8!`. Con estos parámetros se descifró `flag.jackpot` contenido en la captura para recuperar la bandera.

### Task 4: Fresh Powder (Detection Engineering)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Crear las 5 reglas Sigma solicitadas para detección | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Método confirmado:** Se redactaron 5 pull requests (PR) con reglas Sigma que detectan la actividad maliciosa observada en los retos anteriores (exfiltración, webshells, movimientos laterales). Cada regla valida la detección frente a los logs de muestra antes de aceptar el PR.

### Task 5: Agent P (Boot2root)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | user.txt (/home/norm) | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |
| 2 | operator.txt (vanessa) | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |
| 3 | root.txt (root) | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Método confirmado:** Credenciales SSH norm: `N0rm_th3_r0b0t_2026`. A partir de la sesión de `norm` se accede al secreto del operador `b3hind_sch3dul3_th1s_m0nth` que permite moverse a la cuenta `vanessa`. Posteriormente se compromete el WordPress localizado con `wpuser/wp_WjURfdI` como vector para escalar a root. Las banderas `EVILINC{...}` se encuentran en `/home/norm` (user.txt), en la sesión de `vanessa` (operator.txt) y en `/root` (root.txt).

---

**Metodología:** CTF multicategoría: (1) criptoanálisis con ataque de texto conocido contra XOR; (2) explotación web mediante inclusión de archivos con wrappers PHP; (3) forense de red descifrando una exfiltración AES-128-CBC; (4) blue team construyendo reglas Sigma de detección; (5) boot2root con escalada de privilegios en Linux y abuso de WordPress.

**Learning chain:** Known-plaintext attack → php://filter LFI → análisis de pcap + descifrado AES → Sigma detection engineering → credential stuffing → privilege escalation Linux → root.

**MITRE ATT&CK:** T1190, T1000 (Data Exfiltration), T1213, T1078 (Valid Accounts), T1021 (Remote Services), T1068 (Exploitation for Privilege Escalation), T1106, T1059.

**Fuente:** [TryHackMe - Overflow The Jackpot CTF](https://tryhackme.com/r/room/thm-ctf-jackpot-overflow)
