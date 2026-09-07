# CSRF Introduction [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `csrfintroduction`
* **Link:** https://tryhackme.com/room/csrfintroduction
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + máquina/vulnerable web app del room
* **Componentes:** CSRF (Cross-Site Request Forgery) · cookies/sesión · métodos HTTP · tokens anti-CSRF (base64) · demos: cambio de email y demote de rol/admin
* **Impacto rol:** Entender CSRF: qué relación explota (la confianza del navegador en la app), por qué funciona (el navegador envía las cookies automáticamente), qué defensa hay (tokens) y cómo encodear de forma segura los tokens. Es un clásico de OWASP Top 10.

## Solucionario de Tareas / Task Solutions

> **ES:** CSRF abusa de la **relación de confianza** entre el navegador y la aplicación web: tras el login, el navegador incluye automáticamente las **cookies** de sesión en cada petición. Si la app recibe una petición con cookie válida, no sabe si la inició el usuario o un sitio malicioso. El ataque necesita una **acción que cambie el estado** (state-changing: cambiar email, password, rol...), porque leer datos con GET es "inofensivo" desde CSRF. Muchos desarrolladores creen erróneamente que **POST** la evita, pero el atacante solo necesita un formulario web que haga POST. La defensa estándar son los **tokens anti-CSRF**; si el token es débil/predicable (aquí codificado en **base64**), el ataque sigue funcionando. El lab demuestra los dos casos: actualizar el email de una cuenta y demotar a un admin, con flags por cada demo.
> **EN:** CSRF abuses the **trust relationship** between the browser and the web app: after login, the browser automatically includes the **session cookies** in every request. If the app receives a request with a valid cookie it can't tell whether the user or a malicious site initiated it. The attack needs a **state-changing action** (change email, password, role...), because reading data via GET is CSRF-immune. Many developers wrongly believe **POST** prevents it, but an attacker only needs an HTML form that POSTs. The standard defence is **anti-CSRF tokens**; if the token is weak/predictable (here encoded in **base64**), the attack still works. The lab demonstrates both cases — updating an account email and demoting an admin — with a flag per demo.

### Task 1 — Introducción / Introduction *(vm)*

* **Check:** `I have successfully connected to the machine.`
* **ES:** Desplegar y conectar a la máquina del room.
* **EN:** Deploy and connect to the room's machine.

### Task 2 — Qué es CSRF / What is CSRF

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What relationship between the browser and the web application does a CSRF attack abuse? | `Trust` |
| What does the browser **automatically include** with requests after login? | `Cookies` |

* **Confianza / Trust:** CSRF abusa de que la app confía en que quien manda la petición es quien la ve (porque lleva la cookie).
* **Cookies:** tras el login, el navegador adjunta la cookie de sesión automáticamente a cada petición (same-origin policy no lo impide para peticiones con cookie).

### Task 3 — Por Qué Funciona CSRF / Why CSRF Works

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What type of action is usually required for a CSRF attack to succeed? | `State-changing` |

* **Estado / State:** la acción debe **cambiar el estado** del recurso (state-changing), no solo leer datos (safe request).

### Task 4 — Encontrando Vulnerabilidades CSRF / Finding CSRF Vulnerabilities

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What HTTP request method do many developers incorrectly believe prevents CSRF? | `POST` |
| What mechanism is commonly used to protect applications from CSRF attacks? | `CSRF tokens` |

* **POST:** la creencia errónea; un formulario HTML malicioso puede hacer POST igualmente.
* **Defensa / Defence:** tokens anti-CSRF (anti-CSRF tokens): valor aleatorio ligado a la sesión que la app valida en mutaciones.

### Task 5 — Explotación con un Formulario HTML / Exploitation using HTML Form

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag value after updating the email to `attacker@evilmail.thm`? | `THM{Got_The_Evil_Email001}` |
| What is the flag value after updating the email to `special@evilmail.thm`? | `THM{My_Special_Email007}` |

* **Demo email:** una página vulnerable permite cambiar el email por GET/POST sin token. Preparas un HTML en tu máquina que pida cambiar el email:
  ```html
  <form method="POST" action="http://MACHINE_IP/...">
      <input name="email" value="attacker@evilmail.thm">
      <input type="submit" value="Submit">
  </form>
  <script>document.forms[0].submit();</script>
  ```
  Al abrirlo con la sesión activa (o con auto-submit) el email cambia → los dos flags según el email usado.

### Task 6 — Explotación sobre Tokens Débiles / Exploitation over Weak Tokens

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag value after demoting the user from **admin to staff**? (visit the dashboard) | `THM{Weak_CSRF_Role_001}` |
| In the above example, what is the name of the encoding scheme used by the developer for encoding **CSRF tokens**? | `base64` |

* **Demote:** el endpoint de cambio de rol lleva un token CSRF pero **predecible** (en realidad un user-id/base64); lo reutilizas/crafteas y demotas al admin → flag en el dashboard.
* **Encoding:** la "aleatoriedad" del token era engañosa: estaba codificado en **base64** → se puede decodificar/forjar. ***Base64 no es seguridad*.**

### Task 7 — Buenas Prácticas / Best Practices

* **Check:** `I have understood the best practices.`
* **ES:** Buenas prácticas: tokens anti-CSRF fuertes y aleatorios, SameSite=Strict/Lax cookies, comprobar Origin/Referer en peticiones sensibles, mínimo privilegio.
* **EN:** Best practices: strong random anti-CSRF tokens, SameSite=Strict/Lax cookies, Origin/Referer checks on sensitive requests, least privilege.

### Task 8 — Conclusión / Conclusion

* **Check:** `I have successfully completed the room.`
* **ES:** Resumen: CSRF explota confianza+cookies; la defensa es tokens robustos y cookies SameSite.
* **EN:** Summary: CSRF exploits trust+cookies; the defence is robust tokens and SameSite cookies.

## Metodología / Methodology

1. **Paso / Step:** Desplegar la app vulnerable y autenticarse.
2. **Paso / Step:** Revisar con Burp (o el proxy que prefieras) cómo se envían las peticiones de cambio de email/rol (método, cookies, token).
3. **Paso / Step:** Explotar la demo de email con un formulario propio (harvesting de los 2 flags).
4. **Paso / Step:** En la demo de roles, forjar/decodificar el token débil (base64) y demotar al admin → flags.
5. **Paso / Step:** Completar las preguntas teóricas (T2–T4) con las secciones del room.

### Cadena de ataque / Attack Chain

```
víctima autenticada (cookie de sesión válida)
  -> el navegador envía cookies automáticamente (trust)
  -> página maliciosa abre / auto-submit de formulario
  -> petición state-changing (cambio email / cambio rol)
  -> sin token o token débil (base64 forjable)
  -> flags: THM{Got_The_Evil_Email001} · THM{My_Special_Email007} · THM{Weak_CSRF_Role_001}
```

**Mapeo MITRE ATT&CK:** T1189 (Drive-by Compromise) como vector de entrega del form · T1534/uso de credenciales no aplica · impacto: T1098 (Account Manipulation) / T1484 (Domain Policy). Defensa: CWE-352 (Cross-Site Request Forgery) del OWASP Top 10.

**Lección:** *El navegador no es el usuario.* Confiar solo en la cookie = confiar en cualquiera que sepa hacer un GET/POST. Tokens fuertes + SameSite + verificación de Origin.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.