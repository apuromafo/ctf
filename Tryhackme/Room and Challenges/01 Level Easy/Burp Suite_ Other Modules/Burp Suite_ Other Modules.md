# Burp Suite_ Other Modules

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `burpsuiteothermodules` | [TryHackMe](https://tryhackme.com/room/burpsuiteothermodules) | 01 Level Easy | TryHackMe | Burp Suite, Decoder, Comparer, codificación, hash, entropía | Uso de los módulos auxiliares de Burp para decodificar, comparar y analizar datos |

---

**Contexto:** Sala del módulo de Burp Suite que cubre las utilidades auxiliares: el Decoder (codificación, decodificación, hash y entropía) y el Comparer (comparación de respuestas). El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Decoder / Decoder

**Explicación:** Se utiliza el Decoder para identificar y transformar datos: decodificación base64 ("Let's Start Simple"), codificación URL, hash de datos y métricas de entropía.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Smart decode` |
| 3 | *(Pregunta 3 no especificada en el original)* | `TGV0J3MgU3RhcnQgU2ltcGxl`<br>`Next: Decoding`<br>`47`<br>`24034214a720270024142d541357471232250253552c1162d1206c` |
| 4 | *(Pregunta 4 no especificada en el original)* | `6b72350e719a8ef5af560830164b13596cb582757437e21d1879502072238abe`<br>`TcV4QGZZN7y7lwYFRMMoeA==`<br>`key3` |
| 5 | *(Pregunta 5 no especificada en el original)* | `No answer needed` |
| 6 | *(Pregunta 6 no especificada en el original)* | `No answer needed` |

### Task 2: Comparer / Comparer

**Explicación:** Se utiliza el Comparer para examinar respuestas y cifras, seleccionando los términos o resultados correctos en cada comparación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Entropy` |
| 2 | *(Pregunta 2 no especificada en el original)* | `excellent` |
| 3 | *(Pregunta 3 no especificada en el original)* | `No answer needed` |
| 4 | *(Pregunta 4 no especificada en el original)* | `yea` |
| 5 | *(Pregunta 5 no especificada en el original)* | `No answer needed` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Task 1, Pregunta 2 no especificada en el original)* | `Smart decode` |
| 3 | *(Task 1, Pregunta 3 no especificada en el original)* | `TGV0J3MgU3RhcnQgU2ltcGxl`<br>`Next: Decoding`<br>`47`<br>`24034214a720270024142d541357471232250253552c1162d1206c` |
| 4 | *(Task 1, Pregunta 4 no especificada en el original)* | `6b72350e719a8ef5af560830164b13596cb582757437e21d1879502072238abe`<br>`TcV4QGZZN7y7lwYFRMMoeA==`<br>`key3` |
| 5 | *(Task 1, Pregunta 5 no especificada en el original)* | `No answer needed` |
| 6 | *(Task 1, Pregunta 6 no especificada en el original)* | `No answer needed` |
| 7 | *(Task 2, Pregunta 1 no especificada en el original)* | `Entropy` |
| 8 | *(Task 2, Pregunta 2 no especificada en el original)* | `excellent` |
| 9 | *(Task 2, Pregunta 3 no especificada en el original)* | `No answer needed` |
| 10 | *(Task 2, Pregunta 4 no especificada en el original)* | `yea` |
| 11 | *(Task 2, Pregunta 5 no especificada en el original)* | `No answer needed` |

---

**Metodología:** Identificación de los datos con Smart decode → decodificación/decodificación de formato (base64, URL, hash) → análisis de entropía → comparación de respuestas con el Comparer → selección de los valores correctos.

### Cadena de ataque / Attack Chain

```text
Datos de entrada → Smart decode → Decoder (base64/URL/hash/entropía) → Comparer → respuestas
```

**Learning chain:** Burp Suite → Decoder (encode/decode, hash, entropía) → Comparer → análisis de datos

**Lección:** *El Decoder y el Comparer convierten tareas manuales de transformación y comparación de datos en operaciones rápidas dentro del propio flujo de trabajo de Burp.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1140 (Deobfuscate/Decode Files or Information)

**Fuente:** [TryHackMe - Burp Suite_ Other Modules](https://tryhackme.com/room/burpsuiteothermodules)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.