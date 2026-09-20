# Insecure Randomness

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `insecurerandomness` | [TryHackMe](https://tryhackme.com/room/insecurerandomness) | 01 Level Easy | THM | Insecure randomness, PHP sessions, time(), mt_srand, token prediction | Predicción de tokens de sesión y firma como otros usuarios por aleatoriedad débil |

> **Objeto:** Descubrir cómo la aleatoriedad insegura (time(), mt_srand) permite predecir tokens de sesión y firmarse como víctima o administrador en PHP.

---

**Contexto:** Sala de TryHackMe sobre aleatoriedad insegura. Explica por qué la generación de valores aleatorios en PHP puede no ser segura si se usa poca entropía o semillas predecibles, y cómo la función `time()` como semilla permite predicción de tokens. En la práctica se predicen los tokens de sesión para firmarse como usuario víctima, administrador, mago y recursos humanos, obteniendo banderas de cada rol.

> **ES:** Una sala práctica sobre generadores débiles de aleatoriedad en PHP: cómo `time()` y `mt_srand` producen tokens predecibles y cómo explotarlos para autenticarse como otros usuarios.
> **EN:** A hands-on room about weak randomness generators in PHP: how `time()` and `mt_srand` produce predictable tokens and how to exploit them to log in as other users.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Primera aproximación al problema de la aleatoriedad insegura en aplicaciones web.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Hay algo que responder en este apartado? / Is there anything to answer here? | `No answer needed` |

### Task 2: Aleatoriedad en PHP / Randomness in PHP

**Explicación:** Se analiza de dónde procede la aleatoriedad en PHP, la cantidad de entropía implicada y si la función de generación es segura según el material de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2.1 | ¿Qué concepto está relacionado con la generación aleatoria? / Which concept is related to random generation? | `entropy` |
| 2.2 | ¿Es seguro el generador por defecto? / Is the default generator secure? | `nay` |
| 3 | Seleccione la respuesta correcta (opción b) / Select the correct answer (option b) | `b` |

### Task 3: Explotación - Tokens con time() / Exploitation - time() Based Tokens

**Explicación:** Los tokens de sesión se generan usando `time()` como semilla, lo que permite predecirlos calculando la marca temporal. Con ello se firma como usuario víctima y como administrador, obteniendo banderas y confirmando el uso de `time()`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4.1 | Bandera al firmarse como la víctima / Flag when signing in as the victim | `THM{VICTIM_SIGNED_IN}` |
| 4.2 | Bandera al firmarse como administrador / Flag when signing in as admin | `THM{ADMIN_SIGNED_IN007}` |
| 4.3 | ¿Qué función actúa como semilla? / Which function is used as the seed? | `time()` |

### Task 5: Explotación - mt_rand / Exploitation - mt_srand

**Explicación:** El generador se cambia a Mersenne Twister (`mt_rand`) con `mt_srand` como semilla, pero la semilla sigue siendo predecible, permitiendo seguir firmándose como otros roles (magic y HR) y obteniendo sus banderas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 5.1 | Bandera al firmarse como magic / Flag when signing in as magic | `THM{MAGIC_SIGNED_IN11010}` |
| 5.2 | Bandera al firmarse como HR / Flag when signing in as HR | `THM{HR_SIGNED_IN1337}` |
| 5.3 | ¿Qué función se usa como semilla del generador? / Which function seeds the generator? | `mt_srand` |

### Task 6: Conclusión / Conclusion

**Explicación:** Preguntas finales de validación y cierre de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | Seleccione la respuesta correcta (opción d) / Select the correct answer (option d) | `d` |
| 7 | ¿Hay algo que responder al final? / Is there anything to answer at the end? | `No answer needed` |

---

**Metodología:** Se analizó cómo PHP genera los tokens de sesión y se confirmó que la semilla era la marca temporal `time()`, por lo que el token podía replicarse calculando la ventana temporal. Se reutilizó ese token predicho para firmarse como víctima y administrador. Cuando el generador pasó a Mersenne Twister, se identificó `mt_srand` como la semilla y se repitió la predicción para firmarse como magic y HR, obteniendo cada bandera.

### Cadena de ataque / Attack Chain

Análisis del generador de tokens → detección de baja entropía → identificación de `time()` como semilla → predicción del token de sesión → firma como víctima/administrador → cambio a `mt_rand`/`mt_srand` → repetición de la predicción → firma como magic/HR.

**Learning chain:** Insecure randomness → entropy débil → semilla `time()` → predicción de tokens → firma como otros roles → `mt_rand` / `mt_srand` → segunda predicción → banderas.

**Lección:** *La seguridad de un token de sesión depende de la entropía real del generador: semillas predecibles (time()) o PRNG débiles (mt_srand) convierten la autenticación en una función de la marca temporal, permitiendo a un atacante predecir e impersonar cualquier sesión.*

**MITRE ATT&CK:** T1110 (Brute Force), T1078 (Valid Accounts), T1213 (Data from Information Repositories), T1557 (Adversary-in-the-Middle).

**Fuente:** [TryHackMe - Insecure Randomness](https://tryhackme.com/room/insecurerandomness)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.