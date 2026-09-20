# Legal Considerations in DFIR

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Walkthrough / DFIR Legal | legalconsiderationsindfir | https://tryhackme.com/room/legalconsiderationsindfir | 02 Level Medium | TryHackMe | DFIR, Logs IIS/Exchange, Notificación de brecha, Cumplimiento | Análisis de un incidente de seguridad con enfoque legal y de cumplimiento |

---

**Contexto:** La sala **Legal Considerations in DFIR** presenta un caso práctico de respuesta a incidentes en una empresa ficticia (*SwiftSpend Finance*). Se analizan logs de IIS del servidor Exchange para identificar accesos remotos no autorizados, uso personal del correo corporativo y el usuario implicado (**Michael Ascot** → `michaelascot`). Finalmente se correlacionan evidencias (agente reportado, hashes de archivos) y se evalúan las obligaciones legales y de notificación de brecha derivadas del incidente.

## Solucionario

### Task 1: Contexto del caso
**Explicación:**

Se describe el escenario del incidente y los requisitos legales del análisis. No requiere respuesta escrita.

Respuesta: `No answer needed`

### Task 2: Datos del incidente
**Explicación:**

Se recopilan los datos identificativos del caso desde los registros: el número de incidente, el correo de la víctima/PII implicada, el empleado afectado, la fuente de evidencia (logs IIS del Exchange) y la fecha/hora exacta del evento relevante.

1. `2024011900041521`
2. `aliceranallo@swiftspend.finance`
3. `Michael Ascot`
4. `Exchange Server IIS logs`
5. `Fri 1/19/2024 7:34 PM`

Respuesta:

1. `2024011900041521`
2. `aliceranallo@swiftspend.finance`
3. `Michael Ascot`
4. `Exchange Server IIS logs`
5. `Fri 1/19/2024 7:34 PM`

### Task 3: Detectando la actividad sospechosa
**Explicación:**

Se clasifican los hallazgos del análisis de logs: política corporativa vulnerada (uso personal del correo), tipo de acceso no autorizado (logins remotos) y se identifica el User-Agent del atacante junto con el nombre de usuario comprometido.

1. `Personal Use of Corporate Email`
2. `Unauthorised Remote Logins`
3. `Mozilla/5.0+(X11;+Linux+x86_64;+rv:109.0)+Gecko/20100101+Firefox/115.0`
4. `michaelascot`

Respuesta:

1. `Personal Use of Corporate Email`
2. `Unauthorised Remote Logins`
3. `Mozilla/5.0+(X11;+Linux+x86_64;+rv:109.0)+Gecko/20100101+Firefox/115.0`
4. `michaelascot`

### Task 4: Correlación de evidencias
**Explicación:**

Se cruzan las evidencias del caso: el agente que reporta el incidente, el hash del archivo malicioso/artefacto y el hash de otra evidencia relacionada (p. ej. metadatos o archivo incriminado).

1. `Stan Simon`
2. `911da019ee3cb99bdcab48f49a2bf9a49e124c68`
3. `84FAD3490157D94031E8CDF3ED96973ADE5599C4`

Respuesta:

1. `Stan Simon`
2. `911da019ee3cb99bdcab48f49a2bf9a49e124c68`
3. `84FAD3490157D94031E8CDF3ED96973ADE5599C4`

### Task 5: Obligaciones legales
**Explicación:**

Se discuten las decisiones de notificación de brecha y gestión legal del incidente. No requiere respuestas escritas.

Respuesta:

1. `No answer needed`
2. `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Task 1: Contexto del caso | `No answer needed` |
| 2 | Task 2: Número de incidente | `2024011900041521` |
| 2 | Task 2: Correo de la víctima | `aliceranallo@swiftspend.finance` |
| 2 | Task 2: Empleado afectado | `Michael Ascot` |
| 2 | Task 2: Fuente de evidencia | `Exchange Server IIS logs` |
| 2 | Task 2: Fecha/hora del evento | `Fri 1/19/2024 7:34 PM` |
| 3 | Task 3: Política vulnerada | `Personal Use of Corporate Email` |
| 3 | Task 3: Tipo de acceso no autorizado | `Unauthorised Remote Logins` |
| 3 | Task 3: User-Agent del atacante | `Mozilla/5.0+(X11;+Linux+x86_64;+rv:109.0)+Gecko/20100101+Firefox/115.0` |
| 3 | Task 3: Usuario comprometido | `michaelascot` |
| 4 | Task 4: Who reported the incident | `Stan Simon` |
| 4 | Task 4: Hash de la evidencia | `911da019ee3cb99bdcab48f49a2bf9a49e124c68` |
| 4 | Task 4: Hash secundario | `84FAD3490157D94031E8CDF3ED96973ADE5599C4` |
| 5 | Task 5: Obligación legal 1 | `No answer needed` |
| 5 | Task 5: Obligación legal 2 | `No answer needed` |

---

**Metodología:** Revisión de la política de privacidad/uso → análisis de logs IIS de Exchange → identificación de accesos y User-Agent -> correlación con hashes de evidencias → evaluación de obligaciones de notificación y cumplimiento legal.

**Learning chain:** Incidente → logs → usuario comprometido → evidencias (hashes) → decisiones legales.

**Lección:** *En DFIR los hallazgos técnicos deben traducirse a implicaciones legales: documentar evidencia, fuente y cronología es lo que permite decidir una notificación de brecha correcta.*

**MITRE ATT&CK:** T1005 Data from Local System · T1078 Valid Accounts · T1083 File and Directory Discovery.

**Fuente:** [TryHackMe - Legal Considerations in DFIR](https://tryhackme.com/room/legalconsiderationsindfir)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.