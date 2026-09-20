# Avengers Blog

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `avengersblog` |
| **Link** | [TryHackMe](https://tryhackme.com/room/avengersblog) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | XSS, cookies, cabeceras HTTP, inspección web, secretos, exfiltración |
| **Impacto** | Explotación de un blog WordPress mediante comentarios inyectados, cifrado/descifrado de cookies con secretos descubiertos y acceso a rutas y servicios ocultos que conducen a la flag final. |

---

**Contexto:** La sala es un ejercicio práctico sobre el blog de los Vengadores. Se inyectan comentarios que se ejecutan en el navegador del administrador, se descubren los secretos usados para cifrar las cookies (`cookie_secrets`), se identifican cabeceras que no deberían ser accesibles (`headers_are_important`), se inspecciona la página para encontrar valores ocultos y rutas internas como `/portal`, y se accede al servicio final (puerto 223) para recuperar la flag que cierra la cadena.

## Solucionario

### Task 1: Inyección de comentarios / Comment Injection

**Explicación:** Se publican comentarios en el blog que permiten inyectar contenido/código que se carga al revisar la página. La primera flag está en un comentario oculto o en el código de la propia página.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Dejar un comentario e inspeccionar la respuesta de la página. | `No answer needed` |
| 2 | Observar el comentario oculto dentro de la página. | `No answer needed` |

### Task 2: Secreto de las cookies / Cookie Secrets

**Explicación:** Se descubre el secreto utilizado por el blog para cifrar la cookie de sesión del administrador, que se llamará a partir de ahora `cookie_secrets`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el secreto utilizado para cifrar las cookies? | `cookie_secrets` |

### Task 3: Cabeceras importantes / Important Headers

**Explicación:** Se analizan las cabeceras de la aplicación y se identifica un valor oculto que no debería ser evidente, recordando que las cabeceras también son importantes: `headers_are_important`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué valor oculto se encuentra en las cabeceras de la página? | `headers_are_important` |

### Task 4: Inspección de la página / Page Inspection

**Explicación:** Se inspecciona la página (código fuente y respuesta del blog) para localizar el valor oculto que permite continuar con la cadena de ataque.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué valor oculto se encuentra inspeccionando la página? | `8fc651a739befc58d450dc48e1f1fd2e` |

### Task 5: Ruta interna / Internal Route

**Explicación:** Se sigue el rastro de los valores descubiertos hasta una ruta interna de la aplicación, accesible desde el blog.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué ruta interna se descubre/revela? | `/portal` |

### Task 6: Servicio expuesto / Exposed Service

**Explicación:** La ruta interna conduce a un servicio expuesto en un puerto no estándar. Se identifica el puerto en el que responde el servicio objetivo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿En qué puerto responde el servicio objetivo? | `223` |

### Task 7: Flag final / Final Flag

**Explicación:** Accediendo al servicio del puerto 223 con las credenciales/valores descubiertos a lo largo de la cadena se obtiene la flag final de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag final de la sala? | `d335e2d13f36558ba1e67969a1718af7` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Dejar un comentario e inspeccionar la respuesta de la página. | `No answer needed` |
| 2 | Observar el comentario oculto dentro de la página. | `No answer needed` |
| 3 | ¿Cuál es el secreto utilizado para cifrar las cookies? | `cookie_secrets` |
| 4 | ¿Qué valor oculto se encuentra en las cabeceras de la página? | `headers_are_important` |
| 5 | ¿Qué valor oculto se encuentra inspeccionando la página? | `8fc651a739befc58d450dc48e1f1fd2e` |
| 6 | ¿Qué ruta interna se descubre/revela? | `/portal` |
| 7 | ¿En qué puerto responde el servicio objetivo? | `223` |
| 8 | ¿Cuál es la flag final de la sala? | `d335e2d13f36558ba1e67969a1718af7` |

---

**Metodología:**

1. Se inyectan comentarios en el blog y se inspeccionan las respuestas y el código de la página.
2. Se descubre el secreto de cifrado de cookies `cookie_secrets`.
3. Se analizan las cabeceras de la aplicación y se localiza `headers_are_important`.
4. Se inspecciona la página para recuperar el valor oculto `8fc651a739befc58d450dc48e1f1fd2e`.
5. Se sigue el rastro hasta la ruta interna `/portal` y después hasta el servicio del puerto **223**.
6. Se accede al servicio final y se obtiene la flag `d335e2d13f36558ba1e67969a1718af7`.

### Cadena de ataque / Attack Chain

```
Comentarios en el blog (inyección XSS) -> secreto cookie_secrets
  -> Cabeceras -> headers_are_important
  -> Inspección de página -> 8fc651a739befc58d450dc48e1f1fd2e
  -> Ruta interna /portal
  -> Servicio expuesto -> puerto 223
  -> Flag final d335e2d13f36558ba1e67969a1718af7
```

**Learning chain:** Inyección de comentarios → Secreto de cookies → Cabeceras → Inspección web → Ruta interna → Servicio expuesto → Flag final

**Lección:** *Los secretos escondidos en comentarios, cabeceras y cookies de una aplicación web encadenan el acceso a rutas y servicios internos; la validación de entradas y la ausencia de secretos en el lado cliente son esenciales.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1189 (Drive-by Compromise), T1110 (Brute Force), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Avengers Blog](https://tryhackme.com/room/avengersblog)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.