# Memory Acquisition

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|-----------|------|------|------|---------|--------|-------------|---------|
| Easy | walkthrough | `memoryacquisition` | [TryHackMe](https://tryhackme.com/room/memoryacquisition) | 01 Level Easy | THM | Windows, Linux, VM, procdump, gcore, hiderm, LiME, VBoxManage | Adquisición de memoria para análisis forense en múltiples plataformas |

> **Objeto:** Aprender a adquirir imágenes de memoria volátil en sistemas Windows, Linux y máquinas virtuales con las herramientas forenses adecuadas.

---

**Contexto:** Sala de forensia digital centrada en la adquisición de memoria: se abordan los volcados de sistemas Windows (hiberfil.sys, procdump64.exe), procesos Linux (gcore), el módulo del kernel LiME para Linux, los snapshots de VirtualBox (vboxmanage.exe) y las consideraciones de gestión de activos y antiforense asociadas.

> **ES:** Sala sobre adquisición de memoria: hiberfil.sys, procdump, gcore, LiME, snapshots de VirtualBox y antiforense.
> **EN:** Memory acquisition room: hiberfil.sys, procdump, gcore, LiME, VirtualBox snapshots and anti-forensics.

## Solucionario

### Task 1: Introducción / Introduction
**Explicación:** Presentación de la sala y de los fundamentos de la adquisición de memoria volátil.

No answer needed

### Task 2: Bases de la adquisición / Acquisition basics
**Explicación:** Se identifican los archivos y herramientas previos al volcado de memoria en los distintos sistemas operativos.

1. hiberfil.sys
2. gcore

### Task 3: Adquisición en Windows / Windows acquisition
**Explicación:** Se practica el volcado de un proceso en Windows con procdump64.exe y se identifican herramientas relacionadas con el volcado de credenciales.

1. .\procdump64.exe -mt notepad.exe PROCESSNAME_PID_YYMMDD_HHMMSS.dmp
2. mimikatz,procdump64.exe
3. No answer needed

### Task 4: Adquisición en Linux / Linux acquisition
**Explicación:** Se carga el módulo LiME para capturar la memoria de un sistema Linux, tanto por red como escribiendo el volcado con formato y digest.

1. sudo insmod lime-6.8.0-1027-aws.ko "path=tcp:5555 format=raw"
2. sudo insmod lime-6.8.0-1027-aws.ko "path=/tmp/memdump.lime format=lime digest=md5"

### Task 5: Adquisición de máquinas virtuales / Virtual machine acquisition
**Explicación:** Se obtiene el estado de la memoria de una máquina virtual mediante snapshots de VirtualBox.

1. vboxmanage.exe
2. CheckPoint-VM

### Task 6: Gestión y antiforense / Management and anti-forensics
**Explicación:** Se repasa cómo afectan la gestión de activos y las técnicas antiforenses a la toma de imágenes de memoria.

1. Asset Management
2. anti-forensic techniques

### Task 7: Conclusión / Conclusion
**Explicación:** Cierre de la sala y repaso del proceso completo de adquisición.

No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|------|----------|-----------|
| 1 | — | `No answer needed` |
| 2.1 | Archivo de hibernación de Windows | `hiberfil.sys` |
| 2.2 | Herramienta de volcado de procesos en Linux | `gcore` |
| 3.1 | Comando de procdump64.exe | `.\procdump64.exe -mt notepad.exe PROCESSNAME_PID_YYMMDD_HHMMSS.dmp` |
| 3.2 | Herramientas de volcado de credenciales | `mimikatz,procdump64.exe` |
| 3.3 | — | `No answer needed` |
| 4.1 | Volcado LiME por red | `sudo insmod lime-6.8.0-1027-aws.ko "path=tcp:5555 format=raw"` |
| 4.2 | Volcado LiME a archivo con digest | `sudo insmod lime-6.8.0-1027-aws.ko "path=/tmp/memdump.lime format=lime digest=md5"` |
| 5.1 | Herramienta de snapshots de VirtualBox | `vboxmanage.exe` |
| 5.2 | Estado del snapshot | `CheckPoint-VM` |
| 6.1 | Dominio de gestión implicado | `Asset Management` |
| 6.2 | Técnicas que dificultan el análisis | `anti-forensic techniques` |
| 7 | — | `No answer needed` |

---

**Metodología:** Identificación de la plataforma objetivo, selección de la herramienta de adquisición (procdump64.exe en Windows, gcore en Linux, LiME para memoria del kernel, vboxmanage.exe para VMs), ejecución del volcado con el formato y digest adecuados, y valoración de la gestión de activos y las técnicas antiforenses.

### Cadena de ataque / Attack Chain

Sistema objetivo → identificación de la plataforma → herramienta de adquisición (procdump/gcore/LiME/VBoxManage) → volcado de memoria → preservación para el análisis forense.

**Learning chain:** Memoria volátil → adquisición → Windows → Linux → máquinas virtuales → análisis forense

*Lección:* Elegir la herramienta y el orden de volatilidad correctos es esencial para preservar la memoria como evidencia antes de apagar o analizar el sistema.

**MITRE ATT&CK:** T1005 - Data from Local System.

**Fuente:** [TryHackMe - Memory Acquisition](https://tryhackme.com/room/memoryacquisition)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.

**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.

**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).

**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.