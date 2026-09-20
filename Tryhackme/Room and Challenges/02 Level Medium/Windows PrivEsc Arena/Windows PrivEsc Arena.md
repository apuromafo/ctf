# Windows PrivEsc Arena

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | CTF / Explotación | windowsprivescarena | https://tryhackme.com/room/windowsprivescarena | 02 Level Medium | TryHackMe | Windows, escalada de privilegios, servicios, credenciales, arena de práctica | Escalada de privilegios local hasta SYSTEM/administrador en un laboratorio tipo arena |

---

**Contexto:** **Windows PrivEsc Arena** es un laboratorio de práctica de escalada de privilegios en Windows con varios escenarios encadenados. El alumno recorre distintas técnicas de enumeración y explotación sobre la máquina arena, respondiendo los datos obtenidos en cada paso: quién organizó el entorno, credenciales encontradas y confirmaciones de cada técnica aplicada.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**

Presentación de la arena de escalada de privilegios. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 2: Identificación del laboratorio / Lab identification
**Explicación:**

Se identifica el origen u organización del laboratorio de práctica.

1. `No answer needed`
2. `TCM`

### Task 3: Enumeración del sistema / System enumeration
**Explicación:**

Primera fase de enumeración para identificar vectores de escalada. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 4: Enumeración de servicios y avisos / Services and warnings
**Explicación:**

Se revisan servicios y configuraciones advertidas como vectores. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 5: Servicios con configuración insegura / Insecure service config
**Explicación:**

Se comprueban servicios con rutas o permisos mal configurados. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 6: Verificación de binarios de servicio / Service binary check
**Explicación:**

Se examinan los binarios de servicio y sus permisos. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 7: Explotación del servicio / Service exploitation
**Explicación:**

Se abusa del servicio vulnerable para obtener código con privilegios elevados. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 8: Exploración de credenciales / Credential hunting
**Explicación:**

Se buscan credenciales almacenadas en el sistema. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 9: Confirmación de acceso / Access confirmation
**Explicación:**

Se confirma el nivel de acceso alcanzado. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 10: Segundo vector de escalada / Second escalation vector
**Explicación:**

Se identifica y prepara el segundo vector de escalada de privilegios. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 11: Explotación del segundo vector / Second vector exploitation
**Explicación:**

Se ejecuta el ataque del segundo vector. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 12: Credencial en texto plano / Plaintext credential
**Explicación:**

Se recupera una credencial almacenada en texto plano durante la escalada.

Respuesta: `password123`

### Task 13: Escalada final / Final escalation
**Explicación:**

Se completa la escalada hasta el máximo nivel de privilegios. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Task 14: Cierre / Conclusion
**Explicación:**

Recapitulación de la arena. No requiere una respuesta concreta.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción a la arena | `No answer needed` |
| 2.1 | Pregunta previa de identificación | `No answer needed` |
| 2.2 | Organización creadora del laboratorio | `TCM` |
| 3 | Enumeración del sistema | `No answer needed` |
| 4 | Revisión de servicios y avisos | `No answer needed` |
| 5 | Servicios con configuración insegura | `No answer needed` |
| 6 | Verificación de binarios de servicio | `No answer needed` |
| 7 | Explotación del servicio | `No answer needed` |
| 8 | Búsqueda de credenciales | `No answer needed` |
| 9 | Confirmación de acceso | `No answer needed` |
| 10 | Segundo vector de escalada | `No answer needed` |
| 11 | Explotación del segundo vector | `No answer needed` |
| 12 | Credencial en texto plano | `password123` |
| 13 | Escalada final | `No answer needed` |
| 14 | Cierre de la arena | `No answer needed` |

---

**Metodología:** Recorrido práctico por varias técnicas de escalada en Windows dentro de una arena de laboratorio: enumeración de servicios y permisos, abuso de configuraciones inseguras, búsqueda de credenciales y uso de vectores encadenados para elevar privilegios hasta el máximo nivel.

**Learning chain:** Reconocimiento del laboratorio → enumeración → abuso de servicios → credenciales → segundo vector → escalada final → SYSTEM.

**Lección:** *Una arena de práctica demuestra que la escalada en Windows rara vez depende de un único fallo: la combinación de servicios, credenciales y configuración es lo que define los caminos reales.*

**MITRE ATT&CK:** T1543.003 Create or Modify System Process: Windows Service · T1574.001 DLL Search Order Hijacking · T1068 Exploitation for Privilege Escalation · T1003 OS Credential Dumping · T1078 Valid Accounts.

**Fuente:** [TryHackMe - Windows PrivEsc Arena](https://tryhackme.com/room/windowsprivescarena)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.