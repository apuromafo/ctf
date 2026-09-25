# Bandit Nivel 9 - 10

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 9 - 10 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit9@bandit.labs.overthewire.org -p2220` |

# Username
bandit9
# Password
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
# Method of solve
We need to use the Strings command to output human-readable strings from the data.txt, and use the Grep command to only return lines with a specific pattern by using commmand piping
```
strings data.txt | grep '===='
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
