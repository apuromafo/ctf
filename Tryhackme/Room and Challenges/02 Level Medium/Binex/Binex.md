# Binex
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `binex` |
| **Link** | [TryHackMe](https://tryhackme.com/room/binex) |
| **Sección** | Reverse Engineering / Binary Exploitation |
| **Fuente** | Writeup de TryHackMe |
| **Componentes** | SUID binaries, buffer overflow 64-bit, PATH exploit, privilege escalation |
| **Impacto** | Enseña técnicas de explotación de binarios SUID, buffer overflow en arquitectura de 64 bits y abuso de variables de entorno PATH para escalar privilegios. |
---
**Contexto:** Binex es una sala de TryHackMe centrada en la explotación de binarios con permisos SUID, buffer overflows en 64 bits y abusos de la variable PATH. El participante debe comprometer una máquina Linux explotando vulnerabilities en binarios configurados incorrectamente hasta obtener root.
*EN: Binex is a TryHackMe room focused on exploiting SUID binaries, 64-bit buffer overflows, and PATH variable abuse. The participant must compromise a Linux machine by exploiting misconfigured binaries to gain root access.*
## Solucionario
### Task 1 — SUID Exploitation
**Explicación:** Se identifica y explota un binario con bit SUID que permite escalar privilegios. El usuario y contraseña del sistema se obtienen tras la explotación, permitiendo autenticarse y acceder a la primera flag.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What are the credentials you found? | `tryhackme:thebest` |
### Task 2 — SUID Binary
**Explicación:** Se utiliza el binario SUID explotado para obtener acceso elevado y leer la flag de escalada de privilegios.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag for the SUID binary? | `THM{exploit_the_SUID}` |
### Task 3 — Buffer Overflow
**Explicación:** Se ejecuta un buffer overflow en un binario de 64 bits. El buffer se sobrescribe con un payload que redirige el flujo de ejecución para obtener una shell privilegiada, revelando la flag.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag for the buffer overflow? | `THM{buffer_overflow_in_64_bit}` |
### Task 4 — PATH Exploit
**Explicación:** Se abusa de la variable de entorno PATH: se coloca un binario malicioso en un directorio prioritario para que el binario SUID lo ejecute en lugar del legítimo, obteniendo root y la flag final.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag for the PATH exploit? | `THM{SUID_binary_and_PATH_exploit}` |
---
**Metodología:** Enumeración de binarios SUID (`find / -perm -4000`) → identificación de binarios explotables → escalada por SUID → buffer overflow 64-bit (payload + shellcode) → abuso de PATH variable → root.
**Learning chain:** enumeración SUID → explotación directa → buffer overflow en 64-bit → path hijacking → root shell → flags.
**Lección:** *Los permisos SUID mal configurados y las variables de entorno no sanitizadas son vectores de escalada que persisten mientras no se audite cada binario con privilegios elevados.*
**MITRE ATT&CK:** T1548.001 (Setuid and Setgid), T1210 (Exploitation of Remote Services), T1059.004 (Unix Shell), T1068 (Exploitation for Privilege Escalation).
**Fuente:** [TryHackMe - Binex](https://tryhackme.com/room/binex)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
