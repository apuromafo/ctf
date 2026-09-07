# Detection and Analysis

| **Dificultad** | Easy |
| **Tipo** | walkthrough |
| **Slug** | `detectionandanalysis` |
| **Link** | [TryHackMe](https://tryhackme.com/r/room/detectionandanalysis) |
| **Sección** | Incident Response |
| **Fuente** | THM |
| **Componentes** | Validation, Scoping, IOC Tracker, Ticketing, EntraID logs, Phishing analysis |
| **Impacto** | Segunda fase del ciclo IR NIST |

Contexto: Segunda fase del ciclo de vida IR: detección y análisis. Cubre validación de incidentes, alcance (scoping), triggers IR, inventario de activos, tracker de IOCs y laboratorio práctico con análisis de phishing e intrusión en Entra ID.

Solucionario:

## T2 - Detection and Analysis

| Pregunta | Respuesta | Explicación ES |
|----------|-----------|----------------|
| Proceso de confirmar que un incidente de seguridad realmente ocurrió | Detection | La detección implica verificar que la alerta corresponde a un incidente real |
| Proceso de entender el alcance completo de un incidente | Analysis | El análisis incluye cuentas, sistemas y datos afectados |

## T3 - IR Triggers and Communication

| Pregunta | Respuesta |
|----------|-----------|
| Tipo de trigger cuando un proveedor de inteligencia notifica de un compromiso | Third-party notification |
| Sistema que debe usarse para registrar cada acción durante la investigación IR | Ticketing systems |

## T4 - Asset Inventory and IOC Tracker

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué significa IOC? | Indicator of Compromise |
| Herramienta que proporciona registro continuo de indicadores maliciosos | IOC Tracker |

## T5 - Current Incident Context

| Pregunta | Respuesta |
|----------|-----------|
| Estoy listo para tareas prácticas | Completar |

## T6 - Detection Practical

| Pregunta | Respuesta |
|----------|-----------|
| IP de origen de los eventos de inicio de sesión sospechosos | 223.123.4.50 |
| Ciudad de origen del sign-in sospechoso | Amsterdam |
| Timestamp exacto del primer sign-in sospechoso en Laura Chen | 2026-03-30 04:41:30 PM |
| Asunto del email de phishing entregado a Laura Chen | HR Policy Update — Immediate Action Required |
| Dominio del remitente del email de phishing | nexus-verify.thm |

## T7 - Analysis Practical

| Pregunta | Respuesta |
|----------|-----------|
| Cuentas de Nexus Financial con actividad desde IP del atacante | 2 |
| Email de la segunda cuenta comprometida | k.patel@nexusfinancial.thm |
| Nombre de la regla de inbox creada en Laura Chen | Junk Filter Update |
| Empleados que recibieron el email de phishing inicial | 2 |

## T8 - Conclusion

| Pregunta | Respuesta |
|----------|-----------|
| Great work! Ready for Response and Recovery | Completar |

Fuentes: https://simontaplin.net/2026/06/10/answers-for-the-tryhackme-detection-and-analysis-room/ | https://medium.com/@sudoroot523/tryhackme-detection-and-analysis-8f4508665146 | https://medium.com/@lawvye/detection-and-analysis-thm-tryhackme-walkthrough-7523715d5475