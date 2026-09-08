# NoSQL Injection Basics

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `nosqlinjectiontutorial` |
| **Link** | [TryHackMe](https://tryhackme.com/room/nosqlinjectiontutorial) |
| **Sección** | 01 Level Easy |
| **Fuente** | Medium (CyferNest Sec, 0xk3r0), AuditMania (auditmania.com), Motasem Hamdan (Medium) |
| **Componentes** | Burp Suite / MongoDB / $ne / $nin / $regex / JavaScript ($where) / SSH |
| **Impacto** | Fundamentos de inyección NoSQL: bypass de login y extracción de datos con Operador Injection y Syntax Injection en MongoDB |

---

**Contexto:** Esta sala enseña los fundamentos de inyección NoSQL, cubriendo las diferencias entre SQL y NoSQL, los operadores de MongoDB, y los dos tipos principales de inyección NoSQL: Syntax Injection y Operator Injection. Incluye laboratorios prácticos de bypass de login y extracción de datos.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I am ready to learn about NoSQL Injection attacks! | `No answer needed` |

**Explicación:** Introducción al concepto de inyección NoSQL y preparación para el aprendizaje.

### Task 2: What is NoSQL?

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is a group of documents in MongoDB known as? | `collection` |
| 2 | Using the MongoDB Operator Reference, what operator is used to filter data when a field isn't equal to a given value? | `$ne` |
| 3 | Following the example of the 3 documents given before, how many documents would be returned by the following filter: `['gender' => ['$ne' => 'female'] , 'age' => ['$gt' => '65']]`? | `1` |

**Explicación:** En MongoDB, un grupo de documentos se conoce como **collection**. El operador `$ne` (not equal) se usa para filtrar datos cuando un campo no es igual a un valor dado. Si se aplica `['gender' => ['$ne' => 'female'], 'age' => ['$gt' => '65']]`, se devolvería **1** documento (solo el que cumple ambas condiciones).

### Task 3: NoSQL Injection

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of NoSQL Injection is similar to normal SQL Injection? | `Syntax` |
| 2 | What type of NoSQL Injection allows you to modify the behavior of the query, even if you can't escape the syntax? | `Operator` |

**Explicación:** Existen dos tipos principales de inyección NoSQL: **Syntax Injection** (similar a SQL injection clásica, rompe la sintaxis de la consulta) y **Operator Injection** (permite modificar el comportamiento de la consulta inyectando operadores como `$ne` o `$gt` sin escapar la sintaxis). La Operator Injection es más efectiva porque los filtros suelen fallar al detectar operadores NoSQL.

### Task 4: Operator Injection: Bypassing the Login Screen

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When bypassing the login screen using the $ne operator, what is the email of the user that you are logged in as? | `admin@nosql.int` |

**Explicación:** Para bypassear la pantalla de login usando el operador `$ne`, se intercepta la petición de login con Burp Suite y se reemplazan los campos username y password con payloads que usan `$ne`. Por ejemplo:

```
username[$ne]=anything&password[$ne]=anything
```

Esto retorna todos los documentos donde el username y password no sean iguales al valor dado, lo que efectivamente bypassea la autenticación. El email del usuario con el que se inicia sesión es `admin@nosql.int`.

### Task 5: Operator Injection: Logging in as Other Users

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | How many users are there in total? | `4` |
| 2 | There is a user that starts with the letter "p". What is his username? | `pedro` |

**Explicación:** Para acceder a cuentas específicas, se usa el operador `$nin` (not in) para excluir usuarios. Usando:

```
username[$nin][]=admin&password[$ne]=anything
```

se obtiene el siguiente usuario. Iterando, se descubren 4 usuarios en total: admin, pedro, john y secret. El usuario que empieza con "p" es `pedro`.

### Task 6: Operator Injection: Extracting Users' Passwords

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is john's password? | `10584312` |
| 2 | One of the users seems to be reusing his password for many services. Find which one and connect through SSH to retrieve the final flag! | `flag{N0Sql_n01iF3!}` |

**Explicación:** Para extraer contraseñas, se usa el operador `$regex` en un proceso similar al "ahorcado". Primero se prueba la longitud con `password[$regex]=^.{N}$`, luego se adivina cada carácter individualmente. La contraseña de john es `10584312`. Un usuario reutiliza su contraseña para SSH: pedro con la misma contraseña, y al conectarse por SSH se obtiene la flag final `flag{N0Sql_n01iF3!}`.

### Task 7: Syntax Injection: Identification and Data Extraction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What common character is used to test for injection in both SQL and NoSQL solutions? | `'` |
| 2 | What is the email value of the super secret user returned in the last entry? | `Syntax@Injection.FTW` |

**Explicación:** Para identificar Syntax Injection, se inserta un carácter `'` (comilla simple) en los campos de entrada. Si la aplicación retorna un error, indica que la consulta está concatenando input directamente (usando `$where` en JavaScript). Usando `admin' || 1 || 'x` como payload, se bypassea la condición y se obtienen todos los emails. El email del usuario super secreto es `Syntax@Injection.FTW`.

### Task 8: Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I understand NoSQL Injection attacks and acknowledge that user data should never be directly accepted into queries! | `No answer needed` |

**Explicación:** Comprensión de las técnicas de inyección NoSQL y la importancia de las prácticas de codificación segura.

**Metodología:**
1. **Comprensión de NoSQL:** entender la diferencia entre SQL y NoSQL, y cómo MongoDB almacena datos en documentos JSON dentro de colecciones.
2. **Operadores clave:** `$ne` (not equal), `$gt` (greater than), `$nin` (not in) y `$regex` (expresión regular) como operadores explotables.
3. **Bypass de autenticación:** interceptar peticiones de login con Burp Suite y reemplazar campos con `username[$ne]=anything&password[$ne]=anything` para que la consulta retorne documentos (login como `admin@nosql.int`).
4. **Enumeración de usuarios:** usar `$nin` iterativamente (`username[$nin][]=admin&password[$ne]=anything`) para excluir usuarios ya descubiertos y revelar los 4 usuarios: admin, pedro, john y secret.
5. **Extracción de contraseñas:** usar `$regex` tipo "ahorcado": primero longitud con `password[$regex]=^.{N}$` y luego cada carácter → john: `10584312`.
6. **Reutilización de credenciales:** pedro reutiliza la contraseña para SSH → flag final `flag{N0Sql_n01iF3!}`.
7. **Syntax Injection:** probar `'` para detectar concatenación directa (JS `$where`); payload `admin' || 1 || 'x` retorna todos los emails → último email `Syntax@Injection.FTW`.

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

**Learning chain:** identificación de entrada NoSQL → interceptación con Burp → inyección `$ne` (bypass login) → enumeración con `$nin` → extracción con `$regex` → reutilización en SSH → flag{N0Sql_n01iF3!} → Syntax Injection con `'` y `$where`

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1213 (Data from Information Repositories), T1078 (Valid Accounts), T1059.007 (Command and Scripting Interpreter: JavaScript)

**Fuente:** [TryHackMe - NoSQL Injection Basics](https://tryhackme.com/room/nosqlinjectiontutorial)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
