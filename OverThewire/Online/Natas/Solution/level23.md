# Natas Nivel 23 → 24

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 23 → 24 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas23.natas.labs.overthewire.org` |

# username
natas23
# password
dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs
# web app vulnerability
PHP type juggling
# method of solve
There are two requirements for the password that needs to be submitted to receive the credentials for the next level
```
<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>  
```
This code requires that the password contain the string `iloveyou` in it, and it also requires that the password be larger than the integer 10. We need to abuse the way PHP treats strings, and prefix the `iloveyou` string with a number that is greater than the number 10, since the greater-than comparison operator will convert strings to numbers before comparison, so we can use the string `11iloveyou` to fulfill both requirements for the password. The strstr function ensures that the indicated string is included in the password, so `11iloveyou` qualifies.

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/natas/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
