# Zero Logon

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto • Active Directory | zer0logon | https://tryhackme.com/room/zer0logon | 03 Level Hard | TryHackMe | Zerologon, CVE-2020-1472, Netlogon, NetrServerPasswordSet2, Escalada de privilegios, Controlador de dominio | Alto |

---

**Contexto:**
> **ES:** Laboratorio sobre la vulnerabilidad Zerologon (CVE-2020-1472) en el protocolo Netlogon: teoría del mensaje NetrServerPasswordSet2, enumeración del controlador de dominio (DC01, HOLOLIVE / hololive.local) y explotación para neutralizar la autenticación Netlogon y elevar privilegios.
> **EN:** Lab on the Zerologon vulnerability (CVE-2020-1472) in the Netlogon protocol: theory behind the NetrServerPasswordSet2 message, domain controller enumeration (DC01, HOLOLIVE / hololive.local) and exploitation to zero out the Netlogon authentication and gain privileges.

## Solucionario

### Task 1: Visión general / Overview
**Explicación:**
1. No answer needed

### Task 2: Preparación del laboratorio / Lab setup
**Explicación:**
1. No answer needed

### Task 3: Teoría de Netlogon / Netlogon theory
**Explicación:**
1. NetrServerPasswordSet2
2. PrimaryName, AccountName, SecureChannelType, ComputerName, Authenticator, ReturnAuthenticator, ClearNewPassword
3. 30
4. No answer needed

### Task 4: Explotación Zerologon / Zerologon exploitation
**Explicación:**
1. DC01
2. HOLOLIVE
3. hololive.local
4. 3f3ef89114fb063e3d7fc23c20f65568
5. 2
6. THM{Zer0Log0nD4rkTh1rty}

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |
| 2 | `No answer needed` |
| 3.1 | `NetrServerPasswordSet2` |
| 3.2 | `PrimaryName, AccountName, SecureChannelType, ComputerName, Authenticator, ReturnAuthenticator, ClearNewPassword` |
| 3.3 | `30` |
| 3.4 | `No answer needed` |
| 4.1 | `DC01` |
| 4.2 | `HOLOLIVE` |
| 4.3 | `hololive.local` |
| 4.4 | `3f3ef89114fb063e3d7fc23c20f65568` |
| 4.5 | `2` |
| 4.6 | `THM{Zer0Log0nD4rkTh1rty}` |

---

**Metodología:**
Estudio de los campos del mensaje NetrServerPasswordSet2 (con hasta 30 reintentos), enumeración del dominio y ejecución del exploit que pone a cero el secreto de la cuenta de la máquina del DC para elevar privilegios.

### Cadena de ataque / Attack Chain
1. Comprensión del flujo Netlogon y del mensaje vulnerable.
2. Enumeración del dominio (DC01 / HOLOLIVE / hololive.local).
3. Ejecución del exploit Zerologon para neutralizar el secreto de la cuenta del DC.
4. Validación del compromiso y extracción de la flag.

**Learning chain:**
Teoría Netlogon → Enumeración del DC → Exploit CVE-2020-1472 → Compromiso total.

**Lección:** *Zerologon convierte un fallo criptográfico en la negociación Netlogon en un compromiso total del controlador de dominio en segundos.*

**MITRE ATT&CK:**
- T1210 (Exploitation of Remote Services), T1098 (Account Manipulation), T1078 (Valid Accounts).

**Fuente:** [TryHackMe - Zero Logon](https://tryhackme.com/room/zer0logon)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.