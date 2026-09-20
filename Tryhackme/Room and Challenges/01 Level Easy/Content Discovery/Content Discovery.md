# Content Discovery

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough (web) | `contentdiscovery` | https://tryhackme.com/room/contentdiscovery | 01 Level Easy | TryHackMe | Content discovery / robots.txt / sitemap.xml / OWASP / Dir Gobuster / Feroxbuster / OSINT / Google dorks / GitHub / Wappalyzer | Descubrir contenido oculto y paths en aplicaciones web mediante métodos manuales, automatizados y OSINT. |

---

**Contexto:** Room de la ruta de pentesting web centrada en el descubrimiento de contenido. Explica qué es el content discovery y sus tres variantes (manual, automatizada y OSINT), cómo localizar rutas ocultas en robots.txt y sitemap.xml, cómo leer los headers y detectar el stack/framework, cómo usar motores de búsqueda y herramientas web (Wappalyzer, wayback machine) y repositorios GitHub para filtrar información, y cómo automatizar el descubrimiento con herramientas como Gobuster/ffuf. Incluye una máquina desplegable con directorios ocultos.

> **ES:** Descubre contenido oculto y paths de una aplicación web (manualmente, con OSINT y con herramientas automatizadas) para revelar directorios, flags y archivos sensibles.
> **EN:** Discover hidden content and paths of a web application (manually, with OSINT and automated tools) to reveal directories, flags and sensitive files.

## Solucionario

### Task 1: ¿Qué es el Content Discovery? / What is Content Discovery?

**Explicación:** Se presenta el concepto: descubrir contenido no es trivial, porque una aplicación puede tener paths que no enlazan en ningún sitio. Las tres variantes del content discovery son manual (Manually), automatizada (Automated) y basada en OSINT. Se introduce además el marco de referencia OWASP.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuáles son las tres variantes del content discovery? / What are the three variants of content discovery? | `Manually`, `Automated`, `OSINT` |

### Task 2: Descubrimiento manual — Archivos comunes / Manual Discovery — Common Files

**Explicación:** Métodos manuales: se prueban paths comunes (`/robots.txt`, `/sitemap.xml`, `.well-known`) y se repasa el historial HTTPS (wayback machine) en busca de páginas antiguas olvidadas. Sobre la máquina desplegada, `robots.txt` revela `/staff-portal`; analizando sus fuentes aparecen `/cgiirc` y un path en el código; y contrastando con la wayback machine se recupera la página antigua `/s3cr3t-area`.

```bash
curl http://MACHINE/robots.txt        # -> /staff-portal
# /staff-portal -> revisar el código fuente -> /cgiirc
# wayback machine -> https://archive.org/web/ -> /s3cr3t-area
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué path de robots.txt da acceso al portal del staff? / What is the path in the robots.txt that gives access to the staff portal? | `/staff-portal` |
| 2 | En el código fuente de /staff-portal, ¿qué plataforma de chat externa se usa? / In the source code of /staff-portal, what external chat platform is being used? | `cgiirc` |
| 3 | ¿Qué path revela la wayback machine? / What is the path within the wayback machine? | `/s3cr3t-area` |

### Task 3: Descubrimiento manual — Headers y stack de frameworks / Manual Discovery — Headers & Framework Stack

**Explicación:** Los headers HTTP y la "carta de presentación" de la aplicación filtran información: el header de la flag corresponde a una cabecera del servidor (pagina principal) y el valor de otra cabecera (un user-agent personalizado) esconde una segunda flag. Además, reconocer cualquier cambio de framework/stack predeterminado evita quedarse en el default `THM{CHANGE_DEFAULT_CREDENTIALS}`.

```bash
curl http://MACHINE/                        # comprobar headers -> THM{HEADER_FLAG}
curl -H "User-Agent: secret" http://MACHINE/ # header flag vía user-agent
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag oculta en un header del servidor web? / What is the flag hidden in one of the headers of the webserver? | `THM{HEADER_FLAG}` |
| 2 | ¿Cuál es la flag que se esconde tras dejar el valor por defecto de una cabecera/framework? / What is the flag hidden after keeping the default value of a header/framework? | `THM{CHANGE_DEFAULT_CREDENTIALS}` |

### Task 4: OSINT — Motores de búsqueda y herramientas web / OSINT — Search Engines & Web Tools

**Explicación:** El OSINT usa motores de búsqueda y herramientas: el operador de Google que limita a un dominio es `site:`, y herramientas como Wappalyzer y la wayback machine permiten identificar el stack de la aplicación. La wayback machine (archive.org) se usa también en la práctica anterior.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el operador de Google que filtra los resultados a un dominio específico? / What Google operator do you use to filter the results to a specific domain? | `site:` |
| 2 | ¿Qué herramienta web de extensiones de navegador se usa para identificar el stack de tecnologías de una aplicación? / What browser extension tool is used to identify the technology stack of a website? | `Wappalyzer` |

### Task 5: OSINT — GitHub / OSINT — GitHub

**Explicación:** Los repositorios de GitHub filtran información por errores humanos (código con credenciales, ficheros de trabajo) y por el apartado de versiones que muestran los archivos elásticos (como aquí). En la práctica: `/monthly` es un fichero de logs que enumera las horas `fullhour`, el parámetro `year` de GitHub muestra el commit anual de `robots.txt`, y `.s3.amazonaws.com` es el dominio de bucket público de S3 que aparece filtrado. Además, `https://archive.org/web/` fue la respuesta al recordar la manera de buscar versiones antiguas y `version control system` es el término que se usa para referirse a Git.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué enlace consultamos para ver versiones anteriores de una página web? / What link do we consult to see past versions of a website? | `https://archive.org/web/` |
| 2 | ¿Qué término se usa para referirse al sistema de control de versiones Git? / What term is used to refer to the Git version control system? | `version control system` |
| 3 | Después de enumerar, ¿qué dominio de bucket de S3 encontraste? / What S3 bucket domain did you find after enumeration? | `.s3.amazonaws.com` |

### Task 6: Descubrimiento automatizado / Automated Discovery

**Explicación:** Con el robot de Google (wordlist) y herramientas como ffuf, Gobuster o Feroxbuster se automatiza el fuzzing de rutas: `ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -u http://MACHINE/FUZZ`. El fuzzing revela `/monthly` (con el log con un user `fullhour`) y `/development.log` (que contiene la flag).

```bash
ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -u http://MACHINE/FUZZ
curl http://MACHINE/monthly            # -> log, usuario fullhour
curl http://MACHINE/development.log    # -> THM{DEVELOPMENT_LOG_28ORZ}
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué path descubierto menciona una hora concreta (fullhour) tras el fuzzing? / What path discovered mentions a specific hour (fullhour) after fuzzing? | `/monthly` |
| 2 | Después de enumerar, ¿qué fichero de log contiene la flag? / What log file contains the flag after enumeration? | `/development.log` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuáles son las tres variantes del content discovery? / What are the three variants of content discovery? | `Manually`, `Automated`, `OSINT` |
| 2 | ¿Qué path de robots.txt da acceso al portal del staff? / What is the path in the robots.txt that gives access to the staff portal? | `/staff-portal` |
| 3 | ¿Qué plataforma de chat externa se usa en /staff-portal? / What external chat platform is being used? | `cgiirc` |
| 4 | ¿Qué path revela la wayback machine? / What is the path within the wayback machine? | `/s3cr3t-area` |
| 5 | ¿Cuál es la flag oculta en un header del servidor web? / What is the flag hidden in one of the headers of the webserver? | `THM{HEADER_FLAG}` |
| 6 | ¿Cuál es la flag tras dejar el valor por defecto de una cabecera/framework? / What is the flag hidden after keeping the default value? | `THM{CHANGE_DEFAULT_CREDENTIALS}` |
| 7 | ¿Qué operador de Google filtra por dominio específico? / What Google operator filters results to a specific domain? | `site:` |
| 8 | ¿Qué extensión de navegador identifica el stack de tecnologías? / What browser extension identifies the technology stack? | `Wappalyzer` |
| 9 | ¿Qué enlace consultamos para ver versiones antiguas de una web? | `https://archive.org/web/` |
| 10 | ¿Qué término se usa para el sistema de control de versiones Git? | `version control system` |
| 11 | ¿Qué dominio de bucket de S3 encontraste? / What S3 bucket domain did you find? | `.s3.amazonaws.com` |
| 12 | ¿Qué path descubierto menciona una hora concreta (fullhour)? | `/monthly` |
| 13 | ¿Qué fichero de log contiene la flag? | `/development.log` |

---

**Metodología:** Se combinan las tres variantes del content discovery: manual (robots.txt, sitemap, wayback machine, fuentes y headers HTTP), OSINT (Google dorks, Wappalyzer, GitHub, archive.org) y automatizada (ffuf/Gobuster con SecLists). Los hallazgos (`/staff-portal`, `/s3cr3t-area`, `/monthly`, `/development.log`) se verifican con curl para extraer las flags.

### Cadena de ataque / Attack Chain

```text
robots.txt (/staff-portal) -> fuente (/cgiirc) -> wayback machine (/s3cr3t-area) -> headers (THM{HEADER_FLAG}) -> OSINT (site:, Wappalyzer) -> GitHub (.s3.amazonaws.com) -> ffuf/Gobuster (/monthly, /development.log) -> flags
```

**Learning chain:** Concepto de content discovery -> manual (robots.txt/wayback) -> headers/framework -> OSINT (Google/Wappalyzer) -> GitHub -> automatización (ffuf) -> extracción de flags.

**Lección:** *El contenido de una web no es solo lo enlazado: robots.txt, versiones antiguas, headers, repositorios públicos y el fuzzing automático revelan paths y secretos que ningún usuario normal visita.*

**MITRE ATT&CK:** T1595 - Active Scanning; T1083 - File and Directory Discovery

**Fuente:** [TryHackMe - Content Discovery](https://tryhackme.com/room/contentdiscovery)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.