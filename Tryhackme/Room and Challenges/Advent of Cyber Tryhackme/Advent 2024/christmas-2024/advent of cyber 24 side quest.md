# Advent of Cyber '24 Side Quest

| **Dificultad** | N/A | **Tipo** | CTF (Free Room) | **Slug** | dventofcyber24sidequest | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber24sidequest) | | **Seccion** | Advent of Cyber Tryhackme / Advent 2024 Side Quest | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | OSINT / Crypto / Web / Pwn / Forensics / CTF Final | | **Impacto** | Side Quest complementario del AoC 2024 con retos de ofensiva y defensiva |

---

**Contexto:** Room Side Quest del Advent of Cyber 2024 con 13 preguntas de diversa dificultad que cubren OSINT, criptografia, web exploitation, pwn (heap overflow, privilege escalation), forensics y CTF de salida. Cada pregunta corresponde a un desafio independiente dentro del Side Quest.

---

## Solucionario

### Task 1: OSINT - Credenciales

**Explicacion:** Analisis de credenciales encontradas en el entorno del Side Quest, incluyendo passwords codificadas en base64 y valores de archivos comprometidos.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the password the attacker used to register on the site? | QU9DMjAyNHtUaW55X1R |
| 2 | What is the password that the attacker captured? | pbnlfVGlueV9TaDNsbF |
| 3 | What is the password of the zip file transferred by the attacker? | 9jYW5fRW5jcnlwVF9iVXR |
| 4 | What is McSkidy's password that was inside the database file stolen by the attacker? | aXRfSXNfTjB0X0YwMGxwcm8wZn0= |

### Task 2: CTF - Yin Yang

**Explicacion:** Desafio de CTF con tematica Yin/Yang que evalua comprension de conceptos complementarios en ciberseguridad.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 5 | What is the flag for YIN? | THM{Yin.cannot.exist.without.a.little.bit.of.Yang} |
| 6 | What is the flag for YANG? | THM{Yang.also.needs.Yin.to.survive} |

### Task 3: Pwn - Heap Overflow

**Explicacion:** Desafio de pwn que involucra heap overflow en libc reciente, exploit development con GDB/GEF, y escalation de privilegios hasta root. Los archivos foothold.txt, user.txt y root.txt contienen las flags de cada nivel.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 7 | What is the content of the file foothold.txt? | THM{th1s-1s-jusT-th3-B3g1nn1ng} |
| 8 | What is the content of the file user.txt? | THM{h4v1ng-fun-w1th-a-g00d-old-heap-overflowww-in-a-l4t3st-gl1bc} |
| 9 | What is the content of the file root.txt? | THM{w00t-w00t-y0u-escap3-the-may0r-permits} |

### Task 4: Web - Foothold

**Explicacion:** Desafio web que requiere encontrar un foothold inicial, escalar a user y finalmente a root en un entorno Linux.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 10 | What is the content of flag.txt? | THM{unlock_the_door_to_darkness_0nly_f0r_the_brave} |
| 11 | What is the content of user.txt? | THM{krampu5_h00ked_y0ur_l00t} |
| 12 | What is the content of root.txt? | THM{krampu5_&_p0tat0_5alad} |

### Task 5: Forensics - Malware Analysis

**Explicacion:** Analisis forense de muestras de malware con 4 flags que cubren diferentes tecnicas de deteccion y analisis.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 13 | What is the value of flag 1? | THM{09a3f8918a32ea38a2c833c98214336a} |
| 14 | What is the value of flag 2? | THM{647aff4143b04972ba816f040e9b81c2} |
| 15 | What is the value of flag 3? | THM{ff2e079bc7bc3eb925478aa5bc2466a6} |
| 16 | What is the value of flag 4? | THM{05a830d2f52649c96318cce20c562b63} |

### Task 6: Encuesta

**Explicacion:** Encuesta de cierre del Side Quest AoC 2024.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 17 | What is the flag you get at the end of the survey? Please make sure to copy the flag before closing the tab! | THM{bigger_and_maybe_not_as_mean_in_2025} |

---

**Metodologia:**

1. OSINT y recopilacion de credenciales del entorno

2. CTF tematico (Yin/Yang)

3. Pwn y exploit development (heap overflow)

4. Web exploitation

5. Forensics y malware analysis

6. Encuesta de cierre

**Learning chain:** OSINT -> Crypto -> Pwn -> Web -> Forensics -> CTF Final

**Leccion:** *Los Side Quests del AoC complementan las areas de conocimiento cubiertas en el reto principal, incluyendo OSINT, criptografia, pwn y forensics.*

**MITRE ATT&CK:**

- T1592 - Gather Victim Host Information

- T1078 - Valid Accounts

- T1059 - Command and Scripting Interpreter

**Fuente:** [TryHackMe - Advent of Cyber 24 Side Quest](https://tryhackme.com/room/adventofcyber24sidequest)