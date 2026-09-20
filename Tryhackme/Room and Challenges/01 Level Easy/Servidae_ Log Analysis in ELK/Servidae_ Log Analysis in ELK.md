# Servidae_ Log Analysis in ELK

| Dificultad | Tipo | Slug | Link | Sección | Fuente | Componentes | Impacto |
|---|---|---|---|---|---|---|---|
| Easy | walkthrough | `servidaeloganalysisinelk` | [TryHackMe](https://tryhackme.com/room/servidaeloganalysisinelk) | `01 Level Easy` | THM | ELK, Elasticsearch, Logstash, log analysis, incident response | Resolución completa del análisis de logs en ELK |

---

**Contexto:** Room de análisis de logs con la pila ELK (Elasticsearch, Logstash, Kibana): se inspeccionan los logs de un endpoint comprometido para reconstruir la cadena del incidente. Se identifica el índice backdoor, la IP 84.237.252.156 en Letonia descargando curl.exe, procesos como explorer.exe y MSI maliciosos, la persistencia vía registro de Windows Installer y los datos exfiltrados (bank-details.csv).

> **ES:** Análisis forense de logs en ELK para reconstruir un compromiso: búsquedas en Elasticsearch, identificación de procesos, persistencia en HKCU Policies y exfiltración de datos.
> **EN:** Forensic log analysis in ELK to rebuild a compromise: Elasticsearch queries, process identification, registry persistence in HKCU Policies and data exfiltration.

## Solucionario

### Task 1: Introducción / Introduction

**Explicación:** Tarea inicial de la room: se comienza el análisis sin necesidad de respuesta.

1. No answer needed

### Task 2: Motor de búsqueda y registro / Search engine and ingestion

**Explicación:** Se identifica Apache Lucene como el motor de búsqueda subyacente de Elasticsearch y Logstash como la herramienta de ingesta de logs.

1. Apache Lucene
2. Logstash

### Task 3: Preparación / Preparation

**Explicación:** Tarea de preparación del entorno de análisis: no requiere respuesta.

3. No answer needed

### Task 4: Puerto de elástica / Elastic port

**Explicación:** Se responde el puerto por defecto en el que escucha Elasticsearch para las búsquedas.

4. 920

### Task 5: Origen del curl / Origin of curl

**Explicación:** En los logs se identifica la IP de origen 84.237.252.156, ubicada en Letonia, que descargó la herramienta curl.exe hacia el endpoint.

1. 84.237.252.156
2. Latvia
3. curl.exe

### Task 6: Proceso lanzador y PID / Launcher process and PID

**Explicación:** Se localiza el proceso que lanzó la actividad maliciosa: el PID 6712 correspondiente a explorer.exe.

1. 6712
2. explorer.exe

### Task 7: Persistencia en el registro / Registry persistence

**Explicación:** Se identifica la clave de persistencia evilparrot.thm y la ruta HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer usada para mantener el acceso.

1. evilparrot.thm
2. HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer

### Task 8: Instalador malicioso / Malicious installer

**Explicación:** El archivo MSI malicioso implicado en la persistencia es adminshell.msi.

8. adminshell.msi

### Task 9: Backdoor y shell / Backdoor and shell

**Explicación:** Se identifica el índice backdoor en ELK y se recupera la flag THM{C4N_y0U_h34r_m3}; el nombre del proceso de la shell es BackdoorShell.

1. backdoor
2. THM{C4N_y0U_h34r_m3}
3. BackdoorShell

### Task 10: Revershell y exfiltración / Reverse shell and exfiltration

**Explicación:** Se recuperan las credenciales usadas (Password123!), la flag THM{1m_1N_Y0ur_P4YR0LL}, el identificador de la sesión (dt5qhq423goknmq269rg1tal1a) y el archivo exfiltrado bank-details.csv.

1. Password123!
2. THM{1m_1N_Y0ur_P4YR0LL}
3. dt5qhq423goknmq269rg1tal1a
4. bank-details.csv

### Task 11: Cierre / Wrap-up

**Explicación:** Conclusión de la room tras completar el análisis: no requiere respuesta.

11. No answer needed

### Tabla unificada de preguntas y respuestas

| Task | Pregunta | Respuesta |
|---|---|---|
| 1.1 | Arranque de la room | `No answer needed` |
| 2.1 | Motor de búsqueda de Elasticsearch | `Apache Lucene` |
| 2.2 | Herramienta de ingesta de logs | `Logstash` |
| 3.1 | Preparación del entorno | `No answer needed` |
| 4.1 | Puerto por defecto de Elasticsearch | `920` |
| 5.1 | IP de origen del curl | `84.237.252.156` |
| 5.2 | País de la IP de origen | `Latvia` |
| 5.3 | Herramienta descargada | `curl.exe` |
| 6.1 | PID del proceso lanzador | `6712` |
| 6.2 | Proceso lanzador | `explorer.exe` |
| 7.1 | Nombre de la persistencia | `evilparrot.thm` |
| 7.2 | Ruta de persistencia en el registro | `HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer` |
| 8.1 | Instalador MSI malicioso | `adminshell.msi` |
| 9.1 | Índice de la backdoor en ELK | `backdoor` |
| 9.2 | Flag de la backdoor | `THM{C4N_y0U_h34r_m3}` |
| 9.3 | Nombre de la shell | `BackdoorShell` |
| 10.1 | Contraseña usada en el acceso | `Password123!` |
| 10.2 | Flag de la revershell | `THM{1m_1N_Y0ur_P4YR0LL}` |
| 10.3 | Identificador de la sesión | `dt5qhq423goknmq269rg1tal1a` |
| 10.4 | Archivo exfiltrado | `bank-details.csv` |
| 11.1 | Cierre de la room | `No answer needed` |

---

**Metodología:** 1) Acceder a Kibana y preparar el índice. 2) Consultar Elasticsearch (puerto 920) filtrando por proceso y origen. 3) Localizar la descarga de curl.exe desde la IP 84.237.252.156 (Letonia). 4) Identificar el PID 6712 (explorer.exe). 5) Encontrar la persistencia en el registro (evilparrot.thm, ruta del Instalador de Windows). 6) Relacionar adminshell.msi con la backdoor. 7) Recuperar las flags y los datos exfiltrados.

### Cadena de ataque / Attack Chain

```text
curl.exe (84.237.252.156, Latvia) -> explorer.exe (PID 6712) -> persistencia evilparrot.thm en HKCU..\Windows\Installer -> adminshell.msi -> backdoor (index backdoor) -> BackdoorShell -> THM{C4N_y0U_h34r_m3} -> credenciales Password123! -> THM{1m_1N_Y0ur_P4YR0LL} -> exfiltración de bank-details.csv
```

**Learning chain:** ELK stack fundamentals (Lucene, Logstash) -> búsquedas en Elasticsearch -> correlación de logs -> persistencia en registro de Windows -> backdoor y exfiltración -> flags

**Lección:** *La pila ELK convierte logs dispersos en una cadena de evidencia: correlacionar procesos, orígenes de red y claves de registro permite reconstruir un compromiso de principio a fin.*

**MITRE ATT&CK:** T1105 (Ingress Tool Transfer), T1547.001 (Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder), T1059.003 (Command and Scripting Interpreter: Windows Command Shell), T1041 (Exfiltration Over C2 Channel), T1219 (Remote Access Software)

**Fuente:** [TryHackMe - Servidae_ Log Analysis in ELK](https://tryhackme.com/room/servidaeloganalysisinelk)

---

## Descargo de Responsabilidad (Disclaimer)

Este contenido se presenta exclusivamente con fines académicos y educativos.

**Sin Afiliación:** Este espacio no posee ninguna alianza, asociación, patrocinio ni vinculación oficial con TryHackMe.
**Veracidad de los Datos:** La información aquí contenida tiene un propósito ilustrativo y formativo. Los datos, políticas, precios o características de los servicios mencionados pueden variar y no son decididos por TryHackMe en este contexto.
**Referencia Oficial:** Para obtener información precisa, oficial y actualizada, se recomienda encarecidamente visitar el sitio web oficial de TryHackMe (https://tryhackme.com).
**Uso Ético:** No fomentamos ni nos responsabilizamos por el uso indebido de esta información fuera de fines educativos o profesionales legítimos.