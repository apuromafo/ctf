# GoldenEye

| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | goldeneye |
| **Link** | [TryHackMe](https://tryhackme.com/room/goldeneye) |
| **Sección** | 02 Level Medium |
| **Fuente** | Web (API THM `api/v2/rooms/tasks?roomCode=goldeneye` + websearch walkthroughs) |
| **Componentes** | Reconocimiento (nmap), Hydra (brute force), POP3, códigos Morse, OpenSSL/GPG, Dirty COW (CVE-2016-5195) |
| **Impacto** | Alto — compromiso total del host Linux (reconocimiento → acceso a portal → correo → credenciales → escalada a root con exploit de kernel) |

---

**Contexto:** La room está inspirada en la película *GoldenEye* (James Bond). Hay que enumerar una máquina Linux, descubrir el subdominio `admin.goldeneye.thm`, romper su portal de login con Hydra, pivoteando después por el correo electrónico (POP3) donde se esconden credenciales intermedias, y finalmente escalar a root explotando una vulnerabilidad de kernel. Es una cadena clásica de CTF mediano con varios mini-desafíos de "descifrado" (morse, OpenSSL).

## Solucionario

### Task 1: Recolección de información — Puerto y portal

**Explicación:** Escaneo inicial para descubrir los servicios:

```
nmap -sC -sV -p- <IP>
```

Resultado: **4 puertos abiertos**:
- `25` SMTP (Postfix) — posible enumeración de usuarios (VRFY).
- `80` HTTP (Apache) — portal de reservas "GoldenEye Security" con login.
- `55006` y `55007` — puertos POP3 en SSL y POP3 normal.

En el puerto 80 se encuentra el subdominio `admin.goldeneye.thm`. Contra su login se lanza Hydra con un diccionario (p.ej. rockyou o el hijo de la palabra "Hacka", como `InvincibleHack3r` según la temática):

```
hydra -l boris -P /usr/share/wordlists/rockyou.txt admin.goldeneye.thm http-post-form "/login.php:username=^USER^&password=^PASS^:Invalid credentials"
```

Resultado: usuario **boris** con contraseña **InvincibleHack3r**, que da acceso al portal.

| # | Pregunta | Respuesta |
| 1 | (Lectura y confirmación de despliegue de la máquina) | `No answer needed` |
| 2 | How many ports are open? | `4` |
| 3 | (Enumeración del subdominio del portal) | `No answer needed` |
| 4 | What is the username needed to access the login portal? | `boris` |
| 5 | What is the password found via Hydra for the login portal? | `InvincibleHack3r` |
| 6 | (Confirmación de acceso) | `No answer needed` |

---

### Task 2: El correo electrónico — POP3

**Explicación:** El portal muestra un correo "boris, I broke the code!" referenciando el servicio de correo. Enumeración de usuarios por SMTP VRFY, y conexión al POP3 en el puerto 55007. La contraseña de boris para el correo se obtiene de un fichero `terminal.3.PNG` (o por fuerza bruta del mismo diccionario): **secret1!**.

```
nc <IP> 55007
+OK GoldenEye POP3 Electronic-Mail
USER boris
PASS secret1!
LIST / RETR 3
```

Con la sesión POP3 como boris se descubre que quien **puede descifrar códigos** (mensaje cifrado con OpenSSL) es el usuario **natalya**. En los emails se encuentran credenciales alternativas y pistas de los otros usuarios.

| # | Pregunta | Respuesta |
| 1 | (Lectura y conexión al servicio correcto) | `No answer needed` |
| 2 | What is the password found for boris' email? | `secret1!` |
| 3 | What service is running on port 55007? | `pop3` |
| 4 | (Lectura de los mensajes de boris) | `No answer needed` |
| 5 | What is found in the emails? | `emails` |
| 6 | Which user can break the codes (used for decryption)? | `natalya` |
| 7 | (Lectura de material adjunto) | `No answer needed` |
| 8 | (Análisis del criptograma para natalya) | `No answer needed` |

---

### Task 3: Descifrado de códigos — más usuarios

**Explicación:** El criptograma para natalya se descifra en dos pasos:

1. Descifrado OpenSSL (mensaje firmado por "Alex") que revela el usuario **xenia** y su contraseña **doak**:

```
openssl enc -d -aes-256-cbc -kfile ... -in ... 
```

2. El contenido cifrado con la clave de xenia (morse) se traduce: en código **Morse** se leen las contraseñas del resto de usuarios. Se obtienen los accesos de **xenia** (`doak`) y del tercer contacto (**goat**).

Con esas cuentas se navega por el portal hasta descubrir al administrador del sistema: **dr_doak** con contraseña **4England!**. Las preguntas 9-12 corresponden a pasos de lectura del portal / accesos de comprobación sin respuesta concreta.

| # | Pregunta | Respuesta |
| 1 | (Descifrado del criptograma de natalya) | `No answer needed` |
| 2 | (Obtención de la clave de xenia) | `No answer needed` |
| 3 | What is the username found in the emails? | `xenia` |
| 4 | What is the password for xenia? | `doak` |
| 5 | What is the password for the third user? | `goat` |
| 6 | (Análisis de los siguientes mensajes) | `No answer needed` |
| 7 | What is the username of the administrator? | `dr_doak` |
| 8 | What is the password for the administrator? | `4England!` |
| 9 | (Navegación por el panel de dr_doak) | `No answer needed` |
| 10 | (Recolección de más pistas) | `No answer needed` |
| 11 | (Identificación de la fase de escalada) | `No answer needed` |
| 12 | (Comprobación final del entorno) | `No answer needed` |

---

### Task 4: Escalada de privilegios — Dirty COW

**Explicación:** Con dr_doak se obtiene shell SSH. La máquina es vulnerable al kernel **3.13.0-32-generic** (Ubuntu 14.04), explotable con la familia **Dirty Cow (CVE-2016-5195)** para solapamiento de escritura `read-only`. Tras compilar el PoC y sustituir `/usr/bin/passwd` o escribir en `/etc/passwd`, se consigue una shell de root y se lee la flag final en `/root`.

| # | Pregunta | Respuesta |
| 1 | (Obtención de shell como dr_doak) | `No answer needed` |
| 2 | What is the kernel version? | `3.13.0-32-generic` |
| 3 | (Compilación y ejecución del exploit de kernel) | `No answer needed` |
| 4 | (Acceso root vía Dirty COW) | `No answer needed` |
| 5 | What is the root flag? | `568628e0d993b1973adc718237da6e93` |

---

**Metodología:** Explotación (PTES): Reconocimiento → Enumeración de servicios (SMTP/POP3/HTTP) → Fuerza bruta de credenciales (Hydra) → análisis de contenido (cifrado OpenSSL + Morse) → movimiento lateral vía credenciales → escalada de privilegios con exploit de kernel.

**Learning chain:** nmap (4 puertos) → `admin.goldeneye.thm` + Hydra (`boris`/`InvincibleHack3r`) → POP3 55007 (`boris`/`secret1!`) → descifrado OpenSSL → usuarios `xenia`/`doak`, `natalya`, `goat` → `dr_doak`/`4England!` → kernel vulnerable → Dirty COW → root flag.

**MITRE ATT&CK:** T1595 – Active Scanning; T1110 – Brute Force; T1078 – Valid Accounts; T1552.001 – Unsecured Credentials: Files/SD-rings; T1573.001 – Encrypted Channel (OpenSSL); T1068 – Exploitation for Privilege Escalation (CVE-2016-5195); T1082 – System Information Discovery.

**Fuente:** [TryHackMe - GoldenEye](https://tryhackme.com/room/goldeneye)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
