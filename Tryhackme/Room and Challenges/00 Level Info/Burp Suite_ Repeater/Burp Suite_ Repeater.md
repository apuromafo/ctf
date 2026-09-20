# Burp Suite_ Repeater

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Info | walkthrough | `burpsuiterepeater` | [TryHackMe](https://tryhackme.com/room/burpsuiterepeater) | 00 Level Info | TryHackMe | Burp Suite, Repeater, HTTP, Inspector, payloads, renderizado | Manipulación y reenvío de peticiones HTTP con Burp Suite Repeater para pruebas manuales de seguridad web |

---

**Contexto:** Sala dedicada a Burp Suite Repeater, la herramienta de Burp Suite que permite capturar, modificar y reenviar peticiones HTTP de forma repetida para probar manualmente la seguridad de una aplicación web. Se recorren la interfaz, las opciones, los payloads y un par de ejercicios prácticos con flags. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: ¿Qué es Repeater? / What is Repeater?

**Explicación:** Pregunta de arranque de la sala sobre la utilidad de Repeater, sin respuesta que introducir. Respuesta original: `No answer needed`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

### Task 2: La interfaz de Repeater / The Repeater Interface

**Explicación:** Se estudia la interfaz de Repeater y sus paneles; la respuesta destaca la sección `Inspector`, que permite inspeccionar y modificar peticiones y respuestas de forma estructurada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Inspector` |

### Task 3: La petición / The Request

**Explicación:** Se trabaja sobre el panel de la petición HTTP original que se envía al servidor. La respuesta es `Request`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Request` |

### Task 4: La respuesta / The Response

**Explicación:** Se examina el panel de la respuesta del servidor; una de sus capacidades se activa de forma opcional y permite previsualizar el contenido. La respuesta es `Render`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Render` |

### Task 5: Opciones de Repeater / Repeater Options

**Explicación:** Se repasan las opciones adicionales de Repeater relacionadas con el manejo de la petición, como la codificación o el tratamiento de parámetros del cuerpo. La respuesta es `Body Parameters`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `Body Parameters` |

### Task 6: Ejemplo práctico / Practical Example

**Explicación:** Ejercicio práctico guiado con Repeater sobre una petición HTTP: se reproduce la petición y se obtiene la flag `THM{Yzg2MWI2ZDhlYzdlNGFiZTUzZTIzMzVi}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{Yzg2MWI2ZDhlYzdlNGFiZTUzZTIzMzVi}` |

### Task 7: Payloads / Payloads

**Explicación:** Se introduce el uso de payloads en Repeater para automatizar variaciones de la petición. Incluye un ejercicio final que se resuelve sin respuesta y otro que entrega la flag `THM{N2MzMzFhMTA1MmZiYjA2YWQ4M2ZmMzhl}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `THM{N2MzMzFhMTA1MmZiYjA2YWQ4M2ZmMzhl}` |

### Task 8: Conclusión / Conclusion

**Explicación:** Cierre del recorrido sobre Repeater, que se confirma con la flag `THM{ZGE3OTUyZGMyMzkwNjJmZjg3Mzk1NjJh}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `THM{ZGE3OTUyZGMyMzkwNjJmZjg3Mzk1NjJh}` |

### Task 9: Aprende y gana / Learn and Win

**Explicación:** Tarea final de la sala, sin respuesta que introducir. Respuesta original: `No answer needed`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Task 2, Pregunta 1 no especificada en el original)* | `Inspector` |
| 3 | *(Task 3, Pregunta 1 no especificada en el original)* | `Request` |
| 4 | *(Task 4, Pregunta 1 no especificada en el original)* | `Render` |
| 5 | *(Task 5, Pregunta 1 no especificada en el original)* | `Body Parameters` |
| 6 | *(Task 6, Pregunta 1 no especificada en el original)* | `THM{Yzg2MWI2ZDhlYzdlNGFiZTUzZTIzMzVi}` |
| 7 | *(Task 7, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 8 | *(Task 7, Pregunta 2 no especificada en el original)* | `THM{N2MzMzFhMTA1MmZiYjA2YWQ4M2ZmMzhl}` |
| 9 | *(Task 8, Pregunta 1 no especificada en el original)* | `THM{ZGE3OTUyZGMyMzkwNjJmZjg3Mzk1NjJh}` |
| 10 | *(Task 9, Pregunta 1 no especificada en el original)* | `No answer needed` |

---

**Metodología:** Familiarizarse con la interfaz de Repeater (Inspector) → comprender la gestión de la petición y de la respuesta (render) → configurar las opciones (body parameters) → reproducir una petición real y leer su flag → automatizar variaciones con payloads → concluir con la flag final.

### Cadena de ataque / Attack Chain

```text
Repeater → Inspector → Request → Response (Render) → Options (Body Parameters) → petición práctica → flag THM{...} → payloads → flag THM{...} → conclusión → flag THM{...}
```

**Learning chain:** Qué es Repeater → interfaz (Inspector) → petición y respuesta → opciones → ejemplo práctico → payloads → conclusión y flags

**Lección:** *Repeater convierte la petición HTTP en un elemento manipulable e iterable: la repetición controlada de una petición permite validar la lógica del servidor sin tocar el navegador.*

**MITRE ATT&CK:** T1595 (Active Scanning), T1189 (Drive-by Compromise - testing), T1190 (Exploit Public-Facing Application)

**Fuente:** [TryHackMe - Burp Suite_ Repeater](https://tryhackme.com/room/burpsuiterepeater)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.