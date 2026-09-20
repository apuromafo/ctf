# OWASP API Security Top 10 - 2

| **Dificultad** | MEDIUM | **Tipo** | Walkthrough (Premium) | **Slug** | `owaspapisecuritytop102` |
| **Link** | [TryHackMe](https://tryhackme.com/room/owaspapisecuritytop102) | **Sección** | Web / API | **Fuente** | TryHackMe |
| **Componentes** | API Security, Mass Assignment, Security Misconfiguration, Injection, Improper Assets Management, Insufficient Logging & Monitoring, Laravel | **Impacto** | Manipulación de datos no autorizada, fuga de información interna, inyección de código y falta de visibilidad sobre el atacante por las cinco vulnerabilidades restantes del OWASP API Top 10 |

---

**Contexto:** Esta sala es la segunda parte del curso OWASP API Security Top 10 de TryHackMe y cubre los cinco principios restantes de la lista de 2019: Mass Assignment (API6), Security Misconfiguration (API7), Injection (API8), Improper Assets Management (API9) e Insufficient Logging & Monitoring (API10). Se practica sobre la misma aplicación Laravel de la parte 1, comprobando cómo la asignación masiva de campos, la configuración insegura, la inyección, los endpoints olvidados y la falta de logs comprometen la seguridad de las APIs.

> **ES:** Aprendizaje de los conceptos básicos para el desarrollo seguro de APIs (Parte 2): asignación masiva (Mass Assignment), configuración insegura (Security Misconfiguration), inyección (Injection), gestión inadecuada de activos (Improper Assets Management) y registro y monitoreo insuficientes (Insufficient Logging & Monitoring), con ejemplos prácticos explotables.
> **EN:** Learning the basic concepts for secure API development (Part 2): Mass Assignment, Security Misconfiguration, Injection, Improper Assets Management, and Insufficient Logging & Monitoring, with practical exploitable examples.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se introduce la parte 2 del curso. OWASP publicó en 2019 la lista de las diez principales vulnerabilidades de APIs; esta sala cubre las cinco restantes (API6 a API10) y se centra en el desarrollo seguro de APIs.

1. No answer needed

### Task 2: Vulnerabilidad VI — Asignación Masiva / Mass Assignment

**Explicación:** Mass Assignment ocurre cuando la entrada del cliente se asigna automáticamente a objetos o variables del servidor. No es buena práctica insertar/actualizar datos proporcionados por el usuario de forma ciega (`nay`). Usando `/apirule6/user_s` con el valor de crédito 1000 se inserta un registro, pero el servidor devuelve el valor de crédito 50, el valor por defecto forzado por el backend seguro.

1. 1. nay
   2. No answer needed
   3. 50

### Task 3: Vulnerabilidad VII — Configuración Insegura / Security Misconfiguration

**Explicación:** La configuración insegura abarca controles de seguridad mal implementados (documentación pública, credenciales por defecto, error messages verbosos). No es una buena práctica mostrar los logs de la traza de errores a los visitantes (`nay`). Al usar el endpoint seguro `/apirule7/ping_s` se obtiene el código HTTP 500 y el Error ID 1401 en el mensaje de respuesta.

1. 1. nay
   2. No answer needed
   3. 500
   4. 1401

### Task 4: Vulnerabilidad VIII — Inyección / Injection

**Explicación:** La inyección ocurre cuando datos no confiables se envían a un intérprete (SQL, NoSQL, shell) como parte de un comando o consulta. Los ataques de inyección sí pueden realizarse para extraer datos de la base de datos (`yea`) y también pueden resultar en ejecución remota de código (`yea`). El código HTTP devuelto al introducir un username o password inválidos es 403.

1. 1. yea
   2. yea
   3. 403

### Task 5: Vulnerabilidad IX — Gestión Inadecuada de Activos / Improper Assets Management

**Explicación:** La gestión inadecuada de activos ocurre cuando la organización no tiene un inventario completo y actualizado de sus APIs, dejando endpoints antiguos o "shadow" expuestos. No es buena práctica alojar todas las APIs en el mismo servidor (`nay`). Consultando la API se descubre que el balance de la usuaria Alice es 100 y que su país es USA.

1. 1. nay
   2. No answer needed
   3. 100
   4. USA

### Task 6: Vulnerabilidad X — Registro y Monitoreo Insuficientes / Insufficient Logging & Monitoring

**Explicación:** Sin registro y monitoreo adecuado, el atacante puede permanecer en la red durante semanas o meses sin ser detectado. Los logs de la API no deben ser públicamente accesibles (`nay`). El código HTTP en caso de registro exitoso de información de usuario es 200.

1. 1. nay
   2. 200

### Task 7: Conclusión / Conclusion

**Explicación:** Se concluye la segunda parte del curso, habiendo estudiado las cinco vulnerabilidades restantes del OWASP API Security Top 10 (2019) y sus correspondientes medidas de mitigación.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2.1 | Is it a good practice to blindly insert/update user-provided data in the database (yea/nay)? | `nay` |
| 2.2 | Using /apirule6/user_s, insert a record in the database using the credit value as 1000. | `No answer needed` |
| 2.3 | What would be the returned credit value after performing Question #2? | `50` |
| 3.1 | Is it an excellent approach to show error logs from the stack trace to general visitors (yea/nay)? | `nay` |
| 3.2 | Try to use the API call /apirule7/ping_s in the attached VM. | `No answer needed` |
| 3.3 | What is the HTTP response code? | `500` |
| 3.4 | What is the Error ID number in the HTTP response message? | `1401` |
| 4.1 | Can injection attacks be carried out to extract data from the database (yea/nay)? | `yea` |
| 4.2 | Can injection attacks result in remote code execution (yea/nay)? | `yea` |
| 4.3 | What is the HTTP response code if a user enters an invalid username or password? | `403` |
| 5.1 | Is it good practice to host all APIs on the same server (yea/nay)? | `nay` |
| 5.2 | Promiscuous endpoints left behind can leak sensitive information about the company. | `No answer needed` |
| 5.3 | What is the amount of balance associated with user Alice? | `100` |
| 5.4 | What is the country of the user Alice? | `USA` |
| 6.1 | Should the API logs be publically accessible so that the attacker must know they are being logged (yea/nay)? | `nay` |
| 6.2 | What is the HTTP response code in case of successful logging of user information? | `200` |

---

**Metodología:** Para Mass Assignment se envió un POST a `/apirule6/user_s` manipulando el campo `credit` (1000) y se observó que el backend seguro lo forzaba a 50. En Security Misconfiguration se comparó el endpoint inseguro `/apirule7/ping_v` con el seguro `/apirule7/ping_s` y se leyeron los códigos de error y el Error ID 1401. En Injection se probaron entradas maliciosas en los endpoints de búsqueda/login observando el código 403. En Improper Assets Management se localizaron endpoints antiguos y se consultaron datos de usuarios. En Insufficient Logging & Monitoring se verificó la accesibilidad de los logs y el código HTTP 200 al registrar información.

**Learning chain:** Introducción a la parte 2 → Mass Assignment (campos no filtrados y valores por defecto) → Security Misconfiguration (stack traces y códigos de error) → Injection (extracción de datos y RCE) → Improper Assets Management (endpoints olvidados) → Insufficient Logging & Monitoring (visibilidad del atacante) → Conclusión.

**Lección:** *Las cinco vulnerabilidades restantes del OWASP API Top 10 muestran que la seguridad de una API depende de la higiene integral del ciclo de vida: campos permitidos explícitos (fillable/guarded), gestión de errores minimalista, consultas parametrizadas, inventario de endpoints siempre actualizado y registros y monitoreo activo para detectar al atacante.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1082 (System Information Discovery), T1213 (Data from Information Repositories)

**Fuente:** [TryHackMe - OWASP API Security Top 10 - 2](https://tryhackme.com/room/owaspapisecuritytop102)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.