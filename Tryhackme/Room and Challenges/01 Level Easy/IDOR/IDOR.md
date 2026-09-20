# IDOR

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `idor` | [TryHackMe](https://tryhackme.com/room/idor) | 01 Level Easy | THM | IDOR, Insecure Direct Object Reference, base64, md5, User Enumeration | Acceso no autorizado a objetos y datos de otros usuarios mediante referencias directas manipulables |

> **Objeto:** Aprender qué es un IDOR (Insecure Direct Object Reference), cómo aparecen en IDs codificados, hasheados e impredecibles, y explotarlos en un reto práctico de enumeración de usuarios.

---

**Contexto:** Sala de TryHackMe centrada en los IDOR. Explica el concepto de referencia directa insegura a objetos y muestra cómo los identificadores codificados (base64) o hasheados (md5) no son un control de seguridad real, ya que pueden descodificarse, descifrarse o manipularse. Incluye un reto práctico donde se enumeran usuarios y correos mediante IDOR.

> **ES:** Una sala práctica para entender qué es un IDOR, por qué los IDs codificados y hasheados no protegen los objetos, y cómo explotar las referencias directas para acceder a datos de otros usuarios.
> **EN:** A hands-on room to understand what an IDOR is, why encoded and hashed IDs do not protect objects, and how to exploit direct object references to access other users' data.

## Solucionario

### Task 1: ¿Qué es un IDOR? / What is an IDOR?

**Explicación:** Un IDOR (Insecure Direct Object Reference) es una vulnerabilidad que aparece cuando una aplicación usa directamente un identificador (ID) de un objeto sin comprobar si el usuario está autorizado a acceder a él.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué significa IDOR? / What does IDOR stand for? | `Insecure Direct Object Reference` |

### Task 2: IDOR en IDs codificados / IDORs in Encoded IDs

**Explicación:** Los IDs codificados, típicamente en base64, se pueden decodificar con facilidad; modificar el valor decodificado y volver a codificarlo permite acceder a objetos de otros usuarios y obtener la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2 | Obtenga la bandera / Get the flag | `THM{IDOR-VULN-FOUND}` |
| 3 | ¿Qué codificación se utiliza en este apartado? / Which encoding is used here? | `base64` |

### Task 3: IDOR en IDs hasheados / IDORs in Hashed IDs

**Explicación:** Los IDs hasheados con MD5 tampoco son seguros porque el hash de un valor predecible puede descifrarse comparándolo con versiones hasheadas de valores candidatos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 4 | ¿Qué algoritmo de hash se utiliza en este apartado? / Which hashing algorithm is used here? | `md5` |
| 5 | ¿Cuál es el valor correcto? / What is the correct value? | `2` |

### Task 4: IDOR en IDs impredecibles / IDORs in Unpredictable IDs

**Explicación:** Aunque un ID sea impredecible, sigue existiendo una referencia directa al objeto; la seguridad no debe depender de la dificultad de adivinar el identificador, sino de la comprobación de autorización.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 6 | ¿Hay que responder algo en este apartado? / Is there anything to answer here? | `No answer needed` |

### Task 5: Reto práctico / Small Practical Challenge

**Explicación:** Reto final donde se abusa de la referencia directa a una cuenta para cambiar el nombre de usuario y leer el correo del objetivo, enumerando otros usuarios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 7.1 | Introduzca el nombre de usuario del perfil / Enter the profile's username | `adam84` |
| 7.2 | Introduzca el correo electrónico del perfil / Enter the profile's email | `j@fakemail.thm` |

---

**Metodología:** Se identificó la respuesta conceptual del IDOR, y en la práctica los IDs se decodificaron desde base64 y se descifraron desde md5 para manipular las referencias directas. En el reto final se modificó el ID de usuario en la URL para cambiar el nombre de perfil a `adam84` y leer el email `j@fakemail.thm`, obteniéndose la flag `THM{IDOR-VULN-FOUND}`.

### Cadena de ataque / Attack Chain

Identificación del concepto IDOR → localización de IDs codificados (base64) → decodificación y manipulación del valor → localización de IDs hasheados (md5) → descifrado del hash → modificación de la referencia directa en el reto final → lectura de datos del perfil objetivo.

**Learning chain:** IDOR (definición) → IDs codificados base64 → IDs hasheados md5 → IDs impredecibles → enumeración de usuarios → lectura de email ajeno.

**Lección:** *Codificar u oscurecer un identificador (base64, md5) no es un control de autorización: la aplicación debe validar siempre que el usuario tenga permiso sobre el objeto referenciado antes de devolver sus datos.*

**MITRE ATT&CK:** T1087 (Account Discovery), T1213 (Data from Information Repositories), T1530 (Data from Cloud Storage), T1078 (Valid Accounts).

**Fuente:** [TryHackMe - IDOR](https://tryhackme.com/room/idor)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.