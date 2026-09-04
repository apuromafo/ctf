# AllSignsPoint2Pwnage [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** CTF (Premium)
* **Slug:** `allsignspoint2pwnage`
* **Link:** https://tryhackme.com/room/allsignspoint2pwnage
* **Sección / Section:** Windows / CTF
* **Fuente / Source:** Writeup de Rich (happycamper84, Medium), cosmicline (GitHub) y MarCorei7 (WordPress)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Máquina Windows de dificultad media. "All signs point to pwnage" — la cadena de ataque combina enumeración de puertos y shares SMB, subida de una webshell PHP, credenciales en texto plano (auto-logon y scripts .bat) y descifrado de la contraseña VNC.
> **EN:** Medium difficulty Windows machine. "All signs point to pwnage" — the attack chain combines port and SMB share enumeration, uploading a PHP webshell, plaintext credentials (auto-logon and .bat scripts), and VNC password decryption.

---

### Task 1 — Enumeration

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| How many TCP ports under 1024 are open? | `6` |
| What is the hidden share where images should be copied to? | `images$` |

---

### Task 2 — Initial Access

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What user is signed into the console session? | `sign` |
| What hidden, non-standard share is only remotely accessible as an administrative account? | `Installs$` |
| What is the content of user_flag.txt? | `thm{48u51n9_5y573m_func710n4117y_f02_fun_4nd_p20f17}` |

---

### Task 3 — Privilege Escalation

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the Users Password? | `gKY1uxHLuU1zzlI4wwdAcKUw35TPMdv7PAEE5dAFbV2NxpPJVO7eeSH` |
| What is the Administrators Password? | `RCYCc3GIjM0v98HDVJ1KOuUm4xsWUxqZabeofbbpAss9KCKpYfs2rCi` |
| What executable is used to run the installer with the Administrator username and password? | `PsExec.exe` |
| What is the VNC Password? | `5upp0rt9` |

---

### Task 4 — Flags

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the contents of the admin_flag.txt? | `thm{p455w02d_c4n_83_f0und_1n_p141n_73x7_4dm1n_5c21p75}` |

---

## Metodología / Methodology

1. **Reconocimiento / Recon:** escanear con `sudo nmap -sS -sV -Pn <ip>`. Se descubren 6 puertos TCP bajo 1024 abiertos, incluyendo FTP, SMB (139/445) y un servicio web. Enumerar los shares SMB con `smbclient -L //<ip>` o `enum4linux`.
2. **Enumeración SMB / SMB enumeration:** encontrar el share oculto `images$` donde se deben copiar las imágenes. Conectarse al share y subir una **webshell PHP** (p0wny shell) aprovechando que el servidor web sirve el contenido del share.
3. **Acceso inicial / Initial access:** acceder a la webshell desde el navegador (`http://<ip>/shell.php`). Verificar el usuario de la sesión de consola (`sign`) y localizar `user_flag.txt` → `thm{48u51n9_5y573m_func710n4117y_f02_fun_4nd_p20f17}`.
4. **Share administrativo / Administrative share:** descubrir el share oculto no estándar `Installs$`, solo accesible de forma remota con una cuenta administrativa.
5. **Credenciales en texto plano / Plaintext credentials:**
   - Consultar el auto-logon del registro: `Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"` → usuario `.\sign` con contraseña `gKY1uxHLuU1zzlI4wwdAcKUw35TPMdv7PAEE5dAFbV2NxpPJVO7eeSH`.
   - Encontrar el script `Install_www_and_deploy.bat` que contiene la contraseña del Administrador `RCYCc3GIjM0v98HDVJ1KOuUm4xsWUxqZabeofbbpAss9KCKpYfs2rCi` y usa `PsExec.exe` para ejecutar el instalador.
6. **Escalada a Administrador / Escalate to Administrator:** usar `psexec.py` o `wmiexec.py` con las credenciales del Administrador para obtener una shell elevada. Leer `C:\Users\Administrator\Desktop\admin_flag.txt` → `thm{p455w02d_c4n_83_f0und_1n_p141n_73x7_4dm1n_5c21p75}`.
7. **Contraseña VNC / VNC password:** leer `C:\Installs\ultravnc.ini` con el hash `passwd=B3A8F2D8BEA2F1FA70`. Descifrarlo con la herramienta `vncpwd` de Luigi Auriemma (`vncpwd.exe B3A8F2D8BEA2F1FA70`) → `5upp0rt9`.

### Cadena de ataque / Attack Chain

```
Nmap → SMB shares → images$ → PHP webshell upload → Web shell as sign → user_flag.txt → Winlogon auto-logon → sign password → Install_www_and_deploy.bat → Administrator password + PsExec.exe → PsExec/WinRM as Administrator → admin_flag.txt → ultravnc.ini → vncpwd → VNC password
```

**Lección:** las credenciales en texto plano (auto-logon del registro, scripts .bat de instalación) y los shares SMB mal configurados son vectores comunes de compromiso. Los archivos de configuración de VNC almacenan la contraseña ofuscada con un algoritmo débil que se puede descifrar fácilmente.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
