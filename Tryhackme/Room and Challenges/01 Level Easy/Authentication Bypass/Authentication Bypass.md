# Authentication Bypass

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `authenticationbypass` |
| **Link** | [TryHackMe](https://tryhackme.com/room/authenticationbypass) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Username Enumeration, fuerza bruta, cookie tampering, JWT, Base64 |
| **Impacto** | Bypass de autenticación en aplicaciones web mediante enumeración de usuarios, fuerza bruta y manipulación de cookies/JWT. |

---

**Contexto:** La sala practica distintas técnicas para evadir la autenticación de una aplicación web. Se comienza enumerando los usuarios válidos a través de las diferencias en los mensajes de error, se aplica fuerza bruta al formulario de login hasta obtener credenciales válidas, y finalmente se manipulan cookies y tokens (valor secreto, codificación Base64 y modificación de campos del JWT) para acceder al panel de administración y obtener las flags.

## Solucionario

### Task 1: Enumeración de usuarios / Username Enumeration

**Explicación:** Se explora la funcionalidad de registro y login de la aplicación para detectar diferencias en los mensajes de error que permitan enumerar usuarios existentes. Paso práctico sin respuesta numérica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realizar el paso práctico de enumeración de usuarios. | `No answer needed` |

### Task 2: Listado de usuarios / Usernames Found

**Explicación:** Gracias a las diferencias de respuesta de la aplicación se confirman tres usuarios válidos en el sistema: `simon`, `steve` y `robert`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué usuario válido se confirma en primer lugar? | `simon` |
| 2 | ¿Qué usuario válido se confirma en segundo lugar? | `steve` |
| 3 | ¿Qué usuario válido se confirma en tercer lugar? | `robert` |

### Task 3: Fuerza bruta / Brute Force

**Explicación:** Se fuerza bruta al formulario de login con el usuario válido `steve` hasta encontrar su contraseña, obteniendo las credenciales válidas `steve/thunder`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué credencial es válida para acceder al panel? | `steve/thunder` |

### Task 4: Flag del panel / Admin Panel Flag

**Explicación:** Con las credenciales válidas se accede al panel de administración y se localiza la flag que demuestra el bypass completo de la autenticación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag obtenida tras el bypass de autenticación? | `THM{AUTH_BYPASS_COMPLETE}` |

### Task 5: Manipulación de cookies / Cookie Tampering

**Explicación:** Se manipula la cookie/token del panel: primero se altera la cookie para obtener la flag de **cookie tampering**, después se identifican el valor secreto usado en la firma, se decodifica el payload **Base64** y se modifica el campo del token (JSON `eyJpZCI6MSwiYWRtaW4iOnRydWV9`) para elevar los privilegios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la manipulación de cookies? | `THM{COOKIE_TAMPERING}` |
| 2 | ¿Cuál es el valor secreto del token/cookie? | `463729` |
| 3 | ¿Cuál es la flag de la decodificación Base64? | `THM{BASE64_ENCODING}` |
| 4 | ¿Cuál es el valor del token JWT modificado para ser administrador? | `eyJpZCI6MSwiYWRtaW4iOnRydWV9` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Realizar el paso práctico de enumeración de usuarios. | `No answer needed` |
| 2 | ¿Qué usuario válido se confirma en primer lugar? | `simon` |
| 3 | ¿Qué usuario válido se confirma en segundo lugar? | `steve` |
| 4 | ¿Qué usuario válido se confirma en tercer lugar? | `robert` |
| 5 | ¿Qué credencial es válida para acceder al panel? | `steve/thunder` |
| 6 | ¿Cuál es la flag obtenida tras el bypass de autenticación? | `THM{AUTH_BYPASS_COMPLETE}` |
| 7 | ¿Cuál es la flag de la manipulación de cookies? | `THM{COOKIE_TAMPERING}` |
| 8 | ¿Cuál es el valor secreto del token/cookie? | `463729` |
| 9 | ¿Cuál es la flag de la decodificación Base64? | `THM{BASE64_ENCODING}` |
| 10 | ¿Cuál es el valor del token JWT modificado para ser administrador? | `eyJpZCI6MSwiYWRtaW4iOnRydWV9` |

---

**Metodología:**

1. Se practica la enumeración de usuarios detectando diferencias de respuesta y de mensajes de error en el formulario.
2. Se confirman los usuarios `simon`, `steve` y `robert`.
3. Se aplica fuerza bruta al login con el usuario `steve` hasta obtener las credenciales `steve/thunder`.
4. Se accede al panel y se obtiene la flag `THM{AUTH_BYPASS_COMPLETE}`.
5. Se manipula la cookie del panel (cookie tampering) para obtener `THM{COOKIE_TAMPERING}`.
6. Se identifica el valor secreto `463729`, se decodifica el payload Base64 (`THM{BASE64_ENCODING}`) y se modifica el token JWT (`eyJpZCI6MSwiYWRtaW4iOnRydWV9`) para escalar a administrador.

### Cadena de ataque / Attack Chain

```
Username enumeration -> simon, steve, robert
  -> Brute force login -> steve/thunder
  -> Acceso al panel -> THM{AUTH_BYPASS_COMPLETE}
  -> Cookie tampering -> THM{COOKIE_TAMPERING}
  -> Secreto JWT 463729
  -> Decodificar Base64 -> THM{BASE64_ENCODING}
  -> Token modificado eyJpZCI6MSwiYWRtaW4iOnRydWV9 -> admin
```

**Learning chain:** Enumeración de usuarios → Fuerza bruta → Acceso válido → Bypass de autenticación → Manipulación de cookies → JWT/Base64 → Administrador

**Lección:** *Las aplicaciones web no deben filtrar en sus mensajes de error qué credenciales son válidas, y las cookies/tokens firmados con secretos débiles y payloads en Base64 son fáciles de manipular si no se valida la firma del lado del servidor.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1110 (Brute Force), T1078 (Valid Accounts), T1555 (Credentials from Password Stores)

**Fuente:** [TryHackMe - Authentication Bypass](https://tryhackme.com/room/authenticationbypass)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.