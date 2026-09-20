# StuxCTF

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Criptografía | stuxctf | https://tryhackme.com/room/stuxctf | 02 Level Medium | TryHackMe | Criptografía, Hash cracking, ROT, Modularidad, RSA | Descifrado de flags mediante operaciones criptográficas |

---

**Contexto:** La sala **StuxCTF** es un reto CTF centrado en **criptografía y cracking**: a partir de materiales cifrados y hashes entregados en las tareas, el alumno aplica operaciones inversas (crackeo de digests MD5, técnicas de cifrado clásico y aritmética modular sobre números grandes) hasta obtener cada valor que resuelve el reto. Las respuestas son tres objetos criptográficos: un hash caído (MD5), otro digest MD5 y un entero enorme que resulta de una operación modular/RSA.

## Solucionario

### Task 1: Valores del reto criptográfico
**Explicación:**

Se resuelven las tres piezas del reto: se crackea el primer digest MD5, se obtiene el segundo digest MD5 mediante la técnica de descifrado indicada y se calcula el entero enorme que devuelve la operación modular pedida.

1. `0b6044b7807dd100b9e30f1bd09db53f`
2. `0028454003b42601548df551b738976c`
3. `47315028937264895539131328176684350732577039984023005189203993885687328953804202704977050807800832928198526567069446044422855055`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Primer valor criptográfico (MD5) | `0b6044b7807dd100b9e30f1bd09db53f` |
| 1.2 | Segundo valor criptográfico (MD5) | `0028454003b42601548df551b738976c` |
| 1.3 | Entero enorme del reto modular | `47315028937264895539131328176684350732577039984023005189203993885687328953804202704977050807800832928198526567069446044422855055` |

---

**Metodología:** Análisis de los materiales criptográficos del reto, crackeo de digest con diccionario, reversión de la transformación clásica aplicada y cálculo de la operación modular sobre el entero grande.

**Learning chain:** Inspección del material → identificación del algoritmo → crackeo/descifrado → cómputo modular → respuestas del reto.

**Lección:** *Un hash no cifra nada: su debilidad depende de la entropía del texto plano y del diccionario usado; los retos criptográficos se pierden o ganan por el algoritmo y la aritmética.*

**MITRE ATT&CK:** T1110 Brute Force · T1557 Adversary-in-the-Middle (contexto educativo) · T1204 User Execution (no aplica).

**Fuente:** [TryHackMe - StuxCTF](https://tryhackme.com/room/stuxctf)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.