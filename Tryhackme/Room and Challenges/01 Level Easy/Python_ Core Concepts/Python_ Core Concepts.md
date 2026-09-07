# Python: Core Concepts [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `pythoncoreconcepts`
* **Link:** https://tryhackme.com/room/pythoncoreconcepts
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + VM con scripts de práctica (fstrings_demo.py)
* **Componentes:** Python: tipos, f-strings, strings/indexación, listas/dicts, operadores, loops
* **Impacto rol:** Primera parte de la serie Python de THM; cimientos de scripting para automatizar tareas ofensivas/defensivas.

## Solucionario de Tareas / Task Solutions

> **ES:** Repaso acelerado de los core concepts de Python orientado a ciberseguridad. `type()` revela el tipo; `input()` siempre devuelve texto (**str** aunque escribas `3.14`). **f-strings** (`f"..."`) formatean dentro de print; el demo del VM (fstrings_demo.py) cierra con la línea **`Scan complete: 192.168.1.1 has 3 open ports`** (patrón mini-portscanner). Strings: **`len()`** cuenta caracteres, **`word[3:7]`** de `"TryHackMe"` es **`HackM`**, y `"ADMIN".lower()` → `"admin"`. Listas: **`.append()`**; dicts: **`services[80]`** → **`"HTTP"`** y **`.get(clave, fallback)`** para acceso seguro. Operadores: **`%`** = resto, **`10 // 3` = 3** (división entera), **`2 ** 10 = 1024`**. Bucles: **`for`** para iterar listas, **`range(3)`** → **0 1 2**, y **`break`** sale del bucle.
> **EN:** Accelerated review of Python core concepts for security. `type()` reveals the type; `input()` always returns text (**str** even if you type `3.14`). **f-strings** (`f"..."`) format inside print; the VM's fstrings_demo.py closes with **`Scan complete: 192.168.1.1 has 3 open ports`** (mini port-scanner pattern). Strings: **`len()`** counts chars, **`word[3:7]`** of `"TryHackMe"` = **`HackM`**, and `"ADMIN".lower()` → `"admin"`. Lists: **`.append()`**; dicts: **`services[80]`** → **`"HTTP"`** and **`.get(key, fallback)`** for safe access. Operators: **`%`** = remainder, **`10 // 3` = 3** (floor division), **`2 ** 10 = 1024`**. Loops: **`for`** to iterate, **`range(3)`** → **0 1 2**, and **`break`** exits the loop.

### Task 1 — Introducción / Introduction *(vm)*

* **Check:** `Let's master Python's core concepts!` (accede a la VM del room).
* **ES:** Serie Python: este room = fundamentos; el compañero = building scripts.
* **EN:** Python series: this room = fundamentals; companion = building scripts.

### Task 2 — Review Rápida / Quick Review: Hello World, Variables, and Conditionals

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What **built-in function** reveals the data type of a value? | `type` |
| If a user types `3.14` at an `input()` prompt, what **data type** does Python store it as before any conversion? | `str` (string) |
| On the attached VM, open and run `fstrings_demo.py`. What is the **last line** printed to the terminal? | `Scan complete: 192.168.1.1 has 3 open ports` |

* **`type()`:** `type(3.14)` → `<class 'float'>`.
* **input():** siempre `str`; hay que castear (`float(prompt)` / `int(prompt)`).
* **fstrings_demo.py:** demo de f-strings estilo mini port-scanner; la última línea imprime el resumen. *Respuesta literal: **`Scan complete: 192.168.1.1 has 3 open ports`**.*

### Task 3 — Trabajando con Strings / Working with Strings

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What function returns the **number of characters** in a string? | `len` |
| Given `word = "TryHackMe"`, what does `word[3:7]` return? | `HackM` |
| What string **method** converts `"ADMIN"` to `"admin"`? | `lower` |

* **`len("TryHackMe")`** = 9.
* **Indexación / Slicing:** `word[3:7]` = caracteres desde el índice 3 al 6 → **`HackM`** (índices: T=0 r=1 y=2 H=3 a=4 c=5 k=6 M=7 e=8).
* **`.lower()`:** `"ADMIN".lower()` → `"admin"` (también existe `.upper()`).

### Task 4 — Listas y Diccionarios / Lists and Dictionaries

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What method **adds an element to the end** of a list? | `append` |
| Given `services = {22: "SSH", 80: "HTTP"}`, what does `services[80]` return? | `"HTTP"` |
| What dictionary method lets you retrieve a value with a **safe fallback** if the key does not exist? | `get` |

* **`.append(x)`:** `ports = [22]; ports.append(80)` → `[22, 80]`.
* **Dict lookup:** `services[80]` → **`"HTTP"`** (+ KeyError si no existe).
* **`.get(key, default):`** `services.get(443, "closed")` → `"closed"`.

### Task 5 — Operadores Aritméticos y de Membresía / Arithmetic and Membership Operators

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What operator returns the **remainder of a division**? | `%` |
| What does `10 // 3` evaluate to? | `3` |
| What does `2 ** 10` evaluate to? | `1024` |

* **`%`** = módulo (resto). **`//`** = floor division (`10 // 3 = 3`). **`**`** = exponente (`2 ** 10 = 1024`).
* De paso: `in`/`not in` son los operadores de membresía (`"ssh" in service`).

### Task 6 — Bucles: for y while / Loops: for and while

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What type of loop is best suited for **iterating over each item** in a list? | `for` |
| What does `range(3)` produce? | `0 1 2` (0, 1, 2) |
| What keyword **immediately exits** a loop? | `break` |

* **`for item in lista:`** itera directamente sobre cada elemento (el mejor ajuste).
* **`range(3)`** genera `0, 1, 2` (secuencia iterable).
* **`break`** corta el bucle; `continue` salta solo a la siguiente iteración.

### Task 7 — Conclusión / Conclusion

* **Check:** `I have successfully completed the room!`
* **ES:** Continúa con Python: Building Scripts.
* **EN:** Continue with Python: Building Scripts.

## Metodología / Methodology

1. **Paso / Step:** Responder teoría (T2–T6) con ejercicios mentales rápidos.
2. **Paso / Step:** Arrancar la VM y ejecutar `fstrings_demo.py` → copiar la última línea (`Scan complete: 192.168.1.1 has 3 open ports`).
3. **Paso / Step:** Completar el check del final.

### Cadena de aprendizaje / Learning Chain

```
type() + input() (str) -> f-strings (fstrings_demo.py) -> strings (len, slicing, lower)
  -> listas (append) + dicts (get) -> operadores (%, //, **) -> loops (for, range, break)
  -> mini-port-scanner en f-strings (puente hacia scripting)
```

**Mapeo MITRE ATT&CK / relacionado:** sin técnicas; es la base para automatizar T1110 (Bruteforce), T1059.006 (Python scripting en THM: Custom Tooling Using Python / Python for Pentesters).

**Lección:** *Python no "adivina": todo lo que entra por `input()` es texto y el slicing cuenta desde 0.* Dominar tipos e índices ahora evita bugs de scripting en los suivants rooms.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.