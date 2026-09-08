# OWASP Top 10 2025: Application Design Flaws

| **Dificultad** | Easy |
| **Tipo** | Laboratorio web (OWASP Top 10 2025) |
| **Slug** | `owasptopten2025two` |
| **Link** | [TryHackMe](https://tryhackme.com/room/owasptopten2025two) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | OWASP Top 10 2025 / AS02 Security Misconfigurations / AS03 Software Supply Chain Failures / AS04 Cryptographic Failures / AS06 Insecure Design / API / curl / ffuf / AES / CyberChef / LFI |
| **Impacto** | Sala que cubre cuatro categorías del OWASP Top 10 2025 relacionadas con fallos de diseño y arquitectura de las aplicaciones, cada una con su reto práctico: AS02 Security Misconfigurations (errores verbosos que filtran información), AS03 Software Supply Chain Failures (uso de librerías de terceros sin verificar), AS04 Cryptographic Failures (claves AES hardcodeadas en el código) y AS06 Insecure Design (asunciones de diseño fallidas, como que solo los móviles accederán a la API). |

---

**Contexto:** La sala rompe con 4 categorías del OWASP Top 10 2025 que comparten una raíz común: fallos en los cimientos del diseño y la arquitectura. En el reto de AS02 se abusa de un endpoint de gestión de usuarios `/api/user/bad` para provocar un **errores verboso** y obtener la flag; en AS03 se explota un endpoint `/api/process` que invoca una librería vieja y sin verificar (`vulnerable_utils.py`) a través de su modo `debug`; en AS04 se encuentran credenciales criptográficas hardcodeadas en `static/js/decrypt.js` (`SECRET_KEY = "my-secret-key-16"` en modo ECB) que permiten descifrar el documento cifrado en Base64; y en AS06 se descubre que `SecureChat`, pese a asumir acceso solo desde móviles, expone la API `/api/messages/admin` sin autenticación, revelando la clave de acceso del panel de administración. El volcado original de la sala indica además que el flujo incluye un desafío que enseña que "Learn about A02, A03, A06, and A10 and how they relate to design flaws in the application".

## Solucionario

### Task 1: Introducción

**Explicación:** Presentación del módulo: se aprenden las categorías AS02, AS03, AS04 y AS06 del OWASP Top 10 2025 poniendo la teoría en práctica con retos. Antes de comenzar hay que desplegar la máquina práctica pulsando el botón "Start Machine".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Despliega la máquina virtual y accede a las aplicaciones de los retos. | `No answer needed` |

### Task 2: AS02: Security Misconfigurations

**Explicación:** Las configuraciones erróneas surgen cuando sistemas, servidores o aplicaciones se despliegan con defaults inseguros, ajustes incompletos o servicios expuestos (credenciales por defecto, buckets S3 abiertos, endpoints sin autenticación o mensajes de error verbosos). En el reto, navegando a `http://<IP>:5002/` encontramos una API de gestión de usuarios. Probando `/api/user/1` obtenemos JSON normal, pero el comentario "User ID must be numeric" sugiere probar un ID no numérico. Llamando a `/api/user/bad` el servidor filtra un traceback con la flag incrustada en el `debug_info`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag que se obtiene al provocar un error verboso en la API de usuarios (`/api/user/bad`)? | `THM{V3RB0S3_3RR0R_L34K}` |

### Task 3: AS03: Software Supply Chain Failures

**Explicación:** Los fallos de la cadena de suministro ocurren cuando la aplicación depende de componentes, librerías, servicios o modelos comprometidos, desactualizados o mal verificados (el ejemplo clásico es SolarWinds 2021). En el reto, la aplicación importa una librería local antigua `lib/vulnerable_utils.py`. Enviando `{"data": "debug"}` al endpoint `/api/process` (POST) se fuerza el modo debug de la librería, que devuelve `admin_token`, `internal_secret` y la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag que devuelve la librería vulnerable al enviar `{"data":"debug"}` al endpoint `/api/process`? | `THM{SUPPLY_CH41N_VULN3R4B1L1TY}` |

### Task 4: AS04: Cryptographic Failures

**Explicación:** Los fallos criptográficos aparecen cuando el cifrado se usa mal o no se usa: algoritmos débiles (MD5, SHA-1, ECB), claves hardcodeadas o mala gestión de secretos. En `http://<IP>:5004/` vemos un "Secure Document Viewer" con un documento cifrado. Inspeccionando el HTML se referencia `static/js/decrypt.js`, que contiene `const SECRET_KEY = "my-secret-key-16";`, `ENCRYPTION_MODE = "ECB"` y `KEY_SIZE = 128`, además del uso de `atob()` (Base64). Con esa clave, modo y tipo de cifrado se descifra el blob cifrado en CyberChef (AES-128-ECB), obteniendo la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag que se obtiene al descifrar el documento con la clave hardcodeada de `decrypt.js`? | `THM{CRYPTO_FAILURE_H4RDCOD3D_K3Y}` |

### Task 5: AS06: Insecure Design

**Explicación:** El diseño inseguro ocurre cuando hay lógica o arquitectura defectuosa desde el inicio (modelado de amenazas omitido, asunciones fallidas sobre usuarios o modelos, guardrails ausentes). En `http://<IP>:5005/`, "SecureChat" asume que solo los dispositivos móviles acceden a la aplicación. Mediante fuerza bruta de endpoints con `ffuf` (palabra clave `api-endpoints.txt`) y pruebas con `curl`, se descubre `/api/users` (que lista `admin`, `alice` y `bob`) y finalmente `/api/messages/admin`, que devuelve el "Admin panel access key" con la flag.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag del panel de administración accesible por diseño inseguro en `/api/messages/admin`? | `THM{1NS3CUR3_D35IGN_4SSUMPT10N}` |

### Task 6: Conclusión

**Explicación:** Los fallos AS02, AS03, AS04 y AS06 comparten una raíz común: cimientos débiles. La seguridad no se puede añadir al final; los sistemas fuertes empiezan con requisitos claros, asunciones de amenaza realistas, configuraciones controladas, dependencias verificadas y decisiones criptográficas sólidas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión y continúa con la siguiente sala del módulo. | `No answer needed` |

---

**Metodología:** Reconocimiento manual de cada API (exportar endpoints, probar valores), provocación deliberada de errores para extraer tracebacks, inspección de código fuente (HTML y JS) en busca de claves y lógica de negocio, fuerza bruta de endpoints con `ffuf`/`curl` y descifrado del blob con CyberChef utilizando la clave y modo encontrados.
**Learning chain:** despliegue de la máquina → enumeración de endpoints y parámetros → explotar errores verbosos (`AS02`) → abusar de librerías de terceros en modo debug (`AS03`) → localizar secretos hardcodeados y descifrar (`AS04`) → descubrir asunciones de diseño (API sin auth, `AS06`) → recopilar flags.
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1195.001 (Supply Chain Compromise: Software Supply Chain), T1210 (Exploitation of Remote Services), T1005 (Data from Local System), T1530 (Data from Cloud Storage Object)
**Fuente:** [TryHackMe - OWASP Top 10 2025: Application Design Flaws](https://tryhackme.com/room/owasptopten2025two)