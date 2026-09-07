# Windows Basics [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Free)
* **Slug:** `windowsbasics`
* **Link:** https://tryhackme.com/room/windowsbasics
* **Sección / Section:** 01 Level Easy
* **Fuente / Source:** Redacción oficial de TryHackMe + máquina Windows Server 2019 Datacenter del room
* **Componentes:** Windows Server 2019 Datacenter (1809) · Entorno de escritorio (About your PC, Settings, Task Manager, Windows Security/Defender) · EICAR test file
* **Impacto rol:** Fundamentos de Windows: navegar un sistema Windows moderno, leer especificaciones, inspeccionar tareas/usuarios y ejecutar el flujo de un archivo de prueba de AV (EICAR). Base para toda la línea blue team / forense Windows.

## Solucionario de Tareas / Task Solutions

> **ES:** La máquina del room es una **Windows Server 2019 Datacenter** en su rol de estación de trabajo "TryHatMe". Puntos clave de la exploración: **device name = TryHatMe**, **RAM = 4.00 GB**, **versión = 1809**, y el onboarding de la empresa deja dos flags (`THM{welcome_to_tryhatme!}` y `THM{your_first_day!}`). El **EICAR test file** (`tryhatmemaldoc.txt`) es un archivo de prueba inofensivo reconocido por los antivirus: ejecuta el flujo escanear→ver detalles sin riesgo real. En Task Manager → **Users** puedes ver qué cuenta está logueada (Administrator). Es el laboratorio perfecto para perder el miedo a Windows: saber dónde está cada panel es más del 50% del trabajo forense.
> **EN:** The room's machine is a **Windows Server 2019 Datacenter** acting as the "TryHatMe" workstation. Exploration highlights: **device name = TryHatMe**, **RAM = 4.00 GB**, **version = 1809**, and the company onboarding leaves two flags (`THM{welcome_to_tryhatme!}` and `THM{your_first_day!}`). The **EICAR test file** (`tryhatmemaldoc.txt`) is a harmless test file every AV recognises: you walk the scan→details flow with zero real risk. In Task Manager → **Users** you can see which account is logged in (Administrator). The perfect lab to lose the fear of Windows: knowing where every panel lives is more than half of forensic work.

### Task 1 — Introducción / Introduction *(vm)*

* **Check:** `I understand the learning objectives and am ready to learn about Windows!`
* **ES:** Arranca la máquina Windows en split-screen; módulo Pre Security.
* **EN:** Boots the Windows machine in split-screen; Pre Security module.

### Task 2 — Explorando el Espacio de Trabajo de Windows / Exploring the Windows Workspace

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| After opening **About your PC**, go to Device specifications. What is the **Device name** specified? | `TryHatMe` |
| Continue in Device specifications. How much **RAM** is installed on your new work PC? | `4.00 GB` |
| Scroll to Windows specifications. Which **Version of Windows Server 2019 Datacenter** is installed? | `1809` |
| Explore the **TryHatMe Onboarding** folder on the Desktop. What is the flag in **Welcome.txt**? | `THM{welcome_to_tryhatme!}` |

* **About your PC:** Win+I → System → About (o buscar "About your PC"). Device specifications → Device name `TryHatMe`, Installed RAM `4.00 GB`.
* **Version:** Windows specifications → Version `1809` (build base de Server 2019).
* **Welcome.txt:** en el Desktop → `TryHatMe Onboarding` → `Welcome.txt` = `THM{welcome_to_tryhatme!}`.

### Task 3 — Configurando y Protegiendo Windows / Configuring and Securing Windows

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Use the **TryHatMeWelcome** installer. What is the flag you receive after installing and running the application? | `THM{your_first_day!}` |
| Investigate the **Time & Language** section. Which **country or region** is your computer set to? | `United States` |
| Open the **Task Manager** → **Users** tab. Which **account is currently logged in**? | `Administrator` |
| After your custom scan, click `Virus:DOS/EICAR_Test_File` and select **See details**. What file name is shown in **Affected items**? | `tryhatmemaldoc.txt` |

* **Instalador / Installer:** ejecutar `TryHatMeWelcome.exe` (botón derecho → Run as administrator si pide permisos) e iniciar la app → flag `THM{your_first_day!}`.
* **Región / Region:** Settings → Time & Language → Region → `United States`.
* **Task Manager → Users:** pestaña *Users* → cuenta activa = `Administrator` *(verificar en vivo: el room usó en versiones anteriores una pregunta distinta; se responde con la cuenta visible en la pestaña)*.
* **EICAR:** Windows Security → Protection history → ver el detalle de `Virus:DOS/EICAR_Test_File` → *See details* → archivo afectado = `tryhatmemaldoc.txt`. El archivo EICAR es un string estándar inofensivo usado para validar AV.

### Task 4 — Conclusión / Conclusion

* **Check:** `Complete the room and continue on your cyber learning journey!`
* **ES:** Enlaza con los siguientes rooms (Windows system administration / hardening).
* **EN:** Links to the following rooms (Windows system administration / hardening).

## Metodología / Methodology

1. **Paso / Step:** Abrir *About your PC* y anotar Device name, RAM y Version.
2. **Paso / Step:** Leer `Welcome.txt` del onboarding y ejecutar `TryHatMeWelcome.exe`.
3. **Paso / Step:** Revisar Settings → Time & Language (región) y Task Manager → Users (cuenta activa).
4. **Paso / Step:** Ejecutar un escaneo personalizado que detecte el archivo EICAR y ver sus detalles.

### Cadena de aprendizaje / Learning Chain

```
Windows Server 2019 Datacenter (v1809, TryHatMe, 4.00 GB)
  -> reconocimiento del sistema: About your PC (device name, RAM, version)
  -> onboarding: Welcome.txt (THM{welcome_to_tryhatme!}) + instalador (THM{your_first_day!})
  -> configuración local: región (United States), usuarios (Administrator)
  -> seguridad: EICAR test file (tryhatmemaldoc.txt) en Windows Security
```

**Mapeo MITRE ATT&CK / relacionado:** T1082 (System Information Discovery) — device name, RAM, versión; T1012 (Query Registry) no aplica; el flujo EICAR es el fundamento de validar controles (T1015/AV testing no es técnica atacante). Room de fundamentos Windows.

**Lección:** *En Windows, el panel correcto lo es todo.* Device name, versión, región, cuenta y AV: saber leerlos rápido asiste en triage forense, hardening y soporte.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.