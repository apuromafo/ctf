# Toolbox_ Vim

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `toolboxvim` | [TryHackMe - Toolbox_ Vim](https://tryhackme.com/room/toolboxvim) | 01 Level Easy | THM | Vim, editor, comandos, modos | Dominio de los comandos y modos del editor Vim |

---

**Contexto:** Sala práctica de la serie Toolbox dedicada a Vim: modos de inserción y normal, comandos de guardado y salida, copiado/pegado, borrado y búsqueda/sustitución de patrones.

> **ES:** Ejercicios de Vim: modos de inserción, comandos de guardado y salida, yanking, pegado, borrado y búsqueda-sustitución de texto.
> **EN:** Vim exercises: insert modes, save/quit commands, yanking, pasting, deleting and search/replace operations.

## Solucionario

### Task 1: Ejercicios de Vim / Vim exercises

**Explicación:** Respuestas de la sala Toolbox Vim: rutinas de edición, guardado, salida, manipulación de texto y búsqueda con regex.

1. 1. No answer needed
   2. No answer needed
2. 1. i
   2. typing
   3. esc
   4. h
   5. l
   6. k
   7. j
   8. w
   9. e
   10. i
   11. I
   12. a
   13. A
   14. o
   15. No answer needed
3. 1. :w 
   2. :w !sudo tee %
   3. :wq
   4. :q
   5. :q!
   6. :wqa
4. 1. yy
   2. 2yy
   3. y$
   4. p
   5. P
   6. dd
   7. 2dd
   8. D
   9. x
5. 1. /pattern
   2. ?pattern
   3. n
   4. N
   5. :%s/old/new/g
   6. :vimgrep

### Tabla unificada de preguntas / Unified Q&A

| # | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` / `No answer needed` |
| 2 | `i` / `typing` / `esc` / `h` / `l` / `k` / `j` / `w` / `e` / `i` / `I` / `a` / `A` / `o` / `No answer needed` |
| 3 | `:w ` / `:w !sudo tee %` / `:wq` / `:q` / `:q!` / `:wqa` |
| 4 | `yy` / `2yy` / `y$` / `p` / `P` / `dd` / `2dd` / `D` / `x` |
| 5 | `/pattern` / `?pattern` / `n` / `N` / `:%s/old/new/g` / `:vimgrep` |

---

**Metodología:** Se realizaron los ejercicios de Vim de forma guiada: entrada al modo inserción (`i`, `a`, `A`, `o`), salida con `esc`, movimiento por palabras (`w`, `e`) y letras (`h`, `l`, `k`, `j`), guardado y salida (`:w`, `:wq`, `:q`, `:q!`, `:wqa`), escritura con `sudo` (`:w !sudo tee %`), yanking (`yy`, `2yy`, `y$`), pegado (`p`, `P`), borrado (`dd`, `2dd`, `D`, `x`) y búsqueda/sustitución (`/pattern`, `?pattern`, `n`, `N`, `:%s/old/new/g`, `:vimgrep`).

### Cadena de ataque / Attack Chain

1. Abrir Vim y entrar al modo inserción (`i`).
2. Navegar y editar texto (`h`, `l`, `k`, `j`, `w`, `e`).
3. Guardar y salir del archivo (`:wq`).
4. Manipular líneas: yanking, pegado y borrado (`yy`, `p`, `dd`).
5. Buscar y sustituir patrones (`/pattern`, `:%s/old/new/g`).

**Learning chain:** Vim modes → navigation keys → save/quit commands → yanking & pasting → search and replace

**Lección:** *Dominar los modos y atajos de Vim (movimiento, edición, yanking y sustitución) acelera enormemente la edición de archivos en el terminal.*

**MITRE ATT&CK:** No aplica / Not applicable

**Fuente:** [TryHackMe - Toolbox_ Vim](https://tryhackme.com/room/toolboxvim)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.