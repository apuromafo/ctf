# JVM Reverse Engineering

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Reverse Engineering | jvmreverseengineering | https://tryhackme.com/room/jvmreverseengineering | 02 Level Medium | TryHackMe | JVM, Java bytecode, javap, desensamblado, cracking | Comprensión y explotación de binarios Java en la JVM |

---

**Contexto:** La sala **JVM Reverse Engineering** introduce el análisis de aplicaciones Java compiladas a bytecode para la JVM. Se trabaja con herramientas de línea de comandos como `javap` y desensambladores para inspeccionar ficheros `.class`, interpretar la pila de operandos, identificar algoritmos de ofuscación (como `lxor`) y extraer flags de métodos protegidos. La resolución combina lectura de bytecode, análisis sintáctico de salidas verbosas y recuperación de credenciales/flags embebidas en el código.

## Solucionario

### Task 1: Fundamentos del bytecode JVM
**Explicación:**

Se exploran los componentes básicos del fichero `.class` de Java: encabezados, constant pool, métodos y atributos. Se aprende a leer la pila de operandos y el set de instrucciones. Los valores solicitados describen características del archivo de clase: el número de versión menor, un opcode de operación XOR sobre longs (`lxor`) y el modificador de salida de `javap` que muestra detalles adicionales (`verbose`).

Respuesta:

1. `No answer needed`
2. `-3`
3. `lxor`
4. `verbose`

### Task 2: Análisis con javap
**Explicación:**

Con `javap` se desensambla el fichero `.class` objetivo. Se identifica el nombre del archivo fuente compilado (`SecretSourceFile.java`), la referencia simbólica completa de la clase padre (`java/lang/Object`) y el número de métodos que expone la clase.

```bash
javap -verbose -p Secret.class
```

Respuesta:

1. `SecretSourceFile.java`
2. `java/lang/Object`
3. `2`

### Task 3: Flag de la primera aplicación
**Explicación:**

A partir del bytecode desensamblado se reconstruye la lógica del método protegido y se recupera la flag de la primera aplicación Java.

```bash
javap -c -p Target.class
```

Respuesta: `yxvF2ho95ANJVCX`

### Task 4: Flag de la segunda aplicación
**Explicación:**

Se repite el proceso de desensamblado sobre la segunda aplicación, interpretando las instrucciones y las constantes ofuscadas (operaciones XOR incluidas) para obtener la segunda flag.

Respuesta: `aSc2mRT7C6fKql6RD`

### Task 5: Reflexión sobre el proceso
**Explicación:**

Se revisa el flujo completo de ingeniería inversa sobre la JVM. No requiere respuesta escrita.

Respuesta: `No answer needed`

### Task 6: Flag de la tercera aplicación
**Explicación:**

Se analiza una tercera aplicación, aplicando los mismos pasos de descompilación e interpretación del bytecode para extraer la flag correspondiente.

Respuesta: `YafLa7T4m06e1c5R73wkEo4692G`

### Task 7: Flag de la cuarta aplicación
**Explicación:**

En la cuarta y última aplicación se combinan las técnicas vistas (desensamblado, lectura de constantes y resolución de ofuscación) para recuperar la flag final.

Respuesta: `TsVwBSiA2IDqClTtWg6D6p5cM3k`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1: Paso previo | `No answer needed` |
| 1 | Task 1: Versión menor del fichero de clase | `-3` |
| 1 | Task 1: Instrucción XOR de longs en JVM | `lxor` |
| 1 | Task 1: Modificador de javap para salida detallada | `verbose` |
| 2 | Task 2: Nombre del archivo fuente original | `SecretSourceFile.java` |
| 2 | Task 2: Clase padre referenciada | `java/lang/Object` |
| 2 | Task 2: Número de métodos | `2` |
| 3 | Task 3: Flag primera aplicación | `yxvF2ho95ANJVCX` |
| 4 | Task 4: Flag segunda aplicación | `aSc2mRT7C6fKql6RD` |
| 5 | Task 5: Cierre de la sala | `No answer needed` |
| 6 | Task 6: Flag tercera aplicación | `YafLa7T4m06e1c5R73wkEo4692G` |
| 7 | Task 7: Flag cuarta aplicación | `TsVwBSiA2IDqClTtWg6D6p5cM3k` |

---

**Metodología:** Inspección del fichero `.class` con `javap` → lectura del bytecode e instrucciones (incluidas operaciones de ofuscación como `lxor`) → interpretación del constant pool → reconstrucción de la lógica protegida → extracción de flags.

**Learning chain:** Bytecode JVM → herramienta javap → desensamblado → ofuscación XOR → reconstrucción de lógica → flags múltiples.

**Lección:** *El bytecode de la JVM es legible con `javap`: no hay secreto real en un `.class`; cualquier flag persistida en el código puede recuperarse leyendo el desensamblado.*

**MITRE ATT&CK:** T1059.007 Command and Scripting Interpreter: JavaScript/JVM · T1027.002 Obfuscated Files or Information: Software Packing · T1083 File and Directory Discovery.

**Fuente:** [TryHackMe - JVM Reverse Engineering](https://tryhackme.com/room/jvmreverseengineering)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.