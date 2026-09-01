 
# 🕵️‍♂️ Health Hazard — Recursos y Soluciones / Resources & Solutions [EASY]

Este documento recopila las guías y tutoriales para resolver el escenario de **Health Hazard** en TryHackMe.
This document compiles guides and tutorials to solve the **Health Hazard** scenario on TryHackMe.

## 📝 Guías de Análisis y Blogs (Paso a Paso) / Analysis Guides & Blogs (Step by Step)

Estas fuentes contienen la explicación detallada de las consultas (KQL/Splunk/ELK) y el razonamiento detrás de la investigación.

* **[RedTrib3 Blog]** - [Threat Hunting Simulator: Health Hazard](https://blog.redtrib3.in/threat-hunting-simulator-health-hazard?source=more_articles_bottom_blogs)
* *Ideal para entender el flujo de la investigación y el contexto de las amenazas detectadas.*


* **[Medium - iamdonu1]** - [TryHackMe Threat Hunting Simulator Health Hazard](https://medium.com/@iamdonu1/tryhackme-threat-hunting-simulator-health-hazard-99f012e10bd5)
* *Una guía detallada que cubre las preguntas del reto con capturas de pantalla y explicaciones.*



## 💻 Repositorios y Notas Rápidas (Code Snippets) / Repositories & Quick Notes

Referencia directa de comandos y respuestas para una consulta rápida.

* **[GitHub Gist - macostag]** - [THM Health Hazard Notes](https://gist.github.com/macostag/4afaa0183ead00a995c024e167376fa0)
* *Contiene las consultas técnicas y las flags/respuestas organizadas de forma esquemática.*



## 🎥 Walkthroughs en Video (Visual) / Video Walkthroughs

Tutoriales en formato video para observar la ejecución de las herramientas en tiempo real.

1. **[Walkthrough 1]** - [Ver en YouTube](https://www.youtube.com/watch?v=sIHwb98z-8A)
2. **[Walkthrough 2]** - [Ver en YouTube](https://www.youtube.com/watch?v=dr3FOabXU0Q)

---

### 🛠️ Pwn Techniques Note:

Como este reto se basa en **Threat Hunting**, la clave suele estar en identificar:

* **Procesos sospechosos:** (ej. `powershell.exe` ejecutando comandos codificados en Base64).
* **Conexiones de red:** IPs externas inusuales o balizamiento (beaconing).
* **Persistencia:** Modificaciones en el registro o tareas programadas.

¿Te gustaría que extraiga las **consultas específicas (Queries)** de estos enlaces y te las organice en una tabla para que las tengas listas para copiar y pegar en el simulador?

---

**Fuentes / Sources:**
- [RedTrib3 Blog — Threat Hunting Simulator: Health Hazard](https://blog.redtrib3.in/threat-hunting-simulator-health-hazard) — RedTrib3
- [Medium — iamdonu1 — TryHackMe Threat Hunting Simulator Health Hazard](https://medium.com/@iamdonu1/tryhackme-threat-hunting-simulator-health-hazard-99f012e10bd5) — iamdonu1
- [GitHub Gist — macostag — THM Health Hazard Notes](https://gist.github.com/macostag/4afaa0183ead00a995c024e167376fa0) — macostag
- [YouTube — Walkthrough 1](https://www.youtube.com/watch?v=sIHwb98z-8A)
- [YouTube — Walkthrough 2](https://www.youtube.com/watch?v=dr3FOabXU0Q)

**Autor del documento / Document author:** Apuromafo
**Fecha de acceso / Access date:** 2026-09-01