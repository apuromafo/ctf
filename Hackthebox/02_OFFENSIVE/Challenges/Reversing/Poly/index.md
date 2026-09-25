# Poly [INSANE]

> **ES:** Challenge Reversing Insane: un crackme ELF de 64-bit para ARM (`AArch64`), sin símbolos y con llamadas al sistema propias, que muestra el aviso "Things are not as they appear!" y un prompt propio; combina varias pistas falsas (comprobación hash, sección de alta entropía, texto escondido en el banner) con una flag real que se escribe en un descriptor oculto. Hay que emularlo (qemu o Unicorn si no hay qemu) y observar a dónde va cada escritura para quedarse con la salida correcta (`HTB{...}`).
> **EN:** Insane Reversing challenge: a 64-bit ARM (`AArch64`) ELF crackme, stripped with its own syscall wrappers, showing a "Things are not as they appear!" banner and a custom prompt; it mixes several decoys (hash check, high-entropy section, banner-hidden text) with a real flag written to a hidden descriptor. Emulate it (qemu, or Unicorn where qemu is unavailable) and watch where each write goes to keep the right output (`HTB{...}`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Reversing |
| **Dificultad** | Insane |
| **Estado** | Retired |
| **URL** | https://app.hackthebox.com/challenges/Poly [verificar slug exacto] |
| **Archivos** | Binario `poly` (ELF 64-bit ARM AArch64, stripped; secciones `.text` ~32KB, `.flag` ~236KB de alta entropía, `.bss` ~4MB) [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | 100 (según writeup de Esther7171; el stub local antiguo anotaba 10pts con el sistema de puntuación viejo) |
| **Autor / época** | jb0 · publicado el 2020-02-28 aprox. (según writeup detallado citado) [verificar] |

---

## 🎯 Objetivo / Goal

> **ES:** Ejecutar el binario ARM en emulación, descartar los caminos señuelo y capturar la salida que contiene la flag válida con formato `HTB{...}`.
> **EN:** Run the ARM binary under emulation, discard the decoy paths and capture the output holding the valid flag in `HTB{...}` format.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `file`, `readelf`/`objdump` o `rabin2 -I` (triage: arquitectura, secciones, punto de entrada)
- [ ] Emulación: `qemu-aarch64` (+ `strace`) o, sin qemu/sudo, `unicorn` + `capstone` (llegan con `angr` vía pip) con syscalls `read`/`write`/`exit` implementadas en el harness
- [ ] Desensamblador: Ghidra / radare2 / IDA (a elegir) para el REPL y las rutinas cripto
- [ ] `python3` (harness de emulación, pruebas de descifrado, análisis de entropía/Hamming)
- [ ] `rockyou.txt` u otro diccionario solo para confirmar el señuelo documentado (no es la vía de la flag)

---

## 📋 Pasos / Steps

### Paso 1 — Análisis inicial / Triage

> **ES:** El fichero es un ELF de 64-bit para ARM (`AArch64`), no PIE, sin símbolos, con envoltorios de syscall propios (binario "freestanding"). Destacan una sección de ~236KB con entropía alta y otra reservada de varios MB. Al arrancarlo en emulación muestra el aviso de que las cosas no son lo que parecen y un prompt de lectura; acepta una línea y responde. No importa `time`, así que no hay aleatoriedad real dependiente de reloj.
> **EN:** The file is a 64-bit ARM (`AArch64`) ELF, non-PIE, stripped, with its own syscall wrappers ("freestanding" binary). A ~236KB high-entropy section and a multi-MB reserved one stand out. Started under emulation it prints the looks-are-deceiving banner and a read prompt; it takes one line and answers. No `time` import, so no real clock-based randomness.

```bash
file poly
readelf -S poly | grep -E "text|flag|bss"
readelf -l poly | grep -A1 LOAD
# esperado: ELF 64-bit AArch64, EXEC sin símbolos; segmentos de código+datos y reserva grande
```

**Resultado / Result:** Binario ARM identificado y arrancable solo bajo emulación (en x86 no corre nativo); el título + banner avisan de misdirección, así que conviene desconfiar del primer camino "fácil".

### Paso 2 — El señuelo del hash con password de diccionario / Hash-check decoy

> **ES:** El bucle de lectura lleva a una rutina que aplica MD5 a la entrada (se reconoce por sus constantes de inicialización), convierte el resumen a hexadecimal, le añade dos bytes fijos y vuelve a aplicar MD5 para comparar contra un objetivo interno. Con un buffer cifrado por XOR de clave repetida corta como "premio", esa estructura invita a atacar el hash con diccionario. En efecto, una contraseña de diccionario muy alusiva al título supera la comparación y descifra un shellcode que, al ejecutarse emulado, solo devuelve un mensaje de burla ("buen intento, aquí no hay flag"). La sección grande de alta entropía tampoco cede a análisis de distancias: es ruido de distracción.
> **EN:** The read loop leads to a routine that MD5-hashes the input (recognizable by its init constants), hex-encodes the digest, appends two fixed bytes and hashes again for an inner-target comparison. With a short-repeating-key XOR-encrypted buffer as "prize", the layout invites a dictionary attack on the hash. Indeed, a title-pun dictionary password passes the check and decrypts a shellcode that, once emulated, only returns a mocking message ("nice try, no flag here"). The big high-entropy section resists distance analysis too: distraction noise.

```bash
# esquema (no es la vía de la flag; solo confirma el señuelo documentado):
# MD5(input) → hex + b"\x13\x37" → MD5(...) → memcmp contra objetivo
# si ok: buffer XOR con MD5(input) → comprobar magic → ejecutar como código
hashcat -m <modo-doble-md5-documentado> objetivo.txt rockyou.txt
# esperado: una contraseña de diccionario alusiva al título rompe el check,
# pero el payload emulado solo imprime el mensaje de burla
```

**Resultado / Result:** Camino confirmado como señuelo deliberado contra atacantes de fuerza bruta/diccionario; cuando un Insane se resuelve "demasiado fácil", sospechar misdirección y seguir buscando.

### Paso 3 — El señuelo del banner / Banner decoy

> **ES:** El buffer del banner se descifra con XOR de clave corta y muestra el aviso visible; barriendo todas las claves cortas sobre el resto del buffer aparece un texto con formato de flag y un chiste sobre arquitecturas (sin brazos / lago de café). Su formato es atípico (comillas y espacios) y la plataforma lo marca como incorrecto: segundo señuelo plantado.
> **EN:** The banner buffer decrypts with a short-key XOR and shows the visible warning; sweeping all short keys over the rest of the buffer surfaces a flag-looking text with an architecture joke (armless / coffee lake). Its shape is atypical (quotes and spaces) and the platform rejects it: second planted decoy.

```bash
python3 -c "
# esquema: barrido de claves cortas sobre el buffer del banner buscando marcador conocido
# for key in range(0x10000):
#     dec = xor(buffer, key)
#     if b'HTB{' in dec: print(hex(key), dec)
"
# esperado: una sola clave revela el texto señuelo con formato sospechoso (no es la flag)
```

**Resultado / Result:** Segundo señuelo descartado por formato y por rechazo de la plataforma; quedan dos flags falsas documentadas y la real sigue sin aparecer en `stdout`.

### Paso 4 — La vía real: la flag va al descriptor oculto / Real path: hidden-fd exfil

> **ES:** Emulando el binario completo y registrando las escrituras por descriptor se ve el truco: con cualquier entrada incorrecta escribe fragmentos intercalados en dos descriptores a la vez; en pantalla (fd 1) se recompone un mensaje de error del sistema, mientras que en el descriptor 3 (abierto sobre el sumidero nulo al arrancar) se recompone carácter a carácter la flag válida. En máquina con qemu basta redirigir ese descriptor o trazar escrituras; sin qemu se implementa el mismo registro en el harness de Unicorn filtrando por número de descriptor.
> **EN:** Emulating the whole binary while logging writes per descriptor reveals the trick: with any wrong input it writes interleaved fragments to two descriptors at once; on screen (fd 1) they reassemble into a system-error message, while on descriptor 3 (opened on the null sink at startup) they reassemble character by character into the valid flag. On a qemu box just redirect that descriptor or trace writes; without qemu implement the same logging in the Unicorn harness filtering by descriptor number.

```bash
# con qemu + binario ARM real (esquema):
qemu-aarch64 ./poly 3>flag.txt
# (introducir cualquier línea; luego inspeccionar flag.txt frente a stdout)
strace -f -e trace=open,openat,write qemu-aarch64 ./poly
# esperado: open("/dev/null") → fd 3; writes a fd 1 (error visible) y a fd 3 (flag)

# sin qemu (esquema Unicorn): mapear segmentos LOAD, fijar SP,
# hooquear svc: read = inyectar input, write = guardar por fd, exit = parar
# esperado: fd 1 = "CRITICAL: System error!"; fd 3 = HTB{...} (no se reproduce aquí)
```

**Resultado / Result:** Flag válida con formato `HTB{...}` recuperada del descriptor oculto, estable con cualquier entrada (no depende de la contraseña). No se reproduce aquí por integridad del contenido; challenge retirado, ver capturas de las fuentes citadas. [verificar] reproducción propia con captura en `img/`.

---

## 🧠 Lo aprendido / Learned

- [ ] En un Insane, un camino que cae con diccionario/fuerza bruta es sospechoso por defecto: aquí era un señuelo con mensaje de burla.
- [ ] Reconocer primitivas por constantes (MD5 por sus IV, CRC por su bucle de tabla) ahorra reversar el algoritmo entero.
- [ ] XOR de clave repetida corta se rompe por distancia de Hamming/Kasiski o por barrido directo si la clave es de 2 bytes y hay marcador conocido.
- [ ] Lo decisivo fue observar por descriptor, no por contenido: `stdout` mostraba el error y el sumidero oculto llevaba la flag (misdirección "las cosas no son lo que parecen").
- [ ] Sin qemu ni root, Unicorn (+ capstone) permite correr un ARM64 mapeando LOAD, fijando SP y atendiendo `svc` de read/write/exit en el harness.

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia (análisis detallado):** [Poly — HTB Insane (Reversing) — juanitonopro65-pixel/HackTheBox-Writeups](https://github.com/juanitonopro65-pixel/HackTheBox-Writeups/blob/main/Poly.md) — juanitonopro65-pixel (binario ARM64 freestanding, secciones `.text`/`.flag`/`.bss`, REPL con banner, doble-MD5 con password de diccionario como señuelo, banner XOR con texto falso, flag real intercalada en fd 3 vs error en fd 1, método capstone + Unicorn sin qemu; autor jb0, rating 4.8, "Can you find the flag?", 2020-02-28)
- **Referencia de puntos/categoría:** [Poly HTB Challenge - Flag Writeup — Esther7171/HackTheBox-Writeups-Walkthroughs](https://github.com/Esther7171/HackTheBox-Writeups-Walkthroughs/blob/main/Write-ups/Challanges/Poly/readme.md) — Esther7171 ("Category: Reversing, Difficulty: Insane (100 Points)"; su flag transcrita difiere del análisis detallado citado: discrepancia documentada, se sigue el análisis detallado por ser el único con pasos reproducibles)
- **Hilo oficial:** [Poly - HTB Content / Challenges - Hack The Box :: Forums](https://forum.hackthebox.com/t/poly/2346) (binario ARM, qemu)
- **Nota local previa:** stub raíz `Soluciones/Challenges/poly.md` ("# Solved Challenge: Poly / Points: 10pts", sistema de puntos antiguo) migrado a esta plantilla
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
