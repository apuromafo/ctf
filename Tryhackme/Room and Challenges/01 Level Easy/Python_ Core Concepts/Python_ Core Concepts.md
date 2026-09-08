# Python: Core Concepts

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `pythoncoreconcepts` |
| **Link** | [TryHackMe](https://tryhackme.com/room/pythoncoreconcepts) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + VM con scripts de práctica (fstrings_demo.py) |
| **Componentes** | Python: tipos / f-strings / strings e indexación / listas y dicts / operadores / loops |
| **Impacto** | Primera parte de la serie Python de THM; cimientos de scripting para automatizar tareas ofensivas y defensivas |

---

**Contexto:** Repaso acelerado de los core concepts de Python orientado a ciberseguridad. `type()` revela el tipo; `input()` siempre devuelve texto (**str** aunque escribas `3.14`). **f-strings** (`f"..."`) formatean dentro de print; el demo del VM (fstrings_demo.py) cierra con la línea **`Scan complete: 192.168.1.1 has 3 open ports`** (patrón mini-portscanner). Strings: **`len()`** cuenta caracteres, **`word[3:7]`** de `"TryHackMe"` es **`HackM`**, y `"ADMIN".lower()` → `"admin"`. Listas: **`.append()`**; dicts: **`services[80]`** → **`"HTTP"`** y **`.get(clave, fallback)`** para acceso seguro. Operadores: **`%`** = resto, **`10 // 3` = 3** (división entera), **`2 ** 10 = 1024`**. Bucles: **`for`** para iterar listas, **`range(3)`** → **0 1 2**, y **`break`** sale del bucle.

## Solucionario

### Task 1: Introducción / Introduction *(vm)*

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's master Python's core concepts! | `No answer needed` |

**Explicación:** Serie Python: este room = fundamentos; el compañero = building scripts. (Se accede a la VM del room).

### Task 2: Review Rápida / Quick Review: Hello World, Variables, and Conditionals

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What **built-in function** reveals the data type of a value? | `type` |
| 2 | If a user types `3.14` at an `input()` prompt, what **data type** does Python store it as before any conversion? | `str` (string) |
| 3 | On the attached VM, open and run `fstrings_demo.py`. What is the **last line** printed to the terminal? | `Scan complete: 192.168.1.1 has 3 open ports` |

**Explicación:**
- **`type()`:** `type(3.14)` → `<class 'float'>`.
- **input():** siempre `str`; hay que castear (`float(prompt)` / `int(prompt)`).
- **fstrings_demo.py:** demo de f-strings estilo mini port-scanner; la última línea imprime el resumen. *Respuesta literal: **`Scan complete: 192.168.1.1 has 3 open ports`**.*

### Task 3: Trabajando con Strings / Working with Strings

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What function returns the **number of characters** in a string? | `len` |
| 2 | Given `word = "TryHackMe"`, what does `word[3:7]` return? | `HackM` |
| 3 | What string **method** converts `"ADMIN"` to `"admin"`? | `lower` |

**Explicación:**
- **`len("TryHackMe")`** = 9.
- **Indexación / slicing:** `word[3:7]` = caracteres desde el índice 3 al 6 → **`HackM`** (índices: T=0 r=1 y=2 H=3 a=4 c=5 k=6 M=7 e=8).
- **`.lower()`:** `"ADMIN".lower()` → `"admin"` (también existe `.upper()`).

### Task 4: Listas y Diccionarios / Lists and Dictionaries

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What method **adds an element to the end** of a list? | `append` |
| 2 | Given `services = {22: "SSH", 80: "HTTP"}`, what does `services[80]` return? | `"HTTP"` |
| 3 | What dictionary method lets you retrieve a value with a **safe fallback** if the key does not exist? | `get` |

**Explicación:**
- **`.append(x)`:** `ports = [22]; ports.append(80)` → `[22, 80]`.
- **Dict lookup:** `services[80]` → **`"HTTP"`** (+ KeyError si no existe).
- **`.get(key, default)`:** `services.get(443, "closed")` → `"closed"`.

### Task 5: Operadores Aritméticos y de Membresía / Arithmetic and Membership Operators

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What operator returns the **remainder of a division**? | `%` |
| 2 | What does `10 // 3` evaluate to? | `3` |
| 3 | What does `2 ** 10` evaluate to? | `1024` |

**Explicación:**
- **`%`** = módulo (resto). **`//`** = floor division (`10 // 3 = 3`). **`**`** = exponente (`2 ** 10 = 1024`).
- De paso: `in`/`not in` son los operadores de membresía (`"ssh" in service`).

### Task 6: Bucles: for y while / Loops: for and while

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of loop is best suited for **iterating over each item** in a list? | `for` |
| 2 | What does `range(3)` produce? | `0 1 2` (0, 1, 2) |
| 3 | What keyword **immediately exits** a loop? | `break` |

**Explicación:**
- **`for item in lista:`** itera directamente sobre cada elemento (el mejor ajuste).
- **`range(3)`** genera `0, 1, 2` (secuencia iterable).
- **`break`** corta el bucle; `continue` salta solo a la siguiente iteración.

### Task 7: Conclusión / Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have successfully completed the room! | `No answer needed` |

**Explicación:** Continúa con Python: Building Scripts.

**Metodología:**
1. **Review rápida:** `type(3.14)` → `<class 'float'>`; `input()` siempre devuelve `str`, hay que castear (`float(prompt)` / `int(prompt)`); en la VM, `fstrings_demo.py` es una demo de f-strings estilo mini port-scanner y su última línea imprime el resumen literal **`Scan complete: 192.168.1.1 has 3 open ports`**.
2. **Strings:** `len("TryHackMe")` = 9 (número de caracteres = `len`); slicing `word[3:7]` → desde el índice 3 al 6 → **`HackM`** (T=0 r=1 y=2 H=3 a=4 c=5 k=6 M=7 e=8); `"ADMIN".lower()` → `"admin"` (también existe `.upper()`).
3. **Listas y dicts:** `.append(x)` añade al final (`ports = [22]; ports.append(80)` → `[22, 80]`); `services[80]` → **`"HTTP"`** (KeyError si no existe); `.get(key, default)` para acceso seguro (`services.get(443, "closed")` → `"closed"`).
4. **Operadores:** `%` = módulo (resto); `//` = floor division (`10 // 3` = 3); `**` = exponente (`2 ** 10` = 1024); además `in`/`not in` son los operadores de membresía (`"ssh" in service`).
5. **Bucles:** `for item in lista:` itera directamente sobre cada elemento (el mejor ajuste); `range(3)` genera la secuencia iterable `0, 1, 2`; `break` corta el bucle y `continue` salta solo a la siguiente iteración.
6. **Cierre:** arrancar la VM y ejecutar `fstrings_demo.py` → copiar la última línea → completar el check del final y continuar con **Python: Building Scripts**.

```
type() + input() (str) -> f-strings (fstrings_demo.py) -> strings (len, slicing, lower)
  -> listas (append) + dicts (get) -> operadores (%, //, **) -> loops (for, range, break)
  -> mini-port-scanner en f-strings (puente hacia scripting)
```

**Lección:** *Python no "adivina": todo lo que entra por `input()` es texto y el slicing cuenta desde 0.* Dominar tipos e índices ahora evita bugs de scripting en los siguientes rooms.

**Learning chain:** type() + input() (str) → f-strings (fstrings_demo.py) → strings (len, slicing, lower) → listas (append) + dicts (get) → operadores (%, //, **) → loops (for, range, break) → mini-port-scanner en f-strings (puente hacia scripting)

**MITRE ATT&CK:** T1059.006 (Command and Scripting Interpreter: Python), T1110 (Brute Force)

**Fuente:** [TryHackMe - Python: Core Concepts](https://tryhackme.com/room/pythoncoreconcepts)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
