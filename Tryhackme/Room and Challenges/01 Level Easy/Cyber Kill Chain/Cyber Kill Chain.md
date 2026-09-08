# Cyber Kill Chain

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `cyberkillchain` |
| **Link** | [TryHackMe](https://tryhackme.com/room/cyberkillchain) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de Jasper (jalblas.com) + Dan Schwarzentraub (Medium) + Hubert Krauze |
| **Componentes** | Cyber Kill Chain / Lockheed Martin / Reconnaissance / Weaponization / Delivery / Exploitation / Installation / C2 / Actions on Objectives |
| **Impacto** | Explora el marco de Lockheed Martin que divide un ataque en siete fases para ayudar a las organizaciones a defenderse (path SOC Level 1). |

---

**Contexto:** Explora el Cyber Kill Chain de Lockheed Martin, un framework de ciberseguridad que divide un ataque en siete fases para ayudar a las organizaciones a defenderse. Es parte del path SOC Level 1. Las siete fases: **Reconnaissance**, **Weaponization**, **Delivery**, **Exploitation**, **Installation**, **Command & Control (C2)** y **Actions on Objectives**.

Las siete fases del Cyber Kill Chain:

1. **Reconnaissance** — el atacante recopila información sobre el objetivo
2. **Weaponization** — el atacante crea un payload o modifica uno existente
3. **Delivery** — el atacante envía el payload al objetivo
4. **Exploitation** — el payload explota una vulnerabilidad
5. **Installation** — el atacante instala un backdoor o malware para persistencia
6. **Command & Control (C2)** — el atacante controla el sistema comprometido
7. **Actions on Objectives** — el atacante ejecuta sus objetivos (exfiltración, etc.)

## Solucionario

### Task 1: Introduction

**Explicación:** Introducción al framework: el Cyber Kill Chain de Lockheed Martin divide un ataque en siete fases para ayudar a las organizaciones a entender y defenderse de las intrusiones. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - introduction. | `No answer needed` |

### Task 2: Reconnaissance

**Explicación:** La primera fase de un ataque: los adversarios recopilan información sobre infraestructura, empleados y tecnologías. Puede ser pasiva (WHOIS, scraping de redes sociales) o activa (ingeniería social, escaneo de puertos). Incluye OSINT y email harvesting. El **OSINT Framework** es una herramienta web que agrega las herramientas y recursos comunes de open-source intelligence; el **email harvesting** es el proceso de recopilar direcciones de correo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the Intel Gathering Tool that is a web-based interface to the common tools and resources for open-source intelligence? | `OSINT Framework` |
| 2 | What is the definition for the email gathering process during the stage of reconnaissance? | `email harvesting` |

### Task 3: Weaponization

**Explicación:** El atacante crea un payload o modifica uno existente basado en las vulnerabilidades del sistema objetivo. Incluye técnicas como la **obfuscación** (dificultar el análisis del código malicioso para evadir la detección) y **macros** maliciosas en documentos de MS Office (la característica integrada que hace posible crear un documento de Office malicioso).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What technique is mentioned to evade detection by making it challenging to analyse the malicious code? | `Obfuscation` |
| 2 | What built-in feature makes creating a malicious MS Office document possible? | `Macro` |

### Task 4: Delivery

**Explicación:** El método de transmisión del payload al objetivo: emails de phishing, USB infectados o **watering hole attacks**. Un *watering hole attack* se dirige contra un grupo concreto de personas, infectando el sitio web que ese grupo visita habitualmente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the attack when it is performed against a specific group of people, and the attacker seeks to infect the website that the mentioned group of people is constantly visiting? | `Watering hole attack` |

### Task 5: Exploitation

**Explicación:** El payload explota una vulnerabilidad. Incluye el **timestomping** (modificar los atributos de tiempo de los archivos para ocultar cambios o archivos nuevos) y las **web shells** (script malicioso plantado en el servidor web para mantener el acceso y permitir el acceso remoto al servidor comprometido).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Can you provide the technique used to modify file time attributes to hide new or changes to existing files? | `Timestomping` |
| 2 | What malicious script can be planted by an attacker on the web server to maintain access to the compromised system and enables the web server to be accessed remotely? | `Web shell` |

### Task 6: Installation

**Explicación:** El atacante instala un backdoor o malware para asegurar la persistencia. La **web shell** también permite ejecutar comandos del sistema operativo en el objetivo a través de una interfaz de navegador. La defensa clave es el **allowlisting** (permitir solo aplicaciones aprobadas para evitar la ejecución de software no autorizado o malicioso).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What tactic allows attackers to execute operating system commands on a target via a web browser interface? | `web shell` |
| 2 | What technique is mentioned to prevent the execution of unauthorised or malicious software by only allowing approved applications to run? | `allowlisting` |

### Task 7: Command & Control (C2)

**Explicación:** El atacante establece el canal de comunicación con la víctima (C2 beaconing). El **DNS Tunneling** es la comunicación C2 donde la víctima hace solicitudes DNS regulares a un servidor y dominio pertenecientes al atacante. Para ocultar los datos como tráfico web cifrado se usa el protocolo **HTTPS**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the C2 communication where the victim makes regular DNS requests to a DNS server and domain which belong to an attacker? | `DNS Tunneling` |
| 2 | What protocol would the attacker use to smuggle his data as encrypted web traffic? | `HTTPS` |

### Task 8: Actions on Objectives (Exfiltration)

**Explicación:** El atacante ejecuta sus objetivos finales, desde la exfiltración de datos hasta la interrupción de servicios. En Windows, el **Shadow Copy** es una tecnología que crea copias de seguridad o snapshots de archivos o volúmenes, incluso mientras están en uso, y se usa en ataques de ransomware/backup.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Can you provide a technology included in Microsoft Windows that can create backup copies or snapshots of files or volumes on the computer, even when they are in use? | `Shadow Copy` |

### Task 9: Practice Analysis

**Explicación:** Práctica donde se identifican escenarios y se asigna cada uno a la fase correcta del Cyber Kill Chain. La flag es aleatoria por intento; el ejemplo mostrado es `THM{7HR347_1N73L_12_4w35om3}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the practice analysis. Flag is random per attempt (example). | `THM{7HR347_1N73L_12_4w35om3}` |

### Task 10: Conclusion

**Explicación:** Conclusión de la sala: repasa las siete fases y la utilidad defensiva del framework. Sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed - conclusion. | `No answer needed` |

---

**Metodología:**
1. **Reconnaissance:** la primera fase de un ataque; los adversarios recopilan información sobre infraestructura, empleados y tecnologías. Puede ser pasiva (WHOIS, scraping de redes sociales) o activa (ingeniería social, escaneo de puertos). Incluye OSINT (OSINT Framework) y email harvesting.
2. **Weaponization:** el atacante crea un payload o modifica uno existente basado en las vulnerabilidades del objetivo; incluye ofuscación y macros maliciosas en documentos de Office.
3. **Delivery:** el método para transmitir el payload: phishing emails, USB infectados, watering hole attacks.
4. **Exploitation:** el payload explota una vulnerabilidad; incluye timestomping (modificar atributos de tiempo de archivos) y web shells.
5. **Installation:** instalar un backdoor o malware para persistencia; defensa con application allowlisting.
6. **Command & Control (C2):** canal de comunicación con la víctima (C2 beaconing), con DNS tunnelling y HTTPS como canales modernos.
7. **Actions on Objectives (Exfiltration):** ejecutar los objetivos originales, desde exfiltración de datos hasta interrupción de servicios (ej. Shadow Copy de Windows).
8. Completar la práctica identificando la fase correcta de cada escenario (la flag es aleatoria por intento).

**Learning chain:** Reconnaissance (OSINT) → Weaponization (obfuscation, macro) → Delivery (watering hole) → Exploitation (timestomping, web shell) → Installation (allowlisting) → C2 (DNS tunneling, HTTPS) → Actions on Objectives (Shadow Copy, exfiltration).

**MITRE ATT&CK:** T1595 (Active Scanning), T1566 (Phishing), T1203 (Exploitation for Client Execution), T1070.006 (Indicator Removal: Timestomp), T1505.003 (Web Shell), T1071.001 (Application Layer Protocol: Web Protocols), T1041 (Exfiltration Over C2 Channel).

**Fuente:** [TryHackMe - Cyber Kill Chain](https://tryhackme.com/room/cyberkillchain)