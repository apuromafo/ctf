# Windows PrivEsc

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / Explotación | windowsprivesc | https://tryhackme.com/room/windowsprivesc | 02 Level Medium | TryHackMe | Windows, escalada de privilegios, servicios, DACL, rutas sin comillas, credenciales, tokens, privilegios | Escalada de privilegios local hasta SYSTEM/administrador |

---

**Contexto:** La sala **Windows PrivEsc** es un ejercicio práctico de escalada de privilegios en Windows que cubre las técnicas clásicas: abuso de servicios con DACL débiles, rutas de servicio sin comillas, credenciales en texto plano, hashes y privilegios de token. En cada tarea se explota uno de los vectores sobre la máquina de laboratorio y se responde con el dato concreto obtenido (rutas, contraseñas, hashes o privilegios).

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Presentación de la sala y de los vectores de escalada de privilegios que se van a practicar. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 2: Enumeración inicial / Initial enumeration
**Explicación:**

Primera fase de enumeración del sistema para reunir información sobre el usuario, el sistema y los servicios. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 3: Servicio con DACL débil / Weak DACL service
**Explicación:**

Se identifica un servicio cuya lista de control de acceso permite a usuarios sin privilegios modificar su configuración; se anota la ruta del binario del servicio vulnerable.

Respuesta: `C:\Program Files\DACL Service\daclservice.exe`

### Task 4: Servicio con ruta sin comillas / Unquoted path service
**Explicación:**

Se localiza un servicio cuya ruta al binario carece de comillas, permitiendo ejecutar un binario malicioso en un directorio intermedio; se anota la ruta completa del ejecutable.

Respuesta: `C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe`

### Task 5: Verificación de permisos / Permission verification
**Explicación:**

Se comprueban los permisos de escritura y acceso sobre los directorios y binarios de servicio. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 6: Preparación de la explotación / Exploitation prep
**Explicación:**

Se prepara el payload y el entorno para explotar los servicios vulnerables. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 7: Explotación del primer vector / First vector exploitation
**Explicación:**

Se ejecuta el ataque sobre el servicio con DACL débil para obtener código como SYSTEM. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 8: Explotación del segundo vector / Second vector exploitation
**Explicación:**

Se ejecuta el ataque sobre la ruta sin comillas para elevar privilegios. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 9: Credenciales en texto plano / Plaintext credentials
**Explicación:**

Se localizan credenciales almacenadas en texto plano dentro de la máquina victimizada.

Respuesta: `password123`

### Task 10: Verificación adicional / Additional check
**Explicación:**

Se comprueban otros vectores de credenciales o configuración. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 11: Hash encontrado / Hash found
**Explicación:**

Se extrae un hash de contraseña disponible en el sistema como parte de la escalada.

Respuesta: `a9fdfa038c4b75ebc76dc855dd74f0da`

### Task 12: Preparación de la escalada / Escalation prep
**Explicación:**

Preparación de los siguientes pasos de escalada. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 13: Escalada por hash / Hash-based escalation
**Explicación:**

Se utiliza el hash obtenido para autenticarse con privilegios mayores. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 14: Escalada por tareas / Task-based escalation
**Explicación:**

Se comprueba el abuso de tareas programadas o reinicios de servicio. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 15: Escalada por tokens / Token-based escalation
**Explicación:**

Se comprueba la presencia de tokens o privilegios de impersonación. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 16: Privilegios del token / Token privileges
**Explicación:**

Se enumeran los privilegios del token actual que podrían permitir impersonación y asignación de token primario.

1. `SeImpersonatePrivilege`
2. `SeAssignPrimaryTokenPrivilege`

### Task 17: Explotación del token / Token exploitation
**Explicación:**

Se explotan los privilegios de token para ejecutar código como SYSTEM. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 18: Cierre / Conclusion
**Explicación:**

Recapitulación final de la sala. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a la escalada de privilegios | `No answer needed` |
| 2 | Enumeración inicial del sistema | `No answer needed` |
| 3 | Ruta del binario del servicio con DACL débil | `C:\Program Files\DACL Service\daclservice.exe` |
| 4 | Ruta del ejecutable del servicio sin comillas | `C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe` |
| 5 | Verificación de permisos | `No answer needed` |
| 6 | Preparación de la explotación | `No answer needed` |
| 7 | Explotación del DACL débil | `No answer needed` |
| 8 | Explotación de la ruta sin comillas | `No answer needed` |
| 9 | Credencial en texto plano encontrada | `password123` |
| 10 | Verificación adicional de vectores | `No answer needed` |
| 11 | Hash de contraseña extraído | `a9fdfa038c4b75ebc76dc855dd74f0da` |
| 12 | Preparación de la escalada | `No answer needed` |
| 13 | Escalada mediante el hash | `No answer needed` |
| 14 | Escalada mediante tareas/servicios | `No answer needed` |
| 15 | Comprobación de tokens | `No answer needed` |
| 16.1 | Privilegio de impersonación | `SeImpersonatePrivilege` |
| 16.2 | Privilegio de asignación de token primario | `SeAssignPrimaryTokenPrivilege` |
| 17 | Explotación del token | `No answer needed` |
| 18 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Enumeración de servicios y permisos, abuso de servicios con DACL débiles y rutas sin comillas, recolección de credenciales en texto plano y hashes, y explotación de privilegios de token (SeImpersonate/SeAssignPrimaryToken) para escalar hasta SYSTEM en una máquina Windows de laboratorio.

### Cadena de ataque / Attack Chain

```text
Enumeración → servicio con DACL débil → ruta sin comillas → credenciales en texto plano → hash de contraseña → privilegios de token (SeImpersonate) → SYSTEM
```

**Learning chain:** Fundamentos de escalada en Windows → enumeración de servicios → DACL abuse → unquoted path → credenciales → hashes → token impersonation → SYSTEM.

**Lección:** *Los servicios mal configurados son el atajo más rentable hacia SYSTEM: una DACL débil o una ruta sin comillas pesan más que cientos de vulnerabilidades de software.*

**MITRE ATT&CK:** T1543.003 Create or Modify System Process: Windows Service · T1574.001 Hijack Execution Flow: DLL Search Order Hijacking · T1068 Exploitation for Privilege Escalation · T1134 Access Token Manipulation · T1003 OS Credential Dumping · T1078 Valid Accounts.

**Fuente:** [TryHackMe - Windows PrivEsc](https://tryhackme.com/room/windowsprivesc)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.