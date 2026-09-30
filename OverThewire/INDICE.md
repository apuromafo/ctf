# ÍNDICE — OverTheWire / INDEX

> **ES:** Mapa del proyecto: 17 juegos, 114 fichas de nivel. Cada juego tiene su `Solution/`
> dentro de su propia carpeta. Cifras verificadas contra el árbol de trabajo el 2026-09-30.
> **EN:** Project map: 17 games, 114 level writeups. Each game keeps its own `Solution/`.
> Figures verified against the working tree on 2026-09-30.

## Cómo leer esto / How to read this

- `Online/` — juegos por SSH (o HTTP, en el caso de Natas).
- `Offline/` — juego sin conexión; se juega con el material descargado.
- `Released/` — wargames de conferencia **retirados**: solo hay ficha del juego, no niveles jugados.

Las **claves se conservan** como ejemplos reales de laboratorio retirado (decisión del propietario,
2026-09-25, reversión de la redacción `5813bbe1`). Esto choca con [`Rules.md`](Rules.md), que pide no publicar
credenciales; es una decisión consciente y documentada, no un descuido. Ver § Aviso.

## Online — 12 juegos, 102 fichas

| Juego / Game | Fichas | Rango | Patrón de ficheros | Conexión | Estado |
|---|---|---|---|---|---|
| [Bandit](Online/Bandit/Readme.md) | 33 | 0-32 | `level00.md`…`level32.md` | `ssh bandit0@bandit.labs.overthewire.org -p2220` | Completo |
| [Behemoth](Online/Behemoth/Readme.md) | 1 | 0 | `level00.md` | `ssh behemoth0@behemoth.labs.overthewire.org -p2221` | Solo nivel 0 |
| [Drifter](Online/Drifter/Readme.md) | 1 | 0 | `level00.md` | `ssh drifter0@drifter.labs.overthewire.org -p2230` | Solo nivel 0 |
| [FormulaOne](Online/FormulaOne/Readme.md) | 1 | 0 | `level00.md` | `ssh formulaone0@formulaone.labs.overthewire.org -p2232` | Solo nivel 0 |
| [Krypton](Online/Krypton/Readme.md) | 8 | 0-7 | `Nivel0.md`…`Nivel7.md` | `ssh krypton1@krypton.labs.overthewire.org -p2231` | Completo |
| [Leviathan](Online/Leviathan/Readme.md) | 8 | 0-7 | `level00.md`…`level07.md` | `ssh leviathan0@leviathan.labs.overthewire.org -p2223` | Completo |
| [Manpage](Online/Manpage/Readme.md) | 1 | 0 | `level00.md` | `ssh manpage0@manpage.labs.overthewire.org -p2224` | Solo nivel 0 |
| [Maze](Online/Maze/Readme.md) | 1 | 0 | `level00.md` | `ssh maze0@maze.labs.overthewire.org -p2225` | Solo nivel 0 |
| [Narnia](Online/Narnia/Readme.md) | 10 | 0-9 | `level0.md`…`Level9.md` | `ssh narnia0@narnia.labs.overthewire.org -p2226` | Completo |
| [Natas](Online/Natas/Readme.md) | 35 | 0-34 | `00.md`…`34.md` | `http://natasX.natas.labs.overthewire.org` (HTTP, no SSH) | Completo |
| [Utumno](Online/Utumno/Readme.md) | 1 | 0 | `level00.md` | `ssh utumno0@utumno.labs.overthewire.org -p2227` | Solo nivel 0 |
| [Vortex](Online/Vortex/Readme.md) | 2 | 0-1 | `level00.md`, `level01.md` | `ssh vortex0@vortex.labs.overthewire.org -p2228` | 02+ bloqueado |

## Offline — 1 juego, 12 fichas

| Juego / Game | Fichas | Rango | Patrón | Estado |
|---|---|---|---|---|
| [Semtex](Offline/Semtex/Readme.md) | 12 | 0-11 | `level00.md`…`level11.md` | Completo (partido desde una transcripción única) |

## Released — 4 juegos, 0 fichas

| Juego / Game | Conferencia | Descarga | Estado |
|---|---|---|---|
| [Abraxas](Released/Abraxas/Readme.md) | HES 2011 | `.ova` | Ficha del juego; **sin niveles jugados** |
| [HES2010](Released/HES2010/Readme.md) | HES 2010 | `.ova` | Ficha del juego; **sin niveles jugados** |
| [Monxla](Released/Monxla/Readme.md) | HES 2012 | `.iso` | Ficha del juego; **sin niveles jugados** |
| [Kishi](Released/Kishi/Readme.md) | HES 2013 + NSC 2013 | `vagrant init StevenVanAcker/kishi` | Ficha del juego; **sin niveles jugados** |

**Total: 17 juegos, 114 fichas de nivel.** Cobertura: 102 Online + 12 Offline + 0 Released.

## Material adjunto / Attached material

| Ruta | Tamaño | Nota |
|---|---|---|
| `Online/Bandit/Solution/pdf/Bandit-Explain.pdf` | 4,6 MB | Explicación oficial. **No auditada** (contenido binario) |
| `Online/Natas/Solution/pdf/Natas-Explain.pdf` | 2,2 MB | Ídem |
| `Online/Natas/Solution/Script/natas15.py` | 2,9 KB | Único script del proyecto |

No hay carpetas `img/` en ningún juego: **ningún nivel usa capturas**. Todo el contenido son
fichas de texto y terminal.

## Huecos honestos / Honest gaps

- **6 juegos con solo el nivel 0** (Behemoth, Drifter, FormulaOne, Manpage, Maze, Utumno). Son
  "seed": se creó la ficha raíz para tener el sitio mapeado. Los niveles 01+ requieren sesión en el
  laboratorio. No se inventaron niveles.
- **Vortex 02+ bloqueado**: el juego online cambia de estructura y la sesión actual no lo cubre.
- **Los 4 de `Released/` no se han jugado**: son imágenes/VM de wargames ya retirados. La
  ficha documenta la dirección de descarga y el backstory; los niveles, no.
- **Los 2 PDF no se auditaron**: no se abrió el contenido binario para contar niveles ni comprobar
  que cuadra con las fichas.

## Inconsistencias de nombres / Naming inconsistencies

No corregidas: renombrar niveles ya publicados requiere OK del propietario (`NO-TOCAR.md`).

| Juego | Inconsistencia |
|---|---|
| [Narnia](Online/Narnia/Readme.md) | `level0.md`…`level6.md`, luego `Level7.md`, `level8.md`, `Level9.md` — `L` mayúscula en 7 y 9 |
| [Krypton](Online/Krypton/Readme.md) | `Nivel0.md`…`Nivel7.md` en español, frente a `level*.md` en el resto |
| [Natas](Online/Natas/Readme.md) | `00.md`…`34.md`, sin prefijo `level` |
| Bandit, Natas y los 4 de `Released/` | 6 usan `README.md` en mayúsculas; los otros 11 juegos usan `Readme.md` |

## Ver convención de nivel / See the level convention

Cada ficha sigue la misma estructura: título, tabla de campos (juego, nivel, URL, conexión),
objetivo, credencial, método, fuentes y aviso legal. El detalle de la plantilla vive en
[`PLANTILLA_NIVEL.md`](_PLANIFICACION/PLANTILLA_NIVEL.md) (solo local, no versionado).

De las **114 fichas, 63** declaran credencial explícitamente (encabezado `# Password` /
`# Contraseña`); las 51 restantes resuelven el nivel sin llegar a la clave del siguiente.
Recuento con definición estricta de encabezado: 63 con las tres variantes de patrón
comprobadas.

## 📚 Fuentes / Sources

- OTW, índice de wargames: https://overthewire.org/wargames/ — fecha de acceso: 2026-09-30.
- URLs por juego en la tabla de arriba; todas extraídas de las fichas, no inventadas.
- Reglas del proyecto: [`Rules.md`](Rules.md) (texto original de OverTheWire).
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a OverTheWire. Este repositorio publica
> claves de laboratorios **retirados** por decisión deliberada del propietario, al contrario de lo
> que pide [`Rules.md`](Rules.md); ver § Aviso. No contiene sesiones ni cookies activas. `Bandit/Solution/
> level17.md` incluye la clave privada RSA del propio laboratorio: es la respuesta del nivel
> 17→18, material de lab retirado, no una credencial en uso.
> **EN:** Educational and personal use only. Not affiliated with OverTheWire. This repository
> publishes credentials of **retired** labs by deliberate owner decision, against what [`Rules.md`](Rules.md)
> asks; see the note above. It contains no live sessions or cookies. `Bandit/Solution/level17.md`
> embeds the lab's own RSA private key: that is the level 17→18 answer, retired-lab material, not
> a credential in use.

_Fecha de edición: 2026-09-30_
