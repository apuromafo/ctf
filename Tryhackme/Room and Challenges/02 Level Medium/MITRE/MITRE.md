# MITRE

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Blue Team / Purple Team | mitre | https://tryhackme.com/room/mitre | 02 Level Medium | TryHackMe | MITRE ATT&CK, tácticas, técnicas, APT, detecciones | Modelado y detección de amenazas con ATT&CK |

---

**Contexto:** La sala **MITRE** introduce el framework **MITRE ATT&CK**, sus tácticas, técnicas y procedimientos (TTP), los grupos APT, las herramientas y los datos de detección. A lo largo del lab se navega por el repositorio de técnicas, se relaciona cada hallazgo con su táctica (como **Defense Evasion**), se analizan amenazas reales (APT, Cobalt Strike) y se conectan los identificadores de detección con la técnica que representan.

## Solucionario

### Task 1: Introducción
**Explicación:**

Presentación de la sala y del framework MITRE ATT&CK.

Respuesta: `No answer needed`

### Task 2: Tácticas y técnicas
**Explicación:**

Se identifica la **táctica** de un ejemplo concreto (`Defense Evasion`) y la **técnica** asociada (`T1136`, Create Account).

1. `Defense Evasion`
2. `T1136`

### Task 3: Amenaza de ejemplo
**Explicación:**

Análisis de una campaña/APT: la **región de origen** (`China`), la **técnica** de acceso inicial (`T1598`, Phishing for Information) y la **herramienta** utilizada (`Cobalt Strike`).

1. `China`
2. `T1598`
3. `Cobalt Strike`

### Task 4: Grupo APT
**Explicación:**

Sobre el grupo APT analizado se determinan: el **grupo** (`APT33`), el **tipo de cuenta** objetivo (`Cloud Accounts`), la **herramienta** usada (`Ruler`), la **técnica de gestión de cuentas** (`User Account Management`) y el **identificador de detección** (`DET0546`).

1. `APT33`
2. `Cloud Accounts`
3. `Ruler`
4. `User Account Management`
5. `DET0546`

### Task 5: Más técnicas
**Explicación:**

Se clasifican técnicas adicionales por su **táctica** (`Defense Evasion`) y por su **categoría contextual** (`Situational Awareness`).

1. `Defense Evasion`
2. `Situational Awareness`

### Task 6: Detección
**Explicación:**

Se inspeccionan los datos de detección: la técnica de análisis `User Geolocation Logon Pattern Analysis` y el **tipo de sensor** que la alimenta (`Network Traffic`).

1. `User Geolocation Logon Pattern Analysis`
2. `Network Traffic`

### Task 7: Técnica y táctica
**Explicación:**

Se identifica el **identificador** de la técnica/detección (`ADT3025`) y la **táctica** a la que pertenece (`Defense Evasion`).

1. `ADT3025`
2. `Defense Evasion`

### Task 8: Cierre
**Explicación:**

Resumen y reflexión final sobre el uso del framework MITRE ATT&CK.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción al framework | `No answer needed` |
| 2.1 | Táctica del ejemplo | `Defense Evasion` |
| 2.2 | Técnica asociada al ejemplo | `T1136` |
| 3.1 | Región de origen de la campaña | `China` |
| 3.2 | Técnica de acceso inicial | `T1598` |
| 3.3 | Herramienta utilizada | `Cobalt Strike` |
| 4.1 | Grupo APT | `APT33` |
| 4.2 | Tipo de cuenta objetivo | `Cloud Accounts` |
| 4.3 | Herramienta del grupo | `Ruler` |
| 4.4 | Técnica de gestión de cuentas | `User Account Management` |
| 4.5 | Identificador de detección | `DET0546` |
| 5.1 | Táctica de la técnica extra | `Defense Evasion` |
| 5.2 | Categoría contextual | `Situational Awareness` |
| 6.1 | Técnica de análisis | `User Geolocation Logon Pattern Analysis` |
| 6.2 | Tipo de sensor | `Network Traffic` |
| 7.1 | Identificador de la técnica | `ADT3025` |
| 7.2 | Táctica de la técnica | `Defense Evasion` |
| 8 | Cierre | `No answer needed` |

---

**Metodología:** Navegación por MITRE ATT&CK: identificación de tácticas, técnicas, herramientas y grupos APT, y correlación de identificadores de detección (ADT/DET) con las técnicas que cubren.

**Learning chain:** Framework ATT&CK → tácticas/técnicas → campañas y herramientas → grupos APT → detecciones → análisis de sensores.

**Lección:** *MITRE ATT&CK es el lenguaje común entre red team y blue team: conocer tácticas, técnicas y sus detecciones permite modelar y defender campañas reales.*

**MITRE ATT&CK:** T1136 Create Account · T1598 Phishing for Information · T1078 Valid Accounts.

**Fuente:** [TryHackMe - MITRE](https://tryhackme.com/room/mitre)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.