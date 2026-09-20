# OWASP Broken Access Control

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `owaspbrokenaccesscontrol` | https://tryhackme.com/room/owaspbrokenaccesscontrol | 01 Level Easy | TryHackMe | Broken Access Control, IDOR, escalada horizontal/vertical, Burp Suite (Proxy), cookies de sesión | Acceso no autorizado a funcionalidad administrativa y recursos de otros usuarios, incluyendo escalada vertical a un panel admin |

---

**Contexto:** Este módulo de OWASP (Top 10 Web Application Security Risks) introduce el Broken Access Control, la vulnerabilidad número uno del Top 10, mediante una aplicación web deliberadamente vulnerable. Se practica la identificación del tipo de servidor y parámetros clave con Burp Suite, la manipulación de cookies de sesión y la escalada vertical de privilegios hasta acceder a un panel de administración protegido.

> **ES:** Despliega una máquina vulnerable, utiliza Burp Suite para inspeccionar el tráfico, identifica los conceptos de IDOR y escalada horizontal/vertical, manipula la cookie `isadmin` para elevar privilegios y captura la flag del panel de administración.
> **EN:** Deploy a deliberately vulnerable machine, use Burp Suite to inspect traffic, learn IDOR and horizontal/vertical privilege escalation, tamper with the `isadmin` cookie to elevate privileges and capture the flag from the admin panel.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea de presentación del módulo de Broken Access Control dentro del Top 10 de OWASP. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click me to proceed onto the next task | `No answer needed` |

### Task 2: Introducción al Control de Acceso Roto / Broken Access Control Introduction

**Explicación:** Se definen los cuatro conceptos clave que explican cómo se rompe el control de acceso: las Insecure Direct Object References (IDOR), es decir, referencias directas e inseguras a objetos que permiten acceder a recursos ajenos; la escalada horizontal, cuando un atacante accede a recursos de otros usuarios con el mismo nivel de privilegio; la escalada vertical, cuando accede a recursos de usuarios con mayor nivel; y los modelos de autorización basados en atributos (ABAC) o en roles (RBAC).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is IDOR? | `Insecure direct object reference` |
| 2 | What occurs when an attacker can access resources or data belonging to other users with the same level of access? | `Horizontal privilege escalation` |
| 3 | What occurs when an attacker can access resources or data from users with higher access levels? | `Vertical privilege escalation` |
| 4 | What is ABAC? | `Attribute-Based Access Control` |
| 5 | What is RBAC? | `Role-Based Access Control` |

### Task 3: Despliegue de la máquina / Deploy the Machine

**Explicación:** Se inicia la máquina vulnerable para las tareas de explotación. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I have deployed the machine attached to the task | `No answer needed` |

### Task 4: Evaluación de la aplicación web / Assessing the Web Application

**Explicación:** Se levanta la aplicación y se intercepta su tráfico con el módulo **Proxy** de Burp Suite. La respuesta a la petición de login revela las cabeceras que identifican al servidor web como **Apache** (Server: Apache). En la respuesta JSON del envío de credenciales aparece el parámetro `redirect_link`, usado para devolver al cliente una URL de redirección. Con la funcionalidad de "online users" de la aplicación se consulta una tabla de usuarios conectados donde aparece el email del administrador `admin@admin.com`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the type of server that is hosting the web application? This can be found in the response of the request in Burp Suite. | `Apache` |
| 2 | What is the name of the parameter in the JSON response from the login request that contains a redirect link? | `redirect_link` |
| 3 | What Burp Suite module allows us to capture requests and responses between ourselves and our target? | `Proxy` |
| 4 | What is the admin's email that can be found in the online users' table? | `admin@admin.com` |

### Task 5: Explotando la aplicación web / Exploiting the Web Application

**Explicación:** El panel `admin.php` se autentica con una cookie llamada `isadmin` que vale `0` por defecto. Cambiando su valor a `1` se consigue una escalada de privilegios de tipo **vertical** (de usuario normal al rol de administrador) sin conocer credenciales. Al recargar `admin.php` con la cookie falsificada, el sitio devuelve la flag `THM{I_C4n_3xpl01t_B4c}`. Este ejercicio demuestra por qué la autorización no debe confiarse a una cookie fácilmente manipulable.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What kind of privilege escalation happened after accessing admin.php? | `Vertical` |
| 2 | What parameter allows the attacker to access the admin page? | `isadmin` |
| 3 | What is the flag in the admin page? | `THM{I_C4n_3xpl01t_B4c}` |

### Task 6: Mitigación / Mitigation

**Explicación:** Tarea conceptual sobre las buenas prácticas para mitigar el Broken Access Control (autorización en el servidor, deny-by-default, modelos ABAC/RBAC, etc.). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click me to proceed onto the next task | `No answer needed` |

### Task 7: Conclusión / Conclusion

**Explicación:** Cierre del módulo. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click me to finish this room | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Click me to proceed onto the next task | `No answer needed` |
| 2 | What is IDOR? | `Insecure direct object reference` |
| 3 | What occurs when an attacker can access resources or data belonging to other users with the same level of access? | `Horizontal privilege escalation` |
| 4 | What occurs when an attacker can access resources or data from users with higher access levels? | `Vertical privilege escalation` |
| 5 | What is ABAC? | `Attribute-Based Access Control` |
| 6 | What is RBAC? | `Role-Based Access Control` |
| 7 | I have deployed the machine attached to the task | `No answer needed` |
| 8 | What is the type of server that is hosting the web application? This can be found in the response of the request in Burp Suite. | `Apache` |
| 9 | What is the name of the parameter in the JSON response from the login request that contains a redirect link? | `redirect_link` |
| 10 | What Burp Suite module allows us to capture requests and responses between ourselves and our target? | `Proxy` |
| 11 | What is the admin's email that can be found in the online users' table? | `admin@admin.com` |
| 12 | What kind of privilege escalation happened after accessing admin.php? | `Vertical` |
| 13 | What parameter allows the attacker to access the admin page? | `isadmin` |
| 14 | What is the flag in the admin page? | `THM{I_C4n_3xpl01t_B4c}` |
| 15 | Click me to proceed onto the next task | `No answer needed` |
| 16 | Click me to finish this room | `No answer needed` |

---

**Metodología:** Se estudia el modelo de referencia del OWASP Top 10 para Broken Access Control y se aplica sobre una aplicación vulnerable de forma práctica: interceptación con Burp Suite, análisis de cabeceras y parámetros de sesión, manipulación de cookies cliente (`isadmin`) y verificación de una escalada vertical de privilegios.

### Cadena de ataque / Attack Chain

```text
Burp Suite Proxy -> HTTP response (Server: Apache) -> JSON login (redirect_link) -> online users (admin@admin.com) -> cookie isadmin=1 -> admin.php -> THM{I_C4n_3xpl01t_B4c}
```

**Learning chain:** OWASP Top 10 → IDOR → horizontal vs vertical escalation → ABAC/RBAC → Burp Suite Proxy → cookie tampering → vertical privilege escalation → mitigation

**Lección:** *Nunca confíes la autorización a valores controlables por el cliente: una cookie como `isadmin=0` solo separa al usuario de los privilegios de administrador por una costumbre, no por un control real.*

**MITRE ATT&CK:** T1068 (Exploitation for Privilege Escalation) — OWASP A01:2021 (Broken Access Control)

**Fuente:** [TryHackMe - OWASP Broken Access Control](https://tryhackme.com/room/owaspbrokenaccesscontrol)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.