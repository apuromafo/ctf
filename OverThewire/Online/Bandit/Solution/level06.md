# Bandit Nivel 6 - 7

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 6 - 7 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit6@bandit.labs.overthewire.org -p2220` |

# Username
bandit6
# Password
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
# Method of solve
Use the Find command again to locate the file
```
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat /var/lib/dpkg/info/bandit7.password
```

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/bandit/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
