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

**Explicación:** Desplegar y conectar a la máquina del room (app vulnerable). Tarea de introducción, sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - deploy and connect to the machine. | `No answer needed` |

### Task 2: Qué es CSRF

**Explicación:** CSRF abusa de que la app **confía** (trust) en que quien manda la petición es quien la ve (porque lleva la cookie). Tras el login, el navegador adjunta la **cookie** de sesión automáticamente a cada petición (la same-origin policy no impide enviar la cookie en peticiones cross-origin).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What relationship between the browser and the web application does a CSRF attack abuse? | `Trust` |
| 2 | What does the browser **automatically include** with requests after login? | `Cookies` |

### Task 3: Por Qué Funciona CSRF

**Explicación:** La acción debe **cambiar el estado** (state-changing) del recurso (cambiar email, password, rol...), no solo leer datos (safe request). Por eso las peticiones de escritura son las que interesan al atacante.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of action is usually required for a CSRF attack to succeed? | `State-changing` |

### Task 4: Encontrando Vulnerabilidades CSRF

**Explicación:** **POST** es la creencia errónea: un formulario HTML malicioso puede hacer POST igualmente. La defensa estándar son los **tokens anti-CSRF** (anti-CSRF tokens): un valor aleatorio ligado a la sesión que la app valida en las mutaciones (state-changing requests).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What HTTP request method do many developers incorrectly believe prevents CSRF? | `POST` |
| 2 | What mechanism is commonly used to protect applications from CSRF attacks? | `CSRF tokens` |

### Task 5: Explotación con un Formulario HTML

**Explicación:** La demo de email: una página vulnerable permite cambiar el email por GET/POST sin token. Preparas un HTML en tu máquina que pida cambiar el email:

```html
<form method="POST" action="http://MACHINE_IP/...">
    <input name="email" value="attacker@evilmail.thm">
    <input type="submit" value="Submit">
</form>
<script>document.forms[0].submit();</script>
```

Al abrirlo con la sesión activa (o con auto-submit) el email cambia → los dos flags según el email usado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag value after updating the email to `attacker@evilmail.thm`? | `THM{Got_The_Evil_Email001}` |
| 2 | What is the flag value after updating the email to `special@evilmail.thm`? | `THM{My_Special_Email007}` |

### Task 6: Explotación sobre Tokens Débiles

**Explicación:** El endpoint de cambio de rol lleva un token CSRF pero **predecible** (en realidad un user-id/base64); se reutiliza/craftea y se demota al admin de admin a staff → flag en el dashboard. La "aleatoriedad" del token era engañosa: estaba codificado en **base64**, por lo que se puede decodificar y forjar. ***Base64 no es seguridad*** — solo encoding.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag value after demoting the user from **admin to staff**? (visit the dashboard) | `THM{Weak_CSRF_Role_001}` |
| 2 | In the above example, what is the name of the encoding scheme used by the developer for encoding **CSRF tokens**? | `base64` |

### Task 7: Buenas Prácticas

**Explicación:** Buenas prácticas: tokens anti-CSRF fuertes y aleatorios, cookies `SameSite=Strict/Lax`, comprobar `Origin`/`Referer` en peticiones sensibles, y mínimo privilegio. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - best practices understood. | `No answer needed` |

### Task 8: Conclusión

**Explicación:** Resumen: CSRF explota confianza+cookies; la defensa es tokens robustos y cookies SameSite. *El navegador no es el usuario.* Confiar solo en la cookie = confiar en cualquiera que sepa hacer un GET/POST.

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