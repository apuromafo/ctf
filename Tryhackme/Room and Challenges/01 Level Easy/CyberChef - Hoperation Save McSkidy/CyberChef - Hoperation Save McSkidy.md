# CyberChef - Hoperation Save McSkidy

| **Dificultad** | Medium |
| **Tipo** | walkthrough |
| **Slug** | `encoding-decoding-aoc2025-s1a4z7x0c3` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/encoding-decoding-aoc2025-s1a4z7x0c3) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | CyberChef, encoding/decoding, passwords, locks |
| **Impacto** | N/A |

---

**Contexto:** En esta sala del Advent of Cyber 2025 (Día 17), el equipo de McSkidy necesita recuperar un objeto codificado mediante una serie de candillos protegidos por contraseñas. Cada lock requiere decodificar la información con las operaciones adecuadas en CyberChef para avanzar hasta el flag final.

## Solucionario

### Task 1: Day 17 - CyberChef

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password for the first lock? | `Iamsofluffy` |
| 2 | What is the password for the second lock? | `Itoldyoutochangeit!` |
| 3 | What is the password for the third lock? | `BugsBunny` |
| 4 | What is the password for the fourth lock? | `passw0rd1` |
| 5 | What is the password for the fifth lock? | `51rBr34chBl0ck3r` |
| 6 | What is the retrieved flag? | `THM{M3D13V4L_D3C0D3R_4D3P7}` |

---

**Metodología:** Se utilizaron operaciones de decodificación en CyberChef (Base64, ROT13, Hex, Binary, etc.) para descifrar cada contraseña de los candillos, aplicando el pie de claves correctamente hasta obtener la contraseña final y el flag.

**Learning chain:** encoding → decoding → CyberChef operations → password cracking → flag extraction

**MITRE ATT&CK:** N/A

**Fuente:** [TryHackMe - CyberChef - Hoperation Save McSkidy](https://tryhackme.com/r/room/encoding-decoding-aoc2025-s1a4z7x0c3)