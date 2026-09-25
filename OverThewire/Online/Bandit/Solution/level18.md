# Bandit Nivel 18 - 19

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 18 - 19 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit18@bandit.labs.overthewire.org -p2220` |

# username
bandit18
# password
x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
# objective
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.
# method of solve
The system logs you out as soon as you login, so we can run SSH with an argument to read the password file as soon as we login:
```
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
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
