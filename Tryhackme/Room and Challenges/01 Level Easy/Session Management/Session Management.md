# Session Management

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `sessionmanagement` | [TryHackMe](https://tryhackme.com/room/sessionmanagement) | `01 Level Easy` | THM | Session management, cookies, authentication, authorization, accountability | Resolución completa del reto de gestión de sesiones |

---

**Contexto:** Room sobre gestión de sesiones en aplicaciones web: se repasan los estados de la sesión (creación, seguimiento, expiración y terminación), los principios de accountability, autenticación y autorización, y los mecanismos técnicos como la cookie secure, la cabecera Set-Cookie y esquemas como Authorization: Bearer. La última tarea aplica esos conceptos sobre una app objetivo.

> **ES:** Gestión de sesiones web: ciclo de vida de la sesión, accountability/autenticación/autorización y mecanismos como cookies secure, Set-Cookie y Authorization: Bearer.
> **EN:** Web session management: session lifecycle, accountability/authentication/authorization and mechanisms such as secure cookies, Set-Cookie and Authorization: Bearer.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea inicial de la room: se comienza el recorrido sin necesidad de respuesta.

1. No answer needed

### Task 2: Ciclo de vida de la sesión / Session lifecycle

**Explicación:** Se ordenan los estados del ciclo de vida de una sesión: terminación, creación, seguimiento y expiración.

1. Session Termination
2. Session Creation
3. Session Tracking
4. Session Expiry

### Task 3: Responsabilidad y control / Accountability and control

**Explicación:** Se identifican los principios implicados en la gestión de sesiones: accountability (rendición de cuentas), autenticación y autorización.

1. Accountability
2. Authentication
3. Authorisation

### Task 4: Mecanismos técnicos / Technical mechanisms

**Explicación:** Se enumeran los mecanismos técnicos empleados: la flag secure de la cookie, la cabecera Set-Cookie y el esquema Authorization: Bearer.

1. secure
2. Set-Cookie
3. Authorization: Bearer

### Task 5: Aplicación de la teoría / Applying the theory

**Explicación:** Se aplican los conceptos anteriores sobre un ejemplo práctico: creación, terminación y seguimiento de sesión, respondiendo con los estados que corresponden.

1. Session Creation
2. Session Termination
3. Session Tracking
4. Session Creation

### Task 6: Aplicación práctica / Practical application

**Explicación:** Se resuelve la parte práctica sobre la aplicación objetivo: se obtiene la flag del usuario de sesión THM{Got.the.User} y se responden los valores numéricos y las opciones y/n solicitadas.

1. THM{Got.the.User}
2. 1
3. 3
4. 4
5. 3
6. y,n,n

### Task 7: Cierre / Wrap-up

**Explicación:** Conclusión de la room: no requiere respuesta.

7. No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1.1 | Arranque de la room | `No answer needed` |
| 2.1 | Estado de terminación de la sesión | `Session Termination` |
| 2.2 | Estado de creación de la sesión | `Session Creation` |
| 2.3 | Estado de seguimiento de la sesión | `Session Tracking` |
| 2.4 | Estado de expiración de la sesión | `Session Expiry` |
| 3.1 | Principio de rendición de cuentas | `Accountability` |
| 3.2 | Principio de verificación de identidad | `Authentication` |
| 3.3 | Principio de concesión de permisos | `Authorisation` |
| 4.1 | Indicador de cookie solo HTTPS | `secure` |
| 4.2 | Cabecera de establecimiento de cookie | `Set-Cookie` |
| 4.3 | Esquema de autorización con token | `Authorization: Bearer` |
| 5.1 | Estado aplicado en el ejemplo 1 | `Session Creation` |
| 5.2 | Estado aplicado en el ejemplo 2 | `Session Termination` |
| 5.3 | Estado aplicado en el ejemplo 3 | `Session Tracking` |
| 5.4 | Estado aplicado en el ejemplo 4 | `Session Creation` |
| 6.1 | Flag de usuario de la sesión | `THM{Got.the.User}` |
| 6.2 | Valor numérico 1 | `1` |
| 6.3 | Valor numérico 2 | `3` |
| 6.4 | Valor numérico 3 | `4` |
| 6.5 | Valor numérico 4 | `3` |
| 6.6 | Opciones sí/no | `y,n,n` |
| 7.1 | Cierre de la room | `No answer needed` |

---

**Metodología:** 1) Repasar el ciclo de vida de una sesión web. 2) Vincular accountability, autenticación y autorización. 3) Reconocer los mecanismos técnicos (cookie secure, Set-Cookie, Bearer). 4) Aplicar los estados en ejemplos. 5) Resolver la app objetivo, obtener la flag y responder valores numéricos y booleanos.

### Cadena de ataque / Attack Chain

```text
Introducción -> ciclo de vida de sesión (Termination/Creation/Tracking/Expiry) -> Accountability/Authentication/Authorisation -> secure + Set-Cookie + Authorization: Bearer -> aplicación de estados -> THM{Got.the.User} -> valores (1, 3, 4, 3) y opciones (y,n,n) -> cierre
```

**Learning chain:** Session lifecycle -> principios de control (accountability, authN, authZ) -> mecanismos de cookies y tokens -> aplicación práctica -> flag de usuario y respuestas

**Lección:** *Gestionar bien una sesión exige controlar todo su ciclo de vida y emplear mecanismos seguros (cookies secure, cabeceras correctas y tokens); sin ello, las sesiones pueden ser secuestradas o mal autorizadas.*

**MITRE ATT&CK:** N/A (Fundamentos de gestión de sesiones web), T1110.001 (Password Guessing), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Session Management](https://tryhackme.com/room/sessionmanagement)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.