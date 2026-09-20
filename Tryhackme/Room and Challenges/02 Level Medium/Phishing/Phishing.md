# Phishing

| **Dificultad** | MEDIUM | **Tipo** | Walkthrough (Free) | **Slug** | `phishing` |
| **Link** | [TryHackMe](https://tryhackme.com/room/phishing) | **Sección** | Social Engineering / Red Team | **Fuente** | TryHackMe |
| **Componentes** | Phishing, Ingeniería Social, OSINT, GoPhish, Droppers, Phishing Domains, Macros, CVE-2021-40444, TLS/DNS | **Impacto** | Capacita en la planificación y ejecución de campañas de phishing realistas (red team) para capturar credenciales y entregar malware, comprendiendo también los vectores de detección y mitigación |

---

**Contexto:** Esta sala enseña el arte del phishing como simulación de adversario para equipos rojos. Cubre las técnicas psicológicas y los vectores de phishing, la redacción de correos convincentes, la infraestructura necesaria (certificados TLS, registros DNS, GoPhish), el uso de GoPhish para lanzar campañas y capturar credenciales, los droppers, la selección de dominios (expiración y typosquatting), el uso de macros de Office y las vulnerabilidades de navegador como CVE-2021-40444, terminando con un reto práctico.

> **ES:** Formación práctica sobre campañas de phishing: técnicas y vectores, escritura de correos convincentes, infraestructura (SSL/TLS, DNS, GoPhish), droppers, elección de dominios, macros de Office y exploits de navegador, con un reto final de captura de credenciales.
> **EN:** Hands-on training on phishing campaigns: techniques and vectors, writing convincing emails, infrastructure (SSL/TLS, DNS, GoPhish), droppers, domain selection, MS Office macros and browser exploits, with a final credential-capture challenge.

## Solucionario

### Task 1: Brief / Briefing

**Explicación:** Se introduce el objetivo de la sala: entender qué es el phishing, cómo funciona y cómo los equipos rojos lo usan en ejercicios de simulación de adversario para evaluar la seguridad de una organización.

1. No answer needed

### Task 2: Introducción a los Ataques de Phishing / Intro To Phishing Attacks

**Explicación:** El phishing forma parte de la manipulación psicológica conocida como social engineering. Los equipos rojos suelen participar en campañas de spear-phishing, dirigidas a víctimas concretas.

1. 1. social engineering
   2. spear-phishing

### Task 3: Escribiendo Correos de Phishing Convincentes / Writing Convincing Phishing Emails

**Explicación:** Para conseguir realismo se usa OSINT para encontrar marcas o personas con las que la víctima interactúa. En un correo, el texto del ancla (anchor text) de una etiqueta HTML debe modificarse para disfrazar el enlace y que parezca legítimo.

1. 1. OSINT
   2. anchor text

### Task 4: Infraestructura de Phishing / Phishing Infrastructure

**Explicación:** Se configura la infraestructura del atacante: los certificados SSL/TLS hacen que un sitio parezca más auténtico; el protocolo DNS, mediante registros TXT, mejora la entregabilidad de los correos; y GoPhish automatiza la campaña y ofrece analíticas.

1. 1. SSL/TLS Certificates
   2. DNS
   3. GoPhish

### Task 5: Usando GoPhish / Using GoPhish

**Explicación:** GoPhish se configura con sending profiles, landing pages y templates de correo. Al desplegar la campaña contra el grupo de usuarios de prueba, se capturan las credenciales introducidas por el usuario simulado "Brian", cuya contraseña es p4$$w0rd!.

1. p4$$w0rd!

### Task 6: Droppers / Droppers

**Explicación:** Un dropper es el primer componente que ejecuta el código malicioso en el sistema de la víctima. Cuando no tienen ningún otro propósito que descargar y ejecutar una carga útil, los droppers tienden a ser maliciosos (`nay`).

1. nay

### Task 7: Elección de un Dominio de Phishing / Choosing A Phishing Domain

**Explicación:** Para maximizar la credibilidad, es mejor usar un dominio antiguo/expiración (`old`) que uno nuevo. Registrar un dominio muy similar con un error de ortografía se denomina typosquatting.

1. 1. old
   2. typosquatting

### Task 8: Usando MS Office en Phishing / Using MS Office in Phishing

**Explicación:** Los documentos de Microsoft Office pueden contener macros (VBA) que, al ejecutarse, lanzan comandos en la máquina de la víctima, permitiendo descargar e instalar malware.

1. macros

### Task 9: Usando Exploits de Navegador / Using Browser Exploits

**Explicación:** Los exploits de navegador convierten un simple clic en la entrega de la carga útil. El CVE reciente que causó ejecución remota de código en este contexto es CVE-2021-40444, que afecta a Microsoft MSHTML.

1. CVE-2021-40444

### Task 10: Reto Práctico / Phishing Practical

**Explicación:** Se aplica todo lo aprendido en un reto práctico de análisis de una campaña de phishing completa; al resolverse correctamente se obtiene la flag final.

1. THM{I_CAUGHT_ALL_THE_PHISH}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2.1 | What type of psychological manipulation is phishing part of? | `social engineering` |
| 2.2 | What type of phishing campaign do red teams get involved in? | `spear-phishing` |
| 3.1 | What tactic can be used to find brands or people a victim interacts with? | `OSINT` |
| 3.2 | What should be changed on an HTML anchor tag to disguise a link? | `anchor text` |
| 4.1 | What part of a red team infrastructure can make a website look more authentic? | `SSL/TLS Certificates` |
| 4.2 | What protocol has TXT records that can improve email deliverability? | `DNS` |
| 4.3 | What tool can automate a phishing campaign and include analytics? | `GoPhish` |
| 5.1 | What is the password for Brian? | `p4$$w0rd!` |
| 6.1 | Do droppers tend to be malicious? | `nay` |
| 7.1 | What is better, using an expired or new domain? (old/new) | `old` |
| 7.2 | What is the term used to describe registering a similar domain name with a spelling error? | `typosquatting` |
| 8.1 | What can Microsoft Office documents contain, which, when executed can run computer commands? | `macros` |
| 9.1 | Which recent CVE caused remote code execution? | `CVE-2021-40444` |
| 10.1 | What is the flag from the challenge? | `THM{I_CAUGHT_ALL_THE_PHISH}` |

---

**Metodología:** Estudio de la psicología del phishing y sus vectores (vishing, phishing, spear-phishing, whaling). Uso de OSINT para personalizar los correos y manipulación del anchor text de los enlaces. Construcción de la infraestructura con certificados SSL/TLS, registros TXT de DNS, y GoPhish. Simulación de una campaña en GoPhish con una landing page para capturar credenciales y un grupo de usuarios objetivo. Análisis de droppers y de la selección de dominios (expiración y typosquatting). Revisión del abuso de macros en Office, del exploit CVE-2021-40444 y del reto práctico final de análisis de campaña.

**Learning chain:** Introducción → Técnicas y vectores de phishing → Escritura de correos convincentes (OSINT, anchor text) → Infraestructura (SSL/TLS, DNS, GoPhish) → Uso de GoPhish (credenciales de Brian) → Droppers → Elección de dominio (old, typosquatting) → Macros de Office → Exploits de navegador (CVE-2021-40444) → Reto práctico (flag).

**Lección:** *Una campaña de phishing eficaz no depende solo del correo: requiere una infraestructura creíble (TLS, DNS, GoPhish), dominios aparentemente legítimos y una carga útil funcional (droppers, macros o exploits). El entrenamiento del usuario final y los controles técnicos (SPF/DMARC, EDR, filtrado) son la defensa principal.*

**MITRE ATT&CK:** T1566.001 (Phishing: Spearphishing Attachment), T1566.002 (Phishing: Spearphishing Link), T1204.002 (User Execution: Malicious File), T1598 (Phishing for Information)

**Fuente:** [TryHackMe - Phishing](https://tryhackme.com/room/phishing)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.