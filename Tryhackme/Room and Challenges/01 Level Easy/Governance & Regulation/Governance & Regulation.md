# Governance & Regulation

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|--------------|---------|
| Easy | walkthrough | `governanceregulation` | [TryHackMe](https://tryhackme.com/room/governanceregulation) | 01 Level Easy | THM | Gobernanza, Regulación, Riesgo, Frameworks, Controles | Conceptos de gobernanza y regulación en ciberseguridad |

---

**Contexto:** Sala del Beginner Path sobre gobernanza y regulación: repasa la diferencia entre gobernanza y regulación, el ciclo de revisión de políticas, la gestión de riesgos, los frameworks como PCI DSS, los tipos de controles (físicos y administrativos), el tratamiento del riesgo y la disponibilidad.

> **ES:** Recorrer los conceptos de gobernanza, regulación, gestión de riesgos, frameworks y controles de seguridad.
> **EN:** Walk through governance, regulation, risk management, frameworks and security controls.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Presentación de la sala.

No answer needed

### Task 2: Gobernanza y regulación / Governance and Regulation

**Explicación:** Se distingue entre regulación (norma dinámica que hay que cumplir) y gobernanza, y se identifican sectores regulados como el sanitario.

1. `Regulation`
2. `Healthcare`

### Task 3: Políticas / Policies

**Explicación:** Las políticas de la organización se revisan y actualizan, y se formalizan a través de un procedimiento.

1. `Review and update`
2. `Procedure`

### Task 4: Gestión de riesgos / Risk Management

**Explicación:** La gestión de riesgos se encarga de gestionar el riesgo de negocio, y las organizaciones deben involucrarse en ella.

1. `Risk Management`
2. `yea`

### Task 5: Frameworks / Frameworks

**Explicación:** Se repasan los niveles del estándar PCI DSS (4 niveles) y los datos que protege por defecto: los datos de tarjetas (cardholder data).

1. `4`
2. `cardholder data`

### Task 6: Controles / Controls

**Explicación:** Los controles pueden ser de tipo físico o administrativo, y conviene mapearlos con los riesgos asociados.

1. `Physical`
2. `Administrative`
3. `Map`

### Task 7: Tratamiento del riesgo / Risk Treatment

**Explicación:** Se identifican las opciones de tratamiento del riesgo y se garantiza la disponibilidad de los servicios.

1. `Risk treatment`
2. `Availability`

### Task 8: Bandera / Flag

**Explicación:** Al completar la sala se revela la bandera final.

`THM{SECURE_1001}`

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Norma dinámica a cumplir | `Regulation` |
| 2.2 | Sector regulado | `Healthcare` |
| 3.1 | Acción sobre las políticas | `Review and update` |
| 3.2 | Formalización de las políticas | `Procedure` |
| 4.1 | Gestión del riesgo de negocio | `Risk Management` |
| 4.2 | ¿Deben involucrarse las organizaciones? | `yea` |
| 5.1 | Niveles del estándar | `4` |
| 5.2 | Datos protegidos por defecto | `cardholder data` |
| 6.1 | Tipo de control 1 | `Physical` |
| 6.2 | Tipo de control 2 | `Administrative` |
| 6.3 | Relación control-riesgo | `Map` |
| 7.1 | Opciones sobre los riesgos | `Risk treatment` |
| 7.2 | Garantía de servicio | `Availability` |
| 8 | Bandera final | `THM{SECURE_1001}` |

---

**Metodología:** Comprender la diferencia gobernanza/regulación, mantener las políticas revisadas y formalizadas, gestionar el riesgo de negocio, aplicar frameworks (PCI DSS) y controles (físicos/administrativos) mapeados contra los riesgos, y cerrar con el tratamiento del riesgo y la disponibilidad.

### Cadena de ataque / Attack Chain

```text
Introducción -> gobernanza y regulación -> políticas -> gestión de riesgos -> frameworks (PCI DSS) -> controles -> tratamiento del riesgo -> flag
```

**Learning chain:** Governance → Regulation → Policies → Risk Management → Frameworks → Controls → Risk Treatment

**Lección:** *La ciberseguridad no es solo técnica: gobernanza, regulación y gestión de riesgos definen el marco que obliga a proteger los activos críticos como los datos de tarjetas.*

**MITRE ATT&CK:** N/A (Room de gobernanza/regulación)

**Fuente:** [TryHackMe - Governance & Regulation](https://tryhackme.com/room/governanceregulation)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.