# Bypass [EASY]

> **ES:** Challenge de Reversing Easy: un ejecutable Windows `.NET` (`Bypass`/`bypass.exe`) que pide usuario, contraseña y clave secreta en dos fases; la primera fase nunca valida de verdad y hay que forzar el flujo en tiempo de ejecución para llegar a la segunda y leer la clave/flag (`HTB{...}`).
> **EN:** Easy Reversing challenge: a Windows `.NET` executable (`Bypass`/`bypass.exe`) asking for username, password and secret key in two stages; the first stage never truly validates and the flow must be forced at runtime to reach the second one and read the key/flag (`HTB{...}`).

| Campo | Valor |
|-------|-------|
| **Categoría** | Reversing |
| **Dificultad** | Easy |
| **Estado** | Retired |
| **URL** | https://app.hackthebox.com/challenges/Bypass |
| **Archivos** | `Bypass` / `bypass.exe` (descarga zip del challenge) [verificar nombre exacto del zip] |
| **Fecha de resolución** | 2026-09-25 (documentación; resuelto previamente según stub local) |
| **Puntos** | 20 (sistema antiguo; el stub local previo anotaba 2pts) |

---

## 🎯 Objetivo / Goal

> **ES:** Superar el doble control de autenticación del binario ("el cliente tiene el control total") manipulando valores en tiempo de ejecución y extraer la clave que entrega la flag en formato `HTB{...}`.
> **EN:** Defeat the binary's double authentication check ("the client is in full control") by manipulating runtime values and extract the key that yields the flag in `HTB{...}` format.

---

## 🛠️ Herramientas usadas / Tools used

- [ ] Máquina Windows (o VM Windows) para ejecutar el `.exe`
- [ ] `strings` (triage inicial: detectar empaquetado y cadenas reveladoras)
- [ ] dnSpy (versión 32 bits; descompilado .NET + depuración con breakpoints y edición de valores en vivo)
- [ ] Conocimiento alternativo: parcheo del binario (modificar la lógica de comparación) como vía equivalente

---

## 📋 Pasos / Steps

### Paso 1 — Análisis inicial / Triage

> **ES:** Al ejecutar el binario aparece un prompt que pide usuario y contraseña en bucle. El volcado de cadenas muestra restos del runtime .NET, lo que indica que el programa está escrito en C#/.NET y que un desensamblador genérico (p. ej. Radare2) dará poco juego: conviene un descompilador .NET.
> **EN:** Running the binary shows a prompt asking for username and password in a loop. A strings dump reveals .NET runtime leftovers, showing the program is written in C#/.NET and that a generic disassembler (e.g. Radare2) won't go far: a .NET decompiler is the right tool.

```bash
unzip bypass.zip && file Bypass
# esperado: PE32 executable (.NET assembly)

strings Bypass | tail -n 30
# esperado: referencias al framework .NET entre las últimas líneas
```

**Resultado / Result:** Confirmado ejecutable Windows PE32 de .NET; la vía de análisis es dnSpy (32 bits), no depuradores nativos tipo gdb.

### Paso 2 — Primera fase: forzar el booleano / First stage: force the boolean

> **ES:** Al descompilar se ven dos comprobaciones encadenadas. La primera función pide usuario/contraseña pero devuelve siempre falso, así que la condición que lleva a la segunda fase nunca se cumple por la vía normal. La solución es poner un breakpoint antes del `if` y cambiar el valor de la variable de control a verdadero en tiempo de ejecución.
> **EN:** Decompiling reveals two chained checks. The first function asks for username/password but always returns false, so the branch leading to the second stage never triggers normally. The fix is to set a breakpoint before the `if` and flip the control variable to true at runtime.

```bash
# Sin comando: acción en dnSpy (32 bits)
# 1. Abrir Bypass.exe en dnSpy
# 2. Localizar la función principal (doble variable booleana sobre el retorno de la fase 1)
# 3. Breakpoint antes del if que guarda la segunda fase
# 4. Ejecutar (F5), introducir usuario/clave cualquiera
# 5. Al parar en el breakpoint: cambiar la variable de control a true y continuar
```

**Resultado / Result:** El flujo entra en la segunda función, que pide la "secret key" (antes inalcanzable).

### Paso 3 — Segunda fase: leer la clave del fuente / Second stage: read the key from source

> **ES:** La segunda función compara lo introducido con un valor literal visible en el propio código descompilado. Basta con poner un breakpoint en la comparación, leer el valor esperado y volver a ejecutar el programa introduciéndolo para que imprima la flag.
> **EN:** The second function compares the input against a literal value visible in the decompiled source itself. Just breakpoint the comparison, read the expected value, re-run the program with it, and it prints the flag.

```bash
# Sin comando: acción en dnSpy + ejecución
# 1. Breakpoint en la comparación de la clave secreta
# 2. Inspeccionar el operando esperado (cadena literal larga en el fuente)
# 3. Re-ejecutar, pasar la fase 1 como en el paso 2 e introducir la clave correcta
```

**Resultado / Result:** El programa acepta la clave y muestra la flag con formato `HTB{...}` (no se reproduce aquí por integridad del contenido; challenge retirado, ver capturas de las fuentes citadas). [verificar] reproducción propia con captura en `img/`.

> **ES:** Vía alternativa equivalente: parchear el binario (invertir la lógica de comparación/retorno) en lugar de manipular valores en vivo; el efecto es el mismo: saltar la autenticación del cliente.
> **EN:** Equivalent alternative: patch the binary (flip the comparison/return logic) instead of editing live values; same effect: skipping the client-side authentication.

---

## 🧠 Lo aprendido / Learned

- [ ] En binarios `.NET`, `strings` delata el runtime y orienta a dnSpy en vez de desensambladores nativos.
- [ ] "El cliente tiene el control total": toda validación en el cliente puede eludirse (depurador o parcheo).
- [ ] Funciones que siempre devuelven falso bloquean ramas enteras; un breakpoint + edición de la variable de control restaura el flujo.
- [ ] La segunda fase comparaba contra una cadena literal embebida: leer el fuente descompilado basta, sin adivinar nada.
- [ ] dnSpy de 32 bits + breakpoints en `if`/comparaciones es el flujo estándar para este tipo de retos .NET.

---

## 📚 Fuentes y Referencias / Sources

- **Walkthrough de referencia:** [Bypass Walkthrough — Daniel Pérez](https://danielperez660.github.io/bypass.html) — Daniel Pérez (enumeración con `strings`, detección .NET/C#, dnSpy 32 bits, breakpoint y cambio de la variable booleana en vivo, lectura de la clave esperada en la comparación)
- **Resumen oficial del reto:** [Bypass HTB Challenge - Flag Writeup — Esther7171](https://github.com/Esther7171/HackTheBox-Writeups-Walkthroughs/blob/main/Write-ups/Challanges/Bypass/readme.md) — Esther7171 ("Category: Reversing, Difficulty: Easy (20 Points)"; descripción: el cliente tiene el control total, eludir la autenticación y leer la clave)
- **Hilo oficial:** [[Reversing] Bypass - Challenges - Hack The Box :: Forums](https://forum.hackthebox.com/t/reversing-bypass/2358) — varios autores (pistas: desensamblador + breakpoints; dnSpy como herramienta; el autor del reto confirma que está pensado para depurador tipo dnSpy)
- **Walkthrough de referencia:** [Hack The Box Writeup — Bypass — joshuanatan](https://medium.com/swlh/hack-the-boxdwriteup-rev-1-a94282cb0c63) — joshuanatan (concepto de parcheo del binario: modificar el programa para saltar la lógica de autenticación)
- **Nota local previa:** stub raíz `Soluciones/Challenges/bypass.md` ("Points: 2pts") migrado a esta plantilla; el valor de 20 puntos viene de Esther7171 (sistema antiguo)
- **Fecha de acceso:** 2026-09-25
- **Autor de este walkthrough:** Apuromafo (síntesis propia parafraseada a partir de las fuentes citadas)

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Challenge retirado; no se publican flags literales.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Retired challenge; no literal flags published.

_Fecha de edición: 2026-09-25_
