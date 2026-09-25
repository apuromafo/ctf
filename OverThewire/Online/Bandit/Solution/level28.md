# Bandit Nivel 28 - 29

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 28 - 29 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit28@bandit.labs.overthewire.org -p2220` |

# username
bandit28
# password
Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
# objective
* There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.
* Clone the repository and find the password for the next level
# method of solve
* we need to clone the repository like we did in the previous level
```
git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
```
* from here, we take a look at the README.md file, and it looks like the password was redacted
* to take a look at the history for the README.md file, we use this command
```
git log -p
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
