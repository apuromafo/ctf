# Windows Base

| **Dificultad** | Easy |
| **Tipo** | Walkthrough |
| **Slug** | `windowsbase` |
| **Link** | [TryHackMe](https://tryhackme.com/room/windowsbase) |
| **Sección** | 01 Level Easy |
| **Fuente** | Writeup de Sunjid Ahmed Siyem (Medium) |
| **Componentes** | Windows Security / Task Manager / Windows Settings / File Explorer / EICAR test file |
| **Impacto** | Primeros pasos en Windows: interfaz gráfica, Explorador de archivos, configuración del sistema y herramientas básicas de seguridad |

---

**Contexto:** Room para principiantes sobre el sistema operativo Windows. Objetivos: navegar por la interfaz gráfica de Windows, usar el Explorador de archivos, comprobar la configuración del sistema y usar herramientas básicas como el Administrador de tareas y Windows Security.

## Solucionario

### Task 1: Introduction

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | I understand the learning objectives and am ready to learn about Windows! | `No Answer Needed` |

### Task 2: Exploring the Windows Workspace

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | (Preguntas de lectura / reading questions) | `No answer needed` |

### Task 3: Native Windows Security

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Use the `TryHatMeWelcome` installer located within the `TryHatMe Onboarding` folder. What is the flag value you receive after installing and running the application? | `THM{your_first_day!}` |
| 2 | Investigate the **Time & Language** section of the **Windows Settings** app. Which country or region is your computer currently set to? | `United States` |
| 3 | Open the **Task Manager** on your workstation's Desktop and navigate to the **Performance** tab. What is the speed of your computer's CPU? | `2.20 GHz` |
| 4 | After performing your custom scan, click `Virus:DOS/EICAR_Test_File` and select **See details**. What is the file name shown in the **Affected items** section? | `tryhatmemaldoc.txt` |

### Task 4: Conclusion

| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Complete the room and continue on your cyber learning journey! | `No Answer Needed` |

---

**Metodología:**
1. **Explorar el workspace:** antes de Windows, los ordenadores ejecutaban MS-DOS con una pantalla negra donde se escribían comandos; en 1985 Microsoft lanzó **Windows 1.0**, una GUI básica construida sobre DOS. Navegar por la interfaz gráfica moderna y el **Explorador de archivos**.
2. **Windows Security:** es el panel central para gestionar las medidas de protección integradas, dividido en cuatro secciones: **Virus & threat protection** (detecta/elimina malware con protección en tiempo real y escaneos personalizables), **Firewall & network protection** (controla tráfico de red entrante y saliente), **App & browser control** (protege de apps, archivos y sitios inseguros) y **Device security** (protecciones basadas en hardware).
3. **Primera tarea del lab:** instalar y ejecutar el instalador `TryHatMeWelcome` de la carpeta `TryHatMe Onboarding` → flag `THM{your_first_day!}`.
4. **Settings:** investigar la sección **Time & Language** de la app **Windows Settings** → país/región actual = `United States`.
5. **Task Manager:** abrir el **Administrador de tareas** del escritorio y en la pestaña **Performance** leer la velocidad de la CPU → `2.20 GHz`.
6. **Escaneo personalizado:** tras el escaneo, hacer clic en `Virus:DOS/EICAR_Test_File` → **See details**: el nombre de archivo en **Affected items** es `tryhatmemaldoc.txt`.

**Learning chain:** MS-DOS → Windows 1.0 (GUI) → Explorador de archivos → Windows Security (4 secciones) → instalador TryHatMeWelcome → THM{your_first_day!} → Settings (Time & Language → United States) → Task Manager (CPU 2.20 GHz) → scan EICAR → tryhatmemaldoc.txt

**MITRE ATT&CK:** No aplica técnicas ofensivas directas; fundamentos de SO Windows (T1059.003 Command and Scripting Interpreter: Windows Command Shell como base de interacción con el sistema)

**Fuente:** [TryHackMe - Windows Base](https://tryhackme.com/room/windowsbase)