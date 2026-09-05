# Intro to Defensive Security [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough
* **Slug:** `defensivesecurity`
* **Link:** https://tryhackme.com/room/defensivesecurity
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** GitHub (EchoLynx-s), CYB3RM3 (lougerard.github.io), IritT (Medium), JesusGavancho (gitbook)

## Solucionario de Tareas / Task Solutions

> **ES:** Esta sala introduce los conceptos fundamentales de la seguridad defensiva (Blue Team), cubriendo el Centro de Operaciones de Seguridad (SOC), Inteligencia de Amenazas, Investigación Digital y Respuesta a Incidentes (DFIR), y Análisis de Malware. Incluye una simulación práctica de un SOC con un sistema SIEM.
> **EN:** This room introduces fundamental concepts of defensive security (Blue Team), covering Security Operations Center (SOC), Threat Intelligence, Digital Forensics and Incident Response (DFIR), and Malware Analysis. It includes a practical SOC simulation with a SIEM system.

### Task 1 - Introduction to Defensive Security

> **ES:** La seguridad defensiva se opone a la seguridad ofensiva. Mientras la ofensiva se enfoca en romper sistemas (exploit de bugs, configuraciones inseguras, control de acceso deficiente), la defensiva se concentra en dos tareas principales: 1) Prevenir intrusiones y 2) Detectar intrusiones cuando ocurren y responder adecuadamente. El equipo de defensa se conoce como **Blue Team**.
> **EN:** Defensive security is the opposite of offensive security. While offensive focuses on breaking systems (exploiting bugs, insecure setups, poor access control), defensive concentrates on two main tasks: 1) Preventing intrusions and 2) Detecting intrusions when they occur and responding properly. The defense team is known as the **Blue Team**.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which team focuses on defensive security? | `Blue Team` |

### Task 2 - Areas of Defensive Security

> **ES:** Esta tarea cubre las principales áreas de la seguridad defensiva: SOC (monitoreo 24/7 con SIEM), Inteligencia de Amenazas (recopilar, procesar y analizar datos sobre adversarios), DFIR (investigación forense digital y respuesta a incidentes en 4 fases: preparación, detección, contención/recuperación, y post-incidente), y Análisis de Malware (estático y dinámico).
> **EN:** This task covers the main areas of defensive security: SOC (24/7 monitoring with SIEM), Threat Intelligence (collecting, processing, and analyzing data about adversaries), DFIR (digital forensics and incident response in 4 phases: preparation, detection, containment/recovery, and post-incident), and Malware Analysis (static and dynamic).

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What would you call a team of cyber security professionals that monitors a network and its systems for malicious events? | `Security Operations Center` |
| What does DFIR stand for? | `Digital Forensics and Incident Response` |
| Which kind of malware requires the user to pay money to regain access to their files? | `Ransomware` |

### Task 3 - Practical Example of Defensive Security

> **ES:** Se presenta una simulación práctica donde se actúa como analista de un SOC bancario. Se utiliza un dashboard SIEM para monitorear eventos de red y sistema en tiempo real. El flujo es: 1) Inspeccionar alertas en el SIEM, 2) Identificar una IP maliciosa en los logs, 3) Confirmar que la actividad es maliciosa, 4) Reportar y escalar el incidente al equipo correspondiente, 5) Bloquear la IP maliciosa en el firewall.
> **EN:** A practical simulation is presented where you act as a bank SOC analyst. A SIEM dashboard is used to monitor network and system events in real-time. The flow is: 1) Inspect alerts in the SIEM, 2) Identify a malicious IP in the logs, 3) Confirm the activity is malicious, 4) Report and escalate the incident, 5) Block the malicious IP on the firewall.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What is the flag that you obtained by following along? | `THM{THREAT-BLOCKED}` |

## Metodología / Methodology

1. **Paso / Step - Comprensión del rol Blue Team:** Entender que la seguridad defensiva se centra en prevenir, detectar y responder a incidentes, a diferencia del enfoque ofensivo.
2. **Paso / Step - Conocimiento del SOC:** Familiarizarse con el Centro de Operaciones de Seguridad como equipo central de monitoreo, su dashboard SIEM y los tipos de eventos que rastrea (vulnerabilidades, actividad no autorizada, intrusiones).
3. **Paso / Step - Inteligencia de Amenazas:** Aprender el ciclo de inteligencia: Recopilar datos (logs locales, fuentes públicas) -> Procesar (normalizar) -> Analizar (identificar TTPs) -> Recomendar defensas.
4. **Paso / Step - DFIR aplicado:** Entender las 4 fases de respuesta a incidentes y cómo la forense digital analiza evidencia de sistemas de archivos, memoria, logs del sistema y logs de red.
5. **Paso / Step - Análisis de Malware:** Distinguir entre análisis estático (inspección sin ejecutar) y dinámico (ejecución controlada en sandbox).
6. **Paso / Step - Práctica en SIEM:** Interactuar con el dashboard SIEM, identificar alertas maliciosas, rastrear IPs sospechosas, escalar incidentes y aplicar reglas de bloqueo.
7. **Paso / Step - Respuesta al incidente:** Practicar el flujo completo: detectar -> analizar -> contener -> erradicar -> recuperar.

### Cadena de ataque / Attack Chain

```
Monitorización SIEM (24/7)
        |
        v
Alerta detectada (evento rojo en dashboard)
        |
        v
Investigación del evento (identificar IP maliciosa)
        |
        v
Confirmación de actividad maliciosa
        |
        v
Escalación del incidente al equipo apropiado
        |
        v
Bloqueo de IP en firewall
        |
        v
Documentación y cierre del incidente
```

**Lección:** La seguridad defensiva es un proceso continuo que requiere monitoreo constante, inteligencia de amenazas y una respuesta rápida y organizada ante incidentes; el SIEM es la herramienta central que permite可视ibilidad completa del entorno.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
