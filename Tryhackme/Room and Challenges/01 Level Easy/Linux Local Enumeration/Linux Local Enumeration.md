# Linux Local Enumeration [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough
* **Slug:** `lle`
* **Link:** https://tryhackme.com/room/lle
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** GitLab (DhikSec), Yawaraka-sec (yawaraka-sec.com), JinShiranai (hashnode.dev), Writeups AdityaDindi

## Solucionario de Tareas / Task Solutions

> **ES:** Esta sala enseña a enumerar eficientemente una máquina Linux y identificar posibles debilidades después de obtener un reverse shell. Cubre estabilización de shells (TTY), enumeración básica del sistema, archivos importantes en /etc, búsqueda de archivos con find, explotación de SUID, y scripts de enumeración automatizada (LinPEAS, LinEnum).
> **EN:** This room teaches how to efficiently enumerate a Linux machine and identify possible weaknesses after obtaining a reverse shell. It covers shell stabilization (TTY), basic system enumeration, important files in /etc, file searching with find, SUID exploitation, and automated enumeration scripts (LinPEAS, LinEnum).

### Task 1 - Introduction

> **ES:** Para comenzar, se debe obtener un reverse shell navegando a `MACHINE_IP:3000` y siguiendo las instrucciones. Se proporcionan dos métodos: 1) Crear cmd.php con un payload PHP, o 2) Subir un archivo de reverse shell. Se necesita un listener netcat (`nc -lvnp 1234`) en la máquina atacante.
> **EN:** To begin, obtain a reverse shell by navigating to `MACHINE_IP:3000` and following the instructions. Two methods are provided: 1) Create cmd.php with a PHP payload, or 2) Upload a reverse shell file. A netcat listener (`nc -lvnp 1234`) is needed on the attacking machine.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Let's go! | `No answer needed` |

### Task 2 - Unit 1: TTY (Stabilizing the Shell)

> **ES:** Un shell de netcat es inestable y se rompe fácilmente. Para estabilizarlo, se usa `python3 -c 'import pty; pty.spawn("/bin/bash")'`. Para ejecutar /bin/bash con perl: `perl -e 'exec "/bin/bash";'`
> **EN:** A netcat shell is unstable and breaks easily. To stabilize it, use `python3 -c 'import pty; pty.spawn("/bin/bash")'`. To execute /bin/bash with perl: `perl -e 'exec "/bin/bash";'`

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| How would you execute /bin/bash with perl? | `perl -e 'exec "/bin/bash";'` |

### Task 3 - Unit 1: SSH

> **ES:** El archivo `id_rsa` (clave privada SSH) se encuentra normalmente en `/home/user/.ssh/id_rsa`. En esta máquina objetivo no existe un archivo id_rsa disponible.
> **EN:** The `id_rsa` file (SSH private key) is usually located at `/home/user/.ssh/id_rsa`. On this target machine, no id_rsa file is available.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Where can you usually find the id_rsa file? (User = user) | `/home/user/.ssh/id_rsa` |
| Is there an id_rsa file on the box? (yay/nay) | `nay` |

### Task 4 - Unit 2: Basic Enumeration

> **ES:** La enumeración básica incluye: `uname -a` (información del sistema), `~/.bash_history` (historial de comandos), `sudo -V` (versión de sudo, vulnerable si < 1.8.28), y `sudo -l` (derechos sudo del usuario). La flag se encuentra en el historial de bash.
> **EN:** Basic enumeration includes: `uname -a` (system info), `~/.bash_history` (command history), `sudo -V` (sudo version, vulnerable if < 1.8.28), and `sudo -l` (user's sudo rights). The flag is found in bash history.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| How would you print machine hardware name only? | `uname -m` |
| Where can you find bash history? | `~/.bash_history` |
| What's the flag? | `THM{...redacted...}` |

### Task 5 - Unit 3: /etc

> **ES:** La carpeta /etc es el centro de configuración de Linux. `/etc/passwd` contiene información de cuentas de usuario (lectura = enumerar usuarios, escritura = crear usuario root). `/etc/shadow` contiene contraseñas encriptadas (lectura = crackear contraseñas). `/etc/hosts` mapea hostnames a IPs. Se puede leer /etc/passwd en esta máquina.
> **EN:** The /etc folder is Linux's configuration center. `/etc/passwd` contains user account information (read = enumerate users, write = create root user). `/etc/shadow` contains encrypted passwords (read = crack passwords). `/etc/hosts` maps hostnames to IPs. /etc/passwd is readable on this machine.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Can you read /etc/passwd on the box? (yay/nay) | `yay` |

### Task 6 - Unit 4: Find Command and Interesting Files

> **ES:** Usando `find` se buscan archivos interesantes por extensión (.log, .conf, .bak). Encontrar `/var/opt/passwords.bak` revela la contraseña `THMSkidyPass`. Encontrar `/etc/sysconf/flag.conf` revela la flag `thm{conf_file}`.
> **EN:** Using `find`, search for interesting files by extension (.log, .conf, .bak). Finding `/var/opt/passwords.bak` reveals the password `THMSkidyPass`. Finding `/etc/sysconf/flag.conf` reveals the flag `thm{conf_file}`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What's the password you found? | `THMSkidyPass` |
| Did you find a flag? | `thm{conf_file}` |

### Task 7 - Unit 4: SUID

> **ES:** Los binarios con SUID (Set User ID) se ejecutan con permisos de otro usuario. Usando `find / -perm -u=s -type f 2>/dev/null` se encuentran binarios SUID. Referenciando con GTFObins, `grep` puede usarse para escalar privilegios. El payload para leer /etc/shadow es: `grep '' /etc/shadow`
> **EN:** Binaries with SUID (Set User ID) execute with another user's permissions. Using `find / -perm -u=s -type f 2>/dev/null` finds SUID binaries. Cross-referencing with GTFObins, `grep` can be used for privilege escalation. The payload to read /etc/shadow is: `grep '' /etc/shadow`

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which SUID binary has a way to escalate your privileges on the box? | `grep` |
| What's the payload you can use to read /etc/shadow with this SUID? | `grep '' /etc/shadow` |

### Task 8 - [Bonus] Port Forwarding

> **ES:** El port forwarding permite pasar firewalls y enumerar servicios locales. Usar `netstat -tulpn` para ver conexiones de red, puertos en uso y procesos asociados.
> **EN:** Port forwarding allows bypassing firewalls and enumerating local services. Use `netstat -tulpn` to view network connections, ports in use, and associated processes.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Try using those commands on your system! | `No answer needed` |

### Task 9 - Unit 5: Automating Scripts

> **ES:** LinPEAS y LinEnum son scripts automatizados de enumeración. LinPEAS busca paths de escalada de privilegios, contraseñas y abusos de sudo. LinEnum realiza checks scriptados de enumeración y escalada de privilegios. Se recomienda ejecutar ambos y comparar resultados.
> **EN:** LinPEAS and LinEnum are automated enumeration scripts. LinPEAS searches for privilege escalation paths, passwords, and sudo abuses. LinEnum performs scripted local Linux enumeration and privilege escalation checks. It's recommended to run both and compare results.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Got it! | `No answer needed` |

### Task 10 - Resources and What's Next?

> **ES:** Felicitaciones por completar la enumeración local de Linux. Se recomienda continuar con salas de escalada de privilegios y máquinas prácticas para aplicar lo aprendido.
> **EN:** Congratulations on completing Linux local enumeration. It's recommended to continue with privilege escalation rooms and practical machines to apply what you've learned.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Read the above and consider completing mentioned rooms. | `No answer needed` |

## Metodología / Methodology

1. **Paso / Step - Obtención y estabilización del shell:** Obtener un reverse shell y estabilizarlo a TTY completo usando Python, Perl u otros métodos para permitir el uso de comandos como `su` y `sudo`.
2. **Paso / Step - Enumeración básica del sistema:** Ejecutar `uname -a` para identificar SO y versión, revisar `~/.bash_history` para información sensible, verificar `sudo -V` para detectar vulnerabilidades, y usar `sudo -l` para ver derechos sudo.
3. **Paso / Step - Exploración de /etc:** Leer `/etc/passwd` para enumerar usuarios, intentar `/etc/shadow` para contraseñas encriptadas, revisar `/etc/hosts` para mapeo de red.
4. **Paso / Step - Búsqueda de archivos con find:** Usar `find / -type f -name "*.ext" 2>/dev/null` para buscar archivos por extensión (.log, .conf, .bak) que puedan contener credenciales o flags.
5. **Paso / Step - Explotación de SUID:** Ejecutar `find / -perm -u=s -type f 2>/dev/null` para encontrar binarios con SUID, referenciar con GTFObins para identificar explotaciones de escalada.
6. **Paso / Step - Port forwarding:** Usar `netstat -tulpn` para enumerar servicios locales y puertos, aplicar port forwarding para acceder a servicios internos.
7. **Paso / Step - Enumeración automatizada:** Ejecutar LinPEAS y LinEnum para obtener una vista completa de vulnerabilidades y paths de escalada, comparando resultados entre ambos scripts.

### Cadena de ataque / Attack Chain

```
Reverse shell obtenido (PHP payload + netcat)
        |
        v
Estabilización a TTY (python3 -c 'import pty; pty.spawn("/bin/bash")')
        |
        v
Enumeración básica (uname, bash_history, sudo -V, sudo -l)
        |
        v
Exploración de /etc (passwd, shadow, hosts)
        |
        v
Búsqueda de archivos (find -type f -name "*.bak" / "*.conf")
        |
        v
Descubrimiento de credenciales (passwords.bak) y flags (flag.conf)
        |
        v
Identificación de SUID (grep) -> Escalada a root
        |
        v
Port forwarding -> Enumeración de servicios internos
        |
        v
LinPEAS/LinEnum -> Verificación automatizada de hallazgos
```

**Lección:** La enumeración post-explotación es crítica para escalar privilegios; una combinación de métodos manuales (find, /etc, SUID) y automatizados (LinPEAS, LinEnum) proporciona la mejor cobertura para identificar debilidades en una máquina Linux.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
