# 0x41haz

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | reversing challenge | `0x41haz` | https://tryhackme.com/room/0x41haz | 01 Level Easy | TryHackMe | gdb / strings / análisis de binarios ELF / anti-reversing (cabecera dañada) / disassembly | Reto de ingeniería inversa: analizar un binario ELF con una trampa anti-reversing para recuperar la contraseña y obtener la flag. |

---

**Contexto:** Caja sencilla de reversing del catálogo de TryHackMe. Se entrega un binario ELF de Linux y una única pregunta: encontrar la contraseña. El reto incluye una medida anti-análisis (la cabecera del binario aparece dañada), por lo que hay que arreglar la cabecera antes de poder desensamblarlo correctamente y localizar la cadena con la que se compara la contraseña hardcodeada.

> **ES:** "Simple Reversing Challenge": descarga el binario, analízalo y descubre la contraseña. ¡Ten cuidado, puede haber medidas anti-reversing!
> **EN:** "Simple Reversing Challenge": download the binary, analyze it and discover the password. Beware, there may be anti-reversing measures in place!

## Solucionario

### Task 1: Encuentra la contraseña / Find the password

**Explicación:** Tras descargar el binario, `file` muestra una cabecera ELF dañada (medida anti-reversing). Se corrige la cabecera y se desensambla la función `main`. Al revisar el disassembly aparece una cadena llamativa usada en la comparación de la contraseña: `2@@25$gfsT&@L`. Ejecutando el binario con esa contraseña, el programa la acepta y devuelve la flag.

```bash
file ./0x41haz                      # cabecera dañada: no se identifica como ELF válido
# 1) Se arregla la cabecera del ELF
gdb -q ./0x41haz
(gdb) break main
(gdb) run
(gdb) pdf                          # disassemble main -> se ve la comparación con 2@@25$gfsT&@L
# 2) Se ejecuta el binario con la contraseña recuperada
./0x41haz
> 2@@25$gfsT&@L
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password? / ¿Cuál es la contraseña? | `THM{2@@25$gfsT&@L}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the password? / ¿Cuál es la contraseña? | `THM{2@@25$gfsT&@L}` |

---

**Metodología:** Reconocer que el binario está "roto" a propósito (anti-reversing), reparar la cabecera ELF, desensamblar `main` con gdb y localizar la cadena hardcodeada con la que se compara la entrada. Finalmente se ejecuta el binario con esa contraseña para recibir la flag.

### Cadena de ataque / Attack Chain

```text
Descargar binario -> file (cabecera dañada) -> reparar cabecera ELF -> desensamblar main -> localizar cadena de comparación -> ejecutar binario con la contraseña -> obtener flag
```

**Learning chain:** `file` -> arreglar ELF -> gdb/pdf -> strings/disassembly -> ejecución con el input ganador -> flag.

**Lección:** *Una cabecera "corrupta" suele ser una trampa anti-reversing deliberada; arreglarla permite desensamblar el binario como siempre.*

**MITRE ATT&CK:** N/A (reto de ingeniería inversa de un binario local)

**Fuente:** [TryHackMe - 0x41haz](https://tryhackme.com/room/0x41haz)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.