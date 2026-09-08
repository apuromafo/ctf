# AllSignsPoint2Pwnage
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `allsignspoint2pwnage` |
| **Link** | [TryHackMe](https://tryhackme.com/room/allsignspoint2pwnage) |
| **Sección** | Windows / CTF |
| **Fuente** | Writeup de Rich (happycamper84, Medium), cosmicline (GitHub) y MarCorei7 (WordPress) |
| **Componentes** | Windows, SMB (shares ocultos), FTP, webshell PHP (p0wny), Nmap, Winlogon auto-logon, scripts .bat, PsExec, psexec.py/wmiexec.py, VNC (ultravnc.ini, vncpwd) |
| **Impacto** | Máquina Windows de dificultad media. "All signs point to pwnage" — la cadena de ataque combina enumeración de puertos y shares SMB, subida de una webshell PHP, credenciales en texto plano (auto-logon y scripts .bat) y descifrado de la contraseña VNC. |
---
**Contexto:** Máquina Windows de dificultad media. "All signs point to pwnage" — la cadena de ataque combina enumeración de puertos y shares SMB, subida de una webshell PHP, credenciales en texto plano (auto-logon y scripts .bat) y descifrado de la contraseña VNC.
*EN: Medium difficulty Windows machine. "All signs point to pwnage" — the attack chain combines port and SMB share enumeration, uploading a PHP webshell, plaintext credentials (auto-logon and .bat scripts), and VNC password decryption.*
## Solucionario
### Task 1 — Enumeration
**Explicación:** Escaneo con `sudo nmap -sS -sV -Pn <ip>`: hay **6 puertos TCP bajo 1024** abiertos (FTP, SMB 139/445 y web). Con `smbclient -L //<ip>` o `enum4linux` (2> /dev/null) se enumeran los shares SMB y se localiza el share oculto **images$** al que se deben copiar las imágenes.
*EN: Scan with `sudo nmap -sS -sV -Pn <ip>`: 6 TCP ports below 1024 are open (FTP, SMB 139/445 and web). Using `smbclient -L //<ip>` or `enum4linux` the SMB shares are enumerated and the hidden **images$** share is found.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many TCP ports under 1024 are open? | `6` |
| 2 | What is the hidden share where images should be copied to? | `images$` |
### Task 2 — Initial Access
**Explicación:** El servidor web sirve el share `images$`, así que se sube una **webshell PHP (p0wny)** a ese share y se accede desde `http://<ip>/shell.php`. Se determina el usuario de la sesión de consola (**sign**) y se localiza `user_flag.txt`. El share oculto no estándar **Installs$** solo es accesible remotamente como cuenta administrativa.
*EN: The web server serves the `images$` share, so a **PHP webshell (p0wny)** is uploaded and reached at `http://<ip>/shell.php`. The console session user (**sign**) is identified and `user_flag.txt` is found. The hidden non-standard **Installs$** share is only remotely accessible as an administrative account.*

```bash
smbclient //<ip>/images$ -U sign
put shell.php
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What user is signed into the console session? | `sign` |
| 2 | What hidden, non-standard share is only remotely accessible as an administrative account? | `Installs$` |
| 3 | What is the content of user_flag.txt? | `thm{48u51n9_5y573m_func710n4117y_f02_fun_4nd_p20f17}` |
### Task 3 — Privilege Escalation
**Explicación:** Credenciales en texto plano: el auto-logon de `HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` revela el usuario `.\sign` con contraseña `gKY1uxHLuU1zzlI4wwdAcKUw35TPMdv7PAEE5dAFbV2NxpPJVO7eeSH`; el script `Install_www_and_deploy.bat` contiene la contraseña del Administrador `RCYCc3GIjM0v98HDVJ1KOuUm4xsWUxqZabeofbbpAss9KCKpYfs2rCi` y usa **PsExec.exe** para ejecutar el instalador como Administrador. La contraseña VNC se descifra desde `C:\Installs\ultravnc.ini` (hash `passwd=B3A8F2D8BEA2F1FA70`) con `vncpwd` de Luigi Auriemma → `5upp0rt9`.
*EN: Plaintext credentials: the Winlogon auto-logon reveals `.\sign` with password `gKY1uxHLuU1zzlI4wwdAcKUw35TPMdv7PAEE5dAFbV2NxpPJVO7eeSH`; `Install_www_and_deploy.bat` holds the Administrator password `RCYCc3GIjM0v98HDVJ1KOuUm4xsWUxqZabeofbbpAss9KCKpYfs2rCi` and uses **PsExec.exe** to run the installer as Administrator. The VNC password is decrypted from `C:\Installs\ultravnc.ini` (hash `passwd=B3A8F2D8BEA2F1FA70`) with Luigi Auriemma's `vncpwd` → `5upp0rt9`.*

```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```
```bash
vncpwd.exe B3A8F2D8BEA2F1FA70
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the Users Password? | `gKY1uxHLuU1zzlI4wwdAcKUw35TPMdv7PAEE5dAFbV2NxpPJVO7eeSH` |
| 2 | What is the Administrators Password? | `RCYCc3GIjM0v98HDVJ1KOuUm4xsWUxqZabeofbbpAss9KCKpYfs2rCi` |
| 3 | What executable is used to run the installer with the Administrator username and password? | `PsExec.exe` |
| 4 | What is the VNC Password? | `5upp0rt9` |
### Task 4 — Flags
**Explicación:** Con `psexec.py` o `wmiexec.py` y las credenciales del Administrador se obtiene una shell elevada y se lee `C:\Users\Administrator\Desktop\admin_flag.txt`.
*EN: Using `psexec.py` or `wmiexec.py` with the Administrator credentials an elevated shell is obtained and `C:\Users\Administrator\Desktop\admin_flag.txt` is read.*

```
Nmap → SMB shares → images$ → PHP webshell upload → Web shell as sign → user_flag.txt → Winlogon auto-logon → sign password → Install_www_and_deploy.bat → Administrator password + PsExec.exe → PsExec/WinRM as Administrator → admin_flag.txt → ultravnc.ini → vncpwd → VNC password
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the contents of the admin_flag.txt? | `thm{p455w02d_c4n_83_f0und_1n_p141n_73x7_4dm1n_5c21p75}` |
---
**Metodología:** Recon (nmap: 6 puertos) → enumeración SMB (shares, `images$`) → webshell PHP (p0wny) → acceso como `sign` → user flag → credenciales en claro (Winlogon + .bat) → PsExec como Administrador → admin flag → descifrar VNC (ultravnc.ini + vncpwd).
**Learning chain:** shares SMB mal configurados → subida de webshell → credenciales en texto plano (auto-logon, scripts) → ejecución como admin (PsExec) → descifrado del hash VNC.
**MITRE ATT&CK:** T1049 (System Network Connections)/T1190, T1505.003 (Web Shell), T1083 (File and Directory Discovery), T1552.001 (Credentials In Files), T1552.004 (Unsecured Credentials: Private Keys)/registry, T1021.002 (SMB/Windows Admin Shares), T1555/credenciales VNC.
**Fuente:** [TryHackMe - AllSignsPoint2Pwnage](https://tryhackme.com/room/allsignspoint2pwnage)