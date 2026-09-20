# Windows Fundamentals 2

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Info | walkthrough | `windowsfundamentals2x0x` | [TryHackMe](https://tryhackme.com/room/windowsfundamentals2x0x) | 00 Level Info | THM | MSConfig, UAC, Computer Management, System Information, Resource Monitor, Command Prompt, Registry Editor | Comprensión de las herramientas administrativas y de configuración de Windows |

---

**Contexto:**
> **ES:** Segunda parte del módulo Windows Fundamentals: System Configuration (MSConfig), configuración de UAC, Computer Management, System Information, Resource Monitor, Command Prompt y Registry Editor para administrar y configurar el sistema.
> **EN:** Second part of the Windows Fundamentals module: System Configuration (MSConfig), UAC settings, Computer Management, System Information, Resource Monitor, Command Prompt and the Registry Editor to manage and configure the system.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:**
1. No answer needed

### Task 2: Configuración del Sistema / System Configuration
**Explicación:**
1. PsShutdown
2. Windows User
3. C:\Windows\System32\control.exe /name Microsoft.Troubleshooting
4. control.exe

### Task 3: Cambiar la Configuración de UAC / Change UAC Settings
**Explicación:**
3. UserAccountControlSettings.exe

### Task 4: Administración de Equipos / Computer Management
**Explicación:**
1. compmgmt.msc
2. 6:15 AM
3. sh4r3dF0Ld3r

### Task 5: Información del Sistema / System Information
**Explicación:**
1. msinfo32.exe
2. THM-WINFUN2
3. %SystemRoot%\system32\cmd.exe

### Task 6: Monitor de Recursos / Resource Monitor
**Explicación:**
6. resmon.exe

### Task 7: Símbolo del Sistema / Command Prompt
**Explicación:**
1. C:\Windows\System32\cmd.exe /k %windir%\system32\ipconfig.exe
2. ipconfig /all

### Task 8: Editor del Registro / Registry Editor
**Explicación:**
8. regedt32.exe

### Task 9: Conclusión / Conclusion
**Explicación:**
9. No answer needed

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Read the above and start the virtual machine. | `No answer needed` |
| 2.1 | What is the name of the service that lists Systems Internals as the manufacturer? | `PsShutdown` |
| 2.2 | Whom is the Windows license registered to? | `Windows User` |
| 2.3 | What is the command for Windows Troubleshooting? | `C:\Windows\System32\control.exe /name Microsoft.Troubleshooting` |
| 2.4 | What command will open the Control Panel? (The answer is the name of .exe, not the full path) | `control.exe` |
| 3 | What is the command to open User Account Control Settings? | `UserAccountControlSettings.exe` |
| 4.1 | What is the command to open Computer Management? | `compmgmt.msc` |
| 4.2 | When is the npcapwatchdog scheduled task set to run at? | `6:15 AM` |
| 4.3 | What is the name of the hidden shared folder? | `sh4r3dF0Ld3r` |
| 5.1 | What is the command to open System Information? | `msinfo32.exe` |
| 5.2 | What is the System Name? | `THM-WINFUN2` |
| 5.3 | What is the value of ComSpec under Environment Variables? | `%SystemRoot%\system32\cmd.exe` |
| 6 | What is the command to open Resource Monitor? | `resmon.exe` |
| 7.1 | In System Configuration, what is the full command for Internet Protocol Configuration? | `C:\Windows\System32\cmd.exe /k %windir%\system32\ipconfig.exe` |
| 7.2 | For the ipconfig command, how do you show detailed information? | `ipconfig /all` |
| 8 | What is the command to open the Registry Editor? (The answer is the name of the .exe file, not the full path) | `regedt32.exe` |
| 9 | Read the above. | `No answer needed` |

---

**Metodología:**
Recorrido por las utilidades administrativas de Windows: análisis de servicios y herramientas en MSConfig, ajuste de UAC, inspección de Computer Management (tareas programadas, recursos compartidos), obtención de datos del sistema con System Information, monitoreo con Resource Monitor e interacción con Command Prompt y el Editor del Registro.

### Cadena de ataque / Attack Chain
1. Exploración de System Configuration (servicios, inicio, herramientas) y del ajuste de UAC.
2. Revisión de Computer Management: tareas programadas y recursos compartidos ocultos.
3. Recopilación de información del sistema y de variables de entorno.
4. Monitoreo de recursos y uso de Command Prompt para configuración de red.
5. Acceso al Editor del Registro para configuraciones avanzadas.

**Learning chain:**
MSConfig -> UAC Settings -> Computer Management -> System Information -> Resource Monitor -> Command Prompt -> Registry Editor

**Lección:** *Windows concentra su administración en una serie de utilidades integradas (MSConfig, Computer Management, Resource Monitor, regedit) que un atacante puede abusar o que un defensor debe conocer para auditar el sistema.*

**MITRE ATT&CK:**
- N/A (Room de aprendizaje / walkthrough — herramientas administrativas de Windows)

**Fuente:** [TryHackMe - Windows Fundamentals 2](https://tryhackme.com/room/windowsfundamentals2x0x)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.