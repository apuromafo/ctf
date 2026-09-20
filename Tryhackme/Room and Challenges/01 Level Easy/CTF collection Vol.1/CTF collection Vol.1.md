# CTF collection Vol.1

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | CTF / Cryptography & Forensics (mini challenges) | `ctfcollectionvol1` | https://tryhackme.com/room/ctfcollectionvol1 | 01 Level Easy | TryHackMe | Base64 / ExifTool / Steghide / HTML / QR (zbarimg) / strings / base58 / César / PNG header (ghex) / BF (binaryfuck) / XOR / binwalk / stegsolve / SoundCloud / Wayback Machine / Vigenère / dec->hex->ascii / Wireshark | Colección de mini-CTFs de criptografía y esteganografía para practicar decodificación, estego, ingeniería inversa básica y análisis de tráfico de menor a mayor dificultad. |

---

**Contexto:** Sala compuesta por 21 minirretos independientes que cubren un abanico de técnicas clásicas de CTF: decodificación Base64, metadatos EXIF, esteganografía con steghide y stegsolve, texto oculto en HTML, códigos QR, strings en binarios, base58, cifrado de César, reparación de cabeceras PNG, weird-languages (brainfuck), XOR, binwalk, Wayback Machine, Vigenère, conversión dec->hex->ascii y análisis de capturas con Wireshark.

> **ES:** "Veinte y un retos de nivel fácil que te hacen pasar por decodificación, esteganografía, forense de imágenes y ficheros, y análisis de tráfico, con pistas para cada uno."
> **EN:** "21 beginner-friendly challenges that take you through decoding, steganography, file forensics and traffic analysis, with a hint for each one."

## Solucionario

### Task 1: Nota del autor / Author note

**Explicación:** El autor presenta la sala y explica cómo funcionará. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He leído la nota del autor. / I've read the author note. | `No answer needed` |

---

### Task 2: ¿Qué dice la base? / What does the base said?

**Explicación:** Se entrega la cadena `VEhNe2p1NTdfZDNjMGQzXzdoM19iNDUzfQ==`, que termina en `==`, señal inequívoca de Base64. Se decodifica con CyberChef (o `base64 -d`) y se obtiene la bandera.

```bash
echo "VEhNe2p1NTdfZDNjMGQzXzdoM19iNDUzfQ==" | base64 -d
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Puedes decodificar el mensaje en Base64? / Can you decode the Base64 message? | `THM{ju57_d3c0d3_7h3_b453}` |

---

### Task 3: Meta meta

**Explicación:** Se entrega una imagen cuya bandera está oculta en los metadatos. Con `exiftool` se listan los metadatos EXIF y, revisando el campo del propietario (owner), aparece la bandera.

```bash
exiftool imagen.jpg
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Inspecciona los metadatos EXIF de la imagen. ¿Cuál es la bandera? / Inspect the EXIF metadata of the image. What is the flag? | `THM{3x1f_0r_3x17}` |

---

### Task 4: Mon, ¿vamos a estar bien? / Mon, are we going to be okay?

**Explicación:** Algo está oculto dentro del fichero. Con steghide se extrae la información incrustada: `steghide extract -sf <fichero>`. Acepta la contraseña vacía (solo Enter) y se lee el fichero de texto extraído para obtener la bandera.

```bash
steghide extract -sf <fichero>
# Sin passphrase (Enter), se extrae un .txt con la bandera.
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Extrae lo que está escondido con steghide. ¿Cuál es la bandera? / Extract what is hidden with steghide. What is the flag? | `THM{500n3r_0r_l473r_17_15_0ur_7urn}` |

---

### Task 5: Erm......Magick

**Explicación:** Hay texto oculto junto a la pregunta. Se resalta el texto aparentemente vacío de la página (o se inspecciona el HTML del reto) y aparece la bandera en texto blanco.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Busca el texto oculto en la página/HTML. ¿Cuál es la bandera? / Find the hidden text in the page/HTML. What is the flag? | `THM{wh173_fl46}` |

---

### Task 6: QRrrrr

**Explicación:** Se descarga un código QR y se decodifica con `zbarimg` (zbar). La salida del escáner es directamente la bandera.

```bash
sudo apt install zbar-tools
zbarimg qr.png
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Decodifica el código QR. ¿Cuál es la bandera? / Decode the QR code. What is the flag? | `THM{qr_m4k3_l1f3_345y}` |

---

### Task 7: ¿Lo inviertes o lo lees? / Reverse it or read it?

**Explicación:** Se entrega un binario. En lugar de usar Radare2, se aplica el atajo clásico: `strings` sobre el fichero saca las cadenas legibles y la bandera aparece directamente sin necesidad de desensamblar.

```bash
strings <binario>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Busca la bandera en el binario. / Find the flag in the binary. | `THM{345y_f1nd_345y_60}` |

---

### Task 8: Otro decodificado / Another decoding stuff

**Explicación:** Se entrega la cadena `3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L`, codificada en Base58 (el hint lo indica). Con CyberChef (operación Base58) se decodifica y se obtiene la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Decodifica la cadena codificada. ¿Cuál es la bandera? / Decode the encoded string. What is the flag? | `THM{17_h45_l3553r_l3773r5}` |

---

### Task 9: ¿Izquierda o derecha? / Left or right

**Explicación:** Es un cifrado de César. Con CyberChef se prueba la operación ROT ("Ceaser Salad Cipher") variando el desplazamiento hasta que el texto se vuelve legible y aparece la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descifra el mensaje con César. ¿Cuál es la bandera? / Decrypt the message with Caesar. What is the flag? | `THM{hail_the_caesar}` |

---

### Task 10: Haz un comentario / Make a comment

**Explicación:** Igual que la Task 5, se inspecciona el HTML del reto. Esta vez la bandera está guardada en un comentario HTML (`<!-- ... -->`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Mira el comentario en el HTML. ¿Cuál es la bandera? / Check the HTML comment. What is the flag? | `THM{4lw4y5_ch3ck_7h3_c0m3mn7}` |

---

### Task 11: ¿Puedes arreglarlo? / Can you fix it?

**Explicación:** El fichero se entrega con la cabecera dañada: la magic number no es la de PNG (`89 50 4E 47`). Se corrige la cabecera con un editor hexadecimal (ghex) y, al abrir la imagen reparada, aparece la bandera.

```bash
sudo apt install ghex
ghex fichero.png   # corregir el magic number a 89 50 4E 47
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Arregla el fichero y ábrelo. ¿Cuál es la bandera? / Fix the file and open it. What is the flag? | `THM{y35_w3_c4n}` |

---

### Task 12: Léelo / Read it

**Explicación:** La pista apunta a Reddit. Se busca en Google "TryHackMe rooms Reddit" y se localiza la bandera en el perfil/feed asociado de Reddit del reto.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Sigue la pista de Reddit. ¿Cuál es la bandera? / Follow the Reddit hint. What is the flag? | `THM{50c14l_4cc0un7_15_p4r7_0f_051n7}` |

---

### Task 13: Dado de vueltas / Spin my head

**Explicación:** La pista "binaryfuck" apunta al esolang brainfuck. Se usa un decodificador/encoder de brainfuck online, se introduce la entrada del reto y se obtiene la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Decodifica con brainfuck. ¿Cuál es la bandera? / Decode with brainfuck. What is the flag? | `THM{0h_my_h34d}` |

---

### Task 14: ¡Una exclusiva! / An exclusive!

**Explicación:** La pista "S1 XOR S2" indica un XOR entre dos cadenas hexadecimales. Con un pequeño script de Python se hace `int(s1,16) ^ int(s2,16)`, se pasa a ASCII y se obtiene la bandera.

```python
def xor_strings(s1, s2):
    int_s1 = int(s1, 16); int_s2 = int(s2, 16)
    return format(int_s1 ^ int_s2, 'x')

s1 = "44585d6b2368737c65252166234f20626d"
s2 = "1010101010101010101010101010101010"
result = xor_strings(s1, s2)
print(bytes.fromhex(result))
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Aplica XOR a las cadenas. ¿Cuál es la bandera? / XOR the strings. What is the flag? | `THM{3xclu51v3_0r}` |

---

### Task 15: Paseo binario / Binary walk

**Explicación:** El fichero esconde otros ficheros dentro. Con `binwalk -e` se extrae el contenido incrustado y entre los ficheros extraídos aparece la bandera.

```bash
binwalk -e <fichero>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Extrae los ficheros incrustados. ¿Cuál es la bandera? / Extract the embedded files. What is the flag? | `THM{y0u_w4lk_m3_0u7}` |

---

### Task 16: Oscuridad / Darkness

**Explicación:** El reto se resuelve con StegSolve. Se descarga `Stegsolve.jar`, se abre con `java -jar stegsolve.jar` y se navega por las capas de color con los botones `< >` hasta que en una de las capas se revela la bandera.

```bash
wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
chmod +x stegsolve.jar
java -jar stegsolve.jar
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Analiza las capas de color con stegsolve. ¿Cuál es la bandera? / Analyze the colour layers with stegsolve. What is the flag? | `THM{7h3r3_15_h0p3_1n_7h3_d4rkn355}` |

---

### Task 17: Un QR que suena / A sounding QR

**Explicación:** Otra vez se usa `zbarimg` para leer el QR; esta vez el contenido es un enlace de SoundCloud. Escuchando el audio se capta la bandera hablada; la pista advierte que la bandera va en MAYÚSCULAS (All CAPS).

```bash
zbarimg qr.png
# -> enlace a SoundCloud; escuchar -> bandera en mayúsculas.
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Decodifica el QR y escucha la pista. ¿Cuál es la bandera? / Decode the QR and listen to the hint. What is the flag? | `THM{SOUNDINGQR}` |

---

### Task 18: Excava en el pasado / Dig up the past

**Explicación:** La pista es Wayback Machine. Se usa la web de Wayback para ver una versión pasada del sitio del reto y, revisando la fecha indicada, aparece la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Busca en Wayback Machine. ¿Cuál es la bandera? / Check the Wayback Machine. What is the flag? | `THM{ch3ck_th3_h4ckb4ck} ` |

---

### Task 19: ¡Irrompible! / Uncrackable!

**Explicación:** El cifrado es Vigenère. La clave se deduce porque los primeros 9 caracteres del ciphertext `MYKAHODTQ{RVG_YVGGK_FAL_WXF}` deben descifrar a `TRYHACKME`: aplicando la técnica sobre la tabla de Vigenère (T->M, R->Y, Y->K, ...) la clave es `THM`. Con la clave `THM` en CyberChef se descifra la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Descifra el texto con la clave de Vigenère. ¿Cuál es la bandera? / Decrypt with the Vigenère key. What is the flag? | `TRYHACKME{YOU_FOUND_THE_KEY}` |

---

### Task 20: Bases pequeñas / Small bases

**Explicación:** Se entrega el número decimal `581695969015253365094191591547859387620042736036246486373595515576333693`. Se convierte a hexadecimal y después a ASCII con un pequeño script de Python para obtener la bandera.

```python
dec = 581695969015253365094191591547859387620042736036246486373595515576333693
h = hex(dec)[2:]
if len(h) % 2: h = "0" + h
print(bytes.fromhex(h))
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Convierte decimal -> hex -> ascii. ¿Cuál es la bandera? / Convert dec -> hex -> ascii. What is the flag? | `THM{17_ju57_4n_0rd1n4ry_b4535}` |

---

### Task 21: Lee el paquete / Read the packet

**Explicación:** Se abre la captura con Wireshark. La pista sugiere seguir el stream ("Put it into stream"). Se comprueba si se descargó algún fichero: `File > Export Objects > HTTP` y se exporta `flag.txt`, cuyo contenido es la bandera.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Analiza la captura y exporta el fichero. ¿Cuál es la bandera? / Analyze the capture and export the file. What is the flag? | `THM{d0_n07_574lk_m3}` |

---

| # | Task | Pregunta | Respuesta |
|---|------|----------|-----------|
| 1 | Task 1 | Nota del autor. / Author note. | `No answer needed` |
| 2 | Task 2 | Decodifica el Base64. / Decode the Base64. | `THM{ju57_d3c0d3_7h3_b453}` |
| 3 | Task 3 | Metadatos EXIF. / EXIF metadata. | `THM{3x1f_0r_3x17}` |
| 4 | Task 4 | Extrae con steghide. / Extract with steghide. | `THM{500n3r_0r_l473r_17_15_0ur_7urn}` |
| 5 | Task 5 | Texto oculto. / Hidden text. | `THM{wh173_fl46}` |
| 6 | Task 6 | Decodifica el QR. / Decode the QR. | `THM{qr_m4k3_l1f3_345y}` |
| 7 | Task 7 | strings del binario. / strings of the binary. | `THM{345y_f1nd_345y_60}` |
| 8 | Task 8 | Decodifica el Base58. / Decode the Base58. | `THM{17_h45_l3553r_l3773r5}` |
| 9 | Task 9 | Cifrado de César. / Caesar cipher. | `THM{hail_the_caesar}` |
| 10 | Task 10 | Comentario HTML. / HTML comment. | `THM{4lw4y5_ch3ck_7h3_c0m3mn7}` |
| 11 | Task 11 | Cabecera PNG dañada. / Broken PNG header. | `THM{y35_w3_c4n}` |
| 12 | Task 12 | Pista de Reddit. / Reddit hint. | `THM{50c14l_4cc0un7_15_p4r7_0f_051n7}` |
| 13 | Task 13 | Brainfuck. | `THM{0h_my_h34d}` |
| 14 | Task 14 | XOR de cadenas. / XOR strings. | `THM{3xclu51v3_0r}` |
| 15 | Task 15 | binwalk. | `THM{y0u_w4lk_m3_0u7}` |
| 16 | Task 16 | stegsolve. | `THM{7h3r3_15_h0p3_1n_7h3_d4rkn355}` |
| 17 | Task 17 | QR + SoundCloud. | `THM{SOUNDINGQR}` |
| 18 | Task 18 | Wayback Machine. | `THM{ch3ck_th3_h4ckb4ck} ` |
| 19 | Task 19 | Vigenère (clave THM). / Vigenère (key THM). | `TRYHACKME{YOU_FOUND_THE_KEY}` |
| 20 | Task 20 | dec -> hex -> ascii. | `THM{17_ju57_4n_0rd1n4ry_b4535}` |
| 21 | Task 21 | Wireshark/Export Objects. | `THM{d0_n07_574lk_m3}` |

---

**Metodología:** Cada reto se aborda por su pista: identificar la codificación (Base64/Base58) -> decodificar con CyberChef/comandos; inspeccionar metadatos y HTML; extraer estego (steghide, binwalk, stegsolve, zbarimg); revisar strings/cabeceras; aplicar criptografía clásica (César, Vigenère, XOR) con scripts de Python; y usar servicios (Wayback, Reddit, SoundCloud) y Wireshark para los retos restantes.

### Cadena de ataque / Attack Chain

```text
Base64 -> exiftool -> steghide -> HTML -> zbarimg -> strings -> Base58 -> César -> HTML comment -> PNG header -> Reddit -> brainfuck -> XOR -> binwalk -> stegsolve -> QR/SoundCloud -> Wayback -> Vigenère -> dec->hex->ascii -> Wireshark
```

**Learning chain:** decodificación (Base64/58) -> metadatos (exiftool) -> estego (steghide/solves) -> QR (zbar) -> binario (strings/ghex) -> cripto clásica (César/XOR/Vigenère) -> forense de tráfico (Wireshark).

**Lección:** *En un CTF la pista marca el camino: saber reconocer el tipo de codificación o herramienta adecuada (base64, EXIF, steghide, strings...) resuelve la mayoría de retos sin complicaciones.*

**MITRE ATT&CK:** N/A (colección de retos de criptografía/estego; técnicas relacionadas: T1059 descodificación con scripts)

**Fuente:** [TryHackMe - CTF collection Vol.1](https://tryhackme.com/room/ctfcollectionvol1)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.