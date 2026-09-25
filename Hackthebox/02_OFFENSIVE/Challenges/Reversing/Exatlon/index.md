# Exatlon [EASY]

> **ES:** Challenge Reversing Easy: un binario ELF (`exatlon_v1`) empaquetado con UPX que dibuja arte ASCII lentamente, pide una contraseña y la compara codificada contra una lista de números; hay que desempaquetarlo, localizar la función de codificado y revertirla para recuperar la contraseña/flag (`HTB{...}`).
> **EN:** Easy Reversing challenge: a UPX-packed ELF binary (`exatlon_v1`) that draws ASCII art slowly, asks for a password and compares an encoded form against a number list; unpack it, locate the encoding routine and reverse it to recover the password/flag (`HTB{...}`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Reversing |
| **Dificultad** | Easy |
| **Estado** | Retired |
| **URL** | https://app.hackthebox.com/challenges/Exatlon [verificar slug exacto] |
| **Archivos** | `exatlon.zip` → `exatlon_v1` (ELF 64-bit, empaquetado con UPX) [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | 20 (según writeup de Esther7171; el stub local antiguo anotaba 2pts con el sistema de puntuación viejo) |

---

## 🎯 Objetivo / Goal

> **ES:** Desempaquetar el binario, entender cómo transforma la contraseña introducida (desplazamiento de bits) y revertir la comparación para obtener la contraseña válida, que es la flag con formato `HTB{...}`.
> **EN:** Unpack the binary, understand how it transforms the entered password (bit shift) and reverse the comparison to obtain the valid password, which is the flag in `HTB{...}` format.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `unzip`, `file`, `strings`, `hexdump`/`xxd` (triage inicial)
- [ ] `upx` (desempaquetado: `upx -d`)
- [ ] Desensamblador/depurador: radare2 + Cutter, o IDA + GDB (a elegir)
- [ ] `python3` (script de decodificado propio)
- [ ] Opcional: `ltrace`/`strace` para observar el flujo de ejecución

---

## 📋 Pasos / Steps

### Paso 1 — Análisis inicial / Triage

> **ES:** Al descomprimir el descargable aparece un único ELF (`exatlon_v1`) que los desensambladores no abren bien de entrada. Al ejecutarlo dibuja un arte de texto línea a línea con pausas (llamadas a espera) y luego pide contraseña; un fallo devuelve al inicio, lo que desincentiva la fuerza bruta. La inspección del fichero revela firmas del empaquetador UPX.
> **EN:** Unzipping the download yields a single ELF (`exatlon_v1`) that disassemblers don't open cleanly at first. Running it draws text art line by line with pauses (sleep calls) then asks for a password; a failure loops back to the start, discouraging brute force. File inspection reveals UPX packer signatures.

```bash
unzip exatlon.zip && file exatlon_v1
strings exatlon_v1 | grep -i -m5 upx
# esperado: menciones a UPX / "packed" en las cadenas del fichero
./exatlon_v1
# esperado: dibujo ASCII lento → prompt de password → con password mala, vuelta al inicio
```

**Resultado / Result:** Binario identificado como ELF empaquetado con UPX; el comportamiento (arte lento + bucle ante fallo) apunta a análisis estático tras desempaquetar en vez de fuerza bruta.

### Paso 2 — Desempaquetado / Unpacking

> **ES:** Si UPX lo empaquetó, la propia herramienta lo revierte. Se desempaqueta (en copia para conservar el original) y se verifica que el ELF resultante ya se abre en el desensamblador.
> **EN:** If UPX packed it, the same tool reverses it. Unpack (on a copy to preserve the original) and verify the resulting ELF now opens in the disassembler.

```bash
cp exatlon_v1 exatlon_v1.packed
upx -d exatlon_v1 -o exatlon_v1.unpacked
file exatlon_v1.unpacked
# esperado: ELF 64-bit desempacado, analizable en radare2/Cutter o IDA
```

**Resultado / Result:** ELF desempaquetado y analizable; la función `main` y una rutina de apoyo (llamada `exatlon` en los writeups) quedan visibles.

### Paso 3 — Localizar la comparación / Find the check

> **ES:** En `main`, tras la zona de dibujo (sucesivas esperas) y la lectura de la contraseña, hay una llamada a la rutina de codificado y justo después una referencia a una cadena con muchos números separados por espacios (del orden de ~1152 1344 1056 ... 2000). Esa cadena es la contraseña esperada ya codificada; la rutina transforma cada carácter introducido antes de comparar.
> **EN:** In `main`, after the drawing zone (repeated sleeps) and the password read, there is a call to the encoding routine and right after it a reference to a long space-separated number string (around 1152 1344 1056 ... 2000). That string is the expected password in encoded form; the routine transforms each entered character before comparing.

```bash
strings -a exatlon_v1.unpacked | grep -E "^[0-9]{3,4}( [0-9]{3,4})+$"
# esperado: una línea con la lista de valores codificados (~36 números)
# en el desensamblador: main → lectura de password → call exatlon → comparación con esa cadena
```

**Resultado / Result:** Localizada la cadena de referencia codificada y el punto de comparación; queda entender la transformación (paso 4). Un parcheo rápido del salto condicional tras la comparación confirma que tras el check no hay más lógica relevante (el programa no hace nada especial con el acierto).

### Paso 4 — Revertir el codificado y recuperar la contraseña / Reverse the encoding

> **ES:** Depurando con un punto de parada tras la llamada se observa que cada carácter se convierte en un número unas 16 veces mayor (p. ej. la `H` inicial de `HTB` produce el primer valor de la lista). En el desensamblado de la rutina aparece un desplazamiento a la izquierda de 4 bits (`shl ..., 4`), es decir cada byte ASCII se multiplica por 16. Para decodificar basta el proceso inverso: dividir entre 16 (desplazar a la derecha 4 bits) y convertir a carácter.
> **EN:** Debugging with a breakpoint after the call shows each character becomes a number about 16x larger (e.g. the leading `H` of `HTB` yields the first value in the list). Disassembly of the routine shows a 4-bit left shift (`shl ..., 4`), i.e. each ASCII byte multiplied by 16. Decoding is the inverse: divide by 16 (shift right 4 bits) and convert to character.

```bash
python3 -c "
enc = [1152,1344,1056,1968,1728,816,1648,784,1584,816,1728,1520,1840,1664,784,1632,1856,1520,1728,816,1632,1856,1520,784,1760,1840,1824,816,1584,1856,784,1776,1760,528,528,2000]
print(''.join(chr(x >> 4) for x in enc))
"
# esperado: la contraseña/flag en claro con formato HTB{...}

# verificación opcional:
./exatlon_v1.unpacked
# (introducir la cadena recuperada → el programa la acepta)
```

**Resultado / Result:** Cadena recuperada con formato `HTB{...}` (no se reproduce aquí por integridad del contenido; challenge retirado, ver capturas de las fuentes citadas). Con ella el binario acepta la contraseña. [verificar] reproducción propia con captura en `img/`.

---

## 🧠 Lo aprendido / Learned

- [ ] Detectar un binario empaquetado con UPX (`strings`/firmas) y revertirlo con la propia herramienta (`upx -d`).
- [ ] El dibujo lento con pausas + bucle ante fallo es una medida anti-fuerza-bruta, no parte de la lógica del check.
- [ ] Patrón habitual en reversa fácil: `main` → leer input → rutina de codificado → comparar contra referencia codificada.
- [ ] Un desplazamiento de bits (`<< 4` / `>> 4`, factor 16) como "cifrado": se identifica probando pocos caracteres (`H` → primer valor, luego diferencias de 16 entre letras consecutivas) y se revierte con un script mínimo.
- [ ] Depurar con punto de parada tras la rutina permite observar la transformación sin reversar todo el binario.

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [HTB Reversing: Exatlon — David Guest](/dev/dg)](https://davidguest.uk/htb-reversing-exatlon/) — David Guest, 2021-09-08 (binario `exatlon_v1` empaquetado con UPX, `upx -d`, arte lento anti-bruteforce, radare2/Cutter, parcheo de prueba del salto, cadena numérica codificada, punto de parada tras `exatlon`, `shl eax, 4`, script Python `x >> 4` + `chr`)
- **Walkthrough de referencia:** [HackTheBox — Exatlon Reversing Challenge — Writeup — sturu](https://medium.com/%40sturu/hackthebox-exatlon-reversing-challenge-writeup-a98243ed5c36) — sturu (IDA + GDB, binario empaquetado con UPX, función `exatlon` con dos argumentos)
- **Writeup breve:** [Hack The Box - Exatlon — jaeflo](https://jaeflo.github.io/2020/hack-the-box-exatlon/) — jaeflo, 2020-05-28
- **Referencia de puntos/categoría:** [Exatlon — Esther7171/HackTheBox-Writeups-Walkthroughs](https://github.com/Esther7171/HackTheBox-Writeups-Walkthroughs/tree/main/Write-ups/Challanges/Exatlon) — Esther7171 ("Difficulty: Easy (20 Points)"; lo lista además como Forensics/Miscellaneous: discrepancia documentada, se adopta Reversing por la etiqueta oficial del foro + mayoría de writeups)
- **Hilo oficial:** [[Reversing] Exatlon - Challenges - Hack The Box :: Forums](https://forum.hackthebox.com/t/reversing-exatlon/2646/48) (etiqueta oficial Reversing)
- **Nota local previa:** stub raíz `Soluciones/Challenges/exatlon.md` ("# Solved Challenge: Exatlon / Points: 2pts", sistema de puntos antiguo) migrado a esta plantilla
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
