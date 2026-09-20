# Badbyte

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `badbyte` |
| **Link** | [TryHackMe](https://tryhackme.com/room/badbyte) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | nmap, ftp, WordPress, CVE-2020-11738, CVE-2020-25213, escalada de privilegios |
| **Impacto** | Compromiso de una máquina con WordPress: enumeración de puertos, acceso FTP, explotación de plugins vulnerables en WordPress, obtención de shell y escalada a root. |

---

**Contexto:** La sala es una máquina guiada de tipo CTF. Se comienza con un escaneo de puertos que revela dos servicios (SSH y FTP), se accede por FTP con credenciales débiles y se obtiene información del sistema. En el puerto web se descubre un **WordPress** con plugins vulnerables (**CVE-2020-11738** y **CVE-2020-25213**), se explotan para obtener una shell y, tras capturar la primera flag, se escala a root recuperando la contraseña de administración y la flag final.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la máquina y del flujo de trabajo de la sala: enumeración de servicios, acceso FTP, explotación de WordPress y escalada a root. Tarea informativa sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la sala. | `No answer needed` |

### Task 2: Enumeración de puertos / Port Enumeration

**Explicación:** Se escanea la máquina y se descubren **2** puertos abiertos: el puerto del servicio **ssh** y el puerto del servicio **ftp**. El puerto de SSH abierto es el **30024**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos puertos están abiertos en la máquina? | `2` |
| 2 | ¿Qué servicio se ejecuta en el primer puerto? | `ssh` |
| 3 | ¿Qué número de puerto utiliza el servicio SSH? | `30024` |
| 4 | ¿Qué servicio se ejecuta en el otro puerto abierto? | `ftp` |

### Task 3: Conexión FTP / FTP Access

**Explicación:** Se conecta al servicio FTP y, examinando el banner/contenido, se obtienen las credenciales o datos de acceso: el usuario `errorcauser` y la contraseña `cupcake`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué usuario se obtiene del servicio FTP? | `errorcauser` |
| 2 | ¿Qué contraseña se obtiene del servicio FTP? | `cupcake` |

### Task 4: Servicios web / Web Services

**Explicación:** Se identifica la parte web de la máquina: los puertos de los servicios web son **80,3306** y los servicios correspondientes son **http, mysql**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué puertos web/mysql están abiertos en la máquina? | `80,3306` |
| 2 | ¿Qué servicios corren en esos puertos? | `http, mysql` |

### Task 5: Explotación de WordPress / WordPress Exploitation

**Explicación:** Sobre el puerto 80 se identifica un **wordpress**. Tras enumerar el CMS se detectan los plugins vulnerables: **CVE-2020-11738** (Photo Gallery) y **CVE-2020-25213** (Tiny File Manager). Explotándolos se sube/carga un webshell y se obtiene una shell como el usuario `cth`, capturando la flag de usuario.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué CMS se ejecuta en el puerto 80? | `wordpress` |
| 2 | Paso práctico de enumeración del CMS. | `No answer needed` |
| 3 | ¿Qué CVE afecta al plugin Photo Gallery? | `CVE-2020-11738` |
| 4 | ¿Qué CVE afecta al plugin Tiny File Manager? | `CVE-2020-25213` |
| 5 | Paso práctico de explotación de los plugins vulnerables. | `No answer needed` |
| 6 | ¿Qué usuario/shell se obtiene tras la explotación? | `cth` |
| 7 | ¿Cuál es la flag de usuario de la máquina? | `THM{227906201d17d9c45aa93d0122ea1af7}` |

### Task 6: Escalada y flags / Privilege Escalation & Flags

**Explicación:** Con la shell obtenida se escala a root: se recupera o crackea la contraseña del administrador **G00dP@$sw0rd2020** y se accede como root para leer la flag final de la máquina.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la contraseña de root/administración recuperada? | `G00dP@$sw0rd2020` |
| 2 | ¿Cuál es la flag de root de la máquina? | `THM{ad485b44f63393b6a9225974909da5fa}` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la introducción de la sala. | `No answer needed` |
| 2 | ¿Cuántos puertos están abiertos en la máquina? | `2` |
| 3 | ¿Qué servicio se ejecuta en el primer puerto? | `ssh` |
| 4 | ¿Qué número de puerto utiliza el servicio SSH? | `30024` |
| 5 | ¿Qué servicio se ejecuta en el otro puerto abierto? | `ftp` |
| 6 | ¿Qué usuario se obtiene del servicio FTP? | `errorcauser` |
| 7 | ¿Qué contraseña se obtiene del servicio FTP? | `cupcake` |
| 8 | ¿Qué puertos web/mysql están abiertos en la máquina? | `80,3306` |
| 9 | ¿Qué servicios corren en esos puertos? | `http, mysql` |
| 10 | ¿Qué CMS se ejecuta en el puerto 80? | `wordpress` |
| 11 | Paso práctico de enumeración del CMS. | `No answer needed` |
| 12 | ¿Qué CVE afecta al plugin Photo Gallery? | `CVE-2020-11738` |
| 13 | ¿Qué CVE afecta al plugin Tiny File Manager? | `CVE-2020-25213` |
| 14 | Paso práctico de explotación de los plugins vulnerables. | `No answer needed` |
| 15 | ¿Qué usuario/shell se obtiene tras la explotación? | `cth` |
| 16 | ¿Cuál es la flag de usuario de la máquina? | `THM{227906201d17d9c45aa93d0122ea1af7}` |
| 17 | ¿Cuál es la contraseña de root/administración recuperada? | `G00dP@$sw0rd2020` |
| 18 | ¿Cuál es la flag de root de la máquina? | `THM{ad485b44f63393b6a9225974909da5fa}` |

---

**Metodología:**

1. Se ejecuta `nmap` para enumerar los puertos abiertos: **2** puertos con servicios `ssh` (**30024**) y `ftp`.
2. Se accede por FTP y se obtienen las credenciales `errorcauser` / `cupcake`.
3. Se identifican los puertos web `80,3306` con servicios `http, mysql`.
4. Se enumera WordPress y se detectan los plugins vulnerables **CVE-2020-11738** y **CVE-2020-25213**.
5. Se explotan los plugins para cargar un webshell y obtener una shell como `cth`, capturando `THM{227906201d17d9c45aa93d0122ea1af7}`.
6. Se escala a root con la contraseña `G00dP@$sw0rd2020` y se lee la flag final `THM{ad485b44f63393b6a9225974909da5fa}`.

### Cadena de ataque / Attack Chain

```
nmap -> 2 puertos (ssh 30024, ftp)
  -> FTP -> errorcauser / cupcake
  -> Web -> 80,3306 (http, mysql)
  -> WordPress -> plugins vulnerables
  -> CVE-2020-11738 (Photo Gallery)
  -> CVE-2020-25213 (Tiny File Manager)
  -> Webshell -> usuario cth -> THM{2279...1af7}
  -> Escalada a root -> G00dP@$sw0rd2020
  -> THM{ad48...9da5fa}
```

**Learning chain:** Enumeración de puertos → Acceso FTP → Credenciales → Servicios web → Enumeración WordPress → Explotación de plugins → Shell como cth → Escalada a root → Flags

**Lección:** *Los plugins y CMS desactualizados son la superficie de ataque principal: los CVE-2020-11738 y CVE-2020-25213 permiten ejecutar código en WordPress y encadenar el acceso hasta root, por lo que mantener el software actualizado es crítico.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1110 (Brute Force), T1203 (Exploitation for Client Execution), T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Badbyte](https://tryhackme.com/room/badbyte)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.