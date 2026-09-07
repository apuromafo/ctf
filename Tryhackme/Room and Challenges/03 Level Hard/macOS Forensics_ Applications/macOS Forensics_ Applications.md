# macOS Forensics: Applications

| **Dificultad** | Hard |
| **Tipo** | Walkthrough |
| **Slug** | `macosforensicsapplications` |
| **Link** | [TryHackMe](https://tryhackme.com/room/macosforensicsapplications) |
| **Sección** | 03 Level Hard |
| **Fuente** | TryHackMe (Serie macOS Forensics: The Basics / Applications / Artefacts) |
| **Componentes** | SQLite / PLIST / APOLLO / Notes / mdls / Spotlight / grep / strings / macSilo |
| **Impacto** | Análisis forense de artefactos de aplicaciones macOS (instalaciones, autostart, permisos TCC, contactos, mensajes, productividad, Safari y Apple Pay) sobre una imagen de disco para reconstruir la actividad del usuario. |

---

**Contexto:** El room plantea una investigación forense de una imagen de macOS en la que se analizan los artefactos dejados por las aplicaciones: el historial de instalaciones de paquetes (pkg), los LaunchAgents de autostart, la base de datos de permisos TCC, los contactos y mensajes (iMessage/FaceTime), las aplicaciones de productividad (Mail, Calendario, Notas, Recordatorios y Microsoft Word), el historial de Safari y la cartera con Apple Pay. Todas las evidencias se extraen de las bases de datos SQLite y plist del perfil de usuario (`/Users/umair-thm`), lo que permite reconstruir la línea temporal de la actividad y responder a cada pregunta forense.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | No answer needed | `No answer needed` |

### Task 2: Package and Install History

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the date and time when Microsoft Word was installed? | `2025-04-26 06:41:43` |
| 2 | What is the name of the package used to install Microsoft Word? | `Microsoft_Word_Internal.pkg` |

### Task 3: AutoStart Items

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Provide the argument (full path and parameter) with which the Microsoft Update Agent is launched. | `"/Library/Application Support/Microsoft/MAU2.0/Microsoft AutoUpdate.app/Contents/MacOS/Microsoft Update Assistant.app/Contents/MacOS/Microsoft Update Assistant", "--launchByAgent"` |

### Task 4: Permissions (TCC)

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Which application has Full Disk Access permission on this system? | `com.apple.Terminal` |

### Task 5: Contacts and Messages

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | What is the email address of the user using this machine? | `thmguy535@gmail.com` |
| 2 | A FaceTime call was placed. Was this call answered? | `N` |
| 3 | What animal is present in the image attached to the message? | `Dog` |
| 4 | What is the date and time when the previous message was read? | `2025-04-26 05:38:23` |

### Task 6: Productivity Applications

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

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | The user seems to be a fan of TryHackMe. What is the complete URL of the TryHackMe room the user visited using Safari? | `https://tryhackme.com/room/macosforensicsartefacts` |

### Task 8: Photos, Wallet and Apple Pay

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | When querying the passes2023 database with APOLLO, which field replaces `payment_transaction_pass_id`? | `PAYMENT_TRANSACTION.PID` |

### Task 9: Conclusion

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

**Learning chain:** `pkg/instalaciones → LaunchAgents → TCC → contactos/mensajes/FaceTime → Mail/Calendario → Notas (protección) → Recordatorios → Word → Safari → Apple Pay`

**MITRE ATT&CK:** T1005 (Data from Local System), T1555 (Credentials from Password Stores), T1074 (Data Staged), T1204 (User Execution)

**Fuente:** [TryHackMe - macOS Forensics: Applications](https://tryhackme.com/room/macosforensicsapplications)