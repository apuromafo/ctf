# APT28 Inception Theory

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|--------|--------|-------------|---------|
| Medium | Threat Intelligence | apt28inceptiontheory | https://tryhackme.com/room/apt28inceptiontheory | 02 Level Medium | TryHackMe | APT28, GRU, ATT&CK, Phishing | Mapeo técnico de un APT ruso |

---

**Contexto:** La sala **APT28 Inception Theory** desglosa la anatomía del grupo de espionaje cibernético **APT28 (Fancy Bear/Pawn Storm)**, atribuido a la **GRU (Unidad 26165)** rusa y activo desde **2004**. Se analizan sus campañas reales (TV5Monde, objetivos noruegos, Polonia, la cumbre BRICS, respuesta de la ANSSI), los CVEs que explota (CVE-2022-38028, CVE-2023-23397, CVE-2017-0263), las claves de registro que abusa en Windows, sus TTPs (phishing, Pass-the-Hash, acceso por SMB T1021.002) y la familia de malware complementaria **Zebrocy**. Las respuestas documentan cada técnica y artefacto del grupo.

## Solucionario

### Task 1: Introducción
**Explicación:**

Se plantea el contexto de la amenaza y la metodología empleada para estudiar al grupo.

Respuesta: `No answer needed`

### Task 2: Conceptos de amenaza
**Explicación:**

Se definen los conceptos clave: qué es una **Advanced Persistent Threat**, a qué grupo se atribuye la actividad y el grupo objeto de la sala.

1. `Advanced Persistent Threat`
2. `APT29`
3. `APT28`

### Task 3: Atribución del grupo
**Explicación:**

Se documenta el perfil del amenazante: país de origen, unidad militar de la GRU, año estimado de inicio de actividad y el tipo de operación que lleva a cabo.

1. `Russia`
2. `GRU Unit 26165`
3. `2004`
4. `cyber espionage`

### Task 4: Campañas históricas
**Explicación:**

Se enumeran los objetivos documentados del grupo: la emisora francesa afectada, el sector del ataque y los países/eventos objetivo.

1. `TV5Monde`
2. `Norwegian`
3. `Poland`
4. `BRICS Summit`
5. `ANSSI`

### Task 5: Vulnerabilidades explotadas
**Explicación:**

Se identifican las CVEs asociadas a las operaciones del grupo y el vector de entrada principal.

1. `CVE-2022-38028`
2. `CVE-2023-23397`
3. `Phishing`

### Task 6: Claves de registro abusadas
**Explicación:**

Se documentan las rutas del registro de Windows donde el grupo persiste o recupera comandos.

1. `HKCU\Environment\UserInitMprLogonScript`
2. `HKCU\Software\Microsoft\Office test\Special\Perf`

### Task 7: Explotación adicional
**Explicación:**

Se amplían las vulnerabilidades explotadas por el grupo en otras campañas.

1. `CVE-2017-0263`
2. `CVE-2023-23397`

### Task 8: Movimiento lateral
**Explicación:**

Se documentan las técnicas de movimiento lateral empleadas: el acceso a administración de Windows por SMB y el método de suplantación de credenciales.

1. `T1021.002`
2. `Pass the Hash`

### Task 9: Malware complementario
**Explicación:**

Se identifica la familia de malware derivada que complementa las operaciones del grupo.

Respuesta: `Zebrocy`

### Task 10: Aplicación del intelligence
**Explicación:**

Se consolida cómo aplicar la inteligencia de APT en la detección y en el ajuste de defensas.

Respuesta: `No answer needed`

### Tabla de preguntas y respuestas

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Introducción | `No answer needed` |
| 2.1 | Significado de APT | `Advanced Persistent Threat` |
| 2.2 | Grupo con actividad similar | `APT29` |
| 2.3 | Grupo protagonista de la sala | `APT28` |
| 3.1 | País de origen | `Russia` |
| 3.2 | Unidad militar implicada | `GRU Unit 26165` |
| 3.3 | Año de inicio de actividad | `2004` |
| 3.4 | Tipo de operaciones | `cyber espionage` |
| 4.1 | Emisora afectada | `TV5Monde` |
| 4.2 | Sector objetivo | `Norwegian` |
| 4.3 | País objetivo | `Poland` |
| 4.4 | Evento objetivo | `BRICS Summit` |
| 4.5 | Agencia de respuesta documentada | `ANSSI` |
| 5.1 | CVE explotada 1 | `CVE-2022-38028` |
| 5.2 | CVE explotada 2 | `CVE-2023-23397` |
| 5.3 | Vector de entrada principal | `Phishing` |
| 6.1 | Clave de registro de persistencia | `HKCU\Environment\UserInitMprLogonScript` |
| 6.2 | Clave de registro Office | `HKCU\Software\Microsoft\Office test\Special\Perf` |
| 7.1 | CVE explotada adicional 1 | `CVE-2017-0263` |
| 7.2 | CVE explotada adicional 2 | `CVE-2023-23397` |
| 8.1 | Técnica de movimiento lateral (código) | `T1021.002` |
| 8.2 | Método de autenticación alternativo | `Pass the Hash` |
| 9 | Familia de malware derivada | `Zebrocy` |
| 10 | Aplicación del intelligence | `No answer needed` |

---

**Metodología:** Threat Intelligence estructurada (Diamond Model / Cyber Kill Chain): perfil de adversario, atribución a la GRU, campañas documentadas, CVEs explotadas, hijacking de registro, técnicas ATT&CK de movimiento lateral y malware asociado.

**Learning chain:** Conceptos de APT → atribución → campañas → vulnerabilidades → persistencia en registro → movimiento lateral → malware → aplicar la inteligencia.

**Lección:** *Conocer al adversario por sus TTPs — no solo por sus IOCs — permite detectar al mismo actor cuando cambia de herramienta.*

**MITRE ATT&CK:** T1566 Phishing · T1059.003 Command and Scripting Interpreter (Windows Command Shell) · T1550.002 Use Alternate Authentication Material: Pass the Hash · T1021.002 Remote Services: SMB/Windows Admin Shares · T1547 Boot/Logon Autostart Execution.

**Fuente:** [TryHackMe - APT28 Inception Theory](https://tryhackme.com/room/apt28inceptiontheory)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.