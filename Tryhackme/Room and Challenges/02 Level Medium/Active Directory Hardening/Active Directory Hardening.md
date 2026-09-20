# Active Directory Hardening

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Defensivo / Hardening | activedirectoryhardening | https://tryhackme.com/room/activedirectoryhardening | 02 Level Medium | TryHackMe | Active Directory, GPO, Cuentas de usuario, Políticas de contraseñas | Reducción de superficie post-explotación AD |

---

**Contexto:** La sala **Active Directory Hardening** es un ejercicio defensivo donde, partiendo de un dominio corporativo ya comprometido, el alumno aplica medidas de hardening para cerrar las vías de ataque: bloqueo de cuentas de usuario, políticas de contraseñas, perfiles de firewall, configuración DNS y verificación de GPOs. Cada tarea exige responder con datos reales del entorno (nombres, cuentas afectadas, conteos y flags de verificación) para confirmar que las disposiciones defensivas quedaron aplicadas correctamente.

## Solucionario

### Task 1: Preparación del entorno
**Explicación:**

Se configuran las credenciales y se accede al host del dominio para empezar a inspeccionar el estado de seguridad actual del Active Directory.

Respuesta: `No answer needed`

### Task 2: Verificación del dominio
**Explicación:**

Se identifica el FQDN / dominio interno para orientar todas las comprobaciones de GPO, DNS y LDAP posteriores.

Respuesta: `tryhackme.loc`

### Task 3: Comprobación de configuraciones
**Explicación:**

Se revisan los ajustes de hardening aplicados sobre las cuentas y las políticas de seguridad del dominio, anotando en primer lugar una acción descriptiva y, a continuación, el conteo de elementos afectados que arroja la comprobación.

1. `No answer needed`
2. `7`

### Task 4: Vulnerabilidades de cuenta
**Explicación:**

Se verifican cuentas o configuraciones que continúan expuestas tras el endurecimiento inicial, respondiendo afirmativa o negativamente según el estado real detectado en el entorno.

1. `nay`
2. `nay`

### Task 5: Flags de verificación
**Explicación:**

Se recogen las flags de confirmación obtenidas al aplicar correctamente las medidas de endurecimiento sobre el dominio.

1. `THM{00001}`
2. `{THM00191}`

### Task 6: Estado post-hardening
**Explicación:**

Se ejecutan las comprobaciones finales de la política aplicada (acceso por red, firewall / puertos), confirmando el estado y anotando el valor numérico que devuelve la verificación.

1. `yea`
2. `186`

### Task 7: Cierre
**Explicación:**

Se da por concluida la ronda de hardening y se consolida el resultado de la práctica.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Tarea de preparación inicial | `No answer needed` |
| 2 | ¿Cuál es el dominio/FQDN del entorno? | `tryhackme.loc` |
| 3.1 | Tarea descriptiva intermedia | `No answer needed` |
| 3.2 | Conteo de elementos afectados | `7` |
| 4.1 | ¿La cuenta/configuración sigue vulnerable? | `nay` |
| 4.2 | ¿La cuenta/configuración sigue vulnerable? | `nay` |
| 5.1 | Flag de verificación 1 | `THM{00001}` |
| 5.2 | Flag de verificación 2 | `{THM00191}` |
| 6.1 | ¿Quedó aplicada la política correctamente? | `yea` |
| 6.2 | Conteo/valor de la verificación | `186` |
| 7 | Tarea final de cierre | `No answer needed` |

---

**Metodología:** Auditoría defensiva de Active Directory, revisión de GPO y políticas de cuentas, verificación de firewall/DNS y validación post-cambio con flags de confirmación (método NIST SP 800-115 en enfoque "find and fix").

**Learning chain:** Ataque (contexto del público) → endurecimiento de cuentas → políticas de contraseñas → verificación GPO → comprobación de red → validación de cambios → cierre.

**Lección:** *Hardening no es tocar un checkbox: cada política debe verificarse sobre el dominio real con datos observables.*

**MITRE ATT&CK:** T1078 Valid Accounts · T1098 Account Manipulation · T1110 Brute Force (mitigación GPO).

**Fuente:** [TryHackMe - Active Directory Hardening](https://tryhackme.com/room/activedirectoryhardening)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.