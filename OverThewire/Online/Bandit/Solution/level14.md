# Bandit Nivel 14 - 15

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 14 - 15 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit14@bandit.labs.overthewire.org -p2220` |

# username
bandit14
# password
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
# method of solve
The instructions tell us we need to send the password for the current level to localhost port 30000. We can do so with the netcat program
```
nc localhost 30000
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```
We can also do this as a one-liner if we use the echo and a pipe:
```
echo 'MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS' | nc localhost 30000
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
