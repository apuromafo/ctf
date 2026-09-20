# Classic Passwd
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `classicpasswd` |
| **Link** | [TryHackMe](https://tryhackme.com/room/classicpasswd) |
| **Sección** | Reverse Engineering / CTF |
| **Fuente** | Research de repositorios de answers de la comunidad (GitHub) |
| **Componentes** | Password cracking / bypass de autenticación, análisis estático de binario o script, strings/desensamblado, reverse engineering, bandera única |
| **Impacto** | Sala Medium de reto de cracking de contraseñas: analizar el objetivo entregado (binario/secuencia), recuperar la credencial o deformar la comprobación y capturar la bandera única del reto. |
---
**Contexto:** Classic Passwd es un reto de tipo "password" clásico: hay que inspeccionar el objetivo (un binario o flujo que exige una contraseña), entender cómo comprueba la entrada y obtener el valor correcto, que devuelve la bandera. Solo hay una pregunta y una única flag como entregable.
*EN: Classic Passwd is a classic "password" style challenge: you must inspect the target (a binary or flow that requires a password), understand how it checks the input and obtain the correct value, which returns the flag. There is a single question and a unique flag as the deliverable.*
## Solucionario
### Task 1 — Get the Flag
**Explicación:** Ejecutar el reto y analizarlo (strings, objdump/Ghidra para binarios, o lectura directa del script). Al inspeccionar la comparación de la contraseña o probar la cadena recuperada, el programa devuelve la bandera del reto.
*EN: Run the challenge and analyze it (strings, objdump/Ghidra for binaries, or reading the script directly). By inspecting the password comparison or trying the recovered string, the program returns the challenge flag.*

```bash
# Análisis rápido (binario)
strings passwd
# o desensamblar la función de comprobación (radare2/Ghidra)
# Introducir la contraseña recuperada -> bandera
# THM{65235128496}
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Get the flag | `THM{65235128496}` |
---
**Metodología:** Descargar/ejecutar el reto → inspección de strings y flujo de comparación → recuperar la contraseña → ejecutar y leer la bandera.
**Learning chain:** black-box (ejecución) → static analysis (strings/disassemble) → password recovery → flag.
**Lección:** *La contraseña nunca está "segura" en el cliente: si el secreto vive en el mismo binario que lo comprueba, es solo cuestión de strings o un desensamblador bien dirigido.*
**MITRE ATT&CK:** T1212 (Exploitation for Credential Access), T1040 (Network Sniffing, opcional), T1552 (Unsecured Credentials - hardcoded), T1059 (Command and Scripting Interpreter, en entorno de reto).
**Fuente:** [TryHackMe - Classic Passwd](https://tryhackme.com/room/classicpasswd)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.