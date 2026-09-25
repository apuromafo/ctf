# Coffee Invocation [verificar dificultad]

> **ES:** Challenge de Reversing: un binario C que embebe una JVM vía JNI y emula una máquina de café; hay que pasar la flag como argumento y revertir dos verificaciones (`verify1`/`verify2`) que envenenan cachés de clases Java (`Byte`/`Short`, luego `Character`/`Boolean`) y comparan contra clases definidas en memoria (`CAFEBABE`).
> **EN:** Reversing challenge: a C binary embedding a JVM via JNI that emulates a coffee machine; pass the flag as an argument and reverse two checks (`verify1`/`verify2`) that poison Java class caches (`Byte`/`Short`, then `Character`/`Boolean`) and compare against in-memory defined classes (`CAFEBABE`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Reversing |
| **Dificultad** | [verificar — no hallada en las fuentes consultadas; los writeups la tratan como reversing intermedio con JNI] |
| **Estado** | Retired (asumido por fecha 2024 y writeups públicos; [verificar] si sigue activo — no se reproduce flag literal) |
| **URL** | https://app.hackthebox.com/challenges/Coffee%20Invocation [verificar slug exacto] |
| **Archivos** | `coffee_invocation` (binario ELF C + clases Java embebidas) [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos (nota previa)** | 6pts (nota del stub raíz `Soluciones/Challenges/coffee_invocation.md`; puntos oficiales [verificar]) |

---

## 🎯 Objetivo / Goal

> **ES:** Ejecutar `./coffee_invocation <FLAG>` eligiendo la opción de menú correspondiente (descrita como `[REDACTED]`/nº 3 en la fuente) y revertir las dos funciones de verificación para reconstruir la flag completa (formato `HTB{...}`) sin adivinarla por fuerza bruta.
> **EN:** Run `./coffee_invocation <FLAG>` choosing the matching menu option (described as `[REDACTED]`/no. 3 in the source) and reverse the two verification functions to reconstruct the full flag (`HTB{...}` format) instead of brute-forcing it.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] `file`, `strings`, `xxd` (triage del binario)
- [ ] Desensamblador/decompilador C (Ghidra / IDA / Binary Ninja)
- [ ] Decompilador Java (`javap`, CFR / Procyon) para los blobs `CAFEBABE` extraídos
- [ ] `python3` (reimplementar las tablas de sustitución y revertirlas)
- [ ] Documentación JNI (`DefineClass`, cachés de `valueOf`) + OpenJDK de referencia

---

## 📋 Pasos / Steps

### Paso 1 — Análisis inicial / Triage

> **ES:** El binario es un programa C que arranca la JVM con JNI (caso inverso al habitual: no es Java llamando a nativo, sino nativo pilotando Java). Muestra un menú de máquina de café con arte ASCII; la ruta real pide la flag como `argv[1]` y ejecuta dos verificaciones que deben devolver 0.
> **EN:** The binary is a C program that boots a JVM via JNI (the reverse of the usual case: not Java calling native, but native driving Java). It shows a coffee-machine menu with ASCII art; the real path takes the flag as `argv[1]` and runs two verifications that must both return 0.

```bash
file coffee_invocation
strings -n 8 coffee_invocation | grep -iE "java|verify|coffee|exit" | head -30
xxd coffee_invocation | grep -i "cafe babe" | head
# esperado: ELF 64-bit + referencias JNI + cabecera CAFEBABE de clase embebida
```

**Resultado / Result:** Confirmado binario nativo con JVM embebida y al menos un blob de clase Java (`CAFEBABE`) hardcodeado; el flujo pide `argv[1]` y ramifica a `verify1` + `verify2`.

### Paso 2 — Revertir `verify1` (cachés `Byte`/`Short` envenenadas) / Reverse `verify1` (poisoned `Byte`/`Short` caches)

> **ES:** `verify1` instala un shutdown-hook (captura el código de `System.exit`), sobrescribe lo que devuelven `Byte.valueOf()` y `Short.valueOf()` mutando los objetos de sus cachés internas (válido para -128..127 en OpenJDK), define la clase `Verify1` desde el buffer con `DefineClass`, le pasa un array de dos strings (subcadena de `0x1A` chars de `argv[1]` + cadena fija `~PL{A;PL{?;:=|PIC{HzP:A;~x`) e invoca su `main`. El `main` compara con `compareByte(Byte, Short)` usando `==`, que dispara los `valueOf` envenenados: no compara los strings originales sino sus versiones transformadas. Patrón hallado en las tablas: tabla byte desplazada `0x51` (`(i + 0x51) & 0xFF`) y tabla short negada (`(~i + 1) & 0xFF`). Para recuperar la primera parte se invierte el mapeo por carácter.
> **EN:** `verify1` installs a shutdown hook (capturing the `System.exit` code), overrides what `Byte.valueOf()` and `Short.valueOf()` return by mutating their internal cache objects (valid for -128..127 on OpenJDK), defines class `Verify1` from the buffer with `DefineClass`, passes a two-string array (a `0x1A`-char substring of `argv[1]` plus the fixed string `~PL{A;PL{?;:=|PIC{HzP:A;~x`) and invokes its `main`. The `main` compares via `compareByte(Byte, Short)` with `==`, which triggers the poisoned `valueOf`s: it does not compare the original strings but their transformed versions. Table patterns found: byte table shifted by `0x51` (`(i + 0x51) & 0xFF`) and short table negated (`(~i + 1) & 0xFF`). Recover the first part by inverting the mapping per character.

```bash
# Extraer el blob de clase (paráfrasis de pugachev.io): buscar CAFEBABE y volcar
python3 - <<'EOF'
data = open('coffee_invocation','rb').read()
i = data.find(bytes.fromhex('CAFEBABE'))
print('offset:', hex(i))
open('Verify1.class','wb').write(data[i:i+4096])  # ajustar tamaño real con el parser
EOF
javap -p -c Verify1.class | head -60
# esperado: clase Verify1 con main que itera y llama a compareByte / System.exit(3)

# Reversión de la primera parte (lógica parafraseada, sin flag literal):
python3 - <<'EOF'
fixed = "~PL{A;PL{?;:=|PIC{HzP:A;~x"  # cadena fija vista en el binario
out = []
for ch in fixed:
    short_remap = (~ord(ch) + 1) & 0xFF
    byte_remap = (short_remap - 0x51) & 0xFF
    out.append(chr(byte_remap))
print(''.join(out))  # primera parte de la flag (0x1A chars)
EOF
```

**Resultado / Result:** Primera mitad (`0x1A` caracteres) recuperada invirtiendo las dos tablas; el `main` de `Verify1` deja de llamar a `System.exit(3)`.

### Paso 3 — Revertir `verify2` (caché `Character` + `Boolean` invertidos, 13 tablas) / Reverse `verify2` (`Character` cache + flipped `Boolean`, 13 tables)

> **ES:** `verify2` repite el esquema con variantes: hook que además re-selecciona tabla de `Character.valueOf` cuando el código de salida es > 2 (`tabla = exit_code + 1`, 13 tablas en total), invierte `Boolean.TRUE`/`FALSE`, define la clase `Verify2` y le pasa la segunda parte de la flag. Su `main` trocea el input en pares, los ordena con `complexSort(..., true)` y los compara contra pares de una constante ordenada con `complexSort(..., false)`; cada par correcto provoca `System.exit(var2 + 3)`, que conmuta la tabla para el siguiente par. Como ordenar ASCII (en cualquier orden envenenado) siempre da `0123456789ABC...xyz{}`, basta emparejar cada dos caracteres de esa secuencia ordenada contra cada tabla para invertir la segunda parte (longitud `0x1A`).
> **EN:** `verify2` repeats the scheme with twists: a hook that also re-selects the `Character.valueOf` table when the exit code is > 2 (`table = exit_code + 1`, 13 tables total), flips `Boolean.TRUE`/`FALSE`, defines class `Verify2` and passes the flag's second half. Its `main` splits input into pairs, sorts them with `complexSort(..., true)` and compares against pairs of a constant sorted with `complexSort(..., false)`; each correct pair triggers `System.exit(var2 + 3)`, switching the table for the next pair. Since sorting ASCII (in any poisoned order) always yields `0123456789ABC...xyz{}`, match each two characters of that sorted sequence against each table to invert the second half (`0x1A` long).

```bash
# Extraer y decompilar Verify2 igual que en el paso 2, luego invertir por pares:
python3 - <<'EOF'
# characterTables: 13 tablas extraídas del binario (ver fuente para volcado exacto)
# s ordenado de referencia; se empareja cada 2 chars con la tabla i//2
s = "0123456789ABCDEFGHIJKLMNOP"
# for i,ch in enumerate(s):
#     table = characterTables[i//2]
#     print(chr(table.index(ord(ch))), end='')
print('segunda parte: invertir pares contra sus tablas (ver script completo en la fuente)')
EOF
./coffee_invocation 'FLAG_RECONSTRUIDA'
# esperado: ambas verificaciones devuelven 0 y el programa imprime el eco de argv[1]
```

**Resultado / Result:** Segunda mitad recuperada por pares conmutando las 13 tablas; la flag completa (concatenación de ambas mitades) pasa `verify1` y `verify2` y el programa la acepta (no se reproduce aquí por integridad del contenido).

---

## 🧠 Lo aprendido / Learned

- [ ] JNI bidireccional: un binario C puede arrancar la JVM y usar `DefineClass` para ejecutar clases embebidas (`CAFEBABE`).
- [ ] `Byte.valueOf` / `Short.valueOf` / `Character.valueOf` usan cachés de objetos: mutar sus campos privados vía JNI cambia el comportamiento del Java sin tocar su bytecode.
- [ ] Comparar boxeados con `==` en Java fuerza el paso por esas cachés: trampa ideal para un crackme.
- [ ] `Boolean.TRUE`/`FALSE` también son mutables desde nativo e invierten cualquier lógica basada en flags.
- [ ] `System.exit(N)` + shutdown-hook como canal de retorno nativo y como conmutador de tablas (state machine de 13 estados).
- [ ] Ordenar una permutación ASCII siempre converge a la misma secuencia: punto de apoyo para revertir el `complexSort`.

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** ["Coffee Invocation" by Hack The Box — pugachev.io](https://pugachev.io/2024/04/02/coffee-invocation-by-hack-the-box) — pugachev.io / itwaseasy (binario C con JVM vía JNI; `verify1` con tablas byte `+0x51` y short negada; `verify2` con 13 tablas `Character`, `Boolean` invertidos y `complexSort`; código de inversión citado en pasos 2–3, parafraseado aquí)
- **Código de apoyo citado (no copiado):** [crackmes-solutions/hackTheBox/coffee_invocation — itwaseasy](https://github.com/itwaseasy/crackmes-solutions/tree/master/hackTheBox/coffee_invocation) — itwaseasy (clases `Verify1`/`Verify2` decompiladas)
- **Ficha del challenge:** [Coffee Invocation | CTF Base](https://ctfbase.com/writeup/20260521_hackthebox_coffee_invocation) — CTF Base ("native reverse-engineering challenge with embedded Java")
- **Nota local previa:** stub raíz `Soluciones/Challenges/coffee_invocation.md` ("Points: 6pts") migrado a esta plantilla; dificultad oficial no hallada en las fuentes consultadas
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado (según fuentes); no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge (per sources); no literal flags published.

_Fecha de edición: 2026-09-25_
