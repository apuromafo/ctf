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

**Explicación:** Presentación de la sala: endurecimiento (hardening) de sistemas, con foco en gestión de privilegios (sudo) y cortafuegos. Solo lectura.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción al endurecimiento de sistemas. | `No answer needed` |

### Task 2: Conceptos previos

**Explicación:** Apartado de lectura: define qué es el hardening y por qué se aplica de forma constante a los sistemas a lo largo de su ciclo de vida, no como un paso puntual.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 3: Conceptos previos

**Explicación:** Apartado de lectura: por qué la gestión de privilegios es el núcleo del hardening y el papel del comando `sudo` para delegar acciones administrativas de forma controlada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 4: Conceptos previos

**Explicación:** Apartado de lectura: cómo se organizan usuarios y grupos en Linux y por qué la adición al grupo `sudo` (via `usermod -aG sudo`) es la forma habitual de otorgar privilegios administrativos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 5: Conceptos previos

**Explicación:** Apartado de lectura: consulta de los permisos concedidos con `sudo -l` y la estructura del archivo de configuración `/etc/sudoers`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 6: Conceptos previos

**Explicación:** Apartado de lectura: sintaxis de las reglas de sudo con sus palabras clave `group`, `User` y `Command`, y el formato de las líneas de `/etc/sudoers`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 7: Conceptos previos

**Explicación:** Apartado de lectura: cómo sudo almacena las contraseñas en caché durante un tiempo (timestamp) y qué implica en cuanto a reusos del privilegio concedido.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 8: Conceptos previos

**Explicación:** Apartado de lectura: el archivo `opasswd`, que guarda contraseñas antiguas para impedir su reutilización inmediata.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 9: Conceptos previos

**Explicación:** Apartado de lectura: principio de mínimo privilegio aplicado a sudo y al resto de políticas de acceso del sistema.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 10: Conceptos previos

**Explicación:** Apartado de lectura: cierre del bloque de sudo y transición al bloque de conceptos de cortafuegos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 11: Cuestionario de sudo

**Explicación:** Cuestionario del bloque sudo: comandos (`sudo`, `usermod -aG sudo nick`, `sudo -l`), archivos de configuración (`/etc/sudoers`, `opasswd`), palabras clave del sudoers (`group`, `User`, `Command`), el reuso del privilegio (`8` veces) y el principio de mínimo privilegio.

```bash
usermod -aG sudo nick
sudo -l
visudo
```

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

**Explicación:** Apartado de lectura: tipos de cortafuegos (basados en red y basados en host) y el concepto de zonas de red.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 13: Conceptos previos

**Explicación:** Apartado de lectura: la zona desmilitarizada (DMZ) donde se colocan los servicios expuestos a Internet.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 14: Conceptos previos

**Explicación:** Apartado de lectura: el framework de filtrado de paquetes del kernel Linux (`netfilter`), sus tablas y las cadenas de iptables (Input, Output, Forward, Mangle...).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el material de la tarea. | `No answer needed` |

### Task 15: Cuestionario de cortafuegos

**Explicación:** Cuestionario del bloque cortafuegos: tipos (`Network-Based`, `Host-Based`), `Demilitarized Zone`, framework `netfilter`, listas de reglas `ACL`, filtrado por estado con `--ctstate`, cadenas `Forward` y `Mangle`, y la política final de `implicit deny`.

```bash
iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -P FORWARD DROP
```

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