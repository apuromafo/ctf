# Daily Bugle

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Hard | CTF | `dailybugle` | https://tryhackme.com/room/dailybugle | 03 Level Hard | TryHackMe | Joomla / SQL injection / CVE-2017-8917 / John the Ripper / hashcat / escalada de privilegios | Compromiso de una máquina que ejecuta Joomla: inyección SQL en la API de Joomla (CVE-2017-8917), extracción y crackeo del hash de un superusuario, acceso a la consola de administración del CMS y escalada de privilegios para leer la flag de root. |

---

**Contexto:** La sala Daily Bugle despliega una máquina Linux con un CMS Joomla vulnerable. El recorrido típico es: enumeración del sitio, explotación de la inyección SQL conocida en Joomla (CVE-2017-8917) para volcar el hash de la contraseña de un usuario, crackeo del hash (`spiderman123`) contra un diccionario, acceso a la consola de administración del CMS y, finalmente, una escalada de privilegios que permite leer la flag de root. El nombre del superusuario de la base de datos es `spiderman`.

> **ES:** "Compromete la máquina Daily Bugle: explota la inyección SQL de Joomla (CVE-2017-8917), craquea el hash del superusuario, accede al panel de administración y escala privilegios para leer la flag de root."
> **EN:** "Compromise the Daily Bugle machine: exploit the Joomla SQL injection (CVE-2017-8917), crack the superuser hash, get into the admin panel and escalate privileges to read the root flag."

## Solucionario

### Task 1: Enumeración del CMS / CMS enumeration

**Explicación:** Mediante la explotación de la base de datos del CMS se recupera el nombre de usuario del superusuario. Contenido original de la tarea:

```text
1. spiderman
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Nombre de usuario del superusuario de la base de datos. | `spiderman` |

### Task 2: Versión, credenciales y flag de root / Version, credentials and root flag

**Explicación:** Se identifica la versión del CMS Joomla (3.7.0), se crackea la contraseña del usuario (`spiderman123`) a partir de su hash, se reporta el hash MD5 de la contraseña de Joomla y se obtiene la flag de root tras la escalada. Contenido original de la tarea:

```text
2. 1. 3.7.0
   2. spiderman123
   3. 27a260fe3cba712cfdedb1c86d80442e
   4. eec3d53292b1821868266858d7fa6f79
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Versión del CMS Joomla que corre en el servidor. | `3.7.0` |
| 2 | Contraseña descifrada del usuario. | `spiderman123` |
| 3 | Hash de la contraseña de Joomla extraído de la base de datos. | `27a260fe3cba712cfdedb1c86d80442e` |
| 4 | Flag de root obtenida tras la escalada de privilegios. | `eec3d53292b1821868266858d7fa6f79` |

### Task 3: Conclusión / Conclusion

**Explicación:** Tarea de cierre de la sala; no requiere respuesta. Contenido original de la tarea:

```text
3. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Nombre de usuario del superusuario de la base de datos. | `spiderman` |
| 2 | Versión del CMS Joomla que corre en el servidor. | `3.7.0` |
| 3 | Contraseña descifrada del usuario. | `spiderman123` |
| 4 | Hash de la contraseña de Joomla extraído de la base de datos. | `27a260fe3cba712cfdedb1c86d80442e` |
| 5 | Flag de root obtenida tras la escalada de privilegios. | `eec3d53292b1821868266858d7fa6f79` |
| 6 | Leer la conclusión de la sala. | `No answer needed` |

---

**Metodología:**
1. Enumerar el servidor web y detectar Joomla (fingerprint de la versión).
2. Explotar la inyección SQL del core de Joomla (CVE-2017-8917) para volcar los usuarios y sus hashes de la tabla de usuarios.
3. Craquear el hash del superusuario con John the Ripper (wordlist) y obtener la contraseña `spiderman123`.
4. Iniciar sesión en la consola de administración del CMS.
5. Escalar privilegios y leer la flag de root `eec3d53292b1821868266858d7fa6f79`.

### Cadena de ataque / Attack Chain

```text
Enumeración web -> Joomla 3.7.0 -> CVE-2017-8917 (SQL injection) -> volcado de hashes -> John the Ripper -> spiderman123 -> panel de administración -> escalada -> flag de root
```

**Learning chain:** `Recon -> Joomla -> SQLi (CVE-2017-8917) -> dump de la BD -> crackeo de hash -> admistración del CMS -> privesc -> root flag`

**Lección:** *Una inyección SQL en un CMS conocido permite volcar credenciales con hash; combinatoria de hashes débiles, su crackeo con John the Ripper y el abuso de la consola de administración para escalar hasta root.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1110.002 (Password Cracking), T1078 (Valid Accounts), T1068 (Exploitation for Privilege Escalation), T1082 (System Information Discovery)

**Fuente:** [TryHackMe - Daily Bugle](https://tryhackme.com/room/dailybugle)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.