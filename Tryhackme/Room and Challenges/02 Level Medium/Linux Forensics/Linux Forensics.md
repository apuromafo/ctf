# Linux Forensics
| **Dificultad** | Medium |
| **Tipo** | Walkthrough |
| **Slug** | `linuxforensics` |
| **Link** | [TryHackMe](https://tryhackme.com/room/linuxforensics) |
| **Sección** | 02 Level Medium |
| **Fuente** | Solución de laboratorio (repositorio Apuromafo) |
| **Componentes** | Linux forensics, artefactos del filesystem (/etc/passwd, zona horaria, historial de bash), análisis de procesos (VNC), descubrimiento de puertos, recuperación de credenciales |
| **Impacto** | Aprende sobre los artefactos forenses comunes que se encuentran en el sistema de archivos del sistema operativo Linux: usuarios y UIDs, hora de arranque, hostname, zona horaria, servicios en ejecución (VNC), puertos y comandos/credenciales recuperables del sistema. |
---
**Contexto:** Sala centrada en los artefactos forenses que deja un sistema Linux: cuentas de usuario (`ubuntu,pulse`) y el UID del último usuario creado (`1001`), la hora de arranque del sistema (`01:32`), el hostname (`Linux4n6`) y la zona horaria (`Asia/Karachi`), el servicio de escritorio remoto activo (`Xtigervnc` con ruta `/usr/bin/Xtigervnc`), los puertos detectados (`2000`), el historial de comandos del usuario (`sudo apt-get install apache2` ejecutado en `/home/ubuntu`) y la contraseña recuperada (`tryhackme`). Es una sala orientada al análisis forense defensivo (DFIR).
> **ES:** Aprende sobre los artefactos forenses comunes que se encuentran en el sistema de archivos del sistema operativo Linux.
> **EN:** Learn about the common forensic artifacts found in the file system of Linux Operating System.
## Solucionario
### Task 1 — Introducción
**Explicación:** Tarea introductoria a la investigación forense de sistemas Linux. No requiere ninguna respuesta.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta de la tarea 1 (introducción). | `No answer needed` |
### Task 2 — Preparación del análisis
**Explicación:** Ambientación del escenario y de la evidencia a analizar. No requiere ninguna respuesta.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta de la tarea 2 (introducción). | `No answer needed` |
### Task 3 — Usuarios y arranque del sistema
**Explicación:** Análisis de los artefactos de identidad del sistema: los usuarios presentes en `/etc/passwd` y artefactos equivalentes, el UID del último usuario creado y la hora de arranque (boot time) del sistema.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué usuarios existen en el sistema? | `ubuntu,pulse` |
| 2 | ¿Cuál es el UID del último usuario creado? | `1001` |
| 3 | ¿A qué hora se inició (boot) el sistema? | `01:32` |
### Task 4 — Identificación del sistema y escritorio remoto
**Explicación:** Identificación del host y del sistema de escritorio remoto activo: el hostname de la máquina, la zona horaria configurada, el servicio VNC en ejecución y la ruta completa de su binario. La última pregunta de la tarea no precisa respuesta.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuál es el hostname del sistema? | `Linux4n6` |
| 2 | ¿Cuál es la zona horaria del sistema? | `Asia/Karachi` |
| 3 | ¿Qué servicio VNC está en ejecución? | `Xtigervnc` |
| 4 | ¿Cuál es la ruta del binario VNC? | `/usr/bin/Xtigervnc` |
| 5 | Respuesta adicional de la tarea 4. | `No answer needed` |
### Task 5 — Descubrimiento de puertos
**Explicación:** Enumeración de los puertos del sistema analizado: se determina el número total de puertos detectados/expuestos en la evidencia.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Cuántos puertos se detectan en el sistema? | `2000` |
### Task 6 — Historial de comandos
**Explicación:** Revisión del historial de comandos del usuario: se identifica el comando ejecutado (`sudo apt-get install apache2`) y el directorio de trabajo desde el que se lanzó (`/home/ubuntu`).
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué comando aparece en el historial del usuario? | `sudo apt-get install apache2` |
| 2 | ¿En qué directorio se ejecutó el comando anterior? | `/home/ubuntu` |
### Task 7 — Recuperación de credenciales
**Explicación:** Búsqueda de credenciales en los artefactos forenses del sistema: se localiza la contraseña almacenada en la evidencia.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | ¿Qué contraseña se recupera de los artefactos? | `tryhackme` |
### Task 8 — Cierre
**Explicación:** Tarea final de cierre de la sala. No requiere ninguna respuesta adicional.
| # | Pregunta | Respuesta |
|---|----------|-----------|
| 1 | Respuesta de la tarea 8 (cierre). | `No answer needed` |
---
**Metodología:** Análisis forense de un sistema Linux: identificación de cuentas de usuario y UID del último usuario → hora de arranque → hostname y zona horaria → proceso/servicio VNC y su binario → descubrimiento de puertos → revisión del historial de bash del usuario (comando y directorio de trabajo) → búsqueda y recuperación de credenciales en los artefactos.
### Cadena de ataque / Attack Chain
Recolección de los artefactos del filesystem de una máquina Linux comprometida/analizada: se correlacionan `/etc/passwd` (usuarios `ubuntu,pulse` y UID `1001`), la hora de arranque `01:32`, la identidad del sistema (`Linux4n6`, `Asia/Karachi`), el servicio de escritorio remoto (`Xtigervnc` → `/usr/bin/Xtigervnc`), los `2000` puertos detectados, el historial del usuario ubuntu (`sudo apt-get install apache2` desde `/home/ubuntu`) y la contraseña `tryhackme` hallada en los artefactos. No hay payloads de explotación: es un ejercicio de análisis forense.
**Learning chain:** introducción → usuarios/UID → arranque del sistema → hostname/zona horaria → proceso VNC → puertos → historial de comandos → recuperación de credenciales.
**Lección:** *Inspeccionar los artefactos del filesystem Linux (/etc/passwd, zona horaria, historial de bash, procesos en ejecución) permite reconstruir con precisión qué usuarios, servicios, comandos y credenciales formaron parte de la actividad del sistema.*
**MITRE ATT&CK:** T1059.004 (Unix Shell - comandos del historial de bash), T1046 (Network Service Discovery - escaneo de puertos), T1552.001 (Credentials In Files - contraseña `tryhackme` en los artefactos), T1560.001 (Archive Collected Data - empaquetado de evidencia).
**Fuente:** [TryHackMe - Linux Forensics](https://tryhackme.com/room/linuxforensics)

---

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.