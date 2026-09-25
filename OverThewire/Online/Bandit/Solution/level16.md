# Bandit Nivel 16 - 17

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 16 - 17 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit16@bandit.labs.overthewire.org -p2220` |

# username
bandit16
# password
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
# objective
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000
# method of solve
The first thing we need to do is figure out which ports in the range are hosting the SSL service:
```
nmap -p31000-32000 -vv -sV localhost
```
One of the ports is serving SSL, so we send that port the password
```
echo 'kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx' | openssl s_client -quiet -connect localhost:31790
```
We receive a SSH private key as the response, so we'll need to create a private key for the next level

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/bandit/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
