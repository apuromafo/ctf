# Scheme Catcher

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Insane | challenge | `sq2-aoc2025-JxiOKUSD9R` | [TryHackMe](https://tryhackme.com/room/sq2-aoc2025-JxiOKUSD9R) | Advent of Cyber 2025 (Side Quest 2) | THM | binary analysis, beacon, XOR, UAF heap, kernel module | Muy alto — análisis completo de malware binario, explotación de kernel y persistencia avanzada |

---

**Contexto:** El Side Quest 2 de Advent of Cyber 2025 sumerge al jugador en un desafío de análisis de binarios y explotación de bajo nivel. Se debe examinar un archivo beacon.bin oculto en un KeePass, descifrar payloads con XOR, explotar vulnerabilidades UAF en heap y finalmente escalonar privilegios a root mediante un módulo de kernel. Cada etapa desbloquea la siguiente, simulando una cadena de compromiso real.

> **ES:** El Side Quest 2 de Advent of Cyber 2025 es un desafío de ingeniería inversa y explotación de bajo nivel: extraer la clave de un KeePass, analizar beacon.bin, descifrar payloads XOR, explotar una UAF en heap y escalar a root con un módulo de kernel.
> **EN:** Advent of Cyber 2025 Side Quest 2 is a low-level binary analysis and exploitation challenge: extracting the key from a KeePass, analyzing beacon.bin, decrypting XOR payloads, exploiting a heap UAF and escalating to root with a kernel module.

## Solucionario

### Task 1: Unlock

**Explicación:** La primera etapa consiste en desbloquear la base de datos de credenciales KeePass (.Passwords.kdbx). Se debe recuperar la clave de desbloqueo para acceder al archivo beacon.bin oculto y avanzar en la cadena.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Unlock key (KeePass .Passwords.kdbx) | `tit_for_tat` |

### Task 2: Binary Analysis & Exploitation

**Explicación:** Se analiza el binario beacon.bin con `strings` y herramientas de reversing para localizar flags y payloads ofuscados. Se descifran los strings con XOR, se explota la vulnerabilidad Use-After-Free (UAF) en heap para obtener foothold y user.txt, y finalmente se abusa de un módulo de kernel para escalar a root y obtener root.txt.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag hidden in the file? (strings of beacon.bin) | `THM{Welcom3_to_th3_eastmass_pwnland}` |
| 2 | What is the content of foothold.txt? | `THM{byp4ss_and_pack_is_pwn_you_n33d}` |
| 3 | What is the content of user.txt? | `THM{theres_someth1g_in_th3_w4t3r_that_cannot_l3ak}` |
| 4 | What is the content of root.txt? | `THM{final-boss_defeat3d-yay}` |

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1.1 | Unlock key (KeePass .Passwords.kdbx) | `tit_for_tat` |
| 2.1 | What is the flag hidden in the file? (strings of beacon.bin) | `THM{Welcom3_to_th3_eastmass_pwnland}` |
| 2.2 | What is the content of foothold.txt? | `THM{byp4ss_and_pack_is_pwn_you_n33d}` |
| 2.3 | What is the content of user.txt? | `THM{theres_someth1g_in_th3_w4t3r_that_cannot_l3ak}` |
| 2.4 | What is the content of root.txt? | `THM{final-boss_defeat3d-yay}` |

---

**Metodología:** Extracción de clave KeePass → análisis de beacon.bin con `strings` y herramientas de reversing → descifrado XOR de strings ofuscados → explotación de vulnerabilidad UAF (Use-After-Free) en heap → escalada de privilegios mediante módulo de kernel malicioso → obtención de flags en cada nivel de acceso.

### Cadena de ataque / Attack Chain

```text
KeePass (.Passwords.kdbx): tit_for_tat -> beacon.bin (strings) -> XOR decoding -> heap UAF exploitation -> foothold.txt -> user.txt -> kernel module abuse -> root.txt
```

**Learning chain:** KeePass DB extraction → binary RE → XOR decoding → heap exploitation → kernel module abuse → privilege escalation

**Lección:** *Un único archivo puede esconder una cadena de compromiso completa: desbloquear el contenedor inicial, ofuscar los payloads con XOR y explotar bug de bajo nivel (heap/kernel) encadenan acceso inicial, usuario y root.*

**MITRE ATT&CK:** T1027 (Obfuscated Files), T1059.004 (Unix Shell), T1068 (Exploitation for Privilege Escalation), T1547.006 (Kernel Modules and Extensions)

**Fuente:** [TryHackMe - Scheme Catcher](https://tryhackme.com/room/sq2-aoc2025-JxiOKUSD9R)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.