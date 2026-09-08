# Operation Slither

| **Dificultad** | Easy |
| **Tipo** | OSINT (caza de operadores) |
| **Slug** | `operationslitherIU` |
| **Link** | [TryHackMe](https://tryhackme.com/room/operationslitherIU) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | OSINT / Threads / Instagram / SoundCloud / GitHub / base64 / email (ProtonMail) / phishing infrastructure (Terraform, evilginx, GoPhish, Cobalt Strike) |
| **Impacto** | Sala de inteligencia de código abierto (OSINT) que simula la caza de los tres operadores del grupo de ciberdelincuentes "Sneaky Viper". Partiendo de un mensaje publicado en un foro, se cruza información entre redes sociales (Threads, Instagram), secciones de perfil, feeds de SoundCloud y repositorios de GitHub para identificar a cada operador y descifrar las flags (codificadas en base64 en los post). De paso, se observa la infraestructura de ataque anunciada: Terraform para phishing, evilginx, GoPhish, bypass de MFA de Google, scripts de fuerza bruta y payloads de evasión de EDR. |

---

**Contexto:** La sala plantea un escenario de OSINT: se ha obtenido acceso a un foro de hackers donde se venden datos de nuestra empresa. El primer post, firmado por `@v3n0mbyt3_`, anuncia la venta de la base de datos completa de usuarios de "TryTelecomMe" como parte de la "Operation Slither". Siguiendo el rastro, descubrimos que además de Twitter/X el operador usa otra plataforma (`Threads`) y, en su perfil, encontramos un mensaje en base64 que esconde la primera flag. El segundo post, publicado tras la eliminación de la cuenta en el foro, ofrece 60GB de datos lista para subastas; siguiendo el hilo desde la plataforma anterior se identifica al segundo operador (`_myst1cv1x3n_`), cuya presencia se rastrea por Instagram hasta un feed de SoundCloud con un prototipo que libera la segunda flag. El tercer post anuncia "advanced automation scripts" para infraestructura de phishing por $1500 y un contacto en ProtonMail; cruzando toda la información previa se llega a un repositorio de GitHub (author = `sh4d0wF4NG`) cuyo commit `red-team-infra` confirma la tercera flag.

## Solucionario

### Task 1: El Líder / The Leader

![Líder / The Leader](img/leader.png)

*Hemos obtenido acceso a un foro de hackers y encontramos información de nuestra empresa en venta. Todo lo que tenemos es este post. Encuentra cualquier información relacionada con el líder del grupo **Sneaky Viper**.*

**Inteligencia / Intel:**

```shell
Full user database TryTelecomMe on sale!!!

As part of Operation Slither, we've been hiding for weeks in their network and have now started to exfiltrate information.
This is just the beginning. We'll be releasing more data soon. Stay tuned!

@v3n0mbyt3_
```

**Explicación:** En el foro se vende la base de datos completa de "TryTelecomMe" firmada por `@v3n0mbyt3_`. Buscando ese handle se comprueba que el operador está en Twitter/X y además usa otra plataforma social. En el perfil de esa plataforma hay un enlace a un post con contenido ofuscado; **nota:** se debe decodificar de base64 para abordarlo. Fuente: https://www.threads.com/@_myst1cv1x3n_/post/C6G32WIvcJW

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Aparte de Twitter / X, ¿qué otra plataforma usa v3n0mbyt3_? (En minúsculas, formato `*******`) | `threads` |
| 2 | ¿Cuál es el valor de la flag? (formato `***{********_******_***_*****_********}`) | `THM{sl1th3ry_tw33tz_4nd_l34kr_r3pl13s!}` |

### Task 2: El Asistente / The Sidekick

![El Asistente / The Sidekick](img/sidekick.png)

*¡Un segundo mensaje se ha hecho público! Nuestra cuenta en el foro fue eliminada, así que no pudimos obtener el handle del operador esta vez. Sigue el rastro de la primera tarea y caza cualquier información relacionada con el segundo operador del grupo.*

**Inteligencia / Intel:**

```shell
60GB of data owned by TryTelecomMe is now up for bidding!

Number of users: 64500000 Accepting all types of crypto
For takers, send your bid on Threads via this handle:

HIDDEN CONTENT
```

**Explicación:** Siguiendo el rastro de la primera tarea y buscando en la plataforma descubierta antes (Threads), se encuentra al segundo operador que habla con `v3n0mbyt3_`: `_myst1cv1x3n_`. Su presencia se rastrea por Instagram y luego SoundCloud; revisando el prototipo en https://soundcloud.com/v1x3n-195859753/prototype2 sale la flag. **Nota:** el contenido del post vuelve a estar ofuscado en base64.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el nombre de usuario del segundo operador que habla con v3n0mbyt3 desde la plataforma anterior? (formato `_***********_`) | `_myst1cv1x3n_` |
| 2 | ¿Cuál es el valor de la flag? (formato `***{*******_******_******_********}`) | `THM{s0cm1nt_00ps3c_f1ng3r_m1scl1ck}` |

### Task 3: El Último Operador / The Last Operator

![El Último Operador / The Last Operator](img/lastop.png)

*Hay un nuevo post. Caza al tercer operador usando los descubrimientos pasados y encuentra detalles relacionados con la infraestructura utilizada para el ataque.*

**Inteligencia / Intel:**

```shell
FOR SALE

Advanced automation scripts for phishing and initial access!

Inclusions:
- Terraform scripts for a resilient phishing infrastructure
- Updated Google Phishlet (evilginx v3.0)
- GoPhish automation scripts
- Google MFA bypass script
- Google account enumerator
- Automated Google brute-forcing script
- Cobalt Strike aggressor scripts
- SentinelOne, CrowdStrike, Cortex XDR bypass payloads

PRICE: $1500
Accepting all types of crypto
Contact me on REDACTED@protonmail.com
```

**Explicación:** Cruzando mucha información previa (handles y plataformas descubiertas antes), la infraestructura anunciada lleva hasta el repositorio `red-team-infra`; su autoría revela el handle `sh4d0wF4NG` (plataforma `github`) y el análisis de la infraestructura libera la flag. **Nota:** para este reto hay que llegar hasta https://github.com/sh4d0wF4NG/red-team-infra/commit/78de1f17c45b994e97b8629aa7e5f42c31a0e7f7

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el handle del tercer operador? (formato `**********`) | `sh4d0wF4NG` |
| 2 | ¿Qué otra plataforma usa el tercer operador? (En minúsculas, formato `******`) | `github` |
| 3 | ¿Cuál es el valor de la flag? (formato `***{*****_*****_******_******_**}`) | `THM{sh4rp_f4ngz_l34k3d_bl00dy_pw}` |

---

## Resumen rápido

| Task | Pregunta | Respuesta |
| --- | --- | --- |
| 1 | 1 | `threads` |
| 1 | 2 | `THM{sl1th3ry_tw33tz_4nd_l34kr_r3pl13s!}` |
| 2 | 1 | `_myst1cv1x3n_` |
| 2 | 2 | `THM{s0cm1nt_00ps3c_f1ng3r_m1scl1ck}` |
| 3 | 1 | `sh4d0wF4NG` |
| 3 | 2 | `github` |
| 3 | 3 | `THM{sh4rp_f4ngz_l34k3d_bl00dy_pw}` |

---

**Metodología:** Recolección de señuelos desde el foro (posts), expansión por perfiles públicos (Threads/Instagram), plataformas de audio (SoundCloud) y repositorios de código (GitHub), decodificación base64 de los mensajes ofuscados y correlación cruzada de datos (handles, feeds, commits) para resolver cada operador y cada flag.

**Learning chain:** recolectar el post del foro → identificar el handle → buscar en plataformas sociales → seguir perfiles y enlaces (Instagram → SoundCloud, GitHub commits) → decodificar base64 → obtener flags.

**MITRE ATT&CK:** T1583.001 (Acquire Infrastructure: Domains), T1587.001 (Develop Capabilities: Malware), T1588.002 (Obtain Capabilities: Tool), T1591 (Gather Victim Org Information), T1539 (Steal Web Session Cookie)

**Fuente:** [TryHackMe - Operation Slither](https://tryhackme.com/room/operationslitherIU)