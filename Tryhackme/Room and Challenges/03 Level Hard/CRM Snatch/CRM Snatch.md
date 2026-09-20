# CRM Snatch

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Reto • Pentest completo | crmsnatch | https://tryhackme.com/room/crmsnatch | 03 Level Hard | TryHackMe | SSH, credenciales, Rclone, exfiltración de datos | Crítico |

---

**Contexto:**
> **ES:** Laboratorio de pentest contra un servicio CRM: acceso por SSH, enumeración de usuarios y puertos, y exfiltración de datos mediante Rclone para confirmar el robo de información.
> **EN:** Pentest lab against a CRM service: SSH access, user and port enumeration, and data exfiltration via Rclone to confirm information theft.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**
1. No answer needed

### Task 2: Enumeración y exfiltración / Enumeration and exfiltration
**Explicación:**
1. matthew.collins
2. 3455
3. 167.172.41.141
4. Rclone
5. yWKgVA7Rv1iIoG-VWAr7NAFbwKHNiMZGNybJ4QybJHtiFg
6. lucas.rivera@deceptitech.thm

### Preguntas y Respuestas / Questions and Answers

| Task | Respuesta / Answer |
|---|---|
| 1 | `No answer needed` |
| 2.1 | `matthew.collins` |
| 2.2 | `3455` |
| 2.3 | `167.172.41.141` |
| 2.4 | `Rclone` |
| 2.5 | `yWKgVA7Rv1iIoG-VWAr7NAFbwKHNiMZGNybJ4QybJHtiFg` |
| 2.6 | `lucas.rivera@deceptitech.thm` |

---

**Metodología:**
Acceso inicial al servicio CRM, enumeración de credenciales y servicios (SSH), identificación del mecanismo de sincronización (Rclone), recuperación del token y confirmación de la cuenta de exfiltración.

### Cadena de ataque / Attack Chain
1. Reconocimiento del servicio CRM y del servicio SSH.
2. Ordenación de credenciales y usuario válido (matthew.collins).
3. Conexión por el puerto identificado (3455).
4. Descubrimiento de Rclone como herramienta de sincronización.
5. Extracción del token de configuración.
6. Identificación de la cuenta remota de exfiltración.

**Learning chain:**
Reconocimiento -> Credenciales -> SSH -> Rclone -> Token -> Exfiltración.

**Lección:** *Los accesos mal configurados y las herramientas de sincronización legítimas son el canal perfecto para mover datos fuera del perímetro.*

**MITRE ATT&CK:**
- T1078 Valid Accounts
- T1567.001 Exfiltration Over Web Service
- T1003.001 OS Credential Dumping (LSASS)
- T1046 Network Service Discovery

**Fuente:** [TryHackMe - CRM Snatch](https://tryhackme.com/room/crmsnatch)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.