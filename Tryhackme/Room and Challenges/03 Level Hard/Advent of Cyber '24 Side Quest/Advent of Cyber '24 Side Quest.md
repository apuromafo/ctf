# Advent of Cyber '24 Side Quest

| **Dificultad** | Hard |
| **Tipo** | CTF derivado del contenido |
| **Slug** | `adventofcyber24sidequest` |
| **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber24sidequest) |
| **Sección** | 03 Level Hard |
| **Fuente** | TryHackMe (Advent of Cyber 2024, serie Side Quest) |
| **Componentes** | Wireshark / Python / Binary Ninja / XXE / ROS / SSH / IDOR / zip2john / John the Ripper / frida-trace / RustScan / dig / netcat |

**Impacto** | Serie de Side Quests de "The Frosty Five": recuperar las contraseñas robadas por Frostbite Fox, decodificar los flags YIN/YANG y comprometer tres máquinas hasta root para completar el ciclo del Advent of Cyber 2024. |

---

**Contexto:** El Side Quest del Advent of Cyber 2024 plantea cinco mini-CTF (Operation Tiny Frostbite, Yin and Yang, Escaping the Blizzard, Krampus Festival y An Avalanche of Web Apps) precedidos de tres tareas preparatorias. Cada reto requiere una keycard (L1-L5) oculta en las tareas del room principal de AoC 2024, con la que se desbloquea un ZIP, un firewall o un reto de juego. Se combina forense de PCAP y reversado de binarios para recuperar credenciales robadas, ofuscación y abuso de servicios (XXE/ROS, pwn por heap overflow, SQLi + macros con phishing y explotación de aplicaciones web) para escalar a root y cerrar la historia con un último flag.

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 2: Keycard L1

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 3: Keycard L2

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 4: T1: Operation Tiny Frostbite

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password the attacker used to register on the site? | `QU9DMjAyNHtUaW55X1R` |
| 2 | What is the password that the attacker captured? | `pbnlfVGlueV9TaDNsbF` |
| 3 | What is the password of the zip file transferred by the attacker? | `9jYW5fRW5jcnlwVF9iVXR` |
| 4 | What is McSkidy's password that was inside the database file stolen by the attacker? | `faXRfSXNfTjB0X0YwMGxwcm8wZn0=` |

### Task 5: T2: Yin and Yang

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag for YIN? | `THM{Yin.cannot.exist.without.a.little.bit.of.Yang}` |
| 2 | What is the flag for YANG? | `THM{Yang.also.needs.Yin.to.survive}` |

### Task 6: T3: Escaping the Blizzard

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the content of the file foothold.txt? | `THM{th1s-1s-jusT-th3-B3g1nn1ng}` |
| 2 | What is the content of the file user.txt? | `THM{h4v1ng-fun-w1th-a-g00d-old-heap-overflowww-in-a-l4t3st-gl1bc}` |
| 3 | What is the content of the file root.txt? | `THM{w00t-w00t-y0u-escap3-the-may0r-permits}` |

### Task 7: T4: Krampus Festival

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the first flag found in the SMB share ChristmasShare? | `THM{unlock_the_door_to_darkness_0nly_f0r_the_brave}` |
| 2 | What is the value of the flag in the user's desktop (user.txt)? | `THM{krampu5_h00ked_y0ur_l00t}` |
| 3 | What is the value of the flag obtained after the privilege escalation to SYSTEM? | `THM{krampu5_&_p0tat0_5alad}` |

### Task 8: T5: An Avalanche of Web Apps

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of flag 1? | `THM{09a3f8918a32ea38a2c833c98214336a}` |
| 2 | What is the value of flag 2? | `THM{647aff4143b04972ba816f040e9b81c2}` |
| 3 | What is the value of flag 3? | `THM{ff2e079bc7bc3eb925478aa5bc2466a6}` |
| 4 | What is the value of flag 4? | `THM{05a830d2f52649c96318cce20c562b63}` |

### Task 9: The End?

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