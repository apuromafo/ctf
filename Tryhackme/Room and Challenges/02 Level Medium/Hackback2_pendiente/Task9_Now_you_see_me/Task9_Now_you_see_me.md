# Task 9 - Now you see me

**Nivel:** Medium - Steganografía
**Room:** HackBack2 (https://tryhackme.com/room/hackback2)

## Qué era

Una imagen JPG (Alan Turing) con varias capas de archivos escondidos dentro (tars/gzips anidados) y 7 preguntas. Los archivos originales del room están en `reversing_THM/stego1` (no hace falta descargar más: la imagen del room ya fue compartida al inicio de la sesión).

## Cómo se resolvió (resumen)

1. **Flag 1**: metadatos de la imagen -> quién tomó la foto -> passphrase `password` (gpg) -> md5 de "password" = flag 1.
2. **Flag 2**: al final del JPG había un gzip escondido que contenía `flag2.mp3` (gpg-cifrado, pass `Password123`, pista "Entropy on GitHub CyberChef"). El mp3 descifrado dice por voz `2KCABKCAH`.
3. **Flag 3**: un programa ELF escondido en `flag3.txt` (base64) -> flag 3 (md5 del binario).
4. **Flag 4**: `hidden.png` (Lenna) tenía más datos gzip al final -> tar con dos versiones de la misma foto (Grace Hopper). Comparando ambas (diff) y aplicando ROT13 a los bytes finales: `HarvardMarkI`.
5. **Flag 5**: `flag5.jpg` = Steve Wozniak -> fecha de nacimiento `August 11, 1950`.
6. **Flag 6**: `flag6.jpg` = primer empleado -> número de empleado al entrar: `7`.
7. **Flag 7**: Pendiente. AES `key=hey iv=seed`, 10 caracteres. No se encontró ciphertext en los archivos locales con LSB/JSteg/trailing; requiere localizar dónde está embebido (candidato: la imagen principal del room).

## Flags

1. 5f4dcc3b5aa765d61d8327deb882cf99 ✅
2. 2KCABKCAH ✅
3. 00a92932a4fd522632cc7a3315ac22c0 ✅
4. HarvardMarkI ✅
5. August 11, 1950 ✅
6. 7 ✅
7. Pendiente (AES key=hey iv=seed, formato 10 chars)

## Estado

Resueltas: 6 | Pendientes: 1 (flag7)
