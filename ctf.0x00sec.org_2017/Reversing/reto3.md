# 0x00sec 2017 — Reversing challenge-003 (OBFTEANATION)

| Campo | Valor |
|-------|-------|
| **Evento / Event** | 0x00sec CTF 2017 |
| **Categoría / Category** | Reversing 175 (Linux ELF64 ofuscado) |
| **Reto / Challenge** | challenge-003 (OBFTEANATION, binario `sc04`) |

> *Nota: el writeup original no indica número; se asigna a challenge-003 por ser la única tarea Reversing pendiente en CTFtime (175 pts, la de mayor valor). / The original write-up states no number; mapped to challenge-003 as the only pending Reversing task on CTFtime (175 pts, highest value).*

## 🎯 Objetivo / Objective

> **ES:** Pasar el señuelo del `main`, activar el reto real vía variable de entorno y extraer el password que imprime la flag.
> **EN:** Get past the `main` decoy, trigger the real challenge via environment variable, and extract the password that prints the flag.

## 🔑 Flag

`0x00CTF{1tw4SaL0nGtR1p}` (password: `p1C0bfU5K4t0R-2o1T`, con `MAIN=31173`)

## 🛠️ Método / Method

> **ES:** `readelf` canta el truco: declara 25901 secciones pero por tamaño/offset solo caben 29; parchear ese campo (offset 60) y `objdump`/`gdb` vuelven a funcionar. El `main` visible es señuelo (flag falsa `0x00CTF{Th1s_i5_n07_th3_fl4G_Y0uR_l0Ok1n_4}`). El reto real vive en un constructor de `.init_array` (parámetro `init` de `__libc_start_main`): exige variable de entorno de 10 chars (`MAIN=31173`) y salta vía tabla de `RET`s a la rutina que pide Password. Esa rutina valida cada char con XOR ofuscado (tabla de 18 funciones en `0x6020c0`); con gdb (forzar `EDI=0` o probar chars hasta retorno 0) se extrae el password, que al ingresarlo imprime la flag.
> **EN:** `readelf` gives it away: it claims 25901 sections but only 29 fit by size/offset; patch that field (offset 60) and `objdump`/`gdb` work again. The visible `main` is a decoy (fake flag `0x00CTF{Th1s_i5_n07_th3_fl4G_Y0uR_l0Ok1n_4}`). The real challenge lives in a `.init_array` constructor (`init` param of `__libc_start_main`): it requires a 10-char env var (`MAIN=31173`) and jumps via a table of `RET`s to the Password routine. That routine checks each char with obfuscated XOR (18-function table at `0x6020c0`); under gdb (force `EDI=0` or brute-force chars until return 0) the password leaks, and entering it prints the flag.

```bash
cp sc04 sc04.patch
printf '\x1d\x00' | dd of=sc04.patch bs=1 seek=60 count=2 conv=notrunc
MAIN=31173 ./sc04.patch
# Congrats!. You have found the real challenge!!! Let's Play
# Password : p1C0bfU5K4t0R-2o1T
# 0x00CTF{1tw4SaL0nGtR1p}
```

## 📚 Fuentes / Sources

- [[0x00CTF] OBFTEANATION Write-up — 0x00pf (pico, autor del reto)](https://archive.0x00sec.org/t/0x00ctf-obfteanation-write-up/4731.html) — 0x00pf — acceso 2026-09-26 (paráfrasis ES/EN del método).
- Confirmación independiente en el mismo hilo: script gdb de Leeky reproduce password `p1C0bfU5K4t0R-2o1T` y flag `0x00CTF{1tw4SaL0nGtR1p}` — acceso 2026-09-26.
- [CTFtime — 0x00ctf-2017 tasks](https://ctftime.org/event/548/tasks/) — acceso 2026-09-26 (challenge-003, 175 pts, única tarea Reversing sin documentar; base de la asignación numérica).
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente.
> **EN:** Educational and personal use only.

_Fecha de edición: 2026-09-26_
