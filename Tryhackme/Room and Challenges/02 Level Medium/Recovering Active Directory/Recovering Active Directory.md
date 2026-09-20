# Recovering Active Directory

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Room / Recuperación AD | recoveringactivedirectory | https://tryhackme.com/room/recoveringactivedirectory | 02 Level Medium | TryHackMe | Active Directory, Backup (wbadmin), Restauración de sistema, Event Viewer, DCSync, Silver ticket | Recuperación del control sobre el dominio y restauración del servicio de autenticación |

> **Objeto:** Recuperar un Active Directory comprometido: conectar con el controlador de dominio, restaurar el estado del dominio a partir de los backups disponibles y evaluar las respuestas de seguridad; validar la recuperación capturando la flag final del laboratorio.

---

**Contexto:** La sala **Recovering Active Directory** es un laboratorio de defensa (blue team) centrado en el proceso de recuperación de un dominio de Active Directory tras un compromiso. El flujo pasa por conectarse al DC, localizar y usar las herramientas de backup nativas (`wbadmin.msc`), restaurar el sistema de archivos / estado del sistema desde las copias disponibles, revisar el historial de eventos relevantes y ejecutar el cambio de la contraseña de la cuenta de equipo además de validar la supresión de credenciales de servicio. Las preguntas mezclan valores literales (respuestas concretas como `C`, `11`, `Event Viewer`, `DCSync`) con confirmaciones de ejecución (`yea`).

## Solucionario

### Task 1: Conexión inicial / Initial connection
**Explicación:**

Primera parte del laboratorio: no requiere respuesta (solo montaje/arranque) y a continuación se valida el acceso al recurso comprometido.

1. `No answer needed`
2. `THM{I_CAN_CONNECT}`

### Task 2: Backup / Restauración
**Explicación:**

Identificación del volumen o unidad donde se encuentra el backup y de la herramienta de restauración utilizada (`wbadmin.msc`); la última pregunta confirma la ejecución de la restauración.

1. `C`
2. `wbadmin.msc`
3. `yea`

### Task 3: Versión del backup / Selección de la instantánea
**Explicación:**

Se indica el número de la versión/instantánea del backup a restaurar y la utilidad usada para consultar los eventos relacionados con el proceso de recuperación.

1. `11`
2. `Event Viewer`

### Task 4: Credenciales y evento / Credentials and event
**Explicación:**

Se recuperan las credenciales de los backups (usuario `hack@crypto`), el número de evento relevante y el identificador del evento de PowerShell (`4757`).

1. `hack@crypto`
2. `1`
3. `4757`

### Task 5: Contraseña de la cuenta de equipo / Machine account password
**Explicación:**

No requiere respuesta, seguido del cmdlet de PowerShell que regenera la contraseña de la cuenta de máquina (`Reset-ComputerMachinePassword`) y la técnica de ataque que se invalida con ello (`Silver ticket abuse`).

1. `No answer needed`
2. `Reset-ComputerMachinePassword`
3. `Silver ticket abuse`

### Task 6: Restauración del control directorio / Directory restoration
**Explicación:**

La operación de restauración del estado del dominio equivale a recuperar el acceso de escritura (replicación) del mismo tipo que permite un ataque `DCSync`; la segunda respuesta confirma la finalización correcta.

1. `DCSync`
2. `yea`

### Task 7: Flag final / Final flag
**Explicación:**

Una vez completada la recuperación del dominio se obtiene la flag final que acredita el éxito del proceso.

`THM{I_HAVE_RECOVERED_AD}`

### Task 8: Cierre / Wrap-up
**Explicación:**

Última pregunta de confirmación del laboratorio, sin respuesta obligatoria.

`No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Conexión inicial (preparación) | `No answer needed` |
| 2 | Conexión inicial (flag) | `THM{I_CAN_CONNECT}` |
| 3 | Unidad / volumen del backup | `C` |
| 4 | Herramienta de restauración | `wbadmin.msc` |
| 5 | Confirmación de restauración | `yea` |
| 6 | Versión del backup | `11` |
| 7 | Visualización de eventos | `Event Viewer` |
| 8 | Usuario de las credenciales | `hack@crypto` |
| 9 | Número de evento | `1` |
| 10 | Evento de PowerShell | `4757` |
| 11 | Reseteo de contraseña (preparación) | `No answer needed` |
| 12 | Cmdlet de reseteo | `Reset-ComputerMachinePassword` |
| 13 | Técnica invalidada | `Silver ticket abuse` |
| 14 | Operación de replicación | `DCSync` |
| 15 | Confirmación de finalización | `yea` |
| 16 | Flag final | `THM{I_HAVE_RECOVERED_AD}` |
| 17 | Cierre | `No answer needed` |

---

**Metodología:** Conexión al controlador de dominio, localización del backup y restauración con `wbadmin.msc`, comprobación de la versión restaurada y revisión de eventos, recuperación de credenciales de backup, regeneración de la contraseña de la cuenta de equipo y verificación del estado del dominio con la flag final.

**Learning chain:** Acceso al DC → respaldo y restauración con wbadmin → revisión de eventos y credenciales → regeneración de secretos (machine password) → invalidación de Silver Ticket → recuperación verificada.

**Lección:** *Tras un compromiso de AD no basta con limpiar artefactos: hay que restaurar secretos (contraseña de máquina, credenciales de servicio) para invalidar mecanismos de persistencia como los Silver Tickets y el acceso DCSync.*

**MITRE ATT&CK:** T1006 Indirect Data exfiltration · T1078 Valid Accounts · T1068 Exploitation for Privilege Escalation · T1558 Steal or Forge Kerberos Tickets.

**Fuente:** [TryHackMe - Recovering Active Directory](https://tryhackme.com/room/recoveringactivedirectory)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.