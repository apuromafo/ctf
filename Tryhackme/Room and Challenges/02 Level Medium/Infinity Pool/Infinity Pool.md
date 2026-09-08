# Infinity Pool

| **Dificultad** | MEDIUM | **Tipo** | CTF (Evento "Hacker Holidays 2026: The Byte Lotus Hotel") | **Slug** | `hh-infinitypool-5b3548af` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hh-infinitypool-5b3548af) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Linux PrivEsc / Capabilities / Web Exploitation / LFI / RCE / PATH Hijack | **Impacto** | Evalúa la escalada de privilegios Linux desde shell inicial hasta root |

---

**Contexto:** Sala de evento (Hacker Holidays 2026: The Byte Lotus Hotel) de dificultad Medium tipo **Linux / PrivEsc** sobre una VM. El tema "no visible edge" (borde no visible del hotel) orienta a servicios escuchando en puertos no estándar y a binarios con capabilities: enumeración web → shell inicial como usuario → escalada de privilegios (capabilities posix, PATH hijack o sudo) → flag root.

## Solucionario

### Task 1: Infinity Pool

**Explicación:** Tras la enumeration web se explota una superficie de entrada (LFI/RCE limitada) que entrega una shell inicial como usuario; ahí se lee la **user flag**. Para la escalada se revisan binarios con capabilities posix (p. ej. lectura arbitraria de archivos) o `sudo -l`/PATH hijack; con ello se lee la **root flag**. 2 preguntas. English: After web enumeration an entry surface (limited LFI/RCE) is exploited to get an initial shell as a user, where the **user flag** is read. For escalation, binaries with posix capabilities (e.g. arbitrary file read) or `sudo -l`/PATH hijack are reviewed; with that the **root flag** is read. 2 questions.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `THM{n0_v1s1bl3_3dg3}` |
| 2 | What is the root flag? | `THM{tr4c3d_t0_th3_h0r1z0n}` |

---

**Metodología:**
1. Enumeración: `nmap -sV -p-` y fuzzing web sobre el target; el tema "no visible edge" sugiere descubrir servicios escuchando en puertos altos/no estándar.
2. Acceso inicial: se explota una entrada web (LFI que escala a RCE limitada) y se obtiene una shell inicial como usuario no privilegiado.
3. User flag: en el directorio del usuario se lee `THM{n0_v1s1bl3_3dg3}`.
4. PrivEsc: se revisan binarios con capabilities posix (p. ej. `cap_dac_read_search`) y `sudo -l`; se abusa de una capability o de un PATH hijack/script con sudo para leer archivos de root.
5. Root flag: con acceso root se lee `THM{tr4c3d_t0_th3_h0r1z0n}`.

**Learning chain:** web (puertos no estándar, "no visible edge") → LFI/RCE limitada → shell inicial como usuario → user flag THM{n0_v1s1bl3_3dg3} → enumeration → binary con capabilities / sudo -l / PATH hijack → privEsc → root → root flag THM{tr4c3d_t0_th3_h0r1z0n}

**Lección:** *Revisar las capabilities de binarios (posix) y los servicios que escuchan en puertos altos: lo "invisible" desde una enumeración superficial suele ser la superficie real de ataque y de escalada.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application; T1068 - Exploitation for Privilege Escalation; T1548 - Abuse Elevation Control Mechanism; T1053 - Scheduled Task/Job

**Fuente:** [TryHackMe - Infinity Pool](https://tryhackme.com/room/hh-infinitypool-5b3548af)