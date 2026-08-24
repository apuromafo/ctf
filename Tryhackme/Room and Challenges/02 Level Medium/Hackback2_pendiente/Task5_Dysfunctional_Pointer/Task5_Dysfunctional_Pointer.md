# Task 5 - Dysfunctional Pointer

**Nivel:** Easy - Reverse Engineering

## Qué era

Un binario que al ejecutarse se caía (segmentation fault). Dejaba el flag escondido dentro, pero se generaba al ejecutarse, no estaba escrito como texto.

## Cómo se resolvió

1. Se miró el binario por dentro (decompilación).
2. Se encontró una función `get_flag` que convierte `684dad9f` a mayúsculas y lo imprime.
3. El programa guardaba una dirección equivocada en un puntero, por eso crasheaba.
4. Se corrigió ese puntero (4 bytes) para que apuntara a la función correcta.
5. Con el parche aplicado, el programa imprime el flag.

## Flag

THM{684DAD9F}
