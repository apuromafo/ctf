# Do Not Disturb

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | challenge | `hh-donotdisturb-84a45644` | [TryHackMe](https://tryhackme.com/room/hh-donotdisturb-84a45644) | Hunt & Hack House | THM | session hijacking / raw disk access / privilege escalation | Secuestro de sesiones activas y acceso a disco crudo para escalada de privilegios total |

> **Objeto:** Comprometer la máquina apoderándose de una sesión HTTP activa (session hijacking), explotar el acceso directo al disco raw para recuperar credenciales cifradas y escalar privilegios hasta root para capturar las dos flags del laboratorio.

---

**Contexto:** El lema "Do Not Disturb" es irónico: la máquina es vulnerable al secuestro de sesiones HTTP activas. Un atacante puede interceptar tokens de autenticación, explotar acceso directo a disco raw para recuperar credenciales cifradas y escalar privilegios hasta root, demostrando que la comodidad de una sesión persistente es también su mayor debilidad.

> **ES:** Lab de la serie Hunt & Hack House (nivel Medium) vulnerable al secuestro de sesiones HTTP activas. El camino es: escaneo de puertos, detección de sesiones activas e interceptación de cookies/tokens (session hijacking) para acceder al sistema; explotación del acceso al disco raw para extraer credenciales del sistema de archivos y escalada de privilegios hasta root para obtener la flag de usuario y la de root.
> **EN:** A Hunt & Hack House lab (Medium) vulnerable to active HTTP session hijacking. The path is: port scanning, detection of active sessions and cookie/token interception (session hijacking) to get in; raw disk access exploitation to extract credentials from the filesystem, and privilege escalation to root to retrieve the user and root flags.

## Solucionario

### Task 1: User Flag / Flag de usuario
**Explicación:** Tras escanear puertos e identificar los servicios web, se analiza el tráfico HTTP y se detectan sesiones activas. Interceptando la cookie o el token de una sesión legítima (session hijacking) se accede a la máquina como el usuario comprometido y se captura la flag de usuario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? / ¿Cuál es la flag de usuario? | `THM{w4rm_s3ss10n_h1j4ck3d}` |

### Task 2: Root Flag / Flag de root
**Explicación:** Con acceso inicial, se explota el acceso directo al disco crudo (raw disk access) para leer el sistema de archivos fuera del control del kernel y recuperar credenciales almacenadas o cifradas. Con esas credenciales se escala privilegios a root y se captura la flag de root.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the root flag? / ¿Cuál es la flag de root? | `THM{r4w_d1sk_4cc3ss_w4s_t00_much}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? / ¿Cuál es la flag de usuario? | `THM{w4rm_s3ss10n_h1j4ck3d}` |
| 2 | What is the root flag? / ¿Cuál es la flag de root? | `THM{r4w_d1sk_4cc3ss_w4s_t00_much}` |

---

**Metodología:** Se inicia con escaneo de puertos para identificar servicios web activos. Mediante análisis de tráfico se detectan sesiones HTTP activas que permiten session hijacking mediante interceptación de cookies o tokens. Una vez dentro del sistema se explota acceso a disco raw para extraer credenciales almacenadas en el sistema de archivos. Con las credenciales recuperadas se escala privilegios a root y se capturan ambas flags.

### Cadena de ataque / Attack Chain

```text
nmap (puertos/servicios) -> análisis de tráfico HTTP -> detección de sesiones activas -> interceptación de cookie/token -> acceso como usuario legítimo -> raw disk access -> extracción de credenciales -> privilege escalation -> root -> user flag + root flag
```

**Learning chain:** port scanning → web service discovery → session analysis → HTTP session hijacking → raw disk access → credential extraction → privilege escalation → user flag → root flag

**Lección:** *Las sesiones HTTP persistentes sin protección son una superficie de ataque crítica: un token interceptado equivale al control de la cuenta. Además, el acceso al disco raw puede eclipsar los mecanismos de cifrado del sistema y entregar las credenciales al atacante.*

**MITRE ATT&CK:** T1539 (Steal Web Session Cookie), T1005 (Data from Local System), T1003 (OS Credential Dumping), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Do Not Disturb](https://tryhackme.com/room/hh-donotdisturb-84a45644)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.