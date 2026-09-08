# RootMe

| **Dificultad** | Easy |
| **Tipo** | CTF (boot2root) |
| **Slug** | `rrootme` |
| **Link** | [TryHackMe](https://tryhackme.com/room/rrootme) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Apache 2.4.41 / SSH / Gobuster / subida de archivos / bypass de extensión `.php5` / reverse shell / permisos SUID / Python |
| **Impacto** | CTF para principiantes: primero se explota un panel de subida de archivos con un bypass de extensión para subir una webshell `.php5` y obtener una reverse shell, y después se escala a root abusando del binario SUID `/usr/bin/python` en la máquina objetivo. |

---

**Contexto:** La máquina es un CTF pensado para principiantes. En el escaneo inicial solo aparecen 2 puertos abiertos: HTTP (Apache 2.4.41) y SSH (22). Con Gobuster se descubre `/panel/` y `/uploads/`. El panel de subida bloquea archivos `.php`, pero permite subir el mismo payload con la extensión `.php5`, lo que permite guardar una webshell en `/uploads/` y lanzar una reverse shell hacia la máquina atacante. Dentro de la máquina, la primer bandera (`user.txt`) está en `/var/www`; para la segunda hay que buscar binarios con SUID, encontrando `/usr/bin/python` con permisos `rwsr-sr-x` de root, que da una shell de root con `python -c 'import os; os.execl("/bin/sh", "sh", "-p")'`.

## Solucionario

### Task 1: Desplegar la máquina

**Explicación:** Se lanza la máquina asignada por TryHackMe. El CTF empieza sin credenciales; la IP se usa para toda la fase de reconocimiento.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina. | `No answer needed` |

### Task 2: Reconocimiento

**Explicación:** Con `nmap -p- --min-rate 5000 -sV <IP>` se descubren 2 puertos abiertos (HTTP y SSH), se identifica Apache 2.4.41 y el servicio SSH en el puerto 22. Con `gobuster dir -u http://<IP>/ -w <WORDLIST>` se enumeran directorios: `/panel` (301) y `/uploads` (301) son los interesantes. El directorio oculto es `/panel/`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Escanea la máquina, ¿cuántos puertos están abiertos? | `2` |
| 2 | ¿Qué versión de Apache se está ejecutando? | `2.4.41` |
| 3 | ¿Qué servicio corre en el puerto 22? | `ssh` |
| 4 | Encuentra directorios en el servidor web usando Gobuster. | `No answer needed` |
| 5 | ¿Cuál es el directorio oculto? | `/panel/` |

### Task 3: Obtener una shell

**Explicación:** En `/panel/` hay un formulario de subida que impide subir `.php`. Se crea una webshell PHP (reverse shell con `fsockopen` + `proc_open`) y se renombra a `File.php5` para saltarse el filtro. Tras subirla, se localiza en `/uploads/`. Con `nc -lvnp <PORT>` a la escucha y ejecutando el archivo, se obtiene una shell como `www-data`. En `/var/www` está `user.txt` con la primera flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Encuentra un formulario para subir y obtener una reverse shell; sigue la pista para encontrar la flag. | `THM{y0u_g0t_a_sh3ll}` |

### Task 4: Escalada de privilegios

**Explicación:** Con `find / -type f -perm -4000 -ls 2>/dev/null` se buscan binarios con SUID. El extraño es `/usr/bin/python`, con permisos `-rwsr-sr-x root root`. Al ser un binario con SUID se puede generar una shell de root con `python -c 'import os; os.execl("/bin/sh", "sh", "-p")'`. Con la shell de root se lee `root.txt`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Busca archivos con permiso SUID, ¿cuál es el extraño? | `/usr/bin/python` |
| 2 | Encuentra una forma de escalar tus privilegios. | `No answer needed` |
| 3 | Lee la flag `root.txt`. | `THM{pr1v1l3g3_3sc4l4t10n}` |

---

**Metodología:** Enumeración de puertos y servicios con `nmap` → fuzzing de directorios con `gobuster` → análisis del panel de subida → bypass de extensión (`.php` → `.php5`) → subida de webshell y reverse shell con `nc` → búsqueda de SUID → explotación de `/usr/bin/python` para conseguir root.
**Learning chain:** reconocimiento → enumeración web → control de subida de archivos → primer foothold → escalada de privilegios por SUID → flags `user.txt` y `root.txt`.
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1083 (File and Directory Discovery), T1505.003 (Web Shell), T1059.004 (Unix Shell), T1548.001 (Setuid and Setgid)
**Fuente:** [TryHackMe - RootMe](https://tryhackme.com/room/rrootme)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
