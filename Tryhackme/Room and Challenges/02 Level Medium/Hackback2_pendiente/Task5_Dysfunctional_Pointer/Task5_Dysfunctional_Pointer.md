# Task5_Dysfunctional_Pointer
| **Dificultad** | Easy (Reverse Engineering) |
| **Tipo** | Challenge (Reverse Engineering) |
| **Slug** | `task5dysfunctionalpointer` |
| **Link** | [TryHackMe](https://tryhackme.com/room/task5dysfunctionalpointer) |
| **Sección** | 02 Level Medium |
| **Fuente** | Contenido original de la room (Hackback2 — Task 5) |
| **Componentes** | Ingeniería inversa de binarios, decompilación, depuración, corrupción de puntero (4 bytes), parcheo de binario, función `get_flag`, conversión a mayúsculas |
| **Impacto** | Ejercicio de **reverse engineering**: un binario se cae (segmentation fault) porque almacena una dirección equivocada en un puntero; hay que decompilarlo, localizar la función `get_flag` y **corregir el puntero** para que el programa imprima el flag. |
---
**Contexto:** Reto de ingeniería inversa en el que se analiza un binario que termina en *segmentation fault*. El flag no está almacenado como texto plano, sino que se **genera en tiempo de ejecución**: existe una función `get_flag` que toma `684dad9f`, lo convierte a mayúsculas y lo imprime. El fallo se debe a que el programa guarda una **dirección incorrecta en un puntero**, por lo que hay que identificar el offset, corregir esos 4 bytes para que apunten a la función correcta y aplicar el parche.
*EN: Reverse engineering challenge analyzing a binary that crashes with a segmentation fault. The flag is not stored as plaintext but **generated at runtime**: a `get_flag` function takes `684dad9f`, uppercases it and prints it. The crash is caused by the program storing the **wrong address in a pointer**, so the 4 bytes must be corrected to point to the right function and the binary patched.*
## Solucionario
### Task 5: Dysfunctional Pointer
**Explicación:** Un binario que al ejecutarse se caía (*segmentation fault*). Dejaba el flag escondido dentro, pero se generaba al ejecutarse, no estaba escrito como texto.

A binary that crashed on execution (segmentation fault). It hid the flag inside, but it was generated at runtime, not written as text.

**Qué era / What it was**

Un binario que al ejecutarse se caía (segmentation fault). Dejaba el flag escondido dentro, pero se generaba al ejecutarse, no estaba escrito como texto.

**Cómo se resolvió / How it was resolved**

1. Se miró el binario por dentro (decompilación).
2. Se encontró una función `get_flag` que convierte `684dad9f` a mayúsculas y lo imprime.
3. El programa guardaba una dirección equivocada en un puntero, por eso crasheaba.
4. Se corrigió ese puntero (4 bytes) para que apuntara a la función correcta.
5. Con el parche aplicado, el programa imprime el flag.

*EN: The binary was inspected by decompilation; a `get_flag` function was found that uppercases `684dad9f` and prints it; the program stored a wrong address in a pointer, which caused the crash; that pointer (4 bytes) was fixed to point to the correct function; with the patch applied, the program prints the flag.*

**Flag / Bandera**

`THM{684DAD9F}`
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag (Task 5 — Dysfunctional Pointer) | `THM{684DAD9F}` |
---
**Metodología:** Decompilación del binario → localización de la función `get_flag` (`684dad9f` → mayúsculas) → identificación del puntero corrupto → corrección de los 4 bytes apuntando a la función correcta → aplicación del parche → ejecución → lectura del flag.
**Learning chain:** analizar el binario → entender por qué hace *segfault* → localizar la lógica del flag → parchear el puntero → obtener el flag.
**Lección:** *Un puntero que apunta a una dirección incorrecta provoca un crash y oculta la lógica real; el parcheo dirigido (4 bytes) restaura la ejecución y revela el flag, ilustrando el análisis de fallos a nivel de punteros.*
**MITRE ATT&CK:** T1027 (Obfuscated Files or Information) — contexto de análisis, T1140 (Deobfuscate/Decode Files or Information), T1005 (Data from Local System) — contexto.
**Fuente:** [TryHackMe - Task5_Dysfunctional_Pointer](https://tryhackme.com/room/task5dysfunctionalpointer)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
