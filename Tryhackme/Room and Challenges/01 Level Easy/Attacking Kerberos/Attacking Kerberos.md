# Attacking Kerberos

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `attackingkerberos` |
| **Link** | [TryHackMe](https://tryhackme.com/room/attackingkerberos) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Kerberos, TGT, SPN, PAC, AS-REP Roasting, Kerberoasting, Impacket, Hashcat |
| **Impacto** | Compromiso de un dominio Active Directory mediante ataques Kerberos: enumeración de usuarios, Kerberoasting y AS-REP Roasting para obtener y crackear tickets. |

---

**Contexto:** La sala enseña a atacar el protocolo **Kerberos** en un dominio Active Directory. Se repasan los conceptos clave (Ticket Granting Ticket, Service Principal Name, Privilege Attribute Certificate y los intercambios AS/TGS), se enumeran usuarios válidos con Kerbrute, y se ejecutan **Kerberoasting** y **AS-REP Roasting** con Impacket para capturar y crackear tickets con Hashcat, ganando finalmente acceso a cuentas comprometidas y recogiendo las flags.

## Solucionario

### Task 1: Conceptos de Kerberos / Kerberos Basics

**Explicación:** Se repasan los conceptos fundamentales del protocolo Kerberos: el **Ticket Granting Ticket (TGT)**, el **Service Principal Name (SPN)** que identifica de forma única a cada servicio, el **Privilege Attribute Certificate (PAC)** con los permisos del usuario y los dos intercambios del protocolo: **AS** y **TGS**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el ticket que permite obtener el resto de tickets del servicio? | `Ticket Granting Ticket` |
| 2 | ¿Qué componente hace que un servicio sea único dentro del dominio? | `Service Principal Name` |
| 3 | ¿Qué certificado contiene la información de los permisos/privilegios del usuario? | `Privilege Attribute Certificate` |
| 4 | ¿Cuáles son los dos procesos principales en los que se divide la autenticación Kerberos? | `AS, TGS` |
| 5 | Configurar el entorno y verificar la conectividad con el controlador de dominio. | `No answer needed` |

### Task 2: Enumeración de usuarios / User Enumeration

**Explicación:** Se utiliza la herramienta de enumeración Kerberos (Kerbrute) para validar cuentas contra el dominio. Se descubre que existen **10** usuarios válidos, entre ellos la cuenta de servicio **SQLService**, la cuenta de equipo **Machine2** y el usuario **User3**, que serán los objetivos de los ataques posteriores.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos usuarios válidos se detectan en el dominio? | `10` |
| 2 | ¿Qué cuenta de servicio se encuentra en la enumeración? | `SQLService` |
| 3 | ¿Qué cuenta de equipo aparece durante la enumeración? | `Machine2` |
| 4 | ¿Qué usuario válido se obtiene de la herramienta de enumeración? | `User3` |

### Task 3: Kerberoasting / Kerberoasting

**Explicación:** Mediante Kerberoasting se solicitan tickets de servicio (TGS) para las cuentas con SPN registrado. La cuenta **Administrator** aparece como SPN en el dominio y su ticket se solicita contra el servicio del host **CONTROLLER-1**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cuenta con SPN es el objetivo del Kerberoasting? | `Administrator` |
| 2 | ¿Qué host/servicio devuelve el SPN de la cuenta? | `CONTROLLER-1` |

### Task 4: AS-REP Roasting / AS-REP Roasting

**Explicación:** Se aplica AS-REP Roasting contra los usuarios que tienen deshabilitada la preautenticación Kerberos. A partir de los hashes AS-REP obtenidos se crackean las contraseñas **Summer2020** y **MYPassword123#**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué contraseña se obtiene al crackear el hash AS-REP? | `Summer2020` |
| 2 | ¿Qué contraseña se recupera a continuación? | `MYPassword123#` |

### Task 5: Kerberoasting con Impacket / Kerberoasting with Impacket

**Explicación:** Se repite el ataque de Kerberoasting usando las herramientas de Impacket (`GetUserSPNs`). El hash capturado es del tipo **Kerberos 5 AS-REP etype 23**, corresponde al usuario **User3** y al crackearlo se recupera la contraseña **Password3**. Después se ataca la cuenta **Admin2**, cuya contraseña crackeada es **P@$$W0rd2**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué modo de Hashcat corresponde al hash obtenido? | `Kerberos 5 AS-REP etype 23` |
| 2 | ¿Para qué usuario se obtiene el hash en este ataque? | `User3` |
| 3 | ¿Qué contraseña se crackea de este usuario? | `Password3` |
| 4 | ¿Qué cuenta se ataca a continuación? | `Admin2` |
| 5 | ¿Qué contraseña se crackea de esta cuenta? | `P@$$W0rd2` |

### Task 6: Cracking con Hashcat / Hashcat Cracking

**Explicación:** Se utilizan los archivos de mapeo y el diccionario correspondiente para crackear los tickets capturados con Hashcat, completando el paso práctico de recuperación de contraseñas. Sin respuesta numérica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Ejecutar Hashcat para crackear el ticket Kerberoasting de Admin2. | `No answer needed` |

### Task 7: Acceso como Admin2 / Admin2 Access

**Explicación:** Se autentica en el dominio con las credenciales de **Admin2** (contraseña `P@$$W0rd2`) y se accede a su perfil/escritorio, donde se encuentran las dos flags de la sala.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la primera flag de la cuenta Admin2? | `cd40c9ed96265531b21fc5b1dafcfb0a` |
| 2 | ¿Cuál es la segunda flag de la cuenta Admin2? | `2777b7fec870e04dda00cd7260f7bee6` |

### Task 8: Movimiento lateral / Lateral Movement

**Explicación:** Con las credenciales crackeadas se explora el acceso a otros recursos/servicios del dominio como parte del movimiento lateral. Paso de verificación práctica sin respuesta numérica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Completar los pasos de movimiento lateral con las credenciales obtenidas. | `No answer needed` |

### Task 9: Conclusión / Conclusion

**Explicación:** Recapitulación de los ataques Kerberos practicados y de la importancia de la preautenticación, los SPN y las políticas de contraseñas fuertes. No hay respuesta que enviar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el ticket que permite obtener el resto de tickets del servicio? | `Ticket Granting Ticket` |
| 2 | ¿Qué componente hace que un servicio sea único dentro del dominio? | `Service Principal Name` |
| 3 | ¿Qué certificado contiene la información de los permisos/privilegios del usuario? | `Privilege Attribute Certificate` |
| 4 | ¿Cuáles son los dos procesos principales en los que se divide la autenticación Kerberos? | `AS, TGS` |
| 5 | Configurar el entorno y verificar la conectividad con el controlador de dominio. | `No answer needed` |
| 6 | ¿Cuántos usuarios válidos se detectan en el dominio? | `10` |
| 7 | ¿Qué cuenta de servicio se encuentra en la enumeración? | `SQLService` |
| 8 | ¿Qué cuenta de equipo aparece durante la enumeración? | `Machine2` |
| 9 | ¿Qué usuario válido se obtiene de la herramienta de enumeración? | `User3` |
| 10 | ¿Qué cuenta con SPN es el objetivo del Kerberoasting? | `Administrator` |
| 11 | ¿Qué host/servicio devuelve el SPN de la cuenta? | `CONTROLLER-1` |
| 12 | ¿Qué contraseña se obtiene al crackear el hash AS-REP? | `Summer2020` |
| 13 | ¿Qué contraseña se recupera a continuación? | `MYPassword123#` |
| 14 | ¿Qué modo de Hashcat corresponde al hash obtenido? | `Kerberos 5 AS-REP etype 23` |
| 15 | ¿Para qué usuario se obtiene el hash en este ataque? | `User3` |
| 16 | ¿Qué contraseña se crackea de este usuario? | `Password3` |
| 17 | ¿Qué cuenta se ataca a continuación? | `Admin2` |
| 18 | ¿Qué contraseña se crackea de esta cuenta? | `P@$$W0rd2` |
| 19 | Ejecutar Hashcat para crackear el ticket Kerberoasting de Admin2. | `No answer needed` |
| 20 | ¿Cuál es la primera flag de la cuenta Admin2? | `cd40c9ed96265531b21fc5b1dafcfb0a` |
| 21 | ¿Cuál es la segunda flag de la cuenta Admin2? | `2777b7fec870e04dda00cd7260f7bee6` |
| 22 | Completar los pasos de movimiento lateral con las credenciales obtenidas. | `No answer needed` |
| 23 | Leer la conclusión de la sala. | `No answer needed` |

---

**Metodología:**

1. Se repasan los conceptos de Kerberos (TGT, SPN, PAC y los procesos AS/TGS) y se valida el entorno contra el controlador de dominio.
2. Se enumera el dominio con Kerbrute para descubrir usuarios válidos: **10** en total (SQLService, Machine2, User3, ...).
3. Se ejecuta **Kerberoasting** solicitando tickets de servicio para la cuenta con SPN (**Administrator** sobre **CONTROLLER-1**).
4. Se aplica **AS-REP Roasting** sobre cuentas sin preautenticación, crackeando `Summer2020` y `MYPassword123#`.
5. Con Impacket (`GetUserSPNs`) se captura un hash **Kerberos 5 AS-REP etype 23** de **User3** (`Password3`) y de **Admin2** (`P@$$W0rd2`), crackeados con Hashcat.
6. Se autentica como **Admin2** y se recogen las flags `cd40c9ed96265531b21fc5b1dafcfb0a` y `2777b7fec870e04dda00cd7260f7bee6`.

### Cadena de ataque / Attack Chain

```
Kerberos basics (TGT, SPN, PAC, AS/TGS)
  -> Validar entorno (dominio)
  -> Kerbrute -> 10 usuarios (SQLService, Machine2, User3)
  -> Kerberoasting -> Administrator / CONTROLLER-1
  -> AS-REP Roasting -> Summer2020, MYPassword123#
  -> Impacket GetUserSPNs -> hash etype 23 (User3/Admin2)
  -> Hashcat -> Password3, P@$$W0rd2
  -> Acceso como Admin2 -> flags
```

**Learning chain:** Conceptos Kerberos → Validación de dominio → Enumeración de usuarios → Kerberoasting → AS-REP Roasting → Impacket → Hashcat → Acceso Admin2 → Flags

**Lección:** *Los tickets Kerberos (AS-REP y TGS) pueden robarse y crackearse cuando las cuentas no usan preautenticación o exponen SPN; la protección pasa por cuentas de servicio con contraseñas largas, preautenticación Kerberos y monitorización de los eventos de ticket requests.*

**MITRE ATT&CK:** T1558.003 (Steal or Forge Kerberos Tickets: Kerberoasting), T1558.004 (AS-REP Roasting), T1558 (Steal or Forge Kerberos Tickets), T1078 (Valid Accounts)

**Fuente:** [TryHackMe - Attacking Kerberos](https://tryhackme.com/room/attackingkerberos)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.