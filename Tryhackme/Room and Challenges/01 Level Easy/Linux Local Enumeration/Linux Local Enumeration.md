# Linux Local Enumeration

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|------------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | lle | [TryHackMe](https://tryhackme.com/r/room/lle) | 01 Level Easy | THM | reverse shell, TTY, uname, bash history, sudo, /etc, find, SUID, GTFObins, netstat, LinPEAS, LinEnum | Post-explotación: enumeración local que permite identificar credenciales, archivos sensibles y escalar a root vía SUID (grep) |

---

**Contexto:** Sala que enseña a enumerar eficientemente una máquina Linux tras obtener un reverse shell. Cubre estabilización de la shell (TTY), enumeración básica del sistema (uname, bash history, sudo), análisis de archivos en /etc, búsqueda de archivos interesantes con find, abuso de binarios SUID contra GTFObins y enumeración automatizada con LinPEAS y LinEnum.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presenta la metodología de la sala: tras obtener un reverse shell, el objetivo es enumerar la máquina de forma eficiente para descubrir credenciales, archivos sensibles y vectores de escalada de privilegios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's go! | `No answer needed` |

### Task 2: Unidad 1: TTY / Unit 1: TTY

**Explicación:** Se enseña a estabilizar la reverse shell obteniendo un TTY completo. Ejecutar `/bin/bash` desde `perl` permite a la shell comportarse de forma interactiva plena.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How would you execute /bin/bash with perl? | `perl -e 'exec "/bin/bash";'` |

### Task 3: Unidad 1: SSH / Unit 1: SSH

**Explicación:** Se ubican las claves SSH del usuario actual, normalmente en `~/.ssh/`, y se comprueba si existe una `id_rsa` en la máquina que permita mantener acceso persistente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Where can you usually find the id_rsa file? (User = user) | `/home/user/.ssh/id_rsa` |
| 2 | Is there an id_rsa file on the box? (yay/nay) | `nay` |

### Task 4: Unidad 2: Enumeración básica / Unit 2: Basic Enumeration

**Explicación:** Enumeración inicial del sistema con `uname` para obtener el hardware, revisión de `~/.bash_history` (donde se oculta una flag) y comprobación de la configuración de sudo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How would you print machine hardware name only? | `uname -m` |
| 2 | Where can you find bash history? | `~/.bash_history` |
| 3 | What's the flag? | `thm{clear_the_history}` |

### Task 5: Unidad 3: /etc / Unit 3: /etc

**Explicación:** Se auditan los archivos críticos del directorio `/etc`. La lectura de `/etc/passwd` confirma que se dispone de acceso de lectura a información sensible del sistema.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Can you read /etc/passwd on the box? (yay/nay) | `yay` |

### Task 6: Unidad 4: Comando find y archivos interesantes / Unit 4: Find Command and Interesting Files

**Explicación:** Se usa `find` para localizar archivos de interés por extensión y contenido, descubriendo un backup con una contraseña y un archivo de configuración que esconde una flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What's the password you found? | `THMSkidyPass` |
| 2 | Did you find a flag? | `thm{conf_file}` |

### Task 7: Unidad 4: SUID / Unit 4: SUID

**Explicación:** Búsqueda de binarios con el bit SUID (`find / -perm -u=s -type f`). El binario `grep` cuenta con SUID, y consultando GTFObins se obtiene el payload que permite leer `/etc/shadow` y escalar a root.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which SUID binary has a way to escalate your privileges on the box? | `grep` |
| 2 | What's the payload you can use to read /etc/shadow with this SUID? | `grep '' /etc/shadow` |

### Task 8: [Bono] Reenvío de puertos / [Bonus] Port Forwarding

**Explicación:** Se introducen técnicas de reenvío de puertos para acceder a servicios internos de la máquina comprometida desde el equipo atacante.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Try using those commands on your system! | `No answer needed` |

### Task 9: Unidad 5: Scripts de automatización / Unit 5: Automating Scripts

**Explicación:** Se presentan herramientas de enumeración automatizada como LinPEAS y LinEnum, que aceleran la recopilación de información sensible de la máquina.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Got it! | `No answer needed` |

### Task 10: Recursos y ¿qué sigue? / Resources and What's Next?

**Explicación:** Cierre de la sala: se recomiendan recursos y salas complementarias para continuar profundizando en enumeración y escalada de privilegios en Linux.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Read the above and consider completing mentioned rooms. | `No answer needed` |

---

**Metodología:** Se obtiene un reverse shell contra el puerto 3000 (MACHINE_IP:3000) usando un payload PHP y un listener netcat, y la shell se estabiliza a TTY completo con Python/Perl. La enumeración básica empieza con `uname -a`, revisión de `~/.bash_history` (donde aparece la flag `thm{clear_the_history}`), `sudo -V` (versiones < 1.8.28 son vulnerables a CVE-2019-14287) y `sudo -l`. Se exploran los archivos críticos de /etc (passwd, shadow, hosts) y se buscan archivos de interés por extensión (_*.log_, _*.conf_, _*.bak_) con `find`, encontrando `passwords.bak` con `THMSkidyPass` y `flag.conf` con `thm{conf_file}`. Con `find / -perm -u=s -type f` se identifica el binario SUID `grep`, que tras consultar GTFObins permite leer `/etc/shadow` (escalada a root). Finalmente se usa `netstat -tulpn` para enumeración de puertos/procesos y scripts como LinPEAS y LinEnum para verificación automatizada.

### Cadena de ataque / Attack Chain

Reverse shell (PHP + netcat) → estabilización de TTY → enumeración del sistema → análisis de /etc → búsqueda de archivos interesantes → credenciales → SUID grep + GTFObins → lectura de /etc/shadow → escalada a root → reenvío de puertos → verificación automatizada

**Learning chain:** reverse shell (php + netcat) → TTY stabilization → uname/sudo/bash_history enumeration → /etc analysis → find for interesting files → credentials discovery → SUID grep + GTFObins → escalate to root → netstat port forwarding → LinPEAS/LinEnum automated verification

**Lección:** *La enumeración local post-explotación es el paso decisivo: revisar historia de la shell, archivos de `/etc`, binarios SUID y backups olvidados suele revelar credenciales y, combinada con GTFObins, permite escalar a root sin necesidad de exploits complejos.*

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1548.001 (Setuid and Setgid), T1082 (System Information Discovery), T1552.001 (Credentials In Files), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Linux Local Enumeration](https://tryhackme.com/r/room/lle)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.