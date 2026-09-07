# CSRF Introduction

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `csrfintroduction` |
| **Link** | [TryHackMe](https://tryhackme.com/room/csrfintroduction) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + máquina/vulnerable web app del room |
| **Componentes** | CSRF (Cross-Site Request Forgery) / cookies/sesión / métodos HTTP / tokens anti-CSRF (base64) / formularios HTML / Burp Suite |
| **Impacto** | Entiende CSRF: la confianza navegador-app que explota, por qué el navegador envía cookies automáticamente, y la defensa con tokens anti-CSRF (y cómo encodearlos de forma segura). |

---

**Contexto:** CSRF abusa de la **relación de confianza** entre el navegador y la aplicación web: tras el login, el navegador incluye automáticamente las **cookies** de sesión en cada petición. Si la app recibe una petición con cookie válida, no sabe si la inició el usuario o un sitio malicioso. El ataque necesita una **acción que cambie el estado** (state-changing: cambiar email, password, rol...), porque leer datos con GET es "inofensivo" desde CSRF. Muchos desarrolladores creen erróneamente que **POST** la evita, pero el atacante solo necesita un formulario web que haga POST. La defensa estándar son los **tokens anti-CSRF**; si el token es débil/predicable (aquí codificado en **base64**), el ataque sigue funcionando. El lab demuestra los dos casos: actualizar el email de una cuenta y demotar a un admin, con flags por cada demo.

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - deploy and connect to the machine. | `No answer needed` |

### Task 2: Qué es CSRF

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What relationship between the browser and the web application does a CSRF attack abuse? | `Trust` |
| 2 | What does the browser **automatically include** with requests after login? | `Cookies` |

### Task 3: Por Qué Funciona CSRF

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of action is usually required for a CSRF attack to succeed? | `State-changing` |

### Task 4: Encontrando Vulnerabilidades CSRF

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What HTTP request method do many developers incorrectly believe prevents CSRF? | `POST` |
| 2 | What mechanism is commonly used to protect applications from CSRF attacks? | `CSRF tokens` |

### Task 5: Explotación con un Formulario HTML

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag value after updating the email to `attacker@evilmail.thm`? | `THM{Got_The_Evil_Email001}` |
| 2 | What is the flag value after updating the email to `special@evilmail.thm`? | `THM{My_Special_Email007}` |

### Task 6: Explotación sobre Tokens Débiles

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag value after demoting the user from **admin to staff**? (visit the dashboard) | `THM{Weak_CSRF_Role_001}` |
| 2 | In the above example, what is the name of the encoding scheme used by the developer for encoding **CSRF tokens**? | `base64` |

### Task 7: Buenas Prácticas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - best practices understood. | `No answer needed` |

### Task 8: Conclusión

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - room completed. | `No answer needed` |

---

**Metodología:**
1. Desplegar la app vulnerable y autenticarse.
2. Revisar con Burp (o el proxy que prefieras) cómo se envían las peticiones de cambio de email/rol (método, cookies, token).
3. Explotar la demo de email con un formulario propio: una página vulnerable permite cambiar el email por GET/POST sin token; preparas un HTML en tu máquina con `<form method="POST" action="http://MACHINE_IP/..."><input name="email" value="..."><script>document.forms[0].submit()</script></form>`; al abrirlo con la sesión activa el email cambia → los dos flags según el email usado (`attacker@evilmail.thm` y `special@evilmail.thm`).
4. En la demo de roles, forjar/decodificar el token débil (base64) y demotar al admin de admin a staff → flag `THM{Weak_CSRF_Role_001}` en el dashboard; base64 no es seguridad, solo encoding.
5. Completar las preguntas teóricas (T2–T4) con las secciones del room: Trust, Cookies, State-changing, POST (creencia errónea), CSRF tokens.

**Learning chain:** víctima autenticada (cookie de sesión válida) → el navegador envía cookies automáticamente (trust) → página maliciosa auto-submit de formulario → petición state-changing (cambio email/rol) → sin token o token débil (base64 forjable) → flags: THM{Got_The_Evil_Email001} · THM{My_Special_Email007} · THM{Weak_CSRF_Role_001}.

**MITRE ATT&CK:** T1189 (Drive-by Compromise), T1098 (Account Manipulation), T1078 (Valid Accounts).

**Fuente:** [TryHackMe - CSRF Introduction](https://tryhackme.com/room/csrfintroduction)