# XDR_ Credential Access [MEDIUM]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** MEDIUM
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `xdrcredentialaccess`
* **Link:** https://tryhackme.com/room/xdrcredentialaccess
* **Sección / Section:** SOC / XDR
* **Fuente / Source:** Web (simontaplin.net, jawstarsec.in, cherylmaiselobo.medium.com, RosanaFSS/TryHackMe_Cybersecurity_Journey)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Sala que enseña cómo los atacantes roban credenciales y cómo Microsoft Defender XDR (xPlaza XDR) ayuda a prevenirlo, detectarlo y responder. Cubre la táctica de Credential Access de MITRE ATT&CK, las técnicas de fuerza bruta y dumping de credenciales (LSASS, NTDS.dit), un laboratorio de detección e investigación de un password spray, y las mitigaciones (MFA, Credential Guard, ASR, Safe Links).
> **EN:** Room that teaches how attackers steal credentials and how Microsoft Defender XDR helps prevent, detect and respond to it. It covers the MITRE ATT&CK Credential Access tactic, brute force and credential dumping techniques (LSASS, NTDS.dit), a detection and investigation lab for a password spray, and the mitigations (MFA, Credential Guard, ASR, Safe Links).

---

### Task 1 — ¿Qué es Credential Access? / What is Credential Access

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| After a successful credential access tactic, can attackers blend in with legitimate users? (Yea/Nay) | `Yea` |
| What is the process of extracting credentials from system memory called? | `Credential dumping` |
| Credential access can lead to privilege escalation, lateral movement, and? | `Persistence` |

---

### Task 2 — Técnica: Fuerza Bruta / Technique: Brute Force

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What factor increases the time required to crack a password exponentially? | `password complexity` |
| What should be implemented to mitigate automated multiple login attempts? | `account lockout policies` |

---

### Task 3 — Técnica: Dumping de Credenciales / Technique: Credential Dumping

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| As security admins, what control can be implemented to prevent the use of dumped credentials? | `Multi-Factor Authentication` |
| What database do attackers target during NTDS dumping? | `NTDS.dit` |

---

### Task 4 — Laboratorio: Detectar e Investigar con Defender XDR / Lab: Detect and Investigate Using Defender XDR

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| What do you click to go to the advanced hunting page of a specific device from the alert page? | `Go hunt` |
| What is the name of the PowerShell script that was executed? | `WinPwn.ps1` |

---

### Task 5 — XDR: Prevenir, Detectar y Mitigar / XDR: Prevent, Detect, and Mitigate

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Which ASR rule will prevent the delivery of initial payloads that often include credential dumping tools? | `Block executable content from email client and webmail` |
| Which defender for Office 365 policy will block access to websites hosting malicious scripts or executables? | `Safe Links` |
| What should be configured to protect the Local Security Authority Subsystem Service from attackers and stop credential dumping memory? | `Credential Guard` |

---

## Metodología / Methodology

1. **Paso / Step:** Comprender la táctica Credential Access: tras obtener credenciales válidas, el atacante puede mezclarse con usuarios legítimos; el robo de credenciales desde memoria se llama credential dumping y, además de escalada y movimiento lateral, permite lograr persistencia. / Understand the Credential Access tactic: after obtaining valid credentials, the attacker can blend in with legitimate users; extracting credentials from memory is called credential dumping and, besides escalation and lateral movement, enables persistence.
2. **Paso / Step:** Analizar la fuerza bruta: la complejidad de la contraseña aumenta exponencialmente el tiempo de craqueo, y las políticas de bloqueo de cuentas (account lockout) mitigan los intentos de login automatizados. / Analyze brute force: password complexity exponentially increases cracking time, and account lockout policies mitigate automated login attempts.
3. **Paso / Step:** Estudiar el dumping de credenciales: los atacantes apuntan a LSASS en memoria o al fichero NTDS.dit de Active Directory; el control principal para neutralizar credenciales robadas es la autenticación multifactor (MFA). / Study credential dumping: attackers target LSASS in memory or the NTDS.dit Active Directory file; the main control to neutralize stolen credentials is multi-factor authentication (MFA).
4. **Paso / Step:** En el laboratorio, investigar un incidente multi-etapa (password spray) en el portal de Defender XDR: abrir la página del alert, revisar la línea de tiempo y el script PowerShell ejecutado (WinPwn.ps1) y usar "Go hunt" para llegar a la página de advanced hunting del dispositivo. / In the lab, investigate a multi-stage incident (password spray) in the Defender XDR portal: open the alert page, review the timeline and the executed PowerShell script (WinPwn.ps1) and use "Go hunt" to reach the device's advanced hunting page.
5. **Paso / Paso:** Aplicar las mitigaciones de Defender XDR: regla ASR "Block executable content from email client and webmail" para impedir payloads iniciales con herramientas de dumping, Safe Links para bloquear sitios con scripts/ejecutables maliciosos y Credential Guard para proteger LSASS del dumping en memoria. / Apply Defender XDR mitigations: ASR rule "Block executable content from email client and webmail" to prevent initial payloads carrying dumping tools, Safe Links to block sites hosting malicious scripts/executables, and Credential Guard to protect LSASS from in-memory dumping.

### Cadena de ataque / Attack Chain

```
Initial Access -> Credential Access (Tactic)
  -> Brute Force (T1110): complejidad = f(exponencial) -> mitigación: account lockout
  -> Credential Dumping (T1003):
       LSASS memory (Mimikatz/ProcDump) -> protege con Credential Guard
       NTDS.dit (DC) -> restringe acceso / MFA
  -> Credenciales robadas habilitan: Privilege Escalation + Lateral Movement + Persistence
  -> Controles XDR: MFA (neutraliza uso de credenciales robadas),
       ASR (bloquea payloads iniciales), Safe Links (bloquea descargas hostiles),
       Advanced Hunting (KQL) / Go hunt para correlación
  -> Incidente lab: Multi-stage (Execution & Lateral Movement) -> WinPwn.ps1 (password spray)
```

**Lección:** El acceso a credenciales es la puerta del atacante para escalar, moverse lateralmente y persistir simulando ser un usuario legítimo; una estrategia en capas de Microsoft Defender XDR (MFA, Credential Guard, ASR, Safe Links, hunting) es esencial para prevenirlo y detectarlo.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.