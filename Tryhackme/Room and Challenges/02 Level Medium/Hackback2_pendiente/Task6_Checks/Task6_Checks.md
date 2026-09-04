# Hackback2_pendiente\Task6_Checks [MEDIUM]

**Nivel:** Medium - Reverse Engineering

## Qué era / What it was

Un binario con varias comprobaciones antes de mostrar el flag. El original se caía antes de llegar al flag.

## Cómo se resolvió / How it was resolved

1. Se analizó el binario por dentro (decompilación).
2. Se encontró la función `asvv889a` que convierte `88ED12AC` a mayúsculas y lo imprime.
3. El `main` tenía 4 comprobaciones (usuario, variable de entorno, archivo) que impedían llegar ahí.
4. Se parcheó el `main` para que llamara directo a la función del flag.
5. Con el parche aplicado, el programa imprime el flag.

## Flag / Bandera

THM{88ED12AC}

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
