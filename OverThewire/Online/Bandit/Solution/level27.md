# Bandit Nivel 27 - 28

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 27 - 28 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit27@bandit.labs.overthewire.org -p2220` |

# username
bandit27
# password
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
# level description
* There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.
* Clone the repository and find the password for the next level.
# method of solve
* there is a github repo hosted on the ssh service on the localhost, so we have to use ssh to access it
* use this command (we need to be located in a publicly writable directory first)
```
git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
```
* after that, the password is in the README file in the repo
```
cd repo
cat README
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
