# Semtex Nivel 0 - 1

| Campo | Valor |
|-------|-------|
| **Juego / Game** | Semtex (offline) |
| **Nivel / Level** | 0 - 1 |
| **URL** | https://overthewire.org/wargames/semtex/ |

Semtex Level 0
Get a shell
semtex.labs.overthewire.org

x86/elf:	Connect to port 24000
amd64/elf:	Connect to port 24001
ppc/mach-O:	Connect to port 24002
Receive data until the port is closed.

Every second byte you receive is trash, ignore it. The other bytes are an executable that shows you the password.

Then login to semtex1@semtex.labs.overthewire.org on port 2229

Thanks to mrx for the amd64 and ppc binaries!

Reading Material
Beej’s guide to network programming

---

## Fuentes / Sources

- OTW: https://overthewire.org/wargames/semtex/ - fecha de acceso: 2026-09-25.
- Autor notas: Apuromafo.

---

## Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire.

_Fecha de edición: 2026-09-25_
