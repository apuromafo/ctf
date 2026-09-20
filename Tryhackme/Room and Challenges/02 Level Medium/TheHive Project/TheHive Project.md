# TheHive Project
| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / DFIR | thehiveproject | https://tryhackme.com/room/thehiveproject | 02 Level Medium | TryHackMe | TheHive, Cortex, gestión de casos y observables, perfiles y permisos, navegación de analista, MITRE ATT&CK | Uso de TheHive como plataforma de respuesta a incidentes de seguridad (SIRP) para documentar los hallazgos de una investigación |

> **Objeto:** Aprender a usar TheHive, una plataforma de respuesta a incidentes de seguridad (SIRP), para reportar los hallazgos de una investigación.

---
**Contexto:** **TheHive Project** es una sala guiada (walkthrough) de dificultad Media centrada en **TheHive**, una plataforma de respuesta a incidentes de seguridad (SIRP). A lo largo de la sala se revisan las funciones e integraciones de TheHive (como **Cortex**), los perfiles de usuario y sus permisos, y la navegación de la interfaz del analista. El hilo conductor es aprender a documentar de forma estructurada los hallazgos de una investigación: casos, observables, tareas y su vínculo con MITRE ATT&CK.
> **ES:** Aprende a usar TheHive, una plataforma de respuesta a incidentes de seguridad, para reportar los hallazgos de una investigación.
> **EN:** Learn how to use TheHive, a Security Incident Response Platform, to report investigation findings.

## Solucionario
### Task 1: Esquema de la sala / Room Outline
**Explicación:** Presentación del contenido y la estructura de la sala.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 1 | `No answer needed` |

### Task 2: Introducción / Introduction
**Explicación:** Introducción a TheHive como plataforma de respuesta a incidentes y a su papel dentro de un flujo DFIR.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 2 | `No answer needed` |

### Task 3: Funciones e integraciones de TheHive / TheHive Features & Integrations
**Explicación:** Repaso de las funciones de TheHive y de sus integraciones. La integración con **Cortex** permite el análisis y enriquecimiento automático de observables (analyzers y responders).

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 3 | `Cortex` |

### Task 4: Perfiles de usuario y permisos / User Profiles & Permissions
**Explicación:** Se estudian los perfiles de usuario de TheHive y los permisos asociados. Se identifica el perfil administrador, el permiso para gestionar observables y el permiso para gestionar acciones.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 4 (1) | `Admin` |
| Task 4 (2) | `manageObservable` |
| Task 4 (3) | `manageAction` |

### Task 5: Navegación de la interfaz del analista / Analyst Interface Navigation
**Explicación:** Se recorre la interfaz del analista: taxonomías y marcos de referencia (MITRE ATT&CK), tipos de observable (tráfico de red) y la resolución del reto práctico de la sala.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 5 (1) | `MITRE ATT&CK` |
| Task 5 (2) | `Network Traffic` |
| Task 5 (3) | `THM{FILES_ARE_OBSERVABLES}` |

### Task 6: Conclusión de la sala / Room Conclusion
**Explicación:** Cierre y resumen de lo aprendido sobre TheHive.

| Pregunta / Question | Respuesta / Answer |
|---------------------|--------------------|
| Task 6 | `No answer needed` |

### Tabla de preguntas y respuestas
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1 | `No answer needed` |
| 2 | Task 2 | `No answer needed` |
| 3 | Task 3 | `Cortex` |
| 4.1 | Task 4 (1) | `Admin` |
| 4.2 | Task 4 (2) | `manageObservable` |
| 4.3 | Task 4 (3) | `manageAction` |
| 5.1 | Task 5 (1) | `MITRE ATT&CK` |
| 5.2 | Task 5 (2) | `Network Traffic` |
| 5.3 | Task 5 (3) | `THM{FILES_ARE_OBSERVABLES}` |
| 6 | Task 6 | `No answer needed` |

---
**Metodología:** Recorrido guiado por TheHive: visión general → funciones e integraciones (Cortex) → perfiles y permisos → navegación de la interfaz de analista (taxonomías, observables, MITRE ATT&CK) → conclusión.

### Cadena de ataque / Attack Chain
```
Room outline -> Introduction a TheHive -> Features & Integrations (Cortex)
-> User Profiles & Permissions (Admin / manageObservable / manageAction)
-> Analyst Interface Navigation (MITRE ATT&CK, Network Traffic, observables)
-> THM{FILES_ARE_OBSERVABLES} -> Conclusion
```
**Learning chain:** Plataforma SIRP → integraciones → permisos → interfaz de analista → observables y su clasificación → hallazgos documentados.
**Lección:** *Centralizar casos, observables y tareas en una plataforma SIRP como TheHive, con perfiles y permisos bien definidos e integraciones como Cortex, ordena y acelera la respuesta a incidentes.*
**MITRE ATT&CK:** Uso de MITRE ATT&CK dentro de TheHive para clasificar observables y vincularlos a las técnicas del adversario.
**Fuente:** [TryHackMe - TheHive Project](https://tryhackme.com/room/thehiveproject)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
