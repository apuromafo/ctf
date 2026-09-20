# Dependency Management

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `dependencymanagement` | [TryHackMe](https://tryhackme.com/room/dependencymanagement) | 01 Level Easy | THM | Supply Chain, Dependency Confusion, Typosquatting, MageCart | RCE mediante dependencias y cadena de suministro |

> **Objeto:** Comprender los ataques a la cadena de suministro de software: dependencias internas y externas, typosquatting, versionado, dependency confusion y el ataque MageCart, defendiendo y replicando cada escenario.

---

**Contexto:** Sala sobre la gestión de dependencias y la seguridad de la cadena de suministro: clasificación de dependencias en internas y externas, análisis de ataques como typosquatting, manipulación de versiones, dependency confusion y MageCart, y defensa frente a cada uno de ellos.

> **ES:** Sala sobre supply chain: tipos de dependencias, typosquatting, versionado, dependency confusion y MageCart, con escenarios de ataque y defensa.
> **EN:** Room about the supply chain: dependency types, typosquatting, versioning, dependency confusion and MageCart, with attack and defense scenarios.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y del concepto de cadena de suministro.

No answer needed

### Task 2: Conceptos / Concepts
**Explicación:** Definición del ingrediente que compone una aplicación: las dependencias.

Dependencies

### Task 3: Tipos / Types
**Explicación:** Clasificación de las dependencias según su origen.

1. Internal
2. External

### Task 4: Ataque / Attack
**Explicación:** Escenario de ataque sobre una dependencia comprometida tipo MageCart.

1. MageCart
2. supersecretpassword12345@
3. THM{Supply.Chain.Attacks.Are.Super.Powerful}

### Task 5: Defensa / Defense
**Explicación:** Se razona qué dependencia debe revisarse con más detalle para defender la aplicación.

Internal dependency

### Task 6: Amenazas / Threats
**Explicación:** Se analizan técnicas como el typosquatting y el abuso de versiones.

1. Typosquatting
2. Version

### Task 7: Explotación final / RCE
**Explicación:** Se replica el dependency confusion para conseguir ejecución remota de código.

1. Dependency Confusion
2. THM{RCE.Through.Dependency.Confusion}

### Task 8: Recapitulación / Recap
**Explicación:** Cierre y recapitulación de la sala.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2 | ¿Qué compone una aplicación? | `Dependencies` |
| 3.1 | Dependencia dentro de la organización | `Internal` |
| 3.2 | Dependencia de terceros | `External` |
| 4.1 | Tipo de inyección de skimmer | `MageCart` |
| 4.2 | Secreto robado | `supersecretpassword12345@` |
| 4.3 | Flag del escenario de ataque | `THM{Supply.Chain.Attacks.Are.Super.Powerful}` |
| 5 | Dependencia a vigilar | `Internal dependency` |
| 6.1 | Técnica de suplantación de nombre | `Typosquatting` |
| 6.2 | Vector de abuso de lanzamiento | `Version` |
| 7.1 | Conflicto de nombres entre repositorios | `Dependency Confusion` |
| 7.2 | Flag del RCE | `THM{RCE.Through.Dependency.Confusion}` |
| 8 | — | `No answer needed` |

---

**Metodología:** Revisión de los conceptos de dependencias, clasificación en internas y externas, ejecución de los escenarios de ataque (MageCart, typosquatting, abuso de versiones y dependency confusion), priorización de la defensa y obtención de los flags de cada caso.

### Cadena de ataque / Attack Chain

Dependencias → tipos (interna/externa) → ataque MageCart → typosquatting → versiones → dependency confusion → RCE.

**Learning chain:** supply chain → dependencias → MageCart → typosquatting → versiones → dependency confusion → RCE → flag

*Lección:* La cadena de suministro es un vector real: typosquatting, versionado y dependency confusion permiten ejecutar código dentro de aplicaciones aparentemente seguras.

**MITRE ATT&CK:** TA0002 Execution, T1195 Supply Chain Compromise, T1204 User Execution.

**Fuente:** [TryHackMe - Dependency Management](https://tryhackme.com/room/dependencymanagement)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.