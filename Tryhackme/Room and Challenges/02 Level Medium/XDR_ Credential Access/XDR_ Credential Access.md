# XDR: Credential Access

| **Dificultad** | Medium |
| **Tipo** | Walkthrough (Premium) |
| **Slug** | `xdrcredentialaccess` |
| **Link** | [TryHackMe](https://tryhackme.com/room/xdrcredentialaccess) |
| **Sección** | 02 Level Medium |
| **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | MITRE ATT&CK / Credential Access / brute force / credential dumping / LSASS / NTDS.dit / Defender XDR / MFA / ASR |
| **Impacto** | Aprender cómo los atacantes roban credenciales y cómo Microsoft Defender XDR previene, detecta y responde a la táctica de Credential Access |

---

**Contexto:** Sala que enseña cómo los atacantes roban credenciales y cómo Microsoft Defender XDR protege ante ello. Cubre la táctica de Credential Access de MITRE ATT&CK, técnicas de fuerza bruta y dumping de credenciales (LSASS, NTDS.dit), un laboratorio de detección e investigación de un password spray, y las mitigaciones (MFA, Credential Guard, ASR, Safe Links).

## Solucionario

### Task 1: ¿Qué es Credential Access? / What is Credential Access

**Explicación:**

Tras una táctica de credential access exitosa, los atacantes pueden mezclarse con usuarios legítimos (`Yea`). El proceso de extraer credenciales desde la memoria del sistema se llama `Credential dumping`. Además de escalada de privilegios y movimiento lateral, el acesso a credenciales permite lograr `Persistence`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | After a successful credential access tactic, can attackers blend in with legitimate users? (Yea/Nay) | `Yea` |
| 2 | What is the process of extracting credentials from system memory called? | `Credential dumping` |
| 3 | Credential access can lead to privilege escalation, lateral movement, and? | `Persistence` |

### Task 2: Técnica: Fuerza Bruta / Technique: Brute Force

**Explicación:**

La complejidad de la contraseña aumenta exponencialmente el tiempo requerido para craquearla. Las políticas de bloqueo de cuenta (`account lockout policies`) mitigan los intentos de login automatizados.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What factor increases the time required to crack a password exponentially? | `password complexity` |
| 2 | What should be implemented to mitigate automated multiple login attempts? | `account lockout policies` |

### Task 3: Técnica: Dumping de Credenciales / Technique: Credential Dumping

**Explicación:**

La autenticación multifactor (`Multi-Factor Authentication`) impide el uso de credenciales robadas. Durante el NTDS dumping, la base de datos objetivo es `NTDS.dit` (el almacén de AD del Domain Controller).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | As security admins, what control can be implemented to prevent the use of dumped credentials? | `Multi-Factor Authentication` |
| 2 | What database do attackers target during NTDS dumping? | `NTDS.dit` |

### Task 4: Laboratorio: Detectar e Investigar con Defender XDR / Lab: Detect and Investigate Using Defender XDR

**Explicación:**

En el laboratorio se investiga un incidente multi-etapa (password spray / execution & lateral movement) en el portal de Defender XDR. Desde la página del alert se hace clic en `Go hunt` para llegar a la página de advanced hunting del dispositivo. El script de PowerShell ejecutado por el atacante es `WinPwn.ps1`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What do you click to go to the advanced hunting page of a specific device from the alert page? | `Go hunt` |
| 2 | What is the name of the PowerShell script that was executed? | `WinPwn.ps1` |

### Task 5: XDR: Prevenir, Detectar y Mitigar / XDR: Prevent, Detect, and Mitigate

**Explicación:**

La regla ASR que impide la entrega de payloads iniciales con herramientas de dumping es `Block executable content from email client and webmail`. La política de Defender for Office 365 que bloquea sitios web que alojan scripts o ejecutables maliciosos es `Safe Links`. Para proteger el Local Security Authority Subsystem Service (LSASS) del dumping en memoria hay que configurar `Credential Guard`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which ASR rule will prevent the delivery of initial payloads that often include credential dumping tools? | `Block executable content from email client and webmail` |
| 2 | Which defender for Office 365 policy will block access to websites hosting malicious scripts or executables? | `Safe Links` |
| 3 | What should be configured to protect the Local Security Authority Subsystem Service from attackers and stop credential dumping memory? | `Credential Guard` |

---

**Metodología:**

1. **Comprender la táctica:** Tras obtener credenciales válidas, el atacante se mezcla con usuarios legítimos; el robo desde memoria es *credential dumping* y, además de escalada y movimiento lateral, habilita persistencia.
2. **Fuerza bruta (T1110):** la complejidad de la contraseña aumenta exponencialmente el tiempo de craqueo; las *account lockout policies* mitigan los intentos automatizados.
3. **Dumping (T1003):** los atacantes apuntan a LSASS en memoria (Mimikatz/ProcDump) o a `NTDS.dit` en el DC; el control principal que neutraliza credenciales robadas es el MFA.
4. **Laboratorio:** investigar un incidente multi-etapa (password spray) en Defender XDR: abrir el alert, revisar la línea de tiempo y el script `WinPwn.ps1`, y usar `Go hunt` para llegar a advanced hunting.
5. **Mitigaciones:** ASR *Block executable content from email client and webmail* (payloads iniciales), *Safe Links* (bloquea sitios hostiles) y *Credential Guard* (protege LSASS del dumping).

**Cadena de ataque:**

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

**MITRE ATT&CK:** T1110 (Brute Force) · T1003 (OS Credential Dumping: LSASS / DCSync-NTDS.dit) · T1078 (Valid Accounts) · CWE-521 (Weak Password Requirements) · CWE-522 (Insufficiently Protected Credentials)

**Fuente:** [TryHackMe - XDR: Credential Access](https://tryhackme.com/room/xdrcredentialaccess)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
