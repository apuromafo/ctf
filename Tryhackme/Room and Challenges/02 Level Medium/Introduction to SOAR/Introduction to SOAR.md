# Introduction to SOAR

| **Dificultad** | MEDIUM | **Tipo** | Free | **Slug** | `introductiontosoar` |
| **Link** | [TryHackMe](https://tryhackme.com/room/introductiontosoar) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | SOAR / Orchestration / Playbooks / Alert Fatigue / Autopération / Respuesta a incidentes / TheHive | **Impacto** | Explica qué es SOAR y por qué nace (Alert Fatigue), diferencia Orchestration y Playbooks, automatiza la respuesta en el laboratorio con TheHive y captura la flag de la automatización |

---

**Contexto:** Sala introductoria a SOAR (Security Orchestration, Automation and Response): la respuesta al agotamiento de alertas (Alert Fatigue) de los equipos de seguridad. Se distingue la orquestación (conectar herramientas) de los playbooks (automatización de procesos), se decide cuándo automatizar (respuesta afirmativa "yay" con advisory lists y mitigation plan) y en la práctica se monta una automatización sobre TheHive que culmina con la flag `THM{AUT0M@T1N6_S3CUR1T¥}`.

## Solucionario

### Task 1: Introducción a SOAR

**Explicación:** Primer vistazo al concepto de SOAR y a la plataforma TheHive. No se requiere respuesta:

1. No answer needed

### Task 2: ¿Por Qué SOAR?

**Explicación:** El problema que motiva la adopción de SOAR en los SOC modernos:

2. Alert Fatigue

### Task 3: Orquestación y Playbooks

**Explicación:** Los dos bloques fundamentales del modelo SOAR:

3. 1. Orchestration
   2. Playbook

### Task 4: Decidiendo Automatizar

**Explicación:** Pregunta de validación (yay = sí) y componentes de la respuesta automática:

4. 1. yay
   2. Advisory lists
   3. mitigation plan

### Task 5: Automatizando la Respuesta (TheHive)

**Explicación:** Automatización práctica en TheHive; se obtiene la flag:

5. THM{AUT0M@T1N6_S3CUR1T¥}

### Task 6: Conclusión

**Explicación:** Cierre y repaso de la sala. No se requiere respuesta:

6. No answer needed

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué problema del SOC motiva el uso de SOAR? | `Alert Fatigue` |
| 2 | ¿Cómo se llama la conexión e integración de herramientas y procesos? | `Orchestration` |
| 3 | ¿Cómo se llama el documento/automatización que define los pasos de una tarea? | `Playbook` |
| 4 | Pregunta de validación (yay = sí) | `yay` |
| 5 | ¿Qué listas se usan como fuentes de intel en la automatización? | `Advisory lists` |
| 6 | ¿Qué incluye la respuesta automática ante el caso? | `mitigation plan` |
| 7 | Flag de la automatización | `THM{AUT0M@T1N6_S3CUR1T¥}` |

---

**Metodología:**
1. Identificar el problema raíz: Alert Fatigue.
2. Distinguir Orchestration (integraciones) de Playbooks (automatización de procesos).
3. Determinar cuándo automatizar (yay) y con qué componentes (Advisory lists, mitigation plan).
4. Montar la automatización en TheHive y extraer la flag.

**Learning chain:** Alert Fatigue → Orquestación → Playbooks → decisión de automatizar (yay) → Advisory lists → mitigation plan → TheHive → `THM{AUT0M@T1N6_S3CUR1T¥}`

**Lección:** *SOAR no reemplaza al analista: elimina el ruido repetitivo que lo agota. Cuando la orquestación conecta las fuentes y el playbook ejecuta el proceso, el SOC dedica su talento a lo que realmente importa: investigación, respuesta y mejora continua.*

**MITRE ATT&CK:** Sala defensiva de orquestación (blue team). Referencia a técnicas que SOAR ayuda a investigar y mitigar: T1110 - Brute Force; T1059 - Command and Scripting Interpreter; T1078 - Valid Accounts. La automatización de respuesta se alinea con los Courses of Action de las fuentes de intel (Advisory lists)

**Fuente:** [TryHackMe - Introduction to SOAR](https://tryhackme.com/room/introductiontosoar)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.