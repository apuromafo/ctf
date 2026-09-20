# Capture!

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `capture` | [TryHackMe](https://tryhackme.com/room/capture) | 01 Level Easy | THM | Login form, oráculos de error, CAPTCHA aritmético, Python (requests), fuerza bruta | Medio |

---

**Contexto:** La room "Capture!" presenta una aplicación web de login vulnerable a fuerza bruta. El formulario responde con mensajes distintos según el usuario exista ("The user 'X' does not exist") o la contraseña sea incorrecta ("Invalid password for user 'X'"), lo que permite tratar la enumeración de usuarios y la fuerza bruta de contraseñas como dos fases independientes. Tras varios intentos fallidos se activa un rate limiter que exige resolver un CAPTCHA de operaciones aritméticas simples en texto plano, automatizable con un script.

> **ES:** App web con login explotable: se utilizan los oráculos de error para enumerar el usuario válido y después se fuerza bruta la contraseña, resolviendo con un script (Python/requests) el CAPTCHA aritmético regenerado en cada intento hasta acceder a la aplicación y leer flag.txt.

> **EN:** Exploitable web login: use the distinct error oracles to enumerate a valid username, then brute-force the password, while a Python/requests script auto-solves the regenerating arithmetic CAPTCHA on every attempt until the application and flag.txt are reached.

## Solucionario

### Task 1: General Information / Información general

**Explicación:** Task introductoria. SecureSolaCoders ha desarrollado de nuevo una aplicación web con un rate limiter propio en lugar de un WAF. Se deben descargar los ficheros de tarea (capture.zip), que contienen las listas usernames.txt y passwords.txt.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | I have downloaded the capture.zip file. | `No answer needed` |

### Task 2: Bypass the login form / Bypass del formulario de login

**Explicación:** Se accede a la aplicación en http://MACHINE_IP. La automatización se divide en dos fases: (1) enumeración del usuario válido comprobando que la respuesta NO contenga "The user 'X' does not exist"; (2) fuerza bruta de contraseñas sobre ese usuario comprobando que la respuesta NO contenga "Invalid password for user 'X'". En ambas fases hay que parsear y resolver el CAPTCHA aritmético incrustado en la respuesta (mensaje "Captcha enabled") antes de reenviar la petición.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What is the value of flag.txt? | `7df2eabce36f02ca8ed7f237f77ea416` |

---

**Metodología:** Escaneo de puertos → análisis del formulario de login → prueba manual de una credencial arbitraria para identificar los mensajes de error → automatización con Python/requests → detección y resolución del CAPTCHA con regex → enumeración de usuario por ausencia de "does not exist" → fuerza bruta de contraseña por ausencia de "Invalid password" → login → lectura de flag.txt.

### Cadena de ataque / Attack Chain

Reconocimiento del formulario → identificación de oráculos de error diferenciados → bypass del CAPTCHA aritmético → enumeración del usuario válido → fuerza bruta de contraseña → acceso a la aplicación → obtención de la flag.

**Learning chain:** Enumeración web → oráculos de respuesta → automatización con Python → parsing con regex → bypass de CAPTCHA → credential stuffing → captura de la flag.

**Lección:** *Los mensajes de error diferenciados convierten cualquier login en un oráculo de usuarios, un CAPTCHA en texto plano no frena la automatización y el control de acceso debería combinar mensajes genéricos, límite de intentos y retos no triviales.*

**MITRE ATT&CK:** T1110 (Brute Force), T1110.001 (Password Guessing), T1110.004 (Credential Stuffing).

**Fuente:** [TryHackMe - Capture!](https://tryhackme.com/room/capture)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.