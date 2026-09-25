# Natas Nivel 8 → 9

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 8 → 9 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas8.natas.labs.overthewire.org` |

# Username
natas8
# Password
xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q
# Web vulnerability
Exposed sourcecode. Sensitive data acquired by reverse engineering source code.
# Method of solve
Reverse the encryption function and obtain the password.
```
<?

$secret = "3d3d516343746d4d6d6c315669563362";

function decodeSecret($secret) {
    return base64_decode(strrev(hex2bin($secret)));
}
print(decodeSecret($secret));
?>
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
