# Different CTF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `adana` | https://tryhackme.com/room/adana | 03 Level Hard | TryHackMe | CTF / enumeración web / gobuster / directorios / flags | Reto CTF en el que el número de flags aparece en dos partes: una de reconocimiento web (número de endpoints y ruta de directorio) y otra de recolección de tres flags a lo largo del compromiso. |

---

**Contexto:** Sala CTF de nivel Hard cuyo slug es `adana`. La primera parte del reto pide responder con valores de enumeración web (un número y una ruta de directorio), y la segunda parte recoge tres flags HTML-encoded obtenidas durante la explotación del objetivo. El nombre y la mecánica siguen la línea de los CTF clásicos de la plataforma: enumeración, fuzzing de directorios y recolección de banderas.

> **ES:** "CTF clásico: enumera la web, encuentra el número de flags y la ruta de directorio, y recoge las tres flags del reto."
> **EN:** "Classic CTF: enumerate the web, find the number of flags and the directory path, and collect the three room flags."

## Solucionario

### Task 1: Enumeración web / Web enumeration

**Explicación:** Se responden los valores de reconocimiento: el número resultante de la enumeración y la ruta del directorio encontrado. Contenido original de la tarea:

```text
1. 1. 2
   2. /announcements/
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Número resultante de la enumeración de la tarea. | `2` |
| 2 | Ruta del directorio encontrado. | `/announcements/` |

### Task 2: Flags del reto / Room flags

**Explicación:** Se recogen las tres flags del reto. Contenido original de la tarea:

```text
2. 1. THM{343a7e2064a1d992c01ee201c346edff}
   2. THM{8ba9d7715fe726332b7fc9bd00e67127}
   3. THM{c5a9d3e4147a13cbd1ca24b014466a6c}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag 1 del reto. | `THM{343a7e2064a1d992c01ee201c346edff}` |
| 2 | Flag 2 del reto. | `THM{8ba9d7715fe726332b7fc9bd00e67127}` |
| 3 | Flag 3 del reto. | `THM{c5a9d3e4147a13cbd1ca24b014466a6c}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Número resultante de la enumeración de la tarea. | `2` |
| 2 | Ruta del directorio encontrado. | `/announcements/` |
| 3 | Flag 1 del reto. | `THM{343a7e2064a1d992c01ee201c346edff}` |
| 4 | Flag 2 del reto. | `THM{8ba9d7715fe726332b7fc9bd00e67127}` |
| 5 | Flag 3 del reto. | `THM{c5a9d3e4147a13cbd1ca24b014466a6c}` |

---

**Metodología:**
1. Enumerar el objetivo web y obtener el número solicitado por la primera tarea (`2`).
2. Fuzzear directorios y localizar la ruta `/announcements/`.
3. Explotar el recurso o servicio identificado para obtener la primera flag.
4. Seguir la cadena de explotación y recolectar las tres flags del reto.

### Cadena de ataque / Attack Chain

```text
Recon web -> enumeración -> 2 -> gobuster -> /announcements/ -> explotación -> THM{343a7e2064a1d992c01ee201c346edff} -> THM{8ba9d7715fe726332b7fc9bd00e67127} -> THM{c5a9d3e4147a13cbd1ca24b014466a6c}
```

**Learning chain:** `Recon -> web enumeration -> HTTP endpoints -> fuzzing de directorios -> /announcements/ -> flags`

**Lección:** *La enumeración metódica (peticiones y directorios) y la lectura cuidadosa de cada respuesta HTML son la base para resolver un CTF web con múltiples flags en cascada.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1083 (File and Directory Discovery), T1190 (Exploit Public-Facing Application), T1005 (Data from Local System)

**Fuente:** [TryHackMe - Different CTF](https://tryhackme.com/room/adana)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.