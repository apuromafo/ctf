# AppSec IR

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Defensivo / Incident Response | appsecir | https://tryhackme.com/room/appsecir | 02 Level Medium | TryHackMe | SIEM, OWASP Top 10, Playbooks, WAF | Gestión de incidentes en aplicaciones |

---

**Contexto:** La sala **AppSec IR** combina seguridad de aplicaciones y respuesta a incidentes: enseña a detectar compromisos de una aplicación mediante el **SIEM**, aplicar **Containment**, diseñar aplicaciones **Secure by Design**, alinearse con el OWASP Top 10 (especialmente `A09: Security Logging and Monitoring Failures`), manejar recompensas como **Bug Bounty**, mitigar con **WAF** y **Feature Flags**, y ejecutar **IR Playbooks**, **hotfixes** y **Post-mortems**. Termina con una flag de la sala que acredita el rol del respondedor.

## Solucionario

### Task 1: Introducción a AppSec IR
**Explicación:**

Se presenta el marco de trabajo que une el desarrollo seguro de aplicaciones con la respuesta a incidentes.

Respuesta: `No answer needed`

### Task 2: Detección inicial
**Explicación:**

Se identifica el sistema donde se correlacionan los eventos de seguridad de la aplicación y la fase inmediata que busca detener la propagación del incidente.

1. `SIEM`
2. `Containment`

### Task 3: Principios y estándares
**Explicación:**

Se listan los pilares teóricos de la sala: el enfoque de desarrollo que integra la seguridad desde el diseño, la categoría del OWASP Top 10 que penaliza la ausencia de logging y monitoreo, y el documento de procedimientos de respuesta a incidentes.

1. `Secure by Design`
2. `A09: Security Logging and Monitoring Failures`
3. `IR Playbooks`

### Task 4: Defensa de la aplicación
**Explicación:**

Se identifican los controles preventivos y organizativos: el programa de divulgación responsable de vulnerabilidades, el interruptor de despliegue de funcionalidades y el firewall a nivel de aplicación.

1. `Bug Bounty`
2. `Feature Flag`
3. `WAF`

### Task 5: Ciclo del incidente
**Explicación:**

Se ordenan las fases de la respuesta: el parche rápido de emergencia, la acción de contención, el análisis posterior y el documento final del incidente.

1. `hotfix`
2. `Containment`
3. `Post-mortem`
4. `Incident Report`

### Task 6: Flag de la sala
**Explicación:**

Se obtiene la flag que acredita haber completado el ejercicio de respuesta a incidentes de aplicaciones.

Respuesta: `THM{AppS3c_Inc1d3NT_R3sp0Nder}`

### Task 7: Cierre
**Explicación:**

Se consolida el aprendizaje sobre la integración del AppSec con el Incident Response.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción | `No answer needed` |
| 2.1 | Sistema de correlación de eventos | `SIEM` |
| 2.2 | Fase inmediata de respuesta | `Containment` |
| 3.1 | Enfoque de desarrollo seguro | `Secure by Design` |
| 3.2 | Categoría OWASP Top 10 de logging/monitoring | `A09: Security Logging and Monitoring Failures` |
| 3.3 | Procedimiento documentado de respuesta | `IR Playbooks` |
| 4.1 | Programa de divulgación de vulnerabilidades | `Bug Bounty` |
| 4.2 | Interruptor de despliegue de features | `Feature Flag` |
| 4.3 | Firewall de aplicación web | `WAF` |
| 5.1 | Parche de emergencia | `hotfix` |
| 5.2 | Fase de contención | `Containment` |
| 5.3 | Análisis posterior al incidente | `Post-mortem` |
| 5.4 | Documento oficial del incidente | `Incident Report` |
| 6 | Flag de la sala | `THM{AppS3c_Inc1d3NT_R3sp0Nder}` |
| 7 | Cierre | `No answer needed` |

---

**Metodología:** Respuesta a incidentes aplicada a aplicaciones: detección (SIEM), contención, estándares (OWASP Top 10 / Secure by Design), controles (WAF, Feature Flag, Bug Bounty) y ciclo de vida del incidente (hotfix, post-mortem, informe).

**Learning chain:** Detección → contención → estándares → controles de defensa → ciclo del incidente → flag → cierre.

**Lección:** *La seguridad de aplicaciones no termina en el deploy: sin telemetría (logging/monitoring) no hay ni detección ni respuesta.*

**MITRE ATT&CK:** T1078 Valid Accounts · T1190 Exploit Public-Facing Application · TA0009 Collection (visión defensiva/detección); categoría OWASP A09:2021.

**Fuente:** [TryHackMe - AppSec IR](https://tryhackme.com/room/appsecir)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.