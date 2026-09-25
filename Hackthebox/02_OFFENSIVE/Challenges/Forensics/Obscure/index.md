# Obscure [EASY]

> **ES:** Challenge Forensics Easy: un atacante subió una webshell PHP ofuscada (`support.php`) a un Apache; se entrega un PCAP corto de `tcpdump` (dos minutos antes de cortar el HTTP). Hay que desofuscar la shell, entender su protocolo (Base64+XOR+gzip con marcadores) y decodificar las respuestas del PCAP para reconstruir los comandos (`id`, `ls /home/*`, `chdir /home/developer`, exfiltración de `pwdb.kdbx`) y abrir la base KeePass para la flag (`HTB{...}`).
> **EN:** Easy Forensics challenge: an attacker uploaded an obfuscated PHP webshell (`support.php`) to an Apache server; a short `tcpdump` PCAP (two minutes before HTTP was cut) is provided. Deobfuscate the shell, understand its protocol (Base64+XOR+gzip with markers), and decode the PCAP responses to rebuild the commands (`id`, `ls /home/*`, `chdir /home/developer`, `pwdb.kdbx` exfiltration) and open the KeePass database for the flag (`HTB{...}`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Forensics |
| **Dificultad** | Easy |
| **Estado** | Retired (challenge antiguo con writeups públicos desde 2020; sin flag literal aquí por criterio de la colección) |
| **URL** | https://app.hackthebox.com/challenges/Obscure [verificar slug exacto] |
| **Archivos** | `Obscure.zip` → `support.php` + `19-05-21_22532255.pcap` + `to-do.txt` [verificar nombres exactos] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | [verificar] (nota previa local: 3pts, sistema de puntuación antiguo) |

---

## 🎯 Objetivo / Goal

> **ES:** Desofuscar `support.php` (claves y marcadores del protocolo), filtrar los POST/respuestas en el PCAP, invertir la codificación de cada respuesta y reconstruir la secuencia del atacante hasta extraer `pwdb.kdbx`, crackearlo y leer la flag en KeePass.
> **EN:** Deobfuscate `support.php` (protocol keys and markers), filter POSTs/responses in the PCAP, reverse each response's encoding, and rebuild the attacker sequence through extracting `pwdb.kdbx`, cracking it, and reading the flag in KeePass.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `unzip`, `file` (extracción y triage)
- [ ] PHP CLI (`php`) + editor (desofuscación imprimiendo `$u` sin ejecutar la shell)
- [ ] Wireshark/`tshark` (filtro `http.request or http.response`, extracción de cuerpos)
- [ ] Script PHP/Python propio (inversa: quitar `$p/$kh/$kf` → `base64_decode` → XOR con `$k` → `gunzip`)
- [ ] `base64`, `keepass2john`, `hashcat -m 13400` (o `john`), KeePass + `rockyou.txt`

---

## 📋 Pasos / Steps

### Paso 1 — Triage: qué hay en el zip / Triage the zip

> **ES:** El `to-do.txt` describe el incidente: subida arbitraria de PHP, shell ofuscada y PCAP de dos minutos. Se descomprime y se confirma el contenido.
> **EN:** `to-do.txt` describes the incident: arbitrary PHP upload, obfuscated shell, two-minute PCAP. Extract and confirm contents.

```bash
unzip -o Obscure.zip -d obscure/ && file obscure/*
# esperado: support.php (PHP), *.pcap (tcpdump capture), to-do.txt (texto)
cat obscure/to-do.txt
```

**Resultado / Result:** Tres ficheros: `support.php`, PCAP `19-05-21_22532255.pcap` y `to-do.txt` con el contexto del incidente.

### Paso 2 — Desofuscar la webshell / Deobfuscate the webshell

> **ES:** `support.php` esconde el código con `str_replace('u)','',...)` (y variante `FD...create_function`). En vez de ejecutarlo, se imprime la variable construida `$u` y se muere antes de `eval`. El código real usa clave XOR `$k="80e32263"`, marcadores `$kh="6f8af44abea0"` / `$kf="351039f4a7b5"`, prefijo `$p="0UlYyJHG87EJqEz6"`, y flujo petición `base64_decode→XOR→gzuncompress→eval` / respuesta `gzcompress→XOR→base64` envuelta como `$p$kh$r$kf`.
> **EN:** `support.php` hides its code with `str_replace('u)','',...)` (and a `FD...create_function` variant). Instead of running it, print the built `$u` variable and exit before `eval`. The real code uses XOR key `$k="80e32263"`, markers `$kh="6f8af44abea0"` / `$kf="351039f4a7b5"`, prefix `$p="0UlYyJHG87EJqEz6"`, and request flow `base64_decode→XOR→gzuncompress→eval` / response flow `gzcompress→XOR→base64` wrapped as `$p$kh$r$kf`.

```bash
cp obscure/support.php deobf.php
# editar deobf.php: sustituir la línea de ejecución por impresión:
#   $x=$N('',$u);$x();   →   print_r($u); die();
php deobf.php | fold -w 200 | head -20
# esperado: $k/$kh/$kf/$p + function x($t,$k){XOR} + preg_match("/$kh(.+)$kf/", php://input) + eval/gzuncompress ...
```

**Resultado / Result:** Protocolo recuperado: las peticiones POST llevan `$kh + base64 + $kf` y las respuestas devuelven `$p$kh base64 $kf` (paráfrasis de rafidghanim y Mateo Galagorri).

### Paso 3 — PCAP: filtrar POSTs y extraer las 4 respuestas / Filter POSTs and extract the 4 responses

> **ES:** En Wireshark se filtra por `http.request or http.response`; hay cuatro POST sospechosos con el formato de la shell. Se exportan los cuerpos de respuesta (`$r` envuelto).
> **EN:** In Wireshark filter by `http.request or http.response`; there are four suspicious POSTs matching the shell format. Export the response bodies (wrapped `$r`).

```bash
tshark -r obscure/19-05-21_22532255.pcap -Y 'http.request.method==POST' -T fields -e http.file_data | head -4
# esperado: 4 líneas con 6f8af44abea0 ... 351039f4a7b5 (peticiones)
tshark -r obscure/19-05-21_22532255.pcap -Y 'http.response' -T fields -e http.file_data > responses.txt
wc -l responses.txt
# esperado: 4 respuestas con 0UlYyJHG87EJqEz66f8af44abea0 ... 351039f4a7b5
```

**Resultado / Result:** 4 pares petición/respuesta con el formato de la webshell aislados.

### Paso 4 — Invertir cada respuesta y reconstruir los comandos / Reverse each response

> **ES:** Cada respuesta se invierte quitando `$p/$kh/$kf` y aplicando `base64_decode → XOR($k) → gunzip` (el XOR es simétrico, reaplicarlo descifra). Un mini-script PHP automatiza los 4.
> **EN:** Each response is reversed by stripping `$p/$kh/$kf` and applying `base64_decode → XOR($k) → gunzip` (XOR is symmetric, reapplying it decrypts). A tiny PHP script automates all 4.

```bash
cat > decode.php <<'EOF'
<?php
$k="80e32263"; $kh="6f8af44abea0"; $kf="351039f4a7b5"; $p="0UlYyJHG87EJqEz6";
function x($t,$k){$c=strlen($k);$l=strlen($t);$o="";for($i=0;$i<$l;){for($j=0;($j<$c&&$i<$l);$j++,$i++){$o.=$t[$i]^$k[$j];}}return $o;}
foreach(file("responses.txt",FILE_IGNORE_NEW_LINES|FILE_SKIP_EMPTY_LINES) as $r){
  $b=str_replace([$p,$kh,$kf],"",$r);
  print(gzuncompress(x(base64_decode($b),$k))."\n---\n");
}
EOF
php decode.php
# esperado (paráfrasis):
# 1) uid=33(www-data) ...            ← comando `id`
# 2) listado de /home/*              ← comando `ls -lah /home/*`
# 3) /home/developer                 ← `chdir('/home/developer')`
# 4) blob Base64 largo               ← `base64 -w 0 pwdb.kdbx`
```

**Resultado / Result:** Secuencia del atacante reconstruida: `id` → `ls /home/*` → salto a `/home/developer` → exfiltración de `pwdb.kdbx` en Base64. El 4.º resultado es el contenido de la base KeePass codificada.

### Paso 5 — Recuperar pwdb.kdbx, crackear y leer la flag / Recover, crack and read

> **ES:** El Base64 del 4.º resultado se decodifica a `pwdb.kdbx` (verificado con `file`), se extrae su hash con `keepass2john` y se crackea con `hashcat -m 13400` + `rockyou` (contraseña débil de diccionario). Con ella se abre la base en KeePass y aparece la entrada con la flag.
> **EN:** The 4th result's Base64 decodes to `pwdb.kdbx` (verified with `file`), its hash is extracted with `keepass2john` and cracked with `hashcat -m 13400` + `rockyou` (weak dictionary password). Open the database in KeePass with it and the flag entry appears.

```bash
php decode.php | awk '/---/{n++} n==3' > b64kdbx.txt  # 4.º bloque (ajustar índice)
base64 -d b64kdbx.txt > pwdb.kdbx
file pwdb.kdbx
# esperado: KeePass password database 2.x KDBX
keepass2john pwdb.kdbx > kdbx.hash
hashcat -m 13400 kdbx.hash /usr/share/wordlists/rockyou.txt
# esperado: contraseña de diccionario recuperada (ver fuentes citadas)
# Abrir pwdb.kdbx en KeePass/KeePassXC con esa contraseña → entrada con HTB{...}
```

**Resultado / Result:** `pwdb.kdbx` válida, contraseña crackeada por diccionario y flag `HTB{...}` legible en KeePass (no se reproduce literal aquí por criterio de la colección; ver capturas en las fuentes citadas). [verificar] reproducción propia con captura en `img/`.

---

## 🧠 Lo aprendido / Learned

- [ ] Patrón China-chopper-like en PHP: `preg_match(marcadores, php://input)` + `base64+XOR+gzip+eval`; desofuscar imprimiendo la variable construida es más seguro que ejecutar.
- [ ] XOR con clave repetida es simétrico: el mismo `x()` cifra y descifra; quitar envoltorios (`$p/$kh/$kf`) antes de decodificar es el paso que más se olvida.
- [ ] En PCAP, filtrar `http.request or http.response` y correlacionar petición/respuesta por marcadores evita perderse entre tráfico irrelevante.
- [ ] `base64 -w 0 <fichero>` en la respuesta = exfiltración: el tamaño del 4.º bloque delata al `.kdbx` antes de decodificarlo.
- [ ] KeePass 2.x se audita con `keepass2john` + `hashcat -m 13400`; una contraseña de diccionario cae con `rockyou` (lección reutilizable para cualquier `.kdbx`).

---

## 📚 Fuentes y Referencias / Sources

- **Writeup de referencia:** [Hack The Box - Obscure — rafidghanim](https://rafidghanim.github.io/posts/HackTheBox-Obscure-Forensic-Writeup) — rafidghanim, 2024-11-23 (Challenge: Obscure [Easy]; `Obscure.zip` con `19-05-21_22532255.pcap`+`support.php`+`to-do.txt`; desofuscación vía `print_r($u)`, claves `$k/$kh/$kf/$p`, 4 payloads `id`/`ls /home/*`/`chdir /home/developer`/`base64 pwdb.kdbx`, crackeo con John y flag en KeePass)
- **Writeup de referencia:** [Obscure Easy Challenge - Hack the Box — Mateo Galagorri](https://mateogal.com/posts/obscure/) — Mateo Galagorri, 2025-04-22 (challenge forense Easy; script inverso `str_replace`+`base64_decode`+XOR+`gzuncompress`, 4 respuestas decodificadas `uid=33(www-data)`/`/home/developer`/listado/`pwdb.kdbx`, `keepass2john`+`hashcat -m 13400`+rockyou)
- **Hilo oficial:** [Obscure Challenge](https://forum.hackthebox.com/t/obscure-challenge/1866) — Hack The Box :: Forums (discusión oficial del challenge)
- **Nota local previa:** stub raíz `Soluciones/Challenges/obscure.md` ("Points: 3pts") migrado a esta plantilla
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
