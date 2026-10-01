# Natas Nivel 12 → 13

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 12 → 13 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas12.natas.labs.overthewire.org` |

# Username
natas12
# Password
yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB
# Web vulnerability
Insecure file upload, client-side filter bypass
# Method of solve
Upload a malicious php file, but replay the request in Burpsuite, and adjust the file extension, setting it back to PHP, then access the file in the web app, because we are given the file path for the uploaded file.
This is the PHP one-liner to read the password file
```
<?php echo file_get_contents('/etc/natas_webpass/natas13'); ?>
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
