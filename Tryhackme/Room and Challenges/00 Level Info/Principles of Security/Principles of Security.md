# Principles of Security

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Info | Walkthrough | `principlesofsecurity` | https://tryhackme.com/room/principlesofsecurity | 00 Level Info | TryHackMe | tríada CIA / PIM / PAM / Bell-LaPadula / Biba / STRIDE / IR | Principios de seguridad de la información: tríada CIA, gestión de accesos privilegiados y modelos de referencia |

---

**Contexto:** La sala presenta los principios fundamentales de la seguridad de la información: la tríada de la confidencialidad, integridad y disponibilidad (CIA), los conceptos de gestión de identidades y accesos privilegiados (PIM/PAM), los modelos de control de acceso Bell-LaPadula y Biba, y termina con el modelado de amenazas y la respuesta a incidentes.

> **ES:** Se estudian los tres pilares de la seguridad (CIA), PIM/PAM, los modelos Bell-LaPadula y Biba, y se cierra con STRIDE y respuesta a incidentes.
> **EN:** Study the three pillars of security (CIA), PIM/PAM, the Bell-LaPadula and Biba models, and finish with STRIDE and incident response.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** La tarea presenta la sala y el propósito de los principios de seguridad. No hay nada que responder, solo leer el contenido introductorio.

```text
1. No answer needed
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información de la tarea. / Read the task information. | No answer needed |

### Task 2: La tríada de la seguridad / The security triad

**Explicación:** Se repasan los tres pilares de la seguridad: la integridad (que los datos no se alteren), la disponibilidad (que estén accesibles cuando se necesitan) y la confidencialidad (que solo accedan quienes tengan permiso).

```text
2. 1. integrity
   2. availability
   3. confidentiality
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué pilar protege que los datos no se modifiquen? / Which pillar protects against data modification? | `integrity` |
| 2 | ¿Qué pilar mantiene los datos accesibles? / Which pillar keeps data available? | `availability` |
| 3 | ¿Qué pilar restringe quién ve los datos? / Which pillar restricts who can see data? | `confidentiality` |

### Task 3: PIM y PAM / Privileged Identity and Access Management

**Explicación:** Se estudia la gestión de usuarios y accesos privilegiados: la gestión de identidades privilegiadas (PIM, Privileged Identity Management) y la gestión de accesos privilegiados (PAM, Privileged Access Management). El acrónimo identifica el mecanismo completo y el otro la gestión de la propia identidad.

```text
3. 1. Privileged Identity Management
   2. Privileged Access Management
   3. PAM
   4. PIM
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué gestiona la identidad del usuario privilegiado? / What manages the privileged identity? | `Privileged Identity Management` |
| 2 | ¿Qué gestiona el acceso y los permisos privilegiados? / What manages privileged access and permissions? | `Privileged Access Management` |
| 3 | ¿Qué acrónimo define el mecanismo completo de gestión de acceso? / Which acronym defines the full access management mechanism? | `PAM` |
| 4 | ¿Qué acrónimo define la gestión de identidades privilegiadas? / Which acronym defines privileged identity management? | `PIM` |

### Task 4: Modelos de control de acceso / Access control models

**Explicación:** Se comparan los dos modelos de referencia dados en la sala: el modelo Bell-LaPadula (orientado a la confidencialidad, "no read up / no write down") y el modelo Biba (orientado a la integridad). Dos respuestas corresponden a Bell-LaPadula y dos a Biba según la propiedad del modelo.

```text
4. 1. The Bell-LaPadula Model
   2. The Biba Model
   3. The Bell-LaPadula Model
   4. The Biba Model
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué modelo protege la confidencialidad? / Which model protects confidentiality? | `The Bell-LaPadula Model` |
| 2 | ¿Qué modelo protege la integridad? / Which model protects integrity? | `The Biba Model` |
| 3 | ¿Qué modelo impide leer por encima del nivel? / Which model prevents reading above your level? | `The Bell-LaPadula Model` |
| 4 | ¿Qué modelo impide escribir por debajo del nivel? / Which model prevents writing below your level? | `The Biba Model` |

### Task 5: Modelado de amenazas y respuesta / Threat modelling and response

**Explicación:** La tarea introduce el modelado de amenazas (con el acrónimo STRIDE) y el ciclo de respuesta a incidentes (Incident Response). Se identifican categorías del modelado como Tampering (manipulación) y fases de respuesta como Recovery (recuperación).

```text
5. 1. STRIDE
   2. Incident Response
   3. Tampering
   4. Recovery
```

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué framework de modelado de amenazas se usa? / What threat modelling framework is used? | `STRIDE` |
| 2 | ¿Cómo se llama la disciplina de gestión de incidentes? / What is the discipline that manages incidents? | `Incident Response` |
| 3 | ¿Qué categoría de amenaza implica modificar datos? / Which threat category involves tampering with data? | `Tampering` |
| 4 | ¿Qué fase restaura el estado seguro después de un incidente? / Which phase restores a safe state after an incident? | `Recovery` |

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Leer la información de la tarea. / Read the task information. | No answer needed |
| 2 | ¿Qué pilar protege que los datos no se modifiquen? / Which pillar protects against data modification? | `integrity` |
| 3 | ¿Qué pilar mantiene los datos accesibles? / Which pillar keeps data available? | `availability` |
| 4 | ¿Qué pilar restringe quién ve los datos? / Which pillar restricts who can see data? | `confidentiality` |
| 5 | ¿Qué gestiona la identidad del usuario privilegiado? / What manages the privileged identity? | `Privileged Identity Management` |
| 6 | ¿Qué gestiona el acceso y los permisos privilegiados? / What manages privileged access and permissions? | `Privileged Access Management` |
| 7 | ¿Qué acrónimo define el mecanismo completo de gestión de acceso? / Which acronym defines the full access management mechanism? | `PAM` |
| 8 | ¿Qué acrónimo define la gestión de identidades privilegiadas? / Which acronym defines privileged identity management? | `PIM` |
| 9 | ¿Qué modelo protege la confidencialidad? / Which model protects confidentiality? | `The Bell-LaPadula Model` |
| 10 | ¿Qué modelo protege la integridad? / Which model protects integrity? | `The Biba Model` |
| 11 | ¿Qué modelo impide leer por encima del nivel? / Which model prevents reading above your level? | `The Bell-LaPadula Model` |
| 12 | ¿Qué modelo impide escribir por debajo del nivel? / Which model prevents writing below your level? | `The Biba Model` |
| 13 | ¿Qué framework de modelado de amenazas se usa? / What threat modelling framework is used? | `STRIDE` |
| 14 | ¿Cómo se llama la disciplina de gestión de incidentes? / What is the discipline that manages incidents? | `Incident Response` |
| 15 | ¿Qué categoría de amenaza implica modificar datos? / Which threat category involves tampering with data? | `Tampering` |
| 16 | ¿Qué fase restaura el estado seguro después de un incidente? / Which phase restores a safe state after an incident? | `Recovery` |

---

**Metodología:** Revisar la tríada CIA (integridad, disponibilidad, confidencialidad), comprender la gestión de identidades y accesos privilegiados (PIM/PAM), comparar los modelos Bell-LaPadula y Biba según confidencialidad/integridad y, por último, aplicar el modelado de amenazas STRIDE con las fases de respuesta a incidentes.

### Cadena de ataque / Attack Chain

```text
Tríada CIA -> integridad / disponibilidad / confidencialidad -> PIM / PAM -> Bell-LaPadula (confidencialidad) -> Biba (integridad) -> STRIDE -> Incident Response (Tampering / Recovery)
```

**Learning chain:** Seguridad de la información -> CIA -> PIM/PAM -> modelos de acceso (Bell-LaPadula, Biba) -> modelado de amenazas (STRIDE) -> respuesta a incidentes

**Lección:** *Todos los controles de seguridad de una organización derivan de tres principios (confidencialidad, integridad y disponibilidad) y de modelos de acceso bien definidos; conocerlos permite elegir la defensa correcta para cada amenaza.*

**MITRE ATT&CK:** N/A (sala educativa de principios y modelos de seguridad)

**Fuente:** [TryHackMe - Principles of Security](https://tryhackme.com/room/principlesofsecurity)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.