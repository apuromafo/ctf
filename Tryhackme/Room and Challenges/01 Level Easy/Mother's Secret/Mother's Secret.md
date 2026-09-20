# Mother's Secret

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (CTF) | `motherssecret` | https://tryhackme.com/room/motherssecret | 01 Level Easy | TryHackMe | Enumeración / análisis estático / scripting / escalada de privilegios / flags | Reto CTF de nivel Easy: seguir el rastro dejado en la máquina Mother's Secret hasta recuperar las flags de la sala. |

---

**Contexto:** Sala tipo CTF del catálogo de TryHackMe. El recorrido combina enumeración, análisis de archivos y ejecución de comandos hasta desvelar la secuencia de la sala: un primer item de lectura, seguido por valores numéricos, una flag de transformación (`Flag{X3n0M0Rph}`), un usuario (`Ash`), la flag temática `THM_FLAG{0RD3R_937}`, una ruta del sistema (`/opt/m0th3r`) y la flag final de la estructura `Flag{Ensure_return_of_organism_meow_meow!}`. Todo se conserva verbatim.

> **ES:** Completar la secuencia del reto Mother's Secret: valores, flags intermedias, usuario y ruta hasta la flag final.
> **EN:** Complete the Mother's Secret challenge sequence: values, intermediate flags, user and path up to the final flag.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala y de la mecánica del reto. Tarea de lectura sin respuesta.

Contenido original de la tarea / Original task content:

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. / Read the task content. | `No answer needed` |

### Task 2: El secreto de Mother / Mother's secret

**Explicación:** La tarea de resolución acumula los valores que se van descubriendo a lo largo del reto: dos números (`100375` y `937`), la flag intermedia `Flag{X3n0M0Rph}`, el usuario `Ash`, la flag `THM_FLAG{0RD3R_937}`, la ruta `/opt/m0th3r` y la flag final `Flag{Ensure_return_of_organism_meow_meow!}`. Todos se conservan verbatim.

Contenido original de la tarea / Original task content:

```text
2. 1. 100375
   2. 937
   3. Flag{X3n0M0Rph}
   4. Ash
   5. THM_FLAG{0RD3R_937}
   6. /opt/m0th3r
   7. Flag{Ensure_return_of_organism_meow_meow!}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primer valor de la secuencia / First value of the sequence | `100375` |
| 2 | Segundo valor de la secuencia / Second value of the sequence | `937` |
| 3 | Flag de transformación / Transformation flag | `Flag{X3n0M0Rph}` |
| 4 | Usuario encontrado / User found | `Ash` |
| 5 | Flag temática de la sala / Room thematic flag | `THM_FLAG{0RD3R_937}` |
| 6 | Ruta en el sistema / Path on the system | `/opt/m0th3r` |
| 7 | Flag final / Final flag | `Flag{Ensure_return_of_organism_meow_meow!}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Primer valor de la secuencia / First value of the sequence | `100375` |
| 2 | Segundo valor de la secuencia / Second value of the sequence | `937` |
| 3 | Flag de transformación / Transformation flag | `Flag{X3n0M0Rph}` |
| 4 | Usuario encontrado / User found | `Ash` |
| 5 | Flag temática de la sala / Room thematic flag | `THM_FLAG{0RD3R_937}` |
| 6 | Ruta en el sistema / Path on the system | `/opt/m0th3r` |
| 7 | Flag final / Final flag | `Flag{Ensure_return_of_organism_meow_meow!}` |

---

**Metodología:** Avanzar por la secuencia del reto: lectura de la introducción, obtención de los valores numéricos, recuperación de la flag de transformación, identificación del usuario, captura de la flag temática, localización de la ruta `/opt/m0th3r` y obtención de la flag final.

### Cadena de ataque / Attack Chain

```text
Introducción -> 100375 -> 937 -> Flag{X3n0M0Rph} -> Ash -> THM_FLAG{0RD3R_937} -> /opt/m0th3r -> Flag{Ensure_return_of_organism_meow_meow!}
```

**Learning chain:** Lectura inicial -> valores/IDs -> transformación (X3n0M0Rph) -> usuario (Ash) -> flag temática -> ruta del sistema -> flag final.

**Lección:** *Los retos narrativos esconden la solución en una cadena de pistas encadenadas: cada valor descubierto desbloquea el siguiente paso.* 

**MITRE ATT&CK:** T1059 (Command and Scripting Interpreter), T1083 (File and Directory Discovery)

**Fuente:** [TryHackMe - Mother's Secret](https://tryhackme.com/room/motherssecret)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.