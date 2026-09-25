# Bandit Nivel 30 - 31

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 30 - 31 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit30@bandit.labs.overthewire.org -p2220` |

# username
bandit30
# password
qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL
# objective
* There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.
* Clone the repository and find the password for the next level.
# method of solve
* we need to git clone this repo as well, like all the rest
```
git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
```
* there's nothing in the git logs, and nothing in the git branches, but there's a weird looking tag
```
git show-ref --tags
```
* We can look at the the secret tag by using this command:
```
git show secret
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
