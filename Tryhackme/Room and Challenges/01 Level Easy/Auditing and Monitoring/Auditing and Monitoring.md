# Auditing and Monitoring

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `auditingandmonitoring` |
| **Link** | [TryHackMe](https://tryhackme.com/room/auditingandmonitoring) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | Windows Auditing, Event Log, Monitorización, auditorías, Event ID 4625 |
| **Impacto** | Comprensión y configuración de la auditoría y monitorización Windows para detectar accesos y comportamientos anómalos en el sistema. |

---

**Contexto:** La sala explica los fundamentos de la **auditoría y monitorización** en entornos Windows: la diferencia entre auditar y monitorizar, los tipos de auditoría (externa e interna), los estándares y marcos de referencia (PCI DSS, CCTA, ISACA), y la configuración práctica de las políticas de auditoría. Sobre el laboratorio se practica el filtrado del registro de eventos, analizando logs concretos como el **Event ID 4625** (inicios de sesión fallidos) y contabilizando eventos para la detección de actividad maliciosa.

## Solucionario

### Task 1: Conceptos básicos / The Basics

**Explicación:** Se introduce la diferencia entre los dos procesos fundamentales: **Auditing** es el proceso de recopilar y registrar la actividad del sistema, mientras que **Monitoring** es el proceso de analizar y revisar esa información registrada para detectar comportamiento anómalo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué proceso se encarga de registrar la actividad del sistema? | `Auditing` |
| 2 | ¿Qué proceso analiza y revisa la actividad registrada? | `Monitoring` |

### Task 2: Tipos de auditoría / Types of Audits

**Explicación:** Se distinguen los tipos de auditoría según quién la realiza: la **External Audit** la ejecutan terceros ajenos a la organización, mientras que la **Internal Audit** la llevan a cabo miembros de la propia empresa.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de auditoría realiza un tercero externo a la organización? | `External Audit` |
| 2 | ¿Qué tipo de auditoría realiza la propia organización? | `Internal Audit` |

### Task 3: Estándares y marcos / Standards & Frameworks

**Explicación:** Se repasan los estándares y marcos de auditoría relevantes en ciberseguridad: **PCI DSS** (pagos), **CCTA** y los marcos/gobernanza de la organización **ISACA**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué estándar se aplica a la seguridad en el sector de pagos con tarjeta? | `PCI DSS` |
| 2 | ¿Qué marco/estándar se referencia en este contexto? | `CCTA` |
| 3 | ¿Qué organización marca las prácticas de auditoría y gobernanza? | `ISACA` |

### Task 4: Configuración de políticas / Policy Configuration

**Explicación:** Se configuran los niveles de las políticas de auditoría del sistema. Las respuestas corresponden a los valores numéricos que deben establecerse para cada configuración solicitada en el laboratorio.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Valor de configuración de la política de auditoría (paso 1). | `4` |
| 2 | Valor de configuración de la política de auditoría (paso 2). | `5` |
| 3 | Valor de configuración de la política de auditoría (paso 3). | `1` |

### Task 5: Habilitando la auditoría / Enabling Auditing

**Explicación:** Se llevan a cabo los pasos prácticos para habilitar la auditoría sobre los eventos deseados en el sistema Windows del laboratorio. Tarea práctica sin respuesta numérica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Completar los pasos para habilitar la auditoría. | `No answer needed` |

### Task 6: Registro de eventos / Event Log

**Explicación:** Se abre el visor de eventos y se aplican los filtros sobre el registro para contabilizar los eventos solicitados. Los valores encontrados en el laboratorio son los que se indican a continuación.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el valor contabilizado en el registro (paso 1)? | `263` |
| 2 | ¿Cuál es el valor contabilizado en el registro (paso 2)? | `4` |
| 3 | ¿Cuál es el valor contabilizado en el registro (paso 3)? | `227` |

### Task 7: Evento 4625 / Event 4625

**Explicación:** Se analizan los eventos de tipo **4625**, que corresponden a inicios de sesión con errores (failed logons). Tras aplicar los filtros sobre el registro, se indican los recuentos de eventos encontrados.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué ID de evento registra los inicios de sesión fallidos? | `4625` |
| 2 | ¿Cuántos eventos se contabilizan al aplicar el primer recuento? | `2` |
| 3 | ¿Cuántos eventos se contabilizan al aplicar el segundo recuento? | `1` |

### Task 8: Monitorización / Monitoring

**Explicación:** Se introducen las técnicas de monitorización continua del sistema, enfocadas a detectar comportamientos anómalos a partir de la información registrada por la auditoría. Tarea informativa sin respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer los contenidos sobre monitorización. | `No answer needed` |

### Task 9: Reto práctico / Practical Challenge

**Explicación:** Resolución de un reto práctico combinando auditoría y monitorización sobre el sistema del laboratorio. Se lleva a cabo la verificación correspondiente sin respuesta numérica.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Resolver el reto práctico de auditoría y monitorización. | `No answer needed` |

### Task 10: Conclusión / Conclusion

**Explicación:** Recapitulación final de la sala: la importancia de auditar antes de poder monitorizar y de enfocar la monitorización a la detección de anomalías. No hay respuesta que enviar.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué proceso se encarga de registrar la actividad del sistema? | `Auditing` |
| 2 | ¿Qué proceso analiza y revisa la actividad registrada? | `Monitoring` |
| 3 | ¿Qué tipo de auditoría realiza un tercero externo a la organización? | `External Audit` |
| 4 | ¿Qué tipo de auditoría realiza la propia organización? | `Internal Audit` |
| 5 | ¿Qué estándar se aplica a la seguridad en el sector de pagos con tarjeta? | `PCI DSS` |
| 6 | ¿Qué marco/estándar se referencia en este contexto? | `CCTA` |
| 7 | ¿Qué organización marca las prácticas de auditoría y gobernanza? | `ISACA` |
| 8 | Valor de configuración de la política de auditoría (paso 1). | `4` |
| 9 | Valor de configuración de la política de auditoría (paso 2). | `5` |
| 10 | Valor de configuración de la política de auditoría (paso 3). | `1` |
| 11 | Completar los pasos para habilitar la auditoría. | `No answer needed` |
| 12 | ¿Cuál es el valor contabilizado en el registro (paso 1)? | `263` |
| 13 | ¿Cuál es el valor contabilizado en el registro (paso 2)? | `4` |
| 14 | ¿Cuál es el valor contabilizado en el registro (paso 3)? | `227` |
| 15 | ¿Qué ID de evento registra los inicios de sesión fallidos? | `4625` |
| 16 | ¿Cuántos eventos se contabilizan al aplicar el primer recuento? | `2` |
| 17 | ¿Cuántos eventos se contabilizan al aplicar el segundo recuento? | `1` |
| 18 | Leer los contenidos sobre monitorización. | `No answer needed` |
| 19 | Resolver el reto práctico de auditoría y monitorización. | `No answer needed` |
| 20 | Leer la conclusión de la sala. | `No answer needed` |

---

**Metodología:**

1. Se interiorizan los conceptos de **Auditing** (registro de actividad) y **Monitoring** (análisis de la actividad registrada).
2. Se distinguen los tipos de auditoría: **External Audit** e **Internal Audit**.
3. Se repasan los marcos/estándares: **PCI DSS**, **CCTA** e **ISACA**.
4. Se configuran las políticas de auditoría del sistema con los valores solicitados.
5. Se habilita la auditoría y se abre el visor de eventos, aplicando filtros sobre el registro.
6. Se contabilizan los eventos solicitados, incluyendo el análisis de los eventos **4625** (logons fallidos).

### Cadena de ataque / Attack Chain

```
Conceptos (Auditing vs Monitoring)
  -> Tipos de auditoría (External/Internal)
  -> Estándares (PCI DSS, CCTA, ISACA)
  -> Configuración de políticas de auditoría
  -> Habilitar auditoría + visor de eventos
  -> Filtrado y recuento de eventos (263, 4, 227)
  -> Análisis Event ID 4625 (2, 1)
```

**Learning chain:** Fundamentos auditoría/monitorización → Tipos de auditoría → Estándares → Configuración de políticas → Habilitación → Visor de eventos → Recuentos → Evento 4625

**Lección:** *No se puede monitorizar lo que no se audita: la configuración correcta de las políticas de auditoría y el análisis de eventos específicos (como el 4625 de logons fallidos) son la base de toda estrategia de detección.*

**MITRE ATT&CK:** T1110 (Brute Force), T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter)

**Fuente:** [TryHackMe - Auditing and Monitoring](https://tryhackme.com/room/auditingandmonitoring)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.