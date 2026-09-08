# Windows Basics

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `windowsbasics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/windowsbasics) |
| **Sección** | 01 Level Easy |
| **Fuente** | Redacción oficial de TryHackMe + máquina Windows Server 2019 Datacenter del room |
| **Componentes** | Windows Server 2019 Datacenter (1809) / Entorno de escritorio (About your PC, Settings, Task Manager, Windows Security/Defender) / EICAR test file |
| **Impacto** | Fundamentos de Windows: navegar un sistema moderno, leer especificaciones, inspeccionar tareas/usuarios y ejecutar el flujo de un archivo de prueba de AV (EICAR) |

---

**Contexto:** La máquina del room es una **Windows Server 2019 Datacenter** en su rol de estación de trabajo "TryHatMe". Puntos clave de la exploración: **device name = TryHatMe**, **RAM = 4.00 GB**, **versión = 1809**, y el onboarding de la empresa deja dos flags (`THM{welcome_to_tryhatme!}` y `THM{your_first_day!}`). El **EICAR test file** (`tryhatmemaldoc.txt`) es un archivo de prueba inofensivo reconocido por los antivirus: ejecuta el flujo escanear→ver detalles sin riesgo real. En Task Manager → **Users** puedes ver qué cuenta está logueada (Administrator).

## Solucionario

### Task 1: Introducción / Introduction *(vm)*

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I understand the learning objectives and am ready to learn about Windows! | `No answer needed` |

**Explicación:** Introducción al room; la máquina del room es una **Windows Server 2019 Datacenter** en su rol de estación de trabajo "TryHatMe". No requiere respuesta.

### Task 2: Explorando el Espacio de Trabajo de Windows / Exploring the Windows Workspace

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | After opening **About your PC**, go to Device specifications. What is the **Device name** specified? | `TryHatMe` |
| 2 | Continue in Device specifications. How much **RAM** is installed on your new work PC? | `4.00 GB` |
| 3 | Scroll to Windows specifications. Which **Version of Windows Server 2019 Datacenter** is installed? | `1809` |
| 4 | Explore the **TryHatMe Onboarding** folder on the Desktop. What is the flag in **Welcome.txt**? | `THM{welcome_to_tryhatme!}` |

**Explicación:** Se abre *About your PC* (Win+I → System → About, o buscando "About your PC"). En Device specifications: **Device name** = `TryHatMe`, **Installed RAM** = `4.00 GB`. En Windows specifications: **Version** = `1809` (build base de Server 2019). En el Desktop, la carpeta `TryHatMe Onboarding` contiene `Welcome.txt` con la first flag `THM{welcome_to_tryhatme!}`.

### Task 3: Configurando y Protegiendo Windows / Configuring and Securing Windows

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Use the **TryHatMeWelcome** installer. What is the flag you receive after installing and running the application? | `THM{your_first_day!}` |
| 2 | Investigate the **Time & Language** section. Which **country or region** is your computer set to? | `United States` |
| 3 | Open the **Task Manager** → **Users** tab. Which **account is currently logged in**? | `Administrator` |
| 4 | After your custom scan, click `Virus:DOS/EICAR_Test_File` and select **See details**. What file name is shown in **Affected items**? | `tryhatmemaldoc.txt` |

**Explicación:** Se ejecuta `TryHatMeWelcome.exe` (botón derecho → Run as administrator si pide permisos) e inicia la app → flag `THM{your_first_day!}`. En Settings → Time & Language → Region → `United States`. En Task Manager → pestaña *Users* → cuenta activa = `Administrator` *(el room usó en versiones anteriores una pregunta distinta; se responde con la cuenta visible en la pestaña)*. En Windows Security → Protection history → detalle de `Virus:DOS/EICAR_Test_File` → *See details* → archivo afectado = `tryhatmemaldoc.txt` (el EICAR es un string estándar inofensivo usado para validar AV).

### Task 4: Conclusión / Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the room and continue on your cyber learning journey! | `No answer needed` |

**Explicación:** Cierre del room; continuar el camino de aprendizaje de Windows.

---

**Metodología:**
1. **Reconocimiento del sistema:** abrir *About your PC* (Win+I → System → About, o buscar "About your PC"). En Device specifications: **Device name** = `TryHatMe`, **Installed RAM** = `4.00 GB`. En Windows specifications: **Version** = `1809` (build base de Server 2019).
2. **Onboarding:** en el Desktop → carpeta `TryHatMe Onboarding` → `Welcome.txt` = `THM{welcome_to_tryhatme!}`; ejecutar `TryHatMeWelcome.exe` (botón derecho → Run as administrator si pide permisos) e iniciar la app → flag `THM{your_first_day!}`.
3. **Configuración local:** Settings → Time & Language → Region → `United States`; Task Manager → pestaña *Users* → cuenta activa = `Administrator` *(el room usó en versiones anteriores una pregunta distinta; se responde con la cuenta visible en la pestaña)*.
4. **Seguridad (EICAR):** Windows Security → Protection history → ver el detalle de `Virus:DOS/EICAR_Test_File` → *See details* → archivo afectado = `tryhatmemaldoc.txt`. El EICAR es un string estándar inofensivo usado para validar AV.

**Learning chain:** Windows Server 2019 Datacenter (v1809, TryHatMe, 4.00 GB) → reconocimiento del sistema: About your PC (device name, RAM, version) → onboarding: Welcome.txt (THM{welcome_to_tryhatme!}) + instalador (THM{your_first_day!}) → configuración local: región (United States), usuarios (Administrator) → seguridad: EICAR test file (tryhatmemaldoc.txt) en Windows Security

**MITRE ATT&CK:** T1082 (System Information Discovery), T1012 (Query Registry), T1027 (Obfuscated Files or Information)

**Fuente:** [TryHackMe - Windows Basics](https://tryhackme.com/room/windowsbasics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
