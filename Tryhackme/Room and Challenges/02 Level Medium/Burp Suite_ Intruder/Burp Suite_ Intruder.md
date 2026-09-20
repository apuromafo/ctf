# Burp Suite_ Intruder
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `burpsuiteintruder` |
| **Link** | [TryHackMe](https://tryhackme.com/room/burpsuiteintruder) |
| **Sección** | Web / Burp Suite |
| **Fuente** | Writeup de Cajac (GitHub) y Kevinovitz |
| **Componentes** | Burp Suite Intruder, payload positions (§), attack types (Sniper, Battering Ram, Pitchfork, Cluster Bomb), Community vs Pro (300 payloads, 1 thread), HTTP POST login brute force, timing attacks, JSON base64 |
| **Impacto** | Sala Medium de Burp Suite: aprender Intruder (posiciones con §, tipos de ataque, límites Community/Pro), automatizar una fuerza bruta de login y resolver el reto final de autenticación probando tiempos de respuesta. |
---
**Contexto:** Esta sala explica en profundidad la herramienta Intruder de Burp Suite: qué son las posiciones de payload (delimitadas con `§`), los distintos tipos de ataque (Sniper, Battering Ram, Pitchfork, Cluster Bomb) y las diferencias de licencia (Community: máximo 300 payloads por ataque y 1 solo hilo; Pro: ilimitado). La parte práctica automatiza una fuerza bruta sobre un formulario de login y abusa de los tiempos de respuesta del servidor para detectar la contraseña correcta.
*EN: This room dives deeply into Burp Suite's Intruder tool: payload positions (delimited with `§`), attack types (Sniper, Battering Ram, Pitchfork, Cluster Bomb) and license differences (Community: max 300 payloads per attack and a single thread; Pro: unlimited). The practical part automates a login brute force and abuses server response timings to spot the correct password.*
## Solucionario
### Task 1 — Introduction
**Explicación:** Presentación de la sala sobre Burp Suite Intruder, la herramienta para automatizar peticiones repetitivas (fuerza bruta, fuzzing). Sin pregunta con respuesta.
*EN: Room introduction about Burp Suite Intruder, the tool for automating repetitive requests (brute force, fuzzing). No answer needed.*
### Task 2 — Positions
**Explicación:** Intruder modifica "posiciones" dentro de una petición, que son los puntos donde se inyectarán los payloads. En la pestaña Positions se marcan con los caracteres `§` (para añadir o quitar tienes botones dedicados).
*EN: Intruder modifies "positions" inside a request, the insertion points where payloads will be injected. In the Positions tab they are marked with the `§` characters (dedicated buttons add or clear them).*
### Task 3 — Payload Positions
**Explicación:** Los delimitadores `§` son los que indican a Intruder dónde empieza y dónde termina cada posición de payload dentro de la petición.
*EN: The `§` delimiters tell Intruder where each payload position starts and ends inside the request.*
### Task 4 — Attack Types
**Explicación:** Los tipos de ataque determinan cómo se combinan posiciones y payloads. Para una única posición, `Sniper` itera los payloads uno a uno; cuando se quiere añadir un sufijo o prefijo fijo se usa la funcionalidad de "Add suffix/prefix", y con múltiples posiciones aparecen Battering Ram, Pitchfork y Cluster Bomb. La opción de añadir un valor al final/principio se llama "Add suffix".
*EN: Attack types define how positions and payloads are combined. For a single position, `Sniper` iterates payloads one by one; to append or prepend a fixed value you use the "Add suffix/prefix" feature, and with multiple positions you get Battering Ram, Pitchfork and Cluster Bomb. The option that adds a value at the end is called "Add suffix".*
### Task 5 — Attack Types for Open-Source
**Explicación:** El tipo de ataque por defecto de Intruder es `Sniper`, que funciona con una única posición de payload y lanza peticiones secuenciales usando cada payload de la lista.
*EN: Intruder's default attack type is `Sniper`, which works with a single payload position and fires sequential requests using each payload from the list.*
### Task 6 — Resource Pools
**Explicación:** Las licencias limitan el uso de Intruder: la edición Community permite un máximo de 300 payloads por ataque y restringe a 1 el número de hilos abiertos; la Professional no tiene esos límites.
*EN: Licenses limit Intruder usage: the Community edition allows a maximum of 300 payloads per attack and restricts the number of open threads to 1; Professional has no such limits.*
### Task 7 — Workflow
**Explicación:** El flujo de trabajo con Intruder: enviar la petición a Intruder, marcar posiciones, configurar el payload (diccionario), elegir ataque y lanzar. Para el formulario de login de ejemplo, el cuerpo del POST es `username=admin&password=admin`.
*EN: The Intruder workflow: send the request to Intruder, set positions, configure the payload (wordlist), pick an attack type and launch. For the sample login form, the POST body is `username=admin&password=admin`.*
### Task 8 — Passwords & Usernames
**Explicación:** Para el primer ejercicio, se usa una lista de 20 usuarios como payload. El objetivo es descubrir qué credenciales son válidas analizando las respuestas del servidor.
*EN: For the first exercise a wordlist of 20 usernames is used as the payload, aiming to discover valid credentials by analysing server responses.*
### Task 9 — Timing Attacks
**Explicación:** El servidor tarda un tiempo mucho mayor (6000 ms) cuando la contraseña es correcta que cuando falla. Ordenando los resultados por tiempo de respuesta se identifica el par usuario:contraseña ganador. Esta es la base del ataque temporal (timing).
*EN: The server takes much longer (6000 ms) when the password is correct than when it fails. Sorting results by response time reveals the winning username:password pair. This is the basis of the timing attack.*
### Task 10 — Params
**Explicación:** Aplicando el ataque de tiempos sobre el formulario con los parámetros del login, se obtiene el par `m.rivera:letmein1` para el usuario m.rivera.
*EN: Applying the timing attack to the login form parameters yields the pair `m.rivera:letmein1` for user m.rivera.*
### Task 11 — Burp Intruder Challenge
**Explicación:** Reto final: se debe repetir la técnica (Sniper + conteo/timing) sobre el nuevo formulario de login. La contraseña correcta devuelve la bandera del reto. La segunda pregunta es de comprobación sin respuesta.
*EN: Final challenge: repeat the technique (Sniper + counting/timing) on the new login form. The correct password returns the challenge flag. The second question is a check-in with no answer.*

```bash
# Flujo en Burp Suite:
# 1) Enviar POST /login a Intruder (Ctrl+I)
# 2) Marcar posición del parámetro con § username=§admin§&password=admin
# 3) Payloads: userlist.txt / passwordlist.txt
# 4) Tipo: Sniper ; ordenar respuestas por length/time
```
### Task 12 — Params
**Explicación:** Repitiendo la técnica sobre el usuario o.bennett se obtiene el par `o.bennett:bella1`.
*EN: Repeating the technique on user o.bennett yields the pair `o.bennett:bella1`.*
### Task 13 — Practice Time (Bonus)
**Explicación:** Ejercicio extra opcional de consolidación de lo aprendido. Sin pregunta con respuesta.
*EN: Optional bonus exercise to consolidate what was learned. No answer needed.*
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does the word "Positions" refer to in the context of Burp Intruder? | `Positions` |
| 2 | What symbol is used to mark the start and end of a payload position in Intruder? | `§` |
| 3 | What is the name of the option that allows adding a value at the end/beginning of a payload? | `Add suffix` |
| 4 | What is the name of the default attack type used by Intruder? | `Sniper` |
| 5 | What is the maximum number of payloads allowed per attack in the Community edition? | `300` |
| 6 | To how many is the number of open threads limited in the Community edition? | `1` |
| 7 | What is the body of the HTTP POST request used to authenticate to the login form? | `username=admin&password=admin` |
| 8 | How many usernames are there in the userlist used for the brute force? | `20` |
| 9 | When the correct password is submitted, how long (in milliseconds) does the server take to respond? | `6000` |
| 10 | What is the valid username:password pair found for m.rivera? | `m.rivera:letmein1` |
| 11 | What is the name of the attack type used in the final challenge? | `Sniper` |
| 12 | What is the flag obtained in the Burp Intruder final challenge? | `THM{MTMxNTg5NTUzMWM0OWRlYzUzMDVjMzJl}` |
| 13 | What is the valid username:password pair found for o.bennett? | `o.bennett:bella1` |
---
**Metodología:** Recibir la petición del formulario en Burp → enviarla a Intruder → marcar posiciones con `§` → elegir tipo de ataque (Sniper) y lista de payloads (usuarios/contraseñas) → lanzar y clasificar resultados por tamaño/tiempo de respuesta → ataque de timing (6000 ms) para identificar la contraseña correcta → capturar bandera en el reto final.
**Learning chain:** payload positions → attack types → límites de licencia (Community vs Pro) → force bruta de formularios con Intruder → timing attacks → autenticación y bandera.
**Lección:** *Intruder no solo lanza diccionarios: ordenar las respuestas por longitud o por tiempo de respuesta convierte una fuerza bruta ciega en un ataque de timing que revela la credencial correcta entre miles.*
**MITRE ATT&CK:** T1110 (Brute Force), T1110.004 (Credential Stuffing), T1078 (Valid Accounts), T1029, T1059.
**Fuente:** [TryHackMe - Burp Suite_ Intruder](https://tryhackme.com/room/burpsuiteintruder)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.