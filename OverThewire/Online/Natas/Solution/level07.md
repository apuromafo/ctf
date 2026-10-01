# Natas Nivel 7 → 8

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 7 → 8 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas7.natas.labs.overthewire.org` |

# Username
natas7
# Password
bmg8SvU1LizuWjx3y7xkNERkHxGre0GS
# Web vulnerability
Local file inclusion through the `page` URL parameter
# Method of solve
Access the password on the webserver by providing the following file path:
http://natas7.natas.labs.overthewire.org/index.php?page=../../../../../../etc/natas_webpass/natas8

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/natas/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
