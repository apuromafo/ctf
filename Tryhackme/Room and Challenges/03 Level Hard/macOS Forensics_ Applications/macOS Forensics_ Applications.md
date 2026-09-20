# macOS Forensics_ Applications

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Hard | Walkthrough | macosforensicsapplications | https://tryhackme.com/room/macosforensicsapplications | 03 Level Hard | TryHackMe (Serie macOS Forensics: The Basics / Applications / Artefacts) | SQLite / PLIST / APOLLO / Notes / mdls / Spotlight / grep / strings / macSilo | Análisis forense de artefactos de aplicaciones macOS (instalaciones, autostart, permisos TCC, contactos, mensajes, productividad, Safari y Apple Pay) sobre una imagen de disco para reconstruir la actividad del usuario. |

---

**Contexto:**
> **ES:** El room plantea una investigación forense de una imagen de macOS en la que se analizan los artefactos dejados por las aplicaciones: el historial de instalaciones de paquetes (pkg), los LaunchAgents de autostart, la base de datos de permisos TCC, los contactos y mensajes (iMessage/FaceTime), las aplicaciones de productividad (Mail, Calendario, Notas, Recordatorios y Microsoft Word), el historial de Safari y la cartera con Apple Pay. Todas las evidencias se extraen de las bases de datos SQLite y plist del perfil de usuario (`/Users/umair-thm`), lo que permite reconstruir la línea temporal de la actividad y responder a cada pregunta forense.
> **EN:** The room presents a forensic investigation of a macOS image analysing the artefacts left by applications: package installation history (pkg), autostart LaunchAgents, the TCC permissions database, contacts and messages (iMessage/FaceTime), productivity applications (Mail, Calendar, Notes, Reminders and Microsoft Word), the Safari history and the Apple Pay wallet. All evidence is extracted from the SQLite and plist databases of the user profile (`/Users/umair-thm`), allowing the reconstruction of the activity timeline to answer each forensic question.

## Solucionario

### Task 1: Introduction
**Explicación:** Tarea introductoria del room; única pregunta informativa sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 2: Package and Install History
**Explicación:** Análisis del historial de instalaciones de paquetes para datar y nombrar la instalación de Microsoft Word.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the date and time when Microsoft Word was installed? | `2025-04-26 06:41:43` |
| 2 | What is the name of the package used to install Microsoft Word? | `Microsoft_Word_Internal.pkg` |

### Task 3: AutoStart Items
**Explicación:** Revisión de los LaunchAgents de autostart para identificar el argumento de lanzamiento del Microsoft Update Agent.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Provide the argument (full path and parameter) with which the Microsoft Update Agent is launched. | `"/Library/Application Support/Microsoft/MAU2.0/Microsoft AutoUpdate.app/Contents/MacOS/Microsoft Update Assistant.app/Contents/MacOS/Microsoft Update Assistant", "--launchByAgent"` |

### Task 4: Permissions (TCC)
**Explicación:** Consulta de la base de datos TCC para identificar la aplicación con acceso completo al disco.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which application has Full Disk Access permission on this system? | `com.apple.Terminal` |

### Task 5: Contacts and Messages
**Explicación:** Extracción de contactos, mensajes y llamadas FaceTime de las bases SQLite de Messages/Contacts.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the email address of the user using this machine? | `thmguy535@gmail.com` |
| 2 | A FaceTime call was placed. Was this call answered? | `N` |
| 3 | What animal is present in the image attached to the message? | `Dog` |
| 4 | What is the date and time when the previous message was read? | `2025-04-26 05:38:23` |

### Task 6: Productivity Applications
**Explicación:** Reconstrucción de la actividad de productividad (Mail, Calendario, Notas, Recordatorios y Microsoft Word) para responder a cada pregunta forense.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the date of the calendar invite the user received? | `2025-04-27 11:00:00` |
| 2 | What is the time zone of the sender of the email invite? (Format: GMT+xx:xx) | `GMT+03:00` |
| 3 | The user received an invite for the Jingle Cruise event. When is this event going to start? | `2025-04-25 16:00:00` |
| 4 | What is the value (password) used to convert the encrypted Notes database? | `Aquickbrownfoxjumpedoverthelazydog` |
| 5 | One of the notes contains an attached image. What animal is present in the image? | `Giraffe` |
| 6 | What is the due date of the pending reminder? | `2025-04-26 21:00:00` |
| 7 | What is the complete path of the last file opened in Microsoft Word? | `/Users/umair-thm/Downloads/Report-final-updated.pdf` |

### Task 7: Browsing History (Safari)
**Explicación:** Volcado del historial de Safari filtrado por `tryhackme` para identificar el room visitado.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | The user seems to be a fan of TryHackMe. What is the complete URL of the TryHackMe room the user visited using Safari? | `https://tryhackme.com/room/macosforensicsartefacts` |

### Task 8: Photos, Wallet and Apple Pay
**Explicación:** Revisión de la base `passes2023` (Apple Pay) consultada con APOLLO para identificar el campo que reemplaza a `payment_transaction_pass_id`.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When querying the passes2023 database with APOLLO, which field replaces `payment_transaction_pass_id`? | `PAYMENT_TRANSACTION.PID` |

### Task 9: Conclusion
**Explicación:** Tarea de conclusión; pregunta informativa sin respuesta requerida.

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

---

**Metodología:**
1. Montar la imagen del disco de macOS y localizar las bases de datos SQLite y plist del usuario `umair-thm` en `/Users/umair-thm/Library`, agrupadas por dominio de aplicación.
2. Consultar el registro de instalaciones (paquetes `.pkg`) para datar y nombrar la instalación de Microsoft Word.
3. Revisar los LaunchAgents y la base de datos TCC (Full Disk Access) para identificar el autostart del Microsoft Update Agent y la aplicación `com.apple.Terminal` con acceso completo al disco.
4. Extraer contactos, mensajes y FaceTime de las bases SQLite de la app Messages/Contacts para responder sobre el correo del usuario, la llamada y las imágenes adjuntas.
5. Analizar Mail/Calendario (invites y zonas horarias), Notas (base cifrada convertida con la contraseña) y Recordatorios (fechas de vencimiento), y el historial de archivos de Word para reconstruir la actividad de productividad.
6. Volcar el historial y los bookmarks de Safari (filtrados por `tryhackme`) y revisar `passes2023.sqlite` (Apple Pay) para identificar el campo de transacciones `PAYMENT_TRANSACTION.PID`.

### Cadena de ataque / Attack Chain
1. Montaje de la imagen y localización de las bases del perfil `umair-thm`.
2. Análisis de instalaciones (pkg) y autostart (LaunchAgents).
3. Revisión de permisos TCC.
4. Extracción de contactos, mensajes y FaceTime.
5. Reconstrucción de la actividad de productividad (Mail/Calendario/Notas/Recordatorios/Word).
6. Análisis de Safari y Apple Pay.

**Learning chain:** `pkg/instalaciones → LaunchAgents → TCC → contactos/mensajes/FaceTime → Mail/Calendario → Notas (protección) → Recordatorios → Word → Safari → Apple Pay`

**Lección:** *Las aplicaciones dejan un rastro forense completo en SQLite y plist: fechas, argumentos, permisos y credenciales se reconstruyen consultando cada base del perfil de usuario.*

**MITRE ATT&CK:** T1005 (Data from Local System), T1555 (Credentials from Password Stores), T1074 (Data Staged), T1204 (User Execution)

**Fuente:** [TryHackMe - macOS Forensics_ Applications](https://tryhackme.com/room/macosforensicsapplications)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.