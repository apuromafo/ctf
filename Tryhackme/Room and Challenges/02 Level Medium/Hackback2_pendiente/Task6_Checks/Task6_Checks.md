# Task 6 - Checks

**Nivel:** Medium - Reverse Engineering

## Qué era

Un binario con varias comprobaciones antes de mostrar el flag. El original se caía antes de llegar al flag.

## Cómo se resolvió

1. Se analizó el binario por dentro (decompilación).
2. Se encontró la función `asvv889a` que convierte `88ED12AC` a mayúsculas y lo imprime.
3. El `main` tenía 4 comprobaciones (usuario, variable de entorno, archivo) que impedían llegar ahí.
4. Se parcheó el `main` para que llamara directo a la función del flag.
5. Con el parche aplicado, el programa imprime el flag.

## Flag

THM{88ED12AC}
