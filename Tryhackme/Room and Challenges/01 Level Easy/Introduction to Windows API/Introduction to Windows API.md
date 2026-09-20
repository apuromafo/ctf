# Introduction to Windows API

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introductiontowindowsapi` | [TryHackMe](https://tryhackme.com/room/introductiontowindowsapi) | 01 Level Easy | TryHackMe | Windows API, Win32, cabeceras (winuser.h, windows.h), P/Invoke, DllImport, VirtualAlloc, CreateThread, Migración a procesos | Conocer las APIs de Windows que emplea el malware y cómo se llaman desde C/C++ y .NET para entender el comportamiento de los payloads. |

---

**Contexto:** Sala introductoria a la API de Windows vista desde el punto de vista ofensivo. Repasa los tipos y funciones de la API Win32, las cabeceras donde se declaran (windows.h, winuser.h), la distinción entre versiones ANSI (sufijo A) y Unicode (sufijo W) y flags como MEM_RESET, así como el uso de la consola y de ASLR. La segunda parte cubre la llamada a API nativas desde .NET mediante P/Invoke (DllImport, External), la resolución dinámica de funciones con GetProcAddress y LoadLibrary, y una cadena de ejemplo para inyección de código y ejecución de procesos con CreateThread, VirtualAlloc y las funciones de hooking. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

> **ES:** Identificar el papel de la API de Windows, sus funciones y cabeceras, los sufijos A/W y flags de memoria, y saber invocar esas funciones desde .NET por P/Invoke y dinámicamente con LoadLibrary/GetProcAddress.
> **EN:** Identify the role of the Windows API, its functions and headers, the A/W suffixes and memory flags, and learn to call those functions from .NET via P/Invoke and dynamically with LoadLibrary/GetProcAddress.

## Solucionario

### Task 1: Introducción a la API de Windows / Windows API Basics
**Explicación:** Se presenta la API de Windows y su importancia para entender el comportamiento de aplicaciones y malware.

1. No answer needed

### Task 2: Tipos y caracteres / Types and Characters
**Explicación:** Se repasan convenciones de la API, como las que determinan el uso de caracteres anchos o de funciones específicas.

1. N
2. N

### Task 3: Cabeceras / Headers
**Explicación:** Se localizan las declaraciones de las funciones de la API en sus cabeceras, como winuser.h y windows.h.

1. winuser.h
2. windows.h

### Task 4: Funciones y mitigaciones / Functions and Mitigations
**Explicación:** Se distinguen llamadas de sistema y mitigaciones de memoria como ASLR dentro del ecosistema de la API de Windows.

1. system
2. ASLR

### Task 5: Nombre de funciones y flags / Function Names and Flags
**Explicación:** Se identifican los sufijos de las variantes de funciones y una constante de memoria como MEM_RESET.

1. A
2. Ex
3. MEM_RESET

### Task 6: Uso de la consola / Console Usage
**Explicación:** Se valida si ciertas funciones pueden invocarse desde entornos concretos.

1. N

### Task 7: P/Invoke desde .NET / P/Invoke in .NET
**Explicación:** Se aprende a importar funciones nativas en .NET mediante DllImport y la palabra clave External.

1. DllImport
2. External

### Task 8: Resolución dinámica / Dynamic Resolution
**Explicación:** Se obtienen punteros a funciones en tiempo de ejecución con GetProcAddress y se cargan librerías con LoadLibrary.

1. GetProcAddress
2. LoadLibrary

### Task 9: Cadena de inyección y ejecución / Injection and Execution Chain
**Explicación:** Se construye el ciclo completo de una carga útil: obtener el proceso actual, instalar hooks, cargar módulos, reservar memoria con VirtualAlloc, copiar el payload con Marshal.Copy, crear el hilo con CreateThread y esperar con WaitForSingleObject.

1. GetCurrentProcess
2. SetWindowsHookEx
3. GetModuleHandle
4. UnhookWindowsHookEx
5. VirtualAlloc
6. Marshal.copy
7. CreateThread
8. WaitForSingleObject

### Task 10: Práctica final / Final Practice
**Explicación:** Ejercicio de refuerzo sobre el flujo completo del uso de la API de Windows.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Pregunta 1 no especificada en el original) | `No answer needed` |
| 2 | Pregunta de convenciones (1/2) / Convention question (1/2) | `N` |
| 3 | Pregunta de convenciones (2/2) / Convention question (2/2) | `N` |
| 4 | Cabecera de funciones de interfaz / Windows interface header | `winuser.h` |
| 5 | Cabecera principal de la API / Main Windows API header | `windows.h` |
| 6 | Llamada de sistema indicada / Indicated system call | `system` |
| 7 | Mitigación de memoria / Memory mitigation | `ASLR` |
| 8 | Sufijo de variante ANSI / ANSI variant suffix | `A` |
| 9 | Sufijo de versión extendida / Extended version suffix | `Ex` |
| 10 | Constante de memoria indicada / Indicated memory constant | `MEM_RESET` |
| 11 | (Pregunta 11 no especificada en el original) | `N` |
| 12 | Atributo de importación .NET / .NET import attribute | `DllImport` |
| 13 | Palabra clave de método externo / External method keyword | `External` |
| 14 | Resolución de funciones dinámicas / Dynamic function resolution | `GetProcAddress` |
| 15 | Carga de librerías en runtime / Runtime library loading | `LoadLibrary` |
| 16 | Handle del proceso actual / Current process handle | `GetCurrentProcess` |
| 17 | Instalación de hooks / Installing hooks | `SetWindowsHookEx` |
| 18 | Obtención de módulo del proceso / Process module handle | `GetModuleHandle` |
| 19 | Retirada de hooks / Removing hooks | `UnhookWindowsHookEx` |
| 20 | Reserva de memoria / Memory allocation | `VirtualAlloc` |
| 21 | Copia del payload / Payload copy | `Marshal.copy` |
| 22 | Creación del hilo / Thread creation | `CreateThread` |
| 23 | Espera de finalización / Wait for completion | `WaitForSingleObject` |
| 24 | (Pregunta 24 no especificada en el original) | `No answer needed` |

---

**Metodología:** Repasar el modelo de la API de Windows y sus cabeceras, comprender las variantes A/W y las mitigaciones como ASLR, importar funciones nativas desde .NET mediante P/Invoke, resolverlas dinámicamente con LoadLibrary/GetProcAddress y montar la cadena completa de ejecución de un payload con VirtualAlloc, Marshal.Copy, CreateThread y WaitForSingleObject.

### Cadena de ataque / Attack Chain

```text
GetCurrentProcess -> GetModuleHandle -> SetWindowsHookEx/UnhookWindowsHookEx -> VirtualAlloc -> Marshal.copy -> CreateThread -> WaitForSingleObject
```

**Learning chain:** Windows API -> Win32 (winuser.h, windows.h) -> variantes A/W y flags -> mitigaciones (ASLR) -> P/Invoke en .NET -> resolución dinámica -> cadena de inyección y ejecución.

**Lección:** *El malware abusa de la API nativa de Windows: conocer las funciones (VirtualAlloc, CreateThread, hooking) y saber invocarlas desde .NET o resolverlas en runtime permite entender y reproducir el ciclo de ejecución de un payload.*

**MITRE ATT&CK:** T1106 (Native API), T1055 (Process Injection), T1027 (Obfuscated Files or Information), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Introduction to Windows API](https://tryhackme.com/room/introductiontowindowsapi)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.