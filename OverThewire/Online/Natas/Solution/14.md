# Natas Nivel 14 → 15

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 14 → 15 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas14.natas.labs.overthewire.org` |

# Username
natas14
# Password
z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ
# Web vulnerability
SQL injection, login bypass
# Method of solve
The app simulates a login page where it communicates with a database and grants access if the username and password match one that's in the database. The code directly references the user input into the resulting SQL statement, which leaves it open to SQL injection. There's a well-known SQL injection payload that allows bypass of login pages by providing a true statement to the system. It looks like the following
```
" or 1=1 -- 
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
