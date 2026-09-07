# Passwords - A Cracking Christmas

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `attacks-on-ecrypted-files-aoc2025-asdfghj123` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/attacks-on-ecrypted-files-aoc2025-asdfghj123) |
| **Sección** | Advent of Cyber 2025 |
| **Componentes** | John the Ripper, PDF cracking, ZIP cracking |
| **Impacto** | Cracking encrypted files using offline tools for credential/flag extraction |

---

**Contexto:** SOC-mas necesita recuperar archivos cifrados que contienen banderas de seguridad. Los archivos protegidos — un PDF y un ZIP — usan contraseñas débiles crackeables con John the Ripper. Un desafío clásico de cracked passwords en Navidad.

## Solucionario

### Task 1: Cracking Encrypted Files

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag inside the encrypted PDF? | `THM{Cr4ck1ng_PDFs_1s_34$y}` |
| 2 | What is the flag inside the encrypted zip file? | `THM{Cr4ck1n6_z1p$_1s_34$yyyy}` |

---

**Metodología:** Se utilizó `john` con wordlist `rockyou.txt` y la herramienta `pdf2john` / `zip2john` para generar hashes a partir de los archivos cifrados, luego se crackearon las contraseñas débiles para extraer los flags internos.
**Learning chain:** PDF/ZIP encryption → hash extraction (`pdf2john`, `zip2john`) → dictionary attack (John the Ripper + rockyou.txt) → flag retrieval from decrypted content
**MITRE ATT&CK:** N/A (defensive walkthrough)
**Fuente:** [TryHackMe - Passwords - A Cracking Christmas](https://tryhackme.com/r/room/attacks-on-ecrypted-files-aoc2025-asdfghj123)
