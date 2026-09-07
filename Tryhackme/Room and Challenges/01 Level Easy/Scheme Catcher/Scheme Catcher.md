# Scheme Catcher

| **Dificultad** | Insane |
| **Tipo** | challenge |
| **Slug** | `sq2-aoc2025-JxiOKUSD9R` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/sq2-aoc2025-JxiOKUSD9R) |
| **Sección** | Advent of Cyber 2025 (Side Quest 2) |
| **Fuente** | THM |
| **Componentes** | binary analysis, beacon, XOR, UAF heap, kernel module |
| **Impacto** | Muy alto — análisis completo de malware binario, explotación de kernel y persistencia avanzada |

---

**Contexto:** El Side Quest 2 de Advent of Cyber 2025 sumerge al jugador en un desafío de análisis de binarios y explotación de bajo nivel. Se debe examinar un archivo beacon.bin oculto en un KeePass, descifrar payloads con XOR, explotar vulnerabilidades UAF en heap y finalmente escalonar privilegios a root mediante un módulo de kernel. Cada etapa desbloquea la siguiente, simulando una cadena de compromiso real.

## Solucionario

### Task 1: Unlock

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Unlock key (KeePass .Passwords.kdbx) | `tit_for_tat` |

### Task 2: Binary Analysis & Exploitation

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag hidden in the file? (strings of beacon.bin) | `THM{Welcom3_to_th3_eastmass_pwnland}` |
| 2 | What is the content of foothold.txt? | `THM{byp4ss_and_pack_is_pwn_you_n33d}` |
| 3 | What is the content of user.txt? | `THM{theres_someth1g_in_th3_w4t3r_that_cannot_l3ak}` |
| 4 | What is the content of root.txt? | `THM{final-boss_defeat3d-yay}` |

---

**Metodología:** Extracción de clave KeePass → análisis de beacon.bin con `strings` y herramientas de reversing → descifrado XOR de strings ofuscados → explotación de vulnerabilidad UAF (Use-After-Free) en heap → escalada de privilegios mediante módulo de kernel malicioso → obtención de flags en cada nivel de acceso.
**Learning chain:** KeePass DB extraction → binary RE → XOR decoding → heap exploitation → kernel module abuse → privilege escalation
**MITRE ATT&CK:** T1027 (Obfuscated Files), T1059.004 (Unix Shell), T1068 (Exploitation for Privilege Escalation), T1547.006 (Kernel Modules and Extensions)
**Fuente:** [TryHackMe - Scheme Catcher](https://tryhackme.com/r/room/sq2-aoc2025-JxiOKUSD9R)
