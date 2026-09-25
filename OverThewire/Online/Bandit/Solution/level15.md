# Bandit Nivel 15 - 16

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Bandit |
| **Nivel / Level** | 15 - 16 |
| **URL** | https://overthewire.org/wargames/bandit/ |
| **Conexión** | `ssh bandit15@bandit.labs.overthewire.org -p2220` |

# username
bandit15
# password
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
# objective
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.
# method of solve
We can use OpenSSL to send the password:
```
echo '8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo' | openssl s_client -quiet -connect localhost:30001
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
