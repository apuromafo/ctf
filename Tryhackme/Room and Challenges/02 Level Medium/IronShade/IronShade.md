# IronShade

| **Dificultad** | MEDIUM | **Tipo** | Free | **Slug** | `ironshade` |
| **Link** | [TryHackMe](https://tryhackme.com/room/ironshade) | **Sección** | 02 Level Medium | **Fuente** | texto oficial THM + anotaciones propias |
| **Componentes** | Threat Hunting / Linux Forensics / Crontab Persistence / Systemd / Cron / Cron jobs / Malware Analysis / IOC Hunting | **Impacto** | Caza al malware IronShade en un host Linux: se localizan los artefactos de persistencia (cron/systemd), directorios ocultos, servicios comprometidos, conexiones de C2 y se recupera la flag de la investigación |

---

**Contexto:** Sala de threat hunting centrada en la familia de malware IronShade sobre un host Linux comprometido. La investigación sigue el rastro completo del adversario: el usuario/artefacto `mircoservice` con su entrada de cron `@reboot /home/mircoservice/printer_app`, el directorio oculto `.strokes`, la manipulación de `.systmd` y de los servicios `backup.service, strokes.service`, el primer evento a las `Aug  5 22:05:33`, la IP de C2 `10.11.75.247`, el escáner `pscanner` y finalmente la flag `{_tRy_Hack_ME_}`.

## Solucionario

### Task 1: Caza de IronShade en el Host Linux

**Explicación:** Investigación de los 12 hitos de la cadena de infección:

1. `dc7c8ac5c09a4bbfaf3d09d399f10d96` — hash/artefacto identificado primero en el análisis
2. `mircoservice` — usuario/entidad asociado al malware
3. `@reboot /home/mircoservice/printer_app` — entrada de crontab usada para la persistencia
4. `.strokes` — directorio oculto empleado por el adversario
5. `2` — número de elementos/escalón del hallazgo
6. `.systmd` — directorio de systemd manipulado
7. `backup.service, strokes.service` — servicios comprometidos/relacionados
8. `Aug  5 22:05:33` — timestamp del primer evento relevante
9. `10.11.75.247` — IP de conexión/C2 del adversario
10. `8` — segundo recuento de la investigación
11. `pscanner` — herramienta/escáner desplegado por el adversario
12. `{_tRy_Hack_ME_}` — flag final recuperada

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el primer hash/artefacto identificado en el host? | `dc7c8ac5c09a4bbfaf3d09d399f10d96` |
| 2 | ¿Qué usuario/entidad está detrás del artefacto? | `mircoservice` |
| 3 | ¿Qué entrada de crontab garantiza la persistencia? | `@reboot /home/mircoservice/printer_app` |
| 4 | ¿Qué directorio oculto usa el adversario? | `.strokes` |
| 5 | Primer recuento de la investigación | `2` |
| 6 | ¿Qué directorio de systemd está manipulado? | `.systmd` |
| 7 | ¿Qué servicios quedan comprometidos/relacionados? | `backup.service, strokes.service` |
| 8 | ¿Cuándo ocurre el primer evento? | `Aug  5 22:05:33` |
| 9 | ¿Qué IP usa la conexión del adversario? | `10.11.75.247` |
| 10 | Segundo recuento de la investigación | `8` |
| 11 | ¿Qué herramienta/escáner despliega el adversario? | `pscanner` |
| 12 | ¿Cuál es la flag final? | `{_tRy_Hack_ME_}` |

---

**Metodología:**
1. Identificar el primer artefacto del malware (hash) y el usuario asociado (`mircoservice`).
2. Revisar los mecanismos de persistencia: crontab (`@reboot .../printer_app`) y systemd (`.systmd`).
3. Localizar el directorio oculto `.strokes` y los servicios `backup.service, strokes.service`.
4. Establecer la línea de tiempo desde el primer evento (`Aug 5 22:05:33`).
5. Correlacionar la IP de C2 (`10.11.75.247`) y la herramienta `pscanner`.
6. Recuperar la flag final `{_tRy_Hack_ME_}`.

**Learning chain:** dc7c8ac5... → mircoservice → @reboot printer_app → .strokes → 2 → .systmd → backup.service/strokes.service → Aug 5 22:05:33 → 10.11.75.247 → 8 → pscanner → `{_tRy_Hack_ME_}`

**Lección:** *Huntear malware como IronShade exige seguir la persistencia: del artefacto al usuario, del crontab al systemd, de los directorios ocultos a los servicios. Cada hallazgo cierra un hueco en la línea de tiempo y, al final, la cadena completa revela la C2 y la flag.*

**MITRE ATT&CK:** T1053.003 - Scheduled Task/Job: Cron; T1543.002 - Create or Modify System Process: Systemd Service; T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys; T1071.001 - Application Layer Protocol: Web Protocols (C2); T1040 - Network Sniffing / T1046 - Network Service Discovery (pscanner); T1036 - Masquerading (directorios ocultos)

**Fuente:** [TryHackMe - IronShade](https://tryhackme.com/room/ironshade)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.