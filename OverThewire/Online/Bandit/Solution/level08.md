# Bandit Nivel 8 - 9

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 8 - 9 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit8@bandit.labs.overthewire.org -p2220` |

# Username
bandit8
# Password
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
# Method of solve
Locate the line in the file that occurs only once. Use the sort command to organize the data in the groups, then the uniq command with the -c flag to output the number of times each line appears in the file, then the sort command again to return the least occuring lines at the end of the list.
```
sort data.txt | uniq -c | sort
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
