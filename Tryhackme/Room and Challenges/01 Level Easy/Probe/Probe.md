# Probe

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | ctf | `probe` | [TryHackMe](https://tryhackme.com/room/probe) | 01 Level Easy | THM | NMAP, Enumeración web, Virtual host, Credenciales, phpMyAdmin, WordPress, Joomla, lighttpd | Reconocimiento y enumeración de CMS/web |

---

**Contexto:** CTF de reconocimiento y enumeración web: se descubren dos sitios (uno en el puerto estándar y otro en un puerto alternativo con el virtual host dev.probe.thm), se obtienen credenciales de una API, se explora un panel con phpMyAdmin y un blog WordPress, y se identifica un tercer CMS (Joomla) junto al servidor lighttpd, recuperando las banderas del desafío.

> **ES:** Máquina CTF de reconocimiento: puertos alternativos, virtual hosts, credenciales, phpMyAdmin, WordPress, Joomla y flags escondidas en los paneles web.
> **EN:** Recon CTF machine: alternate ports, virtual hosts, credentials, phpMyAdmin, WordPress, Joomla and flags hidden in the web panels.

## Solucionario

### Task 1: Reconocimiento y enumeración / Recon and Enumeration

**Explicación:** Resuelve el reconocimiento completo de la máquina: escaneo de puertos y versión del servidor, descubrimiento de la aplicación en el puerto alternativo con su virtual host (dev.probe.thm), extracción de credenciales y de la primera bandera, y enumeración de los CMS y servicios (phpMyAdmin, WordPress 6.2.2, Joomla, lighttpd) hasta recuperar la bandera final.

1. 1. 2.4.41
   2. 1338
   3. dev.probe.thm
   4. probe@probe.thm
   5. API20190902,NTS
   6. THM{WELCOME_101113}
   7. phpmyadmin
   8. Wordpress
   9. 6.2.2
   10. joomla
   11. license.txt
   12. lighttpd
   13. THM{CONTACT_US_1100}

| Pregunta | Respuesta |
|---|---|
| ¿Qué versión del servidor web corre en el puerto 80? | `2.4.41` |
| ¿Qué puerto alternativo alberga contenido adicional? | `1338` |
| ¿Qué virtual host / subdominio se descubre? | `dev.probe.thm` |
| ¿Qué dirección de correo aparece en la aplicación? | `probe@probe.thm` |
| ¿Cuáles son las credenciales encontradas en la API? | `API20190902,NTS` |
| ¿Cuál es la bandera del panel? | `THM{WELCOME_101113}` |
| ¿Qué panel se identifica tras la autenticación? | `phpmyadmin` |
| ¿Qué CMS / plataforma de blogs se identifica? | `Wordpress` |
| ¿Qué versión de WordPress está instalada? | `6.2.2` |
| ¿Qué otro CMS se encuentra en el host? | `joomla` |
| ¿Qué archivo permite la enumeración de usuarios? | `license.txt` |
| ¿Qué servidor web responde en el puerto 80? | `lighttpd` |
| ¿Cuál es la bandera final del formulario de contacto? | `THM{CONTACT_US_1100}` |

---

**Metodología:** Escaneo de puertos y versiones con NMAP, enumeración de virtual hosts y subdominios, análisis de la aplicación web y sus paneles (phpMyAdmin), fingerprinting de CMS (WordPress, Joomla) y del servidor (lighttpd), revisión de archivos sensibles (license.txt) y extracción de credenciales y banderas.

### Cadena de ataque / Attack Chain
Escaneo NMAP del puerto 80 (Apache 2.4.41) y del puerto alternativo 1338 -> Descubrimiento del virtual host dev.probe.thm -> Obtención de la dirección de correo y de las credenciales (API20190902,NTS) -> Acceso al panel y primera bandera (THM{WELCOME_101113}) -> Enumeración de aplicaciones: phpMyAdmin -> Fingerprinting de WordPress 6.2.2 y Joomla -> Identificación de lighttpd y de license.txt -> Bandera final en el formulario de contacto (THM{CONTACT_US_1100}).

**Learning chain:** Escaneo de puertos y versiones, virtual hosts y subdominios, enumeración de paneles (phpMyAdmin) y CMS (WordPress/Joomla), fingerprinting de servidores web y manejo de credenciales hardcodeadas.

**Lección:** *Los paneles ocultos, las credenciales en el código y los puertos alternativos multiplican la superficie de ataque: la enumeración metódica saca a la luz acceso, datos y banderas que el escaneo superficial no revela.*

**MITRE ATT&CK:** T1595 Active Scanning, T1595.002 Vulnerability Scanning, T1190 Exploit Public-Facing Application, T1110.001 Brute Force (Password Guessing), T1213 Data from Information Repositories.

**Fuente:** [TryHackMe - Probe](https://tryhackme.com/room/probe)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.