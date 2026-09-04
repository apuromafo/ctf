# Cyber Kill Chain [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `cyberkillchainzmt`
* **Link:** https://tryhackme.com/room/cyberkillchainzmt
* **Sección / Section:** SOC Level 1 Path
* **Fuente / Source:** Writeup de Jasper (jalblas.com) + Dan Schwarzentraub (Medium) + Hubert Krauze

---

## Solucionario de Tareas / Task Solutions

> **ES:** Explora el Cyber Kill Chain de Lockheed Martin, un framework de ciberseguridad que divide un ataque en siete fases para ayudar a las organizaciones a defenderse. Es parte del path SOC Level 1.
> **EN:** Explore the Cyber Kill Chain by Lockheed Martin, a cybersecurity framework that divides an attack into seven phases to help organizations defend. Part of the SOC Level 1 path.

Las siete fases del Cyber Kill Chain:

1. **Reconnaissance** — el atacante recopila información sobre el objetivo
2. **Weaponization** — el atacante crea un payload o modifica uno existente
3. **Delivery** — el atacante envía el payload al objetivo
4. **Exploitation** — el payload explota una vulnerabilidad
5. **Installation** — el atacante instala un backdoor o malware para persistencia
6. **Command & Control (C2)** — el atacante controla el sistema comprometido
7. **Actions on Objectives** — el atacante ejecuta sus objetivos (exfiltración, etc.)

---

### Task 1 — Introduction

**Respuesta / Answer:** `No answer needed`

---

### Task 2 — Reconnaissance

La primera fase de un ataque: los adversarios recopilan información sobre infraestructura, empleados y tecnologías. Puede ser pasiva (WHOIS, scraping de redes sociales) o activa (ingeniería social, escaneo de puertos). Incluye OSINT y email harvesting.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the Intel Gathering Tool that is a web-based interface to the common tools and resources for open-source intelligence? | `OSINT Framework` |
| What is the definition for the email gathering process during the stage of reconnaissance? | `email harvesting` |

---

### Task 3 — Weaponization

El atacante crea un payload o modifica uno existente basado en las vulnerabilidades del sistema objetivo. Incluye técnicas como ofuscación y macros maliciosas en documentos de Office.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What technique is mentioned to evade detection by making it challenging to analyse the malicious code? | `Obfuscation` |
| What built-in feature makes creating a malicious MS Office document possible? | `Macro` |

---

### Task 4 — Delivery

El atacante decide el método para transmitir el payload o malware. Métodos comunes: phishing emails, USB infectados, watering hole attacks.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the name of the attack when it is performed against a specific group of people, and the attacker seeks to infect the website that the mentioned group of people is constantly visiting? | `Watering hole attack` |

---

### Task 5 — Exploitation

El payload explota una vulnerabilidad en el sistema objetivo. Incluye técnicas como timestomping (modificar atributos de tiempo de archivos) y web shells.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Can you provide the technique used to modify file time attributes to hide new or changes to existing files? | `Timestomping` |
| What malicious script can be planted by an attacker on the web server to maintain access to the compromised system and enables the web server to be accessed remotely? | `Web shell` |

---

### Task 6 — Installation

La explotación permite al atacante instalar un backdoor o malware para mantener persistencia. Técnicas de defensa: application allowlisting.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What tactic allows attackers to execute operating system commands on a target via a web browser interface? | `web shell` |
| What technique is mentioned to prevent the execution of unauthorised or malicious software by only allowing approved applications to run? | `allowlisting` |

---

### Task 7 — Command & Control (C2)

El atacante establece un canal de comunicación con el sistema de la víctima (C2 beaconing). Canales modernos incluyen DNS tunnelling y HTTPS.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the C2 communication where the victim makes regular DNS requests to a DNS server and domain which belong to an attacker? | `DNS Tunneling` |
| What protocol would the attacker use to smuggle his data as encrypted web traffic? | `HTTPS` |

---

### Task 8 — Actions on Objectives (Exfiltration)

El atacante ejecuta sus objetivos originales, desde exfiltración de datos hasta interrupción de servicios.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Can you provide a technology included in Microsoft Windows that can create backup copies or snapshots of files or volumes on the computer, even when they are in use? | `Shadow Copy` |

---

### Task 9 — Practice Analysis

Completar el sitio estático identificando la fase correcta de cada escenario. La flag es aleatoria por intento (ejemplo: `THM{7HR347_1N73L_12_4w35om3}`).

> **Flag (ejemplo / example):** `THM{7HR347_1N73L_12_4w35om3}` — "threat intel is awesome" (la inteligencia de amenazas es increíble). La flag varía en cada intento.

---

### Task 10 — Conclusion

**Respuesta / Answer:** `No answer needed`

---

## Metodología / Methodology

El Cyber Kill Chain ayuda a los defensores a romper la cadena de ataque en cada fase. Al conocer cada etapa, una organización tiene más posibilidades de interrumpir un ataque en curso. Se combina con otros frameworks (Unified Kill Chain, MITRE ATT&CK) para un enfoque más holístico.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
