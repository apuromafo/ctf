# Brainpan 1

| **Dificultad** | Hard |
| **Tipo** | Walkthrough |
| **Slug** | `brainpan` |
| **Link** | [TryHackMe](https://tryhackme.com/room/brainpan) |
| **Sección** | 03 Level Hard |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | abyss / SimpleHTTPServer / fuzzer / cyclic pattern / mona / msfvenom / meterpreter / /etc/passwd / buffer overflow |
| **Impacto** | Buffer overflow clásico sobre el servicio `abyss` (puerto 9999) con shellcode reverse y escalada a root aprovechando un `/etc/passwd` escritible. |

---

**Contexto:** Brainpan 1 es una sala clásica de buffer overflow (basada en la máquina Brainpan del VulnHub). No se capturan flags: el objetivo se mide por niveles de acceso. Un fuzzer encuentra el offset de EIP, el programa `brainpan.exe` revela la máquina Windows de desarrollo, y una shellcode explota el servicio `abyss` en el puerto 9999 para obtener acceso al sistema Linux y escalar a root.

## Solucionario

### Task 1: No se requiere respuesta

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

---

**Metodología:**
1. Escaneo de puertos: `9999` (`abyss`/Brainpan, pide contraseña) y `10000` (SimpleHTTPServer Python 2.7.3).
2. Enumeración web en el puerto 10000 → directorio `/bin` → se descarga `brainpan.exe`.
3. Fuzzing del servicio `9999`: el programa crashea a ~600 bytes; el desbordamiento ocurre entre 500 y 600 bytes.
4. Con un patrón cíclico se calcula el offset de EIP = `524` bytes.
5. Con `mona`/`!mona jmp esp` se obtiene la dirección `0x311712f3` (brainpan.exe) para el control de flujo.
6. Se usa `msfvenom` para generar shellcode de reverse shell (sin el badcharacter `\x00`) y se añade un NOP-sled.
7. Se envía el exploit con la shellcode `windows/meterpreter/reverse_tcp` → conexión como usuario `puck`.
8. Escalada de privilegios: `/etc/passwd` es escritible → se añade un usuario root con hash conocido → `su` → acceso root.

**Learning chain:** `nmap → 9999 (abyss) y 10000 (SimpleHTTPServer) → /bin → brainpan.exe → fuzzer (crash a 600 bytes) → offset de EIP (524) → JMP ESP (0x311712f3) → shellcode → reverse shell como puck → /etc/passwd escritible → root`

**MITRE ATT&CK:** T1210 (Exploitation of Remote Services), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Brainpan 1](https://tryhackme.com/room/brainpan)