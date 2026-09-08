# Scheme Catcher

| **Dificultad** | INSANE | **Tipo** | CTF (Free Room) | **Slug** | `sq2-aoc2025-JxiOKUSD9R` | | **Link** | [TryHackMe](https://tryhackme.com/room/sq2-aoc2025-JxiOKUSD9R) | | **Seccion** | Advent of Cyber Tryhackme / Advent 2025 Side Quest 2 | | **Fuente** | walkthrough propio + [jaxafed — Side Quest Two](https://jaxafed.github.io/posts/tryhackme-aoc2025_sidequest_two/) + [djalilayed](https://github.com/djalilayed/tryhackme/tree/main/Advent_of_Cyber_Side_Quest_2025/Scheme_Catcher) + [id-root](https://github.com/id-root/Scheme-Catcher) | | **Componentes** | egg decode / nmap / fuzz / dev folder / beacon.bin / pwn / heap / strings / reverse engineering | | **Impacto** | El servidor guarda los secretos. Hopper guarda el rencor. Reto de pwn/heap con 4 flags (hidden, foothold, user, root) |

---

**Contexto:** The server holds the secrets. Hopper holds the grudge. Segundo Side Quest del Advent of Cyber 2025 de dificultad INSANE, enfocado en pwn (heap exploitation) con un servidor "Payload Storage Malhare's". Requiere egg decode, nmap, fuzzing, descubrir un folder `/dev`, analizar `beacon.bin`, y finalmente un heap exploitation.

**Egg Decode Password:** `tit_for_tat`

---

## Solucionario

### Task 1: Flag hidden in the file

**Explicacion:** Egg decode con password `tit_for_tat`. Luego `sudo nmap -sV -p22,80,9004,21337 -sS -T4 --min-rate 2000 -n -Pn 10.66.147.238`. Puertos abiertos: 22 (ssh OpenSSH 9.6p1 Ubuntu), 80 (http Apache 2.4.58 Ubuntu), 9004 (unknown - "Payload Storage Malhare's"), 21337 (http Werkzeug 3.0.1 Python). El puerto 9004 muestra el banner "Payload Storage Malhare's Version 4.2.0" con menu `[1] C: [2] U: [3] D: [4] E:`. Hay un folder `/dev` en el puerto 80. Se ejecuta `./beacon.bin`, Enter key: `EastMass` -> "Hello EastMass! Access granted! Starting socket server... Socket server listening on port 4444...". Leyendo los strings se obtiene la flag 1.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | What is the flag hidden in the file? | `THM{Welcom3_to_th3_eastmass_pwnland}` |

### Task 2: Content of foothold.txt

**Explicacion:** Sobre `tmp` en strings se puede usar como patron para entrar a un folder. El folder tiene otro binario `/7ln6Z1X***` y un file para la flag 2. El siguiente paso es pwn en local y despues en remoto.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 2 | What is the content of foothold.txt? | `THM{byp4ss_and_pack_is_pwn_you_n33d}` |

### Task 3: Content of user.txt

**Explicacion:** Analisis del binario (decompilacion del menu): las funciones son `create()` (malloc), `update()` (read offset), `delete()` (free), `menu()`. El programa permite `[1] C:` create, `[2] U:` update, `[3] D:` delete, `[4] E:` exit. Heap exploitation: el `update()` escribe `chunks[opt] + v2` (offset) con `sizes[opt] - v2` bytes (vulnerabilidad de heap overflow/corruption) y el `delete()` hace `free()` sin UAF check robusto. Condiciones: `opt <= 0xF8 && chunks[opt]`. Referencias de heap exploitation (leakless): `https://corgi.rip/posts/leakless_heap_1/` y `https://github.com/corgeman/leakless_research/`.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 3 | What is the content of user.txt? | `THM{theres_someth1g_in_th3_w4t3r_that_cannot_l3ak}` |

### Task 4: Content of root.txt

**Explicacion:** Escalada final tras el heap exploitation completo.

| # | Pregunta | Respuesta |
| --- | --- | --- |
| 4 | What is the content of root.txt? | `THM{final-boss_defeat3d-yay}` |

---

**Metodologia:**

1. Egg decode (password `tit_for_tat`)

2. Nmap scan de puertos 22,80,9004,21337

3. fuzz del puerto 80; descubrir `/dev` folder

4. Ejecutar `beacon.bin` con key `EastMass`

5. Leer strings para flag 1

6. Descubrir folder `/7ln6Z1X***` con binario y flag 2

7. Heap exploitation del "Payload Storage" (create/update/delete) local y remoto

8. Compilacion de las 4 flags

**Learning chain:** Egg Decode -> Nmap -> fuzz -> `/dev` -> beacon.bin -> strings -> Heap Exploitation -> 4 Flags

**Leccion:** *La explotacion de heap (create/update/delete con free/UAF y offsets) permite obtener compromiso total incluso en retos de dificultad INSANE; las referencias leakless_heap son clave.*

**MITRE ATT&CK:**

- T1210 - Exploitation of Remote Services

- T1068 - Exploitation for Privilege Escalation

- T1059 - Command and Scripting Interpreter

- T1190 - Exploit Public-Facing Application

**Fuente:** [TryHackMe - Scheme Catcher](https://tryhackme.com/room/sq2-aoc2025-JxiOKUSD9R)