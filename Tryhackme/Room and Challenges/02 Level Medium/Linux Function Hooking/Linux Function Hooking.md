# Linux Function Hooking
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `linuxfunctionhooking` |
| **Link** | [TryHackMe](https://tryhackme.com/room/linuxfunctionhooking) |
| **Sección** | 02 Level Medium |
| **Fuente** | Solución de laboratorio (repositorio Apuromafo) |
| **Componentes** | Linux, function hooking, cargador dinámico (ld.so / ld-linux.so), LD_PRELOAD, /etc/ld.so.preload, compilación de librerías (-fPIC, _GNU_SOURCE), readdir/d_ino |
| **Impacto** | Aprende qué es el function hooking en Linux y cómo interceptar funciones de bibliotecas dinámicas: cargador dinámico, variables/ficheros de preload, parcheo de funciones y modificación de estructuras como `d_ino` de `readdir` para evadir o alterar el comportamiento del sistema. |
---
**Contexto:** Sala práctica sobre el hooking (interceptación) de funciones en Linux. Se cubren los artefactos del cargador dinámico (`ld.so`, `ld-linux.so`), las vías de inyección del hook (`LD_PRELOAD` a nivel de proceso, `/etc/ld.so.preload` a nivel de sistema, y la variable de entorno como mecanismo puntual), el número de bytes a sobrescribir del prólogo de la función (`3`), la macro a definir (`_GNU_SOURCE`), la compilación de la biblioteca compartida con `-fPIC`, el mensaje que imprime el hook («Yay») y la sustitución del campo `d_ino` que devuelve `readdir`.
> **ES:** Aprende sobre el hooking de funciones en Linux y diviértete enganchando (hookeando) funciones.
> **EN:** Learn about function hooking in Linux and have fun hooking functions.
## Solucionario
### Task 1 — Introducción
**Explicación:** Tarea introductoria a la sala y al concepto de intercepción de funciones en Linux. No requiere ninguna respuesta.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta de la tarea 1 (introducción). | `No answer needed` |
### Task 2 — Cargador dinámico
**Explicación:** Identificación de los ficheros del cargador dinámico involucrados en el proceso de enlazado/carga de bibliotecas compartidas sobre el que se apoya el hooking.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué dos ficheros del cargador dinámico (linker) intervienen en el hooking? | `ld.so, ld-linux.so` |
### Task 3 — Métodos de inyección del hook
**Explicación:** Vías para forzar la carga de la biblioteca que contiene la función hook: la variable de entorno `LD_PRELOAD` (carga por proceso), el fichero global `/etc/ld.so.preload` (carga para todo el sistema) y la variable de entorno como mecanismo puntual de inyección.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Con qué variable se fuerza la carga del hook a nivel de proceso? | `LD_PRELOAD` |
| 2 | ¿Qué fichero configura el hooking a nivel global/sistema? | `/etc/ld.so.preload` |
| 3 | ¿Qué mecanismo se utiliza para la inyección puntual del hook? | `Environment Variable` |
### Task 4 — Parcheo de la función
**Explicación:** Preparación de la biblioteca y del parche: número de bytes del prólogo de la función que hay que sobrescribir para redirigir la ejecución al hook y macro de glibc que debe definirse en el código de la biblioteca compartida.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos bytes hay que sobrescribir para saltar al hook? | `3` |
| 2 | ¿Qué macro se debe definir en el código de la biblioteca? | `_GNU_SOURCE` |
### Task 5 — Compilación de la biblioteca
**Explicación:** Compilación de la biblioteca compartida que contiene el hook y validación del funcionamiento: la flag que genera código independiente de posición (obligatoria para shared libraries) y el mensaje que imprime el hook al ejecutarse la prueba.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag de compilación se necesita para la biblioteca compartida? | `-fPIC` |
| 2 | ¿Qué mensaje imprime el hook en la prueba? | `Yay` |
### Task 6 — Hooking de readdir (d_ino)
**Explicación:** Aplicación del hook sobre `readdir`: el campo del `struct dirent` que se sustituye/modifica en el hook (`d_ino`) y la comprobación adicional de la tarea (sin respuesta).
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué campo del struct devuelto por `readdir` se modifica en el hook? | `d_ino` |
| 2 | Respuesta adicional de la tarea 6. | `No answer needed` |
### Task 7 — Cierre
**Explicación:** Tarea final de cierre de la sala. No requiere ninguna respuesta adicional.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta de la tarea 7 (cierre). | `No answer needed` |
---
**Metodología:** Compilación de la biblioteca compartida con `-fPIC` definiendo `_GNU_SOURCE` → carga del hook vía `LD_PRELOAD` o `/etc/ld.so.preload` → sobrescritura de los primeros `3` bytes del prólogo de la función objetivo → redirección de la ejecución al hook → modificación del campo `d_ino` de `readdir` → verificación con el mensaje «Yay».
### Cadena de ataque / Attack Chain
Un usuario no privilegiado puede interceptar funciones de bibliotecas dinámicas: se compila una librería que exporta la misma función que el binario objetivo (p. ej. `readdir`) usando `-fPIC` y `_GNU_SOURCE`; se fuerza su carga con `LD_PRELOAD` (por proceso) o escribiéndola en `/etc/ld.so.preload` (todo el sistema); al sobrescribir los `3` bytes del prólogo, el binario ejecuta el hook, que modifica campos como `d_ino` del `struct dirent` devuelto (verificación: mensaje «Yay»). No hay payloads adicionales en el laboratorio.
**Learning chain:** cargador dinámico → métodos de preload (LD_PRELOAD / ld.so.preload) → parcheo de 3 bytes → compilación -fPIC con _GNU_SOURCE → hooking de `readdir` (`d_ino`).
**Lección:** *El function hooking en Linux permite alterar el comportamiento de cualquier binario dinámico sin tocar su código fuente: dominar LD_PRELOAD, el prólogo de las funciones y el cargador dinámico da control total sobre los resultados que el binario devuelve.*
**MITRE ATT&CK:** T1574.006 (Dynamic Linker Hijacking - LD_PRELOAD / /etc/ld.so.preload), T1055 (Process Injection - inyección del hook en el proceso), T1562.001 (Impair Defenses - evasión de detecciones alterando el comportamiento), T1059.004 (Unix Shell - compilación y prueba del hook).
**Fuente:** [TryHackMe - Linux Function Hooking](https://tryhackme.com/room/linuxfunctionhooking)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.