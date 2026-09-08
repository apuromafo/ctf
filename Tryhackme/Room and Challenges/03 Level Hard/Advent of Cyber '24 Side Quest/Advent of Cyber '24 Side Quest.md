# Advent of Cyber '24 Side Quest

| **Dificultad** | Hard |
| **Tipo** | CTF derivado del contenido |
| **Slug** | `adventofcyber24sidequest` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber24sidequest) |
| **Sección** | 03 Level Hard |
| **Fuente** | TryHackMe (Advent of Cyber 2024, serie Side Quest) |
| **Componentes** | Wireshark / Python / Binary Ninja / XXE / ROS / SSH / IDOR / zip2john / John the Ripper / frida-trace / RustScan / dig / netcat |
| **Impacto** | Serie de Side Quests de "The Frosty Five": recuperar las contraseñas robadas por Frostbite Fox, decodificar los flags YIN/YANG y comprometer tres máquinas hasta root para completar el ciclo del Advent of Cyber 2024. |

---

**Contexto:** El Side Quest del Advent of Cyber 2024 plantea cinco mini-CTF (Operation Tiny Frostbite, Yin and Yang, Escaping the Blizzard, Krampus Festival y An Avalanche of Web Apps) precedidos de tres tareas preparatorias. Cada reto requiere una keycard (L1-L5) oculta en las tareas del room principal de AoC 2024, con la que se desbloquea un ZIP, un firewall o un reto de juego. Se combina forense de PCAP y reversado de binarios para recuperar credenciales robadas, ofuscación y abuso de servicios (XXE/ROS, pwn por heap overflow, SQLi + macros con phishing y explotación de aplicaciones web) para escalar a root y cerrar la historia con un último flag.

## Solucionario

### Task 1: Introducción

**Explicación:** La serie Side Quest es una historia paralela al Advent of Cyber 2024. En las tareas 1-3 no hay retos propios: solo se explican las mecánicas (las keycards L1-L5 ocultas en los días del room principal) y las condiciones de desbloqueo de cada mini-juego.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 2: Keycard L1

**Explicación:** La keycard L1 se utiliza para el primer reto (T1: Operation Tiny Frostbite) y aparece apuntada en una de las tareas del AoC 2024 principal. Tarea informativa: no hay respuesta que enviar, solo disponer de la keycard en el entorno del Side Quest.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 3: Keycard L2

**Explicación:** La keycard L2 desbloquea el segundo reto (T2: Yin and Yang). Se encuentra igualmente oculta en el ciclo principal; tarea informativa.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 4: T1: Operation Tiny Frostbite

**Explicación:** En este reto el atacante Frostbite Fox intenta robar credenciales desde una máquina comprometida. Se analiza el tráfico de red con Wireshark (PCAP) y el binario `ff` con Binary Ninja/Python para reconstruir el ataque y extraer las cuatro respuestas, que son fragmentos base64 de una misma cadena: `QU9DMjAyNHtUaW55X1R` + `pbnlfVGlueV9TaDNsbF` + `9jYW5fRW5jcnlwVF9iVXR` + `faXRfSXNfTjB0X0YwMGxwcm8wZn0=` decodifica, concatenada, a `AoC2024{Tiny_T...}` (la password de McSkidy en la base de datos robada). Cada pregunta corresponde a: la password con la que el atacante se registró en el sitio, la password capturada del tráfico, la password del ZIP transferido y la password de la BD.

```bash
# análisis del tráfico
tshark -r capture.pcap
# descifrar fragmentos base64 del tráfico
echo 'QU9DMjAyNHtUaW55X1R...' | base64 -d
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password the attacker used to register on the site? | `QU9DMjAyNHtUaW55X1R` |
| 2 | What is the password that the attacker captured? | `pbnlfVGlueV9TaDNsbF` |
| 3 | What is the password of the zip file transferred by the attacker? | `9jYW5fRW5jcnlwVF9iVXR` |
| 4 | What is McSkidy's password that was inside the database file stolen by the attacker? | `faXRfSXNfTjB0X0YwMGxwcm8wZn0=` |

### Task 5: T2: Yin and Yang

**Explicación:** Two máquinas (yin y yang) conectadas por robots ROS. El XXE de una de las aplicaciones web revela los endpoints internos y servicios ROS; usando `rosservice call` se ejecutan comandos en los robots para leer los flags de `/root` de cada uno. Los flags juegan con la filosofía del yin-yang: ninguno puede existir sin el otro.

```text
rosservice list
rosservice call <service> 'cmd: ls /root'
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag for YIN? | `THM{Yin.cannot.exist.without.a.little.bit.of.Yang}` |
| 2 | What is the flag for YANG? | `THM{Yang.also.needs.Yin.to.survive}` |

### Task 6: T3: Escaping the Blizzard

**Explicación:** Se abusa de un IDOR para obtener la keycard L3, se explota el servicio de permisos del puerto 1337, y mediante un heap overflow clásico contra una versión reciente de glibc se consigue primero foothold, luego user y finalmente root. El ZIP protegido se rompe con zip2john + John the Ripper.

```bash
zip2john secret.zip > hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the content of the file foothold.txt? | `THM{th1s-1s-jusT-th3-B3g1nn1ng}` |
| 2 | What is the content of the file user.txt? | `THM{h4v1ng-fun-w1th-a-g00d-old-heap-overflowww-in-a-l4t3st-gl1bc}` |
| 3 | What is the content of the file root.txt? | `THM{w00t-w00t-y0u-escap3-the-may0r-permits}` |

### Task 7: T4: Krampus Festival

**Explicación:** El evento Krampus Festival combina una app CCTV con bypass de login y SQLi (sqlmap) para bajar el firewall, la explotación de un share SMB (`ChristmasShare`) donde está la primera flag, phishing por SMTP con macros de Office (swaks a Snowflakes) y, para culminar, la escalada a NT AUTHORITY\SYSTEM vía Shadow Credentials (pywhisker + PKINIT), webshell ASP.NET y EfsPotato (impersonación de tokens, SeImpersonate).

```bash
# phishing con swaks
swaks --to snowflakes@elves --from elf@krampus --header "Subject: ..." --body @evil.doc
# SQLi
sqlmap -u "http://<ip>/cctv/?id=1" --batch --dbs
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the first flag found in the SMB share ChristmasShare? | `THM{unlock_the_door_to_darkness_0nly_f0r_the_brave}` |
| 2 | What is the value of the flag in the user's desktop (user.txt)? | `THM{krampu5_h00ked_y0ur_l00t}` |
| 3 | What is the value of the flag obtained after the privilege escalation to SYSTEM? | `THM{krampu5_&_p0tat0_5alad}` |

### Task 8: T5: An Avalanche of Web Apps

**Explicación:** El reto de aplicaciones web: se hackea el juego de Tron con frida-trace (hookeando funciones para obtener la keycard L5), se hace un DNS zone transfer, se aprovecha un npm-registry squatting con un paquete malicioso y se explota una RCE en una de las apps. Cuatro apps comprometidas = cuatro flags.

```bash
frida-trace -U -i "*open*" com.example.game
dig axfr @<dns-server> example.thm
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of flag 1? | `THM{09a3f8918a32ea38a2c833c98214336a}` |
| 2 | What is the value of flag 2? | `THM{647aff4143b04972ba816f040e9b81c2}` |
| 3 | What is the value of flag 3? | `THM{ff2e079bc7bc3eb925478aa5bc2466a6}` |
| 4 | What is the value of flag 4? | `THM{05a830d2f52649c96318cce20c562b63}` |

### Task 9: The End?

**Explicación:** Tras completar los cinco retos, el conjunto de flags revela el flag final de cierre, que juega con el "bigger and meaner 2025" del anuncio del siguiente Advent of Cyber.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag revealed after completing all five challenges? | `THM{bigger_and_maybe_not_as_mean_in_2025}` |

---

**Metodología:**
1. Localizar las keycards L1-L5 ocultas en los días del room principal de AoC 2024 para desbloquear cada reto del Side Quest.
2. T1: escanear el host y analizar el PCAP (Wireshark) junto al binario `ff` (Binary Ninja) para extraer el secreto, descifrar el tráfico robado y leer la base de datos SQL de McSkidy (4 respuestas en base64).
3. T2: pivotar entre las máquinas yin/yang usando el XXE que revela los endpoints y los servicios ROS; ejecutar comandos vía `rosservice` para obtener los flags de `/root` en ambas.
4. T3: encontrar la keycard vía IDOR, explotar el servicio de permisos del puerto 1337 y encadenar la crack del ZIP (zip2john + `enc`) y el heap overflow de glibc hasta foothold, user y root.
5. T4: abrir la app CCTV (bypass de login + SQLi con sqlmap) para bajar el firewall, explotar SMB/SMTP (phishing con macros a Snowflakes, swaks), y escalar con Shadow Credentials (pywhisker/PKINIT), webshell ASP.NET y EfsPotato hasta NT AUTHORITY\SYSTEM.
6. T5: juego hacking con frida-trace para la keycard, DNS zone transfer, npm-registry squatting y RCE contra las aplicaciones web para las 4 flags; cerrar con el flag final.

**Learning chain:** `Keycards AoC → análisis de PCAP/reversado → credenciales robadas → XXE/ROS → pwn glibc → SQLi+macros → Shadow Credentials → SeImpersonate → flags → The End`

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1555 (Credentials from Password Stores), T1203 (Exploitation for Client Execution), T1078 (Valid Accounts), T1068 (Exploitation for Privilege Escalation), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Advent of Cyber '24 Side Quest](https://tryhackme.com/room/adventofcyber24sidequest)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
