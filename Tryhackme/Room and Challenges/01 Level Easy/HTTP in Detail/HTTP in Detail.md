# HTTP in Detail

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `httpindetail` | https://tryhackme.com/room/httpindetail | 01 Level Easy | TryHackMe | HTTP/HTTPS / peticiones y respuestas / métodos HTTP / códigos de estado / cabeceras / cookies | Comprender el protocolo HTTP en profundidad para trabajar con cualquier aplicación web. |

---

**Contexto:** Sala de fundamentos de redes que explica HTTP en detalle: qué es el protocolo y HTTPS, la estructura de peticiones y respuestas, los métodos HTTP, los códigos de estado, las cabeceras principales y el uso de cookies, cerrando con práctica de peticiones reales para obtener varias flags.

> **ES:** Estudia las peticiones y respuestas HTTP, sus métodos, códigos y cabeceras, y practica interactuando con el servidor para obtener las flags.
> **EN:** Study HTTP requests and responses, methods, status codes and headers, and practise interacting with the server to get the flags.

## Solucionario

### Task 1: Qué es HTTP / What is HTTP

**Explicación:** HTTP es el protocolo de transferencia de hipertexto que usan los navegadores; la S de HTTPS indica que la conexión es segura (cifrada). Al examinar la respuesta HTTP del ejercicio aparece la flag del certificado inválido.

1. 1. HyperText Transfer Protocol
   2. secure
   3. THM{INVALID_HTTP_CERT}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa HTTP? / What does HTTP stand for? | `HyperText Transfer Protocol` |
| 2 | ¿Qué significa la S en HTTPS? / What does the S in HTTPS stand for? | `secure` |
| 3 | ¿Cuál es la flag de la respuesta HTTP? / What is the flag from the HTTP response? | `THM{INVALID_HTTP_CERT}` |

### Task 2: Peticiones y respuestas / Requests and Responses

**Explicación:** Las peticiones envían cabeceras que identifican la versión del protocolo y el tamaño del contenido; la cabecera de la respuesta indica la longitud del cuerpo o contenido devuelto.

1. 1. HTTP/1.1
   2. Content-Length

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cabecera indica al servidor la versión de HTTP que usa el cliente? / What header tells the server the HTTP version the client is using? | `HTTP/1.1` |
| 2 | ¿Qué cabecera de la respuesta indica la longitud del contenido? / What header gives the length of the response content? | `Content-Length` |

### Task 3: Métodos HTTP / HTTP Methods

**Explicación:** Los métodos HTTP definen la acción a realizar sobre un recurso: crear, actualizar, eliminar o recuperar.

1. 1. POST
   2. PUT
   3. DELETE
   4. GET

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué método se usa para crear un recurso nuevo? / What method is used to create a new resource? | `POST` |
| 2 | ¿Qué método se usa para actualizar un recurso? / What method is used to update a resource? | `PUT` |
| 3 | ¿Qué método se usa para eliminar un recurso? / What method is used to delete a resource? | `DELETE` |
| 4 | ¿Qué método se usa para recuperar un recurso? / What method is used to retrieve a resource? | `GET` |

### Task 4: Códigos de estado / HTTP Status Codes

**Explicación:** Los códigos de estado comunican el resultado de la petición: `201` creado, `404` no encontrado, `503` servicio no disponible y `401` no autorizado.

1. 1. 201
   2. 404
   3. 503
   4. 401

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué código indica que el recurso se ha creado? / What code indicates a resource was created? | `201` |
| 2 | ¿Qué código indica que el recurso no existe? / What code indicates the resource was not found? | `404` |
| 3 | ¿Qué código indica servicio no disponible? / What code indicates service unavailable? | `503` |
| 4 | ¿Qué código indica no autorizado? / What code indicates unauthorised? | `401` |

### Task 5: Cabeceras / Headers

**Explicación:** Las cabeceras aportan información sobre el cliente, el tipo de datos y el sitio solicitado.

1. 1. User-Agent
   2. Content-Type
   3. Host

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cabecera identifica al cliente y al sistema operativo? / What header identifies the client and OS? | `User-Agent` |
| 2 | ¿Qué cabecera indica el tipo de datos que se envían? / What header tells the web server what type of data is being sent? | `Content-Type` |
| 3 | ¿Qué cabecera indica qué sitio web se está solicitando? / What header specifies which site is being requested? | `Host` |

### Task 6: Cookies

**Explicación:** Las cookies mantienen el estado entre peticiones y se establecen mediante una cabecera de respuesta.

1. 1. Set-Cookie

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cabecera se usa para establecer una cookie? / What header is used to set a cookie? | `Set-Cookie` |

### Task 7: Haciendo peticiones / Making Requests

**Explicación:** Con las herramientas de la sala (Terminal / AttackBox) se realizan peticiones reales al servidor web; cada interacción correcta devuelve una flag distinta.

1. 1. THM{YOU'RE_IN_THE_ROOM}
   2. THM{YOU_FOUND_THE_BLOG}
   3. THM{USER_IS_DELETED}
   4. THM{USER_HAS_UPDATED}
   5. THM{HTTP_REQUEST_MASTER}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Flag de la primera petición. | `THM{YOU'RE_IN_THE_ROOM}` |
| 2 | Flag de la segunda petición. | `THM{YOU_FOUND_THE_BLOG}` |
| 3 | Flag de la tercera petición. | `THM{USER_IS_DELETED}` |
| 4 | Flag de la cuarta petición. | `THM{USER_HAS_UPDATED}` |
| 5 | Flag de la quinta petición. | `THM{HTTP_REQUEST_MASTER}` |

---

| Task | # | Pregunta | Respuesta |
|------|---|----------|-----------|
| 1 | 1 | ¿Qué significa HTTP? / What does HTTP stand for? | `HyperText Transfer Protocol` |
| 1 | 2 | ¿Qué significa la S en HTTPS? / What does the S in HTTPS stand for? | `secure` |
| 1 | 3 | ¿Cuál es la flag de la respuesta HTTP? / What is the flag from the HTTP response? | `THM{INVALID_HTTP_CERT}` |
| 2 | 1 | ¿Qué cabecera indica al servidor la versión de HTTP que usa el cliente? / What header tells the server the HTTP version the client is using? | `HTTP/1.1` |
| 2 | 2 | ¿Qué cabecera de la respuesta indica la longitud del contenido? / What header gives the length of the response content? | `Content-Length` |
| 3 | 1 | ¿Qué método se usa para crear un recurso nuevo? / What method is used to create a new resource? | `POST` |
| 3 | 2 | ¿Qué método se usa para actualizar un recurso? / What method is used to update a resource? | `PUT` |
| 3 | 3 | ¿Qué método se usa para eliminar un recurso? / What method is used to delete a resource? | `DELETE` |
| 3 | 4 | ¿Qué método se usa para recuperar un recurso? / What method is used to retrieve a resource? | `GET` |
| 4 | 1 | ¿Qué código indica que el recurso se ha creado? / What code indicates a resource was created? | `201` |
| 4 | 2 | ¿Qué código indica que el recurso no existe? / What code indicates the resource was not found? | `404` |
| 4 | 3 | ¿Qué código indica servicio no disponible? / What code indicates service unavailable? | `503` |
| 4 | 4 | ¿Qué código indica no autorizado? / What code indicates unauthorised? | `401` |
| 5 | 1 | ¿Qué cabecera identifica al cliente y al sistema operativo? / What header identifies the client and OS? | `User-Agent` |
| 5 | 2 | ¿Qué cabecera indica el tipo de datos que se envían? / What header tells the web server what type of data is being sent? | `Content-Type` |
| 5 | 3 | ¿Qué cabecera indica qué sitio web se está solicitando? / What header specifies which site is being requested? | `Host` |
| 6 | 1 | ¿Qué cabecera se usa para establecer una cookie? / What header is used to set a cookie? | `Set-Cookie` |
| 7 | 1 | Flag de la primera petición. | `THM{YOU'RE_IN_THE_ROOM}` |
| 7 | 2 | Flag de la segunda petición. | `THM{YOU_FOUND_THE_BLOG}` |
| 7 | 3 | Flag de la tercera petición. | `THM{USER_IS_DELETED}` |
| 7 | 4 | Flag de la cuarta petición. | `THM{USER_HAS_UPDATED}` |
| 7 | 5 | Flag de la quinta petición. | `THM{HTTP_REQUEST_MASTER}` |

---

**Metodología:** Estudio del material teórico de HTTP/HTTPS y posterior práctica con peticiones reales al servidor del laboratorio mediante la AttackBox o el terminal, interpretando respuestas, códigos y cabeceras hasta obtener todas las flags.

### Cadena de ataque / Attack Chain

```text
teoría HTTP/HTTPS -> peticiones y respuestas -> métodos HTTP -> códigos de estado -> cabeceras -> cookies -> peticiones reales -> flags
```

**Learning chain:** HTTP -> HTTPS -> Request/Response -> métodos -> status codes -> cabeceras -> cookies -> peticiones prácticas -> flags.

**Lección:** *Dominar las cabeceras, métodos y códigos de estado HTTP es imprescindible para todo trabajo con aplicaciones web y para interpretar correctamente lo que ocurre en cada petición.*

**MITRE ATT&CK:** T1071 (Application Layer Protocol)

**Fuente:** [TryHackMe - HTTP in Detail](https://tryhackme.com/room/httpindetail)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
