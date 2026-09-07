# Preparation (IR)

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `irpreparation` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/irpreparation) |
| **Sección** | Incident Response |
| **Fuente** | THM |
| **Componentes** | NIST SP 800-61, Chain of Custody, SIEM, Detection Gap, VM Practical |
| **Impacto** | Preparación IR |

---

**Contexto:** Primera fase del ciclo NIST de respuesta a incidentes: preparación. Cubre definiciones, marcos NIST, personas/procesos/tecnología, logging y laboratorio práctico con inventario de activos.

## Solucionario

### T2 - What Is Incident Response

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué se declara tras confirmar una amenaza? | Incident |
| ¿Qué se debe completar antes de que el IR pueda comenzar formalmente? | Alert Triage |

### T3 - IR Frameworks

| Pregunta | Respuesta |
|----------|-----------|
| ¿Cuántas fases tiene el ciclo de vida NIST SP 800-61? | 4 |
| ¿Qué fase sigue a Containment, Eradication, and Recovery? | Post-Incident Activity |

### T4 - People, Processes, and Technology

| Pregunta | Respuesta |
|----------|-----------|
| Documento que rastrea el manejo de evidencia desde recolección hasta almacenamiento | Chain of Custody |

### T5 - Visibility, Logging, and Detection

| Pregunta | Respuesta |
|----------|-----------|
| Tipo de log que registra quién, qué y cómo respondió el sistema | Audit Log |
| Plataforma centralizada para colectar y analizar logs en una organización | SIEM |
| Situación donde se recolectan logs pero no hay reglas de alerta para actividad sospechosa | Detection Gap |

### T6 - Practical (VM)

| Pregunta | Respuesta |
|----------|-----------|
| IP del servidor de correo según inventario de activos | 10.10.10.2 |
| Control de autenticación faltante en reporte de pentest | Multi-Factor Authentication |
| Cantidad de hallazgos de alta severidad | 2 |
| Tipo de ataque registrado en NXF-INC-001 | Phishing Campaign |
| Longitud mínima de contraseña configurada | 6 |
| Configuración de auditoría para Audit account logon events | No Auditing |

---

**Fuentes:** https://simontaplin.net/2026/06/11/answers-for-the-tryhackme-preparation-room/ | https://medium.com/@lawvye/preparation-thm-tryhackme-practical-walkthrough-b81f0eacf4ee
