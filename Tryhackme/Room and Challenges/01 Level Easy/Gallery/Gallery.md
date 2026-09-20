# Gallery

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | ctf | `gallery` | https://tryhackme.com/room/gallery666 | 01 Level Easy | TryHackMe | web / SQL Injection / Simple Image Gallery / hash cracking / upload webshell / reverse shell / nano privesc / WordPress | Ofensivo: explotar una galería de imágenes vulnerable (SQLi en el login), subir una webshell, pivotar con una reverse shell y escalar a root por una regla sudo permisiva. |

---

> **Objeto:** Comprometer una aplicación "Simple Image Gallery" mediante inyección SQL en el formulario de login, volcar el hash de la contraseña del administrador y crackearlo, subir una webshell al servidor para obtener una reverse shell y escalar a root explotando una configuración sudo que permite a un usuario ejecutar un binario como root.

**Contexto:** Sala CTF (by Mikaa) que presenta una galería de imágenes apenas protegida. El panel de login de Simple Image Gallery es vulnerable a inyección SQL: la consulta que comprueba `username/password` se construye concatenando la entrada, por lo que se puede autenticar sin conocer credenciales. Extrayendo el hash MD5 de la contraseña del usuario `hamdulay` (`a228b12a08b6527e7978cbe5d914531c`) y crackeándolo, se entra al panel de administración que permite subir imágenes. Subiendo un archivo PHP (webshell) se ejecuta un comando y se obtiene una reverse shell como `www-data`; explorando la máquina se llega al usuario `mike` y, con `sudo -l`, se descubre que puede ejecutar un binario como root, culminando en la flag de root.

> **ES:** "Gallery" — SQLi en el login, crackeo del hash MD5, subida de webshell, reverse shell y escalada a root.
> **EN:** SQL injection on the gallery login, MD5 hash cracking, webshell upload, reverse shell and a sudo misconfiguration to root.

## Solucionario

### Task 1: Despliegue y obtener una shell / Deploy and get a Shell

**Explicación:** El escaneo de puertos revela que solo hay `3` puertos abiertos en la máquina. Navegando a la web se identifica el software que ejecuta: `Simple Image Gallery` (por la petición `login.php` y la ruta de la aplicación). El formulario de login es vulnerable a SQLi: `username=admin' or 1=1-- -` salta la autenticación. Con la inyección también se puede volcar el hash MD5 del admin (`a228b12a08b6527e7978cbe5d914531c` en `gallery.db`/tabla de usuarios), que se crackea y permite entrar al panel de administración. Desde el panel se sube una imagen PHP (webshell) que, abierta con un parámetro, ejecuta comandos: se lanza una reverse shell como `www-data` y se lee la flag de usuario.

> **Texto original / Original text:** Start Machine · "Our gallery is not very well secured." · "Designed and created by Mikaa !"

```bash
nmap -<IP>              # 3 puertos abiertos
# Login SQLi: admin' or 1=1-- -
# Volcar hash: (SQLi union) a228b12a08b6527e7978cbe5d914531c
# crack -> hashcat/john
# Subir webshell .php -> nc -lvnp 4444 -> python3 -c 'import pty; pty.spawn("/bin/bash")'
cat /home/mike/*.txt    # user flag
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos puertos están abiertos? / How many ports are open? | `3` |
| 2 | ¿Qué aplicación se ejecuta en el puerto 80? / What application is running on port 80? | `Simple Image Gallery` |
| 3 | ¿Cuál es el hash de la contraseña del administrador? / What is the admin's password hash? | `a228b12a08b6527e7978cbe5d914531c` |
| 4 | ¿Cuál es la flag de usuario? / What is the user flag? | `THM{af05cd30bfed67849befd546ef}` |

### Task 2: Escalar al usuario root / Escalate to the root user

**Explicación:** Enumerando la máquina se identifica el usuario `mike` (que contiene la flag de usuario en su home). Con `sudo -l` se ve que este usuario puede ejecutar el binario `/usr/bin/nano` como root sin contraseña: `sudo nano` es una conocida técnica de privesc, pues desde el editor se abre `/root/root.txt` (o se invoca una shell con `!`). Se lee la flag de root y se cierra la sala.

> **Texto original / Original text:** "Good luck with the last step !"

```bash
sudo -l                           # (usr/bin/nano) NOPASSWD como root
sudo /usr/bin/nano                # Ctrl+R / Abrir /root/root.txt
# o: en nano, Alt+F2 o ! para lanzar shell
cat /root/root.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | ¿Cuál es la flag de root? / What's the root flag? | `THM{ba87e0dfe5903adfa6b8b450ad7567bafde87}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many ports are open? | `3` |
| 2 | What application is running on port 80? | `Simple Image Gallery` |
| 3 | What is the admin's password hash? | `a228b12a08b6527e7978cbe5d914531c` |
| 4 | What is the user flag? | `THM{af05cd30bfed67849befd546ef}` |
| 5 | What's the root flag? | `THM{ba87e0dfe5903adfa6b8b450ad7567bafde87}` |

---

**Metodología:** Escaneo y reconocimiento del software (Simple Image Gallery). Inyección SQL en el login para saltar la autenticación y volcar el hash administrativo. Crackeo del hash para acceder al panel de administración y subida de una webshell PHP. Ejecución de una reverse shell como `www-data`, enumeración hasta el usuario con privilegios y abuso de la regla `sudo nano` para leer la flag de root.

### Cadena de ataque / Attack Chain

```text
nmap (3 puertos) -> Simple Image Gallery -> SQLi en login -> dump hash MD5 -> crack -> panel admin -> upload webshell -> reverse shell (www-data) -> +user mike -> sudo nano -> root flag
```

**Learning chain:** web recon -> login SQLi -> hash dump + crack -> authenticated upload -> webshell -> reverse shell -> sudo editor (GTFOBins) -> root.

**Lección:** *Un login mal concatenado convierte la autenticación en un canal de exfiltración (hash) y de RCE (upload autorizado); los binarios de edición como `nano` bajo `sudo NOPASSWD` (GTFOBins) cierran la escalada a root sin credenciales.*

**MITRE ATT&CK:** T1190 — Exploit Public-Facing Application; T1213.002 — Data from Information Repositories: Code Repositories; T1505.003 — Server Software Component: Web Shell; T1068 — Exploitation for Privilege Escalation

**Fuente:** [TryHackMe - Gallery](https://tryhackme.com/room/gallery666)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.