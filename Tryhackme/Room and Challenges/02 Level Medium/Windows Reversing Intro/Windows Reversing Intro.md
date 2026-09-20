# Windows Reversing Intro

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Reversing | windowsreversingintro | https://tryhackme.com/room/windowsreversingintro | 02 Level Medium | TryHackMe | Windows x64, ingeniería inversa, debugging, instrucciones x64, printf/format strings | Análisis y comprensión de binarias nativas de Windows |

---

**Contexto:** La sala **Windows Reversing Intro** introduce la ingeniería inversa de binarias nativas x64 en Windows mediante un pequeño ejecutable de ejemplo. Se practica el análisis estático y dinámico con un depurador de Windows, la localización de llamadas a funciones del runtime (como `printf`) y la lectura de instrucciones en ensamblador x64, hasta identificar el formato tratado por el programa.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Presentación de la sala y de las herramientas de reversing que se utilizarán. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 2: Descarga del binario / Binary download
**Explicación:**

Se descarga y despliega el binario de ejemplo en el entorno de laboratorio. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 3: Inspección estática / Static inspection
**Explicación:**

Se examina el binario de forma estática para localizar las cadenas y funciones relevantes. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 4: Abordaje de la rutina de impresión / Print routine
**Explicación:**

Siguiendo la ejecución se localiza la instrucción que carga el puntero al formato dentro de la llamada a la función de impresión (`printf`).

Respuesta: `lea rcx, Format`

### Task 5: Iteración sobre el formato / Format handling
**Explicación:**

Se identifica la instrucción que avanza el puntero sobre la cadena de formato durante el procesamiento.

Respuesta: `inc rcx`

### Task 6: Confirmación del análisis / Analysis confirmation
**Explicación:**

Se verifica el flujo de la función de impresión y el resultado del análisis. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 7: Reflexión final / Final thoughts
**Explicación:**

Se consolidan las técnicas de reversing vistas en la sala. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 8: Cierre / Conclusion
**Explicación:**

Recapitulación final de la sala. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción al reversing | `No answer needed` |
| 2 | Descarga del binario | `No answer needed` |
| 3 | Inspección estática del binario | `No answer needed` |
| 4 | Instrucción que carga el puntero al formato | `lea rcx, Format` |
| 5 | Instrucción que avanza el puntero de formato | `inc rcx` |
| 6 | Confirmación del análisis | `No answer needed` |
| 7 | Reflexión final | `No answer needed` |
| 8 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Ingeniería inversa de una pequeña binaria x64 de Windows: análisis estático para localizar la cadena de formato, seguimiento dinámico con depurador de la función `printf` y lectura de instrucciones x64 (`lea rcx, Format` y `inc rcx`) para entender cómo se procesa el argumento de formato.

**Learning chain:** Preparación del entorno → inspección estática → localización de la rutina de impresión → carga del formato (`lea rcx`) → avance del puntero (`inc rcx`) → consolidación.

**Lección:** *En reversing, la diferencia entre una rutina trivial y una aparentemente compleja es saber qué instrucción carga cada argumento: una sola `lea` puede delatar todo el propósito de una función.*

**MITRE ATT&CK:** T1106 Native API · T1204 User Execution · T1059 Command and Scripting Interpreter.

**Fuente:** [TryHackMe - Windows Reversing Intro](https://tryhackme.com/room/windowsreversingintro)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.