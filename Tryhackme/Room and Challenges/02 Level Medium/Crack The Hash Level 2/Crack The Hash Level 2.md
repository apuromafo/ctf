# Crack The Hash Level 2
| **Dificultad** | Medium |
| **Tipo** | CTF |
| **Slug** | `crackthehashlevel2` |
| **Link** | [TryHackMe](https://tryhackme.com/room/crackthehashlevel2) |
| **Sección** | 02 Level Medium |
| **Fuente** | TryHackMe |
| **Componentes** | Haiti, Hashcat, John the Ripper, wordlistctl, SecLists, CeWL, TTPassGen, Lyricpass, pnwgen, reglas de hashcat/john, MD5, SHA-1, RIPEMD-320, Keccak-256, SHA3-512, Blake2, sha512crypt |
| **Impacto** | Rompe 14 hashes reales combinando identificación de hash, wordlists, reglas y generación de diccionarios personalizados. |
---
**Contexto:** Sala tipo reto centrada en el cracking de hashes de nivel 2. Convierte el proceso en un flujo completo: identificar el tipo de hash con Haiti, aplicar los códigos de Hashcat/John, gestionar wordlists con wordlistctl, generar diccionarios personalizados (reglas, CeWL, TTPassGen, Lyricpass, pnwgen) y finalmente resolver los nueve "consejos" con los hashes propuestos.
## Solucionario
### Task 1: Introduction
**Explicación:** Tarea introductoria de la sala. Solo se prepara el entorno para comenzar el reto de cracking de hashes.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción y despliega el entorno para comenzar. | `No answer needed` |
### Task 2: Hash Identification
**Explicación:** La identificación del tipo de hash es el primer paso. **Haiti** es la herramienta que detecta el formato probable de un hash. Con el primer hash detectamos RIPEMD-320 y con el segundo Keccak-256. Una vez identificado, hay que conocer dos cosas clave para crackearlo: el **código de Hashcat** (número de módulo, `17800`) y el **código de John the Ripper** (nombre de formato, `raw-keccak-256`).

```bash
haiti 741ebf5166b9ece4cca88a3868c44871e8370707cf19af3ceaa4a6fba006f224ae03f39153492853
# RIPEMD-320 [JtR: dynamic_150]

haiti 1aec7a56aa08b25b596057e1ccbcb6d768b770eaa0f355ccbd56aee5040e02ee
# Keccak-256 [HC: 17800] [JtR: raw-keccak-256]
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lanza Haiti sobre el hash `741ebf5166b9ece4cca88a3868c44871e8370707cf19af3ceaa4a6fba006f224ae03f39153492853`. | `No answer needed` |
| 2 | ¿Qué tipo de hash es? | `RIPEMD-320` |
| 3 | Lanza Haiti sobre el hash `1aec7a56aa08b25b596057e1ccbcb6d768b770eaa0f355ccbd56aee5040e02ee`. | `No answer needed` |
| 4 | ¿Cuál es el código de Hashcat para Keccak-256? | `17800` |
| 5 | ¿Cuál es el código de John the Ripper para Keccak-256? | `raw-keccak-256` |
### Task 3: Wordlists
**Explicación:** Para el cracking a menudo se necesitan diccionarios especializados. **SecLists** es una colección de listas (usernames, passwords, URLs, fuzzing, web shells, etc.). **wordlistctl** es un script que permite buscar, instalar, actualizar y descargar archivos de wordlists desde sitios web (más de 6300 wordlists disponibles). La opción `-l` hace que las búsquedas se realicen en archivos locales en lugar de remotos.

```bash
git clone https://github.com/BlackArch/wordlistctl.git
wordlistctl search rockyou
wordlistctl search -l rockyou
# /usr/share/wordlists/passwords/rockyou.txt
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Instala y ejecuta `wordlistctl` para buscar wordlists. | `No answer needed` |
| 2 | ¿Qué opción necesitas añadir al comando anterior para buscar en archivos locales en lugar de remotos? | `-l` |
| 3 | Ejecuta `wordlistctl search -l rockyou` de nuevo. | `No answer needed` |
| 4 | Si ejecutas `wordlistctl search -l rockyou` una vez más, ¿cuál es la ruta donde se almacena la wordlist? | `/usr/share/wordlists/passwords/rockyou.txt` |
| 5 | ¿Cuál es el nombre de la primera wordlist de la categoría de usernames? | `CommonAdminBase64` |
### Task 4: Custom wordlist generation
**Explicación:** No siempre basta con wordlists de fábrica; hay que generar diccionarios personalizados. Aquí se parte de una lista base (por ejemplo `10k-most-common.txt`) y se aplican **reglas** de John/Hashcat para probar mutaciones. El comando de John usa la regla `THM01` (añadir dos dígitos al final `$[0-9]$[0-9]`) para crackear el hash SHA-1 `2d5c517a4f7a14dcb38329d228a7d18a3b78ce83`.

```bash
# johny-local.conf - [List.Rules:THM01] $[0-9]$[0-9]
john hash.txt --format=raw-sha1 --wordlist=/usr/share/wordlists/passwords/10k-most-common.txt --rules=THM01
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descarga/instala las wordlists base indicadas en la tarea. | `No answer needed` |
| 2 | Genera la wordlist personalizada a partir del archivo base y las reglas indicadas. | `No answer needed` |
| 3 | ¿Cuál fue la contraseña obtenida al crackear el hash `2d5c517a4f7a14dcb38329d228a7d18a3b78ce83`? | `moonligh56` |
### Task 5: Generación de diccionarios con CeWL y TTPassGen
**Explicación:** Continuando con la generación de diccionarios personalizados: con wordlists de "nombres de perros" (dogs) se genera `dogs_custom.txt` para crackear el MD5 `ed91365105bba79fdab20c376d83d752`. **CeWL** extrae palabras clave de un sitio web (`cewl -d 2 -w example.txt https://example.org`) para fabricar diccionarios a medida. **TTPassGen** permite generar wordlists mediante reglas (pines numéricos, combinaciones con separadores de guion) y con ellas se construye `combination.txt`.

```bash
john md5.txt --format=Raw-MD5 --wordlist=/usr/share/wordlists/misc/dogs_custom.txt
cewl -d 2 -w example.txt https://example.org
ttpassgen --rule '[?d]{4:4:*}' pin.txt
ttpassgen --rule '[?l]{1:3:*}' abc.txt
ttpassgen --dictlist 'pin.txt,abc.txt' --rule '$0[-]{1}$1' combination.txt
john combi_hash.txt --format=Raw-MD5 --wordlist=combination.txt
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Instala las wordlists de la categoría de mascotas/perros y genera la wordlist `dogs_custom.txt`. | `No answer needed` |
| 2 | Descarga la plataforma/lista necesaria para generar el diccionario personalizado. | `No answer needed` |
| 3 | Crackea el siguiente hash MD5 con la wordlist generada en los pasos anteriores: `ed91365105bba79fdab20c376d83d752`. | `mOlo$$u$` |
| 4 | Ejecuta CeWL sobre `https://example.org` con profundidad 2 guardando en `example.txt`. | `No answer needed` |
| 5 | ¿Cuál es la última palabra de la lista generada? | `information` |
| 6 | Instala TTPassGen. | `No answer needed` |
| 7 | Genera `pin.txt` (pines de 4 dígitos) y `abc.txt` (caracteres de longitud 1 a 3). | `No answer needed` |
| 8 | Combina ambos archivos en `combination.txt` con un separador de guion entre ellos. | `No answer needed` |
| 9 | Crackea este hash MD5 con `combination.txt`: `e5b47b7e8df2597077e703c76ee86aee`. | `1551-li` |
### Task 6: Time to crack the hashes
**Explicación:** Ronda final de hashes, cada uno con un "consejo" distinto que indica cómo generar el diccionario adecuado:
1. Nombres masculinos con reglas (Zachariah1234*).
2. Nombres femeninos con reglas (Angelita35!).
3. Wordlist personalizada (Tl@xc@l@ncing0).
4. Regla `NT` de John sobre Raw-SHA1 (DavIDgUEtTApAn).
5. Letras de Adele con Lyricpass y regla `r` (reverso de la cadena).
6. Números de teléfono con pnwgen usando el prefijo +1721 (Sint Maarten).
7. Hashcat módulo `17600` (SHA3-512).
8. Regla con menos palabras repetidas sobre Raw-Blake2.
9. `sha512crypt` con rockyou.

```bash
john --format=Raw-MD5 hash1.txt --wordlist=malenames-usa-top1000.txt --rules=task01
john --format=Raw-SHA1 hash4.txt --wordlist=hash4_name.txt --rules=NT
lyricpass.py -a Adele
john --format=Raw-MD5 hash5.txt --wordlist=lyrics.txt --rules=r
pnggen  (7 dígitos, prefijo +1721)
hashcat -m 17600 hash7.txt wordlist.txt
john --format=Raw-Blake2 hash8 --wordlist=hash8_final.txt
john --format=sha512crypt hash9.txt --wordlist=/usr/share/wordlists/rockyou.txt
```
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Advice n°1: crackea `b16f211a8ad7f97778e5006c7cecdf31` (MD5). | `Zachariah1234*` |
| 2 | Advice n°2: crackea `7463fcb720de92803d179e7f83070f97` (MD5). | `Angelita35!` |
| 3 | Advice n°3: crackea `f4476669333651be5b37ec6d81ef526f` (MD5). | `Tl@xc@l@ncing0` |
| 4 | Advice n°4: crackea `a3a321e1c246c773177363200a6c0466a5030afc` (SHA-1). | `DavIDgUEtTApAn` |
| 5 | Advice n°5: crackea `d5e085772469d544a447bc8250890949` (MD5). | `uoy ot miws ot em rof peed oot ro ediw oot si revir oN` |
| 6 | Advice n°6: crackea `377081d69d23759c5946a95d1b757adc` (MD5). | `+17215440375` |
| 7 | Advice n°7: crackea `ba6e8f9cd4140ac8b8d2bf96c9acd2fb58c0827d556b78e331d1113fcbfe425ca9299fe917f6015978f7e1644382d1ea45fd581aed6298acde2fa01e7d83cdbd` (SHA3-512). | `!@#redrose!@#` |
| 8 | Advice n°8: crackea `9f7376709d3fe09b389a27876834a13c6f275ed9a806d4c8df78f0ce1aad8fb343316133e810096e0999eaf1d2bca37c336e1b7726b213e001333d636e896617` (Blake2). | `hackinghackinghackinghacking` |
| 9 | Advice n°9: crackea `$6$kI6VJ0a31.SNRsLR$Wk30X8w8iEC2FpasTo0Z5U7wke0TpfbDtSwayrNebqKjYWC4gjKoNEJxO/DkP.YFTLVFirQ5PEh4glQIHuKfA/` (sha512crypt). | `kakashi1` |
### Task 7: Conclusion
**Explicación:** Fin de la sala; repaso del flujo completo de cracking (identificar, elegir módulo/formato, wordlist correcta, reglas y herramientas de generación de diccionarios).
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Conclusión de la sala. | `No answer needed` |
---
**Metodología:** Ataque offline de credenciales (cracking de hashes) con wordlists, reglas y diccionarios generados a medida.
**Learning chain:** Identificación de hash (Haiti) → módulos Hashcat/John → gestión de wordlists (wordlistctl/SecLists) → generación de diccionarios (CeWL, TTPassGen, Lyricpass, pnwgen, reglas) → cracking final.
**MITRE ATT&CK:** T1110.002 (Brute Force: Password Cracking), T1003 (OS Credential Dumping, hash catching).
**Fuente:** [TryHackMe - Crack The Hash Level 2](https://tryhackme.com/room/crackthehashlevel2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
