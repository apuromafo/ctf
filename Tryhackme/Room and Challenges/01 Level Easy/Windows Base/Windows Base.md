# Windows Base [EASY]

### Información de la Sala / Room Information

* **Dificultad / Difficulty:** EASY
* **Tipo / Type:** Walkthrough (Premium)
* **Slug:** `windowsbase`
* **Link:** https://tryhackme.com/room/windowsbase
* **Sección / Section:** Windows / Fundamentos
* **Fuente / Source:** Writeup de Sunjid Ahmed Siyem (Medium)

---

## Solucionario de Tareas / Task Solutions

> **ES:** Room para principiantes sobre el sistema operativo Windows. Objetivos: navegar por la interfaz gráfica de Windows, usar el Explorador de archivos, comprobar la configuración del sistema y usar herramientas básicas como el Administrador de tareas y Windows Security.
> **EN:** Beginner room about the Windows operating system. Objectives: navigate the Windows graphical interface, use File Explorer, check system settings and use basic system tools like Task Manager and Windows Security.

---

### Task 1 — Introduction

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| I understand the learning objectives and am ready to learn about Windows! | `No Answer Needed` |

---

### Task 2 — Exploring the Windows Workspace

Antes de Windows, los ordenadores ejecutaban MS-DOS con una pantalla negra donde se escribían comandos. En 1985, Microsoft lanzó Windows 1.0, una interfaz gráfica de usuario (GUI) básica construida sobre DOS.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| (Preguntas de lectura / reading questions) | `No answer needed` |

---

### Task 3 — Native Windows Security

Windows ofrece herramientas de seguridad integradas. La aplicación **Windows Security** es el panel central para gestionar las medidas de protección integradas de Windows, dividido en cuatro secciones:

* **Virus & threat protection:** detecta y elimina software malicioso con protección en tiempo real y escaneos personalizables.
* **Firewall & network protection:** controla el tráfico de red entrante y saliente.
* **App & browser control:** protege a los usuarios de apps, archivos y sitios web potencialmente inseguros.
* **Device security:** proporciona protecciones basadas en hardware.

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Use the `TryHatMeWelcome` installer located within the `TryHatMe Onboarding` folder. What is the flag value you receive after installing and running the application? | `THM{your_first_day!}` |
| Investigate the **Time & Language** section of the **Windows Settings** app. Which country or region is your computer currently set to? | `United States` |
| Open the **Task Manager** on your workstation's Desktop and navigate to the **Performance** tab. What is the speed of your computer's CPU? | `2.20 GHz` |
| After performing your custom scan, click `Virus:DOS/EICAR_Test_File` and select **See details**. What is the file name shown in the **Affected items** section? | `tryhatmemaldoc.txt` |

---

### Task 4 — Conclusion

| Pregunta / Question | Respuesta / Answer |
|----------|--------|
| Complete the room and continue on your cyber learning journey! | `No Answer Needed` |

---

## Metodología / Methodology

1. **Explorar el workspace:** entender la evolución de Windows desde MS-DOS hasta la GUI moderna.
2. **Windows Security:** gestionar la protección integrada (virus, firewall, app/browser control, device security).
3. **Settings:** investigar Time & Language para ver la región del sistema.
4. **Task Manager:** ver el rendimiento del sistema (velocidad de CPU).
5. **Escaneo personalizado:** detectar el archivo de prueba EICAR.

**Lección:** Windows ofrece herramientas de seguridad integradas y habilitadas por defecto que permiten monitorizar y controlar la seguridad del sistema.

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.
