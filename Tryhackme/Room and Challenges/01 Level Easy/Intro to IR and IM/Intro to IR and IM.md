# Intro to IR and IM

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introtoirandim` | [TryHackMe](https://tryhackme.com/room/introtoirandim) | 01 Level Easy | TryHackMe | Incident Response, Incident Management, Roles, NIST | Fundamentos de respuesta y gestión de incidentes: niveles, roles, proceso NIST y errores comunes |

> **Objeto:** Aprender los fundamentos de Incident Response (IR) e Incident Management (IM): sus diferencias, los niveles de incidente, los roles implicados, el proceso de gestión basado en NIST y los errores comunes a evitar.

---

**Contexto:** Sala introductoria del path Security Engineer que explica la diferencia entre Incident Response (IR), que trata de responder a "¿qué ha pasado?", e Incident Management (IM), que trata de responder a "¿cómo respondemos?". Se cubren los niveles de incidente, los diferentes roles durante un incidente (SOC Analyst, SOC Lead, Forensic Analyst, Threat Hunter, Security Engineer, Incident Manager, etc.), el proceso de gestión de incidentes basado en NIST (Preparation, Detection and Analysis, Containment/Eradication/Recovery) y los errores comunes de la gestión de incidentes.

> **ES:** Sala introductoria a la respuesta a incidentes (IR) y la gestión de incidentes (IM): niveles de incidente, roles, proceso NIST y errores comunes, con flags prácticas en cada bloque.
> **EN:** Introductory room to Incident Response (IR) and Incident Management (IM): incident levels, roles, NIST process and common mistakes, with practical flags in each block.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de los objetivos: entender la diferencia entre respuesta y gestión de incidentes, los roles implicados, el proceso de gestión y los errores comunes.

No answer needed

### Task 2: Qué es la Respuesta y la Gestión de Incidentes / What is Incident Response and Management
**Explicación:** Se distinguen los niveles de incidente y los componentes IR e IM según la pregunta que responden: IR investiga "¿qué ha pasado?" e IM gestiona "¿cómo respondemos a lo ocurrido?".

1. 3
2. 4
3. IM
4. IR

### Task 3: Los diferentes roles durante un incidente / The Different Roles During an Incident
**Explicación:** Se aprenden los roles que intervienen durante un incidente (SOC Analyst, SOC Lead, Forensic Analyst, Malware Analyst, Threat Hunter, Incident Manager, entre otros) y se obtiene una flag al emparejar roles con responsabilidades.

THM{Roles.and.Responsibilities.of.IR.and.IM}

### Task 4: El proceso de gestión de incidentes / The Process of Incident Management
**Explicación:** Se recorre el proceso de gestión de incidentes basado en NIST (Preparation, Detection and Analysis, Containment, Eradication and Recovery) y se obtiene una flag al ordenar correctamente los pasos.

THM{Preparation.is.Key.for.Incident.Management}

### Task 5: Errores comunes durante un incidente / Common Pitfalls During an Incident
**Explicación:** Se identifican los errores comunes de la gestión de incidentes y se obtiene la flag al superarlos.

THM{Avoiding.the.Common.IM.Mistakes}

### Task 6: Conclusión / Conclusion
**Explicación:** Cierre de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | Presentación de la sala | `No answer needed` |
| 2.1 | ¿A qué nivel (solo número) se coloca al SOC en alerta alta para gestionar un incidente? | `3` |
| 2.2 | ¿A qué nivel (solo número) se clasifica un incidente como ciber crisis? | `4` |
| 2.3 | ¿Qué componente (IR o IM) responde a la pregunta "¿cómo respondemos a lo ocurrido?"? | `IM` |
| 2.4 | ¿Qué componente (IR o IM) responde a la pregunta "¿qué ha pasado?"? | `IR` |
| 3.1 | Flag al emparejar los roles y responsabilidades | `THM{Roles.and.Responsibilities.of.IR.and.IM}` |
| 4.1 | Flag al ordenar correctamente los pasos del proceso de gestión de incidentes | `THM{Preparation.is.Key.for.Incident.Management}` |
| 5.1 | Flag al superar los errores comunes de un incidente | `THM{Avoiding.the.Common.IM.Mistakes}` |
| 6 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Revisión de los niveles de incidente y su severidad, identificación de qué componente (IR o IM) responde a cada pregunta, emparejamiento de roles con sus responsabilidades, ordenación de las fases del proceso NIST de gestión de incidentes y análisis de los errores comunes de IM para obtener las flags de cada bloque.

### Cadena de ataque / Attack Chain

Incidente -> nivel de severidad -> IR (¿qué ha pasado?) vs IM (¿cómo respondemos?) -> roles y responsabilidades -> proceso NIST -> preparación -> evitar errores comunes -> flags

**Learning chain:** incident -> severity levels -> incident response -> incident management -> roles -> NIST process -> preparation -> common pitfalls

**Lección:** *La preparación y la correcta asignación de roles y de proceso (IR vs IM) determinan si un incidente se convierte en un caos o en una respuesta controlada.*

**MITRE ATT&CK:** N/A (sala defensiva).

**Fuente:** [TryHackMe - Intro to IR and IM](https://tryhackme.com/room/introtoirandim)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.