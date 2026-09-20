# Task 9: Now you see me — HackBack2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF | task9nowyouseeme | https://tryhackme.com/room/hackback2 | 02 Level Medium | TryHackMe | Esteganografía, JPG, GPG, gzip/tar, ROT13, ELF, OSINT, LSB/JSteg, AES | Extracción de 6 de 7 flags del reto de esteganografía |

---

**Contexto:** La tarea **Now you see me** de HackBack2 es un reto de esteganografía centrado en una imagen JPG de Alan Turing que esconde varias capas de archivos (tars/gzips anidados). Se recuperan 7 preguntas sobre metadatos, archivos ocultos, binarios embebidos y OSINT de las imágenes. Los flags se obtienen con pistas como passphrases GPG, un gzip al final del JPG, un ELF en base64 y comparación de imágenes (diff + ROT13). El flag 7 queda pendiente por no localizar el ciphertext AES (key=hey, iv=seed, 10 caracteres). The lab contents sit in `reversing_THM/stego1` and were shared at the start of the session.

## Solucionario

### Task 9: [Medium] [Steganography] Now you see me

**Explicación:** Se trabaja sobre la imagen JPG original del room (`alan_1570997818295.jpg`, Alan Turing) con varias capas de archivos escondidos dentro (tars/gzips anidados) y 7 preguntas. Cada flag sale de una técnica distinta: metadatos + passphrase gpg (flag 1), gzip oculto al final del JPG con `flag2.mp3` cifrado (flag 2), un programa ELF en `flag3.txt` en base64 (flag 3), más datos gzip en `hidden.png` (Lenna) con un tar de dos versiones de la foto de Grace Hopper (flag 4), y OSINT sobre las fotos de Steve Wozniak y del primer empleado (flags 5 y 6). El flag 7 pide "think outside the box...": AES con `key=hey` e `iv=seed`, formato de 10 caracteres, sin ciphertext localizado aún.

![Lab: imagen JPG de Alan Turing (reto de esteganografía)](img/task9.png)

**Nivel:** Medium - Steganografía
**Room:** HackBack2 (https://tryhackme.com/room/hackback2)

## Qué era / What it was

Una imagen JPG (Alan Turing) con varias capas de archivos escondidos dentro (tars/gzips anidados) y 7 preguntas. Los archivos originales del room están en `reversing_THM/stego1` (no hace falta descargar más: la imagen del room ya fue compartida al inicio de la sesión).

## Cómo se resolvió (resumen) / How it was resolved (summary)

1. **Flag 1**: metadatos de la imagen -> quién tomó la foto -> passphrase `password` (gpg) -> md5 de "password" = flag 1.
2. **Flag 2**: al final del JPG había un gzip escondido que contenía `flag2.mp3` (gpg-cifrado, pass `Password123`, pista "Entropy on GitHub CyberChef"). El mp3 descifrado dice por voz `2KCABKCAH`.
3. **Flag 3**: un programa ELF escondido en `flag3.txt` (base64) -> flag 3 (md5 del binario).
4. **Flag 4**: `hidden.png` (Lenna) tenía más datos gzip al final -> tar con dos versiones de la misma foto (Grace Hopper). Comparando ambas (diff) y aplicando ROT13 a los bytes finales: `HarvardMarkI`.
5. **Flag 5**: `flag5.jpg` = Steve Wozniak -> fecha de nacimiento `August 11, 1950`.
6. **Flag 6**: `flag6.jpg` = primer empleado -> número de empleado al entrar: `7`.
7. **Flag 7**: Pendiente. AES `key=hey iv=seed`, 10 caracteres. No se encontró ciphertext en los archivos locales con LSB/JSteg/trailing; requiere localizar dónde está embebido (candidato: la imagen principal del room).

## Flags / Banderas

1. 5f4dcc3b5aa765d61d8327deb882cf99 ✅
2. 2KCABKCAH ✅
3. 00a92932a4fd522632cc7a3315ac22c0 ✅
4. HarvardMarkI ✅
5. August 11, 1950 ✅
6. 7 ✅
7. Pendiente (AES key=hey iv=seed, formato 10 chars)

## Estado / Status

Resueltas: 6 | Pendientes: 1 (flag7)

### Notas de intento del flag 7 (trypass.sh)

```bash
#!/bin/bash
cd /mnt/c/Users/pente/Downloads/reversing_THM/stego1 || exit 1
for p in 5f4dcc3b5aa765d61d8327deb882cf99 alan grace password123 12345678 thm qwerty turing alan2 grace123 harvard marki 123456789 p4ssw0rd; do
  out=$(gpg --batch --yes --passphrase "$p" -o /tmp/o.bin -d flag2.mp3 2>&1)
  if ! echo "$out" | grep -q "Bad session key"; then
    echo "PASS=[$p] -> $out"
  fi
done
echo "=== done ==="
```

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 9.1 | [+50] What is flag 1? | `5f4dcc3b5aa765d61d8327deb882cf99` |
| 9.2 | [+100] What is flag 2? | `2KCABKCAH` |
| 9.3 | [+50] What is flag 3? | `00a92932a4fd522632cc7a3315ac22c0` |
| 9.4 | [+25] What is flag 4? | `HarvardMarkI` |
| 9.5 | [+25] What is flag 5? | `August 11, 1950` |
| 9.6 | [+50] What was his employee number when he first joined? | `7` |
| 9.7 | [+50] What is flag 7? Think outside the box... | `Pendiente (AES key=hey iv=seed, formato 10 chars)` |

---

**Metodología:** Extracción de metadatos EXIF, búsqueda de trailing data (gzip/tar), descifrado GPG, decodificación base64 de binarios, análisis de imágenes (LSB/JSteg/trailing), diff de versiones de una misma foto con ROT13 en bytes finales y OSINT para identificar personajes (ITSM: esteganografía + criptografía + OSINT).

**Learning chain:** JPG de Alan Turing → metadatos (fotógrafo) → passphrase gpg ("password") → md5 = flag1 → gzip trailing en el JPG → flag2.mp3 (gpg "Password123") → voz = flag2 → flag3.txt base64 → ELF → md5 = flag3 → hidden.png (Lenna) → gzip trailing → tar con 2 fotos (Grace Hopper) → diff + ROT13 = flag4 → flag5.jpg (Steve Wozniak) = 11 de agosto de 1950 → flag6.jpg (primer empleado) = 7 → flag7 (AES key=hey iv=seed) pendiente.

**Lección:** *Los archivos "inocentes" (JPG, PNG) esconden capas completas de datos al final del binario: hay que mirar metadatos, trailing bytes y versiones duplicadas, porque cada capa revela la pista de la siguiente.*

**MITRE ATT&CK:** T1027.003 Steganography (datos ocultos en imágenes) · T1140 Deobfuscate/Decode Files or Information (base64, ROT13, gzip) · T1027 Obfuscated Files or Information (archivos embebidos).

**Fuente:** [TryHackMe - Task 9: Now you see me — HackBack2](https://tryhackme.com/room/hackback2)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.