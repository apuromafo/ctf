# Bandit Nivel 12 - 13

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 12 - 13 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit12@bandit.labs.overthewire.org -p2220` |

# username
bandit12
# password
7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
# method of solve
Reverse the hex dump file with the XXD program
```
mkdir /tmp/...bandit12theshyhat
cp data.txt /tmp/...bandit12theshyhat/data.txt
cd /tmp/...bandit12theshyhat
file data
mv data data.gz
gunzip data.gz
file data
mv data data.bz2
bzip2 -d data.bz2
file data
mv data data.gz
gunzip data.gz
file data
mv data data.tar
tar -xf data.tar
file data5.bin
mv data5.bin data5.tar
tar -xf data5.tar
file data6.bin
mv data6.bin data6.tar
tar -xf data6.tar
mv data6.bin data6.bz2
bzip2 -d data6.bz2
file data6
mv data6 data6.tar
tar -xf data6.tar
file data8.bin
mv data8.bin data8.gz
gunzip data8.gz
file data8
cat data8
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
