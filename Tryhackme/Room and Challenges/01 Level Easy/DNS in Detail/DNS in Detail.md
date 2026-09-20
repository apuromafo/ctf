# DNS in Detail

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `dnsindetail` | [TryHackMe](https://tryhackme.com/room/dnsindetail) | 01 Level Easy | TryHackMe | DNS / jerarquía de dominios / registros DNS (A, AAAA, MX, TXT, CNAME, PTR) / TTL / nslookup / dig | Comprender cómo funciona el DNS y cómo se resuelven los nombres de dominio a direcciones IP. |

> **Objeto:** Aprender qué es el DNS, la jerarquía de dominios, los tipos de registro (A, AAAA, MX, TXT, CNAME), el proceso de resolución con servidores recursivos y autoritativos (TTL), y resolver las consultas prácticas de la room con `dig` y `nslookup` para obtener la flag del laboratorio.

---

**Contexto:** El DNS (Domain Name System) traduce los nombres de dominio legibles por humanos (como website.thm) a direcciones IP que entienden las máquinas, funcionando como una agenda de contactos de Internet. La room recorre la teoría del DNS y culmina en una práctica resolviendo consultas reales contra el servidor DNS de la máquina desplegada.

> **ES:** El DNS traduce nombres de dominio a IP. Se estudia la jerarquía de dominios (subdominios de hasta 63 caracteres y máx. 253 en total, TLD como .co.uk tipo ccTLD), los registros A, AAAA, CNAME, MX y TXT, y la resolución con servidores recursivos y autoritativos junto al TTL. Por último se responden las preguntas prácticas con dig/nslookup contra la máquina y se obtiene la flag del registro TXT.
> **EN:** DNS translates domain names into IP addresses. The room covers the domain hierarchy (subdomains up to 63 chars, 253 total, TLDs such as .co.uk as ccTLD), the A, AAAA, CNAME, MX and TXT records, and the resolution process with recursive and authoritative servers along with TTL. Finally, dig/nslookup are used against the deployed machine to answer the practical questions and get the TXT-record flag.

## Solucionario

### Task 1: ¿Qué es el DNS? / What is DNS?
**Explicación:** Primera tarea teórica de la room: el DNS es el sistema que resuelve nombres de dominio legibles por humanos a direcciones IP. La respuesta confirma el significado del acrónimo DNS.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does DNS stand for? / ¿Qué significa la sigla DNS? | `Domain Name System` |

### Task 2: Jerarquía de dominios / Domain Hierarchy
**Explicación:** La jerarquía del DNS se compone de subdominios y TLD. Un subdominio no puede superar los 63 caracteres, el nombre totalmente cualificado no puede exceder los 253 caracteres y entre los caracteres permitidos está el guion bajo (`_`). Los TLD de país (como .co.uk) se denominan ccTLD.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the maximum length of a subdomain? / ¿Cuál es la longitud máxima de un subdominio? | `63` |
| 2 | Which of the following characters can be used in a subdomain? (Pick - or _) / ¿Cuál de los siguientes caracteres puede usarse en un subdominio? (elige - o _) | `_` |
| 3 | What is the maximum length of a domain name? / ¿Cuál es la longitud máxima de un nombre de dominio? | `253` |
| 4 | What type of TLD is .co.uk? / ¿Qué tipo de TLD es .co.uk? | `ccTLD` |

### Task 3: Tipos de registro / Record Types
**Explicación:** Describe los registros DNS más comunes: A (IPv4), AAAA (IPv6), CNAME (alias), MX (servidor de correo) y TXT (texto libre). Cada tipo indica a qué dirección o servicio apunta el nombre.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What type of record would be used to advise where to send email? / ¿Qué tipo de registro se usa para indicar a dónde enviar el correo? | `MX` |
| 2 | What record would be used to point a domain to an IPv6 address? / ¿Qué registro se usa para apuntar un dominio a una dirección IPv6? | `AAAA` |

### Task 4: Haciendo una petición / Making a Request
**Explicación:** Explica el flujo de una consulta DNS: el cliente pregunta a un resolver recursivo, que a su vez contacta con servidores autoritativos de la zona. El TTL (Time To Live) indica cuánto tiempo puede almacenar en caché el resolver la respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What field specifies how long a DNS resolver should cache a query? / ¿Qué campo indica cuánto tiempo debe cachear un resolver la consulta? | `TTL` |
| 2 | What type of DNS Server performs a recursive query? / ¿Qué tipo de servidor DNS realiza una consulta recursiva? | `recursive` |
| 3 | What type of DNS server holds zones? / ¿Qué tipo de servidor DNS mantiene las zonas? | `authoritative` |

### Task 5: Práctica / Practical
**Explicación:** Con la máquina desplegada, se consultan los registros de website.thm con `dig` y `nslookup`: el CNAME de shops.website.thm apunta a shops.myshopify.com, el registro TXT de website.thm contiene la flag, el TTL numérico de ese registro TXT es 30 y el registro A de www.website.thm apunta a 10.10.10.10.

```bash
dig @MACHINE_IP website.thm               # consultar todos los registros
dig +short TXT website.thm                 # valor del registro TXT (flag)
dig +short A www.website.thm               # IP del registro A
dig +short CNAME shops.website.thm         # alias CNAME
nslookup -type=TXT website.thm
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the CNAME of shops.website.thm? / ¿Cuál es el CNAME de shops.website.thm? | `shops.myshopify.com` |
| 2 | What is the value of the TXT record of website.thm? / ¿Cuál es el valor del registro TXT de website.thm? | `THM{7012BBA60997F35A9516C2E16D2944FF}` |
| 3 | What is the numerical value of the TTL of the TXT record of website.thm? / ¿Cuál es el valor numérico del TTL del registro TXT de website.thm? | `30` |
| 4 | What is the IP address of the A record of www.website.thm? / ¿Cuál es la dirección IP del registro A de www.website.thm? | `10.10.10.10` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What does DNS stand for? / ¿Qué significa la sigla DNS? | `Domain Name System` |
| 2 | What is the maximum length of a subdomain? / ¿Cuál es la longitud máxima de un subdominio? | `63` |
| 3 | Which of the following characters can be used in a subdomain? (Pick - or _) / ¿Cuál de los siguientes caracteres puede usarse en un subdominio? | `_` |
| 4 | What is the maximum length of a domain name? / ¿Cuál es la longitud máxima de un nombre de dominio? | `253` |
| 5 | What type of TLD is .co.uk? / ¿Qué tipo de TLD es .co.uk? | `ccTLD` |
| 6 | What type of record would be used to advise where to send email? / ¿Qué registro se usa para indicar a dónde enviar el correo? | `MX` |
| 7 | What record would be used to point a domain to an IPv6 address? / ¿Qué registro se usa para apuntar un dominio a IPv6? | `AAAA` |
| 8 | What field specifies how long a DNS resolver should cache a query? / ¿Qué campo indica cuánto tiempo cachear una consulta? | `TTL` |
| 9 | What type of DNS Server performs a recursive query? / ¿Qué tipo de servidor DNS realiza una consulta recursiva? | `recursive` |
| 10 | What type of DNS server holds zones? / ¿Qué tipo de servidor DNS mantiene las zonas? | `authoritative` |
| 11 | What is the CNAME of shops.website.thm? / ¿Cuál es el CNAME de shops.website.thm? | `shops.myshopify.com` |
| 12 | What is the value of the TXT record of website.thm? / ¿Cuál es el valor del registro TXT de website.thm? | `THM{7012BBA60997F35A9516C2E16D2944FF}` |
| 13 | What is the numerical value of the TTL of the TXT record of website.thm? / ¿Cuál es el TTL numérico del registro TXT de website.thm? | `30` |
| 14 | What is the IP address of the A record of www.website.thm? / ¿Cuál es la IP del registro A de www.website.thm? | `10.10.10.10` |

---

**Metodología:** Se estudia primero la teoría del DNS (acrónimo, jerarquía de dominios y tipos de registro) y después se practica contra la máquina desplegada: se consultan los registros del dominio del laboratorio con `dig` y `nslookup`, confirmando en la práctica cómo se resuelve un nombre de dominio (CNAME, TXT, TTL y A) y extrayendo la flag del registro TXT.

### Cadena de ataque / Attack Chain

```text
Teoría DNS (acrónimo) -> jerarquía de dominios (63 / _ / 253 / ccTLD) -> tipos de registro (MX / AAAA) -> resolución (TTL / recursivo / autoritativo) -> dig + short (TXT, A, CNAME) -> flag del registro TXT
```

**Learning chain:** What is DNS --> Domain Hierarchy --> Record Types --> Making a Request --> Practical (dig/nslookup) --> TXT flag.

**Lección:** *El DNS es una infraestructura crítica: dominar su jerarquía, sus registros y la resolución recursiva/autoritativa permite diagnosticar, auditar e incluso explotar el servicio durante un pentest.*

**MITRE ATT&CK:** N/A (room de aprendizaje teórico-práctico sobre DNS)

**Fuente:** [TryHackMe - DNS in Detail](https://tryhackme.com/room/dnsindetail)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.