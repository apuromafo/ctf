# Bandit Nivel 26 - 27

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 26 - 27 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit26@bandit.labs.overthewire.org -p2220` |

# username
bandit26
# password
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
# objective
Good job getting a shell! Now hurry and grab the password for bandit27!
# method of solve
* There is a weird script that is used for the default shell for the bandit26 user:
```
#!/bin/sh

export TERM=linux

exec more ~/text.txt
exit 0
```
* This script reads the contents of the `text.txt` file using the `more` command, and then boots the user out
* We can abuse the `more` command by making the text in the terminal really really big, before running the SSH command to login, which triggers `more`
* From there, we can activate the `vi` text editor inside of the `more` command by pressing `v`
* From there, we can use a `vi` method of shell escape
```
:set shell=/usr/bin/bash
:shell
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
