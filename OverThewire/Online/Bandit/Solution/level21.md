# Bandit Nivel 21 - 22

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 21 - 22 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit21@bandit.labs.overthewire.org -p2220` |

# username
bandit21
# password
EeoULMCra2q0dSkYj561DX7s1CpBuOBt
# objective
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
# method of solve
The first thing we should do is enumerate the cron.d directory's contents:
```
ls -la /etc/cron.d/
```
Let's read the cronjob for bandit22:
```
cat /etc/cron.d/cronjob_bandit22
```
And then let's take a look at the script that's being run:
```
cat /usr/bin/cronjob_bandit22.sh
```
This script makes a file in the /tmp directory readable by all users, then copies the password for the bandit22 user into it, so let's read it:
```
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
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
