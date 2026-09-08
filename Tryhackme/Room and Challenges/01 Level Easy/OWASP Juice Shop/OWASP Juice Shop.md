# OWASP Juice Shop

| **Dificultad** | Easy |
| **Tipo** | Práctica guiada sobre OWASP Juice Shop (la tienda online deliberadamente vulnerable) |
| **Slug** | `owaspjuiceshop` |
| **Link** | [TryHackMe](https://tryhackme.com/room/owaspjuiceshop) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Juice Shop (OWASP), inyección SQL en el login, fuerza bruta de login, restablecimiento de contraseña (pregunta de seguridad), archivos confidenciales y backup, módulo de búsqueda (`q`), panel de administración, carrito (basket) por ID, eliminación de reseñas, XSS (DOM, persistente y reflejado), Score Board y hash SHA-1 de las recompensas |
| **Impacto** | Sala de práctica sobre la aplicación Juice Shop de OWASP: el usuario debe completar una serie de retos (login con inyección SQL, fuerza bruta, acceso a datos confidenciales, panel de administración, modificación de carritos, XSS, score board) y, en esta versión, reportar el hash SHA-1 de la descripción de la recompensa de cada hack completado. Cubre de forma práctica los OWASP Top 10 aplicados a una tienda web real. |

---

**Contexto:** La sala despliega la aplicación **Juice Shop** (proyecto de OWASP), una tienda online con muchísimas vulnerabilidades intencionadas. La versión de la sala exige completar los retos de cada bloque de tareas y devolver el **hash SHA-1 de la descripción de la recompensa** de cada hack (a diferencia de versiones antiguas donde se devolvía el texto de la recompensa). Las tareas avanzan del reconocimiento inicial (email del admin, parámetro de búsqueda `q`) a ataques de inyección SQL en el login, fuerza bruta de la cuenta `admin`, restablecimiento de la contraseña de un usuario, exfiltración de documentos y backup, acceso al panel de administración y a un carrito ajeno, borrado masivo de reseñas, tres tipos de XSS y, finalmente, el descubrimiento del Score Board oculto de la aplicación.

## Solucionario

### Task 1: Open for business!

**Explicación:** Despliegue de la máquina y arranque de la tienda Juice Shop. Aún no hay retos que responder.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Arranca la máquina y abre la aplicación Juice Shop. | `No answer needed` |
| 2 | Verifica que la tienda carga correctamente y comienza el reto. | `No answer needed` |

### Task 2: Let's go on an adventure!

**Explicación:** Reconocimiento inicial: se inspecciona la tienda y sus peticiones. El email del administrador aparece en la información/carga de la aplicación (`admin@juice-sh.op`), el buscador usa el parámetro `q` para filtrar productos y en los datos de la tienda se hace referencia a la serie/franquicia **Star Trek**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la dirección de correo del administrador de Juice Shop? | `admin@juice-sh.op` |
| 2 | ¿Qué parámetro usa el buscador interno de la tienda? | `q` |
| 3 | ¿Qué película/serie se menciona en el contenido de la tienda? | `Star Trek` |

### Task 3: Inject the juice (SQLi)

**Explicación:** En el formulario de login se prueba la clásica inyección SQL que evita la comprobación de contraseña. Con `admin' or 1=1--` (o `' OR 1=1--` en el usuario de administración) el backend responde con la recompensa del reto; el mismo método permite entrar con la cuenta del usuario `bender`. En esta versión de la sala las respuestas son los hashes SHA-1 de las descripciones de esas recompensas.

```sql
email       : admin' or 1=1--
password    : (cualquiera)

# login como bender mediante SQLi
email       : bender' or 1=1--
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Resuelve el reto de inyección SQL en el login. ¿Cuál es el hash SHA-1 de la recompensa? | `690fa3247a99d651e0b26f947baf0b79b4f404a9` |
| 2 | Inicia sesión como el usuario `bender` mediante SQLi. ¿Cuál es el hash SHA-1 de la recompensa? | `5ff5052e879e6fef64124e64c82c84ebc809c6c4` |

### Task 4: Who broke my lock?!

**Explicación:** Atques contra la autenticación: con un proxy/interceptor se fuerza bruta el login del usuario `admin` lanzando muchas peticiones con contraseñas del diccionario hasta obtener `HTTP 200` (retos de tipo "Brute Force Login"); y se abusa del flujo de restablecimiento de contraseña de otro usuario (pregunta de seguridad predecible) para tomar el control de su cuenta. Las respuestas son los SHA-1 de las recompensas correspondientes.

```bash
# fuerza bruta: admin -> diccionario hasta HTTP 200
# reset de contraseña: responder la pregunta de seguridad de la víctima y cambiarla
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Consigue entrar en la cuenta de administrador por fuerza bruta (HTTP 200). ¿Cuál es el hash SHA-1 de la recompensa? | `ff4aebffe31b0ffdea9bdd0207a16a3c01ac6c56` |
| 2 | Restablece la contraseña de un usuario mediante el flujo de recuperación vulnerable. ¿Cuál es el hash SHA-1 de la recompensa? | `3c3e2d6ef99b733b947e92f8e2a9ed08bf57ea63` |

### Task 5: AH, don't look!

**Explicación:** Se explora la tienda en busca de datos sensibles mal protegidos: un documento confidencial de la aplicación (archivo de la guía de acceso), la pista cifrada/oculta del personaje "MC SafeSearch" y la copia de seguridad (backup) expuesta, descargable desde el servidor. Cada hallazgo recompensa un hash SHA-1.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Accede al documento confidencial de la aplicación. ¿Cuál es el hash SHA-1 de la recompensa? | `8d2072c6b0a455608ca1a293dc0c9579883fc6a5` |
| 2 | Averigua qué se esconde tras el mensaje de "MC SafeSearch". ¿Cuál es el hash SHA-1 de la recompensa? | `bb105418e73708ceccf1a7b2491f434b8f5230e4` |
| 3 | Descarga el archivo de copia de seguridad expuesto. ¿Cuál es el hash SHA-1 de la recompensa? | `cfdeea14e8f01b4952722fd0e4a77f1928593c9a` |

### Task 6: Who's flying this thing?

**Explicación:** Abuso de control de acceso y lógica: se localiza y abre el panel de administración (página que solo debería ver el equipo de Juice Shop), se accede al carrito de otro usuario manipulando el ID del basket (el backend no valida la propiedad del carrito) y se destruyen todas las reseñas de 5 estrellas de la tienda mediante peticiones a la API. Cada acción devuelve su recompensa (hash SHA-1).

```http
GET /administration               # panel de administración
GET /rest/basket/{id|7}           # carrito de otro usuario
DELETE /rest/products/{id}/reviews  # borrado de reseñas
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Accede al panel de administración oculto. ¿Cuál es el hash SHA-1 de la recompensa? | `71aeb3b0bf01cc6e488f0207bb62f79b41454a87` |
| 2 | Accede al carrito de otro usuario. ¿Cuál es el hash SHA-1 de la recompensa? | `e6982b34b6734ceadd28e5019b251f929a80b815` |
| 3 | Elimina todas las reseñas de 5 estrellas. ¿Cuál es el hash SHA-1 de la recompensa? | `78231b75c0b2180b7e964dcbb1ab3c3f58639f2e` |

### Task 7: Where did that come from?

**Explicación:** Tres retos de XSS: un XSS basado en DOM (el payload se ejecuta manipulando el DOM de la página, sin viajar al servidor), un XSS persistente (la inyección queda almacenada, p. ej., en una reseña de producto que se ejecuta en la sesión de otros usuarios) y un XSS reflejado (la entrada maliciosa viaja al servidor y vuelve reflejada, p. ej., en el banner de la tienda). Cada recompensa se reporta como SHA-1.

```html
<!-- XSS en el nombre de la reseña para persistencia -->
<iframe src="javascript:alert(`xss`)">
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejecuta un XSS basado en DOM en la aplicación. ¿Cuál es el hash SHA-1 de la recompensa? | `4a31a4fe0954199566e360a873802bf64d0d0a84` |
| 2 | Publica un XSS persistente (almacenado). ¿Cuál es el hash SHA-1 de la recompensa? | `c37da14686b69a220fd9febd09bb9593e7d0539f` |
| 3 | Ejecuta un XSS reflejado. ¿Cuál es el hash SHA-1 de la recompensa? | `305021787d3e9cd9cebc057a021c2504550bb3b6` |

### Task 8: Exploration!

**Explicación:** Reto de descubrimiento: existe un "Score Board" de desarrollo oculto de Juice Shop, accesible en una ruta no publicada (`/#/score-board` o mediante la manipulación de cabeceras de desarrollo). Encontrarlo completa el reto de exploración y otorga su recompensa.

```text
/#/score-board   # ruta oculta del Score Board de desarrollo
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Accede al Score Board oculto de Juice Shop. ¿Cuál es el hash SHA-1 de la recompensa? | `2614339936e8282e2f820f023d4d998a1f95e02a` |

---

**Metodología:** Enfoque de reconocimiento primero (admin@juice-sh.op, parámetro `q`) y después explotación progresiva de la tienda: (1) inyección SQL en el login (admin y bender); (2) fuerza bruta de la cuenta admin y reset de contraseñas por pregunta de seguridad; (3) exfiltración de archivos sensibles y backup; (4) control de acceso: panel de administración, IDOR del basket y borrado de reseñas vía API; (5) tres variantes de XSS (DOM, persistente, reflejado); (6) descubrimiento del Score Board. Cada reto se completa y su recompensa se reporta como SHA-1. Todo se verifica contra la API de Juice Shop (`/rest/products`, `/rest/basket`, `/administration`) con el proxy/interceptor o curl.
**Learning chain:** recon básico → SQLi → fuerza bruta / reset de contraseña → datos expuestos → control de acceso y API tampering → XSS (DOM/almacenado/reflejado) → Score Board.
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1213.003 (Data from Information Repositories: Code Repositories), T1005 (Data from Local System), T1110.003 (Password Spraying), T1606.001 (Web Session Cookie), T1189 (Drive-by Compromise)/XSS T1059.007 (JavaScript), T1505.003 (Web Shell no aplica) → retos prácticos de los OWASP Top 10 en una tienda web.
**Fuente:** [TryHackMe - OWASP Juice Shop](https://tryhackme.com/room/owaspjuiceshop)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
