# REloaded

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF / Reverse Engineering | `reloaded` | https://tryhackme.com/room/reloaded | 03 Level Hard | TryHackMe | reverse engineering / Windows 10 / debugger / assembly / jnz / exe packing | Reto de ingeniería inversa sobre un binario de Windows: cinco respuestas que validan el análisis del ejecutable, su versión del sistema, la instrucción clave en ensamblador y las flags por nivel. |

---

**Contexto:** Sala de reverse engineering centrada en analizar un binario de Windows. Las preguntas recogen hallazgos del análisis: una frase relacionada con el nivel 34 (o "Level 340"), la versión del sistema (1709), el texto del level 3 y la instrucción de ensamblador clave (`jnz`), el nivel 4 (`THMctf-L4`) y una frase final sobre Alan Turing. Preservando la ortografía original (incluido el espacio final en `jnz `).

> **ES:** "Ingeniería inversa del binario: responde sobre niveles, instrucción jnz y las flags del ejecutable."
> **EN:** "Reverse engineer the binary: answer about levels, the jnz instruction and the executable flags."

## Solucionario

### Task 1: Frase Level 340 / Level 340 phrase

**Explicación:** Frase obtenida del análisis inicial del binario, relacionada con el level 340. Contenido original de la tarea:

```text
1. L3v3lZ340_is_D02e
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Frase asociada al level 340. | `L3v3lZ340_is_D02e` |

### Task 2: Versión del sistema / System version

**Explicación:** Versión de Windows del sistema sobre el que se analiza el binario. Contenido original de la tarea:

```text
2. 1709
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Versión del sistema operativo. | `1709` |

### Task 3: Level 3 y la instrucción jnz / Level 3 and the jnz instruction

**Explicación:** Las dos respuestas del level 3: el texto del nivel y la instrucción de ensamblador clave. La segunda conserva el espacio final original (`jnz `). Contenido original de la tarea:

```text
3. 1. L3_1s_20t_Th3_L131t
   2. jnz 
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Texto del level 3. | `L3_1s_20t_Th3_L131t` |
| 2 | Instrucción de ensamblador clave del level 3. | `jnz ` |

### Task 4: Level 4 / Level 4

**Explicación:** Flag o texto asociado al level 4 del binario. Contenido original de la tarea:

```text
4. THMctf-L4
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Texto/flag del level 4. | `THMctf-L4` |

### Task 5: Frase final sobre Alan Turing / Final phrase about Alan Turing

**Explicación:** Frase final del reto relacionada con Alan Turing. Se conserva la ortografía y el singular originales ("Was a Geniuse"). Contenido original de la tarea:

```text
5. Alan Turing Was a Geniuse
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Frase final sobre Alan Turing. | `Alan Turing Was a Geniuse` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Frase asociada al level 340. | `L3v3lZ340_is_D02e` |
| 2 | Versión del sistema operativo. | `1709` |
| 3 | Texto del level 3. | `L3_1s_20t_Th3_L131t` |
| 4 | Instrucción de ensamblador clave del level 3. | `jnz ` |
| 5 | Texto/flag del level 4. | `THMctf-L4` |
| 6 | Frase final sobre Alan Turing. | `Alan Turing Was a Geniuse` |

---

**Metodología:**
1. Ejecutar o desempaquetar el binario de Windows y obtener la frase del level 340.
2. Identificar la versión del sistema sobre la que corre el programa.
3. Navegar por los niveles del programa y extraer el texto del level 3.
4. Analizar el flujo en ensamblador y localizar la instrucción de salto clave (`jnz`).
5. Completar el level 4 y recoger la frase final del reto sobre Alan Turing.

### Cadena de ataque / Attack Chain

```text
Binario -> desempaquetado/ejecución -> L3v3lZ340_is_D02e -> Windows 1709 -> Level 3 (L3_1s_20t_Th3_L131t + jnz) -> THMctf-L4 -> "Alan Turing Was a Geniuse"
```

**Learning chain:** `Análisis del binario -> niveles -> ensamblador (jnz) -> versionado del sistema -> texto final`

**Lección:** *El análisis de un binario de reto combina ejecución, lectura de strings y seguimiento del flujo de control (como `jnz`); hay que copiar cada respuesta exactamente, incluso el espacio final de `jnz `.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1059 (Command and Scripting Interpreter), T1106 (Native API), T1211 (Exploitation for Defense Evasion)

**Fuente:** [TryHackMe - REloaded](https://tryhackme.com/room/reloaded)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.