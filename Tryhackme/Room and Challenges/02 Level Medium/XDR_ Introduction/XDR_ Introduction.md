# XDR_ Introduction

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough | xdrintroduction | https://tryhackme.com/room/xdrintroduction | 02 Level Medium | TryHackMe | Microsoft 365 Defender, XDR, KQL | Introducción al concepto de XDR y al ecosistema de Microsoft 365 Defender: detección, investigación y respuesta |

---

**Contexto:** La sala **XDR: Introduction** explica el concepto de XDR (Extended Detection and Response) y su implementación en Microsoft 365 Defender. El alumno identifica los componentes del ecosistema: Defender para Endpoints, Defender for Office 365, Defender for Identity y Defender for Cloud Apps, así como el lenguaje de consulta Kusto (KQL). También se cubren los permisos, la configuración de las cargas de trabajo, la gestión de alertas e incidentes y la navegación por el portal de Microsoft 365 Defender.

## Solucionario

### Task 1: Introducción

**Explicación:**

La sala presenta los fundamentos del XDR y de la plataforma Microsoft 365 Defender.

Respuesta: `No answer needed`

### Task 2: Definición semántica

**Explicación:**

Se responde sobre el ámbito de la detección en el ecosistema XDR: los dispositivos finales (Endpoints) que se monitorizan y la confirmación de la definición ampliada.

1. `Endpoints`
2. `Yea`

### Task 3: Microsoft Defender for Office 365

**Explicación:**

Se identifica el componente responsable de la protección del correo y las aplicaciones de Office: Microsoft Defender for Office 365, y el lenguaje de consulta utilizado para la búsqueda avanzada de amenazas (Kusto Query Language).

1. `Microsoft Defender for Office 365`
2. `Kusto Query Language`

### Task 4: Defender for Identity

**Explicación:**

Se identifica el módulo dedicado a la protección de las identidades: Defender for Identity, junto con la capacidad de respuesta automática basada en la identidad.

1. `Defender for Identity`
2. `Identity automated response`

### Task 5: Permisos y roles

**Explicación:**

Se responde sobre los requisitos de acceso necesarios para operar dentro de la consola de administración del ecosistema XDR.

- `Permissions`

### Task 6: Configuración de cargas de trabajo

**Explicación:**

Se resuelven las preguntas de configuración: el número de cargas de trabajo a considerar y el apartado del portal donde se configuran los ajustes de estas cargas.

1. `2`
2. `Workload settings`

### Task 7: Investigación de incidentes

**Explicación:**

La tarea implica el reconocimiento del flujo de investigación de amenazas dentro de la plataforma.

Respuesta: `No answer needed`

### Task 8: Alertas y respuesta

**Explicación:**

Se indican los elementos de la gestión de la respuesta: la vista donde se muestran las alertas y la opción del menú que permite gestionar un incidente.

1. `alerts`
2. `Manage incident`

### Task 9: Portal de Microsoft 365 Defender

**Explicación:**

Se responde sobre la navegación del portal: el número de opciones de acceso y el apartado de autorización y configuración.

1. `3`
2. `Authorization and settings`

### Task 10: Conclusión

**Explicación:**

La sala concluye la introducción al XDR con el repaso de los componentes de Microsoft 365 Defender.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lectura de la introducción | `No answer needed` |
| 2.1 | Ámbito de la detección | `Endpoints` |
| 2.2 | Confirmación de la definición | `Yea` |
| 3.1 | Componente de Office 365 | `Microsoft Defender for Office 365` |
| 3.2 | Lenguaje de búsqueda avanzada | `Kusto Query Language` |
| 4.1 | Componente de identidades | `Defender for Identity` |
| 4.2 | Respuesta automatizada de identidad | `Identity automated response` |
| 5 | Requisito de acceso | `Permissions` |
| 6.1 | Número de cargas de trabajo | `2` |
| 6.2 | Apartado de configuración | `Workload settings` |
| 7 | Investigación de incidentes | `No answer needed` |
| 8.1 | Vista de alertas | `alerts` |
| 8.2 | Gestión de incidentes | `Manage incident` |
| 9.1 | Opciones de acceso al portal | `3` |
| 9.2 | Autorización y configuración | `Authorization and settings` |
| 10 | Conclusión | `No answer needed` |

---

**Metodología:** Reconocimiento del ecosistema XDR de Microsoft 365 Defender: identificación de componentes, permisos, configuración de cargas de trabajo y flujo de gestión de alertas e incidentes en el portal.

**Learning chain:** XDR → Endpoints → Office 365 → Identity → Permisos → Workloads → Incidentes → Portal → conclusión.

**Lección:** *El valor del XDR está en correlacionar dominios: correo, endpoint, identidad y aplicaciones convergen en una sola plataforma de detección y respuesta.*

**MITRE ATT&CK:** T1078 Valid Accounts · T1059 Command and Scripting Interpreter · T1562 Impair Defenses.

**Fuente:** [TryHackMe - XDR_ Introduction](https://tryhackme.com/room/xdrintroduction)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.