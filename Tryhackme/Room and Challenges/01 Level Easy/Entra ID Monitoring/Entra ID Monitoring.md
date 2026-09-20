# Entra ID Monitoring

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Medium | walkthrough | `entraidmonitoring` | [TryHackMe](https://tryhackme.com/room/entraidmonitoring) | Cloud Monitoring | THM | Microsoft Entra ID, sign-in logs, audit logs, risky sign-ins, CAP | Medium |

> **Objeto:** Aprender a monitorizar Microsoft Entra ID (antes Azure AD) mediante sign-in logs y audit logs: detectar password spraying y brute force, evaluar usuarios en riesgo, revisar Conditional Access Policies, identificar ataques MFA fatigue, y rastrear cuentas backdoor con consent grants maliciosos.

---

**Contexto:** Microsoft Entra ID (anteriormente Azure AD) es el directorio de identidad en la nube de Microsoft. Este room explora el monitoreo de eventos de inicio de sesión, riesgos de usuario, Conditional Access Policies y tráfico SOSPLA/MFA fatigue attacks. Se analizan logs de auditoría para detectar consent grants sospechosos y creación de cuentas backdoor por parte de un adversario.

> **ES:** Room de nivel Medium sobre monitorización de identidad en la nube. Se componen los sign-in logs para localizar el IP que hace password spraying (94.20.222.248) y el que fuerza brute force con throttling (38.165.231.218), hasta la cuenta comprometida (amanda.costa). Luego un usuario en riesgo (allan.senna, riesgo por IP anonimizada), una CAP que bloquea países sospechosos, un ataque MFA fatigue contra igor.bicalho y una cuenta backdoor (rafael.maciel) con rol Global Administrator y un consent grant (Mail.Read.All) para leer todos los buzones.
> **EN:** Medium room on cloud identity monitoring. Sign-in logs pinpoint the password-spraying IP (94.20.222.248) and the throttled brute force IP (38.165.231.218), up to the compromised account (amanda.costa). Then a risky user (allan.senna, risk from anonymized IP), a CAP blocking suspicious countries, an MFA fatigue attack against igor.bicalho and a backdoor account (rafael.maciel) with Global Administrator and a consent grant (Mail.Read.All) to read all mailboxes.

## Solucionario

### Task 1: Password Spraying y Brute Force / Password Spraying & Brute Force
**Explicación:** Se analizan los sign-in logs de Entra ID para distinguir patrones: el password spraying genera muchos intentos de login con pocas contraseñas desde una misma IP, y el brute force con throttling se reconoce por la elevada frecuencia de intentos fallidos desde otra IP. Finalmente se localiza cuál es el usuario cuya cuenta acabó comprometida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which IP address is performing a password spraying? / ¿Qué dirección IP realiza un password spraying? | `94.20.222.248` |
| 2 | Which IP address is performing a throttling brute force? / ¿Qué dirección IP realiza un brute force con throttling? | `38.165.231.218` |
| 3 | What is the user's email address that was compromised? / ¿Cuál es el email del usuario comprometido? | `amanda.costa@finegalo.thm` |

### Task 2: Usuarios en riesgo / Risky Users
**Explicación:** Se revisan las detecciones de riesgo (risk detections) para identificar al usuario marcado como peligroso en el tenant. En el sign-in riesgoso reciente se observa tanto el timestamp exacto como el tipo de riesgo: la IP aparece anonimizada (anonymizedIPAddress).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user email address that is at risk in the tenant? / ¿Cuál es el email del usuario en riesgo del tenant? | `allan.senna@finegalo.thm` |
| 2 | When was the last risky sign-in attempt from this risky user? / ¿Cuándo fue el último sign-in riesgoso de este usuario? | `2026-03-03 13:51:00.569` |
| 3 | What is the type of risk identified during this risky user sign-in based on risk detection logs? / ¿Qué tipo de riesgo se identificó según los logs de detección de riesgos? | `anonymizedIPAddress` |

### Task 3: Conditional Access Policy / Conditional Access Policy
**Explicación:** La CAP (Conditional Access Policy) "Block Suspicious Countries" fue la política que se aplicó y bloqueó los intentos de inicio de sesión del usuario en riesgo. En los registros del evento bloqueado se localiza la IP concreta que fue rechazada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the name of the CAP policy that was enforced and blocked some sign-in attempts from this risky user? / ¿Cuál es el nombre de la CAP que se aplicó y bloqueó intentos de sign-in de este usuario? | `Block Suspicious Countries` |
| 2 | What was the IP address that was blocked from signing in this risky user? / ¿Qué IP fue bloqueada al intentar iniciar sesión de este usuario bajo riesgo? | `94.20.222.251` |

### Task 4: Ataque MFA Fatigue / MFA Fatigue Attack
**Explicación:** El atacante bombardea al usuario con prompts de MFA repetidos (MFA fatigue o MFA push spam) para que termine aceptando uno. En los logs se identifica el usuario objetivo, el error de los prompts fallidos (500121), el país desde el que se conecta normalmente antes del ataque (DK) y el momento exacto en que el atacante consigue autenticarse por fin en la cuenta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which user was the target of an MFA fatigue attack? / ¿Qué usuario fue el objetivo del ataque MFA fatigue? | `igor.bicalho@finegalo.thm` |
| 2 | What is the error code of the failed MFA prompts? / ¿Cuál es el código de error de los prompts MFA fallidos? | `500121` |
| 3 | What is the country code that the user normally signs in before the attack? / ¿Cuál es el código de país desde el que el usuario inicia sesión normalmente antes del ataque? | `DK` |
| 4 | When does the attacker successfully authenticate in the user account? / ¿Cuándo consigue el atacante autenticarse en la cuenta del usuario? | `2026-03-04 13:26:22` |

### Task 5: Cuenta backdoor y consentimientos de aplicaciones / Backdoor Account & Application Consent
**Explicación:** Revisando los audit logs se reconstruye la persistencia del atacante: crea una cuenta backdoor (rafael.maciel), le asigna el rol Global Administrator, añade un nuevo dispositivo MFA para controlar la cuenta y concede permisos a una aplicación (consent grant) con Mail.Read.All para leer todos los buzones del tenant. El valor que permite rastrear todos los consentimientos en los audit logs es la actividad "Consent to application".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the user email address that the attacker created? / ¿Cuál es el email de la cuenta que creó el atacante? | `rafael.maciel@finegalo.thm` |
| 2 | Which role was assigned to this new account? / ¿Qué rol se asignó a esta nueva cuenta? | `Global Administrator` |
| 3 | When did the attacker add a new MFA device? / ¿Cuándo añadió el atacante un nuevo dispositivo MFA? | `2026-03-04 13:36:58` |
| 4 | Which permission allows an application to read all mailboxes within a tenant? / ¿Qué permiso permite a una aplicación leer todos los buzones del tenant? | `Mail.Read.All` |
| 5 | What is the activityDisplayName value you use to track all consent grants to applications within Entra ID audit logs? / ¿Qué valor activityDisplayName usas para rastrear todos los consentimientos a aplicaciones en los audit logs de Entra ID? | `Consent to application` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which IP address is performing a password spraying? | `94.20.222.248` |
| 2 | Which IP address is performing a throttling brute force? | `38.165.231.218` |
| 3 | What is the user's email address that was compromised? | `amanda.costa@finegalo.thm` |
| 4 | What is the user email address that is at risk in the tenant? | `allan.senna@finegalo.thm` |
| 5 | When was the last risky sign-in attempt from this risky user? | `2026-03-03 13:51:00.569` |
| 6 | What is the type of risk identified during this risky user sign-in based on risk detection logs? | `anonymizedIPAddress` |
| 7 | What is the name of the CAP policy that was enforced and blocked some sign-in attempts from this risky user? | `Block Suspicious Countries` |
| 8 | What was the IP address that was blocked from signing in this risky user? | `94.20.222.251` |
| 9 | Which user was the target of an MFA fatigue attack? | `igor.bicalho@finegalo.thm` |
| 10 | What is the error code of the failed MFA prompts? | `500121` |
| 11 | What is the country code that the user normally signs in before the attack? | `DK` |
| 12 | When does the attacker successfully authenticate in the user account? | `2026-03-04 13:26:22` |
| 13 | What is the user email address that the attacker created? | `rafael.maciel@finegalo.thm` |
| 14 | Which role was assigned to this new account? | `Global Administrator` |
| 15 | When did the attacker add a new MFA device? | `2026-03-04 13:36:58` |
| 16 | Which permission allows an application to read all mailboxes within a tenant? | `Mail.Read.All` |
| 17 | What is the activityDisplayName value you use to track all consent grants to applications within Entra ID audit logs? | `Consent to application` |

---

**Metodología:** Se analizan sign-in logs y audit logs de Microsoft Entra ID para rastrear un ataque completo: desde password spraying y brute force, pasando por la evaluación de riesgos de usuario y CAP enforcement, hasta la detección de un ataque MFA fatigue, creación de cuenta backdoor con Global Administrator y consent grants maliciosos para persistent access.

### Cadena de ataque / Attack Chain

```text
Password spraying (94.20.222.248) -> brute force throttling (38.165.231.218) -> compromiso de amanda.costa -> usuario en riesgo allan.senna (IP anonimizada) -> CAP "Block Suspicious Countries" (94.20.222.251) -> MFA fatigue sobre igor.bicalho (500121, éxito 2026-03-04 13:26:22) -> cuenta backdoor rafael.maciel (Global Admin + dispositivo MFA) -> consent grant Mail.Read.All -> persistencia
```

**Learning chain:** Sign-in logs → Risk detection → Conditional Access Policies → MFA fatigue attacks → Audit logs → Consent grants → Backdoor accounts.

**Lección:** *El monitoreo de Entra ID se basa en correlacionar sign-in logs y audit logs: distinguir password spraying de brute force, revisar detecciones de riesgo y CAP enforcement, reconocer MFA fatigue por la ráfaga de prompts fallidos y vigilar consent grants y roles elevados evita que un account takeover inicial se convierta en persistencia total.*

**MITRE ATT&CK:** T1110.003 - Password Spraying, T1621 - Multi-Factor Authentication Request Generation, T1136.003 - Cloud Account, T1098.003 - Additional Cloud Roles, T1550 - Use Alternate Authentication Material

**Fuente:** [TryHackMe - Entra ID Monitoring](https://tryhackme.com/room/entraidmonitoring)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.