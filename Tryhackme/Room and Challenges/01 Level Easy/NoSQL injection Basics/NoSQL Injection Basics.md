# NoSQL Injection Basics [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough
* **Slug:** `nosqlinjectiontutorial`
* **Link:** https://tryhackme.com/room/nosqlinjectiontutorial
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Medium (CyferNest Sec, 0xk3r0), AuditMania (auditmania.com), Motasem Hamdan (Medium)

## Solucionario de Tareas / Task Solutions

> **ES:** Esta sala enseña los fundamentos de inyección NoSQL, cubriendo las diferencias entre SQL y NoSQL, los operadores de MongoDB, y los dos tipos principales de inyección NoSQL: Syntax Injection y Operator Injection. Incluye laboratorios prácticos de bypass de login y extracción de datos.
> **EN:** This room teaches NoSQL injection fundamentals, covering differences between SQL and NoSQL, MongoDB operators, and the two main types of NoSQL injection: Syntax Injection and Operator Injection. It includes practical labs for login bypass and data extraction.

### Task 1 - Introduction

> **ES:** Introducción al concepto de inyección NoSQL y preparación para el aprendizaje.
> **EN:** Introduction to the concept of NoSQL injection and preparation for learning.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I am ready to learn about NoSQL Injection attacks! | `No answer needed` |

### Task 2 - What is NoSQL?

> **ES:** En MongoDB, un grupo de documentos se conoce como **collection**. El operador `$ne` (not equal) se usa para filtrar datos cuando un campo no es igual a un valor dado. Si se aplica `['gender' => ['$ne' => 'female'], 'age' => ['$gt' => '65']]`, se devolvería **1** documento (solo el que cumple ambas condiciones).
> **EN:** In MongoDB, a group of documents is known as a **collection**. The `$ne` (not equal) operator is used to filter data when a field is not equal to a given value. If `['gender' => ['$ne' => 'female'], 'age' => ['$gt' => '65']]` is applied, **1** document would be returned (only the one meeting both conditions).

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is a group of documents in MongoDB known as? | `collection` |
| Using the MongoDB Operator Reference, what operator is used to filter data when a field isn't equal to a given value? | `$ne` |
| Following the example of the 3 documents given before, how many documents would be returned by the following filter: `['gender' => ['$ne' => 'female'] , 'age' => ['$gt' => '65']]`? | `1` |

### Task 3 - NoSQL Injection

> **ES:** Existen dos tipos principales de inyección NoSQL: **Syntax Injection** (similar a SQL injection clásica, rompe la sintaxis de la consulta) y **Operator Injection** (permite modificar el comportamiento de la consulta inyectando operadores como `$ne` o `$gt` sin escapar la sintaxis). La Operator Injection es más efectiva porque los filtros suelen fallar al detectar operadores NoSQL.
> **EN:** There are two main types of NoSQL injection: **Syntax Injection** (similar to classic SQL injection, breaks query syntax) and **Operator Injection** (allows modifying query behavior by injecting operators like `$ne` or `$gt` without escaping syntax). Operator Injection is more effective because filters often fail to detect NoSQL operators.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What type of NoSQL Injection is similar to normal SQL Injection? | `Syntax` |
| What type of NoSQL Injection allows you to modify the behavior of the query, even if you can't escape the syntax? | `Operator` |

### Task 4 - Operator Injection: Bypassing the Login Screen

> **ES:** Para bypassear la pantalla de login usando el operador `$ne`, se intercepta la petición de login con Burp Suite y se reemplazan los campos username y password con payloads que usan `$ne`. Por ejemplo: `username[$ne]=anything&password[$ne]=anything`. Esto retorna todos los documentos donde el username y password no sean iguales al valor dado, lo que efectivamente bypassea la autenticación. El email del usuario con el que se inicia sesión es `admin@nosql.int`.
> **EN:** To bypass the login screen using the `$ne` operator, intercept the login request with Burp Suite and replace the username and password fields with payloads using `$ne`. For example: `username[$ne]=anything&password[$ne]=anything`. This returns all documents where username and password are not equal to the given value, effectively bypassing authentication. The email of the logged-in user is `admin@nosql.int`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| When bypassing the login screen using the $ne operator, what is the email of the user that you are logged in as? | `admin@nosql.int` |

### Task 5 - Operator Injection: Logging in as Other Users

> **ES:** Para acceder a cuentas específicas, se usa el operador `$nin` (not in) para excluir usuarios. Usando `username[$nin][]=admin&password[$ne]=anything`, se obtiene el siguiente usuario. Iterando, se descubren 4 usuarios en total: admin, pedro, john, y secret. El usuario que empieza con "p" es `pedro`.
> **EN:** To access specific accounts, use the `$nin` (not in) operator to exclude users. Using `username[$nin][]=admin&password[$ne]=anything`, the next user is obtained. By iterating, 4 users are discovered total: admin, pedro, john, and secret. The user starting with "p" is `pedro`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| How many users are there in total? | `4` |
| There is a user that starts with the letter "p". What is his username? | `pedro` |

### Task 6 - Operator Injection: Extracting Users' Passwords

> **ES:** Para extraer contraseñas, se usa el operador `$regex` en un proceso similar al "ahorcado". Primero se prueba la longitud con `password[$regex]=^.{N}$`, luego se adivina cada carácter individualmente. La contraseña de john es `10584312`. Un usuario reutiliza su contraseña para SSH: pedro con la misma contraseña, y al conectarse por SSH se obtiene la flag final.
> **EN:** To extract passwords, use the `$regex` operator in a process similar to "hangman". First test the length with `password[$regex]=^.{N}$`, then guess each character individually. John's password is `10584312`. One user reuses their password for SSH: pedro with the same password, and connecting via SSH reveals the final flag.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is john's password? | `10584312` |
| One of the users seems to be reusing his password for many services. Find which one and connect through SSH to retrieve the final flag! | `flag{N0Sql_n01iF3!}` |

### Task 7 - Syntax Injection: Identification and Data Extraction

> **ES:** Para identificar Syntax Injection, se inserta un carácter `'` (comilla simple) en los campos de entrada. Si la aplicación retorna un error, indica que la consulta está concatenando input directamente (usando `$where` en JavaScript). Usando `admin' || 1 || 'x` como payload, se bypassea la condición y se obtienen todos los emails. El email del usuario super secreto es `Syntax@Injection.FTW`.
> **EN:** To identify Syntax Injection, insert a `'` (single quote) character in input fields. If the application returns an error, it indicates the query concatenates input directly (using `$where` in JavaScript). Using `admin' || 1 || 'x` as payload bypasses the condition and returns all emails. The super secret user's email is `Syntax@Injection.FTW`.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What common character is used to test for injection in both SQL and NoSQL solutions? | `'` |
| What is the email value of the super secret user returned in the last entry? | `Syntax@Injection.FTW` |

### Task 8 - Conclusion

> **ES:** Comprensión de las técnicas de inyección NoSQL y la importancia de las prácticas de codificación segura.
> **EN:** Understanding NoSQL injection techniques and the importance of secure coding practices.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I understand NoSQL Injection attacks and acknowledge that user data should never be directly accepted into queries! | `No answer needed` |

## Metodología / Methodology

1. **Paso / Step - Comprensión de NoSQL:** Entender la diferencia entre SQL y NoSQL, y cómo MongoDB almacena datos en documentos JSON dentro de colecciones.
2. **Paso / Step - Identificación de operadores clave:** Conocer `$ne` (not equal), `$gt` (greater than), `$nin` (not in), y `$regex` (expresión regular) como operadores explotables.
3. **Paso / Step - Bypass de autenticación:** Interceptar peticiones de login con Burp Suite y reemplazar campos con payloads usando `$ne` para forzar que la consulta retorne documentos.
4. **Paso / Step - Enumeración de usuarios:** Usar `$nin` iterativamente para excluir usuarios ya descubiertos y revelar todos los usuarios del sistema.
5. **Paso / Step - Extracción de contraseñas:** Usar `$regex` para adivinar longitud y caracteres individuales de contraseñas mediante un proceso de prueba y error.
6. **Paso / Step - Detección de Syntax Injection:** Probar con `'` para detectar errores de concatenación y explotar con payloads de JavaScript (`||1||`).
7. **Paso / Step - Explotación de reutilización de credenciales:** Una vez obtenidas las contraseñas, probarlas en otros servicios como SSH.

### Cadena de ataque / Attack Chain

```
Identificación de entrada NoSQL (login form)
        |
        v
Interceptación con Burp Suite
        |
        v
Inyección de operador ($ne) para bypass de login
        |
        v
Enumeración de usuarios con $nin iterativo
        |
        v
Extracción de contraseñas con $regex
        |
        v
Detección de Syntax Injection con comilla simple (')
        |
        v
Explotación de concatenación insegura ($where)
        |
        v
Reutilización de credenciales en SSH -> Flag
```

**Lección:** La inyección NoSQL es tan peligrosa como la SQL injection clásica; los desarrolladores nunca deben aceptar datos de usuarios directamente en consultas y deben usar consultas parametrizadas tanto para bases de datos SQL como NoSQL.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
