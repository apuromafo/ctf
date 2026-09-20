# MISP

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Blue Team / Threat Intelligence | misp | https://tryhackme.com/room/misp | 02 Level Medium | TryHackMe | MISP, threat intelligence, eventos, feeds, atributos | Enriquecimiento y gestión de inteligencia de amenazas |

---

**Contexto:** La sala **MISP** es una práctica sobre la plataforma **MISP** (Malware Information Sharing Platform). Se recorren los conceptos de **threat intelligence**, el uso de **eventos**, **atributos** y **feeds** de inteligencia, así como la correlación de indicadores con grupos APT (atribuciones, tipos de malware y etiquetas OSINT). En el lab se crean eventos, se gestiona la organización y se analizan datos de amenazas directamente en el portal.

## Solucionario

### Task 1: Concepto de Threat Intelligence
**Explicación:**

Introducción a la inteligencia de amenazas y a la plataforma de intercambio de información entre organizaciones.

Respuesta: `No answer needed`

### Task 2: Iniciar el lab
**Explicación:**

Arranque del laboratorio MISP y acceso al portal de la plataforma.

Respuesta: `No answer needed`

### Task 3: Organización
**Explicación:**

Se practica la gestión del portal: el número de la organización/bloque consultado (`4`) y el **rol administrativo** correspondiente (`Organisation Admin`).

1. `4`
2. `Organisation Admin`

### Task 4: Eventos
**Explicación:**

Creación y gestión de **eventos** dentro de la plataforma MISP para agrupar los indicadores.

Respuesta: `No answer needed`

### Task 5: Análisis de atributos
**Explicación:**

Inspeccionando los eventos con los datos disponibles se responden los valores: el **número de evento** (`1145`), el **tipo de amenaza** (`Remote Access`), la **IP origen** (`89.107.62.39`), la **atribución** al grupo `Magic Hound` y el **tipo/tag del indicador** (`OSINT`).

1. `1145`
2. `Remote Access`
3. `89.107.62.39`
4. `Magic Hound`
5. `OSINT`

### Task 6: Cierre
**Explicación:**

Revisión de lo aprendido en la sala y del ciclo de inteligencia de amenazas.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Concepto de Threat Intelligence | `No answer needed` |
| 2 | Inicio del lab | `No answer needed` |
| 3.1 | Número de la organización consultada | `4` |
| 3.2 | Rol administrador de la organización | `Organisation Admin` |
| 4 | Gestión de eventos | `No answer needed` |
| 5.1 | Número de evento | `1145` |
| 5.2 | Tipo de amenaza | `Remote Access` |
| 5.3 | Dirección IP origen | `89.107.62.39` |
| 5.4 | Grupo APT de la atribución | `Magic Hound` |
| 5.5 | Tipo de indicador | `OSINT` |
| 6 | Cierre de la sala | `No answer needed` |

---

**Metodología:** Uso de la plataforma MISP: gestión de organización y roles, creación de eventos, análisis de atributos y correlación de indicadores con grupos de amenazas persistentes (APT).

**Learning chain:** Threat intelligence → MISP → organización/roles → eventos → atributos → atribución APT → OSINT.

**Lección:** *Una plataforma de intercambio como MISP convierte indicadores sueltos en inteligencia accionable cuando la gestión de eventos, roles y atribuciones está bien configurada.*

**MITRE ATT&CK:** T1204.002 User Execution: Malicious File · T1598 Phishing for Information (contexto de CTI).

**Fuente:** [TryHackMe - MISP](https://tryhackme.com/room/misp)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.