# Bombs Landed [Medium]

> **ES:** Challenge de Reversing nivel Medium: un binario que esconde una contraseña; hay que aplicar ingeniería inversa (análisis estático + depurador) para recuperarla y ejecutarlo con ella para obtener la flag (`HTB{...}`).
> **EN:** Medium Reversing challenge: a binary hiding a password; reverse it (static analysis + debugger) to recover the password and run it with that input to get the flag (`HTB{...}`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Reversing |
| **Dificultad** | Medium |
| **Estado** | Retired |
| **URL** | https://app.hackthebox.com/challenges/ (slug `Bombs Landed`; pendiente de verificar ID exacto) |
| **Archivos** | Descarga con contraseña `hackthebox` (binario ELF de análisis local, sin instancia) [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | 50 (Medium; rango habitual 40–50). Nota histórica: listados antiguos lo muestran con 80 pts (sistema de puntos previo) |

---

## 🎯 Objetivo / Goal

> **ES:** Encontrar la contraseña oculta dentro del binario y usarla como entrada para que el programa imprima la flag con formato `HTB{...}`.
> **EN:** Find the hidden password inside the binary and feed it to the program so it prints the flag in `HTB{...}` format.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `unzip` (contraseña `hackthebox`) + `file` + `strings`
- [ ] `objdump` / `radare2` o desensamblador equivalente (Ghidra/IDA)
- [ ] `ltrace` / `strace` (trazar comparaciones y llamadas)
- [ ] `gdb` (breakpoints, inspección de registros/memoria)

---

## 📋 Pasos / Steps

### Paso 1 — Análisis inicial / Triage

> **ES:** Se extrae la descarga, se identifica el tipo de binario y se observa su comportamiento sin argumentos y con una entrada de prueba.
> **EN:** Extract the download, identify the binary type, and observe its behavior with no arguments and with a test input.

```bash
unzip bombs_landed.zip   # contraseña: hackthebox
file bombs_landed
strings -n 6 bombs_landed | head -n 60
./bombs_landed
./bombs_landed test_password
echo $?
```

**Resultado / Result:** Ejecutable local con mensaje de que falta/espera una contraseña oculta; con entrada incorrecta no revela la flag. Las cadenas y la tabla de símbolos orientan hacia la rutina de comparación (paráfrasis de 0x00).

### Paso 2 — Localizar la comparación / Find the check

> **ES:** Se desensambla el binario y se buscan las funciones de comparación de cadenas y las referencias a textos visibles para acotar dónde se valida la entrada.
> **EN:** Disassemble the binary and look for string-comparison calls and references to visible texts to narrow down where the input is validated.

```bash
objdump -t bombs_landed | head -n 80
objdump -d bombs_landed > bombs_landed.asm
grep -n -i "strcmp\|strncmp\|explode\|phase\|password" bombs_landed.asm | head -n 40
ltrace -s 128 ./bombs_landed test_password 2>&1 | head -n 60
```

**Resultado / Result:** Se identifica la rutina que contrasta la entrada del usuario con el valor esperado (paráfrasis de 0x00: "caza de la contraseña oculta en el binario"). Queda acotada la zona a depurar.

### Paso 3 — Recuperar la contraseña y obtener la flag / Recover password and get flag

> **ES:** Con `gdb` (o lectura del desensamblado) se extrae el valor esperado, se ejecuta el binario con él y se recoge la flag sin publicarla aquí literalmente.
> **EN:** With `gdb` (or by reading the disassembly) extract the expected value, run the binary with it, and collect the flag without reproducing it here literally.

```bash
gdb -q ./bombs_landed
# (gdb) break en la rutina de comparación / main
# (gdb) run test_password
# (gdb) x/s $rdi  # inspeccionar el buffer esperado / argumentos de strcmp
# (gdb) continue
./bombs_landed '<contraseña_recuperada>'
```

**Resultado / Result:** El programa acepta la contraseña recuperada e imprime la flag con formato `HTB{...}` (no se reproduce aquí por integridad del contenido; challenge retirado, ver capturas de la fuente citada).

---

## 🧠 Lo aprendido / Learned

- [ ] Flujo clásico de bomb/crackme: entrada → comparación → éxito/fracaso; el objetivo es invertir la comparación, no adivinar.
- [ ] Triaje con `file`/`strings`/`objdump -t` acota rápido la superficie antes de depurar.
- [ ] `ltrace` muestra comparaciones en claro cuando el binario no está ofuscado.
- [ ] En `gdb`, poner breakpoint en la comparación e inspeccionar registros (`x/s $rdi/$rsi` en x86-64) revela el valor esperado.
- [ ] Los puntos HTB cambian con el tiempo: este reto aparece con 80 pts en listados antiguos y con 50 pts (Medium) en el writeup de 2023.

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [Bombs Landed — Reversing Challenge — HackTheBox Writeup](https://nier0x00.medium.com/bombs-landed-reversing-challenge-hackthebox-writeup-2d980d16566) — 0x00 (Medium, 31-01-2023; describe el reto como "medium-level (50 points) reversing challenge" y la premisa "hunt for the hidden password in the binary"; técnica parafraseada, sin copiar flag)
- **Listado histórico:** [hack the box reversing challenges — Flaviu Popescu](https://flaviu.io/reversing-challenges) — Flaviu Popescu (muestra `Bombs Landed` con 80 puntos en el sistema antiguo; útil solo como evidencia del cambio de puntuación)
- **Nota local previa:** stub raíz `Soluciones/Challenges/bombs_landed.md` ("# Solved Challenge: Bombs Landed / Points: 0pts") migrado a esta plantilla (los "0pts" eran marcador local, no puntuación oficial)
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
