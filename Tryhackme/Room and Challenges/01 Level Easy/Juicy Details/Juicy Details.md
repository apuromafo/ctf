# Juicy Details

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `juicydetails` | https://tryhackme.com/room/juicydetails | 01 Level Easy | TryHackMe | OWASP Juice Shop / API REST / feroxbuster / hydra / sqlmap / curl / XSS / FTP (anonymous) / SSH | Pentest guiado sobre OWASP Juice Shop: enumeración de la API, login, búsqueda de productos, reseñas maliciosas, backups y acceso FTP/SSH. |

---

**Contexto:** Sala del catálogo de TryHackMe que sirve de guía para atacar OWASP Juice Shop (API REST). Se enumeran endpoints (`/rest/user/login`, `/rest/products/search`), se descubren recursos (`/ftp`), se explotan las reseñas de productos y se recuperan archivos de backup y credenciales que permiten accesos por FTP (anonymous) y SSH (`www-data`).

> **ES:** Sala guiada de ataque a OWASP Juice Shop: enumeración con nmap, hydra, sqlmap, curl y feroxbuster, explotación de la API y de las reseñas de productos, y accesos finales por FTP y SSH.
> **EN:** Guided room attacking OWASP Juice Shop: enumeration with nmap, hydra, sqlmap, curl and feroxbuster, exploitation of the API and product reviews, and final FTP/SSH access.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Lectura de la introducción de la sala para arrancar el entorno. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la room. / Read the room introduction. | `I am ready!` |

### Task 2: Enumeración / Enumeration

**Explicación:** Se realiza la enumeración de la aplicación con herramientas como `nmap`, `hydra`, `sqlmap`, `curl` y `feroxbuster`. Se identifican los endpoints de la API: el login en `/rest/user/login`, la búsqueda de productos en `/rest/products/search` (con el parámetro `q`), y se descubre el directorio `/ftp`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Herramientas utilizadas en la enumeración. / Tools used in the enumeration. | `nmap, hydra, sqlmap, curl, feroxbuster` |
| 2 | Endpoint de login de la API. / API login endpoint. | `/rest/user/login` |
| 3 | Endpoint de búsqueda de productos. / Product search endpoint. | `/rest/products/search` |
| 4 | Parámetro de búsqueda usado. / Search parameter used. | `q` |
| 5 | Directorio descubierto en el servidor. / Directory discovered on the server. | `/ftp` |

### Task 3: Explotación / Exploitation

**Explicación:** Se explota la aplicación: las reseñas de productos permiten el payload, el servidor muestra un timestamp (`Yay, 11/Apr/2021:09:16:31 +0000`), se obtienen credenciales (`email, password`), se recuperan los backups `coupons_2013.md.bak` y `www-data.bak`, y se accede por FTP con el usuario `anonymous` y finalmente por SSH como `www-data`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Punto de inyección en el producto. / Injection point in the product. | `product reviews` |
| 2 | Timestamp mostrado por el servidor. / Timestamp shown by the server. | `Yay, 11/Apr/2021:09:16:31 +0000` |
| 3 | Campos de credenciales obtenidos. / Credential fields obtained. | `email, password` |
| 4 | Archivos de backup recuperados. / Backup files recovered. | `coupons_2013.md.bak, www-data.bak` |
| 5 | Servicio y usuario de acceso inicial. / Service and user for initial access. | `ftp, anonymous` |
| 6 | Servicio y usuario del acceso final. / Service and user for final access. | `ssh, www-data` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la room. | `I am ready!` |
| 2 | Herramientas utilizadas en la enumeración. | `nmap, hydra, sqlmap, curl, feroxbuster` |
| 3 | Endpoint de login de la API. | `/rest/user/login` |
| 4 | Endpoint de búsqueda de productos. | `/rest/products/search` |
| 5 | Parámetro de búsqueda usado. | `q` |
| 6 | Directorio descubierto en el servidor. | `/ftp` |
| 7 | Punto de inyección en el producto. | `product reviews` |
| 8 | Timestamp mostrado por el servidor. | `Yay, 11/Apr/2021:09:16:31 +0000` |
| 9 | Campos de credenciales obtenidos. | `email, password` |
| 10 | Archivos de backup recuperados. | `coupons_2013.md.bak, www-data.bak` |
| 11 | Servicio y usuario de acceso inicial. | `ftp, anonymous` |
| 12 | Servicio y usuario del acceso final. | `ssh, www-data` |

---

**Metodología:** Enumerar primero la aplicación (nmap, feroxbuster, hydra, sqlmap, curl) para mapear la API y los recursos (`/ftp`), explotar las reseñas de productos y los endpoints de login/búsqueda, recuperar los backups para extraer credenciales y, finalmente, pivotar por FTP (anonymous) y SSH (`www-data`) hasta completar el acceso.

### Cadena de ataque / Attack Chain

```text
nmap/hydra/sqlmap/curl/feroxbuster -> /rest/user/login -> /rest/products/search?q= -> /ftp -> product reviews (inyección) -> backups (.bak) -> credenciales -> FTP anonymous -> SSH www-data
```

**Learning chain:** enumeración de API -> endpoints -> `/ftp` -> reseñas -> backups -> credenciales -> FTP -> SSH.

**Lección:** *OWASP Juice Shop está lleno de fallos intencionados: enumerar la API y revisar los backups expuestos permite pasar de la web al sistema con credenciales y accesos FTP/SSH mal configurados.*

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application), T1595 (Active Scanning), T1110 (Brute Force), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Juicy Details](https://tryhackme.com/room/juicydetails)
---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.