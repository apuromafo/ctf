# 0x00sec 2017 — Reversing challenge-000 (guessme)

| Campo | Valor |
|-------|-------|
| **Evento / Event** | 0x00sec CTF 2017 |
| **Categoría / Category** | Reversing 50 (Linux ELF64) |
| **Reto / Challenge** | challenge-000 (guessme) |

## 🎯 Objetivo / Objective

> **ES:** Hallar la key que el binario compara char a char (menos `0x61`) hasta imprimir `Good key!` + flag.
> **EN:** Find the key the binary checks char by char (minus `0x61`) until `Good key!` + flag.

## 🔑 Flag

`0x00CTF{abbcdfinvidloz}`

## 🛠️ Método / Method

> **ES:** `file` → ELF64 stripped; al correr pide key y falla. En objdump, el loop resta `0x61` (`lea ebx,[rax-0x61]`) a cada char ingresado y lo compara con la tabla interna. Con gdb, breakpoint en el `cmp` e inspeccionar el char comparado en cada vuelta reconstruye la key `abbcdfinvidloz`.
> **EN:** `file` → stripped ELF64; run asks for a key and FAILs. In objdump, the loop subtracts `0x61` per input char and compares against an internal table. In gdb, break on the `cmp` and read each compared char to rebuild key `abbcdfinvidloz`.

```bash
./guessme
# Enter a key: abbcdfinvidloz
# Good key!
# The flag is: 0x00CTF{abbcdfinvidloz}
```

## 📚 Fuentes / Sources

- [0x00ctf-2017 write-up — st98 (Harekaze)](https://st98.github.io/diary/posts/2017-12-18-0x00ctf-2017.html) — st98 — acceso 2026-09-25 (paráfrasis ES/EN del método).
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente.
> **EN:** Educational and personal use only.

_Fecha de edición: 2026-09-25_
