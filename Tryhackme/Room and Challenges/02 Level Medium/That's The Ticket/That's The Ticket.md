# That's The Ticket

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Ofensivo / Web | thatstheticket | https://tryhackme.com/room/thatstheticket | 02 Level Medium | TryHackMe | osTicket, Helpdesk, Credenciales por defecto, Autenticación | Acceso no autorizado al panel de soporte y compromiso de la app |

---

**Contexto:** La sala **That's The Ticket** ataca un **helpdesk (osTicket/IT support)** que quedó expuesto en la red: la aplicación mantiene cuentas de administrador con credenciales débiles o por defecto. El atacante identifica la cuenta admin y prueba la combinación débil (`adminaccount@itsupport.thm` / `123123`), entra en el panel de soporte sin autorización y obtiene la **flag** que acredita el compromiso del sistema de tickets.

## Solucionario

### Task 1: Acceso al panel de soporte
**Explicación:**

Se localiza la cuenta de administrador del helpdesk y se valida con credenciales débiles, accediendo al panel y capturando la flag que confirma la intrusión.

1. `adminaccount@itsupport.thm`
2. `123123`
3. `THM{6804f45260135ec8418da2d906328473}`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1.1 | Usuario administrador del helpdesk | `adminaccount@itsupport.thm` |
| 1.2 | Contraseña del administrador | `123123` |
| 1.3 | Flag del compromiso | `THM{6804f45260135ec8418da2d906328473}` |

---

**Metodología:** Reconocimiento de la aplicación de soporte, identificación de la cuenta admin, prueba de credenciales débiles/por defecto contra el panel y captura de la flag tras autenticarse.

**Learning chain:** Enumeración → hallazgo del helpdesk → identificación de la cuenta admin → fuerza de credenciales débiles → acceso → flag.

**Lección:** *Las credenciales por defecto en aplicaciones internas son la puerta abierta favorita del atacante: un admin-débil en el panel de tickets equivale a robo total de datos de soporte.*

**MITRE ATT&CK:** T1078 Valid Accounts · T1110.001 Brute Force (Password Guessing) · T1159 (legacy) · T1204 User Execution.

**Fuente:** [TryHackMe - That's The Ticket](https://tryhackme.com/room/thatstheticket)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.