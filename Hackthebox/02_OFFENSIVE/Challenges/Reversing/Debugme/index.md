# Debugme [EASY]

> **ES:** Challenge de Reversing: un binario Windows de 32 bits (MinGW) supuestamente "súper seguro y muy difícil de depurar", protegido con trucos anti-debug clásicos y con su función principal cifrada por XOR; hay que neutralizar las comprobaciones, dejar que se autodescifre y extraer la flag (`HTB{...}`).
> **EN:** Reversing challenge: a 32-bit Windows binary (MinGW) supposedly "super secure and really hard to debug", guarded with classic anti-debug tricks and its main function XOR-encrypted; neutralize the checks, let it self-decrypt, and extract the flag (`HTB{...}`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Reversing |
| **Dificultad** | Easy [verificar etiqueta exacta: foreros la consideraban más dura de lo anunciado] |
| **Estado** | Retired |
| **URL** | https://app.hackthebox.com/challenges/Debugme [verificar slug exacto] |
| **Archivos** | Binario Windows 32 bits (MinGW) [verificar nombre exacto del zip/exe] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | [verificar] (el stub local previo anotaba 4pts) |

---

## 🎯 Objetivo / Goal

> **ES:** Depurar el binario pese a sus protecciones anti-debug, revelar el código real de `main` tras su autocifrado y recuperar la flag en formato `HTB{...}`.
> **EN:** Debug the binary despite its anti-debug protections, reveal the real `main` code after its self-decryption, and recover the flag in `HTB{...}` format.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `file`, visor PE (PEview / CFF Explorer) para secciones (atención a `.tls`)
- [ ] FLOSS / `strings` (triage; en este binario no aporta nada útil)
- [ ] IDA (análisis estático: TLS callbacks, punto de entrada, pseudocódigo)
- [ ] Depurador Windows: OllyDbg / x32dbg (+ plugins anti-debug como ayuda) o parcheo manual del binario

---

## 📋 Pasos / Steps

### Paso 1 — Análisis inicial / Triage

> **ES:** El fichero es un EXE de 32 bits compilado con MinGW. Sus secciones son las habituales (`.text`, `.data`, `.rdata`, `.bss`, `.idata`) más una sección `.tls` que invita a revisar los callbacks de inicialización. Las cadenas ofuscadas no revelan nada útil.
> **EN:** The file is a 32-bit EXE compiled with MinGW. Its sections are the usual ones (`.text`, `.data`, `.rdata`, `.bss`, `.idata`) plus a `.tls` section that calls for checking the init callbacks. Obfuscated strings reveal nothing useful.

```bash
unzip debugme.zip && file *
# esperado: PE32 executable (32-bit, MinGW)

floss debugme.exe
# esperado: sin cadenas útiles (binario ofuscado)
```

**Resultado / Result:** EXE 32 bits MinGW con sección `.tls`; el análisis de cadenas no basta, hay que ir a IDA/depurador.

### Paso 2 — Callbacks TLS: descartar la primera trampa / TLS callbacks: rule out the first trap

> **ES:** Los callbacks TLS se ejecutan antes que el punto de entrada clásico, y el malware/protectores los usan para esconder comprobaciones anti-debug. Al revisarlos en IDA solo invocan la rutina estándar de inicialización de MinGW, sin nada hostil: vía libre hacia el entry point real.
> **EN:** TLS callbacks run before the classic entry point, and malware/protectors use them to hide anti-debug checks. Reviewing them in IDA shows they only call the standard MinGW init routine, nothing hostile: clear path to the real entry point.

```bash
# Sin comando: acción en IDA
# 1. Cargar el binario, pulsar Ctrl+E (lista de entry points / TLS callbacks)
# 2. Revisar el pseudocódigo de TlsCallback_0, TlsCallback_1 y __mingw_TLScallback
# esperado: solo inicialización estándar, sin comprobaciones anti-debug
```

**Resultado / Result:** Los TLS callbacks quedan descartados como amenaza; el análisis se centra en `_mainCRTStartup`.

### Paso 3 — Tres comprobaciones anti-debug en la entrada / Three anti-debug checks at startup

> **ES:** Nada más entrar, el programa encadena tres detecciones clásicas de depurador y aborta si alguna salta: el flag `BeingDebugged` del PEB (vía segmento FS, desplazamiento `0x2`), el campo `NtGlobalFlag` del PEB (desplazamiento `0x68`, que cambia bajo depurador por los flags de heap de ntdll) y una medición de tiempo con dos lecturas del contador de ciclos (`RDTSC`) separadas por instrucciones de relleno: si el delta supera `0x3E8`, asume depurador. Se neutralizan parcheando el binario o con plugins anti-debug del depurador.
> **EN:** Right at startup, the program chains three classic debugger detections and aborts if any fires: the PEB `BeingDebugged` flag (via the FS segment, offset `0x2`), the PEB `NtGlobalFlag` field (offset `0x68`, which changes under a debugger due to ntdll heap flags), and a timing measurement with two cycle-counter reads (`RDTSC`) separated by filler instructions: if the delta exceeds `0x3E8`, it assumes a debugger. Neutralize them by patching the binary or with the debugger's anti-debug plugins.

```bash
# Vía A — parcheo (paráfrasis de las fuentes): neutralizar los tres saltos
# condicionales hacia la salida para que la ejecución continúe siempre.

# Vía B — plugins anti-debug de OllyDbg/x32dbg que falsean
# PEB->BeingDebugged, PEB->NtGlobalFlag y el delta RDTSC.
```

**Resultado / Result:** Las tres comprobaciones superadas; la ejecución continúa hacia la rutina de descifrado en lugar de terminar.

### Paso 4 — Autodescifrado de `main` (XOR `0x5C`) / Self-decryption of `main` (XOR `0x5C`)

> **ES:** Tras las comprobaciones hay un bucle que descifra los opcodes de la función principal con XOR de un byte (`0x5C`). Antes de ejecutarlo, `main` solo muestra bytes sin sentido; la técnica es dejar correr ese bucle en el depurador y examinar `main` ya descifrado.
> **EN:** After the checks there is a loop decrypting the main function's opcodes with a single-byte XOR (`0x5C`). Before running it, `main` shows only garbage bytes; the technique is to let that loop run in the debugger and then examine the decrypted `main`.

```bash
# Sin comando: acción en el depurador
# 1. Ejecutar hasta pasar el bucle XOR (clave 0x5C sobre los opcodes de main)
# 2. Volcar/releer main: ahora el desensamblado es código válido
```

**Resultado / Result:** `main` descifrado y legible; contiene las mismas tres trampas anti-debug repetidas.

### Paso 5 — Repetir el bypass dentro de `main` y extraer la flag / Re-apply the bypass inside `main` and extract the flag

> **ES:** El `main` ya descifrado repite las tres detecciones (PEB + `RDTSC`); la forma rápida de pasarlas en vivo es ejecutar cada comparación y forzar el flag Zero para no tomar el salto de salida. Al final de `main` hay un segundo bucle XOR (clave `0x4B`, `0x24` iteraciones) que descifra la flag en memoria: dejarlo correr y leer el búfer resultante entrega la flag.
> **EN:** The decrypted `main` repeats the three detections (PEB + `RDTSC`); the quick live way past them is to step over each comparison and force the Zero flag so the exit jump is not taken. At the end of `main` a second XOR loop (key `0x4B`, `0x24` iterations) decrypts the flag in memory: let it run and read the resulting buffer to get the flag.

```bash
# Sin comando: acción en el depurador
# 1. En cada cmp de las 3 comprobaciones de main: fijar ZF=1 tras el cmp
#    para evitar el salto de salida aunque el check detecte el depurador
# 2. Ejecutar el bucle final (0x24 iteraciones, XOR 0x4B sobre el búfer
#    apuntado por EDI, instrucción LOOP como contador)
# 3. Leer el búfer descifrado en memoria
```

**Resultado / Result:** Flag legible en memoria con formato `HTB{...}` (no se reproduce aquí por integridad del contenido; challenge retirado, ver capturas de la fuente citada). [verificar] reproducción propia con captura en `img/`.

---

## 🧠 Lo aprendido / Learned

- [ ] Los callbacks TLS corren antes del entry point: hay que auditarlos primero, aunque aquí salieron limpios.
- [ ] Tríada anti-debug clásica Windows: `PEB->BeingDebugged` (FS:`0x30`+`0x2`), `PEB->NtGlobalFlag` (+`0x68`) y delta `RDTSC` con umbral (`0x3E8`).
- [ ] Dos formas de neutralizarlas: parchear los saltos o falsear los valores (plugins anti-debug / forzar ZF tras cada `cmp`).
- [ ] Patrón packer casero: `main` cifrado con XOR mono-byte (`0x5C`) que se autodescifra en runtime; analizarlo en estático antes de correr el bucle solo muestra basura.
- [ ] Segunda etapa XOR (`0x4B`, `0x24` bytes) sobre el búfer de la flag: patrón estándar de "descifrar y leer en memoria".
- [ ] La etiqueta de dificultad anunciada no siempre refleja el esfuerzo real: foreros con todos los reversings hechos calificaron este como el más duro de la tanda.

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [HackTheBox Reversing Challenge: Debugme — Charbel Farhat](https://charbelfarhat.com/blogs/htb-debugme.html) — Charbel Farhat (15-09-2020; EXE 32 bits MinGW, sección `.tls`, análisis de `TlsCallback_0/1` y `__mingw_TLScallback` en IDA, las 3 comprobaciones en `_mainCRTStartup`: `BeingDebugged`, `NtGlobalFlag`, delta `RDTSC` > `0x3E8`; bucle XOR `0x5C` sobre `main`, repetición de trampas con bypass por Zero flag, bucle final XOR `0x4B` de `0x24` iteraciones)
- **Hilo oficial:** [debugme - Challenges - Hack The Box :: Forums](https://forum.hackthebox.com/t/debugme/1659) — varios autores (etiquetas: debugme, reversing, challenge; testimonio de que es el más duro de la tanda pese a su etiqueta; x32dbg + Scylla como herramienta viable)
- **PDF de referencia:** [challenges/reversing/Debugme — Hackplayers (SirBroccoli-Debugme.pdf)](https://github.com/Hackplayers/hackthebox-writeups/blob/master/challenges/reversing/Debugme/SirBroccoli-Debugme.pdf) — Hackplayers/SirBroccoli
- **Nota local previa:** stub raíz `Soluciones/Challenges/debugme.md` ("Points: 4pts") migrado a esta plantilla; dificultad oficial exacta pendiente de verificar
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
