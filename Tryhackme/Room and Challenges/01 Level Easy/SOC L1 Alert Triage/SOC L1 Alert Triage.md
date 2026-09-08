# SOC L1 Alert Triage

| **Dificultad** | Easy |
| **Tipo** | Sala práctica (SOC / Blue Team) |
| **Slug** | `socl1alerttriage` |
| **Link** | [TryHackMe](https://tryhackme.com/room/socl1alerttriage) |
| **Sección** | 01 Level Easy |
| **Fuente** | TryHackMe |
| **Componentes** | SOC / dashboard / triaje de alertas / priorización por severidad / In Progress / veredictos / filtración de datos |
| **Impacto** | Sala que pone al alumno en el rol de analista SOC L1 frente a un dashboard: contar las alertas activas, identificar la más reciente, revisar veredictos previos (False Positive), decidir el orden de priorización (primero media antes que baja severidad, y primero las alertas nuevas), autoasignarse la primera alerta (Potential Data Exfiltration), cambiar su estado a In Progress y obtener flags al triar correctamente tres alertas reales. |

---

**Contexto:** El reto simula un SOC con un dashboard de alertas. El análisis del panel y de los avisos muestra 5 alertas, siendo la más reciente "Double-Extension File Creation". En una alerta previa, "Unusual VPN Login Location", el veredicto fue *False Positive* y mencionaba al usuario `M.Clark`. La política de priorización dicta atender la severidad media sobre la baja (Yea) pero no las alertas más antiguas primero (Nay). La primera alerta a priorizar es "Potential Data Exfiltration"; al triar correctamente las tres alertas priorizadas se obtienen tres flags.

## Solucionario

### Task 1: Dashboard del SOC

**Explicación:** Se abre la máquina y el dashboard de alertas. Empezando por los datos globales: número de alertas visibles y la alerta más reciente.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el número de alertas que ves en el dashboard del SOC? | `5` |
| 2 | ¿Cuál es el nombre de la alerta más reciente que ves? | `Double-Extension File Creation` |

### Task 2: Revisión del veredicto

**Explicación:** Se revisa una alerta previa ya resuelta para reconstruir el contexto del analista.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál fue el veredicto de la alerta "Unusual VPN Login Location"? | `False Positive` |
| 2 | ¿Qué usuario se mencionaba en la alerta "Unusual VPN Login Location"? | `M.Clark` |

### Task 3: Priorización de alertas

**Explicación:** La guía del SOC define el orden de triaje: la severidad media se prioriza sobre la baja, y las alertas más nuevas se atienden antes que las antiguas.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Deberías priorizar primero las alertas de severidad media sobre las de baja? (Yea/Nay) | `Yea` |
| 2 | ¿Deberías atender primero las alertas más nuevas y luego las más antiguas? (Yea/Nay) | `Nay` |

### Task 4: Triaje de la primera alerta

**Explicación:** Te asignas la alerta de primera prioridad y cambias su estado a **In Progress**. El nombre de la alerta seleccionada es la respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Asígnate la alerta de primera prioridad y cambia su estado a In Progress. El nombre de la alerta seleccionada será la respuesta. | `Potential Data Exfiltration` |

### Task 5: Banderas de verificación

**Explicación:** Al triar correctamente cada alerta priorizada, el laboratorio valida y entrega una flag por alerta: la primera (exfiltración de datos relacionada con Zoom/meetings), la segunda (un usuario que cayó en el phishing) y la tercera (uso de GitHub por parte de desarrolladores).

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué flag recibiste tras triar correctamente la alerta de primera prioridad? | `THM{looks_like_lots_of_zoom_meetings}` |
| 2 | ¿Qué flag recibiste tras triar correctamente la alerta de segunda prioridad? | `THM{how_could_this_user_fall_for_it?}` |
| 3 | ¿Qué flag recibiste tras triar correctamente la alerta de tercera prioridad? | `THM{should_we_allow_github_for_devs?}` |

---

**Metodología:** Lectura del dashboard → conteo y orden de alertas → revisión de veredictos previos → aplicación de la política de priorización (severidad media sobre baja; nuevas antes que antiguas) → autoasignación y cambio de estado a In Progress → triaje y validación de cada alerta.
**Learning chain:** entender el dashboard del SOC → interpretar veredictos previos → priorizar correctamente → asignarse y cambiar estado → resolver y verificar cada alerta.
**MITRE ATT&CK:** T1041 (Exfiltration Over C2 Channel), T1048 (Exfiltration Over Alternative Protocol), T1036 (Masquerading - Double Extension), T1078 (Valid Accounts)
**Fuente:** [TryHackMe - SOC L1 Alert Triage](https://tryhackme.com/room/socl1alerttriage)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
