# 📒 CHANGELOG — HackTheBox (Apuromafo)

> **ES:** Cambios notables del lado HTB, recientes primero.
> **EN:** Notable HTB-side changes, newest first.

## 2026-09-30

- Nombres normalizados: `Narnia/Solution/Level7.md` y `Level9.md` → minúscula (sus hermanos 0-6 y 8 ya
  lo estaban); `img/tabla final.jpg` → `img/tabla_final.jpg`.
- `Machines/Medium/Compiled/Walkthrough.md`: **1 carácter** U+FFFD restaurado (`Versión` en la cadena de
  `ver`). Único caso de los 11 U+FFFD de HTB reconstruible con certeza. Los otros 10 se dejan intactos:
  2 en `Certificate` (frase citada de HTB que no aparece en ningún otro fichero, sin término de
  comparación) y 8 en `The Needle` (salida de terminal de la plataforma). No se inventa texto.
- Auditoría de las cifras de `INDICE.md` contra la tabla contigua del mismo fichero: 10/10 exactas.
  Única imprecisión anotada sin tocar el fichero: "164 walkthroughs" cuenta ficheros con pie estándar
  (164 de 176 `.md`; solo 142 son `Walkthrough.md`).
- IppSec reconciliado contra `COMANDOS.md`: **133/142** Machine Writeups con link (131 canónicos +
  Granny/Grandpa + 9 sin link), **132 IDs distintos**. La cifra "124/428" de la planificación local no
  era reproducible.
- `Machines/json/`: 868 dumps fuera del tracking (ya hecho el 2026-09-24, confirmado).
- **Sin cambios en contenido de writeups.** La deriva detectada en `_PLANIFICACION/` (flags 21 → 28,
  infomachine 17 → 20) se corrigió **solo en la capa local no versionada**.

## 2026-09-24

- 24 fichas Challenges <5 KB con cabecera ES/EN + pie (contenido ZH preservado como cita + paráfrasis).
- `ROADMAP.md` + `CHANGELOG.md` creados.
- Token HTB purgado del historial (filter-repo + force push `2a1a08e5`); scrapers usan `HTB_TOKEN`.
- `Machines/json/`: 868 dumps fuera del tracking y del disco.
- Estructura `01_LEARNING/`–`05_COMPETITIONS/`, sin `Soluciones/`; `INDICE.md` como mapa.
- 12 walkthroughs fusionados; Appointment + Brutus + Bumblebee + Tracks + Battlegrounds ordenados.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox.

_Fecha de edición: 2026-09-30_
