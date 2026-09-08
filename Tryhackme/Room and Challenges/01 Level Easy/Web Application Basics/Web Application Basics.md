# Web Application Basics

| **Dificultad** | Easy |
| **Tipo** | Sala teórica/práctica (web) |
| **Slug** | `webapplicationbasics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/webapplicationbasics) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Web server / web browser / WAF / HTTP (HTTPS) / Query String / Request-Response Model / cabeceras / cookies / CSP-HSTS / CRUD |
| **Impacto** | Sala que cubre los fundamentos de las aplicaciones web: los tres componentes (servidor web, navegador web y firewall de aplicaciones web), HTTPS y la seguridad de un dominio, el modelo petición-respuesta HTTP, cabeceras de petición/respuesta y cookies, cabeceras de seguridad (CSP, HSTS, nosniff) y una práctica final de CRUD contra una API para obtener flags. |

---

**Contexto:** El módulo explica cómo se carga una página web: el navegador solicita los recursos al servidor web y un WAF puede interceptar las peticiones. Para acceso seguro se usa **HTTPS**; el **typosquatting** es un ataque con dominios similares y la **Query String** son los parámetros de la URL. El modelo petición-respuesta va de `HTTP/1.1` con métodos como `OPTIONS`, hasta la **Status Line** con estados como **404** (responses de error del servidor). Entre las cabeceras: `Host`, `application/x-www-form-urlencoded` como Content-Type de formularios, o atributos de cookie `Secure` y `HttpOnly`; y de seguridad: `script-src` (CSP), `includeSubDomains` (HSTS) y `nosniff` (X-Content-Type-Options). La práctica final hace un CRUD contra el lab (listar, modificar y eliminar usuarios), entregando tres flags.

## Solucionario

### Task 1: Introducción

**Explicación:** Presentación de la sala y de los objetivos de aprendizaje (HTTP, modelo de petición/respuesta, cabeceras, cookies y seguridad).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: Componentes de una aplicación web

**Explicación:** Los tres componentes que intervienen en la carga de una página web: el **web server** (sirve el contenido), el **web browser** (cliente que lo solicita) y el **web application firewall** (filtra el tráfico).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Nombra el componente que sirve los archivos de la web. | `web server` |
| 2 | Nombra el componente que solicita y muestra la web. | `web browser` |
| 3 | Nombra el componente de seguridad que filtra el tráfico web. | `web application firewall` |

### Task 3: Cómo cargamos las páginas web

**Explicación:** Para acceso seguro se usa el protocolo **HTTPS**. El **typosquatting** engaña usando dominios similares y la **Query String** puede especificar parámetros en la URL.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué protocolo se usa para acceder de forma segura a una web? | `HTTPS` |
| 2 | ¿Cómo se llama la técnica de usar un dominio parecido al legítimo? | `Typosquatting` |
| 3 | ¿Qué parte de la URL contiene los parámetros de la petición? | `Query String` |

### Task 4: El modelo petición-respuesta

**Explicación:** El navegador envía una petición HTTP y recibe una **HTTP response**. Las cabeceras y el cuerpo se separan por una **línea vacía**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué elemento devuelve el servidor al recibir una petición HTTP? | `HTTP response` |
| 2 | ¿Qué separa las cabeceras del cuerpo de la petición/respuesta? | `Empty Line` |

### Task 5: Métodos HTTP

**Explicación:** Las peticiones comienzan con la versión del protocolo (`HTTP/1.1`), el método HTTP (como `OPTIONS`, para consultar capacidades del servidor) y la ruta al recurso (`URL Path`).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué versión de HTTP se usa en la línea de inicio de la petición? | `HTTP/1.1` |
| 2 | ¿Qué método HTTP permite consultar qué opciones soporta un servidor? | `OPTIONS` |
| 3 | ¿Qué parte de la petición indica la ruta al recurso solicitado? | `URL Path` |

### Task 6: Cabeceras de petición

**Explicación:** Las cabeceras de petición (`Request Headers`) aportan contexto al servidor: `Host` indica el dominio, y un formulario envía sus datos con el tipo de contenido `application/x-www-form-urlencoded`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cabecera de petición indica el dominio al que se envía la petición? | `Host` |
| 2 | ¿Qué valor de Content-Type se usa cuando un formulario envía los datos en la petición? | `application/x-www-form-urlencoded` |
| 3 | ¿Cómo se llaman las cabeceras que el navegador envía en la petición? | `Request Headers` |

### Task 7: Códigos de estado

**Explicación:** La respuesta HTTP empieza con una **Status Line** que indica el resultado. Si el recurso no se encuentra el estado es **404**, y los errores internos del servidor se documentan en la sección de **Server Error Responses** (5xx).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama la primera línea de la respuesta HTTP? | `Status Line` |
| 2 | ¿En qué sección se documentan los errores internos del servidor (5xx)? | `Server Error Responses` |
| 3 | ¿Qué código de estado se devuelve cuando el recurso solicitado no existe? | `404` |

### Task 8: Cookies

**Explicación:** Las cookies se establecen con cabeceras de respuesta del servidor (`Server`) y llevan atributos de seguridad: `Secure` (solo por HTTPS) y `HttpOnly` (inaccesibles desde JavaScript).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cabecera de respuesta indica el software del servidor que atendió la petición? | `Server` |
| 2 | ¿Qué atributo de la cookie impide que se envíe por HTTP (solo HTTPS)? | `Secure` |
| 3 | ¿Qué atributo de la cookie impide el acceso desde JavaScript? | `HttpOnly` |

### Task 9: Cabeceras de seguridad

**Explicación:** Las cabeceras de seguridad protegen el contenido: la directiva CSP `script-src` define de dónde pueden venir los scripts, HSTS con `includeSubDomains` fuerza HTTPS también en subdominios y `nosniff` (X-Content-Type-Options) evita que el navegador adivine el tipo de contenido.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué directiva de Content-Security-Policy controla las fuentes válidas de scripts? | `script-src` |
| 2 | ¿Qué atributo de Strict-Transport-Security aplica HTTPS a los subdominios? | `includeSubDomains` |
| 3 | ¿Qué directiva de la cabecera X-Content-Type-Options impide el MIME sniffing? | `nosniff` |

### Task 10: Práctica: CRUD sobre el lab

**Explicación:** Última parte práctica: interactuar con la aplicación web haciendo operaciones CRUD. Listar el listado de usuarios, modificar los datos de un usuario y eliminar un usuario entregan tres flags distintas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Encuentra la flag tras listar el listado de usuarios. | `THM{YOU_HAVE_JUST_FOUND_THE_USER_LIST}` |
| 2 | Modifica los datos de un usuario y encuentra la flag. | `THM{YOU_HAVE_MODIFIED_THE_USER_DATA}` |
| 3 | Elimina un usuario y encuentra la flag. | `THM{YOU_HAVE_JUST_DELETED_A_USER}` |

### Task 11: Conclusión

**Explicación:** Resumen de los fundamentos aprendidos: componentes, HTTP, cabeceras, cookies y seguridad.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. | `No answer needed` |

---

**Metodología:** Repaso de componentes web → lectura del modelo petición-respuesta → análisis de métodos, cabeceras y estados HTTP → revisión de cookies y cabeceras de seguridad → prácticas CRUD con la API del lab.
**Learning chain:** cómo se carga una web → HTTPS/typosquatting/Query String → petición-respuesta HTTP → métodos y cabeceras → estados → cookies → políticas de seguridad → CRUD práctico (flags).
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1598 (Phishing for Information - Typosquatting), T1071.001 (Application Layer Protocol: Web), T1110 (Brute Force - defensa)
**Fuente:** [TryHackMe - Web Application Basics](https://tryhackme.com/room/webapplicationbasics)