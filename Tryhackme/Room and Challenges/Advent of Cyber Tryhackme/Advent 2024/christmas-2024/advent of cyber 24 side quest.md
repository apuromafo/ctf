# Advent of Cyber '24 Side Quest

| **Dificultad** | N/A | **Tipo** | CTF (Free Room) | **Slug** | `adventofcyber24sidequest` | | **Link** | [TryHackMe](https://tryhackme.com/room/adventofcyber24sidequest) | | **Sección** | Advent of Cyber Tryhackme / Advent 2024 Side Quest | | **Fuente** | texto oficial THM + anotaciones propias | | **Componentes** | OSINT / Crypto / Web / Pwn / Forensics / CTF Final | | **Impacto** | Side Quest complementario del AoC 2024 con retos de OSINT, criptografía, web exploitation, pwn, forensics y un CTF de salida |

---

**Contexto:** Room "Side Quest" del Advent of Cyber 2024 con 17 preguntas de diversa dificultad que cubren OSINT/credenciales, un CTF temático Yin/Yang, pwn (heap overflow y privilege escalation en glibc reciente), web exploitation y forensics/malware analysis, cerrando con la encuesta. Cada preguna corresponde a un desafío independiente dentro del Side Quest; el contenido original está en inglés y se añaden anotaciones propias en español.

---

## Solucionario

### Task 1: OSINT - Credenciales

**Explicación:** Análisis de credenciales encontradas en el entorno del Side Quest, incluyendo passwords codificadas en base64 y valores de archivos comprometidos. Las cuatro partes base64 se concatenan para reconstruir la contraseña de McSkidy extraída de la base de datos robada por el atacante.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the password the attacker used to register on the site? | `QU9DMjAyNHtUaW55X1R` |
| 2 | What is the password that the attacker captured? | `pbnlfVGlueV9TaDNsbF` |
| 3 | What is the password of the zip file transferred by the attacker? | `9jYW5fRW5jcnlwVF9iVXR` |
| 4 | What is McSkidy's password that was inside the database file stolen by the attacker? | `aXRfSXNfTjB0X0YwMGxwcm8wZn0=` |

### Task 2: CTF - Yin Yang

**Explicación:** Desafío de CTF con temática Yin/Yang que evalúa la comprensión de conceptos complementarios en ciberseguridad; se requieren ambas flags (YIN y YANG) para completar el reto.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 5 | What is the flag for YIN? | `THM{Yin.cannot.exist.without.a.little.bit.of.Yang}` |
| 6 | What is the flag for YANG? | `THM{Yang.also.needs.Yin.to.survive}` |

### Task 3: Pwn - Heap Overflow

**Explicación:** Desafío de pwn que involucra heap overflow en libc reciente, exploit development con GDB/GEF, y escalada de privilegios hasta root. Los archivos foothold.txt, user.txt y root.txt contienen las flags de cada nivel.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 7 | What is the content of the file foothold.txt? | `THM{th1s-1s-jusT-th3-B3g1nn1ng}` |
| 8 | What is the content of the file user.txt? | `THM{h4v1ng-fun-w1th-a-g00d-old-heap-overflowww-in-a-l4t3st-gl1bc}` |
| 9 | What is the content of the file root.txt? | `THM{w00t-w00t-y0u-escap3-the-may0r-permits}` |

### Task 4: Web - Foothold

**Explicación:** Desafío web que requiere encontrar un foothold inicial, escalar a user y finalmente a root en un entorno Linux, recopilando las flags de cada nivel.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 10 | What is the content of flag.txt? | `THM{unlock_the_door_to_darkness_0nly_f0r_the_brave}` |
| 11 | What is the content of user.txt? | `THM{krampu5_h00ked_y0ur_l00t}` |
| 12 | What is the content of root.txt? | `THM{krampu5_&_p0tat0_5alad}` |

### Task 5: Forensics - Malware Analysis

**Explicación:** Análisis forense de muestras de malware con 4 flags que cubren diferentes técnicas de detección y análisis (floss, strings, hashing y artefactos del binario).

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 13 | What is the value of flag 1? | `THM{09a3f8918a32ea38a2c833c98214336a}` |
| 14 | What is the value of flag 2? | `THM{647aff4143b04972ba816f040e9b81c2}` |
| 15 | What is the value of flag 3? | `THM{ff2e079bc7bc3eb925478aa5bc2466a6}` |
| 16 | What is the value of flag 4? | `THM{05a830d2f52649c96318cce20c562b63}` |

### Task 6: Encuesta

**Explicación:** Encuesta de cierre del Side Quest AoC 2024; entrega la flag final del reto. Conviene copiar la flag antes de cerrar la pestaña.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 17 | What is the flag you get at the end of the survey? Please make sure to copy the flag before closing the tab! | `THM{bigger_and_maybe_not_as_mean_in_2025}` |

---

**Metodología:**

1. OSINT y recopilación de credenciales del entorno (base64 concatenado)

2. CTF temático (Yin/Yang)

3. Pwn y exploit development (heap overflow + privilegios)

4. Web exploitation (foothold -> user -> root)

5. Forensics y malware analysis

6. Encuesta de cierre

**Learning chain:** OSINT -> Crypto -> Pwn -> Web -> Forensics -> CTF Final

**Lección:** *Los Side Quests del AoC complementan las áreas de conocimiento cubiertas en el reto principal, incluyendo OSINT, criptografía, pwn y forensics; requieren encadenar distintas disciplinas para conseguir el set completo de flags.*

**MITRE ATT&CK:**

- T1592 - Gather Victim Host Information

- T1078 - Valid Accounts

- T1059 - Command and Scripting Interpreter

- T1203 - Exploitation for Client Execution

**Fuente:** [TryHackMe - Advent of Cyber 24 Side Quest](https://tryhackme.com/room/adventofcyber24sidequest)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.