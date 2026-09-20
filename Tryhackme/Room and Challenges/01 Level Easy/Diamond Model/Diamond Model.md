# Diamond Model

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `diamondmodel` | https://tryhackme.com/room/diamondmodel | 01 Level Easy | TryHackMe | Diamond Model / Adversary Operator / Victim Personae / Infrastructure / Arsenal | Aprendizaje del modelo atómico de ciberseguridad del Diamond Model y sus componentes aplicados a un incidente. |

---

**Contexto:** El Diamond Model es un marco analítico para describir una intrusión cibernética a través de cuatro elementos interconectados: el adversario (Adversary Operator y Adversary Customer), la víctima (Victim Personae), la capacidad (Adversary Arsenal) y la infraestructura (Type 2 y Type 1 Infrastructure). Cada actividad se caracteriza por fase (Phase), resultado (Result) y recursos (Resources), y el room culmina con un laboratorio de cadena de ataque con flag.

> **ES:** Marco del Diamond Model aplicado a un incidente: adversario, víctima, arsenal, infraestructura y características de cada actividad, más un laboratorio de cadena de ataque.
> **EN:** Diamond Model framework applied to an incident: adversary, victim, arsenal, infrastructure and activity features, plus an attack-chain lab.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación del modelo del Diamante como marco para analizar incidentes de ciberseguridad. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |

### Task 2: El adversario / The Adversary

**Explicación:** El adversario se descompone en dos roles: el `Adversary Operator` (la persona u organización que opera el ataque) y el `Adversary Customer` (quien se beneficia o financia la operación).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el rol del adversario que opera directamente el ataque? / What is the role of the adversary who directly operates the attack? | `Adversary Operator` |
| 2 | ¿Cómo se llama el rol que se beneficia del ataque / encarga la operación? / What is the role that benefits from the attack / commissions the operation? | `Adversary Customer` |

### Task 3: La víctima / The Victim

**Explicación:** La víctima se representa por sus `Victim Personae` (las personas u organizaciones atacadas), que son una de las aristas del modelo junto con los activos de la víctima.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se denomina a las personas u organizaciones atacadas en el modelo? / What are the persons or organisations attacked in the model called? | `Victim Personae` |

### Task 4: La capacidad / The Capability

**Explicación:** La capacidad del adversario es su arsenal de herramientas y técnicas: el `Adversary Arsenal` agrupa los payloads, exploits y métodos que se utilizan durante la intrusión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo se llama el arsenal de herramientas y técnicas del adversario? / What is the adversary's arsenal of tools and techniques called? | `Adversary Arsenal` |

### Task 5: La infraestructura / The Infrastructure

**Explicación:** La infraestructura se divide en `Type 2 Infrastructure` (dominios e IPs controlados por el adversario) y `Type 1 Infrastructure` (infraestructura legítima de la víctima u otras partes).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué tipo de infraestructura es la controlada por el adversario? / Which infrastructure type is controlled by the adversary? | `Type 2 Infrastructure` |
| 2 | ¿Qué tipo de infraestructura corresponde a la legítima o de la víctima? / Which infrastructure type corresponds to legitimate or victim-owned infrastructure? | `Type 1 Infrastructure` |

### Task 6: Características de la actividad / Activity Features

**Explicación:** Cada actividad del modelo se caracteriza por su fase (`Phase`), el resultado (`Result`) y los recursos empleados (`Resources`), que permiten correlacionar eventos de la intrusión.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué característica indica la etapa de la actividad? / Which feature indicates the stage of the activity? | `Phase` |
| 2 | ¿Qué característica describe el resultado de la actividad? / Which feature describes the outcome of the activity? | `Result` |
| 3 | ¿Qué característica recoge los recursos utilizados? / Which feature captures the resources used? | `Resources` |

### Task 7: Fase socio-política / Social-Political Phase

**Explicación:** Se analiza el contexto social y político del adversario y sus motivaciones dentro del modelo. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. | `No answer needed` |

### Task 8: Fase tecnológica / Technology Phase

**Explicación:** Se analiza la dimensión tecnológica del evento (herramientas, infraestructura y capacidad). No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee el contenido de la tarea. | `No answer needed` |

### Task 9: Laboratorio de cadena de ataque / Attack Chain Lab

**Explicación:** En el laboratorio se aplica el Diamond Model para construir la cadena de ataque completa del incidente. Al completarla se obtiene la flag `THM{DIAMOND_MODEL_ATTACK_CHAIN}`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la cadena de ataque del laboratorio? / What is the flag of the attack chain lab? | `THM{DIAMOND_MODEL_ATTACK_CHAIN}` |

### Task 10: Conclusión / Conclusion

**Explicación:** Cierre de la sala con el resumen del modelo del Diamante. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la conclusión de la sala. | `No answer needed` |

---

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Lee la introducción de la sala. | `No answer needed` |
| 2 | ¿Cómo se llama el rol del adversario que opera directamente el ataque? | `Adversary Operator` |
| 3 | ¿Cómo se llama el rol que se beneficia del ataque / encarga la operación? | `Adversary Customer` |
| 4 | ¿Cómo se denomina a las personas u organizaciones atacadas en el modelo? | `Victim Personae` |
| 5 | ¿Cómo se llama el arsenal de herramientas y técnicas del adversario? | `Adversary Arsenal` |
| 6 | ¿Qué tipo de infraestructura es la controlada por el adversario? | `Type 2 Infrastructure` |
| 7 | ¿Qué tipo de infraestructura corresponde a la legítima o de la víctima? | `Type 1 Infrastructure` |
| 8 | ¿Qué característica indica la etapa de la actividad? | `Phase` |
| 9 | ¿Qué característica describe el resultado de la actividad? | `Result` |
| 10 | ¿Qué característica recoge los recursos utilizados? | `Resources` |
| 11 | Lee el contenido de la tarea (fase socio-política). | `No answer needed` |
| 12 | Lee el contenido de la tarea (fase tecnológica). | `No answer needed` |
| 13 | ¿Cuál es la flag de la cadena de ataque del laboratorio? | `THM{DIAMOND_MODEL_ATTACK_CHAIN}` |
| 14 | Lee la conclusión de la sala. | `No answer needed` |

---

**Metodología:** La sala aplica el Diamond Model a un incidente real: se identifican los cuatro componentes básicos (Adversary Operator/Customer, Victim Personae, Adversary Arsenal e Infraestructura Type 1/Type 2) y las características de cada actividad (Phase, Result, Resources). A continuación se exploran las fases socio-política y tecnológica del modelo y, en el laboratorio final, se construye la cadena de ataque completa del incidente obteniendo la flag.

### Cadena de ataque / Attack Chain

```text
Adversary Operator/Customer -> Victim Personae -> Adversary Arsenal (capacidad) -> Infraestructura Type 2/Type 1 -> Activities (Phase, Result, Resources) -> Fase socio-política + tecnológica -> Laboratorio de cadena de ataque -> THM{DIAMOND_MODEL_ATTACK_CHAIN}
```

**Learning chain:** Diamond Model → Adversary Operator → Adversary Customer → Victim Personae → Adversary Arsenal → Type 2/Type 1 Infrastructure → Phase/Result/Resources → socio-política → tecnológica → cadena de ataque.

**Lección:** *El Diamond Model permite visualizar un incidente como un grafo de relaciones entre adversario, víctima, capacidad e infraestructura, y caracterizar cada actividad por su fase, resultado y recursos para reconstruir la cadena de ataque completa.*

**MITRE ATT&CK:** No aplica directamente (marco analítico); se puede correlacionar con técnicas como T1585 (Establish Accounts) y T1584 (Compromise Infrastructure).

**Fuente:** [TryHackMe - Diamond Model](https://tryhackme.com/room/diamondmodel)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.