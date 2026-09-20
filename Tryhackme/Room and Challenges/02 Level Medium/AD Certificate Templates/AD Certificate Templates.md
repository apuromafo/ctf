# AD Certificate Templates

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Ofensivo / Active Directory | adcertificatetemplates | https://tryhackme.com/room/adcertificatetemplates | 02 Level Medium | TryHackMe | AD CS, Certificados, PKI, Kerberos | Escalada a Domain Admin vía misconfiguration de plantillas |

---

**Contexto:** La sala **AD Certificate Templates** enseña a explotar plantillas de certificados mal configuradas en **Active Directory Certificate Services (AD CS)**. Un plantilla con permisos de enrolamiento para usuarios normales y parámetros inseguros (SAN editable) permite al atacante solicitar un certificado a nombre de un **Domain Admin** y autenticarse con él, equivalente a un robo de credenciales Kerberos. La práctica recorre la anatomía del ataque ESC1: qué solicita el certificado, quién puede pedirlo, qué lo vuelve abusable y cómo se materializa la escalada.

## Solucionario

### Task 1: Introducción a AD CS
**Explicación:**

Se revisa el rol de los Servicios de Certificados dentro del dominio y cómo las plantillas mal configuradas se convierten en un vector ofensivo.

Respuesta: `No answer needed`

### Task 2: Conceptos del ataque
**Explicación:**

Se identifican los términos clave que intervienen en el flujo de emisión de un certificado.

1. `No answer needed`
2. `Certificate Signing Request`
3. `Active Directory Certificate Services`

### Task 3: Plantilla vulnerable
**Explicación:**

Se audita la plantilla explotable comprobando quién tiene permiso para enrolarse y qué usos se permiten. La plantilla vulnerable permite que **Domain Users** y **Domain Computers** soliciten un certificado con propósito **Client Authentication** mediante una solicitud de tipo **User Request**.

1. `Domain Users`
2. `Domain Computers`
3. `Client Authentication`
4. `User Request`

### Task 4: El vector de abuso
**Explicación:**

Se identifica el campo que permite suplantar a otra identidad: el **Subject Alternative Name** (SAN) del certificado, que puede apuntar a una **Computer account** privilegiada para forjar una credencial de Domain Admin.

1. `Subject Alternative Name`
2. `Computer account`
3. `No answer needed`

### Task 5: Flag de la sala
**Explicación:**

Tras materializar el ataque se obtiene la flag que acredita el compromiso del dominio a través de los certificados.

Respuesta: `THM{AD.Certs.Can.Get.You.DA}`

### Task 6: Emisión del certificado
**Explicación:**

Se solicita el certificado con la herramienta de explotación (p. ej. `Certify`), indicando el SAN a suplantar, y se obtiene el `.pfx` firmado por la CA.

1. `No answer needed`
2. `No answer needed`

### Task 7: Autenticación con el certificado
**Explicación:**

Se convierte el certificado a formato utilizable (Rubeus / `openssl`) y se solicita un TGT Kerberos como el usuario privilegiado forjado, confirmando el acceso equivalente a Domain Admin.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea introductoria | `No answer needed` |
| 2.1 | Primer concepto teórico | `No answer needed` |
| 2.2 | ¿Qué se envía a la CA para pedir un certificado? | `Certificate Signing Request` |
| 2.3 | ¿Qué servicio emite los certificados en AD? | `Active Directory Certificate Services` |
| 3.1 | ¿Quiénes pueden enrolarse en la plantilla vulnerable? | `Domain Users` |
| 3.2 | ¿Qué identidades adicionales pueden enrolarse? | `Domain Computers` |
| 3.3 | ¿Qué uso tiene el certificado emitido? | `Client Authentication` |
| 3.4 | ¿Qué tipo de solicitud se emplea? | `User Request` |
| 4.1 | Campo que permite suplantar identidad | `Subject Alternative Name` |
| 4.2 | Identidad que se suplanta con el SAN | `Computer account` |
| 4.3 | Pregunta conceptual de cierre | `No answer needed` |
| 5 | Flag de la sala | `THM{AD.Certs.Can.Get.You.DA}` |
| 6 | Tarea de emisión del certificado | `No answer needed` |
| 7 | Tarea de autenticación Kerberos | `No answer needed` |

---

**Metodología:** Auditoría ofensiva de PKI/AD (enrolamiento, SAN controlable, EKU de cliente), emisión de certificado forjado y autenticación Kerberos; alineado con el flujo ESC1 de certificados AD.

**Learning chain:** Conceptos AD CS → anatomy del attack → plantilla vulnerable → SAN spoofing → emisión → pfx/TGT → escalada a DA.

**Lección:** *Una plantilla de certificados mal configurada es una credencial por defecto: quien puede enrolarse a sí mismo, puede suplantar a Domain Admin.*

**MITRE ATT&CK:** T1649 Steal or Forge Authentication Certificates · T1558 Steal or Forge Kerberos Tickets · T1587 Develop Capabilities.

**Fuente:** [TryHackMe - AD Certificate Templates](https://tryhackme.com/room/adcertificatetemplates)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.