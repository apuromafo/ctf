# Island Orchestration

| **Dificultad** | MEDIUM | **Tipo** | Free | **Slug** | `islandorchestration` |
| **Link** | [TryHackMe](https://tryhackme.com/room/islandorchestration) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Orchestration / CTF práctico / Flag CTF | **Impacto** | Reto práctico de orquestación en el que se recorre la infraestructura desplegada hasta recuperar la flag única de la sala |

---

**Contexto:** Sala práctica orientada a la orquestación de servicios en un entorno desplegado estilo CTF. Siguiendo la secuenciación de componentes del lab se avanza hasta obtener la flag de la sala, que confirma la explotación/completado correcto de la infraestructura.

## Solucionario

### Task 1: Obtener la Flag de la Sala

**Explicación:** Flag única de la sala:

1. flag{08bed9fc0bc6d94fff9e51f291577841}

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es la flag de la sala? | `flag{08bed9fc0bc6d94fff9e51f291577841}` |

---

**Metodología:**
1. Desplegar/revisar la infraestructura orquestada del lab.
2. Recorrer los servicios expuestos según la secuencia de la sala.
3. Obtener y validar la flag de la sala.

**Learning chain:** Lab orquestado → secuenciación de servicios → flag

**Lección:** *La orquestación correcta de la infraestructura es la clave de un lab reproducible: desplegar, secuenciar y exponer los servicios en orden es lo que permite alcanzar la flag sin ambigüedad.*

**MITRE ATT&CK:** T1190 - Exploit Public-Facing Application; lab marcado como sala de orquestación: la flag confirma la correcta puesta en marcha de la infraestructura (blue-team/engineering) más que un TTP ofensivo concreto.

**Fuente:** [TryHackMe - Island Orchestration](https://tryhackme.com/room/islandorchestration)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.