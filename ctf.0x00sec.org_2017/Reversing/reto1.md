# 0x00sec 2017 — Reversing reto1 (Gone Fishing)

| Campo | Valor |
|-------|-------|
| **Evento / Event** | 0x00sec CTF 2017 |
| **Categoría / Category** | Reversing (Windows) |
| **Reto / Challenge** | challenge-001 (Gone Fishing) |

## 🎯 Objetivo / Objective

> **ES:** Comparación contra `0G932SE1L48Y6G` que entrega la flag.
> **EN:** Comparison against `0G932SE1L48Y6G` yielding the flag.

## 🔑 Flag

`0x00CTF{F1SH1N9_R3QU1R3S_G00D_B4IT}`

## 🛠️ Método / Method

> **ES:** Diálogo pide serial. El código tras `GetDlgItemTextW` viene con bytes basura anti-debug: reinterpretar desde `0x4013e3` revela el check real en `0x401560` (≥13 chars, comparación de 4 en 4 en `sub_401450`). Con OllyDbg, breakpoint en `cmp ax,[edx]` e ingresar cualquier serial: `edx` apunta al serial real `0G932SE1L48Y6G`. Ingresarlo entrega la flag.
> **EN:** Serial dialog. Junk anti-debug bytes after `GetDlgItemTextW`: re-read from `0x4013e3` to find the real check at `0x401560` (13+ chars, 4-by-4 compare in `sub_401450`). In OllyDbg, break on `cmp ax,[edx]` with any serial: `edx` holds the real one `0G932SE1L48Y6G`.

## 📚 Fuentes / Sources

- Nota original local (`reto1 reversing.txt`) + `referencia.png` y `tabla final.jpg` en esta carpeta.
- [0x00ctf-2017 write-up — st98 (Harekaze, 3er puesto)](https://st98.github.io/diary/posts/2017-12-18-0x00ctf-2017.html) — st98 — acceso 2026-09-25 (paráfrasis del método OllyDbg).
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente.
> **EN:** Educational and personal use only.

_Fecha de edición: 2026-09-25_
