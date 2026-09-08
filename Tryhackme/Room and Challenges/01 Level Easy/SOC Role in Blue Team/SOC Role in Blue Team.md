# SOC Role in Blue Team

| **Dificultad** | Easy |
| **Tipo** | Sala teórica (SOC / Blue Team) |
| **Slug** | `socroleinblueteam` |
| **Link** | [TryHackMe](https://tryhackme.com/room/socroleinblueteam) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | CISO / Red Blue GRC Teams / CIRT (CSIRT/CERT) / L1 L2 Engineer Manager / MSSP / career path |
| **Impacto** | Sala introductoria sobre el rol y el propósito del Blue Team: la jerarquía de seguridad corporativa bajo el CISO, los equipos Red y GRC, el papel del SOC (L1, L2, Engineers, Manager), el CIRT para incidentes urgentes, los roles especializados (Digital Forensics, Threat Intel, AppSec, AI Researcher), la diferencia entre un SOC interno y un MSSP, las rutas de carrera y un reto final que entrega una flag. |

---

**Contexto:** El módulo explica la estructura de seguridad en empresas grandes: el **CISO** es el cargo senior que toma las decisiones de ciberseguridad; el **Blue Team** es el nombre común para los defensores (analistas SOC, ingenieros y responders). El SOC está formado por **L1** (triage y pases a L2), **L2** (ataques avanzados), **Engineers** (configuración de EDR/SIEM) y **Manager**. Cuando el incidente se desborda, entra el **CIRT** (CSIRT/CERT). Para empresas sin SOC propio existen los **MSSP** (outsourcing de seguridad), y la ruta natural de un analista SOC L1 sigue con **SOC L2 Analyst**. El reto final entrega `THM{trysecureme_is_secured!}`.

## Solucionario

### Task 1: Introducción

**Explicación:** La sala asume haber completado la sala "Junior Security Analyst".

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He leído la introducción. | `No answer needed` |

### Task 2: Jerarquía de seguridad

**Explicación:** En empresas grandes el CISO supervisa equipos especializados: Red Team (ofensiva), GRC (políticas y compliance) y Blue Team (defensa). Los analistas SOC y los ingenieros encajan en el **Blue Team**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué cargo senior toma normalmente las decisiones clave de ciberseguridad? | `CISO` |
| 2 | ¿Cuál es el nombre común para roles como analistas o ingenieros SOC? | `Blue Team` |

### Task 3: Conoce al Blue Team

**Explicación:** El SOC se organiza en L1, L2, Engineers y Manager. Si el SOC no puede manejar el incidente, entra el CIRT (también llamado CSIRT o CERT), el equipo "bombero" que atiende incidentes activos o urgentes (ej.: JPCERT, Mandiant, AWS CIRT). El Blue Team se enfoca en la seguridad defensiva y existen roles especializados (Digital Forensics, Threat Intelligence, AppSec, AI Researcher).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿El Blue Team se enfoca en seguridad defensiva u ofensiva? | `Defensive` |
| 2 | ¿Qué departamento maneja los incidentes cibernéticos activos o urgentes? | `CIRT` |

### Task 4: Avanzando en la carrera SOC

**Explicación:** Las organizaciones sin capacidad para operar un SOC propio contratan un MSSP (Managed Security Services Provider) que presta servicios de seguridad externalizados. Para un analista SOC L1, la ruta natural de crecimiento es convertirse en **SOC L2 Analyst**.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cómo llamarías a una empresa de ciberseguridad que provee servicios SOC? | `MSSP` |
| 2 | ¿Qué rol continúa naturalmente tu trayectoria como analista SOC L1? | `SOC L2 Analyst` |

### Task 5: Reto final

**Explicación:** Pequeño reto de verificación (en la variante de la sala se usa una máquina desplegada) que cierra el módulo.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag obtuviste al completar el reto final? | `THM{trysecureme_is_secured!}` |

### Task 6: Conclusión

**Explicación:** Cierre del módulo con el resumen del lugar del SOC en la estructura corporativa.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | He leído la conclusión. | `No answer needed` |

---

**Metodología:** Lectura de la jerarquía corporativa (Red/GRC/Blue) → repaso de la estructura del SOC y del CIRT → identificación de los roles especializados → comparación SOC interno vs MSSP → revisión de la ruta de carrera → reto final de verificación.
**Learning chain:** CISO y departamentos de seguridad → Blue Team como rol defensor → SOC (L1/L2/Engineers/Manager) → CIRT ante incidentes → MSSP y carrera SOC L1→L2 → flag final.
**MITRE ATT&CK:** T1566 (Phishing - defensa), T1078 (Valid Accounts - defensa), T1059.003 (Windows Command Shell - defensa)
**Fuente:** [TryHackMe - SOC Role in Blue Team](https://tryhackme.com/room/socroleinblueteam)