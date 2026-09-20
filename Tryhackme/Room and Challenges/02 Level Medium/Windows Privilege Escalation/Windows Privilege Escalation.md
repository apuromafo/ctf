# Windows Privilege Escalation

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Explotación | windowsprivilegeescalation | https://tryhackme.com/room/windowsprivilegeescalation | 02 Level Medium | TryHackMe | Windows, escalada de privilegios, logon alternativo, contraseñas, servicios, SeBackupPrivilege, DLL hijacking, tareas | Escalada de privilegios local hasta SYSTEM/administrador |

---

**Contexto:** La sala **Windows Privilege Escalation** enseña las técnicas fundamentales de escalada de privilegios en sistemas Windows: acceso por logon alternativo, búsqueda de contraseñas en el sistema, abuso de servicios mal configurados (permisos de binario, rutas sin comillas, configuración de servicio), explotación de privilegios como SeBackupPrivilege y secuestro de DLL. Cada tarea se valida en la máquina de laboratorio y se confirma con flags concretas.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Presentación de la sala y de los vectores de escalada de privilegios que se practicarán. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 2: Acceso por logon alternativo / Alternate logon
**Explicación:**

Se practica el acceso con credenciales alternativas utilizando los tokens almacenados de otros usuarios. La pregunta inicial verifica el grupo del usuario y si dispone de credenciales guardadas.

1. `Administrators`
2. `aye`

### Task 3: Búsqueda de contraseñas / Password hunting
**Explicación:**

Se audita el sistema buscando contraseñas almacenadas en texto plano: archivos de configuración, historial y credenciales de cuentas de servicio.

1. `ZuperCkretPa5z`
2. `098n0x35skjD3`
3. `THM{WHAT_IS_MY_PASSWORD}`
4. `CoolPass2021`

### Task 4: Superficie de ataque / Attack surface
**Explicación:**

Tras consolidar el acceso, se completa la tarea de enumeración de la superficie atacable con su flag de confirmación.

Respuesta: `THM{TASK_COMPLETED}`

### Task 5: Abuso de servicios / Abusing services
**Explicación:**

Se explotan los servicios con configuraciones inseguras: binarios con permisos débiles, rutas sin comillas y parámetros de arranque modificables.

1. `THM{AT_YOUR_SERVICE}`
2. `THM{QUOTES_EVERYWHERE}`
3. `THM{INSECURE_SVC_CONFIG}`

### Task 6: Privilegios con SeBackupPrivilege / SeBackupPrivilege
**Explicación:**

Se abusa del privilegio SeBackupPrivilege para leer archivos de otro usuario (incluido el SAM) y escalar privilegios.

Respuesta: `THM{SEFLAGPRIVILEGE}`

### Task 7: Secuestro de DLL / DLL hijacking
**Explicación:**

Se secuestra una DLL cargada por una aplicación en un directorio en el que se tienen permisos de escritura, reemplazándola por una maliciosa para ejecutar código con los privilegios del proceso.

Respuesta: `THM{EZ_DLL_PROXY_4ME}`

### Task 8: Escalada por tareas / Task-based escalation
**Explicación:**

Se analizan las tareas programadas del sistema en busca de vectores de escalada. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 9: Cierre / Conclusion
**Explicación:**

Recapitulación final de la sala y consolidación de los conceptos. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a la escalada de privilegios | `No answer needed` |
| 2.1 | Grupo del usuario con credenciales alternativas | `Administrators` |
| 2.2 | ¿Dispone el usuario de credenciales guardadas? | `aye` |
| 3.1 | Contraseña en texto plano encontrada 1 | `ZuperCkretPa5z` |
| 3.2 | Contraseña en texto plano encontrada 2 | `098n0x35skjD3` |
| 3.3 | Flag de contraseña de la tarea | `THM{WHAT_IS_MY_PASSWORD}` |
| 3.4 | Contraseña en texto plano encontrada 3 | `CoolPass2021` |
| 4 | Surface de ataque completada | `THM{TASK_COMPLETED}` |
| 5.1 | Flag del binario de servicio con permisos débiles | `THM{AT_YOUR_SERVICE}` |
| 5.2 | Flag de la ruta sin comillas | `THM{QUOTES_EVERYWHERE}` |
| 5.3 | Flag de la configuración de servicio insegura | `THM{INSECURE_SVC_CONFIG}` |
| 6 | Flag del privilegio SeBackupPrivilege | `THM{SEFLAGPRIVILEGE}` |
| 7 | Flag del secuestro de DLL | `THM{EZ_DLL_PROXY_4ME}` |
| 8 | Revisión de tareas programadas | `No answer needed` |
| 9 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Enumeración de usuarios, grupos y credenciales guardadas; búsqueda de contraseñas en el sistema; abuso de servicios con permisos débiles, rutas sin comillas y configuraciones inseguras; explotación de SeBackupPrivilege para leer archivos restringidos y secuestro de DLL en directorios escribibles para ejecutar código como el proceso víctima.

### Cadena de ataque / Attack Chain

```text
Logon alternativo (tokens/credenciales) → búsqueda de contraseñas → superficie de ataque → abuso de servicios → SeBackupPrivilege → DLL hijacking → tareas → SYSTEM
```

**Learning chain:** Alternate logon → password hunting → ataque a servicios → SeBackupPrivilege → DLL hijacking → escalada por tareas → consolidación.

**Lección:** *Cada configuración heredada, credencial duplicada o servicio demasiado permisivo en Windows es un vector: la escalada rara vez requiere exploits, solo observación metódica.*

**MITRE ATT&CK:** T1543.003 Create or Modify System Process: Windows Service · T1574.001 DLL Search Order Hijacking · T1068 Exploitation for Privilege Escalation · T1003 OS Credential Dumping · T1078 Valid Accounts · T1552 Unsecured Credentials · T1053.005 Scheduled Task/Job.

**Fuente:** [TryHackMe - Windows Privilege Escalation](https://tryhackme.com/room/windowsprivilegeescalation)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.