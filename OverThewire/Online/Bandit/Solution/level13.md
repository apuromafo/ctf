# Bandit Nivel 13 - 14

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 13 - 14 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit13@bandit.labs.overthewire.org -p2220` |

# username
bandit13
# password
FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
# method of solve
Use the SSH private key to login to the next level
```
scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private .
chmod 600 sshkey.private
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
cat /etc/bandit_pass/bandit14
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
