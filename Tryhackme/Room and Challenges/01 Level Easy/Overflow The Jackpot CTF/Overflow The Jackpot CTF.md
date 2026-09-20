# Overflow The Jackpot CTF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | challenge | `thm-ctf-jackpot-overflow` | [TryHackMe](https://tryhackme.com/room/thm-ctf-jackpot-overflow) | `CTF` | THM | crypto, web, forensics, detection engineering, boot2root | Resolución completa de los 5 retos del CTF DEF CON |

> **Objeto:** Resolver los cinco desafíos independientes del CTF "Overflow The Jackpot" de la DEF CON: criptoanálisis, explotación web, forense de red, ingeniería de detección y boot2root, registrando la metodología y las credenciales descubiertas.

---

**Contexto:** "Overflow The Jackpot" es un CTF de la DEF CON que combina cinco desafíos independientes que recorren todo el ciclo ofensivo-defensivo: criptoanálisis, explotación web, forense de red, ingeniería de detección y un boot2root completo. Cada reto entrega una bandera que no está publicada públicamente, por lo que se documenta la metodología de resolución confirmada y las credenciales descubiertas durante la explotación.

> **ES:** "Overflow The Jackpot" es un CTF de la DEF CON que combina cinco desafíos independientes que recorren todo el ciclo ofensivo-defensivo: criptoanálisis, explotación web, forense de red, ingeniería de detección y un boot2root completo. Cada reto entrega una bandera que no está publicada públicamente, por lo que se documenta la metodología de resolución confirmada y las credenciales descubiertas durante la explotación.

> **EN:** "Overflow The Jackpot" is a DEF CON CTF that combines five independent challenges spanning the entire offensive-defensive cycle: cryptanalysis, web exploitation, network forensics, detection engineering and a full boot2root. Each challenge delivers a flag that is not publicly published, so the confirmed solving methodology and the credentials discovered during exploitation are documented.

## Solucionario

### Task 1: B1t Recovery (Crypto) / B1t Recovery (Crypto)

**Explicación:** Reto de criptoanálisis para recuperar la clave y descifrar la bandera cifrada mediante un ataque de texto conocido.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Recuperar la clave y descifrar la bandera cifrada | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Método confirmado:** Ataque de known-plaintext XOR. Dado que las banderas de TryHackMe comienzan con el prefijo `THM{`, alineamos ese texto conocido contra el ciphertext y recuperamos la clave de 4 bytes (repetida). Con la clave determinada, se descifra el resto del mensaje para obtener la bandera completa.

### Task 2: Lost Fortune Included (Web) / Lost Fortune Included (Web)

**Explicación:** Reto de explotación web consistente en leer el archivo de bandera del servidor mediante inclusión de ficheros con wrappers PHP.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer el archivo de bandera del servidor | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Método confirmado:** El sitio es vulnerable a inclusión de archivos vía `php://filter`. Se abusó de `php://filter/convert.base64-encode/resource=...` para leer el contenido arbitrario del servidor, obteniendo así `/var/www/flag.txt` (bandera en base64 decodificada).

### Task 3: Casino Heist (Forensics) / Casino Heist (Forensics)

**Explicación:** Reto de forense de red centrado en descifrar la bandera exfiltrada en una captura de tráfico cifrada con AES-128-CBC.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descifrar la bandera exfiltrada en la captura de red | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Método confirmado:** Análisis de pcap: se identificó tráfico de exfiltración cifrado con AES-128-CBC. Claves recuperadas del tráfico: clave `J4ckp0tH4ck3rKey` e IV `Iv_For_Exf1ltr8!`. Con estos parámetros se descifró `flag.jackpot` contenido en la captura para recuperar la bandera.

### Task 4: Fresh Powder (Detection Engineering) / Fresh Powder (Detection Engineering)

**Explicación:** Reto de blue team: crear las 5 reglas Sigma solicitadas para detectar la actividad maliciosa observada en los retos anteriores.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Crear las 5 reglas Sigma solicitadas para detección | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Método confirmado:** Se redactaron 5 pull requests (PR) con reglas Sigma que detectan la actividad maliciosa observada en los retos anteriores (exfiltración, webshells, movimientos laterales). Cada regla valida la detección frente a los logs de muestra antes de aceptar el PR.

### Task 5: Agent P (Boot2root) / Agent P (Boot2root)

**Explicación:** Reto de compromiso total del sistema (boot2root) con tres banderas en diferentes niveles de privilegio (user, operator y root), apoyado en credenciales descubiertas y en un WordPress vulnerable.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | user.txt (/home/norm) | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |
| 2 | operator.txt (vanessa) | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |
| 3 | root.txt (root) | Requiere explotación en vivo (flag redactada en los walkthroughs públicos) |

**Método confirmado:** Credenciales SSH norm: `N0rm_th3_r0b0t_2026`. A partir de la sesión de `norm` se accede al secreto del operador `b3hind_sch3dul3_th1s_m0nth` que permite moverse a la cuenta `vanessa`. Posteriormente se compromete el WordPress localizado con `wpuser/wp_WjURfdI` como vector para escalar a root. Las banderas `EVILINC{...}` se encuentran en `/home/norm` (user.txt), en la sesión de `vanessa` (operator.txt) y en `/root` (root.txt).

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Recuperar la clave y descifrar la bandera cifrada (B1t Recovery) | `Requiere explotación en vivo (flag redactada en los walkthroughs públicos)` |
| 2 | Leer el archivo de bandera del servidor (Lost Fortune Included) | `Requiere explotación en vivo (flag redactada en los walkthroughs públicos)` |
| 3 | Descifrar la bandera exfiltrada en la captura de red (Casino Heist) | `Requiere explotación en vivo (flag redactada en los walkthroughs públicos)` |
| 4 | Crear las 5 reglas Sigma solicitadas para detección (Fresh Powder) | `Requiere explotación en vivo (flag redactada en los walkthroughs públicos)` |
| 5 | user.txt (/home/norm) | `Requiere explotación en vivo (flag redactada en los walkthroughs públicos)` |
| 6 | operator.txt (vanessa) | `Requiere explotación en vivo (flag redactada en los walkthroughs públicos)` |
| 7 | root.txt (root) | `Requiere explotación en vivo (flag redactada en los walkthroughs públicos)` |

---

**Metodología:** CTF multicategoría: (1) criptoanálisis con ataque de texto conocido contra XOR; (2) explotación web mediante inclusión de archivos con wrappers PHP; (3) forense de red descifrando una exfiltración AES-128-CBC; (4) blue team construyendo reglas Sigma de detección; (5) boot2root con escalada de privilegios en Linux y abuso de WordPress.

### Cadena de ataque / Attack Chain

1. Criptoanálisis: known-plaintext XOR con prefijo `THM{` → clave de 4 bytes.
2. Web: inclusión de ficheros vía `php://filter` → `/var/www/flag.txt`.
3. Forense: pcap → exfiltración AES-128-CBC → descifrado con `J4ckp0tH4ck3rKey` / `Iv_For_Exf1ltr8!`.
4. Detección: 5 reglas Sigma aprobadas por PR frente a logs de muestra.
5. Boot2root: SSH `N0rm_th3_r0b0t_2026` → secreto `b3hind_sch3dul3_th1s_m0nth` → `vanessa` → WordPress `wpuser/wp_WjURfdI` → root.

**Learning chain:** Known-plaintext attack → php://filter LFI → análisis de pcap + descifrado AES → Sigma detection engineering → credential stuffing → privilege escalation Linux → root.

**Lección:** *Los CTF multicategoría exigen encadenar criptoanálisis, explotación web, forense de red, detección y escalada de privilegios: cada bandera valida una fase distinta del ciclo ofensivo-defensivo y las credenciales se reutilizan como palanca entre retos.*

**MITRE ATT&CK:** T1190, T1000 (Data Exfiltration), T1213, T1078 (Valid Accounts), T1021 (Remote Services), T1068 (Exploitation for Privilege Escalation), T1106, T1059.

**Fuente:** [TryHackMe - Overflow The Jackpot CTF](https://tryhackme.com/room/thm-ctf-jackpot-overflow)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.