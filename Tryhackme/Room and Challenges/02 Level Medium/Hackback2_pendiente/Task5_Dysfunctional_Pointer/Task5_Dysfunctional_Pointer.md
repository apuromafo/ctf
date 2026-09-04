# Hackback2_pendiente\Task5_Dysfunctional_Pointer [MEDIUM]

**Nivel:** Easy - Reverse Engineering

## Qué era / What it was

Un binario que al ejecutarse se caía (segmentation fault). Dejaba el flag escondido dentro, pero se generaba al ejecutarse, no estaba escrito como texto.

## Cómo se resolvió / How it was resolved

1. Se miró el binario por dentro (decompilación).
2. Se encontró una función `get_flag` que convierte `684dad9f` a mayúsculas y lo imprime.
3. El programa guardaba una dirección equivocada en un puntero, por eso crasheaba.
4. Se corrigió ese puntero (4 bytes) para que apuntara a la función correcta.
5. Con el parche aplicado, el programa imprime el flag.

## Flag / Bandera

THM{684DAD9F}

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
