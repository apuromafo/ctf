# CyberHeroes

| **Dificultad** | Easy |
| **Tipo** | CTF (web) |
| **Slug** | `cyberheroes` |
| **Link** | [TryHackMe](https://tryhackme.com/room/cyberheroes) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Nmap / Análisis de código fuente / JavaScript / CyberChef |
| **Impacto** | Reto web introductorio: encuentra una forma de iniciar sesión en el "CyberHeroes club" examinando el JavaScript del login y revirtiendo una cadena ofuscada. |

---

**Contexto:** "¿Quieres pertenecer al club exclusivo de los CyberHeroes? Demuestra tu valía encontrando la forma de iniciar sesión." El único puerto relevante es un Apache en el 80. El fichero `login.html` contiene una función JavaScript `authenticate()` que compara el usuario con `h3ck3rBoi` y la contraseña con la cadena invertida `54321@terceSrepuS`. Al revertirla con CyberChef se obtiene `SuperSecret@12345`, y al autenticarse se revela la flag directamente en la página.

## Solucionario

### Task 1: Inicia sesión y captura la flag

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del reto? | `flag{edb0be532c540b1a150c3a7e85d2466e}` |

---

**Metodología:** Escaneo de puertos con `nmap -sC -sV` que deja ver Apache en el 80. Se visualiza el código fuente de `login.html`, donde la función `authenticate` revela tanto el usuario (`h3ck3rBoi`) como la contraseña ofuscada. Revertir la cadena `54321@terceSrepuS` con CyberChef (Reverse) produce `SuperSecret@12345`. Al hacer login se carga `RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_...txt` y se muestra la flag.

**Learning chain:** escaneo de puertos → revisión de código fuente → ingeniería inversa de credenciales en JavaScript → login y captura de flag.

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1595 (Active Scanning), T1059.007 (Rust/Javascript)

**Fuente:** [TryHackMe - CyberHeroes](https://tryhackme.com/room/cyberheroes)