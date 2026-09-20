# Brooklyn Nine Nine

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `brooklynninenine` | [TryHackMe](https://tryhackme.com/room/brooklynninenine) | 01 Level Easy | TryHackMe | OSINT, hashing MD5, investigación web | Resolución de un reto de investigación y generación de hashes |

---

**Contexto:** Sala tipo CTF de dificultad fácil inspirada en la serie Brooklyn Nine-Nine. Consiste en investigar pistas en línea y aplicar hashing para responder a las preguntas finales. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Investigación y hashing / Investigation & Hashing

**Explicación:** Se sigue la investigación propuesta por la sala, se identifican los nombres o términos solicitados y se calcula su hash MD5 para entregar las respuestas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `ee11cbb19052e40b07aac0ca060c23ee`<br>`63a9f0ea7bb98050796b649e85481845` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `ee11cbb19052e40b07aac0ca060c23ee`<br>`63a9f0ea7bb98050796b649e85481845` |

---

**Metodología:** Investigación en línea de las pistas proporcionadas → identificación de los nombres o términos solicitados → cálculo de su hash MD5 → entrega de las respuestas.

### Cadena de ataque / Attack Chain

```text
Pistas → investigación web → identificación de objetivos → hashing MD5 → respuestas
```

**Learning chain:** Investigación OSINT → identificación de nombres → hashing MD5 → respuestas de la sala

**Lección:** *Una investigación bien orientada combinada con utilidades de hashing (md5sum) resuelve retos de enumeración sin necesidad de explotar ningún servicio.*

**MITRE ATT&CK:** T1593 (Search Open Websites/Domains), T1592 (Gather Victim Host Information)

**Fuente:** [TryHackMe - Brooklyn Nine Nine](https://tryhackme.com/room/brooklynninenine)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.