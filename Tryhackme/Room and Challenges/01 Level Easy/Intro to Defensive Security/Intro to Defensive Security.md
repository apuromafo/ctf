# Intro to Defensive Security

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `defensivesecurity` |
| **Link** | [TryHackMe](https://tryhackme.com/room/defensivesecurity) |
| **Sección** | 01 Level Easy |
| **Fuente** | GitHub (EchoLynx-s), CYB3RM3 (lougerard.github.io), IritT (Medium), JesusGavancho (gitbook) |
| **Componentes** | Blue Team / SOC / SIEM / Threat Intelligence / DFIR / Malware Analysis / Ransomware |
| **Impacto** | Introduce los conceptos fundamentales de la seguridad defensiva (Blue Team): SOC, Inteligencia de Amenazas, DFIR y Análisis de Malware, con una simulación práctica de un SOC con SIEM. |

---

**Contexto:** Esta sala introduce los conceptos fundamentales de la seguridad defensiva (Blue Team), cubriendo el Centro de Operaciones de Seguridad (SOC), Inteligencia de Amenazas, Investigación Digital y Respuesta a Incidentes (DFIR), y Análisis de Malware. Incluye una simulación práctica de un SOC con un sistema SIEM.

## Solucionario

### Task 1: Introduction to Defensive Security

**Explicación:** La seguridad defensiva se opone a la seguridad ofensiva. Mientras la ofensiva se enfoca en romper sistemas (exploit de bugs, configuraciones inseguras, control de acceso deficiente), la defensiva se concentra en dos tareas principales: 1) Prevenir intrusiones y 2) Detectar intrusiones cuando ocurren y responder adecuadamente. El equipo de defensa se conoce como **Blue Team**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which team focuses on defensive security? | `Blue Team` |

### Task 2: Areas of Defensive Security

**Explicación:** Esta tarea cubre las principales áreas de la seguridad defensiva: **SOC** (monitoreo 24/7 con SIEM), **Inteligencia de Amenazas** (recopilar, procesar y analizar datos sobre adversarios), **DFIR** (investigación forense digital y respuesta a incidentes en 4 fases: preparación, detección, contención/recuperación y post-incidente), y **Análisis de Malware** (estático y dinámico). El **ransomware** es el malware que obliga al usuario a pagar para recuperar el acceso a sus archivos.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What would you call a team of cyber security professionals that monitors a network and its systems for malicious events? | `Security Operations Center` |
| 2 | What does DFIR stand for? | `Digital Forensics and Incident Response` |
| 3 | Which kind of malware requires the user to pay money to regain access to their files? | `Ransomware` |

### Task 3: Practical Example of Defensive Security

**Explicación:** Simulación práctica donde se actúa como analista de un SOC bancario con un dashboard SIEM que monitorea eventos de red y sistema en tiempo real. El flujo: 1) Inspeccionar alertas en el SIEM, 2) Identificar una IP maliciosa en los logs, 3) Confirmar que la actividad es maliciosa, 4) Reportar y escalar el incidente al equipo correspondiente, 5) Bloquear la IP maliciosa en el firewall.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the flag that you obtained by following along? | `THM{THREAT-BLOCKED}` |

---

**Metodología:**
1. **Comprensión del rol Blue Team:** entender que la seguridad defensiva se centra en prevenir, detectar y responder a incidentes, a diferencia del enfoque ofensivo.
2. **Conocimiento del SOC:** familiarizarse con el Centro de Operaciones de Seguridad como equipo central de monitoreo, su dashboard SIEM y los tipos de eventos que rastrea (vulnerabilidades, actividad no autorizada, intrusiones).
3. **Inteligencia de Amenazas:** aprender el ciclo de inteligencia: Recopilar datos (logs locales, fuentes públicas) → Procesar (normalizar) → Analizar (identificar TTPs) → Recomendar defensas.
4. **DFIR aplicado:** entender las 4 fases de respuesta a incidentes y cómo la forense digital analiza evidencia de sistemas de archivos, memoria, logs del sistema y logs de red.
5. **Análisis de Malware:** distinguir entre análisis estático (inspección sin ejecutar) y dinámico (ejecución controlada en sandbox).
6. **Práctica en SIEM:** interactuar con el dashboard SIEM, identificar alertas maliciosas, rastrear IPs sospechosas, escalar incidentes y aplicar reglas de bloqueo.
7. **Respuesta al incidente:** practicar el flujo completo: detectar → analizar → contener → erradicar → recuperar.

**Attack chain:** Monitorización SIEM (24/7) → Alerta detectada (evento rojo en dashboard) → Investigación del evento (identificar IP maliciosa) → Confirmación de actividad maliciosa → Escalación del incidente al equipo apropiado → Bloqueo de IP en firewall → Documentación y cierre del incidente.

**Lección:** La seguridad defensiva es un proceso continuo que requiere monitoreo constante, inteligencia de amenazas y una respuesta rápida y organizada ante incidentes; el SIEM es la herramienta central que permite visibilidad completa del entorno.

**MITRE ATT&CK:** T1566 (Phishing) y T1486 (Data Encrypted for Impact / ransomware) como amenazas típicas que detecta el SOC.

**Fuente:** [TryHackMe - Intro to Defensive Security](https://tryhackme.com/room/defensivesecurity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
