# Introduction to Windows IR

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `introtowindowsir` | [TryHackMe](https://tryhackme.com/room/introtowindowsir) | 01 Level Easy | TryHackMe | Windows IR, Active Directory, OpenDoor, incident response, DefenseBox, DFIR | Fundamentos de respuestas a incidentes en Windows y preparación del laboratorio DFIR |

---

**Contexto:** Sala introductoria del path de DFIR (Digital Forensics and Incident Response) de TryHackMe. Presenta el papel del analista DFIR en entornos Active Directory, donde reside aproximadamente el 95% de las cuentas de las empresas Fortune 500. La sala recorre el flujo real de una respuesta a incidentes: la llamada introductoria con el cliente (OpenDoor LTD), la organización de un *war room* dedicado teniendo en cuenta la OPSEC (anticipar que el adversario pueda leer los chats corporativos) y la preparación de un laboratorio DFIR con DefenseBox, que incluye el almacenamiento de evidencia y el análisis de grandes volúmenes de logs con un SIEM.

## Solucionario

### Task 1: Welcome to Windows IR / Bienvenido a Windows IR

**Explicación:** Tarea informativa de bienvenida al módulo. Solo hay que marcar la tarea como completada para comenzar el recorrido; no se exige ninguna respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Let's go! | `No answer needed` |

### Task 2: Room Introduction / Introducción a la sala

**Explicación:** Tarea informativa que describe el contenido de la sala: el rol del DFIR en Active Directory, el proceso de comunicación con el cliente durante un incidente y la preparación del laboratorio de análisis. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 3: Meet OpenDoor LTD / Conoce a OpenDoor LTD

**Explicación:** El analista DFIR atiende la llamada introductoria de OpenDoor LTD, la empresa víctima del incidente. Se debe leer con atención el informe del incidente que facilita el cliente para extraer la ubicación del centro de datos afectado, la persona a la que OpenDoor señala como sospechosa, los indicadores de compromiso (IoCs) encontrados en el formato solicitado y el EDR que la empresa supone tener desplegado en su red.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Where is the affected data center located? | `London` |
| 2 | Whom does OpenDoor suspect of starting the attack? | `Ruby Evans` |
| 3 | Did OpenDoor manage to find any indicators of compromise? (Answer Format: Indicator, Host) | `hello.exe, DC-04` |
| 4 | What EDR is deployed across OpenDoor's network? | `BitDefender` |

### Task 4: Organize DFIR Chat / Organiza el chat DFIR

**Explicación:** Antes de empezar el análisis hay que organizar un *war room* seguro usando un chat dedicado fuera de los canales corporativos, aplicando buenas prácticas de OPSEC: el adversario podría estar monitorizando los chats internos de la empresa. Al crear ese canal de comunicación se descubre que el EDR realmente en uso por OpenDoor es Trend Micro, que únicamente 15 hosts están protegidos y se obtiene el código de invitación del chat.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What EDR is really in use by OpenDoor? | `TrendMicro` |
| 2 | How many hosts are actually protected with EDR? | `15` |
| 3 | What chat invitation code do you get? | `56-08-32` |

### Task 5: Prepare DFIR Lab / Prepara el laboratorio DFIR

**Explicación:** El analista debe montar su laboratorio DFIR: lanzar DefenseBox (credenciales de ejemplo `DFIRUser:Secure!`), abrir la Usage Guide para conocer la herramienta recomendada para analizar grandes volúmenes de logs y recuperar la flag que aparece al final de la página web de la guía. Después se inspecciona la carpeta DFIR Tools del escritorio y, dentro de la subcarpeta Artifact Collection, se identifica la primera herramienta de recolección de artefactos listada.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What tool was recommended for analyzing large amounts of logs? | `SIEM` |
| 2 | Launch DefenseBox and open the Usage Guide. What flag do you see at the bottom of the web page? | `THM{happy_investigation!}` |
| 3 | Now open the DFIR Tools folder on the desktop. What's the first tool in the Artifact Collection folder? | `DumpIt` |

### Task 6: What's Next / ¿Qué viene después?

**Explicación:** Tarea final informativa que resume los próximos pasos del path DFIR y consolida la preparación del laboratorio realizada a lo largo de la sala. No requiere respuesta.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

---

**Metodología:** Lectura del informe del incidente para extraer los datos de la víctima (centro de datos, sospechoso, IoCs y supuesto EDR) → creación de un *war room* seguro con OPSEC para confirmar el EDR real (Trend Micro) y el número de hosts protegidos → preparación del laboratorio con DefenseBox: revisión de la guía de uso, captura de la flag de la página y reconocimiento de las herramientas de recolección de artefactos (DumpIt) → preparación del análisis masivo de logs mediante SIEM.

### Cadena de ataque / Attack Chain

```text
Reconocimiento del entorno Active Directory de OpenDoor (DC-04)
    -> Ejecución de hello.exe en el controlador de dominio
    -> Intrusión inicial no detectada por el supuesto EDR (BitDefender)
    -> Solo 15 hosts protegidos con el EDR real (TrendMicro)
    -> Posible lectura de comunicaciones corporativas por parte del adversario
    -> Activación de la respuesta a incidentes (DFIR) con un war room OPSEC
    -> Preparación del laboratorio DFIR (DefenseBox + SIEM + recolección de artefactos)
```

**Learning chain:** AD en el ~95% de Fortune 500 → DFIR como rol en el ciclo de vida del incidente → recopilación de información desde la llamada con el cliente → OPSEC y canales seguros (*war room*) → montaje del laboratorio (DefenseBox) → evidencia, artefactos y SIEM.

**Lección:** *La preparación del laboratorio, la recolección de artefactos y un canal de comunicación seguro (OPSEC) son la base de toda respuesta a incidentes efectiva.*

**MITRE ATT&CK:** T1021.001 (Remote Services: Remote Desktop Protocol) y T1078 (Valid Accounts) como vectores de acceso inicial plausibles en el incidente de OpenDoor, junto a prácticas defensivas de planificación de respuesta a incidentes.

**Fuente:** [TryHackMe - Introduction to Windows IR](https://tryhackme.com/room/introtowindowsir)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos. **Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe. **Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto. **Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com). **Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.