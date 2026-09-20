# Psycho Break

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `psychobreak` | https://tryhackme.com/room/psychobreak | 01 Level Easy | THM | Recon, Directory enumeration, Steganography, Password cracking, Cron privilege escalation | Boot-to-root CTF con steganography y escalada de privilegios |

---

**Contexto:** CTF de estilo puzzle centrado en enumeration y steganography sobre una máquina Windows con tema "The Evil Within". Incluye descubrimiento de directorios ocultos, decodificación Vigenère/Atbash/Morse, análisis de imágenes (steghide), command injection, fuerza bruta con diccionarios y escalada de privilegios mediante cron jobs editables.

> **ES:** CTF de estilo puzzle centrado en enumeration y steganography sobre una máquina Windows con tema "The Evil Within". Incluye descubrimiento de directorios ocultos, decodificación Vigenère/Atbash/Morse, análisis de imágenes (steghide), command injection, fuerza bruta con diccionarios y escalada de privilegios mediante cron jobs editables.
> **EN:** A puzzle-style CTF focused on enumeration and steganography on a Windows machine themed around "The Evil Within". Includes discovering hidden directories, Vigenère/Atbash/Morse decoding, image analysis (steghide), command injection, dictionary brute-forcing, and privilege escalation via editable cron jobs.

## Solucionario

### Task 1: Reconocimiento / Recon

**Explicación:** Se realiza un reconocimiento inicial de la máquina con nmap para identificar puertos abiertos y el sistema operativo subyacente, paso previo a cualquier otro tipo de interacción.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Start your target machine and attackbox | `No answer needed` |
| 2 | How many ports are open on the target? | `3` |
| 3 | What operating system is the target running? | `ubuntu` |

### Task 2: Web / Web

**Explicación:** Se explora la aplicación web, se autentica con las credenciales descubiertas y se extrae información desde el dashboard, confirmando los hashes y contraseñas descubiertas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password discovered? | `532219a04ab7a02b56faafbec1a4c1ea` |
| 2 | What is the secret value for portal access? | `Grant_me_access_to_the_map_please` |
| 3 | What is the admin password hash? | `48ee41458eb0b43bf82b986cecf3af01` |
| 4 | What is the flag on the web dashboard? | `you_made_it` |

### Task 3: Ayúdame / Help Mee

**Explicación:** Se descifra la contraseña Vigenère con la clave dada y se usa para acceder por SSH como usuario `joseph`, obteniendo una shell interactiva.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the username discovered? | `joseph` |
| 2 | What is the decrypted password? | `SHOWME` |
| 3 | What is the SSH user? | `joseph` |
| 4 | What is the SSH password? | `intotheterror445` |

### Task 4: Forzar la cerradura / Crack it open

**Explicación:** Se ejecuta un ataque de fuerza bruta o enumeración para obtener las credenciales del siguiente usuario, escalando privilegios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the username discovered? | `kidman` |
| 2 | What is the password? | `KIDMANSPASSWORDISSOSTRANGE` |

### Task 5: Captura la bandera / Go Capture The Flag

**Explicación:** Se completa la escalada final hasta root, se leen los archivos de flags de usuario y root, y se limpia el entorno de prueba.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `4C72A4EF8E6FED69C72B4D58431C4254` |
| 2 | What is the root flag? | `BA33BDF5B8A3BFC431322F7D13F3361E` |
| 3 | Clean up | `No answer needed` |

### Task 6: Conclusión / Conclusion

**Explicación:** Resumen del room y cierre; se comprueba que se completaron todas las tareas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Completion | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Start your target machine and attackbox | `No answer needed` |
| 2 | How many ports are open on the target? | `3` |
| 3 | What operating system is the target running? | `ubuntu` |
| 4 | What is the password discovered? | `532219a04ab7a02b56faafbec1a4c1ea` |
| 5 | What is the secret value for portal access? | `Grant_me_access_to_the_map_please` |
| 6 | What is the admin password hash? | `48ee41458eb0b43bf82b986cecf3af01` |
| 7 | What is the flag on the web dashboard? | `you_made_it` |
| 8 | What is the username discovered? | `joseph` |
| 9 | What is the decrypted password? | `SHOWME` |
| 10 | What is the SSH user? | `joseph` |
| 11 | What is the SSH password? | `intotheterror445` |
| 12 | What is the username discovered? | `kidman` |
| 13 | What is the password? | `KIDMANSPASSWORDISSOSTRANGE` |
| 14 | What is the user flag? | `4C72A4EF8E6FED69C72B4D58431C4254` |
| 15 | What is the root flag? | `BA33BDF5B8A3BFC431322F7D13F3361E` |
| 16 | Clean up | `No answer needed` |
| 17 | Completion | `No answer needed` |

---

**Metodología:** Recon con nmap → enumeration web y descubrimiento de directorios ocultos → decodificación de contraseñas cifradas (Vigenère, Atbash, Morse) → acceso SSH → escalada de privilegios (command injection en cron jobs) → captura de flags.

### Cadena de ataque / Attack Chain

```text
nmap (puertos 22,80,etc.) → fuzzing de directorios web → decodificación Vigenère/Atbash/Morse → acceso SSH con credenciales descifradas → enumeración como usuario → command injection en cron → root → flag
```

**Learning chain:** Recon → Directory fuzzing → Password decoding → SSH login → Command injection (cron) → Root flag

**Lección:** *Las contraseñas cifradas con cifrados clásicos (Vigenère, Atbash) pueden ser forzadas con herramientas simples; los cron jobs editables son un vector habitual de escalada de privilegios en Linux cuando el daemon ejecuta comandos como root sin validar la integridad del script.*

**MITRE ATT&CK:** T1110 (Brute Force), T1552.001 (Credentials In Files), T1053.003 (Cron)

**Fuente:** [TryHackMe - Psycho Break](https://tryhackme.com/room/psychobreak)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.