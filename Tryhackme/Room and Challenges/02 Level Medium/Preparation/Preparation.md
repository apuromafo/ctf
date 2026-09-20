# Preparation

| **Dificultad** | MEDIUM | **Tipo** | Walkthrough (Free) | **Slug** | `preparation` |
| **Link** | [TryHackMe](https://tryhackme.com/room/preparation) | **Sección** | Blue Team / Incident Response | **Fuente** | TryHackMe |
| **Componentes** | Incident Response, SANS PICERL, CSIRT, Chain of Custody, Jump Bag, Windows Event Logs, Software Restriction Policies, Audit Policies | **Impacto** | Prepara al analista para la fase de Preparation del ciclo de respuesta a incidentes: procesos, equipo, herramientas forenses y configuración de logs antes de que ocurra la brecha |

---

**Contexto:** Esta sala es la primera del camino de respuesta a incidentes y cubre la fase de Preparation del modelo SANS PICERL. Se estudian los conceptos de event e incident, las fases del ciclo de vida de la respuesta a incidentes, el equipo CSIRT, los documentos de cadena de custodia, la jump bag del respondedor y, en un laboratorio Windows, la configuración de Sysmon, Software Restriction Policies y Audit Policies con sus correspondientes IDs de eventos y valores por defecto.

> **ES:** Introducción a la preparación en respuesta a incidentes: fases del ciclo de vida, equipo de respuesta, cadena de custodia, jump bag y configuración de herramientas de registro en Windows antes de que ocurra un incidente.
> **EN:** Introduction to incident response preparation: lifecycle phases, response team, chain of custody, jump bag and configuration of Windows logging tools before an incident occurs.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Se presenta el objetivo de la sala: entender la fase de Preparation del modelo de respuesta a incidentes y las herramientas de las que debe disponerse antes de que ocurra un incidente.

1. No answer needed

### Task 2: La Respuesta a Incidentes y sus Fases / Incident Response and its Phases

**Explicación:** Un event (evento) es una ocurrencia observada dentro de un sistema, mientras que un incident es una violación de las políticas y prácticas de seguridad. Bajo la fase de Preparation las organizaciones establecen sus procedimientos, y bajo Recovery and Lessons Learned reanudan completamente las operaciones de negocio y actualizan sus capacidades de respuesta.

1. 1. Event
   2. Incident
   3. Preparation
   4. Recovery and Lessons Learned

### Task 3: El Equipo de Respuesta a Incidentes / The Incident Response Team

**Explicación:** Un grupo que maneja eventos que involucran violaciones de ciberseguridad, formado por individuos con distintas habilidades y experiencia, se conoce como cyber security incident response team (CSIRT). Los documentos que acompañan la evidencia recopilada y llevan el seguimiento de quién y cómo se maneja el proceso de investigación se denominan chain of custody documents.

1. 1. cyber security incident response team
   2. chain of custody documents

### Task 4: La Jump Bag / The Jump Bag

**Explicación:** Un kit que contiene todas las herramientas necesarias para el manejo de incidentes se denomina Jump bag. Debe incluir unidades de almacenamiento para la evidencia, software forense de imagen de disco (como FTK Imager y EnCase), taps de red, cables y adaptadores, y copias de los formularios de respuesta a incidentes.

1. Jump bag

### Task 5: Laboratorio de Windows / Windows Lab

**Explicación:** En el laboratorio Windows se consultan las reglas de Sysmon y las políticas locales: el Event ID de la regla File Created asociada a la prueba es 11. Bajo Software Restriction Policies, el nivel de seguridad por defecto asignado a todas las políticas es Unrestricted. En la carpeta Audit Policy dentro de Local Policies, el valor asignado a la política Audit logon events es Failure.

1. 1. 11
   2. Unrestricted
   3. Failure

### Task 6: Conclusión / Conclusion

**Explicación:** Se concluye la sala, habiendo comprendido la importancia de la preparación: tener procedimientos, equipo, herramientas y capacidades de registro listos antes del incidente, porque una organización sin preparación se ve forzada a improvisar durante una brecha.

1. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 2.1 | What is an observed occurrence within a system? | `Event` |
| 2.2 | What is described as a violation of security policies and practices? | `Incident` |
| 2.3 | Under which incident response phase do organisations lay down their procedures? | `Preparation` |
| 2.4 | Under which phase will an organisation resume business operations fully and update its response capabilities? | `Recovery and Lessons Learned` |
| 3.1 | A group that handles events involving cyber security breaches, comprising individuals with different skills and expertise, is known as? | `cyber security incident response team` |
| 3.2 | Which documents would be used to accompany any evidence collected and keeps track of who handles the investigation procedures? | `chain of custody documents` |
| 4.1 | What would a kit containing the necessary incident-handling tools be called? | `Jump bag` |
| 5.1 | What is the Event ID for the File Created rule associated with the test? | `11` |
| 5.2 | Under the Software Restriction Policies, what is the default security level assigned to all policies? | `Unrestricted` |
| 5.3 | Find the Audit Policy folder under Local Policies. What setting has been assigned to the policy Audit logon events? | `Failure` |

---

**Metodología:** Estudio conceptual de event vs incident y de las fases del ciclo de vida de la respuesta a incidentes (Preparation, Identification, Containment, Eradication, Recovery and Lessons Learned). Definición del CSIRT y de los documentos de cadena de custodia. Revisión del contenido de la jump bag del respondedor. En el laboratorio Windows se inspecciona la configuración de Sysmon (Event ID 11 para File Created), de Software Restriction Policies (nivel por defecto Unrestricted) y de Audit Policies (Audit logon events = Failure).

**Learning chain:** Event vs Incident → Fases de la respuesta a incidentes (Preparation, Recovery and Lessons Learned) → Equipo CSIRT → Chain of custody documents → Jump bag → Laboratorio Windows (Sysmon Event ID 11, SRP Unrestricted, Audit logon events Failure).

**Lección:** *La fase de Preparation determina el éxito de todo lo demás: sin procedimientos escritos, un equipo preparado, herramientas forenses y una jump bag lista, la organización se ve forzada a improvisar durante un incidente, multiplicando el daño y el tiempo de respuesta.*

**MITRE ATT&CK:** T1059.003 (Command and Scripting Interpreter: Windows Command Shell), T1560.001 (Archive Collected Data: Archive via Utility), T1082 (System Information Discovery)

**Fuente:** [TryHackMe - Preparation](https://tryhackme.com/room/preparation)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.