# 0x00sec 2017 — Reversing challenge-004 (hello)

| Campo | Valor |
|-------|-------|
| **Evento / Event** | 0x00sec CTF 2017 |
| **Categoría / Category** | Reversing 50 (Linux ELF64 truncado) |
| **Reto / Challenge** | challenge-004 (hello) |

## 🎯 Objetivo / Objective

> **ES:** Password que, xoreado con el blob en `0x400c18`, produce `0x00CTF{`.
> **EN:** Password that, xored with the blob at `0x400c18`, yields `0x00CTF{`.

## 🔑 Flag

`0x00CTF{0bfU5c473D_PtR4Z3}` (password: `1nItG0T!`)

## 🛠️ Método / Method

> **ES:** `file`/`objdump` fallan (truncado); con r2 sí desensambla. La rutina xorea input con el blob y compara contra `0x00CTF{`. Extraer 8 bytes (`pcp 8 @ 0x400c18`) y xorear con `0x00CTF{` (pwntools) da el password `1nItG0T!`; ingresarlo imprime la flag.
> **EN:** `file`/`objdump` fail (truncated); r2 disassembles fine. The routine xors input with the blob and compares to `0x00CTF{`. Dump 8 bytes (`pcp 8 @ 0x400c18`) and xor with `0x00CTF{` (pwntools) → password `1nItG0T!`; entering it prints the flag.

```bash
./hello
# Welcome to the Twinlight Zone!!!
# Password: 1nItG0T!
# 0x00CTF{0bfU5c473D_PtR4Z3}
```

```python
from pwn import *
buf = bytes([0x01,0x16,0x79,0x44,0x04,0x64,0x12,0x5a])
xor(buf, '0x00CTF{')  # -> b'1nItG0T!'
```

## 📚 Fuentes / Sources

- [0x00ctf-2017 write-up — st98 (Harekaze)](https://st98.github.io/diary/posts/2017-12-18-0x00ctf-2017.html) — st98 — acceso 2026-09-25 (paráfrasis ES/EN del método r2+pwntools).
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente.
> **EN:** Educational and personal use only.

_Fecha de edición: 2026-09-25_
