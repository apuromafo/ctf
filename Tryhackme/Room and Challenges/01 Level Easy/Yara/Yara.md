# Yara

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `yara` | https://tryhackme.com/room/yara | 01 Level Easy | TryHackMe | YARA · reglas de detección · escaneo de webshells | Detección de malware y webshells (b374k) mediante reglas YARA propias y herramientas de análisis |

---

**Contexto:** Sala introductoria de TryHackMe dedicada a YARA, el lenguaje de reglas para identificar y clasificar muestras de malware. La sala presenta la sintaxis básica de YARA, el emparejamiento de cadenas (incluido el formato hexadecimal), y cierra con ejercicios prácticos: escanear archivos como `file2/1ndex.php` con reglas propias (`yara file2.yar file2/1ndex.php`), distinguir resultados positivos y negativos (Yay/Nay, Suspicious/Benign), identificar versiones concretas de webshells como b374k y contrastar la detección con herramientas de escaneo APT como THOR APT Scanner.

> **ES:** La sala enseña a escribir y ejecutar reglas YARA para detectar malware y webshells, escaneando muestras reales como la webshell b374k en `file2/1ndex.php` y cruzando los resultados con herramientas de escaneo APT.
> **EN:** The room teaches writing and running YARA rules to detect malware and webshells, scanning real samples such as the b374k webshell in `file2/1ndex.php` and cross-checking results with APT scanning tools.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:**
1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la tarea introductoria / Read the intro task | `No answer needed` |

### Task 2: Emparejamiento hexadecimal / Hex matching

**Explicación:**
2. 1. hexadecimal
   2. Yay

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Emparejamiento hexadecimal / Hex matching | `1. hexadecimal`<br>`2. Yay` |

### Task 3: Lectura / Reading

**Explicación:**
3. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 3 | Lee la tarea / Read the task | `No answer needed` |

### Task 4: Lectura / Reading

**Explicación:**
4. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | Lee la tarea / Read the task | `No answer needed` |

### Task 5: Lectura / Reading

**Explicación:**
5. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5 | Lee la tarea / Read the task | `No answer needed` |

### Task 6: Lectura / Reading

**Explicación:**
6. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | Lee la tarea / Read the task | `No answer needed` |

### Task 7: Lectura / Reading

**Explicación:**
7. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 7 | Lee la tarea / Read the task | `No answer needed` |

### Task 8: Detección de webshells / Webshell detection

**Explicación:**
8. 1. Suspicious
   2. webshell_metaslsoft
   3. Web Shell
   4. Str1
   5. b374k 2.2
   6. 1
   7. Benign
   8. b374k 3.2.3

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 8 | Escaneo YARA de la webshell b374k / YARA scan of the b374k webshell | `1. Suspicious`<br>`2. webshell_metaslsoft`<br>`3. Web Shell`<br>`4. Str1`<br>`5. b374k 2.2`<br>`6. 1`<br>`7. Benign`<br>`8. b374k 3.2.3` |

### Task 9: Ejecutar reglas YARA / Running YARA rules

**Explicación:**
9. 1. yara file2.yar file2/1ndex.php
   2. Yay
   3. No answer needed
   4. Yay
   5. Zepto
   6. 20
   7. 700KB

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 9 | Ejecución de YARA contra `file2/1ndex.php` / Running YARA against `file2/1ndex.php` | `1. yara file2.yar file2/1ndex.php`<br>`2. Yay`<br>`3. No answer needed`<br>`4. Yay`<br>`5. Zepto`<br>`6. 20`<br>`7. 700KB` |

### Task 10: Detección APT / APT detection

**Explicación:**
10. 1. Yay
    2. Webshell_b374k_rule1
    3. THOR APT Scanner
    4. Nay
    5. EXE
    6. Zepto
    7. Nay

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 10 | Detección de familia y herramientas APT / APT family and tools detection | `1. Yay`<br>`2. Webshell_b374k_rule1`<br>`3. THOR APT Scanner`<br>`4. Nay`<br>`5. EXE`<br>`6. Zepto`<br>`7. Nay` |

### Task 11: Conclusión / Conclusion

**Explicación:**
11. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 11 | Lee la tarea de cierre / Read the closing task | `No answer needed` |

---

**Metodología:** Escribir reglas YARA probando distintos tipos de coincidencia (cadenas en claro y hexadecimales), ejecutar el escáner con `yara <regla> <objetivo>` (p. ej. `yara file2.yar file2/1ndex.php`), interpretar los resultados positivos/negativos (Yay/Nay, Suspicious/Benign), identificar versiones concretas de la webshell b374k (2.2 vs 3.2.3) por sus cadenas (Str1) y validar los hallazgos con herramientas de escaneo APT como THOR APT Scanner.

### Cadena de ataque / Attack Chain

```text
regla YARA (cadenas en claro + hexadecimal) -> yara <regla> <objetivo> -> match (Yay/Suspicious) / no match (Nay/Benign) -> identificación de webshell b374k (versiones) -> validación con escáner APT (THOR)
```

**Learning chain:** YARA -> sintaxis de reglas -> string matching (hexadecimal) -> escaneo de archivos -> detección de webshells -> detección APT.

**Lección:** *Una regla YARA bien construida combina cadenas de texto y hexadecimales y debe probarse contra muestras reales para distinguir binarios benignos de webshells y malware, evitando tanto falsos positivos como falsos negativos.*

**MITRE ATT&CK:** T1505.003 (Web Shell), T1027 (Obfuscated Files or Information), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Yara](https://tryhackme.com/room/yara)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.