# Leviathan Nivel 1 → 2

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Leviathan |
| **Nivel / Level** | 1 → 2 |
| **URL** | https://overthewire.org/wargames/leviathan/ |
| **Conexión** | `ssh leviathan1@leviathan.labs.overthewire.org -p2223` |

# username / password
leviathan1 / 3QJ3TgzHDq
# concept
* inspecting the dynamic library calls and system calls used by a process using the `ltrace` command
# method of solve
* there is a `check` SUID binary in the home directory owned by our target user, `leviathan2`
* when we run the `check` binary, it asks us for a password, but we don't know it
* we use the ltrace command to check which dynamic library calls and system calls are used when it is run
* we see that the binary is doing a `strcmp` function that checks the user input against the `sex` value
* when we provide the correct password, we get an /bin/sh shell.

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/leviathan/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
