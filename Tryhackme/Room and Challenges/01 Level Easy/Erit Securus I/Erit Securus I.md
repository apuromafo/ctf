# Erit Securus I

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `eritsecurusi` | [TryHackMe - Erit Securus I](https://tryhackme.com/room/eritsecurusi) | `01 Level Easy` | THM | nmap, Bolt CMS, exploit python, sudo, /usr/bin/zip, privesc | Exploitation — compromiso total de la máquina |

> **Objeto:** Pwnear la máquina Erit Securus I explotando el CMS Bolt, ganar acceso como www-data, pivotar al usuario jsmith y escalar a root para capturar las banderas.

---

**Contexto:** Erit Securus I es una máquina CTF de nivel inicial. El camino de explotación comienza con un escaneo de puertos, continúa con una aplicación web basada en Bolt CMS vulnerable, la ejecución de un exploit en Python para obtener una shell como www-data, el hallazgo de credenciales, y una escalada de privilegios final mediante un binario sudo mal configurado (/usr/bin/zip) que desemboca en acceso root total.

> **ES:** Máquina CTF: escaneo de puertos (22,80), detección de Bolt CMS, exploit en Python, shell como www-data, credencial del usuario jsmith y escalada a root vía `/usr/bin/zip` con sudo NOPASSWD.
>
> **EN:** CTF box: port scanning (22,80), Bolt CMS detection, Python exploit, www-data shell, jsmith user credentials and root escalation via NOPASSWD `/usr/bin/zip`.

## Solucionario

### Task 1: Preparación / Preparation

**Explicación:** Se despliega la máquina y se prepara el entorno de trabajo para iniciar la fase de reconocimiento.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Preparación del laboratorio | `No answer needed` |

### Task 2: Escaneo de puertos / Port Scanning

**Explicación:** Se realiza un escaneo de la máquina para identificar los servicios expuestos y los puertos abiertos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos puertos abiertos hay? | `2` |
| 2 | ¿Qué puertos están abiertos? | `22,80` |

### Task 3: Reconocimiento web / Web Reconnaissance

**Explicación:** Se enumera la aplicación web para identificar la tecnología detrás del servicio HTTP.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué CMS/CMS-tecnología corre la web? | `Bolt` |

### Task 4: Explotación de la aplicación / Application Exploitation

**Explicación:** Se identifica una vulnerabilidad conocida en la versión del CMS y se explota mediante un script Python para lograr ejecución de código.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lenguaje del exploit utilizado | `python` |
| 2 | Ejecución del exploit / payload | `No answer needed` |

### Task 5: Obtención de acceso inicial / Initial Access

**Explicación:** Tras ejecutar el exploit se obtiene una shell en la máquina bajo el contexto del servicio web.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Con qué usuario se obtiene la shell? | `www-data` |

### Task 6: Credenciales y primera bandera / Credentials and First Flag

**Explicación:** Se localizan credenciales válidas dentro del sistema que permiten acceder a otro usuario del equipo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Contraseña encontrada | `snickers` |
| 2 | Bandera obtenida | `THM{Hey!_Welcome_in}` |

### Task 7: Escalada al usuario jsmith / jsmith Escalation

**Explicación:** Al acceder como el usuario jsmith se descubre un binario con privilegios sudo sin contraseña que puede aprovecharse para escalar privilegios.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué binario puede ejecutar jsmith con sudo? | `(jsmith) NOPASSWD: /usr/bin/zip` |

### Task 8: Segunda bandera / Second Flag

**Explicación:** Se utiliza el binario sudo para escalar privilegios y se obtiene una bandera intermedia del compromiso.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Bandera obtenida tras la escalada | `THM{Welcome_Home_Wile_E_Coyote!}` |

### Task 9: Escalada a root / Root Escalation

**Explicación:** Finalmente se consigue elevar todos los privilegios del usuario actual a una sesión root completa, capturando la bandera final de la máquina.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Privilegios sudo del usuario tras la escalada | `(ALL : ALL) NOPASSWD: ALL` |
| 2 | Bandera final de root | `THM{Great_work!_You_pwned_Erit_Securus_1!}` |

---

**Metodología:** Se realiza reconocimiento con nmap sobre el host objetivo (22,80), se enumera la aplicación web y se identifica Bolt CMS. Se inyecta/ejecuta un exploit en Python que entrega una reverse shell como www-data. Dentro del sistema se obtienen credenciales que permiten el acceso como jsmith, quien puede ejecutar `/usr/bin/zip` con sudo sin contraseña. Aprovechando esa configuración se escala primero a un usuario con sudo ilimitado (`(ALL : ALL) NOPASSWD: ALL`) y finalmente a root.

### Cadena de ataque / Attack Chain

Reconocimiento (nmap: 22,80) → Fingerprinting web (Bolt CMS) → Exploit Python → Shell www-data → Enumeración de credenciales → Usuario jsmith → Abuso de `/usr/bin/zip` con NOPASSWD → `(ALL : ALL) NOPASSWD: ALL` → Root.

**Learning chain:** Network scanning → Web fingerprinting → CMS exploitation → Initial access (www-data) → Credential harvesting → Sudo misconfiguration abuse → Privilege escalation to root

**Lección:** *Un binario permitido en sudo NOPASSWD es una puerta abierta a la escalada de privilegios: `sudo -l` debe auditarse siempre porque configuraciones laxas como `/usr/bin/zip` o `(ALL : ALL) NOPASSWD: ALL` otorgan root sin contraseña.*

**MITRE ATT&CK:** T1046 - Network Service Discovery, T1190 - Exploit Public-Facing Application, T1059.006 - Command and Scripting Interpreter: Python, T1078 - Valid Accounts, T1068 - Exploitation for Privilege Escalation, T1548.003 - Abuse Elevation Control Mechanism: Sudo and Sudo Caching

**Fuente:** [TryHackMe - Erit Securus I](https://tryhackme.com/room/eritsecurusi)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.