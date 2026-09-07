# Do Not Disturb

| **Dificultad** | Medium |
| **Tipo** | challenge |
| **Slug** | `hh-donotdisturb-84a45644` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/hh-donotdisturb-84a45644) |
| **Sección** | Hunt & Hack House |
| **Fuente** | THM |
| **Componentes** | session hijacking/raw disk access/privilege escalation |
| **Impacto** | Secuestro de sesiones activas y acceso a disco crudo para escalada de privilegios total |

---

**Contexto:** El lema "Do Not Disturb" es irónico: la máquina es vulnerable al secuestro de sesiones HTTP activas. Un atacante puede interceptar tokens de autenticación, explotar acceso directo a disco raw para recuperar credenciales cifradas y escalar privilegios hasta root, demostrando que la comodidad de una sesión persistente es también su mayor debilidad.

## Solucionario

### Task 1: User Flag

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user flag? | `THM{w4rm_s3ss10n_h1j4ck3d}` |

### Task 2: Root Flag

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the root flag? | `THM{r4w_d1sk_4cc3ss_w4s_t00_much}` |

---

**Metodología:** Se inicia con escaneo de puertos para identificar servicios web activos. Mediante análisis de tráfico se detectan sesiones HTTP activas que permiten session hijacking mediante interceptación de cookies o tokens. Una vez dentro del sistema se explota acceso a disco raw para extraer credenciales almacenadas en el sistema de archivos. Con las credenciales recuperadas se escala privilegios a root y se capturan ambas flags.

**Learning chain:** port scanning → web service discovery → session analysis → HTTP session hijacking → raw disk access → credential extraction → privilege escalation → user flag → root flag

**MITRE ATT&CK:** T1539 (Steal Web Session Cookie), T1005 (Data from Local System), T1003 (OS Credential Dumping), T1068 (Exploitation for Privilege Escalation)

**Fuente:** [TryHackMe - Do Not Disturb](https://tryhackme.com/r/room/hh-donotdisturb-84a45644)
