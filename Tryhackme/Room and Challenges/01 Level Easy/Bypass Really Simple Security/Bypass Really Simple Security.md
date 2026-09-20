# Bypass Really Simple Security

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `bypassreallysimplesecurity` | [TryHackMe](https://tryhackme.com/room/bypassreallysimplesecurity) | 01 Level Easy | TryHackMe | WordPress, Really Simple Security, API REST, 2FA bypass, autenticación | Bypass de la autenticación y del 2FA en un sitio WordPress abusando de un endpoint REST del plugin |

---

**Contexto:** Sala centrada en una vulnerabilidad del plugin WordPress "Really Simple Security" que permite eludir la autenticación y el segundo factor. Se descubre un endpoint de la API interna del plugin (Rsssl_Two_Factor_On_Board_Api) y una función que expone información de usuario, completando el bypass de acceso. El resumen original conserva únicamente las respuestas posicionales del room, sin los enunciados de las preguntas.

## Solucionario

### Task 1: Descubrimiento de la API / API Discovery

**Explicación:** Se analiza el sitio para descubrir el namespace de la API REST interna del plugin y las funciones que expone, identificando el endpoint y la llamada que revela datos del usuario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Pregunta 2 no especificada en el original)* | `Rsssl_Two_Factor_On_Board_Api`<br>`check_login_and_get_user` |

### Task 2: Bypass de autenticación / Authentication Bypass

**Explicación:** Se abusa del endpoint descubierto para recuperar información del usuario administrador y completar la autenticación eludiendo el segundo factor, respondiendo a las preguntas de cierre del room.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Pregunta 1 no especificada en el original)* | `admin@fake.thm`<br>`3`<br>`POST` |
| 2 | *(Pregunta 2 no especificada en el original)* | `nay`<br>`No answer needed` |
| 3 | *(Pregunta 3 no especificada en el original)* | `No answer needed` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | *(Task 1, Pregunta 1 no especificada en el original)* | `No answer needed` |
| 2 | *(Task 1, Pregunta 2 no especificada en el original)* | `Rsssl_Two_Factor_On_Board_Api`<br>`check_login_and_get_user` |
| 3 | *(Task 2, Pregunta 1 no especificada en el original)* | `admin@fake.thm`<br>`3`<br>`POST` |
| 4 | *(Task 2, Pregunta 2 no especificada en el original)* | `nay`<br>`No answer needed` |
| 5 | *(Task 2, Pregunta 3 no especificada en el original)* | `No answer needed` |

---

**Metodología:** Reconocimiento del WordPress instalado → identificación del namespace REST `Rsssl_Two_Factor_On_Board_Api` → localización de la función `check_login_and_get_user` → explotación del endpoint para obtener datos del administrador → bypass del 2FA con peticiones POST → acceso completado.

### Cadena de ataque / Attack Chain

```text
WordPress → API REST interna → Rsssl_Two_Factor_On_Board_Api → check_login_and_get_user → datos del administrador (admin@fake.thm) → bypass 2FA (POST) → acceso
```

**Learning chain:** Fuzzing/análisis de rutas REST → descubrimiento del namespace del plugin → abuso de la función interna → bypass del 2FA → acceso no autorizado

**Lección:** *Las APIs internas expuestas por los plugins de seguridad pueden convertirse en la puerta de entrada: un endpoint de "onboarding" mal protegido permite saltarse toda la autenticación.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1078 (Valid Accounts), T1556.007 (Modify Authentication Process)

**Fuente:** [TryHackMe - Bypass Really Simple Security](https://tryhackme.com/room/bypassreallysimplesecurity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.