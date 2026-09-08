# Hardening Basics Part 1

| **Dificultad** | Easy |
| **Tipo** | Endurecimiento (hardening) de sistemas |
| **Slug** | `hardeningbasicspart1` |
| **Link** | [TryHackMe](https://tryhackme.com/room/hardeningbasicspart1) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | sudo / /etc/sudoers / Grupos y usuarios / iptables / netfilter / ACLs |
| **Impacto** | Sala teórica de hardening: repasa la gestión de privilegios con sudo (grupos, usuarios, comandos permitidos y almacenamiento de contraseñas) y los fundamentos de los cortafuegos (tipos de firewall, zonas, netfilter, iptables y el principio de denegación implícita). |

---

**Contexto:** La sala introduce los conceptos básicos de endurecimiento (hardening) de sistemas. Cubre dos bloques principales: el control de privilegios con sudo (añadir usuarios al grupo sudo, consultar permisos con `sudo -l`, el archivo `/etc/sudoers`, los alias de grupo/usuario/comando y el archivo de contraseñas antiguas `opasswd`) y los cortafuegos (firewalls basados en red y en host, la zona desmilitarizada, el framework `netfilter`, las reglas de iptables con `--ctstate`, las cadenas Forward/Mangle y la regla final de denegación implícita).

## Solucionario

### Task 1: Introducción

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción al endurecimiento de sistemas. | `No answer needed` |

### Task 2: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 3: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 4: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 5: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 6: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 7: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 8: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 9: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 10: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 11: Cuestionario de sudo

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando se utiliza para ejecutar tareas con privilegios elevados? | `sudo` |
| 2 | ¿Qué comando añade al usuario "nick" al grupo sudo? | `usermod -aG sudo nick` |
| 3 | ¿Qué comando muestra los privilegios sudo del usuario actual? | `sudo -l` |
| 4 | ¿Qué archivo contiene la configuración de los permisos de sudo? | `/etc/sudoers` |
| 5 | ¿Qué palabra clave del archivo /etc/sudoers define un grupo? | `group` |
| 6 | ¿Qué palabra clave define un usuario permitido? | `User` |
| 7 | ¿Qué palabra clave define un comando permitido? | `Command` |
| 8 | ¿Cuál es la contraseña de sudo del usuario? | `yey` |
| 9 | ¿Cuántas veces puede el usuario hacer uso del privilegio concedido? | `8` |
| 10 | ¿Qué archivo almacena las contraseñas antiguas de los usuarios? | `opasswd` |
| 11 | ¿Qué principio de seguridad recomienda conceder únicamente los permisos mínimos necesarios? | `principle of least privilege` |

### Task 12: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 13: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 14: Conceptos previos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 15: Cuestionario de cortafuegos

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de firewall filtra el tráfico a nivel de red? | `Network-Based` |
| 2 | ¿Qué tipo de firewall protege únicamente un host individual? | `Host-Based` |
| 3 | ¿Qué zona aislada aloja los servidores expuestos a Internet? | `Demilitarized Zone` |
| 4 | ¿Qué framework del kernel de Linux proporciona el filtrado de paquetes? | `netfilter` |
| 5 | ¿Qué lista de reglas permite o deniega el tráfico? | `ACL` |
| 6 | ¿Qué flag de iptables filtra según el estado de la conexión? | `--ctstate` |
| 7 | ¿En qué cadena de iptables se procesan los paquetes que se reenvían? | `Forward` |
| 8 | ¿Qué cadena de iptables se utiliza para modificar los paquetes (por ejemplo, el TTL)? | `Mangle` |
| 9 | ¿Qué regla final deniega por defecto el tráfico no permitido explícitamente? | `implicit deny` |

---

**Metodología:** En el bloque de sudo se identifican los comandos para elevar privilegios, la adición de un usuario al grupo sudo, cómo consultar los permisos concedidos con `sudo -l` y la sintaxis del archivo `/etc/sudoers` (palabras clave `group`, `User` y `Command`), completando con el archivo de contraseñas históricas `opasswd` y el principio de mínimo privilegio. En el bloque de cortafuegos se clasifican los firewalls (basados en red o en host), se ubica la zona desmilitarizada, se comprende el framework `netfilter` de Linux y las reglas de iptables (estados con `--ctstate`, cadenas Forward y Mangle) hasta la política final de denegación implícita de todo lo no permitido.

**Learning chain:** gestión de privilegios (sudo) → configuración de /etc/sudoers → conceptos de firewalls → netfilter/iptables → regla de denegación implícita.

**MITRE ATT&CK:** T1548.003 (Abuse Elevation Control Mechanism: Sudo and Sudo Caching), T1548.004 (Abuse Elevation Control Mechanism: Elevated Execution with Prompt), T1562.004 (Impair Defenses: Disable or Modify System Firewall)

**Fuente:** [TryHackMe - Hardening Basics Part 1](https://tryhackme.com/room/hardeningbasicspart1)