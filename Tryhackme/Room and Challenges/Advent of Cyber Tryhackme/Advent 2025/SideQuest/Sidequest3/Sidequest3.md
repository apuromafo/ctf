# Carrotbane of My Existence

| **Dificultad** | MEDIUM | **Tipo** | CTF (Free Room) | **Slug** | sq3-aoc2025-bk3vvbcgiT | | **Link** | [TryHackMe](https://tryhackme.com/room/sq3-aoc2025-bk3vvbcgiT) | | **Seccion** | Advent of Cyber Tryhackme / Advent 2025 Side Quest 3 | | **Fuente** | walkthrough propio + [0xb0b GitBook](https://0xb0b.gitbook.io/writeups/tryhackme/2025/advent-of-cyber-25-side-quest/carrotbane-of-my-existence) + [djalilayed Medium](https://medium.com/@jalilayed/tryhackme-carrotbane-of-my-existence-walk-through-e6e80a4d51df) + [id-root](https://github.com/id-root/Carrotbane-of-My-Existence) | | **Componentes** | investigacion / levantamiento / osint / forensics | | **Impacto** | Investigacion profunda para detener el levantamiento liderado por Hopper con 4 flags de dificultad creciente |

---

**Contexto:** Hopper's uprising is just getting started. En este reto de Advent of Cyber 2025, nos enfrentamos a una investigacion profunda para detener el levantamiento liderado por Hopper. Se debe acceder con la password del egg decode:

**Egg Decode Password:** one_hopper_army`r

---

## Solucionario

### Task 1: Flag 1

**Explicacion:** Primera flag obtenida tras el egg decode con password one_hopper_army y analisis inicial del entorno.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | Flag 1 | THM{9cd687b330554bd807a717e62910e3d0} |

### Task 2: Flag 2

**Explicacion:** Segunda flag tras enumeracion y explotacion de vulnerabilidades en el entorno del asilo.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 2 | Flag 2 | THM{39564de94a133349e3d76a91d3f0501c} |

### Task 3: Flag 3

**Explicacion:** Tercera flag tras escalada de privilegios en el entorno comprometido.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 3 | Flag 3 | THM{3a07cd4e05ce03d953a22e90122c6a89} |

### Task 4: Flag 4

**Explicacion:** Cuarta flag como resultado final de la investigacion completa del levantamiento de Hopper.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 4 | Flag 4 | THM{e116666ffb7fcfadc7e6136ca30f75bf} |

---

**Metodologia:**

1. Egg Decode con password one_hopper_army`r

2. Enumeracion del entorno del asilo

3. Explotacion de vulnerabilidades

4. Escalada de privilegios

5. Investigacion del levantamiento de Hopper

6. Compilacion de las 4 flags

**Learning chain:** Egg Decode -> Enumeration -> Exploitation -> Privilege Escalation -> Investigation -> 4 Flags

**Leccion:** *Los retos de MEDIUM requieren combinacion de OSINT, enumeracion y explotacion para completar una investigacion completa de seguridad.*

**MITRE ATT&CK:**

- T1078 - Valid Accounts

- T1190 - Exploit Public-Facing Application

- T1068 - Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - Carrotbane of My Existence](https://tryhackme.com/room/sq3-aoc2025-bk3vvbcgiT)